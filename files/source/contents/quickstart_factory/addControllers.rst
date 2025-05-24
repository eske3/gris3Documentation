コントローラを追加する
===============================

今まではGRISの基本機能を使用してコントローラを作成してきましたが、
これからカスタムのコントローラを追加してみます。


今回はバックパックにコントローラを追加していきます。

ジョイントを作成する
-------------------------

まずは動かすためのジョイントを作成します。
ジョイントを作成するにはモデルもアタリとして必要なので、
新規シーンにした後にFactoryの機能リストからModelsを選び、
ブラウザからモデルをインポートしてきます。

.. image:: ../img/quickStart_factory/037.png
    :width: 400

続いてバックパックの位置に合わせてジョイントを配置していきます。

.. image:: ../img/quickStart_factory/038.png
    :width: 400

続いてこのジョイントだけを一度JointBuilderで書き出します。
今回は名前をbackpackJointsとして書き出しました。

.. image:: ../img/quickStart_factory/039.png
    :width: 400


スクリプトで親子付けを行う
-------------------------------

書き出したジョイントはワールド階層に置いているのでどこにも
親子付けされていません。
このバックパックのジョイントを、スクリプトを使用して背骨のジョイント
（spineC_jnt_C）の子にします。


setup_highのpreSetupForLOD内に記述します。

.. code-block:: python

    def preSetupForLOD(self):
        r'''
            @brief  setupメソッド前に実行される事前準備用のメソッド。
            @return None
        '''
        # バインドジョイントを作成する。
        # self.createBindJoint('hip_jnt_C')
        cmds.parent('backpackRoot_trs_C', 'spineC_jnt_C')    # ←親子付け

        for s in func.SuffixIter():
            self.createHalfRotater('lowarm_jnt'*s)
            self.createHalfRotater('lowleg_jnt'*s)

        # ExtraJointを読み込む。
        self.loadExtraJoints()

通常ジョイントの親子付けなどはpreSetupForLODのself.loadExtraJoints()
よりも前に記述する事が望ましいです。


スクリプトでコントローラを作成する
------------------------------------

コントローラの挙動を追加するで追加したように、
コントローラの追加記述をsetupメソッド内に追加します。
（前回作成したsetupHeadの下の行に追加）

.. code-block:: python

    def setup(self):
        self.setupHead()
        self.setupBackpack()

今回も別のメソッドを作成（setupBackpack）し、それをsetupメソッド内で
呼び出しています。


コントローラ化を行う
-----------------------
今回追加したメソッド「setupBackpack」を追記していきます。
今回のコントローラは追加したジョイントをFKで動かすようにします。
この仕様のコントローラは比較的簡単にスクリプト化する事ができます。
まずは先程作成したジョイントに対応するコントローラノードを作成します。
以下のコマンドをsetupBackpackメソッド内に記述します。

.. code-block:: python

    def setupBackpack(self):
        self.toController(
            'backpackRoot_trs_C', 'backpack',
            option=self.ChainCtrl|self.IgnoreEndCtrl
        )

このtoControllerと言うメソッドは、第１引数のジョイントに対応する任意の
命名規則に従ったコントローラノードを作成します。


このノードはこの段階ではただのTransformノードであり何の効力も持ちません。


話が少しそれますが、GRISで作成したコントローラは必ずAnimSetと呼ばれるセットに
登録する必要があります。
このtoControllerメソッドを使用すると上記のコントローラは第２引数で指定した
animSetに登録された状態で作成されます。
第２引数のanimSet名は、存在しなければ自動で作成してセットに登録、
存在すれば既存のセットに登録されます。

.. image:: ../img/quickStart_factory/040.png
    :width: 400
    
toControllerを通すとセットから漏れる心配がありませんので、基本的には

    ジョイント作成　→　toControllerで対応コントローラ作成

の流れを踏襲する事をオススメします。
（もちろん全てがこれで対応できるわけではありません）


また、最後の引数option=self.ChainCtrlは選択したジョイントの最下層まで対応する
コントローラを作成する指示をしています。
また|でつないだself.IgnoreEndCtrlは末端のジョイントに対応するコントローラは
作成しないと言う指示になっています。



コントローラのルートを作成する
----------------------------------------------
続いてコントローラ化を行うで作成したコントローラを格納するルートノードを
作成します。
今回のバックパックはspineC_jnt_Cの子として使用するので、このジョイントの
代理親ノードを作成し、そのノード内にコントローラを追加していきます。


代理親ノードを作成するには以下のコマンドを追加します。

.. code-block:: python

    ctrl_root = self.createCtrlRoot('backpack', parentJoint='spineC_jnt_C')

するとコントローラ格納階層にspineC_jnt_Cの代理親ノードである
「backpack_parentProxy」が作成されます。


.. image:: ../img/quickStart_factory/041.png
    :width: 400
    

FKコントローラとしてジョイントと紐づけを行う
-----------------------------------------------------------
これでFKコントローラを作成するためのノードが揃いました。
後はこれらをジョイントに紐づけするだけになります。


紐づけするにはconnectControllerメソッドを使用します。
最終的なsetupBackpackメソッドは以下のようになります。

.. code-block:: python

    def setupBackpack(self):
        self.toController(
            'backpackRoot_trs_C', 'backpack',
            option=self.ChainCtrl|self.IgnoreEndCtrl
        )
        ctrl_root = self.createCtrlRoot(
            'backpack', parentJoint='spineC_jnt_C'
        )
        sc = self.shapeCreator()
        sc.setCurveType('sphere')
        sc.setColorIndex((0.8, 0.1, 0.3))
        sc.setSize(20)
        self.connectController(
            'backpackRoot_trs_C', ctrl_root, sc,
            option=self.ChainCtrl|self.IgnoreEndCtrl
        )

connectControllerは第１引数に与えられたジョイントに対応する任意の名前の
コントローラとなるノードを探し、第２引数ctrl_rootの子に配置します。
そして第１引数のジョイントとの接続処理を行います。


ShapeCreator
---------------
connectControllerの第３引数に渡しているscとはShapeCreatorクラスの
インスタンスです。
ShapeCteatorクラスは任意のノードにアタッチするカーブの形状を定義するもので、
このインスタンスにカーブの形状や色、大きさなどを設定して
connectControllerに渡すと、コントローラに任意のカーブシェイプを
追加してくれます。

.. image:: ../img/quickStart_factory/042.png
    :width: 400

これでコントローラがジョイントと接続され、ビューポート上で選択できるようにカーブシェイプが追加されました。


後は今回追加したジョイントとジオメトリの親子付けを行えばこのセッションは終了です。
親子付けの方法については
:ref:`parentJoint`
を行うをご覧下さい。

また、コマンドで作成したコントローラのシェイプでは選択が難しそうな場合
:ref:`modifyController`
の手順に従い形状修正を行って下さい。

.. image:: ../img/quickStart_factory/043.png
    :width: 400


今回はバックパックのコントローラの形状修正を行ったあと、
CtrlExporterに「backpack」として書き出しました。
（パーツごとに分けておくと後で他のキャラに流用するときに便利です）
