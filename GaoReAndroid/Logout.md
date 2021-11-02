## 登出接口（必接）

### 1 接口定义

```java
/**
* 登出接口
* @param activity 游戏的主activity
*/
public void grLogout()
```

### 2 示例


回调结果在**onLogoutResult(int resultCode)**方法,

研发需要在回调结果中,进行游戏内账号退出，回到游戏登录界面

```java
GrAPI.getInstance().grLogout();
```
