import os
filePath = '/Users/liuyao/Downloads/给学生推荐python书籍'

str1="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export3.dtd">
<en-export export-date="20201125T144417Z" application="Evernote" version="Evernote Mac 9.4.7 Beta 1 (461684)">
<note><title>学习计划</title><content><![CDATA[<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note><h1>视频学习</h1><h2>测试标题-2020-10-12</h2><table style="--en-fitwindow:false;--en-headInfos:[{&quot;style&quot;:{},&quot;text&quot;:&quot;名称&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;进度&quot;,&quot;cellStyle&quot;:{},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;开始时间&quot;,&quot;cellStyle&quot;:{},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;结束时间&quot;,&quot;cellStyle&quot;:{},&quot;countType&quot;:&quot;count&quot;}];--en-showCount:true;--en-type:smarttable;border-left:1px solid #d9d9d9;border-top:1px solid #d9d9d9;border-collapse:collapse;width:760px;text-align:left;" width="760px"><colgroup><col style="width: 190px;" /><col style="width: 190px;" /><col style="width: 190px;" /><col style="width: 190px;" /></colgroup><thead><tr style="--en-compatible:true"><td>名称</td><td>进度</td><td>开始时间</td><td>结束时间</td></tr></thead><tbody>"""

str2="""<tr><td style="--en-typeInfo:{&quot;type&quot;:&quot;text&quot;,&quot;data&quot;:{}};--en-createTime:1606315343159;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>"""

str3="""</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;progressBar&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:null,&quot;showTime&quot;:null,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606315343160;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>0</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;date&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:&quot;YYYY/MM/DD&quot;,&quot;showTime&quot;:false,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606315343161;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div><br /></div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;date&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:&quot;YYYY/MM/DD&quot;,&quot;showTime&quot;:false,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606315343162;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div><br /></div></td></tr>"""

str4="""</tbody></table></en-note>]]></content><created>20201125T140528Z</created><updated>20201125T144405Z</updated><note-attributes><latitude>30.49432373046875</latitude><longitude>104.0858603089731</longitude><altitude>474.50732421875</altitude><author>数数1234</author><source>yinxiang.superNote</source><reminder-order>0</reminder-order><content-class>yinxiang.superNote</content-class></note-attributes></note>
</en-export>"""

filename=[]
for i,j,k in os.walk(filePath):
    filename=k

print(filename)
with open('test.enex','w') as fi:
    fi.write(str1)
    for i in filename:
        fi.write(str2)
        fi.write(i)
        fi.write(str3)
    fi.write(str4)