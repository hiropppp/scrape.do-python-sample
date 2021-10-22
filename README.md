# イメージ作成
docker build -t scrape_do:1.0 /mnt/c/wsl/docker/dev/scrape.do-python-sample/.devcontainer --no-cache

# コンテナ作成
docker run -v /mnt/c/wsl/docker/dev/scrape.do-python-sample:/opt/python/scrape_do --name scrape_do_01 -i -t scrape_do:1.0 /bin/bash

# scrape.doのAPIトークンの設定
scrape.doのダッシュボードに記載のＡＰＩトークンをconfig.pyのAPI_TOKENに設定