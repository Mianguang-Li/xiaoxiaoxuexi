import 'package:flutter/material.dart';
import 'grade1_chinese_bank.dart';
import 'grade1_math_bank.dart';
import 'grade1_english_bank.dart';
import 'grade2_chinese_bank.dart';
import 'grade2_math_bank.dart';
import 'grade2_english_bank.dart';
import 'grade3_chinese_bank.dart';
import 'grade3_math_bank.dart';
import 'grade3_english_bank.dart';
import 'grade4_chinese_bank.dart';
import 'grade4_math_bank.dart';
import 'grade4_english_bank.dart';
import 'grade5_chinese_bank.dart';
import 'grade5_math_bank.dart';
import 'grade5_english_bank.dart';
import 'grade6_chinese_bank.dart';
import 'grade6_math_bank.dart';
import 'grade6_english_bank.dart';
import 'grade7_chinese_bank.dart';
import 'grade7_math_bank.dart';
import 'grade7_english_bank.dart';
import 'grade7_politics_bank.dart';
import 'grade7_geography_bank.dart';
import 'grade7_biology_bank.dart';
import 'grade7_history_bank.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '小小学霸',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: SplashPage(),
    );
  }
}

// 开屏页
class SplashPage extends StatefulWidget {
  @override
  State<SplashPage> createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 2), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => StageSelectPage()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[700],
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.school, size: 100, color: Colors.white),
            SizedBox(height: 20),
            Text(
              '小小学霸',
              style: TextStyle(
                fontSize: 40,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            SizedBox(height: 10),
            Text(
              '让学习更有趣！',
              style: TextStyle(fontSize: 18, color: Colors.white70),
            ),
            SizedBox(height: 40),
            Text(
              '阿绵创意工坊',
              style: TextStyle(fontSize: 14, color: Colors.white60),
            ),
          ],
        ),
      ),
    );
  }
}

// ========== 学习阶段选择页 ==========
class StageSelectPage extends StatelessWidget {
  void _goToStage(BuildContext context, String stage) {
    if (stage == '小学') {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => PrimarySchoolPage()),
      );
    } else {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => MiddleSchoolPage()),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('小小学霸'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: Icon(Icons.info_outline),
            onPressed: () => _showAbout(context),
          ),
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          children: [
            SizedBox(height: 30),
            Icon(Icons.school, size: 80, color: Colors.blue[300]),
            SizedBox(height: 40),
            Text(
              '请选择学习阶段',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 40),
            // 小学按钮
            _StageButton(
              label: '小学',
              subLabel: '一至六年级',
              icon: Icons.child_care,
              color: Colors.blue,
              onTap: () => _goToStage(context, '小学'),
            ),
            SizedBox(height: 20),
            // 初中按钮
            _StageButton(
              label: '初中',
              subLabel: '七至九年级',
              icon: Icons.auto_stories,
              color: Colors.orange,
              onTap: () => _goToStage(context, '初中'),
            ),
            Expanded(child: Container()),
            Text('阿绵创意工坊', style: TextStyle(fontSize: 12, color: Colors.grey)),
            SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  void _showAbout(BuildContext context) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Row(children: [
          Icon(Icons.school, color: Colors.blue),
          SizedBox(width: 8),
          Text('关于我们'),
        ]),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('小小学霸是一款专为学生打造的学习助手。'),
            SizedBox(height: 12),
            Text('支持小学、初中多个年级，涵盖语文、数学、英语等多门学科，让学习变得更有趣！'),
            SizedBox(height: 16),
            Row(children: [
              Icon(Icons.business, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('阿绵创意工坊', style: TextStyle(fontWeight: FontWeight.bold)),
            ]),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.email, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('mianguang@163.com', style: TextStyle(color: Colors.blue[700])),
            ]),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: Text('知道了'),
          ),
        ],
      ),
    );
  }
}

class _StageButton extends StatelessWidget {
  final String label;
  final String subLabel;
  final IconData icon;
  final Color color;
  final VoidCallback onTap;

  _StageButton({
    required this.label,
    required this.subLabel,
    required this.icon,
    required this.color,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: double.infinity,
        padding: EdgeInsets.symmetric(vertical: 24, horizontal: 20),
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(color: color.withOpacity(0.3), blurRadius: 8, offset: Offset(0, 4)),
          ],
        ),
        child: Row(
          children: [
            Icon(icon, size: 50, color: Colors.white),
            SizedBox(width: 20),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  label,
                  style: TextStyle(
                      fontSize: 26, fontWeight: FontWeight.bold, color: Colors.white),
                ),
                Text(subLabel, style: TextStyle(fontSize: 14, color: Colors.white70)),
              ],
            ),
            Spacer(),
            Icon(Icons.arrow_forward_ios, color: Colors.white70, size: 20),
          ],
        ),
      ),
    );
  }
}

// ========== 小学首页 ==========
class PrimarySchoolPage extends StatefulWidget {
  @override
  State<PrimarySchoolPage> createState() => _PrimarySchoolPageState();
}

class _PrimarySchoolPageState extends State<PrimarySchoolPage> {
  int _grade = 1;
  int _subject = 0;
  final _subjects = ['语文', '数学', '英语'];

  final _gradeNames = ['一', '二', '三', '四', '五', '六'];

  List<List<List<dynamic>>> get _bank {
    switch (_grade) {
      case 1:
        return [grade1ChineseBank, grade1MathBank, grade1EnglishBank];
      case 2:
        return [grade2ChineseBank, grade2MathBank, grade2EnglishBank];
      case 3:
        return [grade3ChineseBank, grade3MathBank, grade3EnglishBank];
      case 4:
        return [grade4ChineseBank, grade4MathBank, grade4EnglishBank];
      case 5:
        return [grade5ChineseBank, grade5MathBank, grade5EnglishBank];
      case 6:
        return [grade6ChineseBank, grade6MathBank, grade6EnglishBank];
      default:
        return [grade1ChineseBank, grade1MathBank, grade1EnglishBank];
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('小小学霸 · 小学'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: Icon(Icons.info_outline),
            onPressed: () => _showAbout(context),
          ),
        ],
      ),
      body: Column(
        children: [
          SizedBox(height: 20),
          Text('选择年级', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 10),
          Wrap(children: [
            for (int g = 1; g <= 6; g++)
              GestureDetector(
                onTap: () => setState(() => _grade = g),
                child: Container(
                  margin: EdgeInsets.all(4),
                  width: 50,
                  height: 50,
                  decoration: BoxDecoration(
                    color: _grade == g ? Colors.blue : Colors.grey[300],
                    borderRadius: BorderRadius.circular(25),
                  ),
                  child: Center(
                    child: Text(_gradeNames[g - 1],
                        style: TextStyle(
                            color: _grade == g ? Colors.white : Colors.black87,
                            fontSize: 18,
                            fontWeight: FontWeight.bold)),
                  ),
                ),
              ),
          ]),
          SizedBox(height: 30),
          Icon(Icons.school, size: 80, color: Colors.blue[300]),
          SizedBox(height: 30),
          Text('选择科目', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 10),
          Wrap(children: [
            for (int i = 0; i < _subjects.length; i++)
              GestureDetector(
                onTap: () => setState(() => _subject = i),
                child: Container(
                  margin: EdgeInsets.all(4),
                  padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                  decoration: BoxDecoration(
                    color: _subject == i ? Colors.blue : Colors.grey[300],
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(_subjects[i],
                      style: TextStyle(
                          color: _subject == i ? Colors.white : Colors.black87, fontSize: 16)),
                ),
              ),
          ]),
          Expanded(child: Container()),
          Padding(
            padding: EdgeInsets.all(20),
            child: ElevatedButton(
              onPressed: () => _startStudy(context),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
                padding: EdgeInsets.symmetric(horizontal: 60, vertical: 15),
              ),
              child: Text('开始学习', style: TextStyle(fontSize: 20, color: Colors.white)),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(bottom: 20),
            child: Text('阿绵创意工坊', style: TextStyle(fontSize: 12, color: Colors.grey)),
          ),
        ],
      ),
    );
  }

  void _startStudy(BuildContext context) {
    final bank = _bank[_subject];
    // 随机抽取15道题
    final shuffled = List<List<dynamic>>.from(bank)..shuffle();
    final picked = shuffled.take(15).toList();
    final questions = picked
        .map((q) => Question(q[0] as String, List<String>.from(q[1]), q[2] as String))
        .toList();
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => StudyPage('${_subjects[_subject]} · ${_gradeNames[_grade - 1]}年级', questions),
      ),
    );
  }

  void _showAbout(BuildContext context) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Row(children: [
          Icon(Icons.school, color: Colors.blue),
          SizedBox(width: 8),
          Text('关于我们'),
        ]),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('小小学霸是一款专为学生打造的学习助手。'),
            SizedBox(height: 12),
            Text('支持小学、初中多个年级，涵盖语文、数学、英语等多门学科，让学习变得更有趣！'),
            SizedBox(height: 16),
            Row(children: [
              Icon(Icons.business, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('阿绵创意工坊', style: TextStyle(fontWeight: FontWeight.bold)),
            ]),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.email, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('mianguang@163.com', style: TextStyle(color: Colors.blue[700])),
            ]),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: Text('知道了'),
          ),
        ],
      ),
    );
  }
}

// ========== 初中首页 ==========
class MiddleSchoolPage extends StatefulWidget {
  @override
  State<MiddleSchoolPage> createState() => _MiddleSchoolPageState();
}

class _MiddleSchoolPageState extends State<MiddleSchoolPage> {
  int _grade = 7;
  int _subject = 0;

  final _gradeNames = {7: '七', 8: '八', 9: '九'};

  final Map<int, List<String>> _subjectsMap = {
    7: ['数学', '语文', '英语', '政治', '地理', '生物', '历史'],
    8: ['数学', '语文', '英语', '政治', '地理', '生物', '历史', '物理'],
    9: ['数学', '语文', '英语', '政治', '历史', '物理', '化学'],
  };

  // 七年级题库：数学、语文、英语、政治、地理、生物、历史
  final Map<int, List<List<List<dynamic>>>> _bankMap = {
    7: [
      grade7MathBank,
      grade7ChineseBank,
      grade7EnglishBank,
      grade7PoliticsBank,
      grade7GeographyBank,
      grade7BiologyBank,
      grade7HistoryBank,
    ],
    // 八年级题库
    8: [
      [
        ['解方程：2x = 10', ['x=4', 'x=5', 'x=6', 'x=3'], 'x=5'],
        ['三角形内角和是？', ['90°', '180°', '270°', '360°'], '180°'],
        ['(-1) + (-2) = ?', ['-3', '3', '-1', '1'], '-3'],
      ],
      [
        ['《岳阳楼记》作者是？', ['范仲淹', '欧阳修', '苏轼', '王安石'], '范仲淹'],
        ['先天下之忧而忧下一句是？', ['后天下之乐而乐', '天下兴亡匹夫有责', '位卑未敢忘忧国', '人生自古谁无死'], '后天下之乐而乐'],
        ['说明文的主要特征是？', ['抒情', '叙事', '客观说明', '议论'], '客观说明'],
      ],
      [
        ['good morning 中文是？', ['早上好', '晚安', '你好', '再见'], '早上好'],
        ['study 的中文意思是？', ['学习', '玩耍', '睡觉', '吃饭'], '学习'],
        ['一般疑问句用什么引导？', ['Do/Does', 'What', 'Who', 'Where'], 'Do/Does'],
      ],
      [
        ['人民代表大会制度的组织原则是？', ['民主集中制', '三权分立', '联邦制', '邦联制'], '民主集中制'],
        ['公民满多少岁有选举权？', ['16', '18', '20', '14'], '18'],
        ['维护国家安全义务不包括？', ['向敌人出卖情报', '提供便利条件', '协助侦查', '保守秘密'], '向敌人出卖情报'],
      ],
      [
        ['世界最高峰是？', ['珠穆朗玛峰', '乔戈里峰', '干城章嘉峰', '洛子峰'], '珠穆朗玛峰'],
        ['北纬23.5°叫做什么？', ['北回归线', '南回归线', '赤道', '北极圈'], '北回归线'],
        ['地球自转方向是？', ['自西向东', '自东向西', '自南向北', '自北向南'], '自西向东'],
      ],
      [
        ['植物细胞特有的结构是？', ['细胞壁', '细胞核', '细胞膜', '叶绿体'], '叶绿体'],
        ['人体红细胞的功能是？', ['运输氧气', '抵抗疾病', '止血', '调节体温'], '运输氧气'],
        ['光的折射定律中，入射角和折射角的关系？', ['成正比', '成反比', '满足斯涅尔定律', '无关'], '满足斯涅尔定律'],
      ],
      [
        ['唐朝建立于哪一年？', ['618年', '581年', '907年', '712年'], '618年'],
        ['科举制度正式确立于哪个朝代？', ['隋朝', '唐朝', '宋朝', '明朝'], '隋朝'],
        ['《史记》的作者是？', ['司马迁', '司马光', '班固', '陈寿'], '司马迁'],
      ],
      [
        ['速度公式 v = s/t，其中 s 表示？', ['路程', '时间', '速度', '加速度'], '路程'],
        ['水的密度是？', ['1g/cm3', '0.8g/cm3', '1.5g/cm3', '2g/cm3'], '1g/cm3'],
        ['大气压随海拔升高而如何变化？', ['降低', '升高', '不变', '先升后降'], '降低'],
      ],
    ],
    // 九年级题库
    9: [
      [
        ['抛物线 y = x2 的对称轴是？', ['x=0', 'y=0', 'y=x', 'x=1'], 'x=0'],
        ['若方程 x2 = 4，则 x = ?', ['±2', '2', '-2', '4'], '±2'],
        ['直角三角形两直角边为3和4，斜边是？', ['5', '6', '7', '4'], '5'],
      ],
      [
        ['《孔乙己》作者是？', ['鲁迅', '茅盾', '老舍', '巴金'], '鲁迅'],
        ['《诗经》分为哪三部分？', ['风雅颂', '赋比兴', '古今体', '正变'], '风雅颂'],
        ['春蚕到死丝方尽下一句是？', ['蜡炬成灰泪始干', '化作春泥更护花', '落红不是无情物', '零落成泥碾作尘'], '蜡炬成灰泪始干'],
      ],
      [
        ['goodbye 中文意思是？', ['再见', '你好', '对不起', '谢谢'], '再见'],
        ['被动语态 be + ? + by', ['过去分词', '现在分词', '动词原形', '动名词'], '过去分词'],
        ['If I were you, I would... 是什么语气？', ['虚拟语气', '条件状语', '定语从句', '名词性从句'], '虚拟语气'],
      ],
      [
        ['我国根本政治制度是？', ['人民代表大会制度', '中国共产党领导的多党合作制', '民族区域自治', '基层群众自治'], '人民代表大会制度'],
        ['公民依法服兵役是履行什么义务？', ['国防义务', '纳税义务', '劳动义务', '受教育义务'], '国防义务'],
        ['社会主义法治的根本保证是？', ['党的领导', '人民当家作主', '依法治国', '司法独立'], '党的领导'],
      ],
      [
        ['中国近代史的开端是？', ['鸦片战争', '甲午战争', '辛亥革命', '五四运动'], '鸦片战争'],
        ['抗日战争中牺牲的最高将领是？', ['张自忠', '佟麟阁', '赵登禹', '谢晋元'], '张自忠'],
        ['新中国成立于哪一年？', ['1949年', '1945年', '1950年', '1951年'], '1949年'],
      ],
      [
        ['能量守恒定律内容是？', ['能量既不会凭空产生也不会凭空消失', '能量可以随意转换', '能量会逐渐减少', '能量会逐渐增加'], '能量既不会凭空产生也不会凭空消失'],
        ['欧姆定律公式是？', ['I = U/R', 'P = UI', 'W = Pt', 'F = ma'], 'I = U/R'],
        ['物态变化中，熔化需要？', ['吸热', '放热', '不变', '先吸热后放热'], '吸热'],
      ],
      [
        ['盐酸的化学式是？', ['HCl', 'H2SO4', 'HNO3', 'NaOH'], 'HCl'],
        ['Fe与稀盐酸反应生成？', ['FeCl2 + H2', 'FeCl3 + H2', 'FeO + H2', 'Fe(OH)3 + H2'], 'FeCl2 + H2'],
        ['燃烧需要满足三个条件，灭火可采取？', ['隔绝空气或降温至着火点以下', '增加氧气', '提高温度', '移除可燃物同时增加氧气'], '隔绝空气或降温至着火点以下'],
      ],
    ],
  };

  List<String> get _currentSubjects => _subjectsMap[_grade] ?? [];

  List<List<List<dynamic>>> get _currentBank => _bankMap[_grade] ?? [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('小小学霸 · 初中'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: Icon(Icons.info_outline),
            onPressed: () => _showAbout(context),
          ),
        ],
      ),
      body: Column(
        children: [
          SizedBox(height: 20),
          Text('选择年级', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 10),
          Wrap(children: [
            for (int g in [7, 8, 9])
              GestureDetector(
                onTap: () => setState(() {
                  _grade = g;
                  _subject = 0;
                }),
                child: Container(
                  margin: EdgeInsets.all(4),
                  width: 60,
                  height: 50,
                  decoration: BoxDecoration(
                    color: _grade == g ? Colors.orange : Colors.grey[300],
                    borderRadius: BorderRadius.circular(25),
                  ),
                  child: Center(
                    child: Text(
                      '${_gradeNames[g]}年级',
                      style: TextStyle(
                          color: _grade == g ? Colors.white : Colors.black87,
                          fontSize: 15,
                          fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ),
          ]),
          SizedBox(height: 30),
          Icon(Icons.school, size: 80, color: Colors.orange[300]),
          SizedBox(height: 30),
          Text('选择科目', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 10),
          Wrap(children: [
            for (int i = 0; i < _currentSubjects.length; i++)
              GestureDetector(
                onTap: () => setState(() => _subject = i),
                child: Container(
                  margin: EdgeInsets.all(4),
                  padding: EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                  decoration: BoxDecoration(
                    color: _subject == i ? Colors.orange : Colors.grey[300],
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(_currentSubjects[i],
                      style: TextStyle(
                          color: _subject == i ? Colors.white : Colors.black87, fontSize: 14)),
                ),
              ),
          ]),
          Expanded(child: Container()),
          Padding(
            padding: EdgeInsets.all(20),
            child: ElevatedButton(
              onPressed: () => _startStudy(context),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.orange,
                padding: EdgeInsets.symmetric(horizontal: 60, vertical: 15),
              ),
              child: Text('开始学习', style: TextStyle(fontSize: 20, color: Colors.white)),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(bottom: 20),
            child: Text('阿绵创意工坊', style: TextStyle(fontSize: 12, color: Colors.grey)),
          ),
        ],
      ),
    );
  }

  void _startStudy(BuildContext context) {
    final subject = _currentSubjects[_subject];
    final bank = _currentBank[_subject];
    // 随机抽取15道题
    final shuffled = List<List<dynamic>>.from(bank)..shuffle();
    final picked = shuffled.take(15).toList();
    final questions = picked
        .map((q) => Question(q[0] as String, List<String>.from(q[1]), q[2] as String))
        .toList();
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => StudyPage('${subject} · ${_gradeNames[_grade]}年级', questions),
      ),
    );
  }

  void _showAbout(BuildContext context) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Row(children: [
          Icon(Icons.school, color: Colors.blue),
          SizedBox(width: 8),
          Text('关于我们'),
        ]),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('小小学霸是一款专为学生打造的学习助手。'),
            SizedBox(height: 12),
            Text('支持小学、初中多个年级，涵盖语文、数学、英语等多门学科，让学习变得更有趣！'),
            SizedBox(height: 16),
            Row(children: [
              Icon(Icons.business, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('阿绵创意工坊', style: TextStyle(fontWeight: FontWeight.bold)),
            ]),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.email, size: 16, color: Colors.grey[600]),
              SizedBox(width: 8),
              Text('mianguang@163.com', style: TextStyle(color: Colors.blue[700])),
            ]),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: Text('知道了'),
          ),
        ],
      ),
    );
  }
}

// ========== 题目页 ==========
class Question {
  final String q;
  final List<String> o;
  final String a;
  Question(this.q, this.o, this.a);
}

class StudyPage extends StatefulWidget {
  final String title;
  final List<Question> questions;
  StudyPage(this.title, this.questions);
  @override
  State<StudyPage> createState() => _StudyPageState();
}

class _StudyPageState extends State<StudyPage> {
  int _i = 0;
  int _correct = 0;
  String? _selected;
  bool _show = false;

  void _check(String a) {
    if (_show) return;
    setState(() {
      _selected = a;
      _show = true;
      if (a == widget.questions[_i].a) _correct++;
    });
  }

  void _next() {
    if (_i < widget.questions.length - 1) {
      setState(() { _i++; _selected = null; _show = false; });
    } else {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (_) => ResultPage(_correct, widget.questions.length),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final q = widget.questions[_i];
    return Scaffold(
      appBar: AppBar(title: Text(widget.title), centerTitle: true),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(children: [
              Expanded(
                child: LinearProgressIndicator(
                  value: (_i + 1) / widget.questions.length,
                ),
              ),
              SizedBox(width: 10),
              Text('${_i + 1}/${widget.questions.length}'),
            ]),
            SizedBox(height: 20),
            Text(q.q, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            SizedBox(height: 20),
            ...q.o.map((o) => Padding(
                  padding: EdgeInsets.only(bottom: 10),
                  child: GestureDetector(
                    onTap: () => _check(o),
                    child: Container(
                      width: double.infinity,
                      padding: EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: _show
                            ? (o == q.a
                                ? Colors.green[100]
                                : (o == _selected ? Colors.red[100] : Colors.white))
                            : Colors.white,
                        border: Border.all(
                          color: _show
                              ? (o == q.a
                                  ? Colors.green
                                  : (o == _selected ? Colors.red : Colors.grey))
                              : Colors.grey,
                          width: 2,
                        ),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(o, style: TextStyle(fontSize: 18)),
                    ),
                  ),
                )),
            Spacer(),
            if (_show)
              Center(
                child: ElevatedButton(
                  onPressed: _next,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue,
                    padding: EdgeInsets.symmetric(horizontal: 40, vertical: 12),
                  ),
                  child: Text(
                    _i < widget.questions.length - 1 ? '下一题' : '查看成绩',
                    style: TextStyle(fontSize: 18, color: Colors.white),
                  ),
                ),
              ),
            SizedBox(height: 20),
          ],
        ),
      ),
    );
  }
}

// ========== 结果页 ==========
class ResultPage extends StatelessWidget {
  final int correct;
  final int total;
  ResultPage(this.correct, this.total);

  @override
  Widget build(BuildContext context) {
    double rate = correct / total * 100;
    String message;
    IconData icon;
    if (rate >= 80) {
      message = '太棒了！';
      icon = Icons.star;
    } else if (rate >= 60) {
      message = '还不错！';
      icon = Icons.thumb_up;
    } else {
      message = '继续加油！';
      icon = Icons.favorite;
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('答题结果'),
        centerTitle: true,
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 80, color: Colors.orange),
            SizedBox(height: 20),
            Text(message, style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
            SizedBox(height: 30),
            Text('正确题数', style: TextStyle(fontSize: 16, color: Colors.grey)),
            Text(
              '$correct / $total',
              style: TextStyle(fontSize: 48, fontWeight: FontWeight.bold, color: Colors.blue),
            ),
            SizedBox(height: 10),
            Text('正确率', style: TextStyle(fontSize: 16, color: Colors.grey)),
            Text(
              '${rate.toStringAsFixed(0)}%',
              style: TextStyle(
                  fontSize: 36,
                  fontWeight: FontWeight.bold,
                  color: rate >= 60 ? Colors.green : Colors.orange),
            ),
            SizedBox(height: 40),
            ElevatedButton(
              onPressed: () => Navigator.pop(context),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
                padding: EdgeInsets.symmetric(horizontal: 40, vertical: 12),
              ),
              child: Text('再来一次', style: TextStyle(fontSize: 18, color: Colors.white)),
            ),
            SizedBox(height: 30),
            Text('阿绵创意工坊', style: TextStyle(fontSize: 12, color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}
