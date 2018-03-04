#!/usr/bin/python
# -*- coding: UTF-8 -*-

def change_to_list(filename):
    content = open(filename,"r").read().strip()
    return list(content.split("\n"))


def traceroute_to_dict(filename):

	txtfile = open(filename,"r")
	content = txtfile.read().strip().split("\n")[1:]
	d=dict()

	for i in range(len(content)):
		
		line = content[i]
		if line[1].isdigit():
			if line[4] != "*" :
				latency=line.strip().split("  ")[2]
				asn = line.strip().split("  ")[3]
				route = line.strip().split("  ")[4]
				ip = line.strip().split("  ")[1]
				step = line[0:2]
			else:
				latency="*"
				asn = "*"
				route = "*"
				ip = "*"
				step = line[0:2]
				
			d[int(step)]=dict()
			d[int(step)]["ip"]=ip
			if int(step) < 3:
				d[int(step)]["ip"]="*.*.*.*(已隱藏)"
			d[int(step)]["latency"]=latency
			d[int(step)]["asn"]=asn
			d[int(step)]["route"]=route


	return dict(d)

def traceroute_to_table(filename):
  d = traceroute_to_dict(filename)
  string = ""
  for i in sorted(d.keys()):
    x = d[i]
    template = """
  <tr>
  <td>{}</td>
  <td>{}</td>
  <td>{}</td>
  <td>{}</td>
  <td>{}</td>
  </tr>
  """
    string = string + template.format(i,x["ip"],x["route"],x["asn"],x["latency"]) + "\n"
    
    writefile = open(filename + "_table","w")
    writefile.write(string)
    writefile.close()


def dict_to_table(d,tab):

    table_class = "ui bottom attached tab segment"
    if tab == "first":
        table_class = table_class + " active"
    
    table_html = """
    
    <div class="{0}" data-tab="{1}">
<table class="ui very compact striped table">
  <thead>
    <tr><th>跳數</th>
    <th>IP</th>
    <th>路由</th>
    <th>AS Number</th>
    <th>延遲</th>
  </tr></thead>
  <tbody>
    """.format(table_class,tab)

    for step in sorted(d.keys()):
        table_html = table_html + """
        
        <tr>
      <td>{0}</td>
      <td>{1}</td>
      <td>{2}</td>
      <td>{3}</td>
      <td>{4}</td>
    </tr>
        
        """.format(step,d[step]["ip"],d[step]["route"],d[step]["asn"],d[step]["latency"])

    table_html = table_html + """
      </tbody>
</table>
</div>
    """
    return table_html

html = """

<html>
<head>
    <meta charset="UTF-8" id="home">
    <meta name="keywords" content="Zbench,Function Club,Bench Mark,VPS,主機部落格,測評,測試腳本">
    <title>Zbench v1.0 HTML Output</title>
<link rel="stylesheet" type="text/css" href="https://cdn.bootcss.com/semantic-ui/2.2.13/semantic.min.css">
<script src="https://cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/semantic-ui/2.2.13/semantic.min.js"></script>
</head>
<body>

<div class="ui attached stackable menu">
  <div class="ui container">
    <a class="item" onclick="javascript:scroller('home', 100);">
      <i class="home icon"></i> 首頁
    </a>
    <a class="item" onclick="javascript:scroller('system', 300);">
      <i class="grid layout icon"></i> 系統訊息
    </a>
    <a class="item" onclick="javascript:scroller('hdd', 600);">
      <i class="desktop icon"></i> 硬碟 I/O
    </a>
	<a class="item" onclick="javascript:scroller('net', 900);">
      <i class="sitemap icon"></i> 網路測試
    </a>
	<a class="item" onclick="javascript:scroller('route', 1600);">
      <i class="plug icon"></i> 路由追蹤
    </a>
    <div class="ui simple dropdown item">
      更多
      <i class="dropdown icon"></i>
      <div class="menu">
        <a class="item" href="https://www.github.com/FunctionClub"><i class="edit icon"></i> 關於我們</a>
        <a class="item" href="https://github.com/FunctionClub/ZBench/"><i class="github icon"></i>Github </a>
      </div>
    </div>
    <div class="right item">
      <div class="ui">    
			<a href="https://github.com/FunctionClub/ZBench/">ZBench v1.0-Beta</a>
	  </div>
    </div>
  </div>
</div>

<div class="ui hidden divider"></div>
<div class="ui container">
<div class="ui message red">
<i class="close icon"></i>
  <div class="header">
    您正在使用的是開發中的項目。
  </div>
  <p>此程序正處於開發版, 我們無法保證在運行過程中不會出錯. 我們將在近期測試後放出正式版，敬請期待.</p>
</div>
</div>
<div class="ui hidden divider"></div>
<div class="ui container">
<div class="ui message">
  <div class="header">
    測試數據準確性說明
  </div>
  <p>請注意，所有的測試數據為測試時的即時數據. 我們不保證您的服務商會在日後一直使用保持完全相同的服務。數據僅供參考.</p>
</p>
</div>
</div>
<div class="ui hidden divider" id="system"></div>

<h2 class="ui center aligned icon header">
  <i class="circular Laptop icon"></i>
  系統訊息
</h2>
<div class="ui hidden divider"></div>
<div class="ui container">
<table class="ui celled striped table">
  <thead>
    <tr> 
      <th>項目</th>
      <th>數據</th>
  </tr></thead>
  <tbody>
    <tr>
      <td class="collapsing">
        <i class="Microchip icon"></i> CPU 型號
      </td>
      <td>{0}</td>
    </tr>
    <tr>
      <td>
        <i class="Microchip icon"></i> CPU 核心數
      </td>
      <td>{1}</td>
      
    </tr>
    <tr>
      <td>
        <i class="Microchip icon"></i> CPU 主頻
      </td>
      <td>{2}</td>
      
    </tr>
    <tr>
      <td>
        <i class="Archive icon"></i> 硬碟大小
      </td>
      <td>{3}</td>
      
    </tr>
    <tr>
      <td>
        <i class="Lightning icon"></i> 記憶體大小
      </td>
      <td>{4}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Database icon"></i> SWAP 交換空間大小
      </td>
      <td>{5}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Bar Chart icon"></i> 在線時長
      </td>
      <td>{6}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Pie Chart icon"></i> 系統負載
      </td>
      <td>{7}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Windows icon"></i> 系統
      </td>
      <td>{8}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Columns icon"></i> 架構
      </td>
      <td>{9}</td>
      
    </tr>
	<tr>
      <td>
        <i class="File Code Outline icon"></i> 核心
      </td>
      <td>{10}</td>
      
    </tr>
	<tr>
      <td>
        <i class="Group Object icon"></i> 虛擬化技術
      </td>
      <td>{11}</td>
      
    </tr>
  </tbody>
</table>
</div>



<div class="ui hidden divider" id="hdd"></div>

<h2 class="ui center aligned icon header">
  <i class="circular Clone icon"></i>
  硬碟 I/O
</h2>
<div class="ui hidden divider"></div>
<div class="ui container">
<table class="ui celled striped table">
  <thead>
    <tr>
	<th>次數</th>
      <th>速度</th>
  </tr></thead>
  <tbody>
    <tr>
      <td class="collapsing">
        <i class="folder icon"></i> 第一次測試
      </td>
      <td>{12}</td>
    </tr>
    <tr>
      <td>
        <i class="folder icon"></i> 第二次測試
      </td>
      <td>{13}</td>
    </tr>
    <tr>
      <td>
        <i class="folder icon"></i> 第三次測試
      </td>
      <td>{14}</td>
    </tr>

  </tbody>
</table>
</div>






<div class="ui hidden divider" id="net"></div>
<h2 class="ui center aligned icon header">
  <i class="circular Internet Explorer icon"></i>
  網路測試
</h2>
<div class="ui hidden divider"></div>
<div class="ui container">
<table class="ui compact striped table">
  <thead>
    <tr>
      <th>節點</th>
      <th>IP 地址</th>
      <th>下載速度</th>
	  <th>延遲</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CacheFly</td>
      <td>{15}</td>
      <td>{16}</td>
	  <td>{17}</td>
    </tr>
    <tr>
      <td>Linode 日本</td>
      <td>{18}</td>
      <td>{19}</td>
	  <td>{20}</td>
    </tr>
    <tr>
      <td>Linode 新加坡</td>
      <td>{21}</td>
      <td>{22}</td>
	  <td>{23}</td>
    </tr>
    <tr>
      <td>Linode 英國</td>
      <td>{24}</td>
      <td>{25}</td>
	  <td>{26}</td>
    </tr>
    <tr>
      <td>Linode 法蘭克福</td>
      <td>{27}</td>
      <td>{28}</td>
	  <td>{29}</td>
    </tr>
    <tr>
      <td>Linode 加拿大</td>
      <td>{30}</td>
      <td>{31}</td>
	  <td>{32}</td>
    </tr>
    <tr>
      <td>Softlayer 達拉斯</td>
      <td>{33}</td>
      <td>{34}</td>
	  <td>{35}</td>
    </tr>
    <tr>
      <td>Softlayer 西雅圖</td>
      <td>{36}</td>
      <td>{37}</td>
	  <td>{38}</td>
    </tr>
	<tr>
      <td>Softlayer 法蘭克福</td>
      <td>{39}</td>
      <td>{40}</td>
	  <td>{41}</td>
    </tr>
	<tr>
      <td>Softlayer 新加坡</td>
      <td>{42}</td>
      <td>{43}</td><td>{44}</td>
    </tr>
	<tr>
      <td>Softlayer 香港</td>
      <td>{45}</td>
      <td>{46}</td>
	  <td>{47}</td>
    </tr>
  </tbody>
</table>
</dev>

<div class="ui hidden divider"></div>
<div class="ui container">
<table class="ui compact striped table">
  <thead>
    <tr>
      <th>節點</th>
      <th>上傳速度</th>
      <th>下載速度</th>
	  <th>延遲</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>上海電信</td>
      <td>{48}</td>
      <td>{49}</td>
	  <td>{50}</td>
    </tr>
    <tr>
      <td>成都電信</td>
      <td>{51}</td>
      <td>{52}</td>
	  <td>{53}</td>
    </tr>
    <tr>
      <td>西安電信</td>
      <td>{54}</td>
      <td>{55}</td>
	  <td>{56}</td>
    </tr>
    <tr>
      <td>上海聯通</td>
      <td>{57}</td>
      <td>{58}</td>
	  <td>{59}</td>
    </tr>
    <tr>
      <td>重慶聯通</td>
      <td>{60}</td>
      <td>{61}</td>
	  <td>{62}</td>
    </tr>
    <tr>
      <td>西安移動</td>
      <td>{63}</td>
      <td>{64}</td>
	  <td>{65}</td>
    </tr>
    <tr>
      <td>上海移動</td>
      <td>{66}</td>
      <td>{67}</td>
	  <td>{68}</td>
    </tr>
    <tr>
      <td>成都移動</td>
      <td>{69}</td>
      <td>{70}</td>
	  <td>{71}</td>
    </tr>
  </tbody>
</table>
</div>

<div class="ui hidden divider" id="route"></div>
<h2 class="ui center aligned icon header">
  <i class="circular Blind icon"></i>
  路由追蹤
</h2>

<div class="ui hidden divider"></div>
<div class="ui container">
<div class="ui top attached tabular menu">
  <a class="item active" data-tab="first">上海移動</a>
  <a class="item" data-tab="second">上海電信</a>
  <a class="item" data-tab="third">上海聯通</a>
  <a class="item" data-tab="fourth">廣東移動</a>
  <a class="item" data-tab="fifth">廣東電信</a>
  <a class="item" data-tab="sixth">廣東聯通</a>
</div>

"""


footer = """
</div>
</div>
<div class="ui hidden divider"></div>
<div class="ui visible message">
  <p>CopyRight 2016-2018 <a href="https://www.github.com/FunctionClub">Function Club</a>. All Right Reserved.   Published By <a href="https://www.zhujiboke.com">主機部落格</a></p>
</div>

</body>
<footer>
<script type="text/javascript"> 
//平滑滾動支持
// 轉換為數字
function intval(v)
{
	v = parseInt(v);
	return isNaN(v) ? 0 : v;
}
 
// 獲取元素訊息
function getPos(e)
{
	var l = 0;
	var t  = 0;
	var w = intval(e.style.width);
	var h = intval(e.style.height);
	var wb = e.offsetWidth;
	var hb = e.offsetHeight;
	while (e.offsetParent){
		l += e.offsetLeft + (e.currentStyle?intval(e.currentStyle.borderLeftWidth):0);
		t += e.offsetTop  + (e.currentStyle?intval(e.currentStyle.borderTopWidth):0);
		e = e.offsetParent;
	}
	l += e.offsetLeft + (e.currentStyle?intval(e.currentStyle.borderLeftWidth):0);
	t  += e.offsetTop  + (e.currentStyle?intval(e.currentStyle.borderTopWidth):0);
	return {x:l, y:t, w:w, h:h, wb:wb, hb:hb};
}
 
// 獲取滾動條訊息
function getScroll() 
{
	var t, l, w, h;
	
	if (document.documentElement && document.documentElement.scrollTop) {
		t = document.documentElement.scrollTop;
		l = document.documentElement.scrollLeft;
		w = document.documentElement.scrollWidth;
		h = document.documentElement.scrollHeight;
	} else if (document.body) {
		t = document.body.scrollTop;
		l = document.body.scrollLeft;
		w = document.body.scrollWidth;
		h = document.body.scrollHeight;
	}
	return { t: t, l: l, w: w, h: h };
}
 
// 錨點(Anchor)間平滑跳轉
function scroller(el, duration)
{
	if(typeof el != 'object') { el = document.getElementById(el); }
 
	if(!el) return;
 
	var z = this;
	z.el = el;
	z.p = getPos(el);
	z.s = getScroll();
	z.clear = function(){window.clearInterval(z.timer);z.timer=null};
	z.t=(new Date).getTime();
 
	z.step = function(){
		var t = (new Date).getTime();
		var p = (t - z.t) / duration;
		if (t >= duration + z.t) {
			z.clear();
			window.setTimeout(function(){z.scroll(z.p.y, z.p.x)},13);
		} else {
			st = ((-Math.cos(p*Math.PI)/2) + 0.5) * (z.p.y-z.s.t) + z.s.t;
			sl = ((-Math.cos(p*Math.PI)/2) + 0.5) * (z.p.x-z.s.l) + z.s.l;
			z.scroll(st, sl);
		}
	};
	z.scroll = function (t, l){window.scrollTo(l, t)};
	z.timer = window.setInterval(function(){z.step();},13);
}
</script>
<script type="text/javascript">
//Tab功能支持
	$('.menu .item')
	.tab()
	;
//Message工具
$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;
//Model
$('.ui.basic.modal')
  .modal('show')
  .closable('false')
;
</script>
</footer>
</html>


"""

info = change_to_list("/tmp/info.txt")

speed = change_to_list("/tmp/speed.txt")

speed_tc = change_to_list("/tmp/speed_tc.txt")

shm = traceroute_to_dict("/tmp/shm.txt")
traceroute_to_table("/tmp/shm.txt")
shm_html = dict_to_table(shm,"first")

sht = traceroute_to_dict("/tmp/sht.txt")
traceroute_to_table("/tmp/sht.txt")
sht_html = dict_to_table(sht,"second")

shu = traceroute_to_dict("/tmp/shu.txt")
traceroute_to_table("/tmp/shu.txt")
shu_html = dict_to_table(shu,"third")

gdm = traceroute_to_dict("/tmp/gdm.txt")
traceroute_to_table("/tmp/gdm.txt")
gdm_html = dict_to_table(gdm,"fourth")

gdt = traceroute_to_dict("/tmp/gdt.txt")
traceroute_to_table("/tmp/gdt.txt")
gdt_html = dict_to_table(gdt,"fifth")

gdu = traceroute_to_dict("/tmp/gdu.txt")
traceroute_to_table("/tmp/gdu.txt")
gdu_html = dict_to_table(gdu,"sixth")


html = html.format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10],info[11],info[12],info[13],info[14], \

speed[0],speed[1],speed[2],speed[3],speed[4],speed[5],speed[6],speed[7],speed[8],speed[9],speed[10],speed[11],speed[12],speed[13],speed[14],speed[15],\

speed[16],speed[17],speed[18],speed[19],speed[20],speed[21],speed[22],speed[23],speed[24],speed[25],speed[26],speed[27],speed[28],speed[29],speed[30],speed[31],speed[32],\

speed_tc[0],speed_tc[1],speed_tc[2],speed_tc[3],speed_tc[4],speed_tc[5],speed_tc[6],speed_tc[7],speed_tc[8],speed_tc[9],speed_tc[10],speed_tc[11],speed_tc[12],\

speed_tc[13],speed_tc[14],speed_tc[15],speed_tc[16],speed_tc[17],\

speed_tc[18],speed_tc[19],speed_tc[20],speed_tc[21],speed_tc[22],speed_tc[23])

html = html + shm_html + sht_html + shu_html + gdm_html + gdt_html + gdu_html + footer

web = open("/root/report.html","w")

web.write(html)

web.close()
