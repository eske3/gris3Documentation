*****************************
インストールと起動
*****************************

インストール
=============================
インストールするにはMayaのスクリプトパスにgris3ディレクトリをコピーして下さい。

.. list-table:: 標準的なインストール先のディレクトリ
    :widths: 10 90

    *   - Windows
        - OSドライブ：\\Users\\<username>\\Documents\\maya\\scripts
    *   - Linux
        - ~/maya/scripts
    *   - Mac OSX
        - ~/maya/scripts
        

起動
=============================
grisにはメインとなるファクトリーウィンドウの他、
便利な機能を集めたツールバーなどがあります。
起動するには以下のコマンドをスクリプトエディタのPythonタブにて実行して下さい。

ファクトリーウィンドウ
-----------------------

.. code-block:: python

    import gris3
    gris3.showFactory()


Grisツールバー
-----------------------
    
.. code-block:: python

    import gris3
    gris3.showToolbar()


その他ガジェットの起動
============================================
Grisツールバーは、名前の通りツールバースタイルのウィジェトですが、
特定のツールを集中的に使うには不便な場合もあります。
そのような場合は、特定のツールだけを切り出したガジェットを起動すると良いでしょう。

Joint Editor
---------------------------

.. code-block:: python

    from gris3 import gadgets
    gadgets.openJointEditor()

.. image:: ../img/install/jointEditor.png
    :height: 300
    
.. seealso::
    :doc:`../gadgets/jointEditor`


モデリング用サポートウィンドウ
---------------------------------------

.. code-block:: python

    from gris3 import gadgets
    gadgets.openModelSetup()

.. image:: ../img/install/modelSetup.png
    :height: 300

.. seealso::
    :doc:`../gadgets/modelSetup`


ポリゴンを半分消去するウィンドウ
------------------------------------------

.. code-block:: python

    from gris3 import gadgets
    gadgets.openPolyHalfRemover()

.. image:: ../img/install/polyHalfRemover.png



ポリゴンをミラーリングするウィンドウ
--------------------------------------------

.. code-block:: python

    from gris3 import gadgets
    gadgets.openPolyMirror()

.. image:: ../img/install/polyMirror.png


ポリゴンをを任意の軸でカットするウィンドウ
-----------------------------------------------

.. code-block:: python

    from gris3 import gadgets
    gadgets.openPolyCutter()
    
.. image:: ../img/install/polyCutter.png



リネーマーを起動する
-----------------------
このコマンドは選択オブジェクトの数によってウィンドウが変化します。
単体選択版と復数選択版が存在します。

.. code-block:: python

    from gris3 import gadgets
    gadgets.showRenamer()

.. image:: ../img/install/multRenamer.png
    :height: 300

.. image:: ../img/install/singleRenamer.png