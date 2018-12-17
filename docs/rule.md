# コンセプト

## 自己相関性をもったアーキテクチャ
Fractal: クライアントもサーバも同一。
DNA: WALもHALも同一のConfigから生成される。(Config中心)
Flash: 各レイヤーは今ある情報しか持たない。(過去情報を持たない)

# サポート端末
Raspberry Pi3 (Python3)

# アーキテクチャ

## 概念設計
Web API (REST)
 ↓↑
Controller ⇔ Config
 ↓↑
Hardware

## 外部設計
WAL (Web API Access Layer)
Core (TRAI Core)
HAL (Hardware Access Layer)

## 内部設計
JSONエコノミー
　Edge
   hardware name (who)
   value (what)
   time (when)
   GPIO (where)
   "edge" (why)
   Program command with parametor (how)

　Node
   hostname (who)
   value (what)
    -> Edge
    -> Node
   time (when)
   IP (where)
   "node" (why)
   Request method with parametor (how)

### モジュール設計

# 制約

## 設計ルール

## コーディングルール

# Lint
pylint
flake8
pep 257(pydocstyle)

Recommend
mypy

# バージョンナンバーのナンバリングルール

## コンセプトナンバー x.*.*.*
概念設計設計にレベルのナンバリング。データの管理や仕組み等、根幹のコンセプトの世代番号。

## メジャーナンバー *.x.*.*
大規模な機能追加や節目の世代番号。

## マイナーナンバー
*.*.x.*
バグフィックスやセキュリティアップデート等による更新世代番号。

## ラウンドナンバー
開発者向け世代番号。ソース管理におけるリビジョン番号に近いが、マイナーナンバー毎に0からカウントし直す。