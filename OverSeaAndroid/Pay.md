## 支付接口（必接）

### 1 接口定义

```java
/**
* 支付接口
* @param activity 游戏的主activity
*/
public void grPay(Activity activity, GRPayParams params)
```

### 2 示例

高热SDK支付在前端的回调仅代表付款成功，支付成功后sdk服务端会通知研发服务端发放元宝

```java
GRPayParams params = new GRPayParams();
params.setBuyNum(1); // 写默认1
params.setCoinNum(100); // 写默认100
params.setExtension(System.currentTimeMillis() + "");//透传字段
params.setPrice((float) 4.99); // 单位是美元
params.setProductId("com.twmobile.ljsn.499");//商品ID
params.setProductName("300魔晶");//商品名
params.setProductDesc("購買300魔晶");//商品描述
params.setRoleId("1");//角色ID
params.setRoleLevel(10);//角色等级
params.setRoleName("測試角色名");//角色名
params.setServerId("1");//区服ID
params.setServerName("測試");//区服名
params.setVip("vip1");//vip等级 若无 填'vip0'
GrAPI.getInstance().grPay(MainActivity.this, params);
```
