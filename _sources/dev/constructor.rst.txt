****************************************************
コンストラクタ
****************************************************
コンストラクタはリグ自体の仕様を定義し、
スクリプトベースリギングのスクリプト実行の流れを制御するための仕組みです。

コンストラクタシステムには主に

* Constructorクラス
* ExtraConstructorクラス
* ModuleInfoクラス
* factoryModuleモジュール

などによって構成されています。


.. _CST-Constructor:

Constructor
============================================
このクラスはリグ自体の仕様を定義し、スクリプトによるリグの実行の流れを制御する
仕組みの中核となる機構です。


リグの仕様
----------------------
リグの仕様とはすなわち、Maya内のリグにおける階層構造や名前の規則など、
ありとあらゆる仕様を指します。

grisではデフォルト仕様のBasicConstructorが存在しますが、開発者はこのクラスを
継承したサブクラスでさまざまな動作をカスマイズする事ができます。

カスタマイズする要素としては大まかに以下の要素があります。

* :ref:`CST-createRoot`
* :ref:`CST-createCtrlRoot`
* :ref:`CST-scriptTemplate`

BasicConstructorクラスには未定義の場合にデフォルトで動作する関数が用意されていますが、
これら関数を置き換えることにより、
独自の仕様の階層を持つリグのフォーマットを作成することができます。


.. _CST-createRoot:

ルートの作成
+++++++++++++++++++++++++++++++
リグ全体を格納するためのルートノードと、そのサブグループの作成を定義します。


.. _CST-createCtrlRoot:

コントローラルートの作成
++++++++++++++++++++++++++++++++++
アセット全体の移動や回転を行うためのルートコントローラ作成を定義します。


.. _CST-scriptTemplate:

スクリプトテンプレートの作成
+++++++++++++++++++++++++++++++++++++
リグのビルドを行うためのスクリプトのテンプレートを定義します。



.. _CST-constructionOrder:

ConstructionOrder
----------------------
ConstructionOrderはFactoryからリグのビルドスクリプトを実行する際に、
実行されるメソッドの順番のことを指します。
ConstructionOrderはConstructorクラスのメンバ変数ProcessListによって定義します。

ProcessListはtupleまたはlistであり、その中には３つの文字列を含むtupleを格納します。
３つの文字列はそれぞれ

* メソッド名
* メソッド開始時にユーザーに提示するメッセージテキスト
* メソッド終了時にユーザーに提示するメッセージテキスト

を表します。

**定義例**

.. code-block:: python

    from gris3 import constructors
    class Constructor(constructors.currentConstructor()):
        ProcessList = (
            ('preProcess', 'Start to Pre Process.', 'Pre Process was done.'),
            ('importJoints', 'Import joints.', 'Done to import.'),
            ('importModels', 'Import models.', 'Done to import models.'),
            ('finalizeBaseJoints', None, None),
            ('setupSystem', 'Setup system.', 'Done to setup system.'),
            (
                'createController',
                'Start controller creation.', 'Controller creation was done.'
            ),
            ('preSetup',  'Start pre setup.', 'Done.'),
            ('setup', 'Start setup.', 'Done.'),
            (
                'finalizeSetup',
                'Start to finalize setup.', 'Done finalizing setup.'
            ),
            ('postProcess', 'Start post process.', 'Done.'),
            ('finished', None, None),
        )    

この例の場合、Consutructorは

    1. preProcess
    2. importJoints
    3. importModels
    4. finalizeBaseJoints
    5. createController
    6. preSetup
    7. setup
    8. postProcess
    9. finished

の順に実行されることになります。

.. _CST-ModuleInfo:

ModuleInfoクラス
===================================================