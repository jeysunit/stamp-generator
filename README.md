# スタンプ画像生成（サーバレンダリング）

FastAPI + Jinja2 による「Slack 等向けスタンプ画像生成」Web アプリの初期構成です。Cloud Run にデプロイする前提で、非 root 実行や $PORT 利用などのベストプラクティスに従っています。

## 主要機能（初期）

- トップページに「文字スタンプ生成フォーム」のみ配置
- 画像アップロードは未実装
- 出力サイズは複数プリセット（128 / 256 / 512）

## 技術スタック

- Python 3.11
- FastAPI / Uvicorn
- Jinja2
- Docker

## ローカル実行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

ブラウザで `http://localhost:8080` を開きます。

## Cloud Run デプロイ手順（推奨設定）

1. コンテナをビルドして Artifact Registry に push します。

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com artifactregistry.googleapis.com

gcloud artifacts repositories create stamp-generator \
  --repository-format=docker \
  --location=asia-northeast1

gcloud auth configure-docker asia-northeast1-docker.pkg.dev

docker build -t asia-northeast1-docker.pkg.dev/YOUR_PROJECT_ID/stamp-generator/app:latest .
docker push asia-northeast1-docker.pkg.dev/YOUR_PROJECT_ID/stamp-generator/app:latest
```

2. Cloud Run へデプロイします。

```bash
gcloud run deploy stamp-generator \
  --image asia-northeast1-docker.pkg.dev/YOUR_PROJECT_ID/stamp-generator/app:latest \
  --region asia-northeast1 \
  --platform managed \
  --allow-unauthenticated \
  --port 8080 \
  --min-instances 0 \
  --max-instances 3 \
  --memory 512Mi \
  --cpu 1
```

### 推奨事項

- コンテナは非 root ユーザーで実行（Dockerfile 対応済み）
- Cloud Run の $PORT を使用（Dockerfile 対応済み）
- 永続ストレージを使用しない（このアプリは保存しません）
- 1 コンテナで完結する構成

## ドキュメント

- 要件: `docs/requirements.md`
- セキュリティ: `docs/security.md`
- プライバシー: `docs/privacy.md`
- フォント: `docs/fonts.md`

## ライセンス

MIT License
