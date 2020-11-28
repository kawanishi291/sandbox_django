# sandbox_python

* Python 3.6.5
* pyxel 1.0.2
 
Environments under [Anaconda for Windows](https://www.anaconda.com/distribution/) is tested.

# 今後の予定
    
> **既存の機能**

**○オーナーの予約可能時間設定**

* 日にち指定で良い

**○管理者の駐車場仕様変更**

* ピンを立てるのは駐車場でなくステーション
* 収容台数。管理者チェックボックス。制限台数フラグを追加
* 車を追加する際にステーションと結びつける
* つまり駐車場を検索する際はステーション毎に予約する仕様
* 一つの駐車場IDに複数台追加可能
* 予約の際は駐車場を選んだ後、車両を選択

**○配車予測機能**

* 予測データから配車場所を追加する
* あらかじめ中心地となる座標を指定し格納
* 最も近い値の座標の地域IDをそれぞれ設定
* ステーションIDはより細かくする！
* 目安の数値を決めてそれ以下なら同じステーションIDを割り振り
* ステーションID毎に計算させる！

**○予約の重複を回避**

* 予約テーブルから検索

**○予約方法**

* 車から検索
* 時間から検索


> **新機能最低３つ**

* メール送信
* 電気自動車
* 特殊車両


> **デザイン**

* メディアクエリに対応させる為、cssを分解
* 動画や画像で使い方を説明
* 利用時の必要事項ページ作成


# proconEF($の付いているものはターミナルかコマンドプロンプトで実行)

# info
> **日付入力をカレンダー方式にする方法**

django-bootstrap-datepicker-plusをインストールし、フォームクラス上のwidgetにライブラリのクラスを指定
```
pip install django-bootstrap-datepicker-plus
```
参考サイト:[[Django] 日付入力欄をカレンダー形式にする (bootstrap-datetimepicker)](https://qiita.com/okoppe8/items/999b8e3c86708fbb3926)

 

> **DjangoにおけるDB操作_クエリメソッド（QueryAPI）_**

参考サイト:

[Django逆引きチートシート（QuerySet編）](https://qiita.com/uenosy/items/54136aff0f6373957d22#%E6%A4%9C%E7%B4%A2%E7%B3%BB)

[Django データベース操作 についてのまとめ](https://qiita.com/okoppe8/items/66a8747cf179a538355b)



# Gitコマンド&流れ(エラーや質問は森正or斉藤へ)
## 11/4日にやること(1回のみ！！！)
```
1. 翔ちゃんのGithub(proconEF)をForkする
2. $cd Desktop #自分のPCのデスクトップに移動 
3. $git clone 自分のGithubURL(proconEF)　#URL先のフォルダを自分のPC上にコピー
4. $cd proconEF #proconEFに移動
5. $git remote add remote 翔ちゃんのGithubURL(proconEF) #URL先のフォルダをremoteという名前で追加
6. $git update-index --skip-worktree Pipfile Pipfile.lock config/settings.py
7. VSCodeの左下のmainを押してorigin/djangoをクリック(branchを変更)
8. Djangoでの開発の流れの 11/4日にやること(1回のみ！！！)を実行
```

## 毎回開発の前にやること(proconEFフォルダ内で)
```
1. VSCodeの左下のmainを押してdjangoをクリック(branchを変更)
2. $git pull remote django #前日の変更をローカルに適用
3. 仮想環境の設定を実行
```

## 毎回開発後にやること(proconEFフォルダ内で)
```
1. $git add .
2. $git commit -m "コメント入力"
3. $git push origin django #１,2,3,を実行することで自分のGithubのproconEFのdjangoブランチに変更が送られる
4. Githubのcode下にあるmain▼をdjangoに変更
5. Githubからpull requestsをクリック→翔ちゃんのproconEF djangoに自分のproconEF djangoからcreate pull requestを作成
```

# Djangoでの開発の流れ 
## 11/4日にやること(1回のみ！！！)
```
1. $cd Desktop #Desktopに移動
2. $pip install pipenv
3. 仮想環境の設定を実行
```

## 仮想環境の設定(開発の時毎回やる)
```
$cd Desktop
$cd proconEF
$pipenv install #仮想環境の作成
$pipenv shell #仮想環境に入る(VSCodeのshellが$pipenv or Python~に変わっているか確認)
```

## Djangoコマンド
```
python manage.py makemigrations #データベースにテーブル作成
python manage.py migrate #データベースへ反映
python manage.py createsuperuser #管理者アカウントの作成
python manage.py runserver #サーバー起動
```

