****************************************************
標準付属のフェイシャルシステム
****************************************************
このセクションではGRIS標準で付属するフェイシャルシステム

**basicFacialSystem**

モジュールについて説明します。


このモジュールは
**ExtraConstructor**
です。

.. seealso::

    ExtraConstructorについては
    :ref:`EXCST-ExtraConstructor`
    をご確認下さい。




.. _BFS-LayerModule:

layerモジュール
============================================
このモジュールはフェイシャル機能をレイヤー化するための機能を提供します。
layerモジュールには以下の重要な機能が含まれます。

- :ref:`BFS-layerOperatorClass`
- :ref:`BFS-layerManagerClass`

レイヤー化についての仕様は

 1. 大元の顔ジオメトリのグループ（以後face_grp）をレイヤー毎にコピー
 1. 各レイヤー用の顔メッシュのoutMeshとinMeshをそれぞれ接続する
 1. コピーした顔のメッシュに対し、各レイヤーで任意のリグを構築
 
となります。
3番については、
接続する順番はlayerManagerにlayerOperatorを設定する順序に準じます。

**Phase 1**

大元の顔ジオメトリのグループ（face_grp)を、
任意のプレフィックを付けた状態でコピーし、各LayerOperatorに渡します。

.. blockdiag::

    blockdiag{
        default_shape = roundedbox

        FACE[label = 'face_grp', shape='ellipse', color = '#90B0D0'];
        A[label = 'Jaw Opened Face'];
        B[label = 'Blend Shape Face'];
        C[label = 'Tweaked Face'];
        SKINNED[label = 'Skinned Face'];

        FACE -> A, B, C, SKINNED[label='copy'];
    }
    
**Phase 2**

コピーされた各メッシュのinMesh、outMeshを接続します。
（接続する順番はlayerManagerにlayerOperatorを設定する順序に準じます。）

.. blockdiag::

    blockdiag{
        default_shape = ellipse
        default_node_color = '#90B0D0'

        A[label = 'Jaw Opened Face'];
        B[label = 'Blend Shape Face'];
        C[label = 'Tweaked Face'];
        SKINNED[label = 'Skinned Face'];

        A -> B -> C -> SKINNED[label='in out'];
    }
    
    
**Phase 3**

各LayerOperatorではsetupやpostProcessメソッド内でコピーされたノードに編集を加え、
リグの構築を行います。

.. blockdiag::

    blockdiag{
        default_shape = diamond

        B[label = 'Blend Shape Face', shape='roundedbox'];
        M[label = 'Copied face_grp', shape='ellipse', color = '#90B0D0'];
        PS[label = 'Pre Setup', color = "#F0D080"];
        S[label = 'Setup', color = "#F0D080"];
        PP[label = 'PostProcess', color = "#F0D080"];

        B -> PS, S, PP;
        PS, S, PP -> M;
    }

.. _BFS-layerOperatorClass:

layerOperator
-----------------------------
このクラスはフェイシャルの機能をレイヤー化する際に、
各レイヤー単独の機能を実装するための基底クラスとなります。

各レイヤーはこのクラスを継承し、
各種メソッドをオーバーライドして動作を実装してきます。


.. _BFS-layerManagerClass:

layerManager
-----------------------------



.. code-block:: python

    class Constructor(constructors.currentConstructor()):
        def init(self):
            self.installExtraConstructor('cstExtensions')
