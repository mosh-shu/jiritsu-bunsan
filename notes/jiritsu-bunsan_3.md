# 自律分散協調システム

### 20190422

## 分散プログラムのモデル

- 並行プロセスモデル
    - program = a set of cooperating processes
- 並行オブジェクトモデル
    - program = a set of cooperating objects
- unicast, multicast, broadcast... one-to-one, one-to-many, one-to-all

## 並行オブジェクトプロセス

- Blocking Send... 相手からのリスポンスをずっと待つ
- Non-blocking Send... 相手からのリスポンスに関係なく次のステップに進む
- Send, Recieve療法ある
- LINEでイメージすると既読/メッセージをずっと待つ人 vs 送りっぱなし/チェックだけする人
- Static Workerモデル... 有限個しかプロセスを回さない
- Dynamic Workerモデル... ダイナミックにプロセスの個数を調節する

## 並行プロセスの挙動

- Process P1 <-> Process P2
- でループができるとDeadlock状態になる
    - システムを構成しているすべてのプロセスが起きるはずのない事象を待ち続ける状態
    - 「仮の状態」 を作ってとく
- Pipeline
    - 皿洗いの例
    - blocking-sendだと、皿を洗う人は次のプロセスにいる皿を拭く人が受け取ってくれるまで動けない
- Dynamic Worker Model
    - Brecanyでリクエストを受け取ると, そのたびにWorkerを作り, その中での処理を受け取りぐちに返す
- Static Worker Model
    - ワーカー「仕事頂戴！」と言われたらこれをタスクキューに入れ、仕事が車でまつ
- Distributed Partitioned Sort
    - 分散的にソートする (P1~P3でカードを小さい順に並べる. 一番小さいのがP1, 一番大きいのがP3に行くようにカードを受け渡す).
    - それぞれのプロセスは自分のlocal stateしか観察できないが, global stateとしてsortできる
    -



