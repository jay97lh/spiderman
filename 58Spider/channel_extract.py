import requests
from lxml import etree

start_url = 'http://hf.58.com/sale.shtml?PGTID=0d100000-0034-5a4a-6836-044f9e57cfac&ClickID=4'
url_host = 'http://hf.58.com'


def get_channel_urls(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[@id="ymenu-side"]')
    for info in infos:
        class_urls = info.xpath('ul/li/ul/li/span/a/@href')
        for class_url in class_urls:
            print(url_host + class_url)


channel_list = '''
    http://hf.58.com/iphonesj/
    http://hf.58.com/sanxing/
    http://hf.58.com/xiaomi/
    http://hf.58.com/huaweisj/
    http://hf.58.com/oppo/
    http://hf.58.com/vivo/
    http://hf.58.com/meizu/
    http://hf.58.com/kupaisj/
    http://hf.58.com/lianxiang/
    http://hf.58.com/zhongxingshouji/
    http://hf.58.com/motuoluola/
    http://hf.58.com/nuojiya/
    http://hf.58.com/ailixin/
    http://hf.58.com/heimei/
    http://hf.58.com/yamaha/
    http://hf.58.com/bentianmoto/
    http://hf.58.com/jialing/
    http://hf.58.com/lingmumoto/
    http://hf.58.com/zongshen/
    http://hf.58.com/qingqi/
    http://hf.58.com/wanliang/
    http://hf.58.com/tabanmotuoche/
    http://hf.58.com/qishiche/
    http://hf.58.com/gonglusai/
    http://hf.58.com/miniche/
    http://hf.58.com/dapailiang/   
    http://hf.58.com/aima/
    http://hf.58.com/xiaoniao/
    http://hf.58.com/qingqiddc/
    http://hf.58.com/lvyuanddc/
    http://hf.58.com/xinri/
    http://hf.58.com/diandongzixingche/
    http://hf.58.com/diandongmotuoche/
http://hf.58.com/zhediediandongche/
http://hf.58.com/zhudongche/
http://hf.58.com/laoniandaibuche/
http://hf.58.com/jieante/
http://hf.58.com/meilida/
http://hf.58.com/yongjiu/
http://hf.58.com/fenghuangzxc/
http://hf.58.com/feige/
http://hf.58.com/jiema/
http://hf.58.com/putongzixingche/
http://hf.58.com/shandizixingche/
http://hf.58.com/gongluzixingche/
http://hf.58.com/zhediezixingche/
http://hf.58.com/minizixingche/
http://hf.58.com/jiaotasanlunche/
http://hf.58.com/diandongsanlunche/
http://hf.58.com/zhulisanlunche/
http://hf.58.com/zixingchepeijian/
http://hf.58.com/diandongchekongpeijian/
http://hf.58.com/diandongchedianchi/
http://hf.58.com/xiuchegongju/
http://hf.58.com/qixingzhuangbei/
http://hf.58.com/taishiji/
http://hf.58.com/fuwuqi/
http://hf.58.com/ibm/
http://hf.58.com/lenovo/
http://hf.58.com/apple/
http://hf.58.com/dell/
http://hf.58.com/asus/
http://hf.58.com/compaq/
http://hf.58.com/sony/
http://hf.58.com/samsung/
http://hf.58.com/pbdnipad/
http://hf.58.com/pbdnsanxing/
http://hf.58.com/pbdnlianxiang/
http://hf.58.com/pbdnaiguozhe/
http://hf.58.com/wangka/
http://hf.58.com/xianshiqi/
http://hf.58.com/cpu/
http://hf.58.com/xianka/
http://hf.58.com/zhuban/
http://hf.58.com/yingpan/
http://hf.58.com/ydyingpan/
http://hf.58.com/zhoubianshebei/pve_5620_398628/
http://hf.58.com/bujianduandianyuan/
http://hf.58.com/shubiao/
http://hf.58.com/shexiangtou/
http://hf.58.com/usb/
http://hf.58.com/smqita/pve_5623_398637/
http://hf.58.com/smqita/pve_5623_398636/
http://hf.58.com/smqita/
http://hf.58.com/danfanxiangji/
http://hf.58.com/kapianxiangji/
http://hf.58.com/weidanxiangji/
http://hf.58.com/jingtou/
http://hf.58.com/xiangjipeijian/
http://hf.58.com/qitaxiangji/
http://hf.58.com/ipod/
http://hf.58.com/mpsantouch/
http://hf.58.com/mpsannano/
http://hf.58.com/mpsan/
http://hf.58.com/mpsi/
http://hf.58.com/psp/
http://hf.58.com/yxjpsv/
http://hf.58.com/yxjnds/
http://hf.58.com/yxjxbox/
http://hf.58.com/yxjpssan/
http://hf.58.com/yxjpser/
http://hf.58.com/yxjwii/
http://hf.58.com/biguakt/
http://hf.58.com/guishikt/
http://hf.58.com/zhongyangkt/
http://hf.58.com/yjcaidian/
http://hf.58.com/gqcaidian/
http://hf.58.com/dlzcaidian/
http://hf.58.com/quanzidongxiyiji/
http://hf.58.com/guntongxiyiji/
http://hf.58.com/shuanggangxiyiji/
http://hf.58.com/minixiyiji/
http://hf.58.com/shuangkaimenbx/
http://hf.58.com/duikaimenbx/
http://hf.58.com/minibx/
http://hf.58.com/yingyinjiadian/
http://hf.58.com/shenghuojiadian/
http://hf.58.com/chuweijiadian/
http://hf.58.com/jiadianpeijian/
http://hf.58.com/lishibg/
http://hf.58.com/wohibg/
http://hf.58.com/zhanshibg/
http://hf.58.com/danrenchuang/
http://hf.58.com/shuanrenchuang/
http://hf.58.com/chuangcengchuang/
http://hf.58.com/zhediechuang/
http://hf.58.com/tongchuang/
http://hf.58.com/chuangdian/
http://hf.58.com/guizi/
http://hf.58.com/zhuolei/
http://hf.58.com/zuoju/
http://hf.58.com/jiajushafa/
http://hf.58.com/chaji/
http://hf.58.com/jujia/
http://hf.58.com/muyingzaojiao/
http://hf.58.com/ertongyongpin/
http://hf.58.com/zhiniaoku/
http://hf.58.com/yongpinlalaku/
http://hf.58.com/yongpinbeidai/
http://hf.58.com/yongpinxuebudai/
http://hf.58.com/yongpinyouxidai/
http://hf.58.com/yongpinjianshenjia/
http://hf.58.com/yongpinshuidai/
http://hf.58.com/naifen/
http://hf.58.com/weiyangfushi/
http://hf.58.com/weiyangyingyangpin/
http://hf.58.com/weiyangnaiping/
http://hf.58.com/weiyangnaizui/
http://hf.58.com/weiyangxinaiqi/
http://hf.58.com/weiyangnuannaiqi/
http://hf.58.com/yingerchuang/
http://hf.58.com/yingerche/
http://hf.58.com/tongchexuebu/
http://hf.58.com/tongcheyaoyi/
http://hf.58.com/tongzuoyi/
http://hf.58.com/tongcanyi/
http://hf.58.com/tongniuche/
http://hf.58.com/tongzixingche/
http://hf.58.com/tongsanlunche/
http://hf.58.com/yongpintaixin/
http://hf.58.com/fangfusefu/
http://hf.58.com/mmfuzhuang/
http://hf.58.com/yongpinshoufu/
http://hf.58.com/yongpinyunfuzhen/
http://hf.58.com/fushipeijian/
http://hf.58.com/fuzhuangshoushi/
http://hf.58.com/fuzhuangshoubiao/
http://hf.58.com/fuzhuangtxue/
http://hf.58.com/fuzhuangchenshan/
http://hf.58.com/fuzhuangwaitao/
http://hf.58.com/fuzhuangkuzi/
http://hf.58.com/qunzifs/
http://hf.58.com/fuzhuangxizhuang/
http://hf.58.com/tongzhuang/
http://hf.58.com/xiuxianxie/
http://hf.58.com/yundongxie/
http://hf.58.com/fanbuxie/
http://hf.58.com/gaogenxie/
http://hf.58.com/xiebanxi/
http://hf.58.com/pixie/
http://hf.58.com/xiangbaodanjian/
http://hf.58.com/xiangbaoshuangjian/
http://hf.58.com/xiangbaoshubao/
http://hf.58.com/xiangbaoqianbao/
http://hf.58.com/xiangbaolagan/
http://hf.58.com/xiangbaodiannao/
http://hf.58.com/meirongyongpin/
http://hf.58.com/hufu/
http://hf.58.com/meirongmeiti/
http://hf.58.com/caizhuang/
http://hf.58.com/baojianshipin/
http://hf.58.com/meifa/
http://hf.58.com/xiangshuimr/
http://hf.58.com/gudongguwan/
http://hf.58.com/mingxingwupin/
http://hf.58.com/shufa/
http://hf.58.com/shanshuihua/
http://hf.58.com/renwuhua/
http://hf.58.com/huaniaohua/
http://hf.58.com/zhuangshihua/
http://hf.58.com/guijinshu/
http://hf.58.com/zhubaoshshi/
http://hf.58.com/fangjinshshi/
http://hf.58.com/zhubaoshipin/pve_5731_398646/
http://hf.58.com/zhubaoshipin/pve_5731_398647/
http://hf.58.com/youpiaoyoupin/
http://hf.58.com/fanggujiaju/
http://hf.58.com/aoyunjinianbi/
http://hf.58.com/sbjinianpin/
http://hf.58.com/cddvd/
http://hf.58.com/yingpandianshiju/
http://hf.58.com/ruanjiants/
http://hf.58.com/jishulei/
http://hf.58.com/gongjushu/
http://hf.58.com/kaoshi/
http://hf.58.com/shenghuolei/
http://hf.58.com/xiaoshuo/
http://hf.58.com/youyongwt/
http://hf.58.com/yujiawt/
http://hf.58.com/diaoyuyongju/
http://hf.58.com/qipai/
http://hf.58.com/yundongfushi/pve_5728_398644/
http://hf.58.com/yundongfushi/pve_5728_398648/
http://hf.58.com/tabuji/
http://hf.58.com/peobuji/
http://hf.58.com/anmoyi/
http://hf.58.com/liubinghuaban/
http://hf.58.com/jianshenche/
http://hf.58.com/xueshwenju/
http://hf.58.com/jiaoxueyj/
http://hf.58.com/taiqiuzhuo/
http://hf.58.com/wangqiuyongpin/
http://hf.58.com/zuqiuwt/
http://hf.58.com/pingpangqiuwt/
http://hf.58.com/yumaoqiuwt/
http://hf.58.com/lanqiutw/
http://hf.58.com/jita/
http://hf.58.com/gangqin/
http://hf.58.com/dianziqin/
http://hf.58.com/shoufengqing/
http://hf.58.com/erhuwt/
http://hf.58.com/saomiaoyi/
http://hf.58.com/yitiji/
http://hf.58.com/chuanzhenji/
http://hf.58.com/touyingji/
http://hf.58.com/fuyinji/
http://hf.58.com/dayinji/
http://hf.58.com/tanfen/
http://hf.58.com/mohemoshui/
http://hf.58.com/wenjiangui/
http://hf.58.com/huiyizhuo/
http://hf.58.com/baoxiangui/
http://hf.58.com/bangongzhuoyi/
http://hf.58.com/bangongyi/
http://hf.58.com/bangongjiaju/pve_5733_398638/
http://hf.58.com/bangongjiaju/pve_5733_398639/
http://hf.58.com/huagong/
http://hf.58.com/fangzhi/
http://hf.58.com/fyinshua/
http://hf.58.com/gongcheng/
http://hf.58.com/zaozhi/
http://hf.58.com/kuangye/
http://hf.58.com/mugongshebei/
http://hf.58.com/diandongji/
http://hf.58.com/nongye/
http://hf.58.com/yintundaomo/
http://hf.58.com/xingwanou/
http://hf.58.com/jiandanbianxie/
http://hf.58.com/nanyongchuandai/
http://hf.58.com/fangzhenrufang/
http://hf.58.com/zhendongbang/
http://hf.58.com/yindiciji/
http://hf.58.com/gdianhouting/
http://hf.58.com/tiaodan/
http://hf.58.com/fengrutiaodou/
http://hf.58.com/jiqingyongju/
http://hf.58.com/qingqutiaosao/
http://hf.58.com/lingleiwanju/
http://hf.58.com/yanshitaohuan/
http://hf.58.com/tiaoqingxiangshui/
http://hf.58.com/zhifuyouhuo/
http://hf.58.com/dingziku/
http://hf.58.com/siwameitui/
http://hf.58.com/nanshineiyi/
http://hf.58.com/runhuaji/
http://hf.58.com/aqyp/
http://hf.58.com/anquantao/
http://hf.58.com/qitachengren/
http://hf.58.com/xiaoyuan/pve_5536_1/
http://hf.58.com/xiaoyuan/pve_5536_2/
http://hf.58.com/xiaoyuan/pve_5536_3/
http://hf.58.com/xiaoyuan/pve_5536_4/
http://hf.58.com/xiaoyuan/pve_5536_5/
http://hf.58.com/esqgjiaju/
http://hf.58.com/esqgfuzhuang/
http://hf.58.com/esqgtushu/
http://hf.58.com/ershouqiugou/
http://hf.58.com/wangyou/
http://hf.58.com/huanwu/
http://hf.58.com/lipin/
http://hf.58.com/wuyuanwupin/
http://hf.58.com/fuwujy/
http://hf.58.com/canjirenyongpin/
http://hf.58.com/weixing/
http://hf.58.com/qitatiaozao/
'''
