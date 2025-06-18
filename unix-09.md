# ネットワーク機能

UNIX系システム（WSL上のUbuntuやmacOSなど）は、ネットワークを通じて他のコンピュータと連携するための機能を備えている。この章では、ユーザー情報の確認、他のコンピュータへの接続、ネットワーク診断といった基本的なネットワーク関連のコマンドや概念について学ぶ。ネットワーク機能を活用することで、離れたところからのコンピュータ操作や、複数のコンピュータ間でのデータ共有が可能になる。

## ユーザー情報を調べる

UNIX系システムは、複数のユーザーが同時に一台のコンピュータを利用できるようになっている（マルチユーザーシステム）。ネットワーク経由での利用も一般的である。システムにログインしているユーザーを調べることで、同じコンピュータを利用している他のユーザーの状況を確認できる。

### 誰が何をしているか: `w` コマンド

現在システムにログインしているユーザーと、そのユーザーが実行しているプロセス（処理）の概要を表示するには `w` (ダブリュー) コマンドを使用する。「who and what（誰が何をしているか）」の略であると言われている。システム管理者は、このコマンドを使って現在の利用状況を確認することができる。

**WSL上のUbuntu**
```sh
w
 11:50:04 up 0 min,  1 user,  load average: 0.08, 0.02, 0.01
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
kokubo   pts/1    -                11:50    4.00s  0.02s  0.02s -bash
```

**macOS**
```sh
w
13:43  up  2:14, 2 users, load averages: 1.32 1.49 1.88
USER       TTY      FROM    LOGIN@  IDLE WHAT
kokubo     console  -      11:29    2:13 -
kokubo     s001     -      11:32       - w
```

この出力から、以下の情報が読み取れる。

*   1行目: 現在時刻、システムの稼働時間（2日と15時間30分）、現在のログインユーザー数（2人）、システムの平均負荷 (load average。数値が大きいほど混雑していることを示す)。
*   **USER**: ユーザー名である。この例では「user1」と「user2」の2人が利用中。
*   **TTY**: ユーザーが接続している端末名である (pts/0 などは仮想端末を示す)。
*   **FROM**: ユーザーがどこから接続しているか (IPアドレスやホスト名) を示す。ローカルログインの場合は空白になる。
*   **LOGIN@**: ログインした時刻である。user1は09:30に、user2は10:00にログインしている。
*   **IDLE**: アイドル時間 (最後にキー入力など操作をしてからの経過時間) である。user1は5時間何も操作していない。
*   **WHAT**: 現在実行中のコマンドである。user1は「-bash」（bashシェルを起動したまま）、user2は「w」コマンドを実行中である。

以前紹介した `who` (フー) コマンドよりも詳細な情報が得られる。

**WSL上のUbuntu**
```sh
who
kokubo   pts/1        2025-06-09 11:50
```

**masOS**
```sh
who
kokubo           console      May 21 11:29 
kokubo           ttys001      May 21 11:32
```

## ホスト名とIPアドレス

ネットワークに接続された各コンピュータは、「ホスト名」と「IPアドレス」という二つの識別子を持つ。

*   **ホスト名 (hostname)**: 人間が覚えやすいように付けられたコンピュータの名前である (例: `myserver`, `www.example.com`)。インターネットに公開されているサービスの場合は、「ドメイン名」の一部となる。
*   **IPアドレス (IP address)**: ネットワーク上でコンピュータを一意に識別するための数値的な住所である。住所のようなもので、このアドレスによってネットワーク上のどのコンピュータかを特定できる。現在主に使われているのは以下の2種類がある：
    - **IPv4 (Internet Protocol version 4)**: `192.168.1.10` や `93.184.216.34` のような、4つの数値（0～255）をドット（.）で区切った形式。
    - **IPv6 (Internet Protocol version 6)**: `2001:db8::1` や `2606:2800:220:1:248:1893:25c8:1946` のような、16進数で表現された長い形式。IPv4のアドレスが不足してきたため導入された、より多くのアドレスを扱える新しい形式。

### ホスト名を調べる: `hostname` コマンド

現在使用しているコンピュータのホスト名を表示するには `hostname` (ホストネーム) コマンドを使用する。ネットワーク設定の確認や、複数のコンピュータを操作しているときに現在どのコンピュータを使用しているか確認するのに役立つ。

**WSL上のUbuntu**
```sh
hostname
daivng5520m1
```

**macOS**
```sh
hostname
AtsushinoMacBook-Air.local
```

### ホスト名とIPアドレスの対応を調べる: `host` コマンド

ホスト名からIPアドレスを調べたり、逆にIPアドレスからホスト名を調べたりするには `host` (ホスト) コマンドを使用する。この処理を「名前解決 (name resolution)」と呼ぶ。これは、インターネット上の住所録のようなものであるDNS (Domain Name System) サーバーに問い合わせて行われる。ウェブサイトを閲覧するときも、背後では同様の処理が行われている。

WSL上のUbuntuの場合は以下の事前準備が一回だけ必要である。
```sh
sudo apt install bind9-host
```

WSL上のUbuntu、macOS共通の操作
```sh
host www.hi-tech.ac.jp
www.hi-tech.ac.jp has address 133.98.3.18                                                                                  
www.hi-tech.ac.jp has IPv6 address 2001:2f8:d3:1010::80
```

```sh
host 133.98.3.18
18.3.98.133.in-addr.arpa domain name pointer www.hi-tech.ac.jp.
```

最初の例では `www.hi-tech.ac.jp` というホスト名に対応するIPアドレス (IPv4とIPv6の両方) の情報が表示されている。次の例では、IPアドレス `133.98.3.18` に対応するホスト名（`www.hi-tech.ac.jp`）が表示されている。

より詳細な名前解決情報が必要な場合は `dig` (ディグ) (Domain Information Groper) コマンドが使われる。古いシステムでは `nslookup` (エヌエスルックアップ) コマンドも使われたが、現在は `host` (ホスト) や `dig` (ディグ) の使用が推奨される。

### ☆練習: ホスト名とIPアドレスを調べてみよう☆

1. `hostname` コマンドを実行して、自分のコンピュータのホスト名を確認しよう。
2. 有名なウェブサイト（例：google.com、amazon.com）の IPアドレスを `host` コマンドで調べてみよう。
   - IPv4アドレスとIPv6アドレスの両方が表示されるか確認する。
   - 同じウェブサイトでも複数のIPアドレスが表示される場合がある。なぜだろうか？
3. IPアドレス `8.8.8.8` を `host` コマンドで調べてみよう。どのサービスのIPアドレスだろうか？
   - ヒント: これはGoogle社が提供する公開DNSサーバーのアドレスである。

## ネットワークの状態を調べる

ネットワーク接続のトラブルシューティングなどに役立つコマンドをいくつか紹介する。

### 相手に届くか確認: `ping` コマンド

`ping` コマンドは、指定したホストに対してICMP (Internet Control Message Protocol) のエコー要求パケットと呼ばれる小さなデータパケットを送信し、相手ホストからエコー応答パケットが返ってくるかを確認することで、ネットワーク的な到達可能性を調べるために使われる。インターネット接続の確認や、ネットワーク障害の切り分けに便利なツールである。

```sh
ping example.com
PING example.com (23.215.0.138): 56 data bytes
64 bytes from 23.215.0.138: icmp_seq=0 ttl=47 time=205.120 ms
64 bytes from 23.215.0.138: icmp_seq=1 ttl=47 time=204.879 ms
64 bytes from 23.215.0.138: icmp_seq=2 ttl=47 time=204.961 ms
64 bytes from 23.215.0.138: icmp_seq=3 ttl=47 time=204.969 ms
64 bytes from 23.215.0.138: icmp_seq=4 ttl=47 time=204.921 ms
Ctrl + c
--- example.com ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 204.879/204.970/205.120/0.082 ms
```
<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">Ctrl</kbd>+<kbd class="keyboard-key nowrap" lang="en" style="border: 1px solid #aaa; border-radius: 2px; box-shadow: 1px 2px 2px #ddd; background-color: #f9f9f9; background-image: linear-gradient(top, #eee, #f9f9f9, #eee); padding: 1px 3px; font-family: inherit; font-size: 0.85em;">c</kbd> を押すと終了する。各行は、相手ホストからの応答を示しており、`time=` の部分が応答時間 (ミリ秒) である。最後の統計情報で、送信したパケット数 (transmitted)、受信したパケット数 (received)、失われたパケットの割合 (packet loss)、往復時間 (rtt) の最小/平均/最大/標準偏差などが表示される。応答時間 (time) が非常に大きい場合や、パケットロスが発生している場合は、ネットワーク経路に問題がある可能性が考えられる。

> **注意**: セキュリティ上の理由から、一部のサーバーやファイアウォールでは `ping` コマンドへの応答を制限していることがある。そのため、`ping` が応答を返さなくても、必ずしもサーバーがダウンしているとは限らない。また、公共のWi-Fiや一部の携帯電話ネットワークでも、`ping` が制限されていることがある。

### ネットワークインターフェースの情報を表示

コンピュータが持つネットワークアダプタ（ネットワークインターフェース）の設定情報（IPアドレス、MACアドレスなど）を表示するコマンドは、OSによって異なる。

**WSL上のUbuntu**

`ip addr show` コマンド (または短縮形の `ip a` (アイピー エー)) が推奨される。
```sh
ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:f8:dd:ae brd ff:ff:ff:ff:ff:ff
    inet 172.22.84.204/20 brd 172.22.95.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fef8:ddae/64 scope link
       valid_lft forever preferred_lft forever
```

`eth0` は最初のイーサネットインターフェースを指すことが多い。`inet` の行にIPv4アドレス (CIDR形式)、`inet6` の行にIPv6アドレス、`link/ether` の行にMACアドレスが表示される。

**macOS**

`ifconfig` (イフコンフィグ) コマンドが伝統的に使われる。
```sh
ifconfig -a
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
...
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 26:21:39:d6:8a:f6
	inet6 fe80::cc:6cc9:faab:cebc%en0 prefixlen 64 secured scopeid 0xb 
	inet 192.168.11.14 netmask 0xffffff00 broadcast 192.168.11.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
...
```

`en1` など、インターフェース名は環境によって異なる。`inet` の行にIPv4アドレス、`inet6` の行にIPv6アドレス、`ether` の行にMACアドレス（コンピュータのネットワークインターフェースに固有の物理アドレス）が表示される。


### 練習: ネットワーク状態を確認してみよう

1. `ping` コマンドで、インターネット上のウェブサイトとの接続を確認しよう。
   ```
   ping -c 4 google.com
   ```
   `-c 4` オプションは、4回のping要求を送信したら自動的に終了するという意味である。

2. 自分のコンピュータのネットワークインターフェース情報(自分のIPアドレス（IPv4）など)を確認しよう。
   
   **WSL上のUbuntu**
   ```
   ip addr show
   ```

   **macOS**
   ```
   ifconfig
   ```

## この章で紹介したコマンド

| コマンド       | 説明                                                | 例                                       |
|----------------|-----------------------------------------------------|------------------------------------------|
| `w`            | ログインユーザーと実行プロセス概要                  | `w`                                      |
| `who`          | ログインユーザーの一覧                              | `who`                                    |
| `hostname`     | ホスト名                                            | `hostname`                               |
| `host`         | ホスト名とIPアドレスの対応                          | `host example.com`, `host 93.184.216.34` |
| `ping`         | ホストへの到達可能性と応答時間                      | `ping example.com`                       |
| `ip addr show` | ネットワークインターフェース設定表示: WSL上のUbuntu | `ip addr show eth0`, `ip a`              |
| `ifconfig`     | ネットワークインターフェース設定表示: macOS         | `ifconfig en0`, `ifconfig`               |
