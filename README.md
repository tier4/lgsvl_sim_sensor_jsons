# これは何
- LGSVL-Simulator向け
- lidarのverticalrayanglesを
- linearでない角度で設定された
- jsonを用意した
repositoryです

# LGSVL-Simulator

https://www.lgsvlsimulator.com/
にあるシミュレータです。

# verticalrayanglesをlinearでない角度で

https://github.com/ros-drivers/velodyne/tree/master/velodyne_pointcloud/params
ここに有るyamlの定義からデータを抽出しました。

# jsonの用意(データの作成方法)


``` $ python3 ve.py {https://github.com/ros-drivers/velodyne/tree/master/velodyne_pointcloud/params のyamlファイル} ```


を実行すると、stdoutにyamlから必要なパラメータを抽出した値がstdoutに出力されます。  
その値をjsonのverticalrayanglesの配列にcopy&pasteして下さい。  


jsonのテンプレートファイルは  
**lidar_params/default.lidar.json**  

に用意してあります。このファイルを使用して下さい。  
