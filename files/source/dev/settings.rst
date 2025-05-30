****************************************************
設定にまつわる機能
****************************************************
settingsモジュールはGRISに関する各種設定を定義します。


.. _ST-globalSettingsXML:

globalSettings.xml
============================
このXMLファイルはGRISの拡張モジュールを検索する際に、
検索するモジュールのプレフィックスとなるPythonパッケージを指定できます。


標準的なフォーマット
----------------------
標準では以下のような内容で記述されています。

.. code-block:: xml
    :linenos:

    <?xml version="1.0" encoding="utf-8" ?>
    <grisPref>
        <constructorPrefix>gris3AddOns.constructors</constructorPrefix>
        <rigUnitPrefix>gris3AddOns.rigUnits</rigUnitPrefix>
        <factoryModules>gris3AddOns.factoryModules</factoryModules>
    </grisPref>


利用可能なタグ
----------------------
タグで指定すると、対応した機能を指定したPythonパッケージの中から検索するようになります。

ここで指定する内容はファイルパスではなく、Pythonパッケージである点にご注意下さい。

.. list-table:: 有効なタグ一覧

    *   - constructorPrefix
        - ここで指定したPythonパッケージの下にカスタムのConstructorモジュールを配置すると,
          コンストラクタとして認識されるようになる。
    *   - rigUnitPrefix
        - ここで指定したPythonパッケージの下にリグユニット用モジュールを配置すると,
          リグモジュールとして認識されるようになる。
    *   - factoryModules
        - ここで指定したPythonパッケージの下にFactoryModuleを配置すると、
          FactoryModuleの一つとしてConstructor内で利用できるようになる。
