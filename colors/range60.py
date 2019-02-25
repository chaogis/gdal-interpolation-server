#-*-coding=utf-8-*-
'''
Created on 2018-11-27

@author: chao_qin
@description: 60色阶方案
'''
#60色阶
colors = [
  '#36D281',
  '#41D178',
  '#4DD070',
  '#57CF67',
  '#64CD5D',
  '#6ECC56',
  '#7BCB4D',
  '#8CCD44',
  '#9BCF3A',
  '#ADD131',

  '#C3D325',
  '#D2D51C',
  '#E2D613',
  '#F3D708',
  '#FFD802',
  '#FFD501',
  '#FFD301',
  '#FFD101',
  '#FFCF01',
  '#FFCC01',

  '#FFC900',
  '#FFC500',
  '#FFB700',
  '#FFA700',
  '#FF9A00',
  '#FF8A01',
  '#FF7901',
  '#FF6A01',
  '#FF5C01',
  '#FC4F05',

  '#F94208',
  '#F5350C',
  '#F1270F',
  '#EE1A12',
  '#EA0D15',
  '#E7001A',
  '#DF0020',
  '#D60128',
  '#CC0030',
  '#C20137',

  '#BA013F',
  '#AF0147',
  '#A6014E',
  '#9D0157',
  '#93015D',
  '#91015B',
  '#8E0257',
  '#8C0354',
  '#890351',
  '#86034E',

  '#84044B',
  '#830549',
  '#800545',
  '#7C0641',
  '#76073A',
  '#700932',
  '#69092A',
  '#630B23',
  '#5D0B1B',
  '#570C14'
]

aqi = [
    # 1 - 10
    [0, 5],
    [5.00000000000001, 10],
    [10.00000000000001, 15],
    [15.00000000000001, 20],
    [20.00000000000001, 25],
    [25.00000000000001, 30],
    [30.00000000000001, 35],
    [35.00000000000001, 40],
    [40.00000000000001, 45],
    [45.00000000000001, 50],
    # 11 - 20
    [50.00000000000001, 55],
    [55.00000000000001, 60],
    [60.00000000000001, 65],
    [65.00000000000001, 70],
    [70.00000000000001, 75],
    [75.00000000000001, 80],
    [80.00000000000001, 85],
    [85.00000000000001, 90],
    [90.00000000000001, 95],
    [95.00000000000001, 100],
    # 21 -30
    [100.00000000000001, 105],
    [105.00000000000001, 110],
    [110.00000000000001, 115],
    [115.00000000000001, 120],
    [120.00000000000001, 125],
    [125.00000000000001, 130],
    [130.00000000000001, 135],
    [135.00000000000001, 140],
    [140.00000000000001, 145],
    [145.00000000000001, 150],
    # 31 - 40
    [150.00000000000001, 155],
    [155.00000000000001, 160],
    [160.00000000000001, 165],
    [165.00000000000001, 170],
    [170.00000000000001, 175],
    [175.00000000000001, 180],
    [180.00000000000001, 185],
    [185.00000000000001, 190],
    [190.00000000000001, 195],
    [195.00000000000001, 200],
    # 41 - 50
    [200.00000000000001, 210],
    [210.00000000000001, 220],
    [220.00000000000001, 230],
    [230.00000000000001, 240],
    [240.00000000000001, 250],
    [250.00000000000001, 260],
    [260.00000000000001, 270],
    [270.00000000000001, 280],
    [280.00000000000001, 290],
    [290.00000000000001, 300],
    # 51 - 60
    [300.00000000000001, 320],
    [320.00000000000001, 340],
    [340.00000000000001, 360],
    [360.00000000000001, 380],
    [380.00000000000001, 400],
    [400.00000000000001, 420],
    [420.00000000000001, 440],
    [440.00000000000001, 460],
    [460.00000000000001, 480],
    [480.00000000000001, 500]
]

pm10 = [
    # 1 - 10
    [0, 5],
    [5.00000000000001, 10],
    [10.00000000000001, 15],
    [15.00000000000001, 20],
    [20.00000000000001, 25],
    [25.00000000000001, 30],
    [30.00000000000001, 35],
    [35.00000000000001, 40],
    [40.00000000000001, 45],
    [45.00000000000001, 50],
    # 11 - 20
    [50.00000000000001, 60],
    [60.00000000000001, 70],
    [70.00000000000001, 80],
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    [100.00000000000001, 110],
    [110.00000000000001, 120],
    [120.00000000000001, 130],
    [130.00000000000001, 140],
    [140.00000000000001, 150],
    # 21 - 30
    [150.00000000000001, 160],
    [160.00000000000001, 170],
    [170.00000000000001, 180],
    [180.00000000000001, 190],
    [190.00000000000001, 200],
    [200.00000000000001, 210],
    [210.00000000000001, 220],
    [220.00000000000001, 230],
    [230.00000000000001, 240],
    [240.00000000000001, 250],
    # 31 - 40
    [250.00000000000001, 260],
    [260.00000000000001, 270],
    [270.00000000000001, 280],
    [280.00000000000001, 290],
    [290.00000000000001, 300],
    [300.00000000000001, 310],
    [310.00000000000001, 320],
    [320.00000000000001, 330],
    [330.00000000000001, 340],
    [340.00000000000001, 350],
    # 41 - 50
    [350.00000000000001, 357],
    [357.00000000000001, 364],
    [364.00000000000001, 371],
    [371.00000000000001, 378],
    [378.00000000000001, 385],
    [385.00000000000001, 392],
    [392.00000000000001, 399],
    [399.00000000000001, 406],
    [406.00000000000001, 413],
    [413.00000000000001, 420],
    # 50 - 60
    [420.00000000000001, 438],
    [438.00000000000001, 456],
    [456.00000000000001, 474],
    [474.00000000000001, 492],
    [492.00000000000001, 510],
    [510.00000000000001, 528],
    [528.00000000000001, 546],
    [546.00000000000001, 564],
    [564.00000000000001, 582],
    # [582.00000000000001, 600]
    [582.00000000000001, 1000]
]

pm25 = [
    # 1 - 10
    [0, 3.5],
    [3.50000000000001, 7],
    [7.00000000000001, 10.5],
    [10.50000000000001, 14],
    [14.00000000000001, 17.5],
    [17.50000000000001, 21],
    [21.00000000000001, 24.5],
    [24.50000000000001, 28],
    [28.00000000000001, 31.5],
    [31.50000000000001, 35],
    # 11 - 20
    [35.00000000000001, 39],
    [39.00000000000001, 43],
    [43.00000000000001, 47],
    [47.00000000000001, 51],
    [51.00000000000001, 55],
    [55.00000000000001, 59],
    [59.00000000000001, 63],
    [63.00000000000001, 67],
    [67.00000000000001, 71],
    [71.00000000000001, 75],
    # 21 -30
    [75.00000000000001, 79],
    [79.00000000000001, 83],
    [83.00000000000001, 87],
    [87.00000000000001, 91],
    [91.00000000000001, 95],
    [95.00000000000001, 99],
    [99.00000000000001, 103],
    [103.00000000000001, 107],
    [107.00000000000001, 111],
    [111.00000000000001, 115],
    # 30 - 40
    [115.00000000000001, 118.5],
    [118.50000000000001, 122],
    [122.00000000000001, 125.5],
    [125.50000000000001, 129],
    [129.00000000000001, 132.5],
    [132.50000000000001, 136],
    [136.00000000000001, 139.5],
    [139.50000000000001, 143],
    [143.00000000000001, 146.5],
    [146.50000000000001, 150],
    # 41 - 50
    [150.00000000000001, 160],
    [160.00000000000001, 170],
    [170.00000000000001, 180],
    [180.00000000000001, 190],
    [190.00000000000001, 200],
    [200.00000000000001, 210],
    [210.00000000000001, 220],
    [220.00000000000001, 230],
    [230.00000000000001, 240],
    [240.00000000000001, 250],
    # 50 - 60
    [250.00000000000001, 275],
    [275.00000000000001, 300],
    [300.00000000000001, 325],
    [325.00000000000001, 350],
    [350.00000000000001, 375],
    [375.00000000000001, 400],
    [400.00000000000001, 425],
    [425.00000000000001, 450],
    [450.00000000000001, 475],
    # [475.00000000000001, 500]
    [475.00000000000001, 1000]
]

hour_no2 = [
    # 1 - 10
    [0, 10],
    [10.00000000000001, 20],
    [20.00000000000001, 30],
    [30.00000000000001, 40],
    [40.00000000000001, 50],
    [50.00000000000001, 60],
    [60.00000000000001, 70],
    [70.00000000000001, 80],
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    # 11 - 20
    [100.00000000000001, 110],
    [110.00000000000001, 120],
    [120.00000000000001, 130],
    [130.00000000000001, 140],
    [140.00000000000001, 150],
    [150.00000000000001, 160],
    [160.00000000000001, 170],
    [170.00000000000001, 180],
    [180.00000000000001, 190],
    [190.00000000000001, 200],
    # 21 -30
    [200.00000000000001, 250],
    [250.00000000000001, 300],
    [300.00000000000001, 350],
    [350.00000000000001, 400],
    [400.00000000000001, 450],
    [450.00000000000001, 500],
    [500.00000000000001, 550],
    [550.00000000000001, 600],
    [600.00000000000001, 650],
    [650.00000000000001, 700],
    # 30 - 40
    [700.00000000000001, 750],
    [750.00000000000001, 800],
    [800.00000000000001, 850],
    [850.00000000000001, 900],
    [900.00000000000001, 950],
    [950.00000000000001, 1000],
    [1000.00000000000001, 1050],
    [1050.00000000000001, 1100],
    [1100.00000000000001, 1150],
    [1150.00000000000001, 1200],
    # 40 - 50
    [1200.00000000000001, 1314],
    [1314.00000000000001, 1428],
    [1428.00000000000001, 1542],
    [1542.00000000000001, 1656],
    [1656.00000000000001, 1770],
    [1770.00000000000001, 1884],
    [1884.00000000000001, 1998],
    [1998.00000000000001, 2112],
    [2112.00000000000001, 2226],
    [2226.00000000000001, 2340],
    # 50 - 60
    [2340.00000000000001, 2490],
    [2490.00000000000001, 2640],
    [2640.00000000000001, 2790],
    [2790.00000000000001, 2940],
    [2940.00000000000001, 3090],
    [3090.00000000000001, 3240],
    [3240.00000000000001, 3390],
    [3390.00000000000001, 3540],
    [3540.00000000000001, 3690],
    # [3690.00000000000001, 3840]
    [3690.00000000000001, 5000]
]

hour_o3 = [
    # 1 - 10
    [0, 16],
    [16.00000000000001, 32],
    [32.00000000000001, 48],
    [48.00000000000001, 64],
    [64.00000000000001, 80],
    [80.00000000000001, 96],
    [96.00000000000001, 112],
    [112.00000000000001, 128],
    [128.00000000000001, 144],
    [144.00000000000001, 160],
    # 11 - 20
    [160.00000000000001, 164],
    [164.00000000000001, 168],
    [168.00000000000001, 172],
    [172.00000000000001, 176],
    [176.00000000000001, 180],
    [180.00000000000001, 184],
    [184.00000000000001, 188],
    [188.00000000000001, 192],
    [192.00000000000001, 196],
    [196.00000000000001, 200],
    # 21 - 30
    [200.00000000000001, 210],
    [210.00000000000001, 220],
    [220.00000000000001, 230],
    [230.00000000000001, 240],
    [240.00000000000001, 250],
    [250.00000000000001, 260],
    [260.00000000000001, 270],
    [270.00000000000001, 280],
    [280.00000000000001, 290],
    [290.00000000000001, 300],
    # 31 - 40
    [300.00000000000001, 310],
    [310.00000000000001, 320],
    [320.00000000000001, 330],
    [330.00000000000001, 340],
    [340.00000000000001, 350],
    [350.00000000000001, 360],
    [360.00000000000001, 370],
    [370.00000000000001, 380],
    [380.00000000000001, 390],
    [390.00000000000001, 400],
    # 41 - 50
    [400.00000000000001, 440],
    [440.00000000000001, 480],
    [480.00000000000001, 520],
    [520.00000000000001, 560],
    [560.00000000000001, 600],
    [600.00000000000001, 640],
    [640.00000000000001, 680],
    [680.00000000000001, 720],
    [720.00000000000001, 760],
    [760.00000000000001, 800],
    # 50 - 60
    [800.00000000000001, 840],
    [840.00000000000001, 880],
    [880.00000000000001, 920],
    [920.00000000000001, 960],
    [960.00000000000001, 1000],
    [1000.00000000000001, 1040],
    [1040.00000000000001, 1080],
    [1080.00000000000001, 1120],
    [1120.00000000000001, 1160],
    # [1160.00000000000001, 1200]
    [1160.00000000000001, 2000]
]

hour_co = [
    # 1 - 10
    [0, 0.5],
    [0.50000000000001, 1],
    [1.00000000000001, 1.5],
    [1.50000000000001, 2],
    [2.00000000000001, 2.5],
    [2.50000000000001, 3],
    [3.00000000000001, 3.5],
    [3.50000000000001, 4],
    [4.00000000000001, 4.5],
    [4.50000000000001, 5],
    # 10 - 20
    [5.00000000000001, 5.5],
    [5.50000000000001, 6],
    [6.00000000000001, 6.5],
    [6.50000000000001, 7],
    [7.00000000000001, 7.5],
    [7.50000000000001, 8],
    [8.00000000000001, 8.5],
    [8.50000000000001, 9],
    [9.00000000000001, 9.5],
    [9.50000000000001, 10],
    # 21 -30
    [10.00000000000001, 12.5],
    [12.50000000000001, 15],
    [15.00000000000001, 17.5],
    [17.50000000000001, 20],
    [20.00000000000001, 22.5],
    [22.50000000000001, 25],
    [25.00000000000001, 27.5],
    [27.50000000000001, 30],
    [30.00000000000001, 32.5],
    [32.50000000000001, 35],
    # 31 - 40
    [35.00000000000001, 37.5],
    [37.50000000000001, 40],
    [40.00000000000001, 42.5],
    [42.50000000000001, 45],
    [45.00000000000001, 47.5],
    [47.50000000000001, 50],
    [50.00000000000001, 52.5],
    [52.50000000000001, 55],
    [55.00000000000001, 57.5],
    [57.50000000000001, 60],
    # 41 - 50
    [60.00000000000001, 63],
    [63.00000000000001, 66],
    [66.00000000000001, 69],
    [69.00000000000001, 72],
    [72.00000000000001, 75],
    [75.00000000000001, 78],
    [78.00000000000001, 81],
    [81.00000000000001, 84],
    [84.00000000000001, 87],
    [87.00000000000001, 90],
    # 51 - 60
    [90.00000000000001, 96],
    [96.00000000000001, 102],
    [102.00000000000001, 108],
    [108.00000000000001, 114],
    [114.00000000000001, 120],
    [120.00000000000001, 126],
    [126.00000000000001, 132],
    [132.00000000000001, 138],
    [138.00000000000001, 144],
    # [144.00000000000001, 150]
    [144.00000000000001, 500]
]

hour_so2 = [
    # 1 - 10
    [0, 15],
    [15.00000000000001, 30],
    [30.00000000000001, 45],
    [45.00000000000001, 60],
    [60.00000000000001, 75],
    [75.00000000000001, 90],
    [90.00000000000001, 105],
    [105.00000000000001, 120],
    [120.00000000000001, 135],
    [135.00000000000001, 150],
    # 11 - 20
    [150.00000000000001, 185],
    [185.00000000000001, 220],
    [220.00000000000001, 255],
    [255.00000000000001, 290],
    [290.00000000000001, 325],
    [325.00000000000001, 360],
    [360.00000000000001, 395],
    [395.00000000000001, 430],
    [430.00000000000001, 465],
    [465.00000000000001, 500],
    # 21 -30
    [500.00000000000001, 515],
    [515.00000000000001, 530],
    [530.00000000000001, 545],
    [545.00000000000001, 560],
    [560.00000000000001, 575],
    [575.00000000000001, 590],
    [590.00000000000001, 605],
    [605.00000000000001, 620],
    [620.00000000000001, 635],
    [635.00000000000001, 650],
    # 31 - 40
    [650.00000000000001, 665],
    [665.00000000000001, 680],
    [680.00000000000001, 695],
    [695.00000000000001, 710],
    [710.00000000000001, 725],
    [725.00000000000001, 740],
    [740.00000000000001, 755],
    [755.00000000000001, 770],
    [770.00000000000001, 785],
    [785.00000000000001, 800],
    # 41
    [800.00000000000001, 2000]
]

day_no2 = [
    # 1 - 10
    [0, 4],
    [4.00000000000001, 8],
    [8.00000000000001, 12],
    [12.00000000000001, 16],
    [16.00000000000001, 20],
    [20.00000000000001, 24],
    [24.00000000000001, 28],
    [28.00000000000001, 32],
    [32.00000000000001, 36],
    [36.00000000000001, 40],
    # 11 - 20
    [40.00000000000001, 44],
    [44.00000000000001, 48],
    [48.00000000000001, 52],
    [52.00000000000001, 56],
    [56.00000000000001, 60],
    [60.00000000000001, 64],
    [64.00000000000001, 68],
    [68.00000000000001, 72],
    [72.00000000000001, 76],
    [76.00000000000001, 80],
    # 21 -30
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    [100.00000000000001, 110],
    [110.00000000000001, 120],
    [120.00000000000001, 130],
    [130.00000000000001, 140],
    [140.00000000000001, 150],
    [150.00000000000001, 160],
    [160.00000000000001, 170],
    [170.00000000000001, 180],
    # 31 - 40
    [180.00000000000001, 190],
    [190.00000000000001, 200],
    [200.00000000000001, 210],
    [210.00000000000001, 220],
    [220.00000000000001, 230],
    [230.00000000000001, 240],
    [240.00000000000001, 250],
    [250.00000000000001, 260],
    [260.00000000000001, 270],
    [270.00000000000001, 280],
    # 41 - 50
    [280.00000000000001, 308.5],
    [308.50000000000001, 337],
    [337.00000000000001, 365.5],
    [365.50000000000001, 394],
    [394.00000000000001, 422.5],
    [422.50000000000001, 451],
    [451.00000000000001, 479.5],
    [479.50000000000001, 508],
    [508.00000000000001, 536.5],
    [536.50000000000001, 565],
    # 51 - 60
    [565.00000000000001, 602.5],
    [602.50000000000001, 640],
    [640.00000000000001, 677.5],
    [677.50000000000001, 715],
    [715.00000000000001, 752.5],
    [752.50000000000001, 790],
    [790.00000000000001, 827.5],
    [827.50000000000001, 865],
    [865.00000000000001, 902.5],
    # [902.50000000000001, 940]
    [902.50000000000001, 1500]
]

day_o3 = [
    # 1 - 10
    [0, 10],
    [10.00000000000001, 20],
    [20.00000000000001, 30],
    [30.00000000000001, 40],
    [40.00000000000001, 50],
    [50.00000000000001, 60],
    [60.00000000000001, 70],
    [70.00000000000001, 80],
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    # 11 - 20
    [100.00000000000001, 106],
    [106.00000000000001, 112],
    [112.00000000000001, 118],
    [118.00000000000001, 124],
    [124.00000000000001, 130],
    [130.00000000000001, 136],
    [136.00000000000001, 142],
    [142.00000000000001, 148],
    [148.00000000000001, 154],
    [154.00000000000001, 160],
    # 21 -30
    [160.00000000000001, 165.5],
    [165.50000000000001, 171],
    [171.00000000000001, 176.5],
    [176.50000000000001, 182],
    [182.00000000000001, 187.5],
    [187.50000000000001, 193],
    [193.00000000000001, 198.5],
    [198.50000000000001, 204],
    [204.00000000000001, 209.5],
    [209.50000000000001, 215],
    # 31 - 40
    [215.00000000000001, 220],
    [220.00000000000001, 225],
    [225.00000000000001, 230],
    [230.00000000000001, 235],
    [235.00000000000001, 240],
    [240.00000000000001, 245],
    [245.00000000000001, 250],
    [250.00000000000001, 255],
    [255.00000000000001, 260],
    [260.00000000000001, 265],
    # 41 - 50
    [265.00000000000001, 318.5],
    [318.50000000000001, 372],
    [372.00000000000001, 425.5],
    [425.50000000000001, 479],
    [479.00000000000001, 532.5],
    [532.50000000000001, 586],
    [586.00000000000001, 639.5],
    [639.50000000000001, 693],
    [693.00000000000001, 746.5],
    [746.50000000000001, 800],
    # 51
    [800.00000000000001, 2000]
]

day_co = [
    # 1 - 10
    [0, 0.2],
    [0.20000000000001, 0.4],
    [0.40000000000001, 0.6],
    [0.60000000000001, 0.8],
    [0.80000000000001, 1.0],
    [1.00000000000001, 1.2],
    [1.20000000000001, 1.4],
    [1.40000000000001, 1.6],
    [1.60000000000001, 1.8],
    [1.80000000000001, 2.0],
    # 11 - 20
    [2.00000000000001, 2.2],
    [2.20000000000001, 2.4],
    [2.40000000000001, 2.6],
    [2.60000000000001, 2.8],
    [2.80000000000001, 3.0],
    [3.00000000000001, 3.2],
    [3.20000000000001, 3.4],
    [3.40000000000001, 3.6],
    [3.60000000000001, 3.8],
    [3.80000000000001, 4.0],
    # 21 - 30
    [4.00000000000001, 5],
    [5.00000000000001, 6],
    [6.00000000000001, 7],
    [7.00000000000001, 8],
    [8.00000000000001, 9],
    [9.00000000000001, 10],
    [10.00000000000001, 11],
    [11.00000000000001, 12],
    [12.00000000000001, 13],
    [13.00000000000001, 14],
    # 31 - 40
    [14.00000000000001, 15],
    [15.00000000000001, 16],
    [16.00000000000001, 17],
    [17.00000000000001, 18],
    [18.00000000000001, 19],
    [19.00000000000001, 20],
    [20.00000000000001, 21],
    [21.00000000000001, 22],
    [22.00000000000001, 23],
    [23.00000000000001, 24],
    # 41 - 50
    [24.00000000000001, 25.2],
    [25.20000000000001, 26.4],
    [26.40000000000001, 27.6],
    [27.60000000000001, 28.8],
    [28.80000000000001, 30],
    [30.00000000000001, 31.2],
    [31.20000000000001, 32.4],
    [32.40000000000001, 33.6],
    [33.60000000000001, 34.8],
    [34.80000000000001, 36],
    # 51 - 60
    [36.00000000000001, 38.4],
    [38.40000000000001, 40.8],
    [40.80000000000001, 43.2],
    [43.20000000000001, 45.6],
    [45.60000000000001, 48],
    [48.00000000000001, 50.4],
    [50.40000000000001, 52.8],
    [52.80000000000001, 55.2],
    [55.20000000000001, 57.6],
    # [57.60000000000001, 60]
    [57.60000000000001, 100]
]

day_so2 = [
    # 1 - 10
    [0, 5],
    [5.00000000000001, 10],
    [10.00000000000001, 15],
    [15.00000000000001, 20],
    [20.00000000000001, 25],
    [25.00000000000001, 30],
    [30.00000000000001, 35],
    [35.00000000000001, 40],
    [40.00000000000001, 45],
    [45.00000000000001, 50],
    # 11 - 20
    [50.00000000000001, 60],
    [60.00000000000001, 70],
    [70.00000000000001, 80],
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    [100.00000000000001, 110],
    [110.00000000000001, 120],
    [120.00000000000001, 130],
    [130.00000000000001, 140],
    [140.00000000000001, 150],
    # 21 - 30
    [150.00000000000001, 182.5],
    [182.50000000000001, 215],
    [215.00000000000001, 247.5],
    [247.50000000000001, 280],
    [280.00000000000001, 312.5],
    [312.50000000000001, 345],
    [345.00000000000001, 377.5],
    [377.50000000000001, 410],
    [410.00000000000001, 442.5],
    [442.50000000000001, 475],
    # 31 - 40
    [475.00000000000001, 507.5],
    [507.50000000000001, 540],
    [540.00000000000001, 572.5],
    [572.50000000000001, 605],
    [605.0000000000001, 637.5],
    [637.50000000000001, 670],
    [670.00000000000001, 702.5],
    [702.50000000000001, 735],
    [735.00000000000001, 767.5],
    [767.50000000000001, 800],
    # 41 - 50
    [800.00000000000001, 880],
    [880.00000000000001, 960],
    [960.00000000000001, 1040],
    [1040.00000000000001, 1120],
    [1120.00000000000001, 1200],
    [1200.00000000000001, 1280],
    [1280.00000000000001, 1360],
    [1360.00000000000001, 1440],
    [1440.00000000000001, 1520],
    [1520.00000000000001, 1600],
    # 51 - 60
    [1600.00000000000001, 1702],
    [1702.00000000000001, 1804],
    [1804.00000000000001, 1906],
    [1906.00000000000001, 2008],
    [2008.00000000000001, 2110],
    [2110.00000000000001, 2212],
    [2212.00000000000001, 2314],
    [2314.00000000000001, 2416],
    [2416.00000000000001, 2518],
    # [2518.00000000000001, 2620]
    [2518.00000000000001, 3000]
]