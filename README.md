﻿## ルール
#### 勝敗決定
 - ３つ〇を直線に並べると勝ち
 - ×を３つ並べられると負け
 - ×も〇も3つ並ばなかった場合は引き分け
 - 勝敗の判定はコンソールに表示される
 #### ターン
 - 先行後攻はゲーム開始時にランダムに決定される
 - 〇と×で交互にターンが切り替わる
 - 自分のターンでは画面中央の９つの〇ボタンから１つ選び押す
 - すでに〇か×が描画されているボタンは押しても変化はない
 ## 機能
 #### スタートボタン
 - 最初の一回目は押さないとゲームが開始しない
 - 最初の一回以降は機能なし
 #### リセットボタン
 - 描画されている〇×と勝敗判定の変数をリセットする
 - リセット後は自動で先行後攻が決定され、ゲームが開始する
 #### 戦績ボタン
 - 今までのゲーム勝敗数をコンソールに表示できる
 #### 戦績リセットボタン
 - カウントされていた勝敗数をすべて初期値に戻す
 ## 環境
 - Python3
 ##### ライブラリ
 - tkinter
 - random

