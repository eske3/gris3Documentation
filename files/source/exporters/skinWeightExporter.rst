****************************************************
skinWeightExporter
****************************************************
このモジュールはskinClusterのウェイトを独自フォーマットでのmelによる
書き出し、読み込み機能を提供します。


仕様
===========================

Exporterクラス
-----------------

このモジュールの
:ref:`ESWE-ExporterClass`
クラスによって任意のSkinClusterのウェイトを
melファイルとして書き出します。

書き出されたMelファイルには以下の情報が含まれますが、この情報自体はコメントアウト
されているため、Melファイルを直接読み込んでも反映されません。

    - ウェイト書き出し元のシェイプ名(str)
    - ウェイト書き出し元のskinCluster名(str)
    - スキニングのメソッドの種類(int)
    - インフルエンスの上限の有無(bool)
    - インフルエンスの上限数(int)
    - インフルエンス数(int)
    - ウェイト処理方法(int)
    - ウェイト書き出し元にバインドしていたインフルエンスの登録順序(list)

.. admonition::
    参考

    以下、書き出されたmelファイルの参考例となります。

    .. code-block::
        :linenos:

        // skinWeightExporter 1.0.0
        // Aother               : eske
        // Creation Date        : 2020/03/29 08:39:20
        // -----------------------------------------------------------------------------
        // Skinned Shape        : prpLandingGearRootTubeC_crv_RShape
        // Skin Cluster         : skinCluster75
        // Skinning Method      : 0
        // Maintain Max Inf     : False
        // Max Influences       : 2
        // Number of Influences : 3
        // Weight Distribution  : 1
        // Influence order      : {"prpLandingGear_bndJnt_R", "static_bndJnt", "prpLandingGearTube_bndJnt_R"}
        {
            string $shape = "prpLandingGearRootTubeC_crv_RShape";
            string $skinCluster = findRelatedSkinCluster($shape);
            string $attr[] = `listAttr -m -sn -st "w" ($skinCluster + ".wl")`;
            for ($a in $attr){
                setAttr ($skinCluster + "." + $a) 0;
            }

            setAttr ($skinCluster + ".weightList[0].weights[1]") 1.0;
            ...
        }

書き出されたMelファイルを読み込むと、Mel内で指定されているオブジェクトがすでに
バインドされている場合にそのオブジェクトのウェイトをファイルの情報で上書きします。

インフルエンス数やバインドする順番などがファイルと違う場合は正しく反映されません。


Restorerクラス
-------------------------
Exporterクラスと対になるのが
:ref:`ESWE-RestorerClass`
クラスになります。

このクラスではExporterクラスで書き出されたMelファイルを受け取り、
任意のシェイプに対してバインド、ウェイトの設定を行なうことができます。

また、インフルエンスの名前に対して書き出したMelファイルの情報を修飾してから
バインドすることも可能です。


このように、ExporterとRestorerがセットとなって運用することが前提の仕様となっています。




.. _ESWE-ExporterClass:

Exporter
===========================
このクラスは任意のシェイプに適用されているSkinClusterのウェイトを、
任意のパスに書き出す機能を提供します。

**メソッド**
----------------------

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   setShape
        -   node : str
        -   
        -   ウェイトを書き出すシェイプ名を設定します。
    +   -   shape
        -   
        -   str
        -   setShapeで設定された、ウェイトを書き出すシェイプ名を返します。
    +   -   setExportPath
        -   path : str
        -   
        -   ウェイトファイルの書き出し先のファイル名をフルパスで指定します。
    +   -   export
        -   
        -   
        -   設定に基づいてウェイトを任意のパスへ書き出します。
    +   -   setIsRemapIndex
        -   state : int
        -   
        -   インデックス番号のリマップ処理を行うかどうかセットします。
            デフォルトはTrueですが、動作不良の温床になるため原則Trueのままが
            望ましいです。


使用例
----------------------

.. code-block:: python
    :linenos:

    from gris3.exporter import skinWeightExporter

    exp = skinWeightExporter.Exporter()
    exp.setShape('skinned_mesh')    #バインド済みのメッシュの名前
    exp.setExportPath('temp/test_weight.mel') #書き出し先のファイルパス
    exp.export()

.. caution::
    サンプルコードを実行する前に、あらかじめMayaのシーン中にskinned_meshという名前の
    バインド済みオブジェクトを用意しておく必要があります。
    
    また、書き出し先のディレクトリはあらかじめ作成しておく必要があります。


.. _ESWE-RestorerClass:

Restorer
===========================
このクラスはExporterによって書き出されたファイルを、任意のシェイプに任意の設定で
バインド・ウェイトの復元を行なう機能を提供します。

メソッド
----------------------

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   __init__
        -   filepath : str
        -   
        -   初期化を行なう。引数filepathには読み込み元のウェイトファイルの
            パスを指定できる。
    +   -   setFile
        -   path : str
        -   
        -   再設定するウェイトファイルをフルパスで指定します。
    +   -   setShape
        -   node : str
        -   
        -   ターゲットとなるシェイプをセットします。
    +   -   shape
        -   
        -   str
        -   ターゲットとなるシェイプを返します。
    +   -   setSkinClusterName
        -   name : str
        -   
        -   復元する時につけるskinClusterの名前を設定します。
    +   -   setInfluenceReplacer
        -   function : function
        -   
        -   インフルエンスを置き換えるための関数を設定します。
        
            この関数はインフルエンス名のリストを受け取り、置換後のリストを
            返す関数である必要があります。


使用例
----------------------

.. code-block:: python
    :linenos:

    from gris3.exporter import skinWeightExporter

    rst = skinWeightExporter.Restorer('temp/test_weight.mel') #書き出し先のファイルパス
    rst.setShape(face_name) #バインド前のメッシュの名前
    rst.restore()



.. hint::
    setInfluenceReplacerを使用すると、ウェイト書き出し時に使用したインフルエンス
    ジョイント名に変更を加えた状態でウェイトを適用することができます。
    例えば、書き出す時はインフルエンスジョイント名が
    
    root_jnt_C
    
    だったのに対し、ウェイトを再設定する時は
    
    root_bndJnt_C
    
    のように命名規則が変わっていた場合、以下のような関数を設定するとうまく
    適用できるでしょう。
    
    .. code-block:: python
        :linenos:

        from gris3.exporter import skinWeightExporter
        
        def jnt_to_bindjoint(jointlist):
            return [x.replace('jnt', 'bndJnt') for x in jointlist]

        rst = skinWeightExporter.Restorer('temp/test_weight.mel') #書き出し先のファイルパス
        rst.setShape(face_name) #バインド前のメッシュの名前
        rst.setInfluenceReplacer(jnt_to_bindjoint)
        rst.restore()




.. _ESWE-BasicTemporaryWeightClass:

BasicTemporaryWeight
===========================
一時的にウェイトを書き出し、復元する機能を提供するクラス。

saveメソッドでウェイトをテンポラリ領域に保存する。

restoreメソッドでテンポラリファイルを用いて任意のノードにバインド、
ウェイト適用を行う。



.. _ESWE-TemporaryWeightClass:

TemporaryWeight
===========================
一時的にウェイトを書き出し、復元する機能を提供するクラス。

BasicTemporaryWeightとの違いは、このクラスではSaveメソッド実行時に選択ノード
一つに対して処理を行うため、一時的な使用が簡単な作りになっている。


