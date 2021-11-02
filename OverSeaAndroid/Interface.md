# 1 接口集成

## 1.1 GrAPI类

SDK所有对外接口都定义在该类中，且所有对外接口都为静态方法，可以通过GrAPI.xxx进行调用。

## 1.2 生命周期方法（必接）

```java
GrAPI.getInstance().grOnCreate(savedInstanceState);
GrAPI.getInstance().grOnStart();
GrAPI.getInstance().grOnPause(this);
GrAPI.getInstance().grOnResume(this);
GrAPI.getInstance().grOnNewIntent(intent);
GrAPI.getInstance().grOnStop();
GrAPI.getInstance().grOnDestroy();
GrAPI.getInstance().grOnRestart();
GrAPI.getInstance().grOnConfigurationChanged(newConfig);
GrAPI.getInstance().grOnSaveInstanceState(outState);
GrAPI.getInstance().grOnActivityResult(requestCode, resultCode, data, this);
```
