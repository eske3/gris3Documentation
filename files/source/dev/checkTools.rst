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

AbstractCheckerにはさらにサブクラスとして以下のものがあります。

* :ref:`DEVCT-REBasedNameChecker`
* :ref:`DEVCT-AbstractDagChecker`
* :ref:`DEVCT-REBasedDagNameChecker`
* :ref:`DEVCT-GroupMemberChecker`
* :ref:`DEVCT-DataBasedHierarchyChecker`



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

:ref:`DEVCT-AbstractChecker`

内で紹介したサブクラスを用いる場合は、checkメソッド自体はそれぞれのサブクラス
が専用の機構がすでに記述されているため、別のメソッドを上書きして
運用することになります。

それぞれのサブクラスでどのメソッドを上書きするかは各種リンクからご確認下さい。


.. _DEVCT-REBasedNameChecker:

REBasedNameChecker
================================================
名前ベースのチェッカーの基底クラスです。
メンバー変数NamePatternに適合するかどうかで判断を行います。
NamePatternには任意のコンパイル済み正規表現オブジェクトを格納する必要があります。



.. _DEVCT-AbstractDagChecker:

AbstractDagChecker
================================================
dagを対象とするチェッカーの基底クラスです。
設定されたターゲットに対して、一番下の階層まで再帰的にチェックを行います。



.. _DEVCT-REBasedDagNameChecker:

REBasedDagNameChecker
================================================
名前ベースのdagを対象とするチェッカーの基底クラスでAbstractDagCheckerのサブクラスです。
メンバー変数NamePatternに適合するかどうかで判断を行います。
NamePatternには任意のコンパイル済み正規表現オブジェクトを格納します。
また、名前がシーン中に重複しているかどうかもチェックします。



.. _DEVCT-GroupMemberChecker:

GroupMemberChecker
================================================
階層ベースで一番下階層までチェックを行います。
setTargetで指定したグループの下階層のオブジェクトが対象となります。
（setTargetしたオブジェクトは走査対象にはならない点に注意して下さい。）


.. _DEVCT-DataBasedHierarchyChecker:

DataBasedHierarchyChecker
================================================
データ（dict型など）に基づいてチェックを行う機能を提供するクラスです。



.. _DEVCT-AbstractCategoryOption:

AbstractCategoryOption
=======================================


.. _DEVCT-CheckedResult:

CheckedResult
=================================
