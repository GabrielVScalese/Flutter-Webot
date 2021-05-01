import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:project/models/client.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(
            'Controlador de Webot',
            textAlign: TextAlign.center,
          ),
        ),
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              child: Row(
                children: [
                  Container(
                      height: 100,
                      child: ElevatedButton(
                          onPressed: () async {
                            await Client.execute('l');
                          },
                          child: Icon(
                            Icons.arrow_back_rounded,
                            size: 30,
                          ))),
                  Container(
                      height: 100,
                      margin: EdgeInsets.only(left: 20),
                      child: ElevatedButton(
                          onPressed: () async {
                            await Client.execute('r');
                          },
                          child: Icon(
                            Icons.arrow_forward_rounded,
                            size: 30,
                          )))
                ],
              ),
            ),
            Container(
              child: Row(
                children: [
                  Container(
                      margin: EdgeInsets.only(left: 50),
                      height: 100,
                      child: ElevatedButton(
                          onPressed: () async {
                            await Client.execute('u');
                          },
                          child: Icon(
                            Icons.arrow_upward_rounded,
                            size: 30,
                          ))),
                  Container(
                      margin: EdgeInsets.only(left: 20),
                      height: 100,
                      child: ElevatedButton(
                          onPressed: () async {
                            await Client.execute('d');
                          },
                          child: Icon(
                            Icons.arrow_downward_rounded,
                            size: 30,
                          ))),
                  Container(
                      margin: EdgeInsets.only(left: 20),
                      height: 100,
                      child: ElevatedButton(
                          onPressed: () async {
                            await Client.execute('s');
                          },
                          child: Icon(
                            Icons.stop_circle_rounded,
                            size: 30,
                          ))),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}
