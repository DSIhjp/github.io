## 登录接口（必接）

### 1 接口定义

```java
/**
* 登录接口
* @param activity 游戏的主activity
*/
public void grLogin(Activity activity);
```

### 2 示例

登录回调结果在**onLoginResult(GRToken authResult)**方法：

通过authResult获取用户登录信息

| authResult.getUsername();<br />authResult.getToken();<br />authResult.getUserID(); |
| :--------------------------------------------------------------------------------- |

```java
GrAPI.getInstance().grLogin(MainActivity.this);
```
