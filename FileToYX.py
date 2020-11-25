import os
filePath = "/Volumes/Seagate/01学习视频/未命名文件夹2/CTF特训班视频"

str1="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export3.dtd">
<en-export export-date="20201125T160109Z" application="Evernote" version="Evernote Mac 9.4.7 Beta 1 (461684)">
<note><title>学习计划</title><content><![CDATA[<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note><h1>视频学习</h1><h2>"""

str2="""</h2><div style="--en-codeblock:true;--en-codeblockLanguage:javascript;box-sizing: border-box; padding: 8px; font-family: Monaco, Menlo, Consolas, &quot;Courier New&quot;, monospace; font-size: 12px; color: rgb(51, 51, 51); border-top-left-radius: 4px; border-top-right-radius: 4px; border-bottom-right-radius: 4px; border-bottom-left-radius: 4px; background-color: rgb(251, 250, 248); border: 1px solid rgba(0, 0, 0, 0.14902); background-position: initial initial; background-repeat: initial initial; margin-top: 6px;">"""

str3="""</div><table style="--en-fitwindow:true;--en-headInfos:[{&quot;style&quot;:{},&quot;text&quot;:&quot;序号&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;名称&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;进度&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;评分&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;开始时间&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;},{&quot;style&quot;:{},&quot;text&quot;:&quot;结束时间&quot;,&quot;cellStyle&quot;:{&quot;height&quot;:30},&quot;countType&quot;:&quot;count&quot;}];--en-showCount:false;--en-type:smarttable;border-left:1px solid #d9d9d9;border-top:1px solid #d9d9d9;border-collapse:collapse;width:2218px;text-align:left;" width="2218px"><colgroup><col style="width: 25px;" /><col style="width: 190px;" /><col style="width: 190px;" /><col style="width: 190px;" /><col style="width: 160px;" /><col style="width: 160px;" /><col style="width: 539px;" /><col style="width: 539px;" /></colgroup><thead><tr style="--en-compatible:true"><td>序号</td><td>名称</td><td>进度</td><td>评分</td><td>开始时间</td><td>结束时间</td></tr></thead><tbody>"""

str4="""<tr><td style="--en-typeInfo:{&quot;type&quot;:&quot;number&quot;,&quot;data&quot;:{&quot;decimal&quot;:&quot;none&quot;,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:null,&quot;showTime&quot;:null,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606319858923;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>"""

str5="""</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;text&quot;,&quot;data&quot;:{}};--en-createTime:1606319858924;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>"""

str6="""</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;progressBar&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:null,&quot;showTime&quot;:null,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606321228570;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>0</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;degree&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:null,&quot;showTime&quot;:null,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:&quot;star&quot;,&quot;maxDegree&quot;:5}};--en-createTime:1606321228573;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div>0</div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;date&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:&quot;YYYY/MM/DD&quot;,&quot;showTime&quot;:false,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606321228574;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div><br /></div></td><td style="--en-typeInfo:{&quot;type&quot;:&quot;date&quot;,&quot;data&quot;:{&quot;decimal&quot;:null,&quot;currencyType&quot;:null,&quot;dateFormat&quot;:&quot;YYYY/MM/DD&quot;,&quot;showTime&quot;:false,&quot;options&quot;:null,&quot;min&quot;:0,&quot;max&quot;:100,&quot;icons&quot;:null,&quot;maxDegree&quot;:null}};--en-createTime:1606321228575;--en-createMember:fix me here;border-right:1px solid #d9d9d9;border-bottom:1px solid #d9d9d9;padding:10px;"><div><br /></div></td></tr>"""

str7="""</tbody></table><div><br /></div></en-note>]]></content><created>20201125T140528Z</created><updated>20201125T160057Z</updated><note-attributes><latitude>30.49432373046875</latitude><longitude>104.0858603089731</longitude><altitude>474.50732421875</altitude><author>数数1234</author><source>yinxiang.superNote</source><reminder-order>0</reminder-order><content-class>yinxiang.superNote</content-class></note-attributes></note>
</en-export>"""

filename=[]
for root, dirs, files in os.walk(filePath):
    print("root", root)  # 当前目录路径
    print("dirs", dirs)  # 当前路径下所有子目录
    print("files", files)  # 当前路径下所有非目录子文件

for files in os.listdir(filePath):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
    print(files)
    filename.append(files)

print(filename)
with open('test.enex','w') as fi:
    fi.write(str1)
    fi.write(filePath.split('/')[-1])
    fi.write(str2)
    fi.write(filePath)
    fi.write(str3)
    for i in range(len(filename)):
        fi.write(str4)
        fi.write(str(i+1))
        fi.write(str5)
        fi.write(filename[i])
        fi.write(str6)
    fi.write(str7)