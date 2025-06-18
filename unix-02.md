# UNIXを使ってみよう

前の章では、UNIXシステムの概要について学んだ。この章では、いよいよ実際にUNIXシステムに触れて、基本的なコマンドを使ってみる。コマンド操作は、初めは少し難しく感じるかもしれないが、慣れてくると非常に効率的にコンピュータを操作できるようになる。

## ターミナル

UNIXシステムでコマンドを入力するには、「ターミナル」というアプリケーションを使う。ターミナルは、キーボードから命令（コマンド）を打ち込み操作するためものである。

### ターミナルの起動

* **WSL上のUbuntu**: <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;"><span class="Unicode">⊞</span> Win</kbd> + <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">S</kbd>で検索を起動し、「ubuntu」で検索して「Ubuntu」を起動する。

* **macOS**: Finder <img src="images/macos_finder.png" width="23px" alt="Finder" /> で「アプリケーション」＞「ユーティリティ」＞「ターミナル」と辿ってダブルクリックして起動する。または、Launchpad <img src="images/macos_launchpad.png" width="23px" alt="Launchpad" />で「ターミナル」を検索して起動してもいい。

### プロンプト

ターミナルを起動すると、次のような画面が表示される。

**WSL上のUbuntu**
```sh
ユーザー名@コンピュータ名:~$
```

```sh
(仮想環境名) ユーザー名@コンピュータ名:~$
```

**macOS**
```sh
ユーザー名@コンピュータ名 ~ %
```

```sh
(仮想環境名) ユーザー名@コンピュータ名 ~ %
```

これらの表示を「**プロンプト**（prompt）」と呼ぶ。プロンプトは、「入力促進記号」と呼ばれ、「コマンドを入力してください」というシステムからのメッセージである。このプロンプトに続けて、様々なコマンドを入力していく。

なお、プロンプトはデフォルトでは、WSL上のUbuntuは「`$`」、macOSは「`%`」と表示される。プロンプトの表示はカスタマイズ可能だが、ここでは基本的な表示で説明を進める。

## 演習の準備

**WSL上のUbuntu** ※最初に一回だけ実行

```sh
sudo apt install ncal
```
※パスワードを聞かれた場合、入力する（打っても見えない）

**macOS** ※「`cal`」「`date`」を使う前に実行

```
unset LANG
```

## カレンダーの表示: `cal`

では、プロンプトに対して、次のように「`cal`」と打ち込んでみよう。UNIX システムでは、大文字と小文字は区別されるので、このコマンドは全部小文字で打つこと。

すると、今月のカレンダーが表示される。UNIXのコマンドは英語を省略したものが多いと書いたが、「`cal`」は「**cal**endar (カレンダー)」を省略したものだ。

```sh
cal
     April 2025       
Su Mo Tu We Th Fr Sa  
       1  2  3  4  5  
 6  7  8  9 10 11 12  
13 14 15 16 17 18 19  
20 21 22 23 24 25 26  
27 28 29 30    
```

## コマンド入力の基本とトラブルシューティング

コマンド入力に慣れないうちは、いくつか戸惑うことがあるかもしれない。よくあるケースと対処法を覚えておこう。

* **大文字・小文字の区別**: UNIXコマンドやファイル名では、大文字と小文字は厳密に区別される。
「`cal`」を「`Cal`」や「`CAL`」と入力しても正しく動作しない。
* **入力ミス**: タイプミスは誰にでもある。<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Enter</kbd>キーを押す前であれば、左右キーで前後したり、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Delete</kbd>や<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Backspace</kbd>キーで消すことができる。入力を中断するには <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">c</kbd> (コントロールキーを押しながらcキー)である。

**WSL上のUbuntu**
```sh
cak
Command 'cak' not found, did you mean:
...
```

**macOS**
```sh
cak
zsh: command not found: cak
```

* **コマンドが反応しない・暴走した？**: 意図しないコマンドを実行したり、プログラムが応答しなくなったりときには、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">c</kbd> を押してみる。これは実行中のコマンドを強制的に中断する操作で、多くの場合これでプロンプトが表示される。

## `cal`の引き数

もう少し高度な「`cal`」コマンドの使い方を紹介しよう。
「`cal`」コマンドでは、好きな年月のカレンダーを表示させることができる。「`cal 5 2025`」というふうに月と年を指定して、実行してみよう。

次のように、2025年の5月のカレンダーが表示される。

```sh
cal 4 2025
     April 2025       
Su Mo Tu We Th Fr Sa  
       1  2  3  4  5  
 6  7  8  9 10 11 12  
13 14 15 16 17 18 19  
20 21 22 23 24 25 26  
27 28 29 30    
```

今度は、「月」を省略して、「`cal 2025`」と打ってみよう。
次のように2025年のカレンダーが表示されるはずだ。ただし、画面が小さい場合、最初の部分は流れてしまって、後ろの方の部分だけが画面に残る。
長い出力を1画面ずつ表示させるには、ページャーというプログラムを使う。ページャーについては、後ろの章で紹介する。

```sh
cal 2025
                            2025
      January               February               March
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
          1  2  3  4                     1                     1
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   2  3  4  5  6  7  8
12 13 14 15 16 17 18   9 10 11 12 13 14 15   9 10 11 12 13 14 15
19 20 21 22 23 24 25  16 17 18 19 20 21 22  16 17 18 19 20 21 22
26 27 28 29 30 31     23 24 25 26 27 28     23 24 25 26 27 28 29
                                            30 31

[中略]

      October               November              December
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
          1  2  3  4                     1      1  2  3  4  5  6
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   7  8  9 10 11 12 13
12 13 14 15 16 17 18   9 10 11 12 13 14 15  14 15 16 17 18 19 20
19 20 21 22 23 24 25  16 17 18 19 20 21 22  21 22 23 24 25 26 27
26 27 28 29 30 31     23 24 25 26 27 28 29  28 29 30 31
                      30
```

ひとまず、ここまでのところをまとめよう。「`cal`」コマンドは次のように使う。

```sh
cal 「月」「年」
```

ここで、「年」は西暦で指定する。「月」を省略すると、「年」で指定した年の1 年分のカレンダーが出る。「月」も「年」も省略すると、今月のカレンダーが出る。

この「`cal`」コマンドの「月」や「年」のように、コマンドの後ろに付けて細かい指定をするのに使うものを、「引き数（ひきすう） argument」と言う。
これはプログラミングの本や、マニュアルなどでもよく使う用語なので、おぼえておこう。

### 練習
1. 自分の生まれた日が何曜日だったか調べてみよう。
2. 友だちの生まれた日が何曜日だったか調べてみよう。
ちなみに、平成12年が西暦2000年といったように、平成の年数から12を引くと西暦の下2ケタになる。また、令和の場合は18を足す。

## 日時を表示する: `date`

「`date`」コマンドは、現在の日付と時刻を表示する。
「`date`」コマンドに以下のようなオプションを付けて実行してみよう。

```sh
date "+%a %b %d %T %Z %Y"
Mon Apr 14 14:50:52 JST 2025
```

「`date`」コマンドのオプションでは、表示形式を細かく指定できる。
オプションは「`+`」に続けて書式指定文字を記述する。
例えば、「`"+%Y-%m-%d %H:%M:%S"`」というオプションを付けると、「`年-月-日 時:分:秒`」の形式で表示される。これはプログラムで日時を扱う際などによく使われる形式である。

曜日（`unset LANG`を実行したmacOSでは英語表記）やタイムゾーン（地域ごとの標準時の設定）を含めて表示することもできる。

```sh
date "+%Y年%m月%d日 %H時%M分%S秒 %Z"
2025年04月14日 14時53分15秒 JST
```

主な書式指定文字：
* `%Y`: 西暦年 (4桁)
* `%m`: 月 (01-12)
* `%d`: 日 (01-31)
* `%A`: 曜日名 (例: Sunday, Monday, ..., 日曜日, 月曜日, ...)
* `%a`: 短縮された曜日名 (例: Sun, Mon, ..., 日, 月, ...)
* `%H`: 時 (00-23)
* `%M`: 分 (00-59)
* `%S`: 秒 (00-59)
* `%Z`: タイムゾーン名 (例: JST, UTC)

## ログインしているユーザーを表示する: `who`

「`who`」コマンドは、現在そのコンピュータにログインしているユーザーの一覧を表示する。UNIXシステムは複数のユーザーが同時に利用できるため、このようなコマンドがある。

**WSL上のUbuntu**

```sh
who
kokubo   pts/1        2025-04-14 11:02
```

**macOS**

```sh
who
kokubo           console       4 14 11:29  
kokubo           ttys001       4 14 11:32
```

表示内容は、ユーザー名、利用している端末（`console`や`ttys001`など）、ログイン日時、接続元IPアドレス（リモート接続の場合）などである。

また、「`whoami`」(who am i) というコマンドは、現在操作しているユーザー自身の名前を表示する。

```sh
whoami
ここにユーザー名が表示
```

## Webページの内容を取得する: `curl`

「`curl`」（カール）は、指定したURLからデータを取得するコマンドである。Webページの情報を取得したり、ファイルをダウンロードしたりするのに使える。例えば、[天気情報サイト](https://learn.microsoft.com/ja-jp/connectors/wttrin/)の情報を見てみよう。

```ssh
curl -s "https://wttr.in/Tokyo?format=%l:+%c+%t"
Tokyo: ☀️ +25°C
```

「`curl`」の「`-s`」オプションは、進捗表示などを省略して結果のみを表示する指定である。
「`curl`」は非常に多機能で、Web APIを利用する際などにも強力なツールとなる。

例のようにURLに「`wttr.in`」を指定した場合、「`Tokyo`」の部分を「`Osaka`」や「`London`」など、他の都市名に変えて試してみるとそれぞれの天気を表示することができる。

## 文字列を表示する: `echo`

「`echo`」コマンドは、指定した文字列を画面に表示するシンプルなコマンドである。メッセージを表示したり、他のコマンドと組み合わせて使ったりする。

```sh
echo "こんにちは、UNIXの世界へようこそ！"
こんにちは、UNIXの世界へようこそ！
```

## コマンド操作で困ったときの対処法まとめ

コマンド操作中に困ったときの対処法を改めて整理しておく。

1. **入力ミス・修正**: <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Enter</kbd>キーを押す前なら<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">←</kbd> や <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">→</kbd>キーで移動し、 <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Delete</kbd> や <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Backspace</kbd> で消して修正できる。入力を取り止めたい場合は <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">c</kbd>。
2. **「`Command not found`」**: コマンドのスペルミスがないか確認。ミスがなくてもダメな場合、コマンドがインストールされていない可能性もある。
3. **コマンドが暴走・応答なし**: <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">c</kbd> で強制中断。
4.  **画面の表示が乱れた (文字化けなど)**: ターミナルの表示がおかしくなった場合は、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">l</kbd> (小文字のL) で画面をクリアできる。
5. **コマンド実行後、プロンプトが出ない**: GUIアプリケーションなどを起動した際に、ターミナルがそのアプリケーションの終了を待っている状態になることがある。その場合は、アプリケーションを終了させるか、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">z</kbd> で一時停止し「`bg`」コマンドでバックグラウンド実行に切り替えるなどの対処がある（詳細は後の章で）。
6. **対話型プログラムの終了方法**: <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">d</kbd> (ファイルの終わりを意味する) で終了できるプログラムが多い。プログラムによっては「`quit`」や「`exit`」と入力して終了するものもある。

例えば、「`bc`」という電卓コマンドを起動してみよう。

**WSL上のUbuntu**
```sh
bc
bc 1.07.1
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006, 2008, 2012-2017 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
1+2+3
6
```

※最後に終了させるために、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">d</kbd>を打っているが見えない。

**macOS**
```sh
bc
>>> 1+2+3
6
>>> ^D
```
※最後に終了させるために、<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">d</kbd>を打っていて、こちらでは「`^D`」と表示される。

## この章で学んだコマンド

| コマンド | 説明                                 | 主な使い方                           | 例                               |
| :------- | :----------------------------------- | :----------------------------------- | :------------------------------- |
| `cal`    | カレンダーを表示                     | `cal [月] [日]]`                     | `cal 5 2025`                     |
| `date`   | 現在の日付と時刻を表示                 | `date ["+書式"]`                   | `date "+%Y-%m-%d"`               |
| `who`    | ログインしているユーザーの一覧を表示 | `who`                                | `who`                             |
| `whoami` | 現在操作しているユーザー名を表示     | `whoami`                             | `whoami`                          |
| `curl`   | URLを指定してデータを取得            | `curl [オプション] "URL"`            | `curl -s "https://wttr.in/Tokyo"` |
| `echo`   | 指定した文字列を画面に表示           | `echo "文字列"`                      | `echo "Hello"`                    |
| `bc`     | コマンドライン電卓（対話型）を起動   | `bc`  (終了は `quit` または <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">d</kbd>)| `bc`                              |
