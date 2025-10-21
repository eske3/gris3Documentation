****************************************************
エクストラコンストラクタ
****************************************************
エクストラコンストラクタはコンストラクタを拡張するためのプラグインのような働きをする仕組みです。
リグのビルド用スクリプトのコンストラクタ内でインストールする事によって効果を発揮します。

開発者はエクストラコンストラクタを用意する事により、
本体のコンストラクタを変更せずに機能を拡張することができます。
これによりプロジェクトや特定のアセットに特化したフローを制作し、
機構の再利用性を高めることができます。


.. _EXCST-ExtraConstructor:

ExtraConstructor
============================================
このクラスはコンストラクタを拡張するための機構を提供するクラスです。
開発者はこのクラスを継承したサブクラスに独自の機構を記述します。

ユーザーは使用する際に、
このExtraConstructorをインストールすることによって効果を発揮するようになります。

.. code-block:: python

    class Constructor(constructors.currentConstructor()):
        def init(self):
            self.installExtraConstructor('cstExtensions')


仕様
----------------------
ExtraConstructorはConstructorクラスが定義するConstructionOrder
によって実行されるメソッドの前後に任意の処理を追加するようになっています。
任意のメソッドの前に処理を追加したい場合、ExtraConstrutorに

**_任意のメソッド名**

| という形でメソッドを追加します。
| 任意のメソッドの後に処理を追加する場合はExtraConstrutorに

**任意のメソッド名**

| という形でメソッドを追加します。
| 下記の例ではConstructorのsetupメソッドの前後に処理を入れる場合の記述となります。

.. code-block:: python

    from gris3 import extraConstructor
    class ExtraConstructor(extraConstructor.ExtraConstructor):
        def _setup(self):
            print('Do method before setup.')
        
        def setup(self):
            print('Do method after setup.')


.. seealso::

    ConstructionOrderについては
    :ref:`CST-constructionOrder`
    をご確認下さい。


専用メソッド
----------------------

constructor(self) -> gris3.constructor.BasicConstructor
++++++++++++++++++++++
インストール先のConstrcutorを返します。

createSetupParts(self)
++++++++++++++++++++++
このExtraConstrutorを運用するのに必要なノードを作成する場合はこのメソッドを
オーバーライドします。

このメソッドはConstrcutorのcreateExtraSetupPartsが呼ばれる際に使用されます。


setupUtil(self) -> extraConstructor.ui.ExtraConstructorUtil
++++++++++++++++++++++
ExtraConstrutorを運用するのに必要なノードを作成するためのGUIを返します。

このメソッドで返したGUIクラスは、FactoryのScriptsタブのExtra
Const Utilタブに表示されるようになります。

このメソッドの戻り値は

**extraConstructor.ui.ExtraConstructorUtil**

を継承したサブクラスのインスタンスとなります。