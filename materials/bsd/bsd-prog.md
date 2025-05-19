# プログラミング言語の使い方

ここでは、 UNIX システムで使用可能なプログラミング言語を
簡単に紹介する。 紹介しているプログラムは、円の半径を読み込んで、
円周(2×$\pi$×半径)と円の面積($\pi$×半径×半径)を求めて
表示するものである。

## コンパイラ系

コンパイラ系の各言語は本格的なプログラミングを行うのに向いている。 特に
C はさまざまな場面で用いられていて、応用範囲も広い。
コンパイラ系では、ソース・プログラムを書き、それをコンパイラで
マシン語の実行型ファイルに変換してから実行する。 以下に紹介した
C、Pascal、FORTRAN では、コンパイルの方法は
次のように共通の形式になっている。

::: coml
15.5cm
「コンパイラ・コマンド」  `-o`  「実行型ファイル名」  「ソース・ファイル名」
:::

以下の例では、「実行型ファイル名」に、「ソース・ファイル名」から拡張子を
取り除いたものを使っているが、別な名前[^1]を指定してもいい。

また、コンパイルしてできた実行型ファイルを実行するには、次のようにする。

::: coml
5.5cm `./`「実行型ファイル名」
:::

### C

**プログラム例**

::: progls2
circle.c #include \<stdio.h\>

int main() { /\* 使用する変数の指定 \*/ double pi, hankei, enshuu,
menseki; /\* 円周率 \*/ pi = 3.141593;
:::

::: progls2
/\* 半径を端末から読み込む \*/ printf(\"円の半径を入力してくださいn\");
scanf(\"

/\* 円周と面積を求める \*/ enshuu = 2.0 \* pi \* hankei; menseki = pi \*
hankei \* hankei;

/\* 表示 \*/ printf(\"半径 = printf(\"円周 =

return(0); }
:::

**実行例**

::: progls
円の半径を入力してください 半径 = 20.000000 円周 = 125.663720、面積 =
1256.637200
:::

### Pascal

**プログラム例**

::: progls2
circle.p program circle(input, output); 使用する変数の指定 var pi :
real; hankei : real; enshuu : real; menseki : real;

begin { 円周率 } pi := 3.141593;

{ 半径を端末から読み込む } writeln('円の半径を入力してください');
readln(hankei);

{ 円周と面積を求める } enshuu := 2.0 \* pi \* hankei; menseki := pi \*
hankei\*\*2;

{ 表示 } writeln('半径 = ', hankei); writeln('円周 = ', enshuu, '、面積
= ', menseki); end.
:::

**実行例**

::: progls
円の半径を入力してください 半径 = 2.000000000000000e+01 円周 =
1.256637200000000e+02、面積 = 1.256637200000000e+03
:::

### FORTRAN

**プログラム例**

::: progls2
circle.f PROGRAM CIRCLE C 使用する変数の指定 IMPLICIT NONE REAL PI,
HANKEI, ENSHUU, MENSEKI C 円周率 PI = 3.141593 C 半径を端末から読み込む
WRITE(\*,\*) '円の半径を入力してください' READ(\*,\*) HANKEI C
円周と面積を求める ENSHUU = 2.0 \* PI \* HANKEI MENSEKI = PI \*
HANKEI\*\*2 C 表示 WRITE(\*,\*) '半径 = ', HANKEI WRITE(\*,\*) '円周 =
', ENSHUU, '、面積 = ', MENSEKI STOP END
:::

**実行例**

::: progls
/usr/lib/libg2c.so: warning: tempnam() possibly used unsafely; consider
using mk stemp() 円の半径を入力してください 半径 = 20. 円周 =
125.663719、面積 = 1256.63721
:::

## バイト・コンパイラ系

### Java

バイト・コンパイラ系の Java では、
ソース・プログラムを書き、それをコンパイラ(`javac`)で
中間コードと呼ばれる形式に変換し、 Java
仮想機械と呼ばれるプログラム(`java`)にロードして 実行する。
このことによって、さまざまなマシン上で同じように動くプログラムを
書くことができ、 WWW 関係のプログラミングでよく用いられている。

まず、コンパイルするには次のようにする。

::: coml
8cm `javac`  「ソース・ファイル名」
:::

Java 仮想機械にロードして実行するには次のようにする。
なお、「クラス名」というのは、 以下の例では「`Circle`」である。

::: coml
5.3cm `java`  「クラス名」
:::

**プログラム例**

::: progls2
Circle.java import java.io.\*; class Circle { public static void
main(String\[\] args) throws IOException { /\* 円周率 \*/ double pi =
3.141593;

/\* 半径を端末から読み込む \*/
System.out.println(\"円の半径を入力してください\"); BufferedReader br =
new BufferedReader(new InputStreamReader(System.in)); String str =
br.readLine(); double hankei = Double.parseDouble(str);

/\* 円周と面積を求める \*/ double enshuu = 2.0 \* pi \* hankei; double
menseki = pi \* hankei \* hankei;

/\* 表示 \*/ System.out.println(\"半径 = \" + hankei);
System.out.println(\"円周 = \" + enshuu + \"、面積 = \" + menseki); } }
:::

**実行例**

::: progls
円の半径を入力してください 半径 = 20.0 円周 = 125.66372、面積 =
1256.6372
:::

## インタプリタ系

インタプリタ系では、プログラムを書き、
それをインタプリタにロードして実行する。
手軽にプログラミングできるのが特徴である。 Perl、 Python、 Ruby は、 WWW
で掲示板などに使われる CGI を作るのに よく用いられる言語だ。
また、ここでは紹介していないが、 Web ブラウザ上で動く
インタプリタ系の言語の一種である JavaScript は、 HTML
と組み合わせて利用し、たとえばマウスをボタンに重ねると
ボタンの画像が変わったりするようなしくみに使われている。

以下に紹介したもののうち、 Python、Perl、 Ruby の場合、
個別に書かなかったが、プログラムを書いたらパーミッションを
実行可能にして(「`chmod 755 「プログラム・ファイル名」`」)から
実行すること。 BASIC
の実行の仕方はこれらと異なっているので個別に紹介した。

### Python

**プログラム例**

::: progls2
circle.py #!/usr/local/bin/python import sys \# 円周率 pi = 3.141593

\# 半径を端末から読み込む print \"円の半径を入力してください\"; hankei =
float(sys.stdin.readline());

\# 円周と面積を求める enshuu = 2.0 \* pi \* hankei; menseki = pi \*
hankei \* hankei;

\# 表示 print '半径 = ', hankei; print '円周 = ', enshuu, '、面積 = ',
menseki;
:::

**実行例**

::: progls
円の半径を入力してください 半径 = 20.0 円周 = 125.66372 、面積 =
1256.6372
:::

### Perl

**プログラム例**

**実行例**

::: progls
円の半径を入力してください 半径 = 20 円周 = 125.66372、面積 = 1256.6372
:::

### Ruby

**プログラム例**

::: progls2
circle.rb #!/usr/local/bin/ruby \# 円周率 pi = 3.141593

\# 半径を端末から読み込む print \"円の半径を入力してくださいn\" hankei =
readline() hankei = hankei.to_f

\# 円周と面積を求める enshuu = 2.0 \* pi \* hankei menseki = pi \*
hankei \* hankei

\# 表示 print \"半径 = \", hankei, \"n\" print \"円周 = \", enshuu,
\"、面積 = \", menseki, \"n\"
:::

**実行例**

::: progls
円の半径を入力してください 半径 = 20.0 円周 = 125.66372、面積 =
1256.6372
:::

### BASIC

BASIC の場合、プログラムを書き、 BASIC
を起動(この場合は「`bwbasic`」と入力)して、
その中でプログラムをロード(`load "「ファイル名」"`)し、
「`run`」コマンドで実行する。 BASIC
を終了するには、「`quit`」コマンドである。

**プログラム例**

::: progls2
circle.bas 10 REM 円周率 20 LET PI = 3.141593 30 REM
半径を端末から読み込む 40 PRINT \"円の半径を入力してください\" 50 INPUT
HANKEI 60 REM 円周と面積を求める 70 LET ENSHUU = 2 \* PI \* HANKEI 80
LET MENSEKI = PI \* HANKEI \* HANKEI 90 REM 表示 100 PRINT \"半径 =\";
HANKEI 110 PRINT \"円周 =\"; ENSHUU; \"、面積 =\"; MENSEKI 120 END
:::

**実行例**

::: progls
Bywater BASIC Interpreter/Shell, version 2.20 patch level 1 Copyright
(c) 1993, Ted A. Campbell

bwBASIC: bwBASIC: 円の半径を入力してください ? 半径 = 20 円周 =
125.6637200、面積 = 1256.6372000 bwBASIC:
:::

余談だが、最近の Windows などでは 「`cscript`」という コマンドで、
VBscript(Visual Basic Scripting Edition)などの
プログラムをロードして使うこともできるようになっている。 VBscript で
BASIC のものと同様なプログラムを書くと以下のようになる。 同じ BASIC
という名前がついていても、見た目が随分異なった
プログラムになることがわかるだろう。

**プログラム例**

::: progls2
circle.vbs ' 円周率 pi = 3.141593

' 半径を端末から読み込む Wscript.echo(\"円の半径を入力してください\")
hankei = CDbl(Wscript.StdIn.ReadLine)

' 円周と面積を求める enshuu = 2 \* pi \* hankei menseki = pi \* hankei
\* hankei

' 表示 Wscript.echo(\"半径 = \" & hankei) Wscript.echo(\"円周 = \" &
enshuu & \"、面積 = \" & menseki)
:::

**実行例**

実行するには、 Windows XP
で「スタート」→「すべてのプログラム」→「アクセサリ」→ 「コマンド
プロンプト」として、「コマンド プロンプト」をまず起動する。
起動したら、以下のように実行する。

::: progls
E:ei00ei00000\> Microsoft (R) Windows Script Host Version 5.6 Copyright
(C) Microsoft Corporation 1996-2001. All rights reserved.

円の半径を入力してください 半径 = 20 円周 = 125.66372、面積 = 1256.6372

E:ei00ei00000\>
:::

[^1]: たとえば「`ls`」、
    「`rm`」なども指定できる。ただし、そうするとややこしくなる。
    自分なりに適当な名前を考えて付けよう。
