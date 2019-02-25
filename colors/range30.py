#-*-coding=utf-8-*-
'''
Created on 2018-11-27

@author: chao_qin
@description: 30色阶方案
'''
colors = [
    # 1 - 5
    '#36D281',
    '#4DD070',
    '#64CD5D',
    '#7BCB4D',
    '#9BCF3A',
    # 6 - 10
    '#C3D325',
    '#E2D613',
    '#FFD802',
    '#FFD301',
    '#FFCF01',
    # 11 - 15
    '#FFC900',
    '#FFB700',
    '#FF9A00',
    '#FF7901',
    '#FF5C01',
    # 16 - 20
    '#F94208',
    '#F1270F',
    '#EA0D15',
    '#DF0020',
    '#CC0030',
    # 21 - 25
    '#BA013F',
    '#A6014E',
    '#93015D',
    '#8E0257',
    '#890351',
    # 26 - 30
    '#84044B',
    '#800545',
    '#76073A',
    '#69092A',
    '#5D0B1B'
]

aqi = [
    # 1 - 5
    [0, 10],
    [10.00000000000001, 20],
    [20.00000000000001, 30],
    [30.00000000000001, 40],
    [40.00000000000001, 50],
    # 6 - 10
    [50.00000000000001, 60],
    [60.00000000000001, 70],
    [70.00000000000001, 80],
    [80.00000000000001, 90],
    [90.00000000000001, 100],
    # 11 -15
    [100.00000000000001, 110],
    [110.00000000000001, 120],
    [120.00000000000001, 130],
    [130.00000000000001, 140],
    [140.00000000000001, 150],
    # 16 - 20
    [150.00000000000001, 160],
    [160.00000000000001, 170],
    [170.00000000000001, 180],
    [180.00000000000001, 190],
    [190.00000000000001, 200],
    # 21 - 25
    [200.00000000000001, 220],
    [220.00000000000001, 240],
    [240.00000000000001, 260],
    [260.00000000000001, 280],
    [280.00000000000001, 300],
    # 26 - 30
    [300.00000000000001, 340],
    [340.00000000000001, 380],
    [380.00000000000001, 420],
    [420.00000000000001, 460],
    [460.00000000000001, 500]
]

pm10 = [
    # 1 - 5
    [0, 10],
    [10.00000000000001, 20],
    [20.00000000000001, 30],
    [30.00000000000001, 40],
    [40.00000000000001, 50],
    # 6 - 10
    [50.00000000000001, 70],
    [70.00000000000001, 90],
    [90.00000000000001, 110],
    [110.00000000000001, 130],
    [130.00000000000001, 150],
    # 11 -15
    [150.00000000000001, 170],
    [170.00000000000001, 190],
    [190.00000000000001, 210],
    [210.00000000000001, 230],
    [230.00000000000001, 250],
    # 16 - 20
    [250.00000000000001, 270],
    [270.00000000000001, 290],
    [290.00000000000001, 310],
    [310.00000000000001, 330],
    [330.00000000000001, 350],
    # 21 - 25
    [350.00000000000001, 364],
    [364.00000000000001, 378],
    [378.00000000000001, 392],
    [392.00000000000001, 406],
    [406.00000000000001, 420],
    # 26 - 30
    [420.00000000000001, 456],
    [456.00000000000001, 492],
    [492.00000000000001, 528],
    [528.00000000000001, 564],
    # [564.00000000000001, 600]
    [564.00000000000001, 1000]
]

pm25 = [
    # 1 - 5
    [0, 7],
    [7.00000000000001, 14],
    [14.00000000000001, 21],
    [21.00000000000001, 28],
    [28.00000000000001, 35],
    # 6 - 10
    [35.00000000000001, 43],
    [43.00000000000001, 51],
    [51.00000000000001, 59],
    [59.00000000000001, 67],
    [67.00000000000001, 75],
    # 11 -15
    [75.00000000000001, 83],
    [83.00000000000001, 91],
    [91.00000000000001, 99],
    [99.00000000000001, 107],
    [107.00000000000001, 115],
    # 16 - 20
    [115.00000000000001, 122],
    [122.00000000000001, 129],
    [129.00000000000001, 136],
    [136.00000000000001, 143],
    [143.00000000000001, 150],
    # 21 - 25
    [150.00000000000001, 170],
    [170.00000000000001, 190],
    [190.00000000000001, 210],
    [210.00000000000001, 230],
    [230.00000000000001, 250],
    # 26 - 30
    [250.00000000000001, 300],
    [300.00000000000001, 350],
    [350.00000000000001, 400],
    [400.00000000000001, 450],
    # [450.00000000000001, 500]
    [450.00000000000001, 1000]
]

hour_no2 = [
    # 1 - 5
    [0, 20],
    [20.00000000000001, 40],
    [40.00000000000001, 60],
    [60.00000000000001, 80],
    [80.00000000000001, 100],
    # 6 - 10
    [100.00000000000001, 120],
    [120.00000000000001, 140],
    [140.00000000000001, 160],
    [160.00000000000001, 180],
    [180.00000000000001, 200],
    # 11 -15
    [200.00000000000001, 300],
    [300.00000000000001, 400],
    [400.00000000000001, 500],
    [500.00000000000001, 600],
    [600.00000000000001, 700],
    # 16 - 20
    [700.00000000000001, 800],
    [800.00000000000001, 900],
    [900.00000000000001, 1000],
    [1000.00000000000001, 1100],
    [1100.00000000000001, 1200],
    # 21 - 25
    [1200.00000000000001, 1428],
    [1428.00000000000001, 1656],
    [1656.00000000000001, 1884],
    [1884.00000000000001, 2112],
    [2112.00000000000001, 2340],
    # 26 - 30
    [2340.00000000000001, 2640],
    [2640.00000000000001, 2940],
    [2940.00000000000001, 3240],
    [3240.00000000000001, 3540],
    # [3540.00000000000001, 3840]
    [3540.00000000000001, 5000]
]

hour_o3 = [
    # 1 - 5
    [0, 32],
    [32.00000000000001, 64],
    [64.00000000000001, 96],
    [96.00000000000001, 128],
    [128.00000000000001, 160],
    # 6 - 10
    [160.00000000000001, 168],
    [168.00000000000001, 176],
    [176.00000000000001, 184],
    [184.00000000000001, 192],
    [192.00000000000001, 200],
    # 11 -15
    [200.00000000000001, 220],
    [220.00000000000001, 240],
    [240.00000000000001, 260],
    [260.00000000000001, 280],
    [280.00000000000001, 300],
    # 16 - 20
    [300.00000000000001, 320],
    [320.00000000000001, 340],
    [340.00000000000001, 360],
    [360.00000000000001, 380],
    [380.00000000000001, 400],
    # 21 - 25
    [400.00000000000001, 480],
    [480.00000000000001, 560],
    [560.00000000000001, 640],
    [640.00000000000001, 720],
    [720.00000000000001, 800],
    # 26 - 30
    [800.00000000000001, 880],
    [880.00000000000001, 960],
    [960.00000000000001, 1040],
    [1040.00000000000001, 1120],
    # [1120.00000000000001, 1200]
    [1120.00000000000001, 2000]
]

hour_co = [
    # 1 - 5
    [0, 1],
    [1.00000000000001, 2],
    [2.00000000000001, 3],
    [3.00000000000001, 4],
    [4.00000000000001, 5],
    # 6 - 10
    [5.00000000000001, 6],
    [6.00000000000001, 7],
    [7.00000000000001, 8],
    [8.00000000000001, 9],
    [9.00000000000001, 10],
    # 11 -15
    [10.00000000000001, 15],
    [15.00000000000001, 20],
    [20.00000000000001, 25],
    [25.00000000000001, 30],
    [30.00000000000001, 35],
    # 16 - 20
    [35.00000000000001, 40],
    [40.00000000000001, 45],
    [45.00000000000001, 50],
    [50.00000000000001, 55],
    [55.00000000000001, 60],
    # 21 - 25
    [60.00000000000001, 66],
    [66.00000000000001, 72],
    [72.00000000000001, 78],
    [78.00000000000001, 84],
    [84.00000000000001, 90],
    # 26 - 30
    [90.00000000000001, 102],
    [102.00000000000001, 114],
    [114.00000000000001, 126],
    [126.00000000000001, 138],
    # [138.00000000000001, 150]
    [138.00000000000001, 500]
]

hour_so2 = [
    # 1 - 5
    [0, 30],
    [30.00000000000001, 60],
    [60.00000000000001, 90],
    [90.00000000000001, 120],
    [120.00000000000001, 150],
    # 6 - 10
    [150.00000000000001, 220],
    [220.00000000000001, 290],
    [290.00000000000001, 360],
    [360.00000000000001, 430],
    [430.00000000000001, 500],
    # 11 -15
    [500.00000000000001, 530],
    [530.00000000000001, 560],
    [560.00000000000001, 590],
    [590.00000000000001, 620],
    [620.00000000000001, 650],
    # 16 - 20
    [650.00000000000001, 680],
    [680.00000000000001, 710],
    [710.00000000000001, 740],
    [740.00000000000001, 770],
    [770.00000000000001, 800],
    # 21
    [800.00000000000001, 2000]
]

day_no2 = [
    # 1 - 5
    [0, 8],
    [8.00000000000001, 16],
    [16.00000000000001, 24],
    [24.00000000000001, 32],
    [32.00000000000001, 40],
    # 6 - 10
    [40.00000000000001, 48],
    [48.00000000000001, 56],
    [56.00000000000001, 64],
    [64.00000000000001, 72],
    [72.00000000000001, 80],
    # 11 -15
    [80.00000000000001, 100],
    [100.00000000000001, 120],
    [120.00000000000001, 140],
    [140.00000000000001, 160],
    [160.00000000000001, 180],
    # 16 - 20
    [180.00000000000001, 200],
    [200.00000000000001, 220],
    [220.00000000000001, 240],
    [240.00000000000001, 260],
    [260.00000000000001, 280],
    # 21 - 25
    [280.00000000000001, 337],
    [337.00000000000001, 394],
    [394.00000000000001, 451],
    [451.00000000000001, 508],
    [508.00000000000001, 565],
    # 26 - 30
    [565.00000000000001, 640],
    [640.00000000000001, 715],
    [715.00000000000001, 790],
    [790.00000000000001, 865],
    # [865.00000000000001, 940]
    [865.00000000000001, 1500]
]

day_o3 = [
    # 1 - 5
    [0, 20],
    [20.00000000000001, 40],
    [40.00000000000001, 60],
    [60.00000000000001, 80],
    [80.00000000000001, 100],
    # 6 - 10
    [100.00000000000001, 112],
    [112.00000000000001, 124],
    [124.00000000000001, 136],
    [136.00000000000001, 148],
    [148.00000000000001, 160],
    # 11 -15
    [160.00000000000001, 171],
    [171.00000000000001, 182],
    [182.00000000000001, 193],
    [193.00000000000001, 204],
    [204.00000000000001, 215],
    # 16 - 20
    [215.00000000000001, 225],
    [225.00000000000001, 235],
    [235.00000000000001, 245],
    [245.00000000000001, 255],
    [255.00000000000001, 265],
    # 21 - 25
    [265.00000000000001, 372],
    [372.00000000000001, 479],
    [479.00000000000001, 586],
    [586.00000000000001, 693],
    [693.00000000000001, 800],
    # 26
    [800.00000000000001, 2000]
]

day_co = [
    # 1 - 5
    [0, 0.4],
    [0.40000000000001, 0.8],
    [0.80000000000001, 1.2],
    [1.20000000000001, 1.6],
    [1.60000000000001, 2.0],
    # 6 - 10
    [2.00000000000001, 2.4],
    [2.40000000000001, 2.8],
    [2.80000000000001, 3.2],
    [3.20000000000001, 3.6],
    [3.60000000000001, 4.0],
    # 11 -15
    [4.00000000000001, 6],
    [6.00000000000001, 8],
    [8.00000000000001, 10],
    [10.00000000000001, 12],
    [12.00000000000001, 14],
    # 16 - 20
    [14.00000000000001, 16],
    [16.00000000000001, 18],
    [18.00000000000001, 20],
    [20.00000000000001, 22],
    [22.00000000000001, 24],
    # 21 - 25
    [24.00000000000001, 26.4],
    [26.40000000000001, 28.8],
    [28.80000000000001, 31.2],
    [31.20000000000001, 33.6],
    [33.60000000000001, 36],
    # 26 - 30
    [36.00000000000001, 40.8],
    [40.80000000000001, 45.6],
    [45.60000000000001, 50.4],
    [50.40000000000001, 55.2],
    # [55.20000000000001, 60]
    [55.20000000000001, 100]
]

day_so2 = [
    # 1 - 5
    [0, 10],
    [10.00000000000001, 20],
    [20.00000000000001, 30],
    [30.00000000000001, 40],
    [40.00000000000001, 50],
    # 6 - 10
    [50.00000000000001, 70],
    [70.00000000000001, 90],
    [90.00000000000001, 110],
    [110.00000000000001, 130],
    [130.00000000000001, 150],
    # 11 -15
    [150.00000000000001, 215],
    [215.00000000000001, 280],
    [280.00000000000001, 345],
    [345.00000000000001, 410],
    [410.00000000000001, 475],
    # 16 - 20
    [475.00000000000001, 540],
    [540.00000000000001, 605],
    [605.00000000000001, 670],
    [670.00000000000001, 735],
    [735.00000000000001, 800],
    # 21 - 25
    [800.00000000000001, 960],
    [960.00000000000001, 1120],
    [1120.00000000000001, 1280],
    [1280.00000000000001, 1440],
    [1440.00000000000001, 1600],
    # 26 - 30
    [1600.00000000000001, 1804],
    [1804.00000000000001, 2008],
    [2008.00000000000001, 2212],
    [2212.00000000000001, 2416],
    # [2416.00000000000001, 2620]
    [2416.00000000000001, 3000]
]