## 初始化接口（必接）

### 1 接口定义

```java
/**
* 初始化接口
* @param activity 游戏的主activity
* @param listener回调类,必传
*/
public void grInitSDK(Activity activity, GrSDKCallBack listener);
```

### 2 示例

**SDK所有的回调都统一在GrSDKCallBack 接口里面**

| onInitResult(int code)--------------------初始化回调<br />onLoginResult(GRToken authResult)---登录回调，<br />onLogoutResult(int resultCode)---------注销账号回调<br />onExit()------------------------------------退出游戏回调 |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```java
// 初始化
GrAPI.getInstance().grInitSDK(this, new GrSDKCallBack() {
     @Override
     public void onInitResult(int resultCode) {
         if (resultCode == GrCode.GR_COM_PLATFORM_SUCCESS) {
             LogUtil.d("init success");
          } else {
             LogUtil.d( "init fail");
          }
     }

     @Override
     public void onLoginResult(GRToken authResult) {
          LogUtil.d("get token success,  tokenInfo : " + authResult);
          if (authResult.isSuc()) {
              LogUtil.d( "Username:" + authResult.getUsername());
              LogUtil.d( "channelID:" + authResult.getChannelID());
              LogUtil.d( "Token:" + authResult.getToken());
              LogUtil.d("userid : " + authResult.getUserID());
         } else {
              LogUtil.d("get Token fail");
         }
     }

     @Override
     public void onLogoutResult(int resultCode) {
          LogUtil.d( "logout success");
          if (resultCode == GrCode.LOGOUT_ACCOUNT_SUCCESS) {
              GrAPI.getInstance().grLogin(MainActivity.this);
              return;
          }

     }

     @Override
      public void onPayResult(int result) {
           LogUtil.d( "onPayResult:"+result);
           if (result == GrCode.PAY_GAORE_SUCCESS) {
	       Toast.makeText(MainActivity.this, "支付成功", Toast.LENGTH_SHORT).show();
           } else if (result == GrCode.PAY_GAORE_FAILED) {
	       Toast.makeText(MainActivity.this, "支付失敗", Toast.LENGTH_SHORT).show();
           }
      }

      @Override
      public void onExit() {
          LogUtil.d( "onExit:");
          MainActivity.this.finish();
       }

       @Override
       public void onPermissionsResult(int result) {
	   if (result == GrCode.GR_REQUEST_PERMISSIONS_GRANTED) {//授权成功
	       Toast.makeText(MainActivity.this, "授权成功", Toast.LENGTH_SHORT).show();
	   }
       }

      @Override
      public void onLoginCancel() {
          Toast.makeText(MainActivity.this, "取消登入", Toast.LENGTH_SHORT).show();
      }
});
```
