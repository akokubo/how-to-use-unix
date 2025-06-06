# ネットワーク越しのUNIX：他のコンピュータとの接続と通信

UNIX系システム（macOSやWSL上のUbuntuなど）は、ネットワークを通じて他のコンピュータと連携するための強力な機能を備えている。この章では、ユーザー情報の確認、他のコンピュータへの接続、ネットワーク診断といった基本的なネットワーク関連のコマンドや概念について学ぶ。ネットワーク機能を活用することで、遠隔地からのコンピュータ操作や、複数のコンピュータ間でのデータ共有が可能になる。

## ユーザー情報を調べる

UNIX系システムは、複数のユーザーが同時に一台のコンピュータを利用することを前提に設計されている（マルチユーザーシステム）。ネットワーク経由での利用も一般的である。システムにログインしているユーザーを調べることで、同じコンピュータを利用している他のユーザーの状況を確認できる。

### 誰が何をしているか: `w` コマンド

現在システムにログインしているユーザーと、そのユーザーが実行しているプロセス（処理）の概要を表示するには `w` (ダブリュー) コマンドを使用する。「who and what（誰が何をしているか）」の略であると言われている。システム管理者は、このコマンドを使って現在の利用状況を確認することができる。

```
$ w
 10:05:30 up 2 days, 15:30,  2 users,  load average: 0.08, 0.03, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
user1    pts/0    192.168.0.10     09:30    5:00m  0.20s  0.05s -bash
user2    pts/1    somehost.example.com 10:00    0.00s  0.10s  0.01s w
```

この出力から、以下の情報が読み取れる。

*   1行目: 現在時刻、システムの稼働時間（2日と15時間30分）、現在のログインユーザー数（2人）、システムの平均負荷 (load average。数値が大きいほど混雑していることを示す)。
*   **USER**: ユーザー名である。この例では「user1」と「user2」の2人が利用中。
*   **TTY**: ユーザーが接続している端末名である (pts/0 などは仮想端末を示す)。
*   **FROM**: ユーザーがどこから接続しているか (IPアドレスやホスト名) を示す。ローカルログインの場合は空白になる。
*   **LOGIN@**: ログインした時刻である。user1は09:30に、user2は10:00にログインしている。
*   **IDLE**: アイドル時間 (最後にキー入力など操作をしてからの経過時間) である。user1は5時間何も操作していない。
*   **JCPU**: その端末に関連する全プロセスのCPU使用時間である。
*   **PCPU**: 現在実行中のプロセスのCPU使用時間 (WHAT欄のプロセス) である。
*   **WHAT**: 現在実行中のコマンドである。user1は「-bash」（bashシェルを起動したまま）、user2は「w」コマンドを実行中である。

以前紹介した `who` (フー) コマンドよりも詳細な情報が得られる。

```
$ who
user1    pts/0        2025-05-07 09:30 (192.168.0.10)
user2    pts/1        2025-05-07 10:00 (somehost.example.com)
```

## ホスト名とIPアドレス

ネットワークに接続された各コンピュータは、「ホスト名」と「IPアドレス」という二つの識別子を持つ。

*   **ホスト名 (hostname)**: 人間が覚えやすいように付けられたコンピュータの名前である (例: `myserver`, `www.example.com`)。インターネットに公開されているサービスの場合は、「ドメイン名」の一部となる。
*   **IPアドレス (IP address)**: ネットワーク上でコンピュータを一意に識別するための数値的な住所である。住所のようなもので、このアドレスによってネットワーク上のどのコンピュータかを特定できる。現在主に使われているのは以下の2種類がある：
    - **IPv4 (Internet Protocol version 4)**: `192.168.1.10` や `93.184.216.34` のような、4つの数値（0～255）をドット（.）で区切った形式。
    - **IPv6 (Internet Protocol version 6)**: `2001:db8::1` や `2606:2800:220:1:248:1893:25c8:1946` のような、16進数で表現された長い形式。IPv4のアドレスが不足してきたため導入された、より多くのアドレスを扱える新しい形式。

### ホスト名を調べる: `hostname` コマンド

現在使用しているコンピュータのホスト名を表示するには `hostname` (ホストネーム) コマンドを使用する。ネットワーク設定の確認や、複数のコンピュータを操作しているときに現在どのコンピュータを使用しているか確認するのに役立つ。

```
$ hostname
mycomputer.local
```

### ホスト名とIPアドレスの対応を調べる: `host` コマンド

ホスト名からIPアドレスを調べたり、逆にIPアドレスからホスト名を調べたりするには `host` (ホスト) コマンドを使用する。この処理を「名前解決 (name resolution)」と呼ぶ。これは、インターネット上の住所録のようなものであるDNS (Domain Name System) サーバーに問い合わせて行われる。ウェブサイトを閲覧するときも、背後では同様の処理が行われている。

```
$ host example.com
example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
example.com mail is handled by 0 . 

$ host 93.184.216.34
34.216.184.93.in-addr.arpa domain name pointer example.com.
```
最初の例では `example.com` というホスト名に対応するIPアドレス (IPv4とIPv6の両方) と、メールサーバーの情報が表示されている。次の例では、IPアドレス `93.184.216.34` に対応するホスト名（example.com）が表示されている。

より詳細な名前解決情報が必要な場合は `dig` (ディグ) (Domain Information Groper) コマンドが使われる。古いシステムでは `nslookup` (エヌエスルックアップ) コマンドも使われたが、現在は `host` (ホスト) や `dig` (ディグ) の使用が推奨される。

### ☆練習1: ホスト名とIPアドレスを調べてみよう☆

1. `hostname` コマンドを実行して、自分のコンピュータのホスト名を確認しよう。

2. 有名なウェブサイト（例：google.com、amazon.com）の IPアドレスを `host` コマンドで調べてみよう。
   - IPv4アドレスとIPv6アドレスの両方が表示されるか確認する。
   - 同じウェブサイトでも複数のIPアドレスが表示される場合がある。なぜだろうか？

3. IPアドレス `8.8.8.8` を `host` コマンドで調べてみよう。どのサービスのIPアドレスだろうか？
   - ヒント: これはGoogle社が提供する公開DNSサーバーのアドレスである。


## ネットワークの状態を調べる

ネットワーク接続のトラブルシューティングなどに役立つコマンドをいくつか紹介する。

### 相手に届くか確認: `ping` コマンド

`ping` (ピング) コマンドは、指定したホストに対してICMP (Internet Control Message Protocol) のエコー要求パケットと呼ばれる小さなデータパケットを送信し、相手ホストからエコー応答パケットが返ってくるかを確認することで、ネットワーク的な到達可能性を調べるために使われる。インターネット接続の確認や、ネットワーク障害の切り分けに便利なツールである。

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

> **注意**: セキュリティ上の理由から、一部のサーバーやファイアウォールでは `ping` コマンドへの応答を制限していることがある。そのため、`ping` が応答を返さなくても、必ずしもサーバーがダウンしているとは限らない。また、公共のWi-Fiや一部の携帯電話ネットワークでも、`ping` が制限されていることがある。

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
    `en0` は有線LAN、`en1` は無線LANなど、インターフェース名は環境によって異なる。`inet` の行にIPv4アドレス、`inet6` の行にIPv6アドレス、`ether` の行にMACアドレス（コンピュータのネットワークインターフェースに固有の物理アドレス）が表示される。

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

### ☆練習3: ネットワーク状態を確認してみよう☆

1. `ping` コマンドで、インターネット上のウェブサイトとの接続を確認しよう。
   ```
   $ ping -c 4 google.com
   ```
   `-c 4` オプションは、4回のping要求を送信したら自動的に終了するという意味である。

2. 自分のコンピュータのネットワークインターフェース情報を確認しよう。
   
   macOSの場合：
   ```
   $ ifconfig
   ```
   
   WSL Ubuntuの場合：
   ```
   $ ip a
   ```
   
   表示された自分のIPアドレス（IPv4）を確認しよう。

## この章で学んだこと

この章では、ネットワークに関連するUNIXコマンドの基礎を学んだ。まずシステムにログインしているユーザーを確認する `w` や `who` コマンド、次にホスト名とIPアドレスに関する `hostname` と `host` コマンド、他のコンピュータに安全に接続するための `ssh` コマンド、ネットワーク到達性を確認する `ping` コマンド、そして自分のコンピュータのネットワーク設定を表示する `ifconfig` や `ip addr show` コマンドを学習した。

これらのコマンドは、ネットワーク環境での作業を効率的に行うための基本ツールである。特に、`ssh` コマンドは、リモートサーバーの管理において非常に強力なツールであり、インターネット上の様々なサービスやクラウド環境での操作の基盤となっている。

## この章で紹介したコマンド

| コマンド        | ふりがな        | 説明                                     | 主な使い方例                               |
|---------------|-----------------|------------------------------------------|-------------------------------------------|
| `w`           | ダブリュー      | ログインユーザーと実行プロセス概要を表示     | `w`                                       |
| `who`         | フー            | ログインユーザーの一覧を表示               | `who`                                     |
| `hostname`    | ホストネーム    | 自ホスト名を表示                           | `hostname`                                |
| `host`        | ホスト          | ホスト名とIPアドレスの対応を調べる         | `host example.com`, `host 93.184.216.34`  |
| `dig`         | ディグ          | DNS情報を詳細に調べる                      | `dig example.com`                         |
| `ping`        | ピング          | ホストへの到達可能性と応答時間を確認       | `ping example.com`, `ping -c 4 example.com` |
| `ifconfig`    | イフコンフィグ  | (主にmacOS) ネットワークインターフェース設定表示 | `ifconfig en0`, `ifconfig`                |
| `ip addr show`| アイピー エーディーディーアール ショウ | (主にLinux) ネットワークインターフェース設定表示 | `ip addr show eth0`, `ip a`               |
| `nslookup`    | エヌエスルックアップ | (旧) ホスト名とIPアドレスの対応を調べる    | `nslookup example.com`                    |

これらのコマンドは、ネットワークを利用した作業や、ネットワークの問題解決の第一歩として役立つだろう。
