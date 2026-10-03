import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# ===================== 内置景点数据 =====================
# 字段：名称, 城市, 类型, 评分(5分制), 门票价格(元), 建议游玩时长(小时),
#       适合季节, 适合人群, 简介
SPOTS = [
    ("故宫博物院", "北京", "历史人文", 4.9, 60, 4, "四季", "全家/文化爱好者",
     "明清两代皇家宫殿，中国古代宫廷建筑精华"),
    ("八达岭长城", "北京", "历史人文", 4.7, 40, 4, "春秋", "全家/徒步",
     "万里长城最具代表性的段落，'不到长城非好汉'"),
    ("颐和园", "北京", "园林风光", 4.7, 30, 3, "夏秋", "全家",
     "中国现存规模最大的皇家园林，昆明湖万寿山"),
    ("天坛公园", "北京", "历史人文", 4.6, 15, 2, "四季", "文化爱好者",
     "明清皇帝祭天祈谷场所，祈年殿建筑奇观"),
    ("上海外滩", "上海", "都市观光", 4.8, 0, 2, "四季", "情侣/摄影",
     "万国建筑博览群与陆家嘴天际线隔江相望"),
    ("上海迪士尼乐园", "上海", "主题乐园", 4.7, 475, 8, "四季", "亲子/情侣",
     "中国内地首座迪士尼主题乐园"),
    ("东方明珠", "上海", "都市观光", 4.6, 160, 2, "四季", "全家",
     "上海地标建筑，高空俯瞰浦江两岸"),
    ("豫园", "上海", "园林风光", 4.5, 40, 2, "春秋", "文化爱好者",
     "明代私家园林，江南古典园林代表"),
    ("杭州西湖", "杭州", "自然风光", 4.8, 0, 5, "春夏", "情侣/全家",
     "'欲把西湖比西子'，世界文化遗产，免费开放"),
    ("灵隐寺", "杭州", "历史人文", 4.6, 75, 3, "四季", "文化爱好者",
     "江南著名古刹，飞来峰石窟造像"),
    ("千岛湖", "杭州", "自然风光", 4.6, 130, 6, "夏秋", "全家/摄影",
     "1078座岛屿星罗棋布，天下第一秀水"),
    ("乌镇", "嘉兴", "古镇水乡", 4.7, 150, 6, "春秋", "情侣/摄影",
     "典型江南水乡古镇，戏剧节举办地"),
    ("西塘古镇", "嘉兴", "古镇水乡", 4.5, 95, 5, "春秋", "情侣/摄影",
     "生活着的千年古镇，烟雨长廊"),
    ("苏州拙政园", "苏州", "园林风光", 4.8, 80, 2, "春秋", "文化爱好者",
     "中国四大名园之首，江南园林典范"),
    ("周庄", "苏州", "古镇水乡", 4.6, 100, 5, "春秋", "情侣/摄影",
     "'中国第一水乡'，双桥闻名于世"),
    ("黄山", "黄山", "自然风光", 4.9, 190, 10, "春秋", "徒步/摄影",
     "'五岳归来不看山，黄山归来不看岳'，奇松怪石云海"),
    ("九寨沟", "阿坝", "自然风光", 4.8, 280, 8, "秋季", "摄影/全家",
     "世界自然遗产，彩色海子与瀑布群"),
    ("成都大熊猫繁育研究基地", "成都", "主题乐园", 4.7, 55, 3, "四季", "亲子",
     "近距离观看大熊猫的最佳地点"),
    ("宽窄巷子", "成都", "都市观光", 4.5, 0, 2, "四季", "美食/情侣",
     "清代古街区，体验老成都慢生活"),
    ("都江堰", "成都", "历史人文", 4.7, 80, 3, "四季", "文化爱好者",
     "两千年仍在使用的古代水利工程奇迹"),
    ("张家界国家森林公园", "张家界", "自然风光", 4.8, 228, 12, "春秋", "徒步/摄影",
     "阿凡达悬浮山取景地，石英砂岩峰林奇观"),
    ("凤凰古城", "湘西", "古镇水乡", 4.5, 0, 6, "春秋", "情侣/摄影",
     "沱江边的苗族风情古城，沈从文故里"),
    ("兵马俑", "西安", "历史人文", 4.9, 120, 3, "四季", "全家/文化爱好者",
     "世界第八大奇迹，秦始皇地下军阵"),
    ("大雁塔", "西安", "历史人文", 4.5, 30, 2, "四季", "文化爱好者",
     "玄奘译经之地，唐代佛教建筑标志"),
    ("大唐不夜城", "西安", "都市观光", 4.7, 0, 3, "四季", "情侣/美食",
     "盛唐主题步行街，夜间灯光秀"),
    ("鼓浪屿", "厦门", "自然风光", 4.6, 35, 6, "春秋", "情侣/摄影",
     "海上花园，万国建筑与钢琴之岛"),
    ("厦门大学", "厦门", "都市观光", 4.6, 0, 2, "四季", "情侣/摄影",
     "中国最美校园之一，芙蓉隧道涂鸦"),
    ("三亚亚龙湾", "三亚", "海滨度假", 4.7, 0, 8, "冬季", "情侣/亲子",
     "'天下第一湾'，热带海滨度假胜地"),
    ("蜈支洲岛", "三亚", "海滨度假", 4.6, 144, 8, "冬季", "情侣/潜水",
     "中国马尔代夫，水上项目丰富"),
    ("桂林漓江", "桂林", "自然风光", 4.8, 215, 5, "夏秋", "全家/摄影",
     "'桂林山水甲天下'，竹筏漂流漓江"),
    ("阳朔西街", "桂林", "古镇水乡", 4.4, 0, 3, "春秋", "情侣/美食",
     "洋人街，喀斯特峰林中的风情小镇"),
    ("丽江古城", "丽江", "古镇水乡", 4.6, 50, 6, "春秋", "情侣/摄影",
     "纳西族古城，雪山脚下的慢生活"),
    ("玉龙雪山", "丽江", "自然风光", 4.6, 130, 8, "秋冬", "徒步/摄影",
     "北半球最南的雪山，纳西族神山"),
    ("大理古城", "大理", "古镇水乡", 4.6, 0, 5, "春秋", "情侣/摄影",
     "苍山洱海间的南诏古都"),
    ("洱海", "大理", "自然风光", 4.7, 0, 5, "春秋", "情侣/摄影",
     "环湖骑行，风花雪月的高原湖泊"),
    ("布达拉宫", "拉萨", "历史人文", 4.9, 200, 3, "夏秋", "文化爱好者",
     "世界海拔最高的宫殿，藏族艺术宝库"),
    ("纳木错", "拉萨", "自然风光", 4.7, 120, 8, "夏季", "摄影/徒步",
     "天湖，西藏三大圣湖之一"),
    ("青海湖", "海南州", "自然风光", 4.7, 100, 8, "夏季", "全家/摄影",
     "中国最大内陆湖，七月油菜花海"),
    ("茶卡盐湖", "海西州", "自然风光", 4.5, 60, 4, "夏秋", "摄影/情侣",
     "天空之镜，倒映整个世界"),
    ("泰山", "泰安", "自然风光", 4.8, 115, 8, "春秋", "徒步/文化爱好者",
     "五岳之首，登泰山而小天下"),
    ("曲阜三孔", "济宁", "历史人文", 4.6, 140, 4, "四季", "文化爱好者",
     "孔庙孔府孔林，儒家文化圣地"),
    ("哈尔滨冰雪大世界", "哈尔滨", "主题乐园", 4.7, 328, 4, "冬季", "亲子/情侣",
     "世界最大冰雪主题乐园"),
    ("中央大街", "哈尔滨", "都市观光", 4.6, 0, 2, "冬夏", "情侣/美食",
     "百年欧式建筑步行街"),
    ("长隆野生动物世界", "广州", "主题乐园", 4.8, 350, 8, "四季", "亲子",
     "亚洲最大野生动物主题公园"),
    ("广州塔(小蛮腰)", "广州", "都市观光", 4.6, 150, 2, "四季", "情侣/摄影",
     "广州地标，云端观景与摩天轮"),
    ("黄鹤楼", "武汉", "历史人文", 4.6, 70, 2, "春秋", "文化爱好者",
     "江南三大名楼之一，'昔人已乘黄鹤去'"),
    ("武汉大学", "武汉", "都市观光", 4.7, 0, 2, "春季", "摄影/情侣",
     "三月樱花大道，中国最美大学之一"),
    ("故宫角楼咖啡区域/什刹海", "北京", "都市观光", 4.4, 0, 2, "夏秋", "情侣/美食",
     "老北京胡同与后海酒吧街"),
    ("莫高窟", "敦煌", "历史人文", 4.9, 238, 4, "秋季", "文化爱好者",
     "千年佛教艺术石窟，壁画彩塑殿堂"),
    ("鸣沙山月牙泉", "敦煌", "自然风光", 4.7, 110, 4, "夏秋", "摄影/情侣",
     "大漠孤烟中的沙漠与千年不涸清泉"),
]

COLUMNS = [
    ("name", "景点名称", 200),
    ("city", "城市", 80),
    ("category", "类型", 90),
    ("rating", "评分", 60),
    ("price", "门票(元)", 80),
    ("duration", "时长(h)", 70),
    ("season", "适合季节", 90),
    ("crowd", "适合人群", 130),
    ("desc", "简介", 360),
]

CATEGORIES = ["全部", "历史人文", "自然风光", "园林风光", "古镇水乡",
              "海滨度假", "都市观光", "主题乐园"]
SEASONS = ["全部", "春季", "夏季", "秋季", "冬季", "春秋", "夏秋",
           "春夏", "秋冬", "冬夏", "四季"]
CROWDS = ["全部", "亲子", "情侣", "全家", "徒步", "摄影", "文化爱好者", "美食"]


class TravelFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("旅游景点筛选程序")
        self.root.geometry("1180x680")
        self.sort_col = "rating"
        self.sort_reverse = True

        self._build_filter_bar()
        self._build_table()
        self._build_status_bar()
        self.apply_filters()

    # ---------- 筛选条件区 ----------
    def _build_filter_bar(self):
        bar = ttk.LabelFrame(self.root, text="筛选条件", padding=10)
        bar.pack(fill="x", padx=10, pady=(10, 5))

        # 第一行：城市/类型/季节/人群
        row1 = ttk.Frame(bar)
        row1.pack(fill="x", pady=3)

        ttk.Label(row1, text="城市:").pack(side="left")
        self.city_var = tk.StringVar(value="全部")
        cities = ["全部"] + sorted(set(s[1] for s in SPOTS))
        ttk.Combobox(row1, textvariable=self.city_var, values=cities,
                     width=10, state="readonly").pack(side="left", padx=(4, 16))

        ttk.Label(row1, text="类型:").pack(side="left")
        self.cat_var = tk.StringVar(value="全部")
        ttk.Combobox(row1, textvariable=self.cat_var, values=CATEGORIES,
                     width=10, state="readonly").pack(side="left", padx=(4, 16))

        ttk.Label(row1, text="季节:").pack(side="left")
        self.season_var = tk.StringVar(value="全部")
        ttk.Combobox(row1, textvariable=self.season_var, values=SEASONS,
                     width=8, state="readonly").pack(side="left", padx=(4, 16))

        ttk.Label(row1, text="人群:").pack(side="left")
        self.crowd_var = tk.StringVar(value="全部")
        ttk.Combobox(row1, textvariable=self.crowd_var, values=CROWDS,
                     width=12, state="readonly").pack(side="left", padx=(4, 16))

        # 第二行：评分/价格/关键词/按钮
        row2 = ttk.Frame(bar)
        row2.pack(fill="x", pady=3)

        ttk.Label(row2, text="最低评分:").pack(side="left")
        self.rating_var = tk.StringVar(value="0")
        ttk.Combobox(row2, textvariable=self.rating_var, width=5,
                     values=["0", "4.0", "4.5", "4.7", "4.8", "4.9"],
                     state="readonly").pack(side="left", padx=(4, 16))

        ttk.Label(row2, text="最高票价:").pack(side="left")
        self.price_var = tk.StringVar(value="不限")
        ttk.Combobox(row2, textvariable=self.price_var, width=7,
                     values=["不限", "50", "100", "150", "200", "300"],
                     state="readonly").pack(side="left", padx=(4, 16))

        ttk.Label(row2, text="关键词:").pack(side="left")
        self.keyword_var = tk.StringVar()
        ent = ttk.Entry(row2, textvariable=self.keyword_var, width=18)
        ent.pack(side="left", padx=(4, 16))
        ent.bind("<Return>", lambda e: self.apply_filters())

        ttk.Button(row2, text="🔍 筛选", command=self.apply_filters).pack(
            side="left", padx=4)
        ttk.Button(row2, text="↺ 重置", command=self.reset_filters).pack(
            side="left", padx=4)
        ttk.Button(row2, text="💾 导出CSV", command=self.export_csv).pack(
            side="left", padx=4)

        # 下拉变化时自动刷新
        for v in (self.city_var, self.cat_var, self.season_var,
                  self.crowd_var, self.rating_var, self.price_var):
            v.trace_add("write", lambda *_: self.apply_filters())

    # ---------- 结果表格 ----------
    def _build_table(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(
            frame, columns=[c[0] for c in COLUMNS], show="headings")
        for key, text, width in COLUMNS:
            self.tree.heading(key, text=text,
                              command=lambda k=key: self.sort_by(k))
            anchor = "center" if key in ("city", "category", "rating",
                                         "price", "duration", "season") else "w"
            self.tree.column(key, width=width, anchor=anchor)

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        # 隔行变色 + 高分标记
        self.tree.tag_configure("top", background="#FFF3CD")
        self.tree.tag_configure("free", background="#D4EDDA")

    # ---------- 状态栏 ----------
    def _build_status_bar(self):
        self.status_var = tk.StringVar()
        ttk.Label(self.root, textvariable=self.status_var, relief="sunken",
                  anchor="w", padding=5).pack(fill="x", side="bottom")

    # ---------- 核心筛选逻辑 ----------
    def _match(self, spot):
        _, city, cat, rating, price, _, season, crowd, desc = spot
        if self.city_var.get() != "全部" and city != self.city_var.get():
            return False
        if self.cat_var.get() != "全部" and cat != self.cat_var.get():
            return False
        if rating < float(self.rating_var.get()):
            return False
        price_limit = self.price_var.get()
        if price_limit != "不限" and price > int(price_limit):
            return False
        if self.season_var.get() != "全部":
            s = self.season_var.get()
            # 季节兼容：选"秋季"时"春秋/夏秋/四季"也匹配
            if s not in season and season != "四季":
                return False
        if self.crowd_var.get() != "全部":
            if self.crowd_var.get() not in crowd:
                return False
        kw = self.keyword_var.get().strip()
        if kw and kw not in f"{spot[0]}{spot[1]}{desc}":
            return False
        return True

    def apply_filters(self):
        rows = [s for s in SPOTS if self._match(s)]
        rows.sort(key=lambda s: s[self._sort_index()],
                  reverse=self.sort_reverse)
        self.current_rows = rows

        for item in self.tree.get_children():
            self.tree.delete(item)
        for s in rows:
            name, city, cat, rating, price, dur, season, crowd, desc = s
            tags = ()
            if rating >= 4.8:
                tags = ("top",)
            elif price == 0:
                tags = ("free",)
            self.tree.insert("", "end", values=(
                name, city, cat, f"{rating:.1f}",
                "免费" if price == 0 else price,
                dur, season, crowd, desc), tags=tags)

        free_n = sum(1 for s in rows if s[4] == 0)
        avg = sum(s[3] for s in rows) / len(rows) if rows else 0
        self.status_var.set(
            f"共找到 {len(rows)} 个景点  |  免费 {free_n} 个  |  "
            f"平均评分 {avg:.2f}  |  黄色底=评分4.8+，绿色底=免费景点")

    def _sort_index(self):
        keys = [c[0] for c in COLUMNS]
        return keys.index(self.sort_col)

    def sort_by(self, key):
        if self.sort_col == key:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_col = key
            self.sort_reverse = True
        self.apply_filters()

    def reset_filters(self):
        self.city_var.set("全部")
        self.cat_var.set("全部")
        self.season_var.set("全部")
        self.crowd_var.set("全部")
        self.rating_var.set("0")
        self.price_var.set("不限")
        self.keyword_var.set("")
        self.apply_filters()  # 关键词框未绑定自动刷新，重置后需手动刷新一次

    # ---------- 导出 CSV ----------
    def export_csv(self):
        if not getattr(self, "current_rows", None):
            messagebox.showwarning("提示", "当前没有可导出的筛选结果")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialdir=r"e:\\",
            initialfile="旅游景点筛选结果.csv",
            filetypes=[("CSV 文件", "*.csv")])
        if not path:
            return
        # 加 utf-8-sig，Excel 直接打开不乱码
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow([c[1] for c in COLUMNS])
            for s in self.current_rows:
                name, city, cat, rating, price, dur, season, crowd, desc = s
                w.writerow([name, city, cat, rating,
                            "免费" if price == 0 else price,
                            dur, season, crowd, desc])
        messagebox.showinfo("导出成功", f"已导出 {len(self.current_rows)} 条到：\n{path}")


def main():
    root = tk.Tk()
    try:
        ttk.Style().theme_use("clam")
    except tk.TclError:
        pass
    TravelFilterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
