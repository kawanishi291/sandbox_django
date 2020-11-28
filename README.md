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
__*carsharing_req(カーシェアリング利用登録)*__
*ボス*
1. models.pyにCarsharUserModel[class]を追加
2. forms.pyを作成し、models.pyで作ったmodelをimport
```bash
from.models import CarsharUserModel
```
3. forms.pyにCarsharUserModelを継承させたCarsharUserCreateForm[class]を記入
```bash
class CarsharUserCreateForm(forms.ModelForm):
    class Meta:
        model = CarsharUserModel
        fields = ['id', 'name', 'mail', ... ]
```

2. views.pyにTemplateViewをimport
```bash
from django.views.generic import TemplateView
```
3. views.pyにCarsharUser[class]を宣言(TemplateViewを使用)
4. views.pyのCarsharUser[class]にコンストラクタを設定
```bash
def __init__(self):
        self.params = {
            'title': 'タイトル',
        }
```
params内に使用変数を定義

4. urls.pyにviews.py内で宣言したCarsharUser[class]をimport
```bash
from .views import CarsharUser
```
5. urls.pyに以下の記述でアプリケーション名を追記
```bash
app_name = 'carsharing_req'
```
6. urls.pyにCarsharUserclassのディレクトリを追記
```bash
path('index/', CarsharUser.as_view(), name='index')
```

7. ルートディレクトリ直下のtemplatesフォルダ内にcarsharing_reqフォルダを作成
```bash
$ mkdir carsharing_req
```
8. carsharing_reqフォルダ内にindex.htmlを作成
```bash
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
    <title>{{ title }}</title>
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{ title }}</h1>
    <p class="h5 mt-4">{{ message|safe }}</p>
    <form action="{% url 'index' %}" method="post">
        {% csrf_token %}
        {{ form.as_table }}
        <input class="btn btn-primary my-2" type="submit" value="click">
    </form>
</body>
</html>
```
9. さあ、runserverしてみよう

__*carsharing_booking(カーシェア予約)*__
*おおにしちゃん＆はっしー*


__*owners_req(カーシェアオーナー申請)*__
*おおにしちゃん*
1. ログインしているか確認するコントローラ[views.py]
2. DBへ登録する内容のClass[models.py]
3. 登録画面のフォーム[forms.py]
4. バリデーション機能[views.py]
5. オーナー詳細画面[views.py]
6. 変更コントローラ（登録と同様に）[views.py]
7. 削除コントローラ（登録と同様に）[views.py]
8. HTMLのコンポーネント化[base.html]の継承
9. デザイン変更


__*parking_req(駐車場オーナー申請)*__
*はっしー*
1. ログインしているか確認するコントローラ[views.py]
2. DBへ登録する内容の駐車場登録Class追加[models.py]
3. 登録画面のフォーム[forms.py]
4. バリデーション機能[views.py]
5. オーナー詳細画面[views.py]
6. 変更コントローラ（登録と同様に）[views.py]
7. 削除コントローラ（登録と同様に）[views.py]
8. HTMLのコンポーネント化[base.html]の継承
9. デザイン変更


__*secondhandcar(中古車提案)*__
*ボス*


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

