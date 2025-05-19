# WWW と電子メール

もともと、 WWW (World Wide Web) は UNIX の世界を中心に広まったものだ。
この章では Netscape Communicator などを使って WWW と電子メールの
使い方を紹介しよう。

## Web ブラウザいろいろ

UNIX にはいろいろな Web ブラウザがある。
はじめて画像を表示することができた Mosaic、 Netscape の各種バージョン、
テキスト・ベースの Lynx、試験的に作られた Arena、 HTML エディタと Web
ブラウザが融合した Amaya、 最近脚光を浴びている Opera。

::: minipage
<figure>

<figcaption>XMosaic</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Netscape 3</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Netscape 6</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Mozilla</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>lynx</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Arena</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Amaya</figcaption>
</figure>
:::

::: minipage
<figure>

<figcaption>Opera</figcaption>
</figure>
:::

今回は、これら Web ブラウザのうち Netscape Communicator (ver. 4
系)、それから w3m について紹介する。

## Netscape Communicator の使い方

現在、 UNIX の世界で一番メジャーだと思われるブラウザが Netscape
Communicator である。

Netscape は、 UNIX の場合、完全に個人で環境設定でき、
ブックマークの使用も問題なくできる。

### 起動

まず、 Netscape Communicator を起動するには、 `netscape`
というコマンドを入力する。

::: progls
:::

すると、ウィンドウが次々と開いて図 [1.1](#nsstart){reference-type="ref"
reference="nsstart"} のような画面になる。

<figure id="nsstart">

<figcaption>Netscape Communicator の起動直後</figcaption>
</figure>

### 使用許諾条件

使用許諾条件が表示される。 これを受け入れる場合にのみ使用できる。
受け入れるならば、 をクリックする。

<figure>

</figure>

### 初回起動時メッセージ

メッセージがいくつかでて、 Netscape が起動する。

<figure>

</figure>

しばらくすると、 Netscape 社のページに接続しようとして動きはじめる。
しかし、設定が済んでいないうちは接続できないので、「停止」
ボタンを押して止める。

<figure>

</figure>

キャッシュを作成した等のメッセージは をクリックして閉じる。

<figure>

</figure>

<figure>

</figure>

### 設定

Netscape の設定を行う。
まず、メニュー・バーの「編集」から「設定」を選ぶ。

<figure>

</figure>

#### プロキシの設定(必須)

最初にプロキシの設定を行う。
まず、画面左側に出ている「カテゴリ」の中の「詳細」を開く。
これを開くには、左側にある「△」のマークをクリックすればよい。

次に現われたサブ・メニューの中から「プロキシ」を選択する。

画面右側に移って「手動でプロキシを設定する」の左側のチェック・ボックスを
クリックしてチェックする。
その後、すぐ右側にある「表示」をクリックする。

<figure>

</figure>

現われたウィンドウの「HTTP
プロキシ」に「`cache.edu.aomori-u.ac.jp`」を、
そのポートに「`8080`」を指定する。 その後で「確認」をクリック。

<figure>

</figure>

#### 起動時に表示するページの設定

画面左側の \[Navigator\] メニューをクリックする。
次に、画面右側の「ホーム ページ」の「場所」の部分に、
起動時に表示したいページの URL を指定する。
たとえば「`http://www.aomori-u.ac.jp/`」など。
もしも、起動時に空白ページを表示したい場合には、
「ブラウザの開始時」の「空白ページ」を選択しておく。

<figure>

</figure>

#### メールの設定

**個人情報**

画面左側の \[メール と ニュース\] の左の△をクリックして開き、 その中の
\[個人情報\] を選択する。

画面右側に現われたダイアログに「名前」をローマ字などで、 「電子メール
アドレス」には 「`ei0X0XX@` `edu.aomori-u.ac.jp`」など自分のものを、
「組織」にはたとえば「Dept. Info. Sys. Eng., Aomori
Univ.(青森大学情報システム工学科)」などを入力する。

<figure>

</figure>

**メール サーバ**

画面左側の \[メール と グループ\] の \[メール サーバ\] を選択する。

<figure>

</figure>

画面右側の「受信メール サーバ」から「`pop`」を選択し、
「編集」をクリックする。

<figure>

</figure>

現われたダイアログの「全般」タブを選択する。
「サーバ名」に「`msedu0.edu.aomori-u.ac.jp`」を指定する。
「ユーザ名」に「`ei0X0XX`」など、自分のものを指定する。
ほかのオプションも好みで設定していいだろう。

<figure>

</figure>

今後、基本的には常に FreeBSD 側でメールを読もうという人以外
[^1]は、サーバにメールを残す ように設定をしておこう。
まず、「POP」タブを選択する。
現われたダイアログの「サーバにメッセージを残す」にチェックを入れる。
後は、「確認」をクリックする。

<figure>

</figure>

「送信メール サーバ」に「`msedu0.edu.aomori-u.ac.jp`」を指定する。

<figure>

</figure>

#### ネットニューズの設定

Netscape でネットニューズを読もうという人だけ以下の設定を行う。

まず、画面左側の \[メール と グループ\] の \[グループ サーバ\]
を選択する。

<figure>

</figure>

次に画面右側から「追加」をクリックする。

<figure>

</figure>

「サーバ」に「`news0.mono.aomori-u.ac.jp`」を指定し、
「確認」をクリック。

<figure>

</figure>

すると、新たに「`news0.mono.aomori-u.ac.jp`」が現われているので
これを選択し、 「標準に設定」をクリック。

<figure>

</figure>

「`news0.mono.aomori-u.ac.jp`」が 「標準設定」になった。

次には、「`news`」を選択し、 「削除」をクリックする。

<figure>

</figure>

「ニュース サーバ `news` とそのすべてのニュースグループを
削除してもよいですか？」と聞かれるが、 「確認」をクリックして削除する。

<figure>

</figure>

#### 設定終了

すべての設定が終了したら、画面左下の「確認」をクリックする。

<figure>

</figure>

### ホーム ページの表示

「ホーム」をクリックすると、「ホーム ページ」に指定した URL
が表示される。

<figure>

</figure>

### Netscape の操作

Netscape の操作は、基本的にメニューのボタンと「場所」ダイアログの 2
つで行える。

まず、メニューの方は、以下のようになっていて、非常に直感的に構成
されている。 ほとんど説明する必要はないと思われるので、割愛する。

<figure>

</figure>

それから、「場所」ダイアログ・ボックスには、直接 URL
を入力することができ、 入力して することでページを表示させられる。

<figure>

</figure>

### Netscape で日本語入力

たとえば、検索エンジンなどのページで、
ダイアログ・ボックスに日本語を入力し、 検索を実行したくなることがある。
Netscape では[^2]、 XIM プロトコルを通じて `kinput2` というソフトを
使って日本語入力を使用することができる。

`kinput2` による日本語入力の on / off は、 + である。 日本語変換には
Mule と同様に Canna が使われている。 on / off が、この場合は +、 Mule
の場合は「`c-o`」ということ以外はほとんど同じ操作である。

<figure>

</figure>

### Netscape でメールを使う

#### Netscape Messenger の起動

Netscape でメールを使うには、メニューバーの「Communicator」から
「Messenger メールボックス」を選択する。

また、「`netscape &`」の代わりに「`netscape -mail &`」
として起動すると、最初からメール・モードで立ち上がる。

<figure>

</figure>

Netscape Messenger が起動する。

<figure>

</figure>

#### メールを書く

メールを書くには「新規作成」をクリックする。

<figure>

</figure>

「メッセージの作成」ウィンドウが開く。
宛先「`To:`」にメール・アドレスを、 「`件名:`」(`Subject:`)に題名を、
そして本文を記入する。
メールが書きあがったら「送信」ボタンをクリックすると送信される。
なお、日本語入力は、 `kinput2` によるもので、 + で on / off である。

<figure>

</figure>

#### メールを読む

メールを読むには「取り込み」をクリックする。

<figure>

</figure>

すると、メールのパスワードを聞かれるので、ダイアログ・ボックスに入力して、
「確認」をクリックする。

<figure>

</figure>

メールが届いていると、メールをサーバから読み出し、
一覧が画面の右側に表示される。
この一覧からメールを選ぶと、すぐ下の部分に表示される。

<figure>

</figure>

## テキスト・ブラウザ w3m

w3m は伊藤彰則さんの作られたテキスト・ブラウザだ。
このブラウザは、最近のバージョンは画像も表示可能だが、
元々は基本的に文字だけで Web ページを表示するものだった。
文字の表示だけだと、非常に高速に Web ページを表示することが可能になり、
ストレスなく Web ブラウジングが可能になる。

起動するには、次のようにする。

::: progls
:::

すると、次のような画面になって、 w3m が起動する。 使い方は、基本的に
`jless` などのページャーと同様である。

::: progls
[Welcome to w3m!]{style="color: blue"}

[This is w3m version
w3m/0.2.3.2+cvs-1.196-img-1.17]{style="color: blue"} [Written by Akinori
Ito]{style="color: blue"}

[[≪↑↓Viewing \<W3M startup
page\>]{style="color: white"}]{style="background-color: black"}
:::

Web ページを見るには次のようにする。 まず、「`U`」と打つ。
すると、画面一番下に URL を入力できるようになる。

::: progls
Goto URL:
:::

ここにたとえば、 `http://www.aomori-u.ac.jp/` などの URL を指定して
する。

::: progls
Goto URL:
:::

すると、下の図のように、画像まで読み込んでページを表示してくれる。

<figure>

<figcaption>w3m の画面</figcaption>
</figure>

カーソルの移動やコマンドは、次のようになっている。

::: center
  **コマンド**   **動作**
  -------------- --------------------
                 ひとつ前の行へ
                 ひとつ次の行へ
                 一文字前に
                 一文字後ろに
                 次のリンクの位置へ
                 下の画面へ
  b              上の画面へ
                 左の画面へ
                 右の画面へ
  J              一行上にスクロール
  K              一行上にスクロール
  /「文字」      前方サーチ
  ?「文字」      後方サーチ

  : カーソルの移動
:::

::: center
  **コマンド**   **動作**
  -------------- ----------------------------------------
  q              終了
  リンクの上で   リンク先へ飛ぶ
  B              前のページにもどる
  U              URL を指定する
  v              ページのソースを表示(表示を戻すには B)
  M-b            ブックマークの表示
  M-a            ブックマークへの追加
  o              オプションの設定
  H              ヘルプの表示

  : さまざまなコマンド
:::

w3m では、画像がそのまま表示されるが、
これはむしろ表示しない方がブラウザの動作はスムーズだ。
もしも、表示しないように設定したければ、
「`o`」と入力してオプションを表示してみよう。

この画面を下にスクロールすると、「インライン画像を表示」という
オプションがある。 「`OFF`」の前の「`( )`」で を入力し、
チェックを入れる。

::: progls
インライン画像を表示 ( )ON ([\*]{style="color: red"})OFF
:::

そして「[`[OK]`]{style="color: red"}」の上で する。
今度は、さきほど見ていたページが文字データとして表示される。

::: progls
[青森大学・青森短期大学]{style="color: green"}
[\[t\]]{style="color: green"} [\* カット]{style="color: green"}
[\*]{style="color: green"} [大学院]{style="color: green"} [What's
New]{style="color: green"} [経営学部]{style="color: green"}
[\*]{style="color: green"} [\*]{style="color: green"}
[経営学科／産業デザイン学科]{style="color: blue"}
[メッセージ]{style="color: green"} [社会学部]{style="color: green"}
[\*]{style="color: green"} [\*]{style="color: green"}
[社会学科／社会福祉学科]{style="color: blue"}
[入試情報]{style="color: green"} [工学部]{style="color: green"}
[\*]{style="color: green"} [\*]{style="color: green"}
[電子システム工学科／情報システム工学科／生物工学]{style="color: blue"}
[大学案内]{style="color: green"} [青森短期大学]{style="color: green"}
[\*]{style="color: green"} [\*]{style="color: green"}
[商経科第一部／商経科第二部]{style="color: blue"}
[キャンパスニュース]{style="color: green"} [\*]{style="color: green"}
[トピックス]{style="color: green"} [サイトマップ]{style="color: green"}
[\*]{style="color: green"} [\*]{style="color: green"} ◆
[青森大学工学部創立10周年記念講演会(第11回青森大]{style="color: blue"}
[リンク集]{style="color: green"}
[月12日(土)13:30より、青森大学メモリアルホールで]{style="color: blue"}
[場は無料です。]{style="color: blue"} ◆
[出張講義のページをリニューアルしました。随時受付]{style="color: blue"}
[ご利用ください。]{style="color: blue"} ◆
[青森大学・青森短期大学オープンキャンパスへ参加し]{style="color: blue"}
[３回オープンキャンパスは９月21日(土)です。]{style="color: blue"} ◆
[本学図書館新館2階展示資料室にて「没後90年石川啄]{style="color: blue"}
[催中です(〜9/20迄)。]{style="color: blue"} [[≪↑↓Viewing
\<青森大学・青森短期大学\>]{style="color: white"}]{style="background-color: black"}
:::

この状態だと、いろいろなページを高速に表示することができて非常に便利である。
このように、絵を見たい場合、文字を高速に表示したい場合、
それぞれに合わせて適切なブラウザを選択しよう。

## この章で紹介したコマンド {#この章で紹介したコマンド .unnumbered}

::::: center
:::: minipage
::: itembox
WWW 関連コマンド他

`netscape` :

:   Netscape Communicator

    使い方: `netscape &`    Netscape Communicator 起動

               `-mail` オプションをつけるとメール・モードで起動

`w3m` :

:   テキスト・ベース Web ブラウザ

    使い方: `w3m -v`          w3m 起動
:::
::::
:::::

[^1]: たとえば、基本的には Windows でメールを読む。 FreeBSD
    側はサブで使うという人

[^2]: 正確には Netscape に限らず、 X Windows System
    のアプリケーション一般も同様
