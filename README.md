# ROS2 package
本リポジトリは, 千葉工業大学先進工学部未来ロボティクス学科 ロボットシステム学(2024~2025)の課題2で使用したリポジトリです.

### 概要
このリポジトリはROS2で動作します. 
- talker: ランダムな文章をトピックにパブリッシュします.
- listener: トピックからメッセージを受信し,単語数と文字数をカウントします.

### 使用方法
ランダムな文章(英語)をトピックにパブリッシュするtalkerノードを起動します.
'''
ros2 run mypkg talker
'''
もう一つのターミナルを起動し, トピックからメッセージを受け取り, 単語数と文字数をカウントするlistenerノードを起動します.
'''
ros2 run mypkg listener
'''

### 実行例
terminal 1
'''
[INFO] [talker]: Publishing: "I have a pen."
[INFO] [talker]: Publishing: "Thank you."
'''
terminal 2
'''
[INFO] [listener]: Received: "I have a pen." (Word count: 5, Character count: 12)
[INFO] [listener]: Received: "Thank you." (Word count: 2, Character count: 10)
'''

### 注意書き
・日本語のテキスト処理には対応していません.

・極端に長い文字列を処理すると, システムのパフォーマンスに影響を与える可能性があります.

### ソフトウェア

### テスト環境
