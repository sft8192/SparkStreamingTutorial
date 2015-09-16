# Spark-Streaming-Test

spark streamingのチュートリアルプログラム

## Description

echo-serverを建ててspark-streamingが動作していることを確認することが可能

## Requirement

Python2系が必要

## Usage

echo_sercer.pyを起動

`$ python echo_server.py`

spark-streaming-sample直下に移動

`$sbt`

`$run`



echo_serverに接続すると、echo_serverがクライアントへ１秒毎に英文を流す
sparkは送られてきた英文の中からbutを含む英文を5秒毎に出力する
