****************************************************
jointEditor
****************************************************
このモジュールはジョイント制御を行うのに便利な関数等を提供するPythonモジュールです。


.. _TJE-OrientationModifier:

OrientationModifier
===========================
ジョイントの軸を制御するための機能を提供するクラスです。

使用例
----------------------

.. code-block:: python
    :linenos:

    from gris3 import node
    from gris3.tools import jointEditor
    # ジョイントを作成。
    j = node.createNode('joint', n='main_jnt')
    j.setPosition((0, 10, 0))
    ej = node.createNode('joint', n='mainEnd_jnt', p=j)
    ej.setPosition((0, 8, 1.5))

    om = jointEditor.OrientationModifier()
    # Z軸をY軸に向ける設定を行う。
    om.setSecondaryAxis('+Z')
    om.setTargetUpAxis('+Y')
    om.setSecondaryMode('vector')
    om.execute(j)


パラメータ
----------------------

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   setApplyToChildren
        -   bool
        - 
        -   子供にも影響を与えるかどうかを指定する
    +   -   setApplyToChildren
        - 
        -   bool
        -   子供にも影響を与えるかどうかを指定する
    +   -   setSecondaryAxis
        -   str
        - 
        -   セカンダリ軸をどの軸にするかを指定する。
    +   -   setTargetUpAxis
        -   str
        - 
        -   セカンダリ軸をどの軸に向けるかを指定する。
    +   -   setSecondaryMode
        -   str
        - 
        -   セカンダリ軸を向ける際のモードを設定する。
            使用できる文字列は以下の通り。
            
            'origin', 'vector', 'node', 'surface'
