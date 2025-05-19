# ファイルとディレクトリ操作の練習

![絶対パス](images/absolutepath.00.jpg)

![相対パス](images/relativepath.01.jpg)

## ホームディレクトリに移動
### その1
```sh
cd # cdで引数なし
pwd # 確認
ls # 確認
```

### その2
```sh
cd ~ # ~（ホームディレクトリ）に移動
pwd # 確認
ls # 確認
```

## リダイレクトでファイルを作る
```sh
# 出力を確認
date "+%Y-%m-%d %H:%M:%S"
# ファイルにリダイレクト
date "+%Y-%m-%d %H:%M:%S" > ima.txt
# ファイルができているか確認
ls
# ファイルの中身を確認
cat ima.txt
```

## ホームディレクトリの一つ上に移動
Ubuntu /home、macOS /Users
### その1
一旦、ホームディレクトリに戻る
```sh
cd
pwd
ls
```

```sh
cd .. # ..（一つ上）に移動
pwd
ls
```

### その2
ディレクトリに入る
```sh
# Ubuntuの場合
cd /home # /home（一つ上に相当）に移動
# macOSの場合
cd /Users # /Users（一つ上に相当）に移動
pwd
ls
```

## 一番上のルートディレクトリ（/）に移動
### その1
```sh
cd / # /（ルートディレクトリ）に移動
pwd
ls
```

### その2
一旦、ホームディレクトリに戻る
```sh
cd
pwd
ls
```

```sh
cd ../.. # ../.. 1つ上の1つ上（ルートディレクトリ）に移動
pwd
ls
```

### その3
一旦、ホームディレクトリに戻る
```sh
cd
pwd
ls
```

```sh
cd .. # .. 1つ上に移動
pwd
ls
cd .. # .. 更に1つ上（ルートディレクトリ）に移動
pwd
ls
```

## /etcに移動

```sh
cd /etc # /etcに移動
pwd
ls
```

# ディレクトリpracticeを作る
一旦、ホームディレクトリに戻る
```sh
cd
pwd
```

## ディレクトリを作る
```sh
mkdir practice
ls
```

ディレクトリpracticeに入る
```sh
cd practice
pwd
ls
```

## ディレクトリpracticeを消す
一旦、ホームディレクトリに戻る
```sh
cd
pwd
```

ディレクトリpracticeとその中を確認
```sh
ls
ls practice
```

ディレクトリpracticeが空なら消す
```sh
rmdir practice
ls
```

## ディレクトリpracticeの中にファイルを作り、消す
### その1
ディレクトリpracticeを確認する
```sh
cd
pwd
ls
```

ディレクトリpracticeがなければ作る
```sh
mkdir practice
ls
```

ディレクトリpracticeの中にファイルを作る
```sh
uname -a > practice/info.txt
ls practice
cat practice/info.txt
```

作ったファイルを消す
```sh
rm practice/info.txt
ls practice
```

### その2
ディレクトリpracticeを確認する
```sh
cd
ls
```

ディレクトリpracticeがなければ作る
```sh
mkdir practice
ls
```

ディレクトリpracticeの中に入り、ファイルを作る
```sh
cd practice
uname -a > info.txt
ls
cat info.txt
```

作ったファイルを消す
```sh
rm info.txt
ls
```
