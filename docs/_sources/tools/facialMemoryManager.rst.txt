****************************************************
facialMemoryManager
****************************************************
このモジュールはブレンドシェイプの登録されたアトリビュートの組み合わせの状態を登録し、
再現、管理するための機能を提供するモジュールです。
モジュール名の通り、主に表情管理を行うための機能となります。


関数
===========================

listManagerNode
-------------------------------------
シーン内の表情マネージャノードをリストします。
戻り値は
:REF:`TFMM-FacialMemoryManagerRoot`
を持つリストです。


createManagerNode
-------------------------------------
フェイシャル情報を保持するノードを作成します。
戻り値は
:REF:`TFMM-FacialMemoryManagerRoot`
を持つリストです。

.. list-table::

    +   -   **引数**
        -   **型**
        -   **説明**
    +   -   parent
        -   str
        -   この関数で作成するFacialMemoryManagerRootノードの親ノードの名前


.. _TFMM-FacialMemoryManagerRoot:

FacialMemoryManagerRoot
===========================
登録した表情を管理します。

メソッド
----------------------

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   setBlendShapeName
        -   blendShapeName : str
        -   
        -   操作対象となるブレンドシェイプ名を設定する。
    +   -   blendShapeName
        - 
        -   str
        -   設定されている操作対象となるブレンドシェイプ名を返す。
    +   -   blendShape
        -   
        -   node.BlendShape
        -   設定されている操作対象ブレンドシェイプをオブジェクト形式で返す。
    +   -   listExpressions
        -   
        -   OrderedDict
        -   このノードが保持する表情データノートのリストを返す。

            戻り値はOrderedDictで、表情名をキーとし、それに対応するTransformを値とする。
    +   -   listExpressionData
        -   
        -   dict
        -   このノードが保持する表情データノードのリストを返す。

            戻り値は辞書型で、表情名をキーとし、それに対応するblendShapeの
            アトリビュート名と値の辞書を値としたデータ。

    +   -   addExpression
        -   expressionName : str
        -   
        -   現在のblendShapeのアトリビュート値を用いて、
            引数expressionで指定した表情データとして登録する。
    +   -   setExpressionFromCurrentState
        -   expression : str
        -   
        -   現在のblendShapeのアトリビュート値を用いて、
            引数expressionで指定した表情データとして登録する。
    +   -   clearExpressions
        -   
        -   
        -   保持する表情データノードをすべて破棄する。
    +   -   removeExpression
        -   expression : str
        -   
        -   引数expressionで指定した表情データを削除する。
    +   -   setExpressionFromDataList
        -   datalist : dict
        -   
        -   引数datalistで指定した辞書データを元に、表情と対応値を一括設定する。

            datalistは

            　キー：表情名

            　値：表情に対応するblendShapeのアトリビュート名と値の辞書

            を持つ。
    +   -   updateExpressionFromDataList
        -   expressionlist : list
        -   int
        -   引数expressionlistで指定された表情名のリストで更新を行う。

            expressionlist内に既存の表情があった場合、その値は保持する。

            既存の表情リストとexpressionlistが順番も含めて全く同じだった場合は
            何もせずに0を返す。

            それ以外の場合は1を返す。
    +   -   renameExpressionFromDataList
        -   expressionlist : list
        -   int
        -   引数expressionlistで指定された表情名のリストで更新を行う。

            expressionlist内に既存の表情があった場合、その値は保持する。

            既存の表情リストとexpressionlistが順番も含めて全く同じだった場合は
            何もせずに0を返す。

            それ以外の場合は1を返す。
    +   -   applyExpression
        -   expression : str
        -   
        -   引数expressionで指定した表情パラメータをblendShapeに適用する。

