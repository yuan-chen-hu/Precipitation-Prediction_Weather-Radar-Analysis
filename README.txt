###############DEMO網站網址######################
雷達回波預報網站:
https://reurl.cc/9dE4d
可點進去看，架在免費的後端資料庫有點慢要等一下
###############可執行檔案說明####################
./dist/python20191225final.exe

0.  執行上面的檔案

1.  執行後等待
1.1 網路記得開啟
1.2 請用window系統
1.3 ./dist/裡面的資料不要動
1.4 如果有防火牆等問題，要重新啟動exe檔案
1.5 terminal會顯示一切進度、天氣資料與資訊
2.  會自動下載一2020xxxxxxxx.xml檔案(不同時間的即時雷達回波檔案)
3.  會開啟網頁進行爬蟲
4.  資料會上傳
    雷達回波預報網站: 
    https://reurl.cc/9dE4d
    可以去check

5.  跑完會關閉所有firefox
6.  沒關掉exe的話每幾分鐘會確定中央氣象局有沒有更新雷達回波
7.  有的話就會自己重跑更新重新上傳
8.  有時候會error雖然會自己restart查了應該是pyinstsaller轉成exe時版本不相容...

###############Python .py 檔案說明###############

Python20191225final.py =>主要運行檔案
Python20191224final.py =>主要運行檔案舊檔

svr_training.py	       =>svr training檔案

delete_Test.py         =>網站資料庫刪除測試檔案

geckodriver.exe        =>爬蟲要用到的
geckodriver.log        =>爬蟲要用到的
ghostdriver.log        =>爬蟲要用到的

scaler.pkl	       =>svr training模型相關
svr_model.pkl          =>svr training模型結果