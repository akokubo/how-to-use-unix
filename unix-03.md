# ファイルとディレクトリの基本操作

前の章では、ターミナルを開いて最初のUNIXコマンドを実行する方法を学んだ。この章では、UNIXシステムにおけるファイルとディレクトリの基本的な操作方法について解説する。

UNIXシステムでは、情報は「ファイル」という単位で保存され、ファイルは「ディレクトリ」（WindowsやmacOSでの「フォルダ」に相当する）という入れ物を使って階層的に整理される。この階層構造は、木の枝が分かれていく様子に似ているため、「ツリー構造」とも呼ばれる。ただし、木は上下逆さまに描いたようになっている。

この章では、具体的に以下の3つのコマンドの使い方を学ぶ。

* 現在自分が作業しているディレクトリを確認する `pwd` (ピーダブルディー)
* ファイルやディレクトリの一覧を表示する `ls` (エルエス)
* ディレクトリを移動する `cd` (シーディー)

これらのコマンドは、UNIXシステムを操作する上で最も基本的かつ重要なものであるため、しっかりと習得しよう。

## 現在の場所を確認する: `pwd`

UNIXシステムでは、自分が今どこのディレクトリで作業しているのかを正確に把握することが非常に重要である。「`pwd`」コマンドは「**p**rint **w**orking **d**irectory」（現在の作業ディレクトリを表示する）の略であり、これを実行すると、現在いるディレクトリの「絶対パス」が表示される。

絶対パスとは、ファイルシステムの階層構造の一番上である「ルートディレクトリ」（記号 `/` で表される）から始まり、目的のディレクトリに至るまでの全てのディレクトリ名をスラッシュ `/` で区切って並べたものである。ちょうど、住所で「東京都 千代田区 ...」と大きな単位から順に示すのに似ている。

ターミナルで `pwd` と入力して実行してみよう。

**WSL上のUbuntu**
```sh
pwd
/home/kokubo
```

**macOS**
```sh
pwd
/Users/kokubo
```

WSL上のUbuntuでは、`/home/ユーザー名` というパスが表示されている。これは、ルートディレクトリ `/` の中の `home` ディレクトリ、その中の `ユーザー名` ディレクトリに現在いることを示している。

macOSでは、`/Users/ユーザー名` というパスが表示され、ルートディレクトリ `/` の中の `Users` ディレクトリ、その中の `ユーザー名` ディレクトリに現在いることを示している。

このように、`pwd` コマンドを使うことで、いつでも自分が現在いる場所を正確に確認できる。

## ファイルやディレクトリの一覧を見る: `ls`

「`ls`」コマンドは「**l**i**s**t directory contents」（一覧）の略であり、指定したディレクトリにあるファイルやサブディレクトリの一覧を表示する。ディレクトリを指定しなかった場合、現在いるディレクトリの中の一覧を表示する。

```sh
ls
現在いるディレクトリの中が表示される
```

```sh
ls /
一番上のルートディレクトリの中が表示される
```


### `ls` コマンドの便利なオプション

`ls` コマンドには、表示形式を変えたり、より詳しい情報を表示させたりするための様々な「オプション」がある。オプションは、コマンド名の後にスペースを空けて、ハイフン `-` などに続けて指定する。

#### 詳細表示: `-l` オプション

「`-l`」オプション（long format）を付けて `ls -l` と実行すると、ファイルやディレクトリの詳細情報が表示される。具体的には、パーミッション（アクセス権限）、所有者、サイズ、最終更新日時などが含まれる。

**WSL上のUbuntu**
```sh
ls -l /
total 10
total 10
drwxrwxr-x  178 root  admin  5696  5  8 08:58 Applications/
drwxr-xr-x@  39 root  wheel  1248  4 12 14:16 bin/
drwxr-xr-x    2 root  wheel    64 10 22  2024 cores/
dr-xr-xr-x    4 root  wheel  4724  5  7 07:41 dev/
…
```

**macOS**
```sh
ls -l /
total 10
drwxrwxr-x  178 root  admin  5696  6 11 13:12 Applications/
drwxr-xr-x@  39 root  wheel  1248  5  4 14:39 bin/
drwxr-xr-x    2 root  wheel    64 10 22  2024 cores/
dr-xr-xr-x    4 root  wheel  4800  6 11 13:11 dev/
lrwxr-xr-x@   1 root  wheel    11  5  4 14:39 etc@ -> private/etc
lrwxr-xr-x    1 root  wheel    25  6 11 13:11 home@ -> /System/Volumes/Data/home
drwxr-xr-x   79 root  wheel  2528  5 13 13:27 Library/
drwxr-xr-x    5 root  wheel   160  3 24 09:46 opt/
drwxr-xr-x    6 root  wheel   192  6 11 13:11 private/
drwxr-xr-x@  76 root  wheel  2432  5  4 14:39 sbin/
drwxr-xr-x@  10 root  wheel   320  5  4 14:39 System/
lrwxr-xr-x@   1 root  wheel    11  5  4 14:39 tmp@ -> private/tmp
drwxr-xr-x    8 root  admin   256  5 21 11:28 Users/
drwxr-xr-x@  11 root  wheel   352  5  4 14:39 usr/
lrwxr-xr-x@   1 root  wheel    11  5  4 14:39 var@ -> private/var
drwxr-xr-x    5 root  wheel   160  6 11 14:40 Volumes/
```

各項目の意味は以下の通りである。
*   1列目: ファイルの種類とパーミッション（アクセス権限）。最初の文字が `d` ならディレクトリ、`-` ならファイルである。パーミッションの詳しい見方については、後の章で改めて解説する。
*   2列目: ハードリンクの数
*   3列目: 所有者名
*   4列目: グループ名
*   5列目: ファイルサイズ（バイト単位）
*   6,7,8列目: 最終更新日時
*   9列目: ファイル名またはディレクトリ名

最初の文字が `d` であればディレクトリ、`-` であればファイルを示す。

#### 隠しファイルも表示: `-a` オプション

UNIXシステムでは、ファイル名の先頭がドット `.` で始まるファイルやディレクトリは「隠しファイル」または「不可視ファイル」と呼ばれ、通常の `ls` コマンドでは表示されない。これらは主にシステムの設定ファイルや、アプリケーションが内部的に使用するファイルなどである（例: `.zshrc`, `.bash_profile`, `.gitconfig`, `.DS_Store` など）。これらも表示するには、「`-a`」オプション（all）を使う。
```sh
ls -a ~
.
..
.alias
.bash_history
.bash_profile
.bash_profile
.bash_sessions
.bashrc
.cache
…
```
`.` はそのディレクトリ、`..` はその一つ上の親ディレクトリを指す特殊なディレクトリ名である。これらも隠しファイルと同様に `.` で始まるため、`-a` オプションで表示される。

#### ファイルの種類を記号で表示: `-F` オプション

「`-F`」オプション（classify）を付けると、ファイルの種類を示す記号が名前の後ろに表示される。
*   ディレクトリ: `/`
*   実行可能ファイル: `*`
*   シンボリックリンク: `@`

```sh
ls -F /
Applications/   dev/            Library/        sbin/           Users/          Volumes/
bin/            etc@            opt/            System/         usr/
cores/          home@           private/        tmp@            var@
```

オプションは組み合わせて使うこともできる。例えば、隠しファイルを含めた詳細情報を、ファイルの種類を示す記号付きで表示したい場合は `ls -laF` のように指定する。これは非常によく使われる組み合わせである。

## ディレクトリを移動する: `cd` コマンド (シーディー)

「`cd`」コマンドは「**c**hange **d**irectory」（ディレクトリを変更する）の略であり、別のディレクトリに移動する、つまり作業ディレクトリを変更するために使う。
```sh
cd 「移動先のディレクトリ名」
```

たとえば、 `/etc` というディレクトリへ移動したい場合は、次のように入力する。
なお、 `/etc` にはシステムの設定ファイルが入っている。

```sh
pwd
/home/ユーザー名 あるいは /Users/ユーザー名
```
```sh
cd /etc
pwd
/etc
```
`pwd` コマンドで確認すると、現在のディレクトリが `/etc` に変わっていることがわかる。

### 特殊なディレクトリ名

`cd` コマンドでは、いくつかの特殊なディレクトリ名がよく使われる。これらを覚えると、ディレクトリ移動が格段に楽になる。

*   **`.` (ドット1つ)**: 現在のディレクトリを指す。つまり、 `cd .` と打っても何も変わらない。
*   **`..` (ドット2つ)**: 一つ上の親ディレクトリを指す。例えば、`/Users/ユーザー名` にいるときに `cd ..` とすると、`/Users` に移動する。

    ```sh
    pwd
    /home/ユーザー名 あるいは /Users/ユーザー名
    ```
    ```sh
    cd ..
    pwd
    /home あるいは /Users
    ```
*   **`~` (チルダ)**: ホームディレクトリを指す。ホームディレクトリとは、ユーザーがログインしたときに最初に入るディレクトリのことである。どのディレクトリにいても、`cd ~` または単に `cd` と入力するだけでホームディレクトリに戻ることができる。

    ```sh
    pwd
    /etc
    ```
    ```sh
    cd ~
    pwd
    /home/ユーザー名 あるいは /Users/ユーザー名
    ```
    ```sh
    cd
    pwd
    /home/ユーザー名 あるいは /Users/ユーザー名
    ```
*   **`/` (スラッシュ)**: UNIXシステムの階層構造の一番上である、ルート（根っこ）ディレクトリを指す。`cd /` とすると、ルートディレクトリに移動する。

    ```sh
    pwd
    /home/ユーザー名 あるいは /Users/ユーザー名
    ```
    ```sh
    cd /
    pwd
    /
    ```

### 絶対パスと相対パス

ディレクトリを指定する方法には、「絶対パス」と「相対パス」の2種類がある。どちらを理解することも重要である。

*   **絶対パス (Absolute Path)**: 一番上のルートディレクトリ `/` から始まる完全なパスを指定する方法である。例えば、`cd /usr/bin` のように指定する。現在の場所に関わらず、場所を同じパスで指し示すことができる。
*   **相対パス (Relative Path)**: 現在のディレクトリを基準としたパスを指定する方法である。例えば、現在 `/home/ユーザー名` にいて、その中にある `test` ディレクトリに移動したい場合、`cd test` と指定する。これは相対パスである。また、`cd ../taro` のように `..` を使って親ディレクトリを経由することもできる。

絶対パスは最初が `/` からはじまり、そうでなければ相対パスである。

どちらを使うかは状況によるが、一般的に、現在地から近い場所へ移動する場合は相対パスが、遠い場所や特定の決まった場所へ移動する際には絶対パスが便利である。

### タブ補完：入力の手間を省き、ミスを防ぐ強力な味方

ディレクトリ名やファイル名を入力する際に、途中まで入力して <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Tab</kbd> キーを押すと、残りの部分を自動で補完してくれる機能がある。これを「タブ補完」と呼ぶ。これはUNIXのシェルが提供していて、コマンド入力を簡単にする非常に強力で便利な機能である。

例えば、 `/` に `e` ではじまるディレクトリが `/etc` しかない場合、`cd /e` まで入力して <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Tab</kbd> キーを押すだけで `cd /etc/` と補完される。もし `etc` 以外にも、 `export` のように `e` で始まるものが他にもある場合、`cd /e` で <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Tab</kbd> を押すと、共通部分まで補完されるか、あるいは何も変わらず、もう一度 <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Tab</kbd> を押すと候補の一覧が表示される。

タブ補完を積極的に使うことで、長い名前を正確に入力する手間が大幅に減り、タイプミスによるエラーも劇的に少なくなる。ぜひ習慣づけよう。

## 新しいディレクトリを作成する: `mkdir` コマンド (メイクディレクトリー)

ファイルやディレクトリを整理する際には、新しいディレクトリを作成する必要がある。そのためのコマンドが `mkdir` (「**m**a**k**e **dir**ectory」の略) である。

使い方は簡単で、`mkdir` の後に作成したいディレクトリ名を指定する。

```sh
mkdir 新しいディレクトリ名
```

例えば、現在のディレクトリに `unix_practice` という名前のディレクトリを作成するには、次のように入力する。
ただし、既に存在していた場合は、エラーになる。

```sh
cd
pwd
/home/ユーザー名 または /Users/ユーザー名
```
```sh
ls
# (ホームディレクトリにファイルがあれば表示される)
mkdir unix_practice
※unix_practiceがまだ存在していない場合は作成される。存在するとエラーが出る
```

`ls` コマンドで確認すると、`unix_practice` ディレクトリが作成されていることがわかる。

```sh
ls
※unix_practiceも表示される
```

一度に複数のディレクトリを作成することもできる。
```sh
mkdir dir1 dir2 dir3
```
また、`-p` オプションを使うと、深い階層のディレクトリを一度に作成できる。例えば、`mkdir -p project/src/main` とすると、`project` ディレクトリがなければ作成し、その中に `src` を、さらにその中に `main` を作成する。

> ### ☆練習☆
>
> 1.  ホームディレクトリに移動し (`cd ~` または `cd`)、`pwd` コマンドで現在のディレクトリを確認してみよう。
> 2.  `ls -a` コマンドを実行し、ホームディレクトリにある隠しファイルや隠しディレクトリを確認してみよう。`.zshrc` や `.bash_profile` といったシェル設定ファイル、`.gitconfig` といったGitの設定ファイルなどが見つかるかもしれない。
> 3.  `mkdir unix_practice` コマンドを使って `unix_practice` という名前のディレクトリを作成してみよう。すでに村ざししている場合はそのままでよい。
> 4.  `cd unix_practice` コマンドで、作成した `unix_practice` ディレクトリに移動してみよう。
> 5.  `unix_practice` ディレクトリの中で、さらに `mkdir test_dir` コマンドを使って `test_dir` というディレクトリを作成し、そこに `cd test_dir` で移動してみよう。
> 6.  `pwd` で現在地を確認後、`cd ..` コマンドを使って、一つ上の `unix_practice` ディレクトリに戻ってみよう。そして再度 `pwd` で確認しよう。
> 7.  さらに `cd ../..` のように `..` を繋げて、一気に二つ上の階層に移動してみよう。`pwd` で確認しよう。
> 8.  絶対パスを使って、`unix_practice/test_dir` に一気に戻ってみよう（例: `cd /Users/ユーザー名/unix_practice/test_dir` または `cd /home/ユーザー名/unix_practice/test_dir`）。
> 9.  タブ補完を試してみよう。ホームディレクトリで `cd /e` まで入力して <kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Tab</kbd> キーを押すとどうなるか試してみよう？

## この章のまとめ

この章では、ファイルとディレクトリを操作するための基本的なコマンドを学んだ。

*   `pwd` (ピーダブルディー): 現在の作業ディレクトリを表示する。
*   `ls` (エルエス): ファイルやディレクトリの一覧を表示する。
    *   `-l`: 詳細表示
    *   `-a`: 隠しファイルも表示 (例: `.bashrc`, `.gitconfig`)
    *   `-F`: ファイルの種類を記号で表示 (`/`, `*`, `@` など)
    *   オプションの組み合わせ (例: `ls -laF`)
*   `cd` (シーディー): ディレクトリを移動する。
    *   `.`: 現在のディレクトリ
    *   `..`: 親ディレクトリ
    *   `~`: ホームディレクトリ
    *   `/`: ルートディレクトリ
    *   絶対パスと相対パス
    *   タブ補完の活用
*   `mkdir` (メイクディレクトリー): 新しいディレクトリを作成する。
    *   `mkdir ディレクトリ名`
    *   `mkdir -p 親ディレクトリ/子ディレクトリ` (深い階層まで一度に作成)

これらのコマンドは、UNIXシステムを使いこなすための基礎中の基礎である。コマンドの意味を理解し、実際に手を動かして何度も練習することで、スムーズに操作できるようになる。最初は難しく感じるかもしれないが、慣れれば非常に効率的な作業が可能になるだろう。
