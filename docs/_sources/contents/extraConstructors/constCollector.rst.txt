constCollector
*****************************
ctrl_grp内に存在する、
コントローラーをまとめるグループ内にあるコンストレインをすべてrig_grp内に収集します。

インストール後の戻り値である、
このExtraConstructorのインスタンスに対して以下のような設定を行うことができます。

.. list-table:: 設定できる機能一覧

    *   -   **メソッド名/変数名**
        -   **引数の型**
        -   **説明**
    *   -   addNodeFilter
        -   *function
        -   判別用のフィルタ関数を追加します。
    *   -   removeNodeFilter
        -   *function
        -   判別用のフィルタ関数を削除します。
    *   -   useDefault
        -   bool
        -   デフォルトのフォルタ（コンストレインだけを取得）を
            使用するかどうかを指定します。
    *   -   ConstGroupName(メンバ変数)
        -   str
        -   コンストレインを格納するグループ名を指定します。
            
            デフォルトではctrlCst_grpという名前のグループに格納されます。
            
            これはメンバ変数なので、直接=で任意の名前を代入して下さい。


addNodeFilter
=============================
このメソッドはグループ内にあるノードを収集する際にフィルタとなる関数を追加することができます。
デフォルトではコンストレインノードをすべて収集するようになっていますが、
他にも収集するものを追加場合にはこのメソッドを使用して独自のフィルタを追加して下さい。

このメソッドにわたす引数は関数です。
関数は以下のフォーマットで定義して下さい。


.. code-block:: python
    
    def functionName(node_name):
        return True

第一引数はフィルタするためのノード名を受け取るようにします。
また戻り値はフィルタの結果の可否をBoolとして返します。

フィルタは複数追加することができます。
このコンストラクタは追加したフィルタすべてでノードのテストを行い、
一つでもTrueになれば収集対象となるようになっています。


useDefault
==========================
このメソッドはデフォルトで動作するフィルタ機能をOFFにします。
デフォルトで動作するフィルタは、
グループ内のすべてのコンストレインノードを適用対象とするようになっています。

デフォルトフィルタは以下の内容になっています。

.. code-block:: python

    from maya import cmds
    def defaultFilter(target):
        return bool(cmds.ls(target, type='constraint'))

コンストレインすべてを収集対象としたくない場合はこのメソッドでTrueを設定し、
独自の収集関数を追加して下さい。



使用例
===================

.. code-block:: python

    class Constructor(constructors.currentConstructor()):
        def ignoreAimConstraint(self, node_name):
            r"""
                エイムコンストレインだけを収集の対象から外すフィルタ。
            """
            if (
                cmds.ls(node_name, type='constraint') and
                not cmds.ls(node_name, type='aimConstraint')
            ):
                return True
            else:
                return False

        def init(self):
            ext_cst = self.installExtraConstructor('constCollector')
            ext_cst.addNodeFilter(self.ignoreAimConstraint)
            ext_cst.useDefault(False)