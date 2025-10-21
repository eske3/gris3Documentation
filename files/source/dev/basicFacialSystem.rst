****************************************************
標準付属のフェイシャルシステム
****************************************************
このセクションではGRIS標準で付属するフェイシャルシステム

**basicFacialSystem**

モジュールについて説明します。


このモジュールは
**ExtraConstructor**
です。

.. seealso::

    ExtraConstructorについては
    :ref:`EXCST-ExtraConstructor`
    をご確認下さい。


.. caution::

    このバージョンは現在開発中のため、今後仕様が大幅に変更される可能性があります。
    使用の際にはその点を十分に留意して下さい。



.. _BFS-LayerModule:

layerモジュール
============================================
このモジュールはフェイシャル機能をレイヤー化するための機能を提供します。
layerモジュールには以下の重要な機能が含まれます。

- :ref:`BFS-layerOperatorClass`
- :ref:`BFS-layerManagerClass`

レイヤー化についての仕様は

  #. 大元の顔ジオメトリのグループ（以後face_grp）をレイヤー毎にコピー
  #. 各レイヤー用の顔メッシュのoutMeshとinMeshをそれぞれ接続する
  #. コピーした顔のメッシュに対し、各レイヤーで任意のリグを構築

となります。
3番については、
接続する順番はlayerManagerにlayerOperatorを設定する順序に準じます。

**Phase 1**

大元の顔ジオメトリのグループ（face_grp)を、
任意のプレフィックを付けた状態でコピーし、各LayerOperatorに渡します。

.. blockdiag::

    blockdiag{
        default_shape = roundedbox

        FACE[label = 'face_grp', shape='ellipse', color = '#90B0D0'];
        A[label = 'Jaw Opened Face'];
        B[label = 'Blend Shape Face'];
        C[label = 'Tweaked Face'];
        SKINNED[label = 'Skinned Face'];

        FACE -> A, B, C, SKINNED[label='copy'];
    }
    
**Phase 2**

コピーされた各メッシュのinMesh、outMeshを接続します。
（接続する順番はlayerManagerにlayerOperatorを設定する順序に準じます。）

.. blockdiag::

    blockdiag{
        default_shape = ellipse
        default_node_color = '#90B0D0'

        A[label = 'Jaw Opened Face'];
        B[label = 'Blend Shape Face'];
        C[label = 'Tweaked Face'];
        SKINNED[label = 'Skinned Face'];

        A -> B -> C -> SKINNED[label='in out'];
    }
    
    
**Phase 3**

各LayerOperatorではsetupやpostProcessメソッド内でコピーされたノードに編集を加え、
リグの構築を行います。

.. blockdiag::

    blockdiag{
        default_shape = diamond

        B[label = 'Blend Shape Face', shape='roundedbox'];
        M[label = 'Copied face_grp', shape='ellipse', color = '#90B0D0'];
        PS[label = 'Pre Setup', color = "#F0D080"];
        S[label = 'Setup', color = "#F0D080"];
        PP[label = 'PostProcess', color = "#F0D080"];

        B -> PS, S, PP;
        PS, S, PP -> M;
    }

.. _BFS-layerOperatorClass:

layerOperator
-----------------------------
このクラスはフェイシャルの機能をレイヤー化する際に、
各レイヤー単独の機能を実装するための基底クラスとなります。

各レイヤーはこのクラスを継承し、
各種メソッドをオーバーライドして動作を実装してきます。

現在、標準以下のlayerOperatorが用意されています。

- BlendShape
- JawOpenner
- Tweaked



.. _BFS-layerManagerClass:

layerManager
-----------------------------

:ref:`BFS-layerOperatorClass`
を管理する機能を提供します。
この機能を経由してbasicFacialSystemにlayerOperatorを登録することにより、
ビルド時に登録されたフェイシャルのリグが構築されます。

layerManagerにはbasicFacialSystemをインストールした戻り値（以後BFSオブジェクト）の
**layerManager**
メソッドからアクセスすることができます。

layerManager.addLayersメソッドを用いてlayerOperatorを追加することができます。
BFSオブジェクトのdefaultLayerOperatorsメソッドを呼ぶと、
標準で推奨されるlayerOperatorを取得できるので、まずはこれを追加してみると良いでしょう。

.. code-block:: python
    :linenos:

    from gris3 import constructors

    class Constructor(constructors.currentConstructor()):
        def init(self):
            cst = self.installExtraConstructor('basicFacialSystem')
            cst.layerManager().addLayers(*cst.defaultLayerOperators())


標準搭載のlayerOperatorを一覧、追加する
++++++++++++++++++++++++++++++++++++++++++

標準搭載されているlayerOperatorを一覧するには
layerOperatorsパッケージのlistAllLayerOperators
を使用します。

.. code-block:: python
    :linenos:

    from gris3.extraConstructor.basicFacialSystem import layerOperators
    lo = layerOperators.listAllLayerOperators()
    
listAllLayerOperatorsの戻り値は辞書であり、
- レイヤー名をキー
- 対応するクラスを値
として保持しています。
アクセスるには使用したいレイヤー名をキーとして渡します。

.. code-block:: python
    :linenos:

    from gris3 import constructors
    from gris3.extraConstructor.basicFacialSystem import layerOperators

    class Constructor(constructors.currentConstructor()):
        def init(self):
            cst = self.installExtraConstructor('basicFacialSystem')
            lo = layerOperators.listAllLayerOperators()
            cst.layerManager().addLayers(lo['BlendShape']) # BlendShapeレイヤを追加


追加されたLayerOperatorを初期化時に調整する
++++++++++++++++++++++++++++++++++++++++++++++++++++++
本ExtraConstructorがインストールされると、ビルド時に様々な処理が行われます。
その中で最初の処理として「大元の顔ジオメトリグループのコピー」が行われます。

（
:ref:`BFS-LayerModule`
Phase1に該当）

Phase１ではlayerManagerの
**setup**
が呼ばれますが、その中では

  1. 大元の顔ジオメトリのグループをコピー
  2. 追加されたlayerOperatorのインスタンスを作成
  3. インスタンスにコピーされた顔ジオメトリグループを渡す
  4. コピーされた顔ジオメトリグループに対し、一つ前のレイヤーのコピーされた
     顔ジオメトリグループを接続する

という処理が行われます。

この中で「２」の処理で初めてLayerOperatorのインスタンスが作成されます。
このインスタンス化されたLayerOperator（以下Layerオブジェクト）に対し、初期化処理
を行いたい場合があります。（クラスのメンバ変数の変更など）

その場合は、インストール先のコンストラクタ内で

**initFacialLayerOperator(self, operator:basicFacialSystem.layer.LayerOperator):**

メソッドを追加すると、Layerオブジェクトの初期化処理をカスタマイズすることができます。

下記の例ではtweakedLayerOperatorに対し、StackFaceName変数の内容を変更しています。

.. code-block:: python
    :linenos:

    from gris3 import constructors
    class Constructor(constructors.currentConstructor()):
        def init(self):
            cst = self.installExtraConstructor('basicFacialSystem')
            cst.layerManager().addLayers(*cst.defaultLayerOperators())

        def initFacialLayerOperator(self, operator):
            if operator.prefix() == 'tweek':
                # tweakLayerOperatorのメンバ変数を変更。
                operator.StackFaceName = {
                    'face':'head_geo', 'faceParts':['facialBrowJnt_grp']
                }


このように、layerOperator開発時ににメンバ変数を設けておくと、
後から操作対象やオペレーションのスイッチなどをアセット毎に行えるようになるため
非常に汎用性があがるためお勧めです。
