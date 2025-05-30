****************************************************
ファクトリーモジュール
****************************************************
コンストラクタがビルドする際に、
必要となる要素を作成、書き出すための仕組みを提供することを目的とした
モジュール群です。

ファクトリーモジュールは都合に応じて追加、拡張することができます。


仕様
============================
ファクトリーモジュールを追加するにはFactoryModulesパス内に
任意の仕様で作成したPythonモジュールを作成します。

FactoryModuleパスはデフォルトではfactoryModulesパッケージ直下、
ならびに
**globalSettings.xml**
によって定義されるPythonモジュール内になります。

.. seealso::
    :ref:`ST-globalSettingsXML`


モジュールの仕様
-------------------------------
ファクトリーモジュールは、Pythonのモジュールでもパッケージでも問題ありませんが、
基本的にはパッケージで作成することをオススメします。
以下基本的なパッケージ構成を示します。

.. blockdiag::

    blockdiag{
        A[label='FactoryModuleName', color='#cfbc7a', shape=note];
        B[label='__init__.py'];
        C[label='icon.png'];
        D[label='python_module.py...', stacked];
        
        A -> B,C,D;
    }


__init__.py
--------------------------
このモジュール内には必ず
:ref:`FM-AbstractDepartmentClass`
クラスを継承した
**Departmentクラス**
を作成する必要があります。

また、ファクトリー用のGUIについては
:ref:`FM-AbstractDepartmentGUIClass`
を継承したクラスを作成し、DepartmentクラスのGUIメソッドで返します。

.. code-block:: python
    :linenos:
    :caption: __init__.py

    from gris3 import factoryModules


    class Department(factoryModules.AbstractDepartment):
        def init(self):
            self.setDirectoryName('extraJointScripts')

        def label(self):
            r"""
                表示するラベルを返す。
                
                Returns:
                    str:
            """
            return 'Custom Factory'

        def priority(self):
            r"""
                表示順序のプライオリティを返す
                
                Returns:
                    int:
            """
            return 10

        def GUI(self):
            r"""
                GUIを返す。
                
                Returns:
                    CustomFactoryGUI:
            """
            return CustomFactoryGUI



作成に使用するクラス
============================
ファクトリーモジュールを作成するにあたって、以下のクラスを使用します。

* :ref:`FM-AbstractDepartmentClass`
* :ref:`FM-AbstractDepartmentGUIClass`



.. _FM-AbstractDepartmentClass:

factoryModules.AbstractDepartment
================================================
このクラスはFactoryのセクションを定義する機能を提供する基底クラスです。

新たなファクトリーモジュールを作成する場合はこのクラスを継承したクラスを
作成する必要があります。

よく使用するメソッド一覧
-----------------------------------

.. list-table:: メソッド一覧

    *   - init
        - __init__内で呼ばれる初期化用のオーバーライド用メソッド。
          用途の指定は特にないので、初期化用として自由に使用可能。
    *   - label -> str
        - Factoryの一覧に表示されるときのラベルを返す上書き用メソッド。
    *   - setAliasName(name : str)
        - Factoryの一覧に表示されるときのエイリアス名を設定する。
          こちらでエイリアス名が設定されている場合、
          labelの戻り値ではなくこちらがFactoryの一覧に表示される。
    *   - priority -> int
        - Factoryのリストに表示する際の優先度を返す上書き用メソッド。
          数字が高い方がリストの上に表示される。
          -1の場合はリストの下方へ回される。
    *   - directoryName -> str
        - 操作対象ディレクトリ名を返す。
    *   - rootPath -> str
        - Factoryが現在管理するプロジェクトのルートパスを返す。
          directoryNameと合わせて操作対象となるディレクトリパスを取得できる。


.. _FM-AbstractDepartmentGUIClass:

factoryModules.AbstractDepartmentGUI
================================================
このクラスはFactory内に表示するGUIのベースを提供します。

AbstractDepartmentクラスのGUIメソッドでは、このクラスを継承した
クラスを返す必要があります。
