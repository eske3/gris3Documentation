from gris3 import factory, constructors, factoryModules
# 使用するコンストラクタ名を定義しておく。
constructor_name = 'standardConstructor'

# アセットの設定を行う。
settings = factory.FactoryData()
settings.setRootPath('D:/assets/testRig')
settings.setAssetName('grico')
settings.setAssetType('CH')
settings.setProject('RigTraining')
settings.setConstructorName(constructor_name)

# 各モジュールのデフォルトの書き出し先のテーブルを作成する。
fmm = factoryModules.FactoryModuleManager()
dir_table = {
    name : f_cls().directoryName()
    for name, f_cls in fmm.moduleNameList().items()
}

# 使用するコンストラクタクラスのインスタンスを作成し、
# 要求されるデフォルトのファクトリーモジュールセットのリストを取得。
cm = constructors.ConstructorManager()
m = cm.module(constructor_name) #コンストラクタを格納しているpyモジュール
c = m.Constructor(settings)     #コンストラクタのインスタンス
modulelist = c.FactoryModules

for info in modulelist:
    module_name = info.moduleName()
    dirname = dir_table.get(module_name)
    if not dirname:
        raise RuntimeError(
            'A module {} was not found in default factory modules.'.format(
                module_name
            )
        )
    # 新規でModuleInfoを作成し、その中にデフォルトの書き出し先の名前も格納しておく。
    new_mod = factory.ModuleInfo(module_name, dirname, info.alias(), info.tag())
    # FactoryDataにモジュール情報を追加する。
    settings.addModule(module_name,  new_mod)

# モデル保存用と作業データ保存用ディレクトリを追加する。
for module_name, dirname in c.SpecialModules.items():
    new_mod = factory.ModuleInfo(module_name, dirname, '', '')
    settings.addModule(module_name,  new_mod)

# プロジェクト設定を書き出す。
settings.saveFile()

# プロジェクト設定に基づいて、プロジェクトディレクトリ内にファクトリーモジュールが
# 必用とする書き出し先ディレクトリを作成する。
factory.createFactoryDirectory(settings)

# コンストラクタに用意されているスクリプトのテンプレートを作成する。
cmd, module = cm.getConstructionScriptCmd(constructor_name, True)
cmd(settings, module)