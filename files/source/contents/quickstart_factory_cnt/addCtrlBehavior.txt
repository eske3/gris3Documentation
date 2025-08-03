コントローラの挙動を追加する
=======================================

今回の例のキャラには顔の表示切り替えを行う必要があります。
その切り替え機能を頭部のコントローラ（head_ctrl_C）に追加してみます。
これからの作業はスクリプトの方で行います。


setup_highを開き、Constructorクラスのsetupメソッドまで移動します。
setupメソッドはリグなどの仕組みを構築するための工程を記述します。
super(Constructor, self).setup()の下に、メソッドの実行を行うための
新たな一行を追加します。


.. code-block:: python

    def setup(self):
        r'''
            @brief  コントローラのセットアップを行う。
            @return None
        '''
        super(Constructor, self).setup()
        self.setupHead() #追加した１行

その後、Constructorクラスの何処かに追加したメソッドの内容を記述してみましょう。


.. code-block:: python

    def setupHead(self):
            head_ctrl = node.asObject('head_ctrl_C')
            plug = head_ctrl.addEnumAttr(
                'faceType', ['normal', 'broken'], default=0
            )
            nml_cndt = node.createUtil('condition', n='faceNormalDisp_cdt')
            nml_cndt('colorIfTrueR', 1)
            nml_cndt('colorIfFalseR', 0)
            plug >> nml_cndt.attr('firstTerm')
            nml_cndt.attr('outColorR') >> 'faceMaskGeo_grp.v'
            plug >> 'faceMaskBreakGeo_grp.v'


このようにリグに関する追加、修正は基本的にsetupメソッド内に記述します。
また、パーツごとにメソッドを分けておくと後で流用、メンテナンスの時に便利です。

