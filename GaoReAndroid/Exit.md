## 退出接口（必接）

### 1 接口定义

```java
/**
*退出接口。
* @param activity 游戏的主activity
*/
public void grExit(Activity activity) 
```

### 2 示例

接口回调结果在**onExit()**方法，需在回调中关闭游戏

研发需要在MainActivity下的**onBackPressed()**方法和**onKeyDown**(int keyCode, KeyEvent event)方法下调用该接口，代码如下

```java
@Override
public void onBackPressed() {
    super.onBackPressed();
    GrAPI.getInstance().grExit(this);
}
@Override
public boolean onKeyDown(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_BACK) {
	GrAPI.getInstance().grExit(this);
    }
```
