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
GrPayParams params = new GrPayParams();
params.setBuyNum(1); // 写默认1
params.setCoinNum(100); // 写默认100
params.setExtension(System.currentTimeMillis() + "");//扩展参数
params.setPrice(1); // 单位是元
params.setProductId("1");
params.setProductName("元宝");
params.setProductDesc("购买100元宝");
params.setRoleId("1");
params.setRoleLevel(1);
params.setRoleName("测试角色名");
params.setServerId("1");
params.setServerName("测试");
params.setVip("vip1");
GrAPI.getInstance().grPay(MainActivity.this, params);
```
