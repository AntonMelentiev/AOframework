# Allure

Install Allure on Ubuntu:
```
curl -o allure-2.21.0.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.21.0.tgz
sudo tar -zxvf allure-2.21.0.tgz -C /opt/
sudo ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure
allure --version
```