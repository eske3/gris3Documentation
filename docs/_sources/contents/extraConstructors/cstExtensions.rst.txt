cstExtensions
*****************************
コンストラクタに追加・拡張機能を提供するExtraConstructorです。

funcモジュールと違い、
こちらはコンストラクタの仕様に則ったルール内で使用できる機能を提供します。

このExtraConstructorをインストールしてもコンストラクタ自体の挙動に変化はなく、
コンストラクタで以下のメソッドが使用できるようになります。


alignJointOnSurface
======================================
このメソッドは任意のNurbsSurfaceにジョイントチェーンを追従させる機能を提供します。
またジョイントチェーンにはFKコントローラが追加され、
サーフェースに追従した状態からオフセットでFK制御が可能になります。
メソッドの引数は以下の通りです。

.. list-table:: 引数の説明

    *   -   **引数名**
        -   **型**
        -   **説明**
    *   -   joints
        -   list
        -   サーフェースに追従するジョイントの名前のリストを指定します。
        
            このリストにはジョイントチェーンのトップノードの名前のリストを入れます。
            
            各ジョイントチェーンの末端までサーフェースに追従するようになります。
    *   -   surfaceName
        -   str
        -   ジョイントを追従させるためのNurbsサーフェース名を指定します。
    *   -   ctrlRoot
        -   gris3.node.Transform
        -   ジョイントチェーンをFK制御するためのコントローラを格納するためのルートノードを指定します。
    *   -   setupRoot
        -   gris3.node.Transform
        -   ジョイントがサーフェースに追従するための仕組みを格納するためのグループノードを指定します。
    *   -   basename
        -   str
        -   animSet等、各必要ノードのベースとなる名前を指定します。
    *   -   blendAttrName
        -   str
        -   各FKコントローラがサーフェースに追従するかどうかのブレンド率を設定するためのアトリビュート名を指定します。
    *   -   globalBlendAttr
        -   str
        -   全FKコントローラがサーフェースに追従するかどうかのブレンド率を設定するためのアトリビュート名を指定します。
        
            こちらはノード名.アトリビュート名という形で一つのコントローラのアトリビュートを指定します。
    *   -   sc
        -   gris3.tools.curvePrimitives.PrimitiveCreator
        -   各FKコントローラに使用するコントローラーのシェイプを定義するオブジェクトを指定します。
    *   -   scModifier
        -   dict
        -   各FKコントローラを作成する際に、L/R/Cなど位置に応じた設定を変更するための辞書を指定します。

使用例
==================

.. code-block:: python

    # 予めこのExtraConstructorはインストールされているものとする。
    from gris3 import constructors, func, node
    mainModule = constructors.mainModule(__name__, True)

    class Constructor(mainModule.Constructor):
        def setupCollar(self):
            base_name = 'collar'
            parent_jnt = 'spineC_jnt_C'
            setup_root = self.createSetupRoot(
                base_name, parentJoint=parent_jnt, isFollow=True
            )
            ctrl_root = self.createCtrlRoot(base_name, parentJoint=parent_jnt)

            sc = self.shapeCreator()
            sc.setCurveType('pin')
            sc.setTranslation()
            sc.setSize(1)

            for joint in [
                'collarA_jnt_L', 'collarB_jnt_L', 'collarA_jnt_R', 'collarB_jnt_R', 
            ]:
                ctrls = self.alignJointOnSurface(
                    joint, 'collarBase_srfShape', ctrl_root, setup_root,
                    base_name, 'followCollarToBody',
                    'spineHip_ctrl_C.followCollarToBody',
                    sc
                )