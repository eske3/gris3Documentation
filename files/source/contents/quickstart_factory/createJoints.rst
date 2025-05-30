ジョイントを作成する
=======================================
アセット用のジョイントを作成していきます。
ジョイント作成には以下の方法があります。

* Mayaの機能を用いて作成する
* Grisの機能を使用して作成する
* Grisのモジュールを使用して作成する

まずは３のモジュールを使用した所謂「モジュラーリギング」
でのアプローチを行います。


また、この作業にはモデルも必要ですので
:ref:`export_model`
で書き出したモデルを開くかインポートしておきます。


ルートを作成する
---------------------------------
ジョイント作成の前に、まずは全アセット共通となるrootノードを作成します。
まずはFactoryの機能一覧からJointBuilderを選択し、
続いてUnit作成ボタンをクリックしてユニット作成GUIを表示させます。

.. image:: ../img/quickStart_factory/013.png
    :width: 400
    
続いてCreate Rootボタンをクリックしてrootを作成します。

.. image:: ../img/quickStart_factory/014.png
    :width: 400


モジュールからジョイントを作成する
---------------------------------------------
つづいてもジューラーリギングの機能を使用して骨を作成します。
まずは人型のモジュールである
**「humanSpineRig」**
や
**「humanArmRig」**
などを使用して組み立てていきますが、
通常の人型の場合はプリセットがあるのでそちらを使用します。
PresetsからBasic Humanを選択し、作成ボタンをクリックします。

.. seealso::
    リグのプリセットモジュールでである
    **ユニット**
    関しては
    :doc:`rigUnits`
    を御覧ください。


.. image:: ../img/quickStart_factory/015.png
    :width: 400

作成されたジョイントは「root|joint_grp|world_trs」の下に作成されます。
これから作成していくベースのジョイントはすべてこのworld_trsの下に作成します。


ジョイント調整時に注意点
----------------------------
BasicHumanで作成されたジョイントは、今回のプロジェクトで使用する
基礎ジョイントをすべて内包しているので、まずはこれをキャラクタの
関節位置に合わせます。
位置を調整する方法は通常のジョイントの位置調整と同じですが、デフォルトで
作成された時の軸の向きは維持しておいて下さい。

.. figure:: ../img/quickStart_factory/016.png
    :width: 400
    
    例えば肘の場合、Z軸が肘の後ろ方向を向くなど

また、モジュールで作成されたジョイントはリグ用の構成を保持する
メタノードが含まれています。(このメタノードはunit_grp下に置かれています)

.. image:: ../img/quickStart_factory/017.png
    :width: 400

メタノードには必要ノードのコネクションがはられており、これがなくなると
リグの構築ができなくなるので、モジュラーリギング用の骨は基本的に
削除しないで下さい。
(コネクションの差し替えによる動作調整を行うことができるモジュールも
ありますが今回は割愛します)


ジョイントをミラーリングする場合はJointBuilderのミラーリング機能を
使用して下さい。

.. image:: ../img/quickStart_factory/018.png
    :width: 400


人型のジョイント位置を調整する
----------------------------------
移動や回転を使用してキャラクタの体型にジョイントをあわせていきます。

.. image:: ../img/quickStart_factory/019.png
    :width: 400

基本的にほとんどのキャラは左右対称なので、まずは左半身の位置をあわせます。


続いてジョイントの軸を調整します。


このヒューマンプリセットは中心ならびに左半身は原則X軸が子供のほうを
向かせます。

.. image:: ../img/quickStart_factory/020.png
    :width: 400

位置調整を行うときに移動で行うとX軸が子供の方からずれている場合があります。
その場合はJointBuilderのEditタブのFixOrientationボタンを
クリックすると現在状態を維持しながらX軸を子供の方へ向けることができます。


また、任意の方法でジョイントの軸を調整することも可能です。

.. image:: ../img/quickStart_factory/021.png
    :width: 400
.. image:: ../img/quickStart_factory/022.png
    :width: 400


モジューラーリグジョイントをミラーリングする
--------------------------------------------------
各軸の向きが適正かどうかを確認後、問題なければ左右反転します。


左右反転するにはJointBuilderのEditタブのミラーリングを行います。
今回は鎖骨（clavicle）や大腿（thigh）を選択して実行します。

.. image:: ../img/quickStart_factory/023.png
    :width: 400

最後にジョイントのルートを選択して（hip_jnt_C）を選択してFixOrientationを
クリックしてジョイントの回転値をリセットしておくと良いでしょう。


最後の一度この状態をWorkspaceに保存しておきます。

.. image:: ../img/quickStart_factory/024.png
    :width: 400

Workspaceのブラウザに任意の名前を入力して保存しておきましょう。


ジョイントを書き出す
-------------------------
作業が完了したら人型のジョイントを含んだrootを書き出します。
書き出すにはJointBuilderのSaveJointsタブをクリックし、
表示されるブラウザを使用します。

.. image:: ../img/quickStart_factory/025.png
    :width: 400

Outlinerからrootを選択し、ブラウザのBasenameに「baseJoint」と入力しExport
ボタンをクリックして書き出します。


最後に書き出したデータを開き、問題なく書き出されているか確認します。
