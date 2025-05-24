****************************************************
ファクトリーセッティング
****************************************************
このシステムは、コンストラクタとファクトリーモジュールを管理、
運用するためのものです。
この章ではコマンドによってファクトリーセッティングを操作し、
どのような挙動を行うものなのかを解説していきます。



運用に使用するクラス
============================
ファクトリーセッティングを運用するにあたって、主に以下のクラスを使用します。

* :ref:`FS-FactoryDataClass`
* :ref:`FS-factoryModuleManager`
* :ref:`FS-constructorManager`



.. _FS-FactoryDataClass:

factory.FactoryData
================================================
このクラスはファクトリーセッティングそのものであり、
このクラスでプロジェクトディレクトリ単位のファクトリーの設定を作成、
編集する事ができます。

FactoryDataクラスではスクリプトベースのリギングを行う上で必用な情報を設定します。


setRootPath(str)
----------------------
このメソッドはファクトリーセッティングを行う上で最も重要なメソッドです。
このメソッドの引数にはディレクトリパスを指定します。

.. code-block:: python
    :linenos:

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')

指定されたディレクトリパスは、ファクトリーセッティングの
プロジェクトディレクトリとして認識されます。
ファクトリーの操作は、
全てこのプロジェクトディレクトリとして認識されたデータに対して行われます。

.. seealso::
    :ref:`SBR-ProjectDirectory`


その他の編集・参照用メソッド
-----------------------------------
ルートディレクトリを設定したら、以下のメソッドも使用する事ができます。
この設定により、ファクトリーセッティングとして操作する対象のアセット情報を
登録する事ができます。

.. list-table:: メソッド一覧

    *   - setAssetName(str)
        - アセット名を設定する。
    *   - setAssetType(str)
        - アセットの種類を設定する
    *   - setProject(str)
        - プロジェクト名を設定する。
    *   - setConstructorName(str)
        - 使用するコンストラクタ名を設定する。
          使用できるコンストラクタ名については
          :ref:`FS-listConstructorNames`
          を参照。

.. code-block:: python
    :linenos:
    :emphasize-lines: 4,5,6,7

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.setAssetName('grico')
    settings.setAssetType('CH')
    settings.setProject('RigTraining')
    settings.setConstructorName('standardConstructor')


情報をプロジェクトディレクトリに保存する。
----------------------------------------------------
これらの情報を設定した後に、
**saveFile**
メソッドを使用すると
**setRootPath**
で指定したディレクトリの直下に、設定された情報に基づいた
**grisFactoryWorkspace.xml**
が作成されます。

.. code-block:: python
    :linenos:
    :emphasize-lines: 9

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.setAssetName('grico')
    settings.setAssetType('CH')
    settings.setProject('RigTraining')
    settings.setConstructorName('standardConstructor')

    settings.saveFile()

既存のプロジェクトディレクトリの情報を取得する。
----------------------------------------------------------
すでに設定用xmlファイルが保存されているプロジェクトディレクトリに対して
setRootPathを行った場合、設定ファイルが自動的に読み込まれ、アセット情報が
設定されている状態になります。

設定されている情報を取得するには以下のメソッドを使用することで可能です。

.. list-table:: メソッド一覧

    *   - assetName
        - アセット名を取得する。
    *   - assetType
        - アセットの種類を取得する。
    *   - project
        - プロジェクト名を取得する。
    *   - constructorName
        - 使用するコンストラクタ名を取得する。

.. code-block:: python
    :linenos:

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.assetName()
    # Result: grico # 



.. _FS-constructorManager:

constructors.ConstructorManager
================================================
このクラスはコンストラクタを管理するためのクラスです。
カレントのコンストラクタを設定したり、使用できるコンストラクタのリストの情報など
を管理しています。

また、コンストラクタにはデフォルトで取り扱うファクトリーモジュールの情報も
持っています。
ファクトリーセッティングを運用する上で、
このファクトリーモジュールの情報が必用になるため、
これらクラスを使用して必用な情報を集めてきます。

コンストラクタ自体の詳細な説明については
:doc:`constructor`
をご覧下さい。

.. _FS-listConstructorNames:

使用可能コンストラクタの一覧を取得する
---------------------------------------------------
ファクトリーセッティングに渡す、使用可能なコンストラクター名の一覧を取得するには
以下の方法で行います。

.. code-block:: python
    :linenos:

    from gris3 import constructors
    cst_mngr = constructors.ConstructorManager()
    cst_mngr.names()
    # Result: ['standardConstructor', 'unityConstructor'] # 


コンストラクタのインスタンスを取得する
---------------------------------------------------
各コンストラクタは、pythonのモジュールとして記述されています。
このモジュール自体を取得するには
**module**
メソッドを使用します。

このメソッドの引数には
**names**
メソッドによって取得できるリストのいずれかの文字列になります。

.. code-block:: python
    :linenos:

    from gris3 import constructors
    cst_mngr = constructors.ConstructorManager()
    cst_mod = cst_mngr.module('standardConstructor')
    # Result: <module 'gris3.constructors.standardConstructor' from ~>

コンストラクタ用モジュールには必ずConstructorクラスが存在します。
コンストラクタークラスの引数には上記のFactoryDataのインスタンスを渡します。

.. code-block:: python
    :linenos:
    :emphasize-lines: 11,12

    from gris3 import factory, constructors
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.setAssetName('grico')
    settings.setAssetType('CH')
    settings.setProject('RigTraining')
    settings.setConstructorName('standardConstructor')

    cst_mngr = constructors.ConstructorManager()
    cst_mod = cst_mngr.module('standardConstructor')
    cst = cst_mod.Constructor(settings)
    # Result: <gris3.constructors.standardConstructor.Constructor object at ~> # 


デフォルトのファクトリーモジュール一覧を取得する
-----------------------------------------------------
前述のように、コンストラクタには取り扱うファクトリーモジュールの
デフォルトセットが登録されています。
この一覧を取得し、FactoryDataに反映させます。

デフォルトのファクトリーモジュールセットは
**FactoryModules**
変数内に格納されています。

.. code-block:: python
    :linenos:

    from gris3 import constructors
    cst_mngr = constructors.ConstructorManager()
    cst = cst_mngr.module('standardConstructor').Constructor()
    cst.FactoryModules
    # Result: (
    #  <gris3.factory.ModuleInfo : "jointBuilder" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "cageManager" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "drivenManager" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "weightManager" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "facial" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "extraJointManager" / "None" / "None" / "">,
    #  <gris3.factory.ModuleInfo : "controllerExporter" / "None" / "None" / "">
    #)

この変数に格納されているのは
**ModuleInfo**
クラスを複数持つリストです。

ModuleInfoは

* モジュール名
* このモジュールが操作対象とするディレクトリ名
* エイリアス名（別名）
* 内部操作する際にキーワードとなるタグ

の４つの情報を持つクラスで、
ファクトリーセッティングやコンストラクタはこの情報を元にファクトリーモジュールの
管理を行います。

.. seealso::
    ModuleInfoの詳細については
    :ref:`CST-ModuleInfo`
    をご覧下さい。

ユーザーはアセットごとにこの情報をカスタマイズする事が出来ますが、
基本的にコンストラクタが要求するデフォルトのファクトリーモジュールセットは
必ず作るようにして下さい。

このファクトリーモジュールセットをFactoryDataオブジェクトに追加します。

.. code-block:: python
    :linenos:
    :caption: FactoryDataにモジュールセットを登録し、保存する。

    from gris3 import factory, constructors
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')

    cst_mngr = constructors.ConstructorManager()
    cst = cst_mngr.module('standardConstructor').Constructor()
    for info in cst.FactoryModules:
        settings.addModule(info.moduleName(), info)

    settings.saveFile()

この操作により、このアセットが取り扱うコンストラクタと、
ファクトリーモジュールのセットに関する設定が完了しました。

完了するとgrisFactoryWorkspace.xml内には各種情報とファクトリーモジュールセット
に関する情報が追記されます。



.. _FS-factoryModuleManager:

factoryModules.FactoryModuleManager
================================================
このクラスはgrisが管理するファクトリーモジュールの管理や、
情報取得機能を提供するクラスです。

このクラスのインスタンスを作成すると、
grisが管理するファクトリーモジュールを一度全てインポートします。
この処理は時間がかかるため、
このクラスはシングルトンになっており余計な処理を挟まないようになっています。

ファクトリーモジュールは要素の書き出し機能と、
書き出し先がペアとなる事で成立します。
モジュールと書き出し先のペアリングは、
ファクトリーセッティングによりプロジェクトディレクトリ単位で設定する事ができます。
しかし、毎回ペアリングを設定しなくてもいいように、
各ファクトリーモジュールはデフォルトの書き出し先名を持っています。

FactoryModuleManagerクラスはこのペアリング情報を提供します。


モジュールと書き出し先のデフォルトのペア情報を取得する
------------------------------------------------------------
FactoryModuleManagerのmoduleNameListメソッドを使用すると、
現在使用可能なファクトリーモジュールの一覧が取得できます。
この一覧は辞書型式になっており、
モジュール名とそのモジュールを管理するクラスにアクセスできるようになります。

.. code-block:: python
    :linenos:

    from gris3 import factoryModules
    fmm = factoryModules.FactoryModuleManager()
    fmm.moduleNameList()
    # Result: {
    #    'extraJointManager': <class 'gris3.factoryModules.extraJointManager.Department'>,
    #    'facial': <class 'gris3.factoryModules.facial.Department'>,
    #    'cageManager': <class 'gris3.factoryModules.cageManager.Department'>,
    #    'controllerExporter': <class 'gris3.factoryModules.controllerExporter.Department'>,
    #    'workspace': <class 'gris3.factoryModules.workspace.Department'>,
    #    'weightManager': <class 'gris3.factoryModules.weightManager.Department'>,
    #    'model': <class 'gris3.factoryModules.model.Department'>,
    #    'drivenManager': <class 'gris3.factoryModules.drivenManager.Department'>,
    #    'jointBuilder': <class 'gris3.factoryModules.jointBuilder.Department'>
    #}

各モジュールには必ずDepartmentクラスを持っており、
このクラスが各モジュールの動作を定義しています。

モジュールのデフォルトで設定されている
書き出し先ディレクトリ名もこのクラスが管理しています。

.. code-block:: python
    :linenos:
    :caption: jointBuilderモジュールのデフォルト書き出し先名を取得する。

    from gris3 import factoryModules
    fmm = factoryModules.FactoryModuleManager()
    cls = fmm.moduleNameList().get('jointBuilder')
    cls().directoryName()
    # Result: joints # 



.. _FS-factorySettingsClass:

factoryModules.FactorySettings
=============================================
このクラスはファクトリーウィンドウと紐付けられた非常に重要なクラスですが、
実態は
:ref:`FS-FactoryDataClass`
クラスを親クラスとしたサブクラスです。

従って
:ref:`FS-createProjDir`
内で記述されている

.. code-block:: python

    settings = factory.FactoryData()

を

.. code-block:: python

    settings = factoryModules.FactorySettings()

に置き換えても動作するようになっています。


FactoryDataクラスとの違い
--------------------------------------------
前述の説明だけ見るとほぼFactoryDataクラスと同じ内容ですが、
こちらはQtCore.QObjectからも多重継承しており、
設定変更を行う度にGUIへシグナルを送出するようになっています。

.. blockdiag::

    blockdiag{
        QtCore.QObject, factory.FactoryData -> factoryModules.FactorySettings;
    }

そのため、このクラスはシングルトンで作られており、
存在するファクトリーウィンドウや実行するConstructorなど、
すべてに対して影響を与えます。

.. warning::
    このクラスはGUIへの影響が大きいため取り扱いには注意が必用です。

ファクトリーセッティングというシステムにおいては、
起動中のアプリ内で復数のアセットを同時進行で扱う事はないという前提があります。
そのためファクトリーセッティングでは常に現在作業中のアセットの情報のみが提供され、
Constructorに関する機能はこの一つのアセットの情報のみを取り扱うように設計されています。

.. blockdiag::

    blockdiag{
        A[label = 'FactorySettings'];
        B[label = 'ConstructorManager'];
        C[label = 'Constructor'];
        D[label = 'FactoryWindow(GUI)'];
        
        A <-> B,C,D [label='data'];
    }
 
代表的なのはconstructorモジュールのcurrentConstructorメソッドです。
このメソッドは現在FactorySettingsクラスのsetRootPathされている
プロジェクトディレクトリが設定されているコンストラクタを返すようになっています。

これはcurrentConstructor内でFactorySettingsクラスを呼び出し、
このクラスがセットしているプロジェクトディレクトリの設定を
読み取るようになっているためです。

.. blockdiag::

    blockdiag{
        A[label = 'ConstructorManager'];
        B[label = 'FactorySettings'];
        
        A -> B [label='access'];
        B -> A [label='data'];
    }


FactorySettingsを任意のFactoryDataに置き換える
---------------------------------------------------
通常はFactorySettingsを使用する事によって問題なく運用する事ができますが、
このクラスはファクトリーウィンドウなどのGUIにも影響を及ぼすため、
スクリプトを裏で実行したい場合などには向かないケースもあります。

このようにGUI起動中に別の設定でConstructorを実行したいなどの場合は

**factoryModulues.startManualy**

を使用します。
このクラスはインスタンス作成時にFactoryDataオブジェクトを渡して使用する、
with文用のコンテキストです。

このクラスをwith文で使用すると、
with内で呼ばれるFactorySettingsは全てインスタンス時に渡した
FactoryDataオブジェクトに置き換わります。

.. code-block:: python
    :linenos:

    from gris3 import factoryModules, constructors, factory
    # GUIに連動した設定オブジェクトを作成。
    fs = factoryModules.FactorySettings()
    fs.setRootPath('D:/assets/testRig')
    fs.setConstructorName('standardConstructor')

    # currentConstructorメソッドは常にFactorySettingsの内容を反映する。========
    constructors.currentConstructor()
    # Result: <class 'gris3.constructors.standardConstructor.Constructor'> # 

    fs.setConstructorName('unityConstructor')
    constructors.currentConstructor()
    # Result: <class 'gris3.constructors.unityConstructor.Constructor'> # 

    fd = factory.FactoryData()
    fd.setRootPath('D:/assets/testRig')
    fd.setConstructorName('standardConstructor')
    constructors.currentConstructor()
    # Result: <class 'gris3.constructors.unityConstructor.Constructor'> # 
    # =========================================================================

    # startManualy内だけcurrentConstructorメソッドの挙動が変わる。=============
    with factoryModules.startManualy(fd):
        constructors.currentConstructor()
        # Result: <class 'gris3.constructors.standardConstructor.Constructor'> # 
    cm.currentConstructor()
    # Result: <class 'gris3.constructors.unityConstructor.Constructor'> # 
    # =========================================================================

constructorモジュール内の機能にはFactorySettingsにアクセスしているものが多いため、
このモジュールにまつわる何かを呼ぶ際にはstartManualyを使用すると良いでしょう。



.. _FS-createProjDir:

プロジェクトディレクトリをコマンドで作成する
========================================================================
このセクションでは前述した仕組みを使用して、
スクリプトでファクトリーが取り扱うプロジェクトディレクトリを作成してみましょう。

以下のコードでは任意のディレクトリにstandardConstructorのデフォルトセットを設定し、
プロジェクトディレクトリを作成しています。

尚、FactoryDataにセットするディレクトリパスは、
予め作成しておく必用があります。

.. literalinclude:: factorySettings/createRigProject.py
    :language: python
    :linenos:
    


.. _FS-executeBuildScript:

プロジェクトディレクトリのビルドスクリプトを実行する
========================================================================
このセクションではアセットのリギングが完了した
プロジェクトディレクトリのスクリプトを、コマンドから実行してみましょう。

まずは定番の、
FactoryDataクラスを作成してプロジェクトディレクトリのパスを設定から初めます。

.. code-block:: python
    :linenos:

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')

続いて、実行可能なモジュールの一覧を取得してみましょう。

.. code-block:: python
    :linenos:
    :emphasize-lines: 4,5

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.listScripts()
    # Result: ['setup_high', 'setup_low', '__init__'] # 

FactoryData.listScriptsメソッドは、
Constructorとして実行可能なPythonモジュールがリストとして返ってきます。

Constructorとして実行可能とは、
単純にモジュール内にConstructorという名前の機能が存在するかどうかで判定しています。
また原則として__init__は実行しても無効です。（対応する読み込みモデルが存在しないため）


最後にこのリストの中の一つを実行してみましょう。
尚リストの中身がわかっているのであれば、listScriptsは行う必要はありません。

.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    from gris3 import factory
    settings = factory.FactoryData()
    settings.setRootPath('D:/assets/testRig')
    settings.execScript('setup_high')

これで目的のアセットのビルドが開始されます。