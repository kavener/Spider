import requests
import re
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

pattern = re.compile(
    'class="board-index.*?>(.*?)</i>.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="score"><.*?>(.*?)<.*?class="fraction">(.*?)</i>',
    re.S)
li = '''

<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>TOP100榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>
  cid = "c_wx6zb55";
  ci = 59;
val = {"subnavId":4};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';

  </script>
  <link rel="stylesheet" href="//ms0.meituan.net/mywww/common.4b838ec3.css"/>
<link rel="stylesheet" href="//ms0.meituan.net/mywww/board-index.92a06072.css"/>
  <script src="//ms0.meituan.net/mywww/stat.74891044.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//ms0.meituan.net/mywww/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face {
      font-family: stonefont;
      src: url('//vfile.meituan.net/colorstone/98d3947ad8da2416208d61cce5be37623168.eot');
      src: url('//vfile.meituan.net/colorstone/98d3947ad8da2416208d61cce5be37623168.eot?#iefix') format('embedded-opentype'),
           url('//vfile.meituan.net/colorstone/e2cb1cd2cea3fa7d4ae7d33146f688582080.woff') format('woff');
    }

    .stonefont {
      font-family: stonefont;
    }
  </style>
</head>
<body>


<div class="header">
  <div class="header-inner">
        <a href="/" class="logo" data-act="icon-click"></a>
        <div class="city-container" data-val="{currentcityid:59 }">
            <div class="city-selected">
                <div class="city-name">
                  成都
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 59 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city">成都</a></div>
                
            </div>
        </div>


        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click"  >首页</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
            </ul>
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="http://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          href="/board/7"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          data-state-val="{subnavId:4}"
          class="active" href="javascript:void(0);"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2018-07-28<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-51">51</i>
    <a href="/films/3294" title="勇敢的心" class="image-link" data-act="boarditem-click" data-val="{movieId:3294}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/f8e9d5a90224746d15dfdbd53d4fae3d209420.jpg@160w_220h_1e_1c" alt="勇敢的心" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/3294" title="勇敢的心" data-act="boarditem-click" data-val="{movieId:3294}">勇敢的心</a></p>
        <p class="star">
                主演：梅尔·吉布森,苏菲·玛索,帕特里克·麦高汉
        </p>
<p class="releasetime">上映时间：1995-05-24(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-52">52</i>
    <a href="/films/9053" title="黑客帝国3：矩阵革命" class="image-link" data-act="boarditem-click" data-val="{movieId:9053}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/5ca6ffcbb994a51cd6215e7c4fff2d9b71039.jpg@160w_220h_1e_1c" alt="黑客帝国3：矩阵革命" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/9053" title="黑客帝国3：矩阵革命" data-act="boarditem-click" data-val="{movieId:9053}">黑客帝国3：矩阵革命</a></p>
        <p class="star">
                主演：基努·里维斯,雨果·维文,凯瑞-安·莫斯
        </p>
<p class="releasetime">上映时间：2003-11-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-53">53</i>
    <a href="/films/43" title="三傻大闹宝莱坞" class="image-link" data-act="boarditem-click" data-val="{movieId:43}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/4bb144bc0a674ba6908349018fd092e6330929.jpg@160w_220h_1e_1c" alt="三傻大闹宝莱坞" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/43" title="三傻大闹宝莱坞" data-act="boarditem-click" data-val="{movieId:43}">三傻大闹宝莱坞</a></p>
        <p class="star">
                主演：阿米尔·汗,黄渤,卡琳娜·卡普尔
        </p>
<p class="releasetime">上映时间：2011-12-08</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-54">54</i>
    <a href="/films/14652" title="断背山" class="image-link" data-act="boarditem-click" data-val="{movieId:14652}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/e71affe126eeb4f8bfcc738cbddeebc8288766.jpg@160w_220h_1e_1c" alt="断背山" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/14652" title="断背山" data-act="boarditem-click" data-val="{movieId:14652}">断背山</a></p>
        <p class="star">
                主演：希斯·莱杰,杰克·吉伦哈尔,米歇尔·威廉姆斯
        </p>
<p class="releasetime">上映时间：2006-01-13(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-55">55</i>
    <a href="/films/6289" title="闻香识女人" class="image-link" data-act="boarditem-click" data-val="{movieId:6289}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/7cb7965469cb7ff95613714389f1ea3d87743.jpg@160w_220h_1e_1c" alt="闻香识女人" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/6289" title="闻香识女人" data-act="boarditem-click" data-val="{movieId:6289}">闻香识女人</a></p>
        <p class="star">
                主演：阿尔·帕西诺,克里斯·奥唐纳,加布里埃尔·安瓦尔
        </p>
<p class="releasetime">上映时间：1992-12-23(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-56">56</i>
    <a href="/films/614" title="飞屋环游记" class="image-link" data-act="boarditem-click" data-val="{movieId:614}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/47dd790e19dad72b50580641de5608c5199014.jpg@160w_220h_1e_1c" alt="飞屋环游记" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/614" title="飞屋环游记" data-act="boarditem-click" data-val="{movieId:614}">飞屋环游记</a></p>
        <p class="star">
                主演：爱德华·阿斯纳,乔丹·长井,鲍勃·彼德森
        </p>
<p class="releasetime">上映时间：2009-08-04</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-57">57</i>
    <a href="/films/1262" title="鬼子来了" class="image-link" data-act="boarditem-click" data-val="{movieId:1262}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/0b507aa44c4dfbbcc91949b69b1b39a168922.jpg@160w_220h_1e_1c" alt="鬼子来了" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1262" title="鬼子来了" data-act="boarditem-click" data-val="{movieId:1262}">鬼子来了</a></p>
        <p class="star">
                主演：姜文,姜宏波,陈强
        </p>
<p class="releasetime">上映时间：2000-05-12(法国戛纳)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-58">58</i>
    <a href="/films/1322" title="飞越疯人院" class="image-link" data-act="boarditem-click" data-val="{movieId:1322}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/4dddd98730274c3b1464ff0a0ad195e5233381.jpg@160w_220h_1e_1c" alt="飞越疯人院" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1322" title="飞越疯人院" data-act="boarditem-click" data-val="{movieId:1322}">飞越疯人院</a></p>
        <p class="star">
                主演：杰克·尼科尔森,路易丝·弗莱彻,威尔·萨姆森
        </p>
<p class="releasetime">上映时间：1975-11-19(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-59">59</i>
    <a href="/films/1332" title="美国往事" class="image-link" data-act="boarditem-click" data-val="{movieId:1332}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/92198a6fc8c3f5d13aa1bdf203572c0f99438.jpg@160w_220h_1e_1c" alt="美国往事" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1332" title="美国往事" data-act="boarditem-click" data-val="{movieId:1332}">美国往事</a></p>
        <p class="star">
                主演：罗伯特·德尼罗,詹姆斯·伍兹,伊丽莎白·麦戈文
        </p>
<p class="releasetime">上映时间：1984-02-17(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-60">60</i>
    <a href="/films/995" title="少年派的奇幻漂流" class="image-link" data-act="boarditem-click" data-val="{movieId:995}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/34998e31c6d07475f1add6b8b16fd21d192579.jpg@160w_220h_1e_1c" alt="少年派的奇幻漂流" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/995" title="少年派的奇幻漂流" data-act="boarditem-click" data-val="{movieId:995}">少年派的奇幻漂流</a></p>
        <p class="star">
                主演：苏拉·沙玛,伊尔凡·可汗,塔布
        </p>
<p class="releasetime">上映时间：2012-11-22</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
            <div class="pager-main">
                
  
  <ul class="list-pager">

<li>  <a class="page_5"
      href="?offset=40"
  >上一页</a>
</li>


  
      <li >
    <a class="page_1"
      href="?offset=0"
  >1</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_4"
      href="?offset=30"
  >4</a>

</li>
  <li >
    <a class="page_5"
      href="?offset=40"
  >5</a>

</li>
  <li class="active">
    <a class="page_6"
      href="javascript:void(0);" style="cursor: default"
  >6</a>

</li>
  <li >
    <a class="page_7"
      href="?offset=60"
  >7</a>

</li>
  <li >
    <a class="page_8"
      href="?offset=70"
  >8</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_10"
      href="?offset=90"
  >10</a>

</li>


<li>  <a class="page_7"
      href="?offset=60"
  >下一页</a>
</li>
</ul>


            </div>
    </div>
</div>

    </div>

<div class="footer">
    <p class="friendly-links">
      商务合作邮箱：v@maoyan.com
      客服电话：10105335
      违法和不良信息举报电话：4006018900
      <br/>
      投诉举报邮箱：tousujubao@meituan.com
      舞弊线索举报邮箱：wubijubao@maoyan.com
    </p>
    <p class="friendly-links">
        友情链接 :
        <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
        <span></span>
        <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
    </p>
    <p>
        &copy;2016
        猫眼电影 maoyan.com
        <a href="https://tsm.miit.gov.cn/pages/EnterpriseSearchList_Portal.aspx?type=0&keyword=京ICP证160733号&pageNo=1" target="_blank">京ICP证160733号</a>
        <a href="http://www.miibeian.gov.cn" target="_blank">京ICP备16022489号-1</a>
        <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备 11010102003232号</a>
        <a href="/about/licence" target="_blank">网络文化经营许可证</a>
        <a href="http://www.meituan.com/about/rules" target="_blank">电子公告服务规则</a>
    </p>
    <p>北京猫眼文化传媒有限公司</p>
</div>

    <!--[if IE 8]><script src="//ms0.meituan.net/mywww/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script src="//ms0.meituan.net/mywww/es5-sham.d6ea26f4.js"></script><![endif]-->
    <script src="//ms0.meituan.net/mywww/common.dc33ab40.js"></script>
<script src="//ms0.meituan.net/mywww/board-index.4aa00764.js"></script>
</body>
</html>

'''
items = re.findall(pattern, li)
print(items)


def get_info(url):
    return requests.get(url=url, headers=headers).text


def make_url(offset):
    return 'http://maoyan.com/board/4?offset=' + str(offset)


def get_movie_info(html):
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'ranking': item[0],
            'film_name': item[1],
            'To_star': item[2].strip()[3:],
            'Release_time': item[3],
            'score': item[4] + item[5]
        }


def save_info(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = make_url(offset)
    html = get_info(url)
    for item in get_movie_info(html):
        print(item)
        save_info(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)