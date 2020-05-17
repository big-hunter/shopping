create database shopping;


INSERT INTO `shopping`.`shop_user` (`user_id`, `username`, `password`, `phone`, `sex`, `age`, `status`, `add_time`,`last_login`) VALUES ('1', 'tester', '123456', '10086', '男', '20', '1', '2020-05-15 16:36:46.740147','2020-05-14 16:36:46.740147');


-- 一级分类
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('1', '1', '女装', '1', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('2', '2', '男装', '1', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('3', '3', '儿童服饰', '1', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('4', '4', '男包|女包', '1', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('5', '5', '潮流前线', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');


-- 二级分类 1
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('6', '1', '秋款风衣', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('7','1',  '机车皮衣', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('8','1',  '秋款连衣裙', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('9','1',  '休闲裤', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('10','1', '打底裤', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');

-- 二级分类 2
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('11', '2',  '个性潮男', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('12', '2',  '时尚休闲', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('13', '2',  '商务绅士', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('14', '2',  '休闲衬衫', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('15', '2',  '西服套装', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('16', '2',  '直筒西裤', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
-- 二级分类 3
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('17', '3',  '毛衣|针织衫', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('18', '3',  '儿童男装', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('19', '3',  '儿童女装', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('20', '3',  '表演服饰', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('21', '3',  '亲子装', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('22', '3',  '休闲套装', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
-- 二级分类 4
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('23', '5',  '珠宝首饰', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('24', '5',  '时尚饰品', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('25', '5',  '品质手表', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('26', '5',  '眼镜配饰', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('27', '5',  '男人饰品', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');

-- 二级分类 5
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('28', '4',  '秋新款', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('29', '4',  '单肩包', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('30', '4',  '斜挎包', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('31', '4',  '手提包', '2', '10', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('32', '4',  '大牌包', '2', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');

INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('33', '33', '珠宝首饰', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('34', '34', '时尚饰品', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('35', '35', '品质手表', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('36', '36', '眼镜配饰', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('37', '37', '男人饰品', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
INSERT INTO `shopping`.`shop_goodstype` (`id`, `paren_id`, `typename`, `type_level`, `popular`, `path`, `addtime`, `nowtime`) VALUES ('38', '38', '原创饰品', '1', '20', '1', '2020-05-14 16:36:46.740147', '2020-05-14 16:36:46.740147');
-- 商品添加
--- 首页上5个 最流行的商品
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('1', '1', '流行女包', '特价销售', '200', '/static/shop/images/banner_01.jpg', 'PARDA', '1', '1', 'red', '流行|女包', '100', '100', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('2', '3', '时尚童装', '特价销售', '200', '/static/shop/images/banner_02.jpg', 'PARDA', '1', '1', 'red', '童装|男款|女款', '300', '300', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('3', '1', '女款卫衣', '特价销售', '200', '/static/shop/images/banner_03.jpg', 'PARDA', '1', '1', 'red', '女装|流行卫衣', '200', '2050', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('4', '1', '全家款', '特价销售', '200', '/static/shop/images/banner_04.jpg', 'PARDA', '1', '1', 'red', '全家款|衬衫', '200', '200', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('5', '5', '流行女包', '特价销售', '200', '/static/shop/images/banner_05.jpg', 'PARDA', '1', '1', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
--- 详细页设计灵感
UPDATE `shopping`.`shop_goods` SET `descr` = '<div class=\"b1\"><h4>摇滚女神的热情似火</h4>此款衣服的最大亮点在于三套式穿法 ，外套，马甲，连衣裙 无论是成套还是单穿都十分有个性，加上上面大面积红色的运用，结合军装感的基本，在女子妖娆中，体现出飒爽英姿。</div>' WHERE (`id` = '2');
UPDATE `shopping`.`shop_goods` SET `descr` = '<div class=\"b1\"><h4>摇滚女神的热情似火</h4>此款衣服的最大亮点在于三套式穿法 ，外套，马甲，连衣裙 无论是成套还是单穿都十分有个性，加上上面大面积红色的运用，结合军装感的基本，在女子妖娆中，体现出飒爽英姿。</div>' WHERE (`id` = '3');

-- 第二列的产品
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('6', '1', '红色风衣', '设计灵感描述', '500', '/static/shop/images/pic1.jpg', 'PARDA', '1', '0.8', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('7', '2', '男士夹克', '设计灵感描述', '600', '/static/shop/images/pic2.jpg', 'CHANNEL', '1', '0.8', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('8', '5', '女士卫衣', '设计灵感描述', '700', '/static/shop/images/pic3.jpg', 'HERMES', '1', '0.8', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
INSERT INTO `shopping`.`shop_goods` (`id`, `good_type`, `gname`, `descr`, `price`, `pic_path`, `brand`, `state`, `discount`, `color`, `tag`, `store`, `num`, `addtime`, `popular`) VALUES ('9', '5', '潮流夹克', '设计灵感描述', '800', '/static/shop/images/pic4.jpg', 'VERICe', '1', '0.8', 'red', '流行|女包', '200', '200', '2020-05-14 16:36:46.740147', '100');
