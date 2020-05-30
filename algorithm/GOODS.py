import pandas as pd
import random
import datetime
import os

class Good():
    good_type= ""
    gname=""
    descr="" # 或者 设计灵感
    price=""
    pic_path=""
    brand=""
    state=""
    discount=""# 打折 1  0.8 0.7 or 0.6
    color= "" # 颜色
    popular="" # 0 - 100 的流行程度
    addtime=""


if __name__ == '__main__':
    data_set_path = "/static/shop/images/dataset/"  # data_Set 文件路径
    # static\shop\images\dataset
    df = pd.read_table("list_box_inshop.txt", delim_whitespace=True)
    print(df["image_name"])

    read_result = []
    # 数据集里不同的衣服对应不同 商品id , 也可以自己加一些
    type_dict = {
                 "Blouses_Shirts": 12,
                 "Dresses": 8,
                 "Sweatshirts_Hoodies": 11,
                 "Skirts": 5,
                 "Tees_Tanks": 13,
                 "Cardigans": 15,
                 "Jackets_Coats": 7,
                 "Sweaters": 17,
                 "Graphic_Tees": 20,
                  "Shorts": 7,
                  "Pants": 9,
                  "Jackets_Vests": 14
                 }
    brand = ["CHANEL", "VERICE", "PARADA", "GUCCI", "HERMES", "Armani", "Versace"]  # 与 页面顺序一致
    start_id = int(11)  # 根据数据库里的值来做 写主键id 开始位置
    for i in range(0, len(df["image_name"])):
        path = df["image_name"][i]
        path_s = path.split("/")
        if path_s[4].split("_")[2] == "full.jpg".lower():
            good = Good()
            good.gname = path_s[2] + path_s[3].split('_')[1]
            good.type = type_dict[path_s[2]]
            good.path = data_set_path + path.replace("\\", '/') # 数据库里存的是 文件绝对地址
            good.price = random.randrange(100, 5000)
            good.brand = random.randint(0, 7)
            # 根据需要替换一下吧
            good.descr = "<div class=\'b1\'><h4>摇滚女神的热情似火</h4>此款衣服的最大亮点在于三套式穿法 ，外套，马甲，连衣裙 " \
                                      "无论是成套还是单穿都十分有个性，加上上面大面积红色的运用，结合军装感的基本，在女子妖娆中，体现出飒爽英姿。</div>"
            good.status = "1"
            good.discount = round(random.random(), 1)
            good.popular = random.randrange(10, 100)
            good.addtime = '2020-05-25 22:36:46.740147'
            sql = "INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES" \
                                                      "('{id}',  '{good_type}', '{gname}', '{descr}', '{price}', '{pic_path}', '{brand}', '{status}', '{discount}', 'red', '', '200', '200', '{addtime}', '{popular}');"
            ''' 
            INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) 
                                          VALUES ('9',  '5', '潮流夹克', '设计灵感描述', '800', '/static/shop/images/pic4.jpg', 'VERICe', '1', '0.8', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
            '''
            final = sql.format(id=str(start_id), good_type=good.type, gname=good.gname, descr=good.descr, price=good.price,
                               pic_path=good.path,  brand=good.brand, status=good.status,
                               discount=good.discount, addtime=good.addtime, popular=good.popular)
            print(final)
            read_result.append(final)
            start_id = start_id+1
   # 可以在控制台粘贴一下 就不用写到文件里了
   #file_name = "inster.sql"
   #with open(file_name, 'a',encoding='utf8') as file:
   #    for line in read_result:
   #        file.write(line+"\n")

   #file.close()