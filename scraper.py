from bs4 import BeautifulSoup
import json
import re

food = re.compile("(^.+)\(([A-Z]{0,4})\)")

html = """
<div style="width:980px;padding:0px 5px;margin:0px auto;background-color:#fff;">

    <div id="column2">


<table cellpadding="0" cellspacing="0" border="0" bgcolor="" width="100%"><tbody><tr>
<td height="0"><img src="null/img/b.gif" border="0" height="0" width="1" alt=""></td>
</tr></tbody></table></div>


<div id="column1" style="float:right;width:300px;padding:10px 0px 0px 0px;">



	 
<div style="padding:3px 0px 9px 0px;text-align:center;">
 	
 	
<div style="text-align:center;" class="boldGreyNine">advertisement</div>
	
<span id="adv300x250"><script type="text/javascript">
<!--
var tempHTML = '';
var adURL = 'http://ad.doubleclick.net/adi/'+((GetCookie('etsFlag'))?'ets.wsj.com':'interactive.wsj.com')+'/marketsdata_usstocks;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';ptile=2;sz=300x250;ord=23221232212322123221;';
if ( isSafari ) {
  tempHTML += '<iframe id="adR" src="'+adURL+'" width="300" height="250" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:300">';
} else {
  tempHTML += '<iframe id="adR" src="/static_html_files/blank.htm" width="300" height="250" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:300px;">';
  ListOfIframes.adR= adURL;
}
tempHTML += '<a href="http://ad.doubleclick.net/jump/'+((GetCookie('etsFlag'))?'ets.wsj.com':'interactive.wsj.com')+'/marketsdata_usstocks;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';ptile=2;sz=300x250;ord=23221232212322123221;" target="_new">';
tempHTML += '<img src="http://ad.doubleclick.net/ad/'+((GetCookie('etsFlag'))?'ets.wsj.com':'interactive.wsj.com')+'/marketsdata_usstocks;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';ptile=2;sz=300x250;ord=23221232212322123221;" border="0" width="300" height="250" vspace="0" alt="Advertisement" /></a><br /></iframe>';
document.write(tempHTML);
// -->
</script><iframe id="adR" src="http://ad.doubleclick.net/adi/interactive.wsj.com/marketsdata_usstocks;!category=;msrc=null;null;;ptile=2;sz=300x250;ord=23221232212322123221;" width="300" height="250" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="display: none !important;" hidden=""><a href="http://ad.doubleclick.net/jump/interactive.wsj.com/marketsdata_usstocks;!category=;msrc=null;null;;ptile=2;sz=300x250;ord=23221232212322123221;" target="_new"><img src="http://ad.doubleclick.net/ad/interactive.wsj.com/marketsdata_usstocks;!category=;msrc=null;null;;ptile=2;sz=300x250;ord=23221232212322123221;" border="0" width="300" height="250" vspace="0" alt="Advertisement" /></a><br /></iframe>
</span>
</div>

</div>

<div id="column0" style="width:645px;padding:10px 0px 0px 5px;">



	<script type="text/javascript" language="JavaScript">

var arrPos = new Array();
function countHypen()
{
var compUrl=document.location.href;
var chip_Pos,k =0;


var i =  compUrl.indexOf("-");
var numChips;
var j =  compUrl.indexOf(".html");

for (i=0;i < j+1;i++)
{
text = compUrl.substring(i,i+1);
if (text.match('-'))
{
chip_Pos = i;
arrPos[k]=i;
k++;
}

}

arrPos[arrPos.length]=j;
return k+1;
};


function chipReplace(chipnum, chipvalue)
{
var searchChip = chipnum;
var replaceStr = '-'+chipvalue;
var compUrl=document.location.href;

k = countHypen();
var arrValues = new Array();



for (i=0; i < k;i++)
{
arrValues[i]=compUrl.substring(arrPos[i],arrPos[i+1]);
}


var searchStr = arrValues[chipnum];

var oldURL = compUrl.substring(0,compUrl.lastIndexOf(".html"));

var newURL = compUrl.replace(searchStr,replaceStr);

window.location= newURL;

};

function getXmlFeedData(xmlfname,csvfname)
{

var completeUrl=document.location.href;

var part1 =  completeUrl.indexOf("/mdc");

var i1 =  completeUrl.lastIndexOf("-");
var j1 =  completeUrl.indexOf(".html");

var storeDate = completeUrl.substring(i1+1,j1);

var lastChipVal ='';

var arrVal = new Array();
 
arrVal = completeUrl.match(/\d{8}/);

if (arrVal){
lastChipVal = arrVal[0];
}

//alert(" Date is "+lastChipVal);

var finalUrl = completeUrl.substring(0,part1)+'/mdc/public/npage/2_3045-'+xmlfname+lastChipVal+'-'+csvfname+'.html';

//alert (finalUrl);

window.location.href =finalUrl ;

};

</script>










<script language="javascript" type="text/javascript">var tableDate="09/20/2018";</script>
<div class="mdcNarrowM">
<div class="mdcHead">
<span class="mdcTblName">NYSE Most Active Stocks</span>
<span style="padding-left:8px;"> | 
<a onclick="chipReplace('0','activnnm'); return false;" class="linkb11" href="/mdc/public/page/2_3021-activnnm-actives.html">Nasdaq</a> |
<a onclick="chipReplace('0','activarca'); return false;" class="linkb11" href="/mdc/public/page/2_3021-activarca-actives.html">Arca</a> |
<a onclick="chipReplace('0','activcomp'); return false;" class="linkb11" href="/mdc/public/page/2_3021-activcomp-actives.html">Composite</a>
</span>
</div>
<div style="padding-top:2px;padding-bottom:2px;border-top:1px solid #B49D49;" class="tbltime">
<span style="display: block; padding-right: 4px; padding-bottom: 5px;" id="showCal">
<div style="float: right;" id="histcalendar">
<a onclick="document.getElementById('findHist').style.color='#FF9933';" style="text-decoration:none;" class="unvisited" href="javascript:lcs(document.getElementById('histcalendar'))">
<span style="padding-right:4px;font-weight:normal;font-size:12px;" class="unvisited" id="findHist">Find Historical Data</span>
<img width="27" align="absbottom" style="border:0px;" src="/img/cal.gif" height="19">
</a>
<span style="padding-right:0px;padding-left:5px;" id="whatis" class="text">
<span style="padding-right:4px;font-weight:normal;font-size:10px;" class="text">|</span>
<a onclick="OpenWin(this.href,'Whats_this',630,510,'tool,scroll,resize',true,153,40); return false;" href="/static_html_files/whatsthis.html" class="p10 unvisited">WHAT'S THIS?</a>
</span>
</div>
</span>
<script type="text/javascript" language="javascript">
<!--

 if (typeof (mdcTableArchived)!= "undefined"){

  if(mdcTableArchived) 
	document.getElementById('showCal').style.display = 'block';
}
else
{
 
}
-->
</script>
<span>Thursday,  September 20, 2018 - 5:32 pm ET</span>
</div>
<table border="0" cellspacing="0" cellpadding="0" class="mdcTable" width="100%">
<tbody><tr>
<td style="text-align:left" class="colhead">&nbsp;</td>
<td style="text-align:left" class="colhead">Issue<span class="textb10gray" style="margin-left: 8px;">(Roll over for charts and headlines)</span>
</td>
<td class="colhead">Volume</td>
<td class="colhead">Price</td>
<td style="width:35px;" class="colhead">Chg</td>
<td class="colhead">% Chg</td>
</tr>
<tr>
<td class="num">1</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=GE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'GE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">General Electric (GE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">87,503,875</td>
<td class="nnum">$12.46</td>
<td class="nnum">-0.40</td>
<td style="border-right:0px" class="nnum">-3.11</td>
</tr>
<tr>
<td class="num">2</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=BAC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'BAC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Bank of America (BAC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">82,486,805</td>
<td class="pnum">31.19</td>
<td class="pnum">0.19</td>
<td style="border-right:0px" class="pnum">0.61</td>
</tr>
<tr>
<td class="num">3</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=F" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'F')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Ford Motor (F)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">42,619,979</td>
<td class="pnum">9.81</td>
<td class="pnum">0.03</td>
<td style="border-right:0px" class="pnum">0.31</td>
</tr>
<tr>
<td class="num">4</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NIO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NIO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">NIO ADR (NIO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">40,101,324</td>
<td class="pnum">8.78</td>
<td class="pnum">0.28</td>
<td style="border-right:0px" class="pnum">3.29</td>
</tr>
<tr>
<td class="num">5</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ELAN" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ELAN')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Elanco Animal Health (ELAN)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">39,964,397</td>
<td class="pnum">36.00</td>
<td class="pnum">12.00</td>
<td style="border-right:0px" class="pnum">50.00</td>
</tr>
<tr>
<td class="num">6</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CHK" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CHK')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Chesapeake Energy (CHK)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">29,021,429</td>
<td class="pnum">4.41</td>
<td class="pnum">0.11</td>
<td style="border-right:0px" class="pnum">2.56</td>
</tr>
<tr>
<td class="num">7</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SNAP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SNAP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Snap (SNAP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">26,423,966</td>
<td class="pnum">9.21</td>
<td class="pnum">0.05</td>
<td style="border-right:0px" class="pnum">0.55</td>
</tr>
<tr>
<td class="num">8</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ORCL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ORCL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Oracle (ORCL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">26,178,789</td>
<td class="pnum">50.43</td>
<td class="pnum">1.00</td>
<td style="border-right:0px" class="pnum">2.02</td>
</tr>
<tr>
<td class="num">9</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=T" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'T')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">AT&amp;T (T)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">24,308,489</td>
<td class="pnum">33.44</td>
<td class="pnum">0.07</td>
<td style="border-right:0px" class="pnum">0.21</td>
</tr>
<tr>
<td class="num">10</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=C" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'C')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Citigroup (C)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">23,317,893</td>
<td class="pnum">74.79</td>
<td class="pnum">1.07</td>
<td style="border-right:0px" class="pnum">1.45</td>
</tr>
<tr>
<td class="num">11</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SWN" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SWN')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Southwestern Energy (SWN)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">23,036,790</td>
<td class="pnum">5.64</td>
<td class="pnum">0.13</td>
<td style="border-right:0px" class="pnum">2.36</td>
</tr>
<tr>
<td class="num">12</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KEY" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KEY')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">KeyCorp (KEY)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">23,029,973</td>
<td class="pnum">20.75</td>
<td class="pnum">0.58</td>
<td style="border-right:0px" class="pnum">2.88</td>
</tr>
<tr>
<td class="num">13</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=BABA" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'BABA')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Alibaba Group Holding ADR (BABA)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">22,007,391</td>
<td class="pnum">165.88</td>
<td class="pnum">3.25</td>
<td style="border-right:0px" class="pnum">2.00</td>
</tr>
<tr>
<td class="num">14</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=FCX" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'FCX')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Freeport-McMoRan (FCX)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">21,682,724</td>
<td class="pnum">14.39</td>
<td class="pnum">0.09</td>
<td style="border-right:0px" class="pnum">0.63</td>
</tr>
<tr>
<td class="num">15</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ABEV" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ABEV')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Ambev ADR (ABEV)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">21,135,001</td>
<td class="pnum">4.62</td>
<td class="pnum">0.05</td>
<td style="border-right:0px" class="pnum">1.09</td>
</tr>
<tr>
<td class="num">16</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RIG" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RIG')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Transocean (RIG)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">20,630,271</td>
<td class="pnum">12.63</td>
<td class="pnum">0.27</td>
<td style="border-right:0px" class="pnum">2.18</td>
</tr>
<tr>
<td class="num">17</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=WFC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'WFC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Wells Fargo (WFC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">20,011,088</td>
<td class="pnum">55.55</td>
<td class="pnum">0.33</td>
<td style="border-right:0px" class="pnum">0.60</td>
</tr>
<tr>
<td class="num">18</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CGC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CGC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Canopy Growth (CGC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">18,949,581</td>
<td class="pnum">52.40</td>
<td class="pnum">3.05</td>
<td style="border-right:0px" class="pnum">6.18</td>
</tr>
<tr>
<td class="num">19</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=VALE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'VALE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Vale ADR (VALE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">18,511,847</td>
<td class="pnum">14.52</td>
<td class="pnum">0.30</td>
<td style="border-right:0px" class="pnum">2.11</td>
</tr>
<tr>
<td class="num">20</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=PFE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'PFE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Pfizer (PFE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">16,640,660</td>
<td class="pnum">43.75</td>
<td class="pnum">0.49</td>
<td style="border-right:0px" class="pnum">1.13</td>
</tr>
<tr>
<td class="num">21</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=FTV" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'FTV')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Fortive (FTV)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">16,468,599</td>
<td class="pnum">87.37</td>
<td class="pnum">1.38</td>
<td style="border-right:0px" class="pnum">1.60</td>
</tr>
<tr>
<td class="num">22</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=JPM" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'JPM')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">JPMorgan Chase (JPM)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">15,201,740</td>
<td class="pnum">118.63</td>
<td class="pnum">1.01</td>
<td style="border-right:0px" class="pnum">0.86</td>
</tr>
<tr>
<td class="num">23</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=TWTR" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'TWTR')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Twitter (TWTR)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">14,683,412</td>
<td class="pnum">29.85</td>
<td class="pnum">0.33</td>
<td style="border-right:0px" class="pnum">1.12</td>
</tr>
<tr>
<td class="num">24</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ABX" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ABX')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Barrick Gold (ABX)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">13,922,028</td>
<td class="pnum">10.62</td>
<td class="pnum">0.02</td>
<td style="border-right:0px" class="pnum">0.19</td>
</tr>
<tr>
<td class="num">25</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NOK" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NOK')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Nokia ADR (NOK)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">13,494,788</td>
<td class="pnum">5.52</td>
<td class="pnum">0.06</td>
<td style="border-right:0px" class="pnum">1.10</td>
</tr>
<tr>
<td class="num">26</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=VZ" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'VZ')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Verizon Communications (VZ)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">13,243,253</td>
<td class="pnum">53.95</td>
<td class="pnum">0.45</td>
<td style="border-right:0px" class="pnum">0.84</td>
</tr>
<tr>
<td class="num">27</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=PBR" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'PBR')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Petroleo Brasileiro ADR (PBR)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">13,221,885</td>
<td class="pnum">11.36</td>
<td class="pnum">0.11</td>
<td style="border-right:0px" class="pnum">0.98</td>
</tr>
<tr>
<td class="num">28</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=VIPS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'VIPS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Vipshop Holdings ADR (VIPS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">12,389,095</td>
<td class="pnum">6.55</td>
<td class="pnum">0.22</td>
<td style="border-right:0px" class="pnum">3.48</td>
</tr>
<tr>
<td class="num">29</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KKR" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KKR')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">KKR Cl A (KKR)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">12,327,276</td>
<td class="pnum">28.02</td>
<td class="pnum">0.13</td>
<td style="border-right:0px" class="pnum">0.47</td>
</tr>
<tr>
<td class="num">30</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NLY" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NLY')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Annaly Capital Management (NLY)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">12,315,635</td>
<td class="pnum">10.31</td>
<td class="pnum">0.03</td>
<td style="border-right:0px" class="pnum">0.29</td>
</tr>
<tr>
<td class="num">31</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=WFT" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'WFT')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Weatherford International (WFT)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">12,135,444</td>
<td class="pnum">2.57</td>
<td class="pnum">0.05</td>
<td style="border-right:0px" class="pnum">1.98</td>
</tr>
<tr>
<td class="num">32</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KMI" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KMI')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Kinder Morgan (KMI)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,958,296</td>
<td class="nnum">18.04</td>
<td class="nnum">-0.22</td>
<td style="border-right:0px" class="nnum">-1.20</td>
</tr>
<tr>
<td class="num">33</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=EGO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'EGO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Eldorado Gold (EGO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,779,232</td>
<td class="nnum">0.89</td>
<td class="nnum">-0.07</td>
<td style="border-right:0px" class="nnum">-7.48</td>
</tr>
<tr>
<td class="num">34</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ITUB" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ITUB')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Itau Unibanco Holding ADR (ITUB)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,622,202</td>
<td class="pnum">10.64</td>
<td class="pnum">0.13</td>
<td style="border-right:0px" class="pnum">1.24</td>
</tr>
<tr>
<td class="num">35</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=HST" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'HST')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Host Hotels&amp;Resorts (HST)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,570,525</td>
<td class="pnum">21.22</td>
<td class="pnum">0.08</td>
<td style="border-right:0px" class="pnum">0.38</td>
</tr>
<tr>
<td class="num">36</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=UAA" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'UAA')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Under Armour Cl A (UAA)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,530,136</td>
<td class="pnum">20.00</td>
<td class="pnum">1.24</td>
<td style="border-right:0px" class="pnum">6.61</td>
</tr>
<tr>
<td class="num">37</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=MS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'MS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Morgan Stanley (MS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,505,348</td>
<td class="pnum">49.88</td>
<td class="pnum">0.78</td>
<td style="border-right:0px" class="pnum">1.59</td>
</tr>
<tr>
<td class="num">38</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CLF" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CLF')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Cleveland-Cliffs (CLF)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,208,468</td>
<td class="pnum">12.22</td>
<td class="pnum">0.11</td>
<td style="border-right:0px" class="pnum">0.91</td>
</tr>
<tr>
<td class="num">39</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=GM" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'GM')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">General Motors (GM)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,147,104</td>
<td class="pnum">36.08</td>
<td class="pnum">0.35</td>
<td style="border-right:0px" class="pnum">0.98</td>
</tr>
<tr>
<td class="num">40</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ESV" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ESV')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">ENSCO (ESV)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">11,082,556</td>
<td class="pnum">7.70</td>
<td class="pnum">0.09</td>
<td style="border-right:0px" class="pnum">1.18</td>
</tr>
<tr>
<td class="num">41</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=EB" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'EB')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Eventbrite (EB)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,831,576</td>
<td class="pnum">36.50</td>
<td class="pnum">13.50</td>
<td style="border-right:0px" class="pnum">58.70</td>
</tr>
<tr>
<td class="num">42</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CTL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CTL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">CenturyLink (CTL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,803,965</td>
<td class="nnum">22.57</td>
<td class="nnum">-0.17</td>
<td style="border-right:0px" class="nnum">-0.75</td>
</tr>
<tr>
<td class="num">43</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=VER" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'VER')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">VEREIT (VER)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,800,200</td>
<td class="pnum">7.46</td>
<td class="pnum">0.11</td>
<td style="border-right:0px" class="pnum">1.50</td>
</tr>
<tr>
<td class="num">44</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=WMB" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'WMB')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Williams (WMB)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,710,317</td>
<td class="pnum">28.25</td>
<td class="pnum">0.06</td>
<td style="border-right:0px" class="pnum">0.21</td>
</tr>
<tr>
<td class="num">45</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=FBP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'FBP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">First BanCorp (Puerto Rico) (FBP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,694,598</td>
<td class="pnum">9.04</td>
<td class="pnum">0.42</td>
<td style="border-right:0px" class="pnum">4.87</td>
</tr>
<tr>
<td class="num">46</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ATUS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ATUS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Altice USA Cl A (ATUS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,457,813</td>
<td class="pnum">19.21</td>
<td class="pnum">0.25</td>
<td style="border-right:0px" class="pnum">1.32</td>
</tr>
<tr>
<td class="num">47</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=XOM" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'XOM')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Exxon Mobil (XOM)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,405,128</td>
<td class="pnum">84.82</td>
<td class="pnum">0.19</td>
<td style="border-right:0px" class="pnum">0.22</td>
</tr>
<tr>
<td class="num">48</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RRC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RRC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Range Resources (RRC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">10,168,830</td>
<td class="pnum">17.82</td>
<td class="pnum">0.63</td>
<td style="border-right:0px" class="pnum">3.66</td>
</tr>
<tr>
<td class="num">49</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RHT" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RHT')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Red Hat (RHT)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,930,860</td>
<td class="nnum">133.81</td>
<td class="nnum">-9.35</td>
<td style="border-right:0px" class="nnum">-6.53</td>
</tr>
<tr>
<td class="num">50</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Southern (SO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,848,830</td>
<td class="nnum">43.29</td>
<td class="nnum">-0.41</td>
<td style="border-right:0px" class="nnum">-0.94</td>
</tr>
<tr>
<td class="num">51</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=HPQ" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'HPQ')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">HP (HPQ)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,831,748</td>
<td class="pnum">25.69</td>
<td class="pnum">0.43</td>
<td style="border-right:0px" class="pnum">1.70</td>
</tr>
<tr>
<td class="num">52</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SAN" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SAN')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Banco Santander ADR (SAN)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,705,553</td>
<td class="pnum">5.41</td>
<td class="pnum">0.16</td>
<td style="border-right:0px" class="pnum">3.05</td>
</tr>
<tr>
<td class="num">53</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=JCP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'JCP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">J.C. Penney (JCP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,626,139</td>
<td class="num">2.00</td>
<td class="num">0.00</td>
<td style="border-right:0px" class="num">0.00</td>
</tr>
<tr>
<td class="num">54</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=AUY" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'AUY')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Yamana Gold (AUY)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,537,094</td>
<td class="nnum">2.54</td>
<td class="nnum">-0.02</td>
<td style="border-right:0px" class="nnum">-0.78</td>
</tr>
<tr>
<td class="num">55</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=INFY" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'INFY')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Infosys ADR (INFY)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,336,611</td>
<td class="pnum">10.07</td>
<td class="pnum">0.06</td>
<td style="border-right:0px" class="pnum">0.60</td>
</tr>
<tr>
<td class="num">56</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=AKS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'AKS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">AK Steel Holding (AKS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,327,982</td>
<td class="pnum">4.85</td>
<td class="pnum">0.06</td>
<td style="border-right:0px" class="pnum">1.25</td>
</tr>
<tr>
<td class="num">57</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Coca-Cola (KO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,268,593</td>
<td class="pnum">46.64</td>
<td class="pnum">0.68</td>
<td style="border-right:0px" class="pnum">1.48</td>
</tr>
<tr>
<td class="num">58</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ADT" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ADT')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">ADT (ADT)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,255,001</td>
<td class="pnum">8.92</td>
<td class="pnum">0.55</td>
<td style="border-right:0px" class="pnum">6.57</td>
</tr>
<tr>
<td class="num">59</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=PG" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'PG')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Procter&amp;Gamble (PG)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,124,883</td>
<td class="pnum">85.36</td>
<td class="pnum">1.36</td>
<td style="border-right:0px" class="pnum">1.62</td>
</tr>
<tr>
<td class="num">60</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SQ" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SQ')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Square Cl A (SQ)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,068,869</td>
<td class="pnum">86.51</td>
<td class="pnum">1.71</td>
<td style="border-right:0px" class="pnum">2.02</td>
</tr>
<tr>
<td class="num">61</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=BP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'BP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">BP ADR (BP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">9,008,909</td>
<td class="pnum">44.57</td>
<td class="pnum">0.59</td>
<td style="border-right:0px" class="pnum">1.34</td>
</tr>
<tr>
<td class="num">62</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=TEVA" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'TEVA')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Teva Pharmaceutical Industries ADR (TEVA)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,946,002</td>
<td class="pnum">24.83</td>
<td class="pnum">0.19</td>
<td style="border-right:0px" class="pnum">0.77</td>
</tr>
<tr>
<td class="num">63</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NWL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NWL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Newell Brands (NWL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,797,797</td>
<td class="pnum">22.00</td>
<td class="pnum">0.36</td>
<td style="border-right:0px" class="pnum">1.66</td>
</tr>
<tr>
<td class="num">64</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KR" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KR')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Kroger (KR)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,775,062</td>
<td class="pnum">29.18</td>
<td class="pnum">0.30</td>
<td style="border-right:0px" class="pnum">1.04</td>
</tr>
<tr>
<td class="num">65</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RF" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RF')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Regions Financial (RF)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,665,679</td>
<td class="pnum">19.49</td>
<td class="pnum">0.33</td>
<td style="border-right:0px" class="pnum">1.72</td>
</tr>
<tr>
<td class="num">66</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=HPE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'HPE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Hewlett Packard Enterprise (HPE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,410,674</td>
<td class="pnum">16.87</td>
<td class="pnum">0.23</td>
<td style="border-right:0px" class="pnum">1.38</td>
</tr>
<tr>
<td class="num">67</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SBGL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SBGL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Sibanye-Stillwater ADR (SBGL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,110,198</td>
<td class="nnum">2.51</td>
<td class="nnum">-0.05</td>
<td style="border-right:0px" class="nnum">-1.95</td>
</tr>
<tr>
<td class="num">68</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=X" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'X')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">United States Steel (X)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">8,022,106</td>
<td class="num">29.85</td>
<td class="num">0.00</td>
<td style="border-right:0px" class="num">0.00</td>
</tr>
<tr>
<td class="num">69</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=STM" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'STM')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">STMicroelectronics (STM)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,995,866</td>
<td class="pnum">19.06</td>
<td class="pnum">0.76</td>
<td style="border-right:0px" class="pnum">4.15</td>
</tr>
<tr>
<td class="num">70</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=DNR" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'DNR')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Denbury Resources (DNR)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,970,321</td>
<td class="nnum">5.54</td>
<td class="nnum">-0.05</td>
<td style="border-right:0px" class="nnum">-0.89</td>
</tr>
<tr>
<td class="num">71</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=DWDP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'DWDP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">DowDuPont (DWDP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,898,139</td>
<td class="pnum">70.03</td>
<td class="pnum">1.30</td>
<td style="border-right:0px" class="pnum">1.89</td>
</tr>
<tr>
<td class="num">72</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=GGB" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'GGB')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Gerdau ADR (GGB)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,888,075</td>
<td class="pnum">4.15</td>
<td class="pnum">0.10</td>
<td style="border-right:0px" class="pnum">2.47</td>
</tr>
<tr>
<td class="num">73</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=KGC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'KGC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Kinross Gold (KGC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,824,475</td>
<td class="nnum">3.01</td>
<td class="nnum">-0.02</td>
<td style="border-right:0px" class="nnum">-0.66</td>
</tr>
<tr>
<td class="num">74</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=MRO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'MRO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Marathon Oil (MRO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,812,349</td>
<td class="nnum">21.55</td>
<td class="nnum">-0.21</td>
<td style="border-right:0px" class="nnum">-0.97</td>
</tr>
<tr>
<td class="num">75</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=PHM" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'PHM')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">PulteGroup (PHM)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,759,714</td>
<td class="nnum">26.39</td>
<td class="nnum">-0.30</td>
<td style="border-right:0px" class="nnum">-1.12</td>
</tr>
<tr>
<td class="num">76</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=HAL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'HAL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Halliburton (HAL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,347,460</td>
<td class="pnum">40.39</td>
<td class="pnum">0.33</td>
<td style="border-right:0px" class="pnum">0.82</td>
</tr>
<tr>
<td class="num">77</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=AVP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'AVP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Avon Products (AVP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,259,249</td>
<td class="pnum">2.40</td>
<td class="pnum">0.08</td>
<td style="border-right:0px" class="pnum">3.45</td>
</tr>
<tr>
<td class="num">78</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=GLW" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'GLW')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Corning (GLW)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,195,702</td>
<td class="pnum">36.13</td>
<td class="pnum">0.88</td>
<td style="border-right:0px" class="pnum">2.50</td>
</tr>
<tr>
<td class="num">79</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SPN" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SPN')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Superior Energy Services (SPN)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,194,531</td>
<td class="nnum">9.61</td>
<td class="nnum">-0.10</td>
<td style="border-right:0px" class="nnum">-1.03</td>
</tr>
<tr>
<td class="num">80</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RDC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RDC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Rowan Cos. (RDC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">7,024,867</td>
<td class="pnum">17.48</td>
<td class="pnum">0.74</td>
<td style="border-right:0px" class="pnum">4.42</td>
</tr>
<tr>
<td class="num">81</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=COTY" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'COTY')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Coty Cl A (COTY)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,992,387</td>
<td class="pnum">13.01</td>
<td class="pnum">0.35</td>
<td style="border-right:0px" class="pnum">2.76</td>
</tr>
<tr>
<td class="num">82</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=DIS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'DIS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Walt Disney (DIS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,983,876</td>
<td class="pnum">111.62</td>
<td class="pnum">1.83</td>
<td style="border-right:0px" class="pnum">1.67</td>
</tr>
<tr>
<td class="num">83</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=V" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'V')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">VISA Cl A (V)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,978,802</td>
<td class="pnum">149.24</td>
<td class="pnum">1.82</td>
<td style="border-right:0px" class="pnum">1.23</td>
</tr>
<tr>
<td class="num">84</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Noble (NE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,918,082</td>
<td class="pnum">6.51</td>
<td class="pnum">0.21</td>
<td style="border-right:0px" class="pnum">3.33</td>
</tr>
<tr>
<td class="num">85</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SLB" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SLB')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Schlumberger (SLB)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,913,407</td>
<td class="pnum">61.57</td>
<td class="pnum">0.34</td>
<td style="border-right:0px" class="pnum">0.56</td>
</tr>
<tr>
<td class="num">86</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=BHC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'BHC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Bausch Health (BHC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,883,990</td>
<td class="pnum">25.01</td>
<td class="pnum">0.94</td>
<td style="border-right:0px" class="pnum">3.91</td>
</tr>
<tr>
<td class="num">87</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=COG" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'COG')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Cabot Oil&amp;Gas (COG)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,838,559</td>
<td class="pnum">22.90</td>
<td class="pnum">0.64</td>
<td style="border-right:0px" class="pnum">2.88</td>
</tr>
<tr>
<td class="num">88</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=HL" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'HL')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Hecla Mining (HL)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,684,321</td>
<td class="num">3.04</td>
<td class="num">0.00</td>
<td style="border-right:0px" class="num">0.00</td>
</tr>
<tr>
<td class="num">89</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=THO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'THO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Thor Industries (THO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,654,737</td>
<td class="nnum">91.95</td>
<td class="nnum">-13.69</td>
<td style="border-right:0px" class="nnum">-12.96</td>
</tr>
<tr>
<td class="num">90</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=GG" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'GG')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Goldcorp (GG)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,633,468</td>
<td class="nnum">10.77</td>
<td class="nnum">-0.03</td>
<td style="border-right:0px" class="nnum">-0.28</td>
</tr>
<tr>
<td class="num">91</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CAT" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CAT')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Caterpillar (CAT)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,616,377</td>
<td class="pnum">156.00</td>
<td class="pnum">3.24</td>
<td style="border-right:0px" class="pnum">2.12</td>
</tr>
<tr>
<td class="num">92</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=CVS" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'CVS')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">CVS Health (CVS)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,590,862</td>
<td class="pnum">79.39</td>
<td class="pnum">0.43</td>
<td style="border-right:0px" class="pnum">0.54</td>
</tr>
<tr>
<td class="num">93</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=BEN" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'BEN')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Franklin Resources (BEN)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,532,727</td>
<td class="pnum">32.92</td>
<td class="pnum">0.46</td>
<td style="border-right:0px" class="pnum">1.42</td>
</tr>
<tr>
<td class="num">94</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=ECA" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'ECA')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Encana (ECA)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,504,970</td>
<td class="pnum">12.64</td>
<td class="pnum">0.02</td>
<td style="border-right:0px" class="pnum">0.16</td>
</tr>
<tr>
<td class="num">95</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=SKX" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'SKX')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Skechers USA Cl A (SKX)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,498,905</td>
<td class="nnum">26.58</td>
<td class="nnum">-1.26</td>
<td style="border-right:0px" class="nnum">-4.53</td>
</tr>
<tr>
<td class="num">96</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=M" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'M')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Macy's (M)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,378,769</td>
<td class="nnum">35.18</td>
<td class="nnum">-0.37</td>
<td style="border-right:0px" class="nnum">-1.04</td>
</tr>
<tr>
<td class="num">97</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=UNP" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'UNP')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Union Pacific (UNP)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,372,729</td>
<td class="pnum">164.01</td>
<td class="pnum">1.21</td>
<td style="border-right:0px" class="pnum">0.74</td>
</tr>
<tr>
<td class="num">98</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=MPC" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'MPC')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Marathon Petroleum (MPC)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,350,695</td>
<td class="pnum">81.93</td>
<td class="pnum">1.39</td>
<td style="border-right:0px" class="pnum">1.73</td>
</tr>
<tr>
<td class="num">99</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=NKE" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'NKE')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Nike Cl B (NKE)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,334,693</td>
<td class="pnum">85.37</td>
<td class="pnum">0.94</td>
<td style="border-right:0px" class="pnum">1.11</td>
</tr>
<tr>
<td class="num">100</td>
<td style="max-width:307px" class="text">
<a href="/public/quotes/main.html?symbol=RIO" class="linkb" onmouseover="com.dowjones.rolloverQuotes.show(this,'RIO')" onmouseout="com.dowjones.rolloverQuotes.hidelater();">Rio Tinto ADR (RIO)
</a>
</td>
<td style="font-weight:bold;" align="right" class="num">6,310,336</td>
<td class="pnum">51.15</td>
<td class="pnum">1.87</td>
<td style="border-right:0px" class="pnum">3.79</td>
</tr>
</tbody></table>
<div class="footer">Includes common, closed end funds, ETFs, ETNs and REITS</div>
<div class="footer">x - stock is trading ex-dividend</div>
<div class="footerSource" style="">Source: WSJ Market Data Group</div>
</div>



</div>

<div id="column3" style="clear:both;width:980px;text-align:center;">







<table cellpadding="0" cellspacing="0" border="0" bgcolor="" width="100%">
	<tbody><tr><td height="20px"><img src="/img/b.gif" border="0" height="20px" width="1" alt=""></td></tr>
</tbody></table>
<table style="border:1px solid #cfc7b7;margin-bottom:5px;" align="center" width="575px" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff">
<tbody><tr>
<td colspan="3" class="b12" bgcolor="#e9e7e0" style="padding:3px 0px 3px 0px;"><span class="p10" style="color:#000; float:right">An Advertising Feature&nbsp;&nbsp;</span>&nbsp;&nbsp;PARTNER CENTER</td>
</tr>

<tr>
<td class="p10" valign="top" align="center" style="padding:10px 0px 5px 0px;border-right:1px solid #cfc7b7;">



<script type="text/javascript">
<!--
var tempHTML = '';
var adURL = 'http://ad.doubleclick.net/adi/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=1;sz=170x67;ord=23221232212322123221;';
if ( isSafari ) {
  tempHTML += '<iframe id="mdc_tradingcenter1" src="'+adURL+'" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170">';
} else {
  tempHTML += '<iframe id="mdc_tradingcenter1" src="/static_html_files/blank.htm" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170px;">';
  ListOfIframes.mdc_tradingcenter1= adURL;
}
tempHTML += '<a href="http://ad.doubleclick.net/jump/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=1;sz=170x67;ord=23221232212322123221;" target="_new">';
tempHTML += '<img src="http://ad.doubleclick.net/ad/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=1;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>';
document.write(tempHTML);
// -->
</script><iframe id="mdc_tradingcenter1" src="http://ad.doubleclick.net/adi/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=1;sz=170x67;ord=23221232212322123221;" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="display: none !important;" hidden=""><a href="http://ad.doubleclick.net/jump/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=1;sz=170x67;ord=23221232212322123221;" target="_new"><img src="http://ad.doubleclick.net/ad/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=1;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>
</td>

<td class="p10" valign="top" align="center" style="padding:10px 0px 5px 0px;border-right:1px solid #cfc7b7;">



<script type="text/javascript">
<!--
var tempHTML = '';
var adURL = 'http://ad.doubleclick.net/adi/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=2;sz=170x67;ord=23221232212322123221;';
if ( isSafari ) {
  tempHTML += '<iframe id="mdc_tradingcenter2" src="'+adURL+'" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170">';
} else {
  tempHTML += '<iframe id="mdc_tradingcenter2" src="/static_html_files/blank.htm" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170px;">';
  ListOfIframes.mdc_tradingcenter2= adURL;
}
tempHTML += '<a href="http://ad.doubleclick.net/jump/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=2;sz=170x67;ord=23221232212322123221;" target="_new">';
tempHTML += '<img src="http://ad.doubleclick.net/ad/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=2;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>';
document.write(tempHTML);
// -->
</script><iframe id="mdc_tradingcenter2" src="http://ad.doubleclick.net/adi/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=2;sz=170x67;ord=23221232212322123221;" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="display: none !important;" hidden=""><a href="http://ad.doubleclick.net/jump/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=2;sz=170x67;ord=23221232212322123221;" target="_new"><img src="http://ad.doubleclick.net/ad/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=2;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>
</td>

<td class="p10" valign="top" align="center" style="padding:10px 0px 5px 0px;">



<script type="text/javascript">
<!--
var tempHTML = '';
var adURL = 'http://ad.doubleclick.net/adi/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=3;sz=170x67;ord=23221232212322123221;';
if ( isSafari ) {
  tempHTML += '<iframe id="mdc_tradingcenter3" src="'+adURL+'" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170">';
} else {
  tempHTML += '<iframe id="mdc_tradingcenter3" src="/static_html_files/blank.htm" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170px;">';
  ListOfIframes.mdc_tradingcenter3= adURL;
}
tempHTML += '<a href="http://ad.doubleclick.net/jump/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=3;sz=170x67;ord=23221232212322123221;" target="_new">';
tempHTML += '<img src="http://ad.doubleclick.net/ad/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=3;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>';
document.write(tempHTML);
// -->
</script><iframe id="mdc_tradingcenter3" src="http://ad.doubleclick.net/adi/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=3;sz=170x67;ord=23221232212322123221;" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="display: none !important;" hidden=""><a href="http://ad.doubleclick.net/jump/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=3;sz=170x67;ord=23221232212322123221;" target="_new"><img src="http://ad.doubleclick.net/ad/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=3;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>
</td>

</tr>

<tr>
<td class="p10" valign="top" align="center" style="padding:10px 0px 5px 0px;border-right:1px solid #cfc7b7;border-top:1px solid #cfc7b7;">



<script type="text/javascript">
<!--
var tempHTML = '';
var adURL = 'http://ad.doubleclick.net/adi/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=4;sz=170x67;ord=23221232212322123221;';
if ( isSafari ) {
  tempHTML += '<iframe id="mdc_tradingcenter4" src="'+adURL+'" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170">';
} else {
  tempHTML += '<iframe id="mdc_tradingcenter4" src="/static_html_files/blank.htm" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="width:170px;">';
  ListOfIframes.mdc_tradingcenter4= adURL;
}
tempHTML += '<a href="http://ad.doubleclick.net/jump/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=4;sz=170x67;ord=23221232212322123221;" target="_new">';
tempHTML += '<img src="http://ad.doubleclick.net/ad/'+((GetCookie('etsFlag'))?'ets.wsj.com':'brokerbuttons.wsj.com')+'/markets_front;!category=;msrc=' + msrc + ';' + segQS + ';' + mc + ';tile=4;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>';
document.write(tempHTML);
// -->
</script><iframe id="mdc_tradingcenter4" src="http://ad.doubleclick.net/adi/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=4;sz=170x67;ord=23221232212322123221;" width="170" height="67" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="display: none !important;" hidden=""><a href="http://ad.doubleclick.net/jump/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=4;sz=170x67;ord=23221232212322123221;" target="_new"><img src="http://ad.doubleclick.net/ad/brokerbuttons.wsj.com/markets_front;!category=;msrc=null;null;;tile=4;sz=170x67;ord=23221232212322123221;" border="0" width="170" height="67" vspace="0" alt="Advertisement" /></a><br /></iframe>
</td>

<td width="33%" style="border-top:1px solid #cfc7b7;">&nbsp;</td>
		
<td width="33%" style="border-top:1px solid #cfc7b7;">&nbsp;</td>
		
</tr>

</tbody></table>
<table cellpadding="0" cellspacing="0" border="0" bgcolor="" width="100%">
	<tbody><tr><td height="20px"><img src="/img/b.gif" border="0" height="20px" width="1" alt=""></td></tr>
</tbody></table>








	<script id="mNCC" language="javascript">     medianet_width = "474";     medianet_height = "250";     medianet_crid = "141666508";     medianet_versionId = "111299";      (function() {         var isSSL = 'https:' == document.location.protocol;         var mnSrc = (isSSL ? 'https:' : 'http:') + '//contextual.media.net/nmedianet.js?cid=8CU6CD37D' + (isSSL ? '&https=1' : '');         document.write('<scr' + 'ipt type="text/javascript" id="mNSC" src="' + mnSrc + '"></scr' + 'ipt>');     })();   </script><script type="text/javascript" id="mNSC" src="http://contextual.media.net/nmedianet.js?cid=8CU6CD37D"></script>
</div>

<div>
  <div class="p12" style="text-align:center;padding:17px 0px 10px 0px">

    <a href="#top" class="unvisited">Return To Top</a>

  </div>
  <div style="border-top:1px solid #ccc;">



	<h1 style="text-align: center; font-family: arial; font-size: 9px; color: #666666; padding: 15px 0px 15px 0px; border-bottom: 1px solid #CCCCCC; 
	margin:0px;">NYSE Most Active Stocks - Markets Data Center - WSJ.com</h1>

<link rel="stylesheet" media="all" type="text/css" href="http://www.wsj.com/public/npage/0_0_W0_1102-filterPageBy-I=%7BslimHeader,MDCsubnav,newGlobalFooter2012%7D.css">
<link rel="stylesheet" media="all" type="text/css" href="http://www.wsj.com/public/npage/0_0_W0_1103-filterPageBy-I=%7BslimHeader,MDCsubnav,newGlobalFooter2012%7D.css">
<link rel="stylesheet" media="all" type="text/css" href="http://www.wsj.com/public/npage/0_0_W0_1104-filterPageBy-I=%7BslimHeader,MDCsubnav,newGlobalFooter2012%7D.css">
<script>
dojo.addOnLoad = function() {

if(dojo.byId('contactUs')!=null&&dojo.byId('contactUs')!=undefined){ dojo.connect(dojo.byId('contactUs'), 'onclick', function (e) {openLiveHelp(e)});}

function openLiveHelp (ev) {
	dojo.stopEvent(ev);
	dojo.io.script.get(
	{
		url: "https://customercenter.wsj.com/livechat/services/status",
		callbackParamName: "callback",
		preventCache: true,
		content: {product:"WSJ"},
		load: function(data)
		{
			if(data["proactive"] != undefined && data["proactive"] != null && data["proactive"]["feature"] && data["proactive"]["agentsAvailable"])
			{
				window.open('https://customercenter.wsj.com/livechat/chat?product=WSJ', 'DowJones_Live_Chat','width=510,height=420,location=no,menubar=no,status=no,toolbar=no,scrollbars=no,resizable=no');return false;
			}
			else
			{
				if(typeof parent.window.location.href != "undefined"){
					parent.location=dojo.byId('contactUs').href;
				}else{
					window.location=dojo.byId('contactUs').href;
				}
			}
		}
	});
}

		dj.context.core.custChatUrl = "https://customercenter.wsj.com/livechat/chat?product=wsjmdc";
		dojo.connect(dojo.query(".liveChat")[0], "onclick", function (e) {openChatWindow(e)});
		dj.util.User.isLoggedIn(function (isLogged){
			if (isLogged) {
				if (dojo.query(".custChatLink")[0] != null)
					dojo.connect(dojo.query(".custChatLink")[0], "onclick", function (e) {openChatWindow(e)});

				dj.util.User.isSubLoggedIn(function (isSub){
					if (isSub) {
						dojo.removeClass(dojo.byId("footerFullWide"), "subType-unsubscribed");
						dojo.removeClass(dojo.byId("footerFullWide"), "sectionType-unsub-none");
						dojo.addClass(dojo.byId("footerFullWide"), "subType-subscribed");
						dojo.query(".footerLabel").removeClass("hidden");
					}
				});
				dj.util.User.isRegLoggedIn(function (isReg){
					if (isReg) {
						dojo.removeClass(dojo.byId("footerFullWide"), "subType-unsubscribed");
						dojo.removeClass(dojo.byId("footerFullWide"), "sectionType-unsub-none");
						dojo.addClass(dojo.byId("footerFullWide"), "navType-black subType-unsubscribed");
						dojo.addClass(dojo.byId("footerLogin"), "hidden");
						dojo.addClass(dojo.byId("footerReg"), "hidden");
						dojo.addClass(dojo.byId("headerPromoContainer"), "hidden");
						dj.module.header2012.userDetails.init();
					}
				});
			}
		});
	}
	function openChatWindow (ev) {
		dojo.stopEvent(ev);
		if(dj.module.header2012.userDetails.custChatWin==undefined || dj.module.header2012.userDetails.custChatWin==null||dj.module.header2012.userDetails.custChatWin.closed) {
	        dj.module.header2012.userDetails.custChatWin=window.open(dj.context.core.custChatUrl, "DowJones_Live_Chat","width=510,height=420,location=no,menubar=no,status=no,toolbar=no,scrollbars=no,resizable=no");
	    } else{
	        dj.module.header2012.userDetails.custChatWin.focus();
	    }
	}
</script>
<div class="fullwide pagewide subType-unsubscribed" id="footerFullWide">
		<div class="newFooterWrap">
			<div class="newFooter">
				<!--TOP BAR LINKS-->
				<ul class="topLinks clearFix">
					<li class="wsjLogo"><a href="https://www.wsj.com/">Wall Street Journal</a></li>
					<li class="socialLogo"><a title="Facebook" href="http://www.facebook.com/wsj" class="facebook">Facebook</a></li>
					<li class="socialLogo"><a title="Twitter" href="http://twitter.com/WSJ" class="twitter">Twitter</a></li>
					<li class="socialLogo"><a title="LinkedIn" href="http://www.linkedin.com/today/online.wsj.com" class="linkedin">LinkedIn</a></li>
					<li class="socialLogo"><a title="FourSquare" href="https://foursquare.com/wsj" class="foursquare">FourSquare</a></li>
					<li class="socialLogo"><a title="Google+" href="https://plus.google.com/117720626238470886461/posts" class="gplus" rel="publisher">Google+</a></li>
					<li class="socialLogo"><a title="YouTube" href="http://www.youtube.com/user/WSJDigitalNetwork" class="youtube">YouTube</a></li>
					<li class="socialLogo"><a title="Podcasts" href="http://www.wsj.com/public/page/podcast.html?mod=WSJ_footer" class="podcast">Podcasts</a></li>
					<li class="socialLogo"><a title="RSS" href="http://www.wsj.com/public/page/rss_news_and_feeds.html?mod=WSJ_footer" class="rssfeed">RSS Feed</a></li>
					<li class="socialLogo"><a title="AppStore" href="https://itunes.apple.com/us/app/the-wall-street-journal./id364387007?mt=8" class="appstore">AppStore</a></li>
					<li class="login_sub">
						<ul class="clearFix">
							<li class="subscribe"><a href="https://buy.wsj.com/offers/html/offerPrnDnPI.html?trackCode=aap9e0ow">Subscribe</a></li>
							<li id="footerLogin" class="login"><span>/</span><a href="https://id.wsj.com/access/509b1a086458232f6e000002/latest/login_standalone.html" ref="nofollow" data-widget="LIFP.login">Login</a></li>
						</ul>
					</li>
					<li class="backToTop"><a href="#top">Back to Top<span class="rotate">�</span></a></li>
				</ul>
				<!--MIDDLE COLUMN LINKS-->
				<ul class="contentLinks clearFix">
				<li class="linksCol"><h4>Customer Service</h4>
					<ul>
						<li><a href="http://help.wsj.com/customer-service/?mod=WSJ_footer">Customer Center</a></li>
						<li><a href="#" class="liveChat"><span class="lcHighlight">New!</span> Live Chat</a></li>
						<li><a href="https://customercenter.wsj.com/view/contactus.html?mod=WSJ_footer">Contact Us</a></li>
						<li><a href="http://www.subscribe.wsj.com/getweekendnow?mod=WSJ_footer">WSJ Weekend</a></li>
						<li><a href="https://customercenter.wsj.com/view/ctdir/contactdirectory.html?mod=WSJ_footer">Contact Directory</a></li>
						<li><a href="https://www.wsj.com/news/column/Corrections?mod=WSJ_footer" rel="nofollow">Corrections</a></li></ul></li>
						<li class="linksCol"><h4>Policy</h4>
							<ul>
								<li><a href="http://www.wsj.com/public/page/privacy-policy.html?mod=WSJ_footer" rel="nofollow">Privacy Policy</a></li>
<li> <a href="http://www.wsj.com/public/page/cookie-policy.html?mod=WSJ_footer" rel="nofollow">Cookie Policy</a></li>
								<li><a href="http://www.wsj.com/public/page/data-policy.html?mod=WSJ_footer">Data Policy</a></li>
								<li><a href="http://www.wsj.com/public/page/copyright_policy.html?mod=WSJ_footer">Copyright Policy</a></li>
								<li><a href="http://www.wsj.com/public/page/subscriber_agreement.html?mod=WSJ_footer">Subscriber Agreement<br>&amp; Terms of Use</a></li>
<li><a href="http://www.wsj.com/public/page/cookie-policy.html?mod=WSJ_footer#cookies_advertising" rel="nofollow">Your Ad Choices</a></li>
	 </ul>
      </li>
      <li class="linksCol">
        <h4>Advertise</h4>
        <ul>
          <li><a href="http://www.wsjdigital.com?mod=WSJ_footer" rel="nofollow">Advertise</a></li>
	  <li><a href="http://classifieds.wsj.com?mod=WSJ_footer" rel="nofollow">Place a Classified Ad</a></li>
	  <li><a href="https://classifieds.wsj.com/ad/Residential-Real-Estate-Ads?mod=WSJ_footer" rel="nofollow">Sell Your Home</a></li>
	  <li><a href="https://classifieds.wsj.com/ad/Business-For-Sale-Ads?mod=WSJ_footer" rel="nofollow">Sell Your Business</a></li>
	  <li><a href="https://classifieds.wsj.com/ad/Commercial-Real-Estate-Ads?mod=WSJ_footer" rel="nofollow">Commercial Real Estate Ads</a></li>
	  <li><a href="https://classifieds.wsj.com/ad/Job-Ads?mod=WSJ_footer" rel="nofollow">Recruitment &amp; Career Ads</a></li>
	  <li><a href="https://classifieds.wsj.com/ad/Franchise-For-Sale-Ads?mod=WSJ_footer" rel="nofollow">Franchising</a></li>
          <li><a href="http://www.wsjlocal.com?mod=WSJ_footer" rel="nofollow">Advertise Locally</a></li>
        </ul>
						</li>
						<li class="linksCol"><h4>Tools &amp; Features</h4>
							<ul>
								<li><a href="http://www.wsj.com/public/page/designtech-wsjModuleHome.html?mod=WSJ_footer">Apps</a></li>
								<li><a href="http://www.wsj.com/public/page/email-setup.html?mod=WSJ_footer">Emails &amp; Alerts</a></li>
								<li><a href="http://www.wsj.com/public/page/news-interactive-features-trends.html?mod=WSJ_footer">Graphics &amp; Photos</a></li>
								<li><a href="http://www.wsj.com/page/columnists.html?mod=WSJ_footer">Columns</a></li>
								<li><a href="http://topics.wsj.com/?mod=WSJ_footer">Topics</a></li>
								<li><a href="http://www.wsj.com/public/page/guides.html?mod=WSJ_footer">Guides</a></li>
								<li><a href="http://portfolio.wsj.com/?mod=wsj_port_foot">Portfolio</a></li>
								<li><a href="http://ds.wsj.com/wsjportfolio/portfolio?cmd=mainwindow&amp;mod=wsj_portold_foot">Old Portfolio</a></li>
							</ul>
						</li>
						<li class="linksCol"><h4>More</h4>
							<ul>
								<li><a href="http://subscription.wsj.com/" rel="nofollow">Why Subscribe</a></li>
								<li><a id="footerReg" class="registerUserClass" rel="nofollow" href="https://id.wsj.com/access/509b1a086458232f6e000002/latest/register_standalone.html" ref="nofollow" data-widget="LIFP.freeregistration">Register for Free</a></li><li><a href="http://www.djreprints.com/?mod=WSJ_footer">Reprints</a></li>
								<li><a href="http://wsj.com/partner/?mod=WSJ_footer">Content Partnerships</a></li>
								<li><a href="http://www.wsj.com/conferences?mod=WSJ_footer">Conferences</a></li>
								<li><a href="https://www.wsjsafehouse.com/">SafeHouse</a></li>
								<li><a href="http://m.wsj.com/">Mobile Site</a></li>
								<li class="footerLabel hidden"><a href="http://setup1.wsj.com/pznsetup/sub/pvemail/setup.html?mod=WSJ_footer">Price &amp; Volume</a></li>
								<li class="footerLabel hidden"><a href="http://setup1.wsj.com/pznsetup/sub/ksemail/setup.html?mod=WSJ_footer">Keyword &amp; Symbol</a></li>
								<li><a href="http://www.wsj.com/public/page/archive.html?mod=WSJ_footer">News Archive</a></li>
							</ul>
						</li>
					</ul>
					<!--FOOTNOTE LINKS-->
					<ul class="footnoteLinks clearFix">
						<li class="http://www.dowjones.com/careers.asp?mod=WSJ_footer"><a href="http://www.dowjones.com/careers.asp?mod=WSJ_footer">Jobs at WSJ</a></li>
						<li class="copyright">Copyright ©2017 <a href="http://www.wsj.com/public/page/copyright_policy.html?mod=WSJ_footer">Dow Jones &amp; Company</a>, Inc. All Rights Reserved.</li>
					</ul>
			</div>
		</div>
</div>
<!-- data-module-name="dj.module.footer.DesktopFooter" -->

</div>
</div>
</div>
      """

page = BeautifulSoup(html, 'html.parser')

tabs = page.find_all("tr")

data = {}
# blocks = []
for row in tabs:
  try:
    tds = row.find_all("td")
    name = tds[1].find("a").get_text()
    matches = food.match(name)
    tup = matches.group(1,2)
    
    price = tds[3].get_text()
    box = [tup[0].strip(), price]
    data[tup[1]] = box
  except:
    pass

with open('data.txt', 'w') as outfile:
  json.dump(data, outfile)