## 常见问题

### 1 SDK初始化失败

**情况1：**

初始化sdk的Activity没有调用

GrAPI.getInstance().grOnActivityResult(requestCode, resultCode, data, this)或者
GrAPI.getInstance().grOnRequestPermissionsResult(MainActivity.this, requestCode, permissions, grantResults);

**解决：**

查看demo的MainActivity类, 接入生命周期方法
