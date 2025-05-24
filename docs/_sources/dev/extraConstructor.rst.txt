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

.. seealso::

    ConstructionOrderについては
    :ref:`CST-constructionOrder`
    をご確認下さい。