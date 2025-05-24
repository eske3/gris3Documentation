****************************************************
命名規則管理システム
****************************************************
データの管理を行う上で名前のルールは非常に重要です。
grisではジョイントやリグ、コントローラを作成する際の命名規則を厳重に管理しています。

命名規則の管理を行うシステムをカスタマイズする事で、独自の命名規則に従ったシステムを構築する事ができます。


.. _NRS-minimumNamingRule:

命名規則の最小限のルール
======================================
命名規則をカスタマイズする事はできますが、必要最低限のルールは存在します。
命名規則管理システムをカスタマイズする上で、以下の要素は必ず意識する必要があります。

+ ベース名（主に名前をつける対象を表す具体的な名前）
+ ノードの種類
+ 位置を表す文字列
+ プレフィックス
+ サフィックス
+ ベース名に追加する特殊文字
+ ネームスペース

命名規則はこれらの要素を組み合わせて作る必要がありますが、
全ての要素を入れる必要はありません。

命名規則を作成する際、上記の要素を`＿`で区切ります。
例えばGrisデフォルトの命名規則では以下のようになります。


    ベース名_ノードの種類_位置を表す文字列

    spineA_jnt_C


命名規則に従った名前の操作と仕組み
=============================================================
NameRuleオブジェクト
------------------------------------
一度girsの命名規則に従った名前の扱い方を、サンプルコードを見ながら見てみましょう。

.. code-block:: python
    :linenos:
    
    from gris3 import func
    n = func.Name('spineA_jnt_C')
    n.name()
    # Result: spineA # 
    n.nodeType()
    # Result: jnt # 
    n.position()
    # Result: C # 
    
    n2 = func.Name('J_C_spineA')
    # Error: ValueError: The given name is not supported : J_C_spineA # 

Name関数に文字列を渡すと、文字列を解析して
:ref:`NRS-minimumNamingRule`
の要素に分解した状態でデータを保持する
**NameRuleオブジェクト**
が返されます。

NameRuleオブジェクトでは各要素に対して
**name**
や
**nodeType**
などの専用メソッドを用いてアクセスする事ができます。

また、命名規則違反の文字列を渡された場合はエラーを返します。


ベース名やノードの種類を置き換える
---------------------------------------------
NameRuleオブジェクトはベース名やノードの種類、
位置を表す文字列などの最小限の要素ごとにアクセスできるだけでなく、
編集を加える事も可能です。

以下のサンプルコードではNameRuleオブジェクト化した後に、
ベース名とノードの種類に変更を加えています。

.. code-block:: python
    :linenos:
    
    from gris3 import func
    n = func.Name('spineA_jnt_C')
    n.setNodeType('jntProxy')
    print(n())
    # Result: spineA_jntProxy_C #
    n.setName('head')
    print(n())
    # Result: head_jntProxy_C #

NameRuleオブジェクトは()を付けて呼び出す事により、
変更後の名前を文字列として返します。

.. _NRS-funcName:

func.Nameの正体
-----------------------------
func.Nameはラッパー関数であり、
実際にNameRuleオブジェクトの生成は別のシステムが担っています。

func.Nameの内部は以下のようになっています。

.. code-block:: python

    def Name(name=''):
        from .system import GlobalSys
        return GlobalSys().nameRule()(name)

Name関数の内部ではsystemモジュールのGlobalSysクラスが呼びだされており、
このクラスがNameRuleオブジェクトを生成して返すようになっています。

GlobalSysクラスはgrisの全体管理を行うシステムクラスです。
このクラスが現在有効となっているNameRuleオブジェクトを返す事により、
システムで作成されるノードの名前を一意のルールで管理する事ができるようになっています。



命名規則管理クラス
===========================
grisでは命名規則を管理するための「
**NameRule**
」オブジェクトが存在しています。、

GlobalSysクラスは
:ref:`NRS-funcName`
で紹介したように、現在有効になっているNameRuleオブジェクトを返しています。

開発者はこのNameRuleオブジェクトをカスタマイズし、
GlobalSysにカスタムNameRuleオブジェクトをセットする事により、
システム全体の命名規則の管理を行う事ができるようになります。


system.AbstractNameRuleクラス
---------------------------------------
このクラスは命名規則の定義を行うための抽象クラスです。
:ref:`NRS-minimumNamingRule`
の要件をベースに名前ルールを定義する事ができるように設計されています。



system.BasicNameRuleクラス
------------------------------------
このクラスはsystem.AbstractNameRuleクラスのサブクラスであり、
grisの基本形となる命名規則を定義、管理するクラスです。
デフォルトではこの命名規則管理クラスによって名前が決定されます。

このクラスでは

* ネームスペース
* ベース名
* ノードの種類
* 位置

で構成される名前をサポートしています。
    **(ネームスペース:)ノード名_ノードの種類(_位置）**
のルールに則った文字列をインスタンス生成時に受け取ると、
解析後、問題なければ各要素に分けて名前を保持します。

問題がある場合はエラーを返します。


.. _NRC-customizeNameRuleClass:

BasicNameRuleクラスをカスタマイズする
==================================================
BasicNameRuleクラスは必要最低限の機能を持った命名管理クラスですが、
プロジェクトによっては必要要素は同じでもベース名やノードの種類名などの位置が違う場合もあります。

.. list-table:: 

    *   - 元の命名規則
        - (ネームスペース:)ノード名_ノードの種類(_位置）
        - 例）spineA_jnt_C
    *   - 新しい命名規則
        - (ネームスペース:)ノードの種類_位置_ノード名
        - 例）J_C_spineA

このような場合、元のBasicNameRuleクラスを継承したサブクラスを作成すると良いでしょう。


命名規則のチェックパターンを編集する
---------------------------------------------
BasicNameRuleクラスには命名規則をチェックするための４つのアトリビュートがあります。

.. list-table:: 

    *   - **アトリビュート名**
        - **デフォルト値**
        - **説明**
    *   - AllNamePattern
        - ^([a-zA-Z][a-zA-Z\d]+:|)([a-zA-Z][a-zA-Z\d]+)_([a-zA-Z\d]+)(?:_([A-Z]+)$|$)
        - 入力文字列チェック用の正規表現
    *   - NamePattern
        - ^[a-zA-Z][a-zA-Z\d]+$
        - ベース名のチェック用正規表現
    *   - TypePattern
        - ^[a-zA-Z\d]+$
        - ノードの種類のチェック用正規表現
    *   - PosPattern
        - '^[A-Z]+$'
        - 位置を表す文字列のチェック用正規表現

これらアトリビュートはすべて正規表現オブジェクトです。

継承したサブクラスでこれらアトリビュートを変更する事により入力文字列のチェックを行う事ができるようになります。

AllNamePatternに使用する正規表現は（）でグループ化し、
後の工程で要素ごとに取り出せるようにする必要があります。


AllNamePatternを各要素に分解する
-----------------------------------------------
上記アトリビュートの変更は、チェック機構の変更を意味します。
変更した後に、AllNamePatternによって返される正規表現オブジェクトを使用して各要素に分解する必要があります。

正規表現オブジェクトから要素の分解を行うにはsetupメソッドを上書きします。

.. code-block:: python

    def setup(self, name, mobj):

引き数mobjはAllNamePatternによって生成された正規表現オブジェクトです。

setupメソッド内では、self.setNameやself.setNodeType、
self.setPositionなどのメソッドを使用して要素として登録します。


分解した要素を任意の順番に置き換える
-----------------------------------------------
setupで分解した要素をそれぞれに登録し終わったら、最後に各要素の順番を変更します。
養素の順番を変更するにはelementsメソッドを上書きします。

.. code-block:: python

    def elements(self):
        return []

BasicNameRuleクラスはelementsで返された文字列のリストを_で結合して返すようになります。


サンプルコード
----------------

.. code-block:: python
    :linenos:

    import re
    from gris3 import system
    class MyNameRule(system.BasicNameRule):
        AllNamePattern = re.compile(
            '^([a-zA-Z][a-zA-Z\d]+:|)([A-Z])_([A-Z])_([a-zA-Z][a-zA-Z\d]+$)'
        )
        NamePattern = re.compile('^[a-zA-Z][a-zA-Z\d]+$')
        TypePattern = re.compile('^[a-zA-Z]')
        PosPattern = re.compile('^[A-Z]')

        def setup(self, name, mobj):
            # 引き数mobjはAllNamePatternのsearchを行った結果の正規表現オブジェクト。
            self.setNamespace(mobj.group(1)[:-1])
            self.setName(mobj.group(4))
            self.setNodeType(mobj.group(2))
            self.setPosition(mobj.group(3))

        def elements(self):
            return [self.nodeType(), self.position(), self.name()]

    MyNameRule('J_C_spineA')
    # Result: J_C_spineA # 


カスタム命名規則管理クラスでキャストできるようにする
===========================================================
命名規則オブジェクトをカスタマイズするメリットとして、
ある命名規則をカスタムした命名規則にキャストする事ができると言う点があります。

命名規則オブジェクトは
**>>**
演算子をサポートしており、
この演算子を使用する事によって名前を別の規則にキャストする事ができます。

:ref:`NRC-customizeNameRuleClass`
でカスタムした命名規則オブジェクトを使用して、gris標準命名規則からキャストを行ってみます。

.. code-block:: python
    :linenos:
    
    from gris3 import system
    s = system.BasicNameRule('spineA_jnt_C')
    d = MyNameRule()
    s >> d
    print(d())
    # Result: jnt_C_spineA # 


キャスト方法を最適化する
------------------------------------
無事キャストが完了し、カスタムした命名規則に変換されました。

しかしカスタムした命名規則はノードの種類を表す文字列を１文字と定義しているため、
キャスト後の名前は正しくありません。

そこでノードの種類を設定するsetNodeTypeメソッドをカスタマイズして、
理想的な名前にキャストできるよう挙動を修正します。

:ref:`NRC-customizeNameRuleClass`
でカスタマイズしたクラスのsetNodeTypeを変更します。

.. code-block:: python
    :linenos:

    import re
    from gris3 import system
    class MyNameRule(system.BasicNameRule):
        AllNamePattern = re.compile(
            '^([a-zA-Z][a-zA-Z\d]+:|)([A-Z])_([A-Z])_([a-zA-Z][a-zA-Z\d]+$)'
        )
        NamePattern = re.compile('^[a-zA-Z][a-zA-Z\d]+$')
        TypePattern = re.compile('^[a-zA-Z]')
        PosPattern = re.compile('^[A-Z]')

        def setup(self, name, mobj):
            # 引き数mobjはAllNamePatternのsearchを行った結果の正規表現オブジェクト。
            self.setNamespace(mobj.group(1)[:-1])
            self.setName(mobj.group(4))
            self.setNodeType(mobj.group(2))
            self.setPosition(mobj.group(3))

        def elements(self):
            return [self.nodeType(), self.position(), self.name()]

        def setNodeType(self, nodeType):
            super(MyNameRule, self).setNodeType(nodeType[0].upper())
            

    s = system.BasicNameRule('spineA_jnt_C')
    d = MyNameRule()
    s >> d
    print(d())
    # Result: J_C_spineA # 

これで無事正しいキャストができるようになりました。