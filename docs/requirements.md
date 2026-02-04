# 要件定義

## 初期機能

- トップページに「文字スタンプ生成フォーム」のみ配置
- 画像アップロードは未実装
- 出力サイズは複数プリセット（128 / 256 / 512）

## 将来機能（未実装）

- 文字入力 → スタンプ画像生成
- 写真入力 → スタンプ画像生成
- 写真は fit（余白で合わせる）
- テンプレ: シンプル / 縁取り / 吹き出し

## 技術要件

- Python 3.11
- FastAPI / Uvicorn
- Jinja2（サーバレンダリング）
- 画像処理は Pillow（後続実装）
- Docker 前提
- デプロイ先は Google Cloud Run

## Cloud Run 制約

- Dockerfile は python:3.11-slim ベース
- root ユーザーで実行しない（非 root user を作成する）
- Cloud Run の $PORT 環境変数を使用する
- 永続ストレージを使用しない
- 1 コンテナで完結する構成
- 本番コンテナには開発用ツールを含めない

## 依存管理

- 本番依存と開発依存を分離
  - requirements.txt（本番）
  - requirements-dev.txt（lint / test）
- CI では両方をインストール
- Dockerfile では本番依存のみをインストール
