****************************************************
extraJoint
****************************************************
このモジュールはサブジョイントの生成や管理を行う機能を提供します。


関数
===========================

listExtraJoints
----------------------
任意のノードのリストの中からExtraJointをリストします。
戻り値は
:REF:`TEJ-ExtraJointClass`
を持つリストです。

.. list-table::

    +   -   **引数**
        -   **型**
        -   **説明**
    +   -   nodelist
        -   list(またはNone）
        -   リストアップする対象となるノード名のリストを指定します。
            Noneが指定されている場合は選択ノードからリストアップされます。
    +   -   tag
        -   str
        -   このタグでリストアップするExtraJointをフィルタします。
            この引数で指定した文字列にマッチするタグを持つExtraJointだけがリストされます。


selectExtraJoint
----------------------
任意のノードの階層下にあるExtraJointを選択します。
戻り値は選択された
:REF:`TEJ-ExtraJointClass`
のリストを返します。

.. list-table::

    +   -   **引数**
        -   **型**
        -   **説明**
    +   -   topNodes
        -   list(またはNone）
        -   この引数で指定されたノードの階層下にあるExtraJointを選択します。
            Noneの場合選択ノード下にあるExtraJointを選択します。
    +   -   tag
        -   str
        -   このタグで選択するExtraJointをフィルタします。
            この引数で指定した文字列にマッチするタグを持つExtraJointだけが選択されます。


createMirroredJoint
--------------------------
選択されたExtraJointをミラーリングします。

.. list-table::

    +   -   **引数**
        -   **型**
        -   **説明**
    +   -   targetJoints
        -   list(またはNone）
        -   リストアップする対象となるノード名のリストを指定します。
            Noneが指定されている場合は選択ノードからリストアップされます。


create
-----------------
ExtraJointを作成します。

引数parentLengthは親の長さを入力します。
親の長さとは親ノードから親ノードの最初の子ノードまでの長さで、
引数parentに指定したノードの同様の長さとの比率で、
matrixで指定した位置に補正をかけます。

.. list-table::

    +   -   **引数**
        -   **型**
        -   **説明**
    +   -   basename
        -   str
        -   ベースとなる名前を指定します。
    +   -   nodeType='joint'
        -   str
        -   ノードの種類を指定します。基本的にはjointを使用します。
    +   -   nodeTypeLabel='bndJnt'
        -   str
        -   ノードの種類を表す文字列を指定します。
    +   -   side=0
        -   str or int
        -   ノードの位置を表す値または一文字の文字を指定します。
    +   -   parent=None
        -   str
        -   作成する際の親ノードを指定します。
    +   -   offset
        -   int
        -   オフセット用の階層をいくつ作るかを指定します。
    +   -   matrix=None
        -   listまたはNone
        -   作成位置を表す行列を設定します。
            Noneが指定されている場合は親と同位置に配置されます。
    +   -   worldSpace=False
        -   bool
        -   matrixをワールド空間として扱うかどうかを指定します。
    +   -   radius
        -   float
        -   implicitSphereの大きさを指定します。
    +   -   jointSize
        -   float
        -   jointの大きさを指定します。
    +   -   parentLength
        -   float
        -   
    +   -   tag
        -   str
        -   任意のタグを指定します。
        

.. _TEJ-ExtraJointClass:

ExtraJoint
===========================
エクストラジョイントを制御するための機能を提供するクラスです。

メソッド
----------------------

.. list-table::

    +   -   **メソッド名**
        -   **引数**
        -   **戻り値**
        -   **説明**
    +   -   shape
        -   
        -   node.Transform
        -   ExtraJointのシェイプオブジェクトを戻す。
    +   -   isValid
        - 
        -   bool
        -   初期化を行ったオブジェクト名がExtraJointかどうかを返す。
    +   -   joint
        -   
        -   node.Joint
        -   ExtraJointのSpace階層直下のジョイントを返す。
    +   -   radius
        -   
        -   float
        -   シェイプの描画半径を返す。
    +   -   jointRadius
        -   
        -   float
        -   このExtraJointが持つジョイントの大きさを返す。
    +   -   tag
        -   
        -   str
        -   設定されているタグを返す。
    +   -   setTag
        -   str
        -   
        -   任意のタグを設定する。

使用例
----------------------

.. code-block:: python
    :linenos:

    from gris3 import node
    from gris3.tools import extraJoint