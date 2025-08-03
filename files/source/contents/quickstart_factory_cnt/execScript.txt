スクリプトを実行する
=======================================
GRISのFactoryではスクリプトを使用してリギングを行います。
リギングに必要な要素を書き出し、スクリプト内で書き出した要素を
組み立てるための記述を行い、それを実行してリグを作成します。


モデルとジョイントが用意できたので一度スクリプトを実行してみましょう。
スクリプトの管理・実行はFactoryのScriptタブで行います。

.. image:: ../img/quickStart_factory/026.png
    :width: 400

スクリプトは基本的にPythonで記述されており、
このリストにあるファイルもすべてPythonファイルになっています。


各種ファイルは以下のような構成になっています。

.. list-table:: 
    :widths: 20 80

    * - __init__
      - パッケージの初期化用スクリプト。
      
        highやlowなどのLODに関わらず必ず使用されます。
    * - setup_high
      - ハイモデル用のスクリプト。
      
        実行する場合はこのスクリプトを使用します。

スクリプトは基本的にPythonで記述されており、
このリストにあるファイルもすべてPythonファイルになっています。


試しに実行してみる
-------------------------
ひとまず説明は置いておいて実行してみます。
setup_highを選択してからExecuteボタンを押します。

.. image:: ../img/quickStart_factory/027.png
    :width: 400

成功すると先程書き出したモデルやジョイントが読み込まれてリグが作成されます。
今回は人型のプリセットを使用したので人型のリグも作成されています。
ただしモデルとの紐づけ作業は行っていないので、world系コントローラ以外は
モデルが動きません。


.. _parentJoint:

スクリプトを編集して親子付けを行う
--------------------------------------------------

作った骨にモデルがついてくるようにするにはスクリプトを書き換える必要があります。


今回のプロジェクトでは主に親子付けがメインなので、どのグループやメッシュが
どのジョイントの子になるのかの紐づけを記述します。


Setup_highをテキストエディタで開きます。

.. note::
    Pythonファイルが何らかのエディタに紐づけされている場合はFactoryの
    Scriptタブの一覧からsetup_highをダブルクリックすると開きます。


    もしエディタを紐づけしていない場合はOpenDirectoryボタンをクリックして
    Explorerを開いたり、リストからエディタにドラッグ＆ドロップして下さい。
    
    .. image:: ../img/quickStart_factory/028.png
        :width: 400


setup_highはハイモデルリギング用のスクリプトを記述するファイルです。
__init__の方はハイ・ロウ両方に必要な内容を記述します。
親子付けはハイモデルにしか行わないので今回はsetup_highの方に記述していきます。
Setup_highをテキストエディタで開くと予めある程度のコードが記述されていることがわかります。

その中で親子付けについては変数ParentListに記述する事で実現します。
変数ParentListは辞書型になっており、辞書のキーには親となるジョイント名、辞書の値にはジョイントの子にしたいジオメトリ名（またはグループ名）をリストにして記述します。
例えば今回の例では頭部のジョイント（head_jnt_C）に頭パーツ（headGeo_grp）を親子付けしたい場合はParentListに以下のように記述します。

.. code-block:: python

    ParentList = {
        'head_jnt_C':['headGeo_grp']
    }

また、手や足のように左右わかれている場合はParentListLRに記述すると良いでしょう。
こちらに記述する場合は_L/_Rを抜いた名前を記述していきます。

.. code-block:: python

    ParentListLR = {
        'clavicle_jnt' : ['clavicleGeo_grp'],
        'uparm_jnt' : ['uparmGeo_grp'],
        'lowarm_jnt' : ['elbowGeo_grp', 'lowarmGeo_grp'],

        'thigh_jnt' : ['thighGeo_grp'],
        'lowleg_jnt' : ['kneeGeo_grp', 'lowlegGeo_grp'],
        'foot_jnt' : ['footGeo_grp'],
    }


ここではテストで親子付けしています。
後ほどの工程で親子付けするジョイントを増やすので、今は何点かテストしてみて
動作を確認できたら一旦終了します。



特殊なジョイントをスクリプトで追加する
--------------------------------------------------

肘や膝の関節用に特殊なジョイントを追加してみます。


このジョイントは前腕（または膝）の回転の半分の回転を行うジョイントです。
以後このジョイントのことをHalfRotaterと呼びます。


HalfRotaterはスクリプトによって作成します。
setup_highのConstructorクラスのpreSetupForLODメソッド内に
コメントアウトされた箇所があります。

.. code-block:: python

    # バインドジョイントを作成する。
    # self.createBindJoint('hip_jnt_C')

この下に以下の記述を追記します。


.. code-block:: python

    # バインドジョイントを作成する。
    # self.createBindJoint('hip_jnt_C')
    for s in func.SuffixIter():
        self.createHalfRotater('lowarm_jnt'*s)
        self.createHalfRotater('lowleg_jnt'*s)

func.SuffixIter()は[L,R]のリストを拡張したイテレータです。
今回は詳細は省略しますが

.. code-block:: python

    for s in 'LR':
        self.createHalfRotater('lowarm_jnt'+'_'+s)
        self.createHalfRotater('lowleg_jnt'+'_'+s)

の代わりの記述だと思っておいて下さい。


この状態でスクリプトを実行するとlowarmとlowlegのそれぞれの同階層に
HalfRotaterが作成されます。

.. image:: ../img/quickStart_factory/029.png
    :width: 400
    


メソッド・関数を調べる
----------------------------------------------
今回のHalfRotaterはConstructorクラスに実装されたメソッドです。
またイテレータとして呼び出したSuffixIterはfuncモジュールに入っています。
基本的にGRISのFactoryでリグを組む際にはこれらConstructorクラスのメソッドと
funcモジュールの関数を多用します。


これらについてのHelpはFactoryのScriptタブの下部にある「Constructor Commands」
「func Commands」を参照して下さい。

.. image:: ../img/quickStart_factory/030.png
    :width: 400