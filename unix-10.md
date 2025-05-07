# ネットワーク越しのUNIX：他のコンピュータとの接続

UNIX系システム（macOSやLinuxなど）は、ネットワークを通じて他のコンピュータと連携するための強力な機能を備えている。この章では、ユーザー情報の確認、他のコンピュータへの接続、ネットワーク診断といった基本的なネットワーク関連のコマンドや概念について学ぶ。

## ユーザー情報を調べる

UNIX系システムは、複数のユーザーが同時に一台のコンピュータを利用することを前提に設計されている（マルチユーザーシステム）。ネットワーク経由での利用も一般的である。

### 誰が何をしているか: `w` コマンド

現在システムにログインしているユーザーと、そのユーザーが実行しているプロセス（処理）の概要を表示するには `w` (ダブリュー) コマンドを使用する。「who and what（誰が何をしているか）」の略であると言われている。

```
$ w
 10:05:30 up 2 days, 15:30,  2 users,  load average: 0.08, 0.03, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
user1    pts/0    192.168.0.10     09:30    5:00m  0.20s  0.05s -bash
user2    pts/1    somehost.example.com 10:00    0.00s  0.10s  0.01s w
```

この出力から、以下の情報が読み取れる。

*   1行目: 現在時刻、システムの稼働時間、現在のログインユーザー数、システムの平均負荷 (load average。数値が大きいほど混雑していることを示す)。
*   **USER**: ユーザー名である。
*   **TTY**: ユーザーが接続している端末名である (pts/0 などは仮想端末を示す)。
*   **FROM**: ユーザーがどこから接続しているか (IPアドレスやホスト名) を示す。
*   **LOGIN@**: ログインした時刻である。
*   **IDLE**: アイドル時間 (最後にキー入力など操作をしてからの経過時間) である。
*   **JCPU**: その端末に関連する全プロセスのCPU使用時間である。
*   **PCPU**: 現在実行中のプロセスのCPU使用時間 (WHAT欄のプロセス) である。
*   **WHAT**: 現在実行中のコマンドである。

以前紹介した `who` (フー) コマンドよりも詳細な情報が得られる。

```
$ who
user1    pts/0        2025-05-07 09:30 (192.168.0.10)
user2    pts/1        2025-05-07 10:00 (somehost.example.com)
```

### より詳しいユーザー情報を調べる: `finger` コマンド

`finger` (フィンガー) コマンドは、指定したユーザーに関するより詳細な情報（フルネーム、ホームディレクトリ、ログインシェル、最終ログイン日時など）を表示する。

> **注意**: `finger` (フィンガー) コマンドは、個人の情報が外部から参照できてしまうというセキュリティ上の懸念から、最近のシステムではデフォルトでインストールされていなかったり、機能が制限されていたりすることがある。WSL Ubuntuなどで使用できない場合は、`sudo apt update && sudo apt install finger` コマンドでインストールできる場合があるが、利用は慎重に行うべきである。

```
$ finger user1
Login: user1         		Name: User One
Directory: /home/user1       	Shell: /bin/bash
On since Wed May  7 09:30 (JST) on pts/0 from 192.168.0.10
   5 hours 5 minutes idle
No mail.
No Plan.
```
*   **Login**: ユーザー名
*   **Name**: フルネーム（設定されていれば）
*   **Directory**: ホームディレクトリ
*   **Shell**: ログインシェル
*   **On since**: 最終ログイン日時と接続元
*   **idle**: アイドル時間
*   **Mail**: メールに関する情報（古いシステムで使われた機能）
*   **Plan**: `.plan`ファイルの内容（ユーザーが公開したい情報を記述するファイル。これも古い機能である）

`finger` (フィンガー) コマンドは、引数なしで実行すると、現在ログインしている全ユーザーの情報を表示する。

かつては `finger ユーザー名@ホスト名` のようにして、ネットワーク越しの他のコンピュータのユーザー情報を参照できたが、プライバシーやセキュリティの観点から、現在ではほとんどのシステムでこの機能は無効化されているか、許可されていない。

## ホスト名とIPアドレス

ネットワークに接続された各コンピュータは、「ホスト名」と「IPアドレス」という二つの識別子を持つ。

*   **ホスト名 (hostname)**: 人間が覚えやすいように付けられたコンピュータの名前である (例: `myserver`, `www.example.com`)。
*   **IPアドレス (IP address)**: ネットワーク上でコンピュータを一位に識別するための数値的な住所である (例: `192.168.1.10`, `2001:db8::1`)。現在主に使われているのはIPv4 (例: `93.184.216.34`) と、より新しいIPv6 (例: `2606:2800:220:1:248:1893:25c8:1946`) の二種類がある。

### ホスト名を調べる: `hostname` コマンド

現在使用しているコンピュータのホスト名を表示するには `hostname` (ホストネーム) コマンドを使用する。

```
$ hostname
mycomputer.local
```

### ホスト名とIPアドレスの対応を調べる: `host` コマンド

ホスト名からIPアドレスを調べたり、逆にIPアドレスからホスト名を調べたりするには `host` (ホスト) コマンドを使用する。この処理を「名前解決 (name resolution)」と呼ぶ。これは、インターネット上の住所録のようなものであるDNS (Domain Name System) サーバーに問い合わせて行われる。

```
$ host example.com
example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
example.com mail is handled by 0 . 

$ host 93.184.216.34
34.216.184.93.in-addr.arpa domain name pointer example.com.
```
最初の例では `example.com` というホスト名に対応するIPアドレス (IPv4とIPv6の両方) と、メールサーバーの情報が表示されている。次の例では、IPアドレス `93.184.216.34` に対応するホスト名が表示されている。

より詳細な名前解決情報が必要な場合は `dig` (ディグ) (Domain Information Groper) コマンドが使われる。古いシステムでは `nslookup` (エヌエスルックアップ) コマンドも使われたが、現在は `host` (ホスト) や `dig` (ディグ) の使用が推奨される。

## 他のコンピュータに接続する: `ssh` コマンド

`ssh` (エスエスエイチ) (Secure SHell) は、ネットワーク経由で他のコンピュータに安全にログインし、コマンドを実行するためのプロトコルおよびコマンドである。通信内容は暗号化されるため、パスワードやデータが第三者に盗聴される危険性が低い。

接続するには、以下の形式でコマンドを実行する。
```
ssh ユーザー名@ホスト名
```
例えば、`server.example.com` というホストに `user1` というユーザー名で接続する場合：
```
$ ssh user1@server.example.com
```

初めて接続するホストの場合、以下のようなメッセージが表示されることがある。
```
The authenticity of host 'server.example.com (192.0.2.10)' can't be established.
ECDSA key fingerprint is SHA256:AbCdEfGhIjKlMnOpQrStUvWxYz1234567890aBcDeFg.
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
```
これは、「接続しようとしている `server.example.com` (IPアドレス `192.0.2.10`) の正当性が確認できません。このホストの鍵の指紋 (フィンガープリント) は `SHA256:AbCdEf...` です。接続を続行しますか？」という意味である。これは、中間者攻撃（なりすまし）を防ぐための重要な警告である。ホストの管理者にフィンガープリントが正しいか確認するなどして正当性を確認後、`yes` と入力すると接続が続行され、そのホストの情報 (ホスト名と公開鍵) が `~/.ssh/known_hosts` ファイルに保存される。次回以降、同じホストに接続する際にはこの警告は表示されない（保存された鍵と一致するため）。もしフィンガープリントが一致しないという警告が出た場合は、接続先が偽物である可能性があるので注意が必要である。

その後、パスワードの入力を求められる（パスワード認証の場合）。
```
user1@server.example.com's password: [パスワードを入力]
```
(入力したパスワードは画面には表示されない。)

認証に成功すると、リモートホストのシェルが利用可能になる。
```
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-generic x86_64)

Last login: Wed May  7 10:30:00 2025 from clientpc.example.org
user1@server:~$ pwd
/home/user1
user1@server:~$ 
```
プロンプトが `user1@server:~$` のように変わり、リモートホスト (`server`) 上でコマンドを実行していることがわかる。

接続を終了するには `exit` (イグジット) コマンドを実行する。
```
user1@server:~$ exit
logout
Connection to server.example.com closed.
$
```

`ssh` (エスエスエイチ) には、パスワード認証の他に、より安全で便利な公開鍵認証方式もある。これは、事前に自分の公開鍵を接続先サーバーに登録しておくことで、パスワードなしでログインできる方式である。また、`-X` オプションを付けて接続すると、リモートホスト上のGUIアプリケーションを手元のコンピュータに表示して操作するX11フォワーディング機能も利用できる（別途、手元のコンピュータにXQuartz (macOS) やXming (Windows) などのXサーバーソフトウェアが必要な場合がある）。

## ネットワークの状態を調べる

ネットワーク接続のトラブルシューティングなどに役立つコマンドをいくつか紹介する。

### 相手に届くか確認: `ping` コマンド

`ping` (ピング) コマンドは、指定したホストに対してICMP (Internet Control Message Protocol) のエコー要求パケットと呼ばれる小さなデータパケットを送信し、相手ホストからエコー応答パケットが返ってくるかを確認することで、ネットワーク的な到達可能性を調べるために使われる。

```
$ ping example.com
PING example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=50 time=15.5 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=50 time=16.2 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=50 time=15.8 ms

--- example.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 15.528/15.845/16.201/0.280 ms
```
`Ctrl+C` を押すと終了する。各行は、相手ホストからの応答を示しており、`time=` の部分が応答時間 (ミリ秒) である。最後の統計情報で、送信したパケット数 (transmitted)、受信したパケット数 (received)、失われたパケットの割合 (packet loss)、往復時間 (rtt) の最小/平均/最大/標準偏差などが表示される。応答時間 (time) が非常に大きい場合や、パケットロスが発生している場合は、ネットワーク経路に問題がある可能性が考えられる。

### ネットワークインターフェースの情報を表示

コンピュータが持つネットワークアダプタ（ネットワークインターフェース）の設定情報（IPアドレス、MACアドレスなど）を表示するコマンドは、OSによって異なる。

*   **macOS の場合**: `ifconfig` (イフコンフィグ) コマンドが伝統的に使われる。
    ```
    $ ifconfig en0
    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 00:11:22:33:44:55 
        inet6 fe80::123:4567:89ab:cdef%en0 prefixlen 64 secured scopeid 0x5
        inet 192.168.1.102 netmask 0xffffff00 broadcast 192.168.1.255
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect
        status: active
    ```
    `en0` は有線LAN、`en1` は無線LANなど、インターフェース名は環境によって異なる。`inet` の行にIPv4アドレス、`inet6` の行にIPv6アドレス、`ether` の行にMACアドレスが表示される。

*   **Linux (WSL Ubuntuなど) の場合**: `ip addr show` (アイピー エーディーディーアール ショウ) コマンド (または短縮形の `ip a` (アイピー エー)) が推奨される。
    ```
    $ ip addr show eth0
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:15:5d:01:02:03 brd ff:ff:ff:ff:ff:ff
        inet 172.20.130.5/20 brd 172.20.143.255 scope global eth0
           valid_lft forever preferred_lft forever
        inet6 fe80::215:5dff:fe01:203/64 scope link 
           valid_lft forever preferred_lft forever
    ```
    `eth0` は最初のイーサネットインターフェースを指すことが多い。`inet` の行にIPv4アドレス (CIDR形式)、`inet6` の行にIPv6アドレス、`link/ether` の行にMACアドレスが表示される。`ifconfig` (イフコンフィグ) コマンドも `net-tools` パッケージをインストールすれば利用できる場合がある。

## (補足) かつてのコミュニケーションツール: `talk` など

古いUNIXシステムには、同じコンピュータやネットワーク上の他のユーザーとリアルタイムでテキストチャットを行うための `talk` (トーク) や `phone` (フォン) といったコマンドが存在した。しかし、これらは現代のmacOSやLinuxディストリビューションでは標準でインストールされていないことが多く、セキュリティや機能面から、Slack、Discord、Microsoft Teams、各種メッセンジャーアプリ、IRCといったより高機能なコミュニケーションツールに取って代わられている。

もしターミナル上で複数ユーザーが共同作業をしたい場合は、`ssh` (エスエスエイチ) で同じサーバーにログインし、`tmux` (ティーマックス) や `screen` (スクリーン) といったターミナルマルチプレクサを使ってセッションを共有する方法がある。また、`write` (ライト) コマンドを使えば、同じシステムにログインしている別のユーザーの端末に短いメッセージを送信できるが、これもあまり使われなくなっている。

## この章で紹介したコマンド

| コマンド        | ふりがな        | 説明                                     | 主な使い方例                               |
|---------------|-----------------|------------------------------------------|-------------------------------------------|
| `w`           | ダブリュー      | ログインユーザーと実行プロセス概要を表示     | `w`                                       |
| `who`         | フー            | ログインユーザーの一覧を表示               | `who`                                     |
| `finger`      | フィンガー      | ユーザー情報を表示                         | `finger ユーザー名`, `finger`             |
| `hostname`    | ホストネーム    | 自ホスト名を表示                           | `hostname`                                |
| `host`        | ホスト          | ホスト名とIPアドレスの対応を調べる         | `host example.com`, `host 93.184.216.34`  |
| `dig`         | ディグ          | DNS情報を詳細に調べる                      | `dig example.com`                         |
| `ssh`         | エスエスエイチ  | Secure Shellでリモートホストに接続         | `ssh ユーザー名@ホスト名`                   |
| `exit`        | イグジット      | 現在のシェルを終了する（ssh接続も終了）    | `exit`                                    |
| `ping`        | ピング          | ホストへの到達可能性と応答時間を確認       | `ping example.com`                        |
| `ifconfig`    | イフコンフィグ  | (主にmacOS) ネットワークインターフェース設定表示 | `ifconfig en0`, `ifconfig`                |
| `ip addr show`| アイピー エーディーディーアール ショウ | (主にLinux) ネットワークインターフェース設定表示 | `ip addr show eth0`, `ip a`               |
| `nslookup`    | エヌエスルックアップ | (旧) ホスト名とIPアドレスの対応を調べる    | `nslookup example.com`                    |
| `talk`        | トーク          | (旧) 他ユーザーとチャットする              | `talk ユーザー名@ホスト名`                |
| `write`       | ライト          | (旧) 他ユーザーの端末にメッセージを送信    | `write ユーザー名`                        |

これらのコマンドは、ネットワークを利用した作業や、ネットワークの問題解決の第一歩として役立つだろう。
