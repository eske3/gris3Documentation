*****************************
更新履歴
*****************************
0.9.10.0
============================
+ extraConstructor.ExtraConstructorにcreateSetupPartsを追加。
+ constructor.ConstructorにcreateExtraSetupPartsを追加。
+ toolsにanimUtilモジュールを追加。
+ constructor.BasicConstructorのloadSkinWeightsでウェイトの読み込み順序の制御機構を追加。
    - 読み込む前に予めメッシュのinMesh/outMeshの接続を走査し、下流の方から読み込むように挙動を変更。


0.9.9.2
============================
+ gris3.showFactoryにプロジェクトパスを渡した際に、プロジェクト履歴にパスが追加されるように変更。
+ settingsモジュールに、ファクトリーのプロジェクト履歴を追加するaddPathToHistory関数を追加。


0.9.9.1
============================
+ tools.selectionUtilにselectHardEdges関数を追加。
+ tools.modelingSupporterにunlockAndSetNormal関数を追加。
+ gadgets.cleanupToolsにunlockAndSetNormalへアクセスするボタンを追加。

0.9.9.0
============================
+ ハードサーフェースモデリング用の便利機能モジュールhardsurfaceModelerを追加。
+ ハードサーフェースモデリング用の便利機能集ガジェットを追加(β版)。
+ 高解像度モニタ対応（β版）
+ showFactory関数に強制的にGUIを更新するforceUpdateオプションを追加。
+ rigScripts.PresetElementクラスにsuffixを追加。
    - インスタンス時の第3引き数にsuffixを追加。
    - suffixにアクセスするためのメソッド
      **suffix()**
      を追加。
    - PresetElement__call__時の戻り値のフォーマットが
        unitName-position
      から
        unitNameSuffix-position
      に変更。
+ funcモジュール。
    - funcモジュール内のドキュメントを更新。
    - func.SoftModificationで作成されるradiusコントローラのアトリビュートをscaleXからradiusに変更。
    - func.createSculptDeformerの戻り値の中身を全てnode.AbstractNode系に統一。
    
0.9.8.1
============================
+ nodeモジュールにshadingNode関数を追加。

0.9.8.0
============================
+ QObjectのサブクラスの__new__処理を全て削除し、maya2020に対応

