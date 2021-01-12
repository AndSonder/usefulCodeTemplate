```
name{Pygame界面模版}
introduce{提供了一些Pygame最基础的功能，平时想写一些需要点击的小程序非常好用}
```
# Pygame 界面模版


好用的pygame界面模版

你可以通过修改 `__init__` 中的参数基本参数才使用

```python
self.width = 500  # the width of the screen
self.height = 500  # the height of the screen
self.screen_name = 'Power by coronaPolvo'
self.background_image = 'aaa.png'  # the background image's file path
```

提供的基本功能有绘制背景图片和绘制文字

绘制背景图片只需要通过修改`self.background_image`即可
绘制文字使用方法`self.__write_words()`进行绘制即可

具体细节请看代码注释