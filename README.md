# 2048
This project contains three main file for three different versions.

- `game_2048_no_gui.py` is written in python with no gui.

- `game_2048_with_gui.py` is written in python with gui.

- `Game.java` is written in java with no gui.

# Play
For Python:
```
$ python3 game_2048_no_gui.py
```
```
$ python3 game_2048_with_gui.py
```
For Java:
```
$ javac Game.java
$ java Game
```

# Test Cases
[0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0]

mergeList记录i-4的情况
```
+-----+-----+-----+-----+
|     |   4 |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
+-----+-----+-----+-----+
|     |   2 |     |     |
+-----+-----+-----+-----+
|     |   2 |     |     |
+-----+-----+-----+-----+
```

[0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0]

mergeList记录i的情况
```
+-----+-----+-----+-----+
|     |     |     |     |
+-----+-----+-----+-----+
|     |   2 |     |     |
+-----+-----+-----+-----+
|     |   2 |     |     |
+-----+-----+-----+-----+
|     |   4 |     |     |
+-----+-----+-----+-----+
```

