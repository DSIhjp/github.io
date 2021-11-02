# 登录认证（必接）

## 1 登录认证地址

**注：后面的斜杠”/”不要少**

```java
http://apisdk.gaore.com/user/verifyAccount/
```

## 2 请求方式

* POST
* GET

## 3 参数

| 参数      | 描述                                                      |
| --------- | --------------------------------------------------------- |
| userID    | 登录认证成功之后，返回的userID                            |
| game_sign | 游戏标识，平台提供固定值game_sign                         |
| token     | SDK登录认证成功之后，返回到游戏前端的token                |
| time      | 当前时间戳，超时10分钟                                    |
| sign      | md5(userID+appid+token+time+loginkey);login_key由平台提供 |

## 4 返回

```
{
   state: 1(登录认证成功)；其他失败
    data: 认证成功才有数据，否则为空
        {
          userID:唯一用户ID
          username:用户名
        }
}
```
