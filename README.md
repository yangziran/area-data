## 中国行政区划数据

### 数据来源：
    民政部行政区划代码：[2020年1月中华人民共和国县以上行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003061536.html)
    国家统计局统计用区划和城乡划分代码：[2019年度统计用区划代码和城乡划分代码](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html)

### 说明
    根据 [民政统计代码编制规则](http://www.mca.gov.cn/article/sj/xzqh/1980/201507/20150715854848.shtml) 发现在 [2020年1月中华人民共和国县以上行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003061536.html) 中，以6590开头的区域代码没有二级单位：659000，故手动修改 659001~659010 的父级编码为：659000 。此时为保证数据树结构的完整，根据 [2019年度统计用区划代码和城乡划分代码](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html) 的数据，需要手动添加一条：659000 自治区直辖县级行政区划 的数据
    香港、澳门、台湾三地暂无二、三级数据，未找到官方发布。