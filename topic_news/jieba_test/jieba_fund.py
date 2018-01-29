#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import HTMLParser
from jieba import analyse
from textrank4zh import TextRank4Keyword,TextRank4Sentence

reload(sys)
sys.setdefaultencoding("utf-8")

def jieba_tags():
    sentences=u'特朗普访华'
    tags=analyse.extract_tags(sentence=sentences,topK=2)
    print ','.join(tags)

def textrank_summary():
    html_parser=HTMLParser.HTMLParser()
    text='''&lt;?xml version='1.0' encoding='utf-8'?&gt;&lt;div&gt;&lt;p&gt;周三亚市早盘，美国相关资产盘中异动。稍早美国媒体报道称， 特朗普要求时任FBI局长科米结束调查弗林事件。他在上周突然解除了科米的职务。&lt;/p&gt;&lt;p&gt;亚市早盘，标普500股指期货一度下跌0.7%。美国10年国债收益率跌3个基点，报2.30%。COMEX黄金涨近10美元。ICE美元指数延续跌势，一度跌破98，报97.94，再创去年11月9日（美国大选次日）以来新低，迄今已连跌五日。&lt;/p&gt;&lt;p&gt;昨日纽约时报报道称，已被解职的联邦调查局（FBI）局长科米(James Comey)2月会见特朗普后不久在备忘录中称，总统要求他结束对前国家安全顾问迈克尔&middot;弗林(Michael Flynn)的调查。&lt;/p&gt;&lt;p&gt;不过，白宫对纽约时报的报道予以否认，称&ldquo;特朗普从未要求科米或任何人结束任何调查，包括关于弗林的调查。报道中提及的备忘录的内容并非事实，其对于总统和科密之间谈话内容的描述并不准确。&rdquo;&lt;/p&gt;&lt;p&gt;同时，《华盛顿邮报》报道称，特朗普上周在椭圆形办公室会见俄罗斯外长拉夫罗夫及俄罗斯驻美大使，可能向他们泄露了有关恐怖组织伊斯兰国（IS）的绝密情报。&lt;/p&gt;&lt;p&gt;此事凸显出白宫面临的新政治风险：总统可能妨碍司法公正。一旦这被判定为事实，极有可能导致特朗普被弹劾。&lt;/p&gt;&lt;p&gt;随着特朗普向俄罗斯&ldquo;泄密门&rdquo;事件逐渐发酵，投资者越来越担心特朗普可能无法完成任期。分析师称，即使特朗普能够完成任期，也会有很多来自政治方面的事件分散其推进经济刺激计划的注意力。&lt;/p&gt;&lt;h2&gt;特朗普被弹劾概率攀升？&lt;/h2&gt;&lt;p&gt;如果要弹劾总统，众议院必须有多数议员的支持。民主党目前并没有人表态支持弹劾总统，或者建议开启弹劾程序。&lt;/p&gt;&lt;p&gt;然而，人们已经开始为&ldquo;特朗普通俄门&rdquo;事件可能的糟糕结果做准备了。根据PredictIt网站，特朗普今年被弹劾的概率已翻了一倍，从19%飙升至29%。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df6db35c283.jpeg&quot;&gt;&lt;p&gt;金融市场也开始对相关风险开始计价。美元/日元大跌40个点：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/2079000a8f8215a482a8.jpeg&quot;&gt;&lt;p&gt;标普500股指期货亚市早盘明显下挫：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd655b194d28.jpeg&quot;&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207b0003a87d33d268c6.jpeg&quot;&gt;&lt;p&gt;国际金价大涨：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd6661e97441.jpeg&quot;&gt;&lt;h2&gt;&ldquo;特朗普通俄门&rdquo;发酵&lt;/h2&gt;&lt;p&gt;纽约时报报道称，科米在备忘录中写道，特朗普在2月的会面中对他说：&ldquo;我希望你可以让这件事过去&rdquo;。而科密并未直接回应特朗普的要求。&lt;/p&gt;&lt;p&gt;5月9日，特朗普在毫无先兆的情况下解雇了科米。当时此事令全球愕然，连科米本人都显得措手不及。甚至有美国媒体和官员将此事与当年尼克松试图阻挠国会调查&ldquo;水门事件&rdquo;联系起来。&lt;/p&gt;&lt;p&gt;英国《卫报》当时评论称，特朗普解雇科米，不仅让人质疑FBI在调查特朗普竞选期间与俄罗斯联系案件的独立性。特朗普称解雇科米是因为他对希拉里&ldquo;邮件门&rdquo;的调查，但民主党却认为，特朗普此举是在阻挠FBI对其&ldquo;通俄门&rdquo;进行调查。&lt;/p&gt;&lt;p&gt;此前，包括前总统国家安全顾问弗林、司法部长等多名高官在内的特朗普政府官员都卷入了特朗普团队在去年竞选期间与俄罗斯相联系的&ldquo;通俄门&rdquo;。&lt;/p&gt;&lt;p&gt;今年2月14日，也就是特朗普就任总统还不到一个月的时间，白宫国家安全顾问迈克尔&middot;弗林因被指在与俄国驻美国大使馆通话事件上误导政府而提出辞职。&lt;/p&gt;&lt;p&gt;弗林被指在去年12月（也就是特朗普宣誓就职前）与俄国驻美国大使馆Sergey I. Kislyak就美对俄制裁问题通话，这一行为违反了美国法律。当时他尚未被任命为国家安全顾问。&lt;/p&gt;&lt;p&gt;CNN 5月9日报道称，陪审团已开始考虑传唤弗林。若果真如此，则意味着对特朗普竞选团队的&ldquo;通俄门&rdquo;调查将进入一个新阶段。&lt;/p&gt;&lt;p&gt;就在特朗普炒了科米鱿鱼之后不久，《华盛顿邮报》报道了有关&ldquo;特朗普通俄门&rdquo;的另一个消息：特朗普上周在椭圆形办公室会议上向俄罗斯外长及俄罗斯驻美大使泄露了有关伊斯兰国（IS）意图的高度机密信息。&lt;/p&gt;&lt;p&gt;《华盛顿邮报》引述一名未公开身分的美国官员报道称，特朗普上周三在白宫与俄罗斯外长拉夫罗夫会晤时，曾向来宾炫耀他每天都可以得到关于伊斯兰国组织的恐怖威胁的绝对可靠信息，他并详细描述了一个该组织与在飞机上使用手提电脑有关的恐怖行动方案。&lt;/p&gt;&lt;p&gt;这名美国官员向《华邮》表示，特朗普向俄罗斯客人透露的信息比美国向自己的盟友透露的还要多，都属于美国各情报部门列为绝密级别最高的信息。&lt;/p&gt;&lt;p&gt;不过，《华盛顿邮报》的报道并没有说特朗普泄露了情报来源或方式，也没有说特朗普泄露任何军事行动。报道称，该情报是从一个与美国开展情报合作的国家得来的。&lt;/p&gt;&lt;p&gt;值得注意的是这件事发生的时机：几天之后，特朗普就将开启他作为美国总统的首次外访，目的地包括沙特阿拉伯和以色列&mdash;&mdash;这是美国在打击IS组织前线上两个至关重要的盟友。&lt;/p&gt;&lt;h2&gt;总统的反击&lt;/h2&gt;&lt;p&gt;针对《华盛顿邮报》的上述报道内容，特朗普周二连续发布twitter称，在关于与俄罗斯官员分享有关恐怖分子的信息这个问题上，他拥有&ldquo;绝对权力&rdquo;：&lt;/p&gt;&lt;blockquote&gt;&lt;p&gt;作为总统，我希望与俄罗斯(在一次会议计划公开披露的白宫会晤中)分享与恐怖主义以及飞行安全有关的信息，我有绝对的权力这么做。&lt;/p&gt;&lt;p&gt;出于人道主义原因，而且我希望俄罗斯大幅加强他们打击伊斯兰国组织以及恐怖主义的行动。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df5a142e55d.jpeg&quot;&gt;&lt;/blockquote&gt;&lt;p&gt;国家安全委员会发言人Michael Anton称，总统的推文与白宫高级官员驳斥该报道的表态并不矛盾。&lt;/p&gt;&lt;p&gt;白宫国家安全顾问H.R. McMaster表示，&ldquo;这篇报道内容失实，交谈自始至终都没有涉及情报来源或方式，总统也未透露任何尚未公开的军事行动。&rdquo;&lt;/p&gt;&lt;p&gt;而关于有报道称特朗普上周在椭圆形办公室会议中泄露高度机密信息，民主党和共和党都有议员对此表达了关切，他们同时要求此事应有更为详尽的解释。&lt;/p&gt;&lt;/div&gt;'''
#     text='''&lt;?xml version='1.0' encoding='utf-8'?&gt;
# &lt;div&gt;
#
#                         &lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142769.jpg&quot;&gt;&lt;/p&gt;
# &lt;p&gt;8月3日，巴基斯坦总理阿巴西在伊斯兰堡检阅仪仗队。来源：视觉中国&lt;/p&gt;
# &lt;p&gt;当地时间周四下午，巴基斯坦总理阿巴西与军方将领们召开会议，商讨应对美国阿富汗新战略的方案。&lt;/p&gt;
# &lt;p&gt;三天前，美国总统特朗普宣布改变在阿富汗战争上的立场，将加大军事存在，同时也以空前严厉的语气指责反恐盟友巴基斯坦。他说，&ldquo;不会再纵容巴基斯坦成为恐怖组织的天堂&rdquo;，同时还意外邀请巴基斯坦的&ldquo;死敌&rdquo;印度更多地参与阿富汗的反恐行动。&lt;/p&gt;
# &lt;p&gt;特朗普表态过后，白宫官员们更是添油加醋，进一步威胁要缩减对巴援助和军事预算。&lt;/p&gt;
# &lt;p&gt;目前，总理阿巴西本人尚未对此公开回应，但外交部长阿西夫称，华盛顿方面不应该把阿富汗战争的失败归责于巴基斯坦。巴基斯坦也否认自己是武装分子的避风港。&lt;/p&gt;
# &lt;p&gt;阿西夫也出席了周四全国安全委员会的会议，此前一天他还会见了美国驻巴基斯坦大使大卫&middot;黑尔，并表示相对于美国的援助金，巴基斯坦更需要信任和理解。&lt;/p&gt;
# &lt;p&gt;据路透社报道，巴官员们对华盛顿方面的表态感到愤怒，称其无视该国在反武装斗争和抗击基地组织、ISIS以及巴基斯坦塔利班方面所取得的成绩。&lt;/p&gt;
# &lt;p&gt;据巴方估计，自2001年美国发动反恐战争以来，巴基斯坦为此牺牲了7万人。&lt;/p&gt;
# &lt;p&gt;&ldquo;我们认为特朗普政府的立场完全是片面的，对巴基斯坦不公平，未能承认和尊重巴方在反恐战发挥的重要作用。&rdquo;巴参议院国防委员会主席沙耶德周四对路透社说。&lt;/p&gt;
# &lt;p&gt;不仅如此，巴基斯坦官员还对印度受邀重建阿富汗感到愤怒，并警告印度在喀布尔的作用越大，给地区和平带来的威胁就越大。自1947年独立之后，巴基斯坦已与印度打了三场战争。&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142233.jpg&quot;&gt;&lt;/p&gt;
# &lt;p&gt;中国国务委员杨洁篪23日呼吁美国重视巴基斯坦在阿富汗问题上的重要作用，尊重巴基斯坦的主权和合理安全关切。中国西部领土与巴基斯坦和阿富汗接壤。&lt;/p&gt;
# &lt;p&gt;巴参议院国防委员会主席沙耶德对此补充说，&ldquo;9&middot;11事件以来，地区形势对比已大为改变。今天的美国在本地区的影响力已大幅减弱，而巴基斯坦在外交政策上的战略和选择空间也更大了。&rdquo;&lt;/p&gt;
# &lt;p&gt;上世纪冷战期间，巴美关系密切。9&middot;11事件后，巴基斯坦参加国际反恐战争，参与打击塔利班和&ldquo;基地&rdquo;组织，积极参与阿富汗重建。&lt;/p&gt;
# &lt;p&gt;美国奥巴马政府上台后出台对阿富汗、巴基斯坦新战略，加大对巴基斯坦军事和经济投入，但两国间互信不足。2011年，受本&middot;拉登在巴基斯坦境内被击毙、美北约越境空袭巴基斯坦边境哨所事件等影响，巴关闭境内北约后勤补给线，一度中断同美高层互访，两国关系降至低点。&lt;/p&gt;
# &lt;p&gt;2012年以来，两国高层逐渐恢复接触，关系逐步得到改善，并于2014年3月重启巴美战略对话。&lt;/p&gt;
# &lt;p&gt;2016年1月，阿巴中美四方协调组首次会议召开，致力于推进&ldquo;阿人主导，阿人所有&rdquo;的和解进程。&lt;/p&gt;
# 					&lt;/div&gt;'''
    text=html_parser.unescape(text)
    print text
    tr4s=TextRank4Sentence()
    tr4s.analyze(text=text)
    s_list=tr4s.get_key_sentences(num=3)
    for i in s_list:
        print i.sentence,i.weight


def textrank_keywords():
    html_parser = HTMLParser.HTMLParser()
    text = '''&lt;?xml version='1.0' encoding='utf-8'?&gt;&lt;div&gt;&lt;p&gt;周三亚市早盘，美国相关资产盘中异动。稍早美国媒体报道称， 特朗普要求时任FBI局长科米结束调查弗林事件。他在上周突然解除了科米的职务。&lt;/p&gt;&lt;p&gt;亚市早盘，标普500股指期货一度下跌0.7%。美国10年国债收益率跌3个基点，报2.30%。COMEX黄金涨近10美元。ICE美元指数延续跌势，一度跌破98，报97.94，再创去年11月9日（美国大选次日）以来新低，迄今已连跌五日。&lt;/p&gt;&lt;p&gt;昨日纽约时报报道称，已被解职的联邦调查局（FBI）局长科米(James Comey)2月会见特朗普后不久在备忘录中称，总统要求他结束对前国家安全顾问迈克尔&middot;弗林(Michael Flynn)的调查。&lt;/p&gt;&lt;p&gt;不过，白宫对纽约时报的报道予以否认，称&ldquo;特朗普从未要求科米或任何人结束任何调查，包括关于弗林的调查。报道中提及的备忘录的内容并非事实，其对于总统和科密之间谈话内容的描述并不准确。&rdquo;&lt;/p&gt;&lt;p&gt;同时，《华盛顿邮报》报道称，特朗普上周在椭圆形办公室会见俄罗斯外长拉夫罗夫及俄罗斯驻美大使，可能向他们泄露了有关恐怖组织伊斯兰国（IS）的绝密情报。&lt;/p&gt;&lt;p&gt;此事凸显出白宫面临的新政治风险：总统可能妨碍司法公正。一旦这被判定为事实，极有可能导致特朗普被弹劾。&lt;/p&gt;&lt;p&gt;随着特朗普向俄罗斯&ldquo;泄密门&rdquo;事件逐渐发酵，投资者越来越担心特朗普可能无法完成任期。分析师称，即使特朗普能够完成任期，也会有很多来自政治方面的事件分散其推进经济刺激计划的注意力。&lt;/p&gt;&lt;h2&gt;特朗普被弹劾概率攀升？&lt;/h2&gt;&lt;p&gt;如果要弹劾总统，众议院必须有多数议员的支持。民主党目前并没有人表态支持弹劾总统，或者建议开启弹劾程序。&lt;/p&gt;&lt;p&gt;然而，人们已经开始为&ldquo;特朗普通俄门&rdquo;事件可能的糟糕结果做准备了。根据PredictIt网站，特朗普今年被弹劾的概率已翻了一倍，从19%飙升至29%。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df6db35c283.jpeg&quot;&gt;&lt;p&gt;金融市场也开始对相关风险开始计价。美元/日元大跌40个点：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/2079000a8f8215a482a8.jpeg&quot;&gt;&lt;p&gt;标普500股指期货亚市早盘明显下挫：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd655b194d28.jpeg&quot;&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207b0003a87d33d268c6.jpeg&quot;&gt;&lt;p&gt;国际金价大涨：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd6661e97441.jpeg&quot;&gt;&lt;h2&gt;&ldquo;特朗普通俄门&rdquo;发酵&lt;/h2&gt;&lt;p&gt;纽约时报报道称，科米在备忘录中写道，特朗普在2月的会面中对他说：&ldquo;我希望你可以让这件事过去&rdquo;。而科密并未直接回应特朗普的要求。&lt;/p&gt;&lt;p&gt;5月9日，特朗普在毫无先兆的情况下解雇了科米。当时此事令全球愕然，连科米本人都显得措手不及。甚至有美国媒体和官员将此事与当年尼克松试图阻挠国会调查&ldquo;水门事件&rdquo;联系起来。&lt;/p&gt;&lt;p&gt;英国《卫报》当时评论称，特朗普解雇科米，不仅让人质疑FBI在调查特朗普竞选期间与俄罗斯联系案件的独立性。特朗普称解雇科米是因为他对希拉里&ldquo;邮件门&rdquo;的调查，但民主党却认为，特朗普此举是在阻挠FBI对其&ldquo;通俄门&rdquo;进行调查。&lt;/p&gt;&lt;p&gt;此前，包括前总统国家安全顾问弗林、司法部长等多名高官在内的特朗普政府官员都卷入了特朗普团队在去年竞选期间与俄罗斯相联系的&ldquo;通俄门&rdquo;。&lt;/p&gt;&lt;p&gt;今年2月14日，也就是特朗普就任总统还不到一个月的时间，白宫国家安全顾问迈克尔&middot;弗林因被指在与俄国驻美国大使馆通话事件上误导政府而提出辞职。&lt;/p&gt;&lt;p&gt;弗林被指在去年12月（也就是特朗普宣誓就职前）与俄国驻美国大使馆Sergey I. Kislyak就美对俄制裁问题通话，这一行为违反了美国法律。当时他尚未被任命为国家安全顾问。&lt;/p&gt;&lt;p&gt;CNN 5月9日报道称，陪审团已开始考虑传唤弗林。若果真如此，则意味着对特朗普竞选团队的&ldquo;通俄门&rdquo;调查将进入一个新阶段。&lt;/p&gt;&lt;p&gt;就在特朗普炒了科米鱿鱼之后不久，《华盛顿邮报》报道了有关&ldquo;特朗普通俄门&rdquo;的另一个消息：特朗普上周在椭圆形办公室会议上向俄罗斯外长及俄罗斯驻美大使泄露了有关伊斯兰国（IS）意图的高度机密信息。&lt;/p&gt;&lt;p&gt;《华盛顿邮报》引述一名未公开身分的美国官员报道称，特朗普上周三在白宫与俄罗斯外长拉夫罗夫会晤时，曾向来宾炫耀他每天都可以得到关于伊斯兰国组织的恐怖威胁的绝对可靠信息，他并详细描述了一个该组织与在飞机上使用手提电脑有关的恐怖行动方案。&lt;/p&gt;&lt;p&gt;这名美国官员向《华邮》表示，特朗普向俄罗斯客人透露的信息比美国向自己的盟友透露的还要多，都属于美国各情报部门列为绝密级别最高的信息。&lt;/p&gt;&lt;p&gt;不过，《华盛顿邮报》的报道并没有说特朗普泄露了情报来源或方式，也没有说特朗普泄露任何军事行动。报道称，该情报是从一个与美国开展情报合作的国家得来的。&lt;/p&gt;&lt;p&gt;值得注意的是这件事发生的时机：几天之后，特朗普就将开启他作为美国总统的首次外访，目的地包括沙特阿拉伯和以色列&mdash;&mdash;这是美国在打击IS组织前线上两个至关重要的盟友。&lt;/p&gt;&lt;h2&gt;总统的反击&lt;/h2&gt;&lt;p&gt;针对《华盛顿邮报》的上述报道内容，特朗普周二连续发布twitter称，在关于与俄罗斯官员分享有关恐怖分子的信息这个问题上，他拥有&ldquo;绝对权力&rdquo;：&lt;/p&gt;&lt;blockquote&gt;&lt;p&gt;作为总统，我希望与俄罗斯(在一次会议计划公开披露的白宫会晤中)分享与恐怖主义以及飞行安全有关的信息，我有绝对的权力这么做。&lt;/p&gt;&lt;p&gt;出于人道主义原因，而且我希望俄罗斯大幅加强他们打击伊斯兰国组织以及恐怖主义的行动。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df5a142e55d.jpeg&quot;&gt;&lt;/blockquote&gt;&lt;p&gt;国家安全委员会发言人Michael Anton称，总统的推文与白宫高级官员驳斥该报道的表态并不矛盾。&lt;/p&gt;&lt;p&gt;白宫国家安全顾问H.R. McMaster表示，&ldquo;这篇报道内容失实，交谈自始至终都没有涉及情报来源或方式，总统也未透露任何尚未公开的军事行动。&rdquo;&lt;/p&gt;&lt;p&gt;而关于有报道称特朗普上周在椭圆形办公室会议中泄露高度机密信息，民主党和共和党都有议员对此表达了关切，他们同时要求此事应有更为详尽的解释。&lt;/p&gt;&lt;/div&gt;'''
    #     text='''&lt;?xml version='1.0' encoding='utf-8'?&gt;
    # &lt;div&gt;
    #
    #                         &lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142769.jpg&quot;&gt;&lt;/p&gt;
    # &lt;p&gt;8月3日，巴基斯坦总理阿巴西在伊斯兰堡检阅仪仗队。来源：视觉中国&lt;/p&gt;
    # &lt;p&gt;当地时间周四下午，巴基斯坦总理阿巴西与军方将领们召开会议，商讨应对美国阿富汗新战略的方案。&lt;/p&gt;
    # &lt;p&gt;三天前，美国总统特朗普宣布改变在阿富汗战争上的立场，将加大军事存在，同时也以空前严厉的语气指责反恐盟友巴基斯坦。他说，&ldquo;不会再纵容巴基斯坦成为恐怖组织的天堂&rdquo;，同时还意外邀请巴基斯坦的&ldquo;死敌&rdquo;印度更多地参与阿富汗的反恐行动。&lt;/p&gt;
    # &lt;p&gt;特朗普表态过后，白宫官员们更是添油加醋，进一步威胁要缩减对巴援助和军事预算。&lt;/p&gt;
    # &lt;p&gt;目前，总理阿巴西本人尚未对此公开回应，但外交部长阿西夫称，华盛顿方面不应该把阿富汗战争的失败归责于巴基斯坦。巴基斯坦也否认自己是武装分子的避风港。&lt;/p&gt;
    # &lt;p&gt;阿西夫也出席了周四全国安全委员会的会议，此前一天他还会见了美国驻巴基斯坦大使大卫&middot;黑尔，并表示相对于美国的援助金，巴基斯坦更需要信任和理解。&lt;/p&gt;
    # &lt;p&gt;据路透社报道，巴官员们对华盛顿方面的表态感到愤怒，称其无视该国在反武装斗争和抗击基地组织、ISIS以及巴基斯坦塔利班方面所取得的成绩。&lt;/p&gt;
    # &lt;p&gt;据巴方估计，自2001年美国发动反恐战争以来，巴基斯坦为此牺牲了7万人。&lt;/p&gt;
    # &lt;p&gt;&ldquo;我们认为特朗普政府的立场完全是片面的，对巴基斯坦不公平，未能承认和尊重巴方在反恐战发挥的重要作用。&rdquo;巴参议院国防委员会主席沙耶德周四对路透社说。&lt;/p&gt;
    # &lt;p&gt;不仅如此，巴基斯坦官员还对印度受邀重建阿富汗感到愤怒，并警告印度在喀布尔的作用越大，给地区和平带来的威胁就越大。自1947年独立之后，巴基斯坦已与印度打了三场战争。&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142233.jpg&quot;&gt;&lt;/p&gt;
    # &lt;p&gt;中国国务委员杨洁篪23日呼吁美国重视巴基斯坦在阿富汗问题上的重要作用，尊重巴基斯坦的主权和合理安全关切。中国西部领土与巴基斯坦和阿富汗接壤。&lt;/p&gt;
    # &lt;p&gt;巴参议院国防委员会主席沙耶德对此补充说，&ldquo;9&middot;11事件以来，地区形势对比已大为改变。今天的美国在本地区的影响力已大幅减弱，而巴基斯坦在外交政策上的战略和选择空间也更大了。&rdquo;&lt;/p&gt;
    # &lt;p&gt;上世纪冷战期间，巴美关系密切。9&middot;11事件后，巴基斯坦参加国际反恐战争，参与打击塔利班和&ldquo;基地&rdquo;组织，积极参与阿富汗重建。&lt;/p&gt;
    # &lt;p&gt;美国奥巴马政府上台后出台对阿富汗、巴基斯坦新战略，加大对巴基斯坦军事和经济投入，但两国间互信不足。2011年，受本&middot;拉登在巴基斯坦境内被击毙、美北约越境空袭巴基斯坦边境哨所事件等影响，巴关闭境内北约后勤补给线，一度中断同美高层互访，两国关系降至低点。&lt;/p&gt;
    # &lt;p&gt;2012年以来，两国高层逐渐恢复接触，关系逐步得到改善，并于2014年3月重启巴美战略对话。&lt;/p&gt;
    # &lt;p&gt;2016年1月，阿巴中美四方协调组首次会议召开，致力于推进&ldquo;阿人主导，阿人所有&rdquo;的和解进程。&lt;/p&gt;
    # 					&lt;/div&gt;'''
    text = html_parser.unescape(text)
    word=TextRank4Keyword()
    word.analyze(text)
    w_list=word.get_keywords(num=10)
    for i in w_list:
        print i.word,i.weight

def jieba_keywords():
    html_parser = HTMLParser.HTMLParser()
    text = '''&lt;?xml version='1.0' encoding='utf-8'?&gt;&lt;div&gt;&lt;p&gt;周三亚市早盘，美国相关资产盘中异动。稍早美国媒体报道称， 特朗普要求时任FBI局长科米结束调查弗林事件。他在上周突然解除了科米的职务。&lt;/p&gt;&lt;p&gt;亚市早盘，标普500股指期货一度下跌0.7%。美国10年国债收益率跌3个基点，报2.30%。COMEX黄金涨近10美元。ICE美元指数延续跌势，一度跌破98，报97.94，再创去年11月9日（美国大选次日）以来新低，迄今已连跌五日。&lt;/p&gt;&lt;p&gt;昨日纽约时报报道称，已被解职的联邦调查局（FBI）局长科米(James Comey)2月会见特朗普后不久在备忘录中称，总统要求他结束对前国家安全顾问迈克尔&middot;弗林(Michael Flynn)的调查。&lt;/p&gt;&lt;p&gt;不过，白宫对纽约时报的报道予以否认，称&ldquo;特朗普从未要求科米或任何人结束任何调查，包括关于弗林的调查。报道中提及的备忘录的内容并非事实，其对于总统和科密之间谈话内容的描述并不准确。&rdquo;&lt;/p&gt;&lt;p&gt;同时，《华盛顿邮报》报道称，特朗普上周在椭圆形办公室会见俄罗斯外长拉夫罗夫及俄罗斯驻美大使，可能向他们泄露了有关恐怖组织伊斯兰国（IS）的绝密情报。&lt;/p&gt;&lt;p&gt;此事凸显出白宫面临的新政治风险：总统可能妨碍司法公正。一旦这被判定为事实，极有可能导致特朗普被弹劾。&lt;/p&gt;&lt;p&gt;随着特朗普向俄罗斯&ldquo;泄密门&rdquo;事件逐渐发酵，投资者越来越担心特朗普可能无法完成任期。分析师称，即使特朗普能够完成任期，也会有很多来自政治方面的事件分散其推进经济刺激计划的注意力。&lt;/p&gt;&lt;h2&gt;特朗普被弹劾概率攀升？&lt;/h2&gt;&lt;p&gt;如果要弹劾总统，众议院必须有多数议员的支持。民主党目前并没有人表态支持弹劾总统，或者建议开启弹劾程序。&lt;/p&gt;&lt;p&gt;然而，人们已经开始为&ldquo;特朗普通俄门&rdquo;事件可能的糟糕结果做准备了。根据PredictIt网站，特朗普今年被弹劾的概率已翻了一倍，从19%飙升至29%。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df6db35c283.jpeg&quot;&gt;&lt;p&gt;金融市场也开始对相关风险开始计价。美元/日元大跌40个点：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/2079000a8f8215a482a8.jpeg&quot;&gt;&lt;p&gt;标普500股指期货亚市早盘明显下挫：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd655b194d28.jpeg&quot;&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207b0003a87d33d268c6.jpeg&quot;&gt;&lt;p&gt;国际金价大涨：&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/207a0003dd6661e97441.jpeg&quot;&gt;&lt;h2&gt;&ldquo;特朗普通俄门&rdquo;发酵&lt;/h2&gt;&lt;p&gt;纽约时报报道称，科米在备忘录中写道，特朗普在2月的会面中对他说：&ldquo;我希望你可以让这件事过去&rdquo;。而科密并未直接回应特朗普的要求。&lt;/p&gt;&lt;p&gt;5月9日，特朗普在毫无先兆的情况下解雇了科米。当时此事令全球愕然，连科米本人都显得措手不及。甚至有美国媒体和官员将此事与当年尼克松试图阻挠国会调查&ldquo;水门事件&rdquo;联系起来。&lt;/p&gt;&lt;p&gt;英国《卫报》当时评论称，特朗普解雇科米，不仅让人质疑FBI在调查特朗普竞选期间与俄罗斯联系案件的独立性。特朗普称解雇科米是因为他对希拉里&ldquo;邮件门&rdquo;的调查，但民主党却认为，特朗普此举是在阻挠FBI对其&ldquo;通俄门&rdquo;进行调查。&lt;/p&gt;&lt;p&gt;此前，包括前总统国家安全顾问弗林、司法部长等多名高官在内的特朗普政府官员都卷入了特朗普团队在去年竞选期间与俄罗斯相联系的&ldquo;通俄门&rdquo;。&lt;/p&gt;&lt;p&gt;今年2月14日，也就是特朗普就任总统还不到一个月的时间，白宫国家安全顾问迈克尔&middot;弗林因被指在与俄国驻美国大使馆通话事件上误导政府而提出辞职。&lt;/p&gt;&lt;p&gt;弗林被指在去年12月（也就是特朗普宣誓就职前）与俄国驻美国大使馆Sergey I. Kislyak就美对俄制裁问题通话，这一行为违反了美国法律。当时他尚未被任命为国家安全顾问。&lt;/p&gt;&lt;p&gt;CNN 5月9日报道称，陪审团已开始考虑传唤弗林。若果真如此，则意味着对特朗普竞选团队的&ldquo;通俄门&rdquo;调查将进入一个新阶段。&lt;/p&gt;&lt;p&gt;就在特朗普炒了科米鱿鱼之后不久，《华盛顿邮报》报道了有关&ldquo;特朗普通俄门&rdquo;的另一个消息：特朗普上周在椭圆形办公室会议上向俄罗斯外长及俄罗斯驻美大使泄露了有关伊斯兰国（IS）意图的高度机密信息。&lt;/p&gt;&lt;p&gt;《华盛顿邮报》引述一名未公开身分的美国官员报道称，特朗普上周三在白宫与俄罗斯外长拉夫罗夫会晤时，曾向来宾炫耀他每天都可以得到关于伊斯兰国组织的恐怖威胁的绝对可靠信息，他并详细描述了一个该组织与在飞机上使用手提电脑有关的恐怖行动方案。&lt;/p&gt;&lt;p&gt;这名美国官员向《华邮》表示，特朗普向俄罗斯客人透露的信息比美国向自己的盟友透露的还要多，都属于美国各情报部门列为绝密级别最高的信息。&lt;/p&gt;&lt;p&gt;不过，《华盛顿邮报》的报道并没有说特朗普泄露了情报来源或方式，也没有说特朗普泄露任何军事行动。报道称，该情报是从一个与美国开展情报合作的国家得来的。&lt;/p&gt;&lt;p&gt;值得注意的是这件事发生的时机：几天之后，特朗普就将开启他作为美国总统的首次外访，目的地包括沙特阿拉伯和以色列&mdash;&mdash;这是美国在打击IS组织前线上两个至关重要的盟友。&lt;/p&gt;&lt;h2&gt;总统的反击&lt;/h2&gt;&lt;p&gt;针对《华盛顿邮报》的上述报道内容，特朗普周二连续发布twitter称，在关于与俄罗斯官员分享有关恐怖分子的信息这个问题上，他拥有&ldquo;绝对权力&rdquo;：&lt;/p&gt;&lt;blockquote&gt;&lt;p&gt;作为总统，我希望与俄罗斯(在一次会议计划公开披露的白宫会晤中)分享与恐怖主义以及飞行安全有关的信息，我有绝对的权力这么做。&lt;/p&gt;&lt;p&gt;出于人道主义原因，而且我希望俄罗斯大幅加强他们打击伊斯兰国组织以及恐怖主义的行动。&lt;/p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/208100039df5a142e55d.jpeg&quot;&gt;&lt;/blockquote&gt;&lt;p&gt;国家安全委员会发言人Michael Anton称，总统的推文与白宫高级官员驳斥该报道的表态并不矛盾。&lt;/p&gt;&lt;p&gt;白宫国家安全顾问H.R. McMaster表示，&ldquo;这篇报道内容失实，交谈自始至终都没有涉及情报来源或方式，总统也未透露任何尚未公开的军事行动。&rdquo;&lt;/p&gt;&lt;p&gt;而关于有报道称特朗普上周在椭圆形办公室会议中泄露高度机密信息，民主党和共和党都有议员对此表达了关切，他们同时要求此事应有更为详尽的解释。&lt;/p&gt;&lt;/div&gt;'''
    #     text='''&lt;?xml version='1.0' encoding='utf-8'?&gt;
    # &lt;div&gt;
    #
    #                         &lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142769.jpg&quot;&gt;&lt;/p&gt;
    # &lt;p&gt;8月3日，巴基斯坦总理阿巴西在伊斯兰堡检阅仪仗队。来源：视觉中国&lt;/p&gt;
    # &lt;p&gt;当地时间周四下午，巴基斯坦总理阿巴西与军方将领们召开会议，商讨应对美国阿富汗新战略的方案。&lt;/p&gt;
    # &lt;p&gt;三天前，美国总统特朗普宣布改变在阿富汗战争上的立场，将加大军事存在，同时也以空前严厉的语气指责反恐盟友巴基斯坦。他说，&ldquo;不会再纵容巴基斯坦成为恐怖组织的天堂&rdquo;，同时还意外邀请巴基斯坦的&ldquo;死敌&rdquo;印度更多地参与阿富汗的反恐行动。&lt;/p&gt;
    # &lt;p&gt;特朗普表态过后，白宫官员们更是添油加醋，进一步威胁要缩减对巴援助和军事预算。&lt;/p&gt;
    # &lt;p&gt;目前，总理阿巴西本人尚未对此公开回应，但外交部长阿西夫称，华盛顿方面不应该把阿富汗战争的失败归责于巴基斯坦。巴基斯坦也否认自己是武装分子的避风港。&lt;/p&gt;
    # &lt;p&gt;阿西夫也出席了周四全国安全委员会的会议，此前一天他还会见了美国驻巴基斯坦大使大卫&middot;黑尔，并表示相对于美国的援助金，巴基斯坦更需要信任和理解。&lt;/p&gt;
    # &lt;p&gt;据路透社报道，巴官员们对华盛顿方面的表态感到愤怒，称其无视该国在反武装斗争和抗击基地组织、ISIS以及巴基斯坦塔利班方面所取得的成绩。&lt;/p&gt;
    # &lt;p&gt;据巴方估计，自2001年美国发动反恐战争以来，巴基斯坦为此牺牲了7万人。&lt;/p&gt;
    # &lt;p&gt;&ldquo;我们认为特朗普政府的立场完全是片面的，对巴基斯坦不公平，未能承认和尊重巴方在反恐战发挥的重要作用。&rdquo;巴参议院国防委员会主席沙耶德周四对路透社说。&lt;/p&gt;
    # &lt;p&gt;不仅如此，巴基斯坦官员还对印度受邀重建阿富汗感到愤怒，并警告印度在喀布尔的作用越大，给地区和平带来的威胁就越大。自1947年独立之后，巴基斯坦已与印度打了三场战争。&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/img/201708/1503620142233.jpg&quot;&gt;&lt;/p&gt;
    # &lt;p&gt;中国国务委员杨洁篪23日呼吁美国重视巴基斯坦在阿富汗问题上的重要作用，尊重巴基斯坦的主权和合理安全关切。中国西部领土与巴基斯坦和阿富汗接壤。&lt;/p&gt;
    # &lt;p&gt;巴参议院国防委员会主席沙耶德对此补充说，&ldquo;9&middot;11事件以来，地区形势对比已大为改变。今天的美国在本地区的影响力已大幅减弱，而巴基斯坦在外交政策上的战略和选择空间也更大了。&rdquo;&lt;/p&gt;
    # &lt;p&gt;上世纪冷战期间，巴美关系密切。9&middot;11事件后，巴基斯坦参加国际反恐战争，参与打击塔利班和&ldquo;基地&rdquo;组织，积极参与阿富汗重建。&lt;/p&gt;
    # &lt;p&gt;美国奥巴马政府上台后出台对阿富汗、巴基斯坦新战略，加大对巴基斯坦军事和经济投入，但两国间互信不足。2011年，受本&middot;拉登在巴基斯坦境内被击毙、美北约越境空袭巴基斯坦边境哨所事件等影响，巴关闭境内北约后勤补给线，一度中断同美高层互访，两国关系降至低点。&lt;/p&gt;
    # &lt;p&gt;2012年以来，两国高层逐渐恢复接触，关系逐步得到改善，并于2014年3月重启巴美战略对话。&lt;/p&gt;
    # &lt;p&gt;2016年1月，阿巴中美四方协调组首次会议召开，致力于推进&ldquo;阿人主导，阿人所有&rdquo;的和解进程。&lt;/p&gt;
    # 					&lt;/div&gt;'''
    text = html_parser.unescape(text)
    tags=analyse.extract_tags(sentence=text,topK=10)
    for i in tags:
        print i
    # print ','.join(tags)

if __name__ == '__main__':
    # jieba_keywords()
    textrank_keywords()
    # textrank_summary()
    # jieba_tags()