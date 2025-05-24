モデルを保存する
==================
all_grpを用意する
--------------------------
リグを入れるモデルは、決められたディレクトリに保存する必用があります。
またScene内には決まった階層構造を作成する必用があります。


まずはMaya上で通常の方法でモデルを開きます。

.. image:: ../img/quickStart_factory/007.png
    :width: 400

初期設定を行った際に設定したConustrutorTypeが「StandardConsutructor」の場合、
モデルには必ず

* all_grp
* modelAllSet

の２つが必要になります。もしこれらがない場合は下記の手順で作成し、
all_grpの中にすべてのモデルデータを格納した状態にする必要があります。


上記2つのグループとセットを作成するにはFactoryのModelSetupツールの
Create all_grpから作成します。

.. image:: ../img/quickStart_factory/008.png
    :width: 400


ワークに保存する
----------------------
ここまで作業したところで一度作業ファイルを保存しましょう。
GRISのFactoryには作業データを保存するための格納場所が定められているので、
そこへ保存します。


まずはFactory左の機能一覧からWorkspaceをクリックし、ブラウザを表示させます。

.. image:: ../img/quickStart_factory/009.png
    :width: 400

次にBasenameに「model」など適当に自分が判別できる名前を入力し、
保存ボタンをクリックして保存します。
このWorkspaceはあくまで最終的なデータを作成するための作業シーンを
保存するための仮データ置き場です。
今後作成するジョイントやウェイト作業などの途中データもこのWorkspace内に
保存していくことになります。


.. _export_model:

モデルデータを書き出す
----------------------


それではモデルデータを一度書き出します。


まずはOutlinerからall_grpを選択します。
続いてFactoryの機能一覧からModelsを選択し、
モデル書き出しGUIを表示させます。

.. image:: ../img/quickStart_factory/010.png
    :width: 400

Basenameから「アセット名_high」を選択しExportボタンをクリックして
書き出します。
これでモデルがHighModelとして書き出されます。
今回はLowアセットは用意しませんので、モデルの書き出しはこれにて終了です。


書き出したデータをチェックする
---------------------------------
MayaはExportを行うと、まれにバグで書き出したデータを破壊する事があります。
従って念の為書き出したデータのチェックを行いましょう。


FactoryのModelsを選択し、ブラウザから先程書き出したファイル
(今回はryofuA_high)の横の三角マークをクリックして履歴を表示させます。

.. image:: ../img/quickStart_factory/011.png
    :width: 400

今回保存した.v01をダブルクリックしてファイル操作オプションを表示させ、
そこからOpenを選択してシーンを開きます。

.. image:: ../img/quickStart_factory/012.png
    :width: 400

開いたシーンを確認し、問題がなければモデルの書き出しは完了となります。