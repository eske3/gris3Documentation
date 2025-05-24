ツールを起動し初期設定を行う
=======================================
リギングを行うためのツール「GRIS」を起動します。
起動するにはScriptEditorのPythonタブで以下のコマンドを実行します。

.. code-block:: python

    import gris3
    gris3.showFactory()

.. image:: ../img/quickStart_factory/001.png
    :width: 400

まずはProjectSelectorが起動するので、任意のディレクトリパスをPath
フィールドに入力し、SetProjectボタンをクリックするかEnterキーを
プロジェクトディレクトリを確定します。

.. image:: ../img/quickStart_factory/002.png
    :width: 400

続いて初回のディレクトリを指定した場合はプロジェクト情報設定画面に
なりますので、任意の設定を入力します。

.. image:: ../img/quickStart_factory/003.png
    :width: 400

AssetNameに任意（今回はcharAAとします）のアセット名を入力、
ProjectはTraining、AssetTypeはキャラの場合はCH、背景ならBG、
プロップはPR、乗り物はVRなどを選択して下さい。


ConstructorTypeは今回は「Standard Constructor」を選択し、
Applyボタンをクリックします。

.. seealso::
    コンストラクタについての詳細は
    :doc:`constructor`
    を御覧ください。

設定が成功すると、ProjectSelectorで選択したディレクトリ内に必要ファイル
(xml等）とディレクトリが作成され、FactorytタブへとGUIが変更されます。

.. image:: ../img/quickStart_factory/004.png
    :width: 400
.. image:: ../img/quickStart_factory/005.png
    :width: 400

これで初期設定は完了です。
**以後、このリギング用ツールの事をFactoryと呼称します。**


次回GRISのFactoryを起動すると再びProjectSelectorが現れます。
その際履歴が残っているので履歴から目的のアセットを選択すると
Factoryタブから開始されます。

.. image:: ../img/quickStart_factory/006.png
    :width: 400