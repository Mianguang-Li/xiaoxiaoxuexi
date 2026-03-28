import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Study',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomePage(),
    );
  }
}

class Question {
  final String q;
  final List<String> o;
  final String a;
  Question(this.q, this.o, this.a);
}

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _grade = 1;
  int _subject = 0;
  final _subjects = ['Chinese', 'Math', 'English'];
  final List<List<Question>> _bank = [
    [
      Question('A is initial?', ['a','o','e','i'], 'a'),
      Question('tian=4?', ['2','3','4','5'], '4'),
      Question('da-xiao?', ['shang','xia','xiao','zuo'], 'xiao'),
    ],
    [
      Question('1+2=?', ['2','3','4','5'], '3'),
      Question('>3?', ['1','2','3','4'], '4'),
      Question('3x4=?', ['7','10','12','14'], '12'),
    ],
    [
      Question('A->a?', ['a','b','c','d'], 'a'),
      Question('apple?', ['banana','apple','orange','grape'], 'apple'),
      Question('cat/dog?', ['dog/cat','cat/dog','fish/bird','pig/rabbit'], 'cat/dog'),
    ],
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Study [_subject]')),
      body: Column(
        children: [
          Text('Grade: '),
          Wrap(children: [1,2,3,4,5,6].map((g) => GestureDetector(
            onTap: () => setState(() => _grade = g),
            child: Container(
              margin: EdgeInsets.all(4),
              padding: EdgeInsets.all(8),
              color: _grade == g ? Colors.blue : Colors.grey,
              child: Text('G', style: TextStyle(color: Colors.white)),
            ),
          )).toList()),
          Expanded(child: Container()),
          ElevatedButton(
            onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => StudyPage(_subjects[_subject], _grade, _bank[_subject]))),
            child: Text('START'),
          ),
        ],
      ),
    );
  }
}

class StudyPage extends StatefulWidget {
  final String subject;
  final int grade;
  final List<Question> questions;
  StudyPage(this.subject, this.grade, this.questions);
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
      Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => ResultPage(_correct, widget.questions.length)));
    }
  }

  @override
  Widget build(BuildContext context) {
    var q = widget.questions[_i];
    return Scaffold(
      appBar: AppBar(title: Text(' G')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            LinearProgressIndicator(value: (_i+1)/widget.questions.length),
            SizedBox(height: 16),
            Text(q.q, style: TextStyle(fontSize: 20)),
            SizedBox(height: 16),
            ...q.o.map((o) => Padding(
              padding: EdgeInsets.only(bottom: 8),
              child: GestureDetector(
                onTap: () => _check(o),
                child: Container(
                  width: double.infinity,
                  padding: EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: _show ? (o==q.a ? Colors.green[100] : (o==_selected ? Colors.red[100] : Colors.white)) : Colors.white,
                    border: Border.all(color: _show ? (o==q.a ? Colors.green : (o==_selected ? Colors.red : Colors.grey)) : Colors.grey),
                  ),
                  child: Text(o),
                ),
              ),
            )).toList(),
            if (_show) ElevatedButton(onPressed: _next, child: Text(_i < widget.questions.length - 1 ? 'NEXT' : 'RESULT')),
          ],
        ),
      ),
    );
  }
}

class ResultPage extends StatelessWidget {
  final int correct;
  final int total;
  ResultPage(this.correct, this.total);
  @override
  Widget build(BuildContext context) {
    double rate = correct / total * 100;
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(rate >= 80 ? 'GREAT!' : (rate >= 60 ? 'GOOD!' : 'TRY AGAIN!'), style: TextStyle(fontSize: 32)),
            SizedBox(height: 20),
            Text('Correct:  / '),
            Text('Rate: %'),
            SizedBox(height: 20),
            ElevatedButton(onPressed: () => Navigator.pop(context), child: Text('AGAIN')),
          ],
        ),
      ),
    );
  }
}
