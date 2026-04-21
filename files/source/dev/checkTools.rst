****************************************************
checkToolsの拡張
****************************************************
checkToolsは各チェックカテゴリがモジュール形式になっているため、
拡張で独自のチェック機構を追加することができます。




AbstractCheckerとAbstractCategoryOption
================================================
checkToolsのカテゴリモジュールは大別すると2つの機構で構成さています。

１つは実際にシーン中のノードのチェックを行う

**AbstractCheckerクラス**

によるチェック機構。

もう１つはAbstractCheckerを用いてチェックを行い、その結果を表示するためのGUI
機能を構成する

**AbstractCategoryOptionクラス**

になります。



.. _DEVCT-AbstractChecker:

AbstractChecker
================================================
このクラスはシーン中の特定のオブジェクトをチェックし、
その結果をGUIへ渡すための機構を備えた基底クラスです。

仕組み
------------------------
checkToolsのカテゴリモジュールでは
:ref:`DEVCT-AbstractCategoryOption`
で定義した設定に基づいて、AbstractCheckerのcheckメソッドを呼び出し、
その結果エラーや警告があった場合は、AbstractCategoryOptionに紐づけられている
結果表示ビューワにその結果内容を表示します。

.. blockdiag::

    blockdiag{
        span_width = 128;
        span_height = 96;

        A[label='AbstractCategoryOption'];
        B[label='AbstractChecker', shape=diamond];
        C[label='ResuleViewer', shape=flowchart.terminator];
        
        A -> B [label='execCheck'];
        A -> C [label='define'];
        B -> C [label='buildUI'];
    }


このクラスのいくつか重要なメソッドを紹介します。

メソッド
+++++++++++++++++++++++++++++++++++++

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   setCategory
        -   category : str
        -   
        -   チェッカーの種類を設定します。
        
            チェッカーの目的を表す任意の名前を設定して下さい。
    +   -   check
        -   
        -   list
        -   対象となるノードに対してチェックを行うための具体的な
            手続きを記述します。
            
            チェックの結果エラーや警告などがある場合、
            エラー内容とエラーレベルを格納する特殊オブジェクト
            
            :ref:`DEVCT-CheckedResult`
            
            にその内容を格納し、リスト化して返します。
            
checkメソッド
+++++++++++++++++++++++++++++++++++++
checkToolsのカテゴリモジュールを新たに開発する場合、
基本的にはこのメソッドを上書きし、チェック結果に応じた戻り値を返します。

ただし

:ref:`DEVCT-AbstractAssetChecker`

内で紹介したサブクラスを用いる場合は、checkメソッド自体はそれぞれのサブクラス
が専用の機構がすでに記述されているため、別のメソッドを上書きして
運用することになります。

それぞれのサブクラスでどのメソッドを上書きするかは各種リンクからご確認下さい。




.. _DEVCT-AbstractAssetChecker:

AbstractAssetChecker(AbstractChecker)
================================================

各種チェッカーの基底クラスです。

:ref:`DEVCT-AbstractChecker`
よりも各種ノードのチェックを行うための拡張が行われています。

AbstractAssetCheckerにはサブクラスとして以下のものがあります。

* :ref:`DEVCT-REBasedNameChecker`
* :ref:`DEVCT-AbstractDagChecker`
* :ref:`DEVCT-REBasedDagNameChecker`
* :ref:`DEVCT-GroupMemberChecker`
* :ref:`DEVCT-DataBasedHierarchyChecker`



概要
------------------------

具体的にはcheckメソッド内で
**setTrargets**
した各対象に対し
**checkObject**
メソッドでエラーがないかのチェックを行い、その結果を返す仕組みとなっています。

:ref:`DEVCT-AbstractChecker`

はチェック機構すべてを記述する必要があるのに対し、本クラスでは各対象オブジェクトに対するチェックを
記述するだけのシンプルな構造になっているため、開発者はチェックルーチンのみの実装に専念することができるようになっています。


メソッド
+++++++++++++++++++++++++++++++++++++

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   checkObject
        -   targetObject : node.AbstractNode
        -   list(CheckResult)
        -   引数targetObjectに対し、チェックを行います。
        
            問題がなければ空のリストを返しますが、問題がある場合はその内容をCheckResultオブジェクトに
            記述し（複数可）リストとして返します。




.. _DEVCT-REBasedNameChecker:

REBasedNameChecker(AbstractAssetChecker)
================================================
名前ベースのチェッカーの基底クラスです。

メンバー変数NamePatternに適合するかどうかで判断を行います。
NamePatternには任意のコンパイル済み正規表現オブジェクトを格納する必要があります。

デフォルトではNamePatternには

**.***

が入っています。



.. _DEVCT-AbstractDagChecker:

AbstractDagChecker(AbstractAssetChecker)
================================================
dagを対象とするチェッカーの基底クラスです。
設定されたターゲットに対して、一番下の階層まで再帰的にチェックを行います。



.. _DEVCT-REBasedDagNameChecker:

REBasedDagNameChecker(AbstractDagChecker)
================================================
名前ベースのdagを対象とするチェッカーの基底クラスでAbstractDagCheckerのサブクラスです。
メンバー変数NamePatternに適合するかどうかで判断を行います。
NamePatternには任意のコンパイル済み正規表現オブジェクトを格納します。
また、名前がシーン中に重複しているかどうかもチェックします。




.. _DEVCT-GroupMemberChecker:

GroupMemberChecker(REBasedDagNameChecker)
================================================
階層ベースで一番下階層までチェックを行います。
setTargetで指定したグループの下階層のオブジェクトが対象となります。
（setTargetしたオブジェクトは走査対象にはならない点に注意して下さい。）




.. _DEVCT-DataBasedHierarchyChecker:

DataBasedHierarchyChecker(AbstractAssetChecker)
================================================
データ（dict型など）に基づいて階層チェックを行う機能を提供するクラスです。


概要
------------------------

AbstractAssetCheckerクラスでは任意のノードに対して操作するのに対し、このクラスでは
**setTargets**
メソッドに辞書オブジェクトを渡し、辞書の内容と照らし合わせてシーン内のノードのチェックを行います。


階層定義辞書オブジェクト
------------------------
**setTargets**に渡す辞書オブジェクトは以下の仕様に基づいて階層を定義する必要があります。

.. list-table::

    +   -   **キー**
        -   **値**
        -   **説明**
    +   -   ノード名
        -   オプション(dict)
        -   値に渡す辞書は以下の内容になります。

            .. list-table::

                +   -   **キー**
                    -   **値**
                    -   **説明**
                +   -   priority
                    -   int
                    -   ノードの優先度を指定します。チェックする際に優先度が設定された場合、
                        指定優先度よりもこの数値が大きい場合はチェック対象外となります。
                +   -   children
                    -   dict
                    -   子となるノードを指定します。キーは本dictオブジェクトと同じになります。


オプション辞書のキー
**children**
には上記の辞書と同じ構造のものを渡します。（入れ子構造）

詳細については下記のサンプルを参照して下さい。


.. code-block:: python
    :linenos:

    'root' : {
        'children' : {
            'childA1' : {
                'priority' : 1,
                'children' : {
                    'childA2':{
                        'priority' : 1,
                        'children' : {
                            'childA3' : {}
                        }
                    }
                }
            },
            'childB' : {
                'priority' : 5
            }
        }
    }



メソッドと辞書オブジェクト
------------------------

メソッド
+++++++++++++++++++++++++++++++++++++

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   setPriorityLevel
        -   level : int
        -   
        -   ノードを検出する際にフィルタとなるpriorityを設定します。
            
            このpriorityよりも上回る数値を設定されたノードは走査しなくなります。

    +   -   getHir（static)
        -   targets : list
            
            priorityFilter(None) : function
        -   dict
        -   階層データを書き出すための便利関数です。
        
            引数targetsにはgris3.node.TransformかJointを渡す必要があります。
            
            引数priorityFilterには、走査中のオブジェクトのpriorityをいくつに
            設定するかのフィルタ用関数を設定します。


getHir(static)
++++++++++++++++++++++++++++++++
このメソッドはsetTargetsに渡すための辞書オブジェクトを生成するための便利メソッドになります。

任意の階層定義辞書オブジェクトを作成する場合、シーン内にあらかじめ必要な階層構造を作成しておき、
その階層のトップ階層をこのメソッドに渡せば必要な階層定義辞書オブジェクトを生成して返します。

.. code-block:: python
    :linenos:

    from gris3.tools import checkUtil
    from gris3 import node
    
    # root以下の階層構造を調べ、辞書オブジェクト化する。
    checkUtil.DataBasedHierarchyChecker.getHir(
        [node.asObject('root')]
    )



.. _DEVCT-AbstractCategoryOption:

AbstractCategoryOption
=======================================


.. _DEVCT-CheckedResult:

CheckedResult
=================================
