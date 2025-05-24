fkCtrlHelper
*****************************
FKコントローラの作成を補助する機能を提供するExtraConstructorです。
親子付けやFKコントローラの作成などの一連の流れ作業を簡単なコマンドで行います。


使用方法
======================================
このExtraConstructorをインストールすると、メインのConstructorに

**setJointAsFkController**

メソッドが追加されます。
ユーザーはこのメソッドを使用して任意のジョイントの親子付と
FKコントローラの作成を行うことができます。

.. list-table:: 引数の説明

    *   -   **引数名**
        -   **型**
        -   **説明**
    *   -   joints
        -   str or list
        -   FKコントローラにするジョイント名のリストを指定します。
            渡す値はジョイント名のリストまたは単体の名前になります。
    *   -   parent
        -   str
        -   FKコントローラにするジョイントの親ジョイント名を指定します。
    *   -   setName
        -   str
        -   作成されるFKコントローラが帰属するAnimSet名を指定します。
    *   -   side=None
        -   str
        -   FKコントローラの位置を表す文字（'L'や'R'、'None'など）
    *   -   shapeCreator=None
        -   gris3.tools.curvePrimitives.PrimitiveCreator
        -   作成されるFKコントローラの形状を指定します。
    *   -   ctrlArgs=None
        -   dict
        -   内部で呼ばれるtoControllerメソッドに渡すオプションを辞書形式で指定します。
    *   -   connectArgs=None
        -   dict
        -   内部で呼ばれるconnectControllerメソッドに渡すオプションを辞書形式で指定します。
    *   -   expandChildren=False
        -   bool
        -   このオプションをTrueにすると、第一引数jointsに渡したノードの子が操作対象になります。
            目的のジョイントをグループ分けしている場合などに便利です。


使用例
==================

.. code-block:: python

    # __init__.py
    from gris3 import constructors, func, node
    cmds = func.cmds
    
    LOD_LIST = ['high', 'low']

    class Constructor(constructors.currentConstructor()):
        def init(self):
            self.installExtraConstructor('fkCtrlHelper')

        def createController(self):
            # FKコントローラの親ジョイント名
            parent_joint = 'spineA_jnt_C'
            
            # コントローラ形状の設定。
            sc = self.shapeCreator()
            sc.setCurveType('circleArrow')
            sc.setRotation((180.0, 0.0, 90.0))
            sc.setSize(8.0)
            
            # コントローラの作成オプション。
            opt = {'option':self.ChainCtrl|self.IgnoreEndCtrl}

            self.setJointAsFkController(
                'skirtJoint_grp', parent_joint, 'skirt',
                shapeCreator=sc, ctrlArgs=opt, connectArgs=opt,
                expandChildren=True
            )
