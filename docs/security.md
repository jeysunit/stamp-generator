# セキュリティ

## 基本方針

- 画像や入力データを永続保存しない
- ログに入力データを残さない
- 秘密情報をコミットしない

## セキュリティヘッダ

FastAPI のミドルウェアで以下のヘッダを付与します。

- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy

## 追加予定

- 画像生成機能実装時の入力バリデーション
- レート制限などの運用対策
