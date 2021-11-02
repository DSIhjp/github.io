## Activity的生命周期（必接）

### 1 接口定义

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

### 2 示例

**研发需要在Activity的相应生命周期下添加如下方法：**

```
@Override
protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       GrAPI.getInstance().grOnCreate(savedInstanceState);
}

@Override
protected void onStart() {
       super.onStart();
       GrAPI.getInstance().grOnStart();
}

@Override
protected void onPause() {
	super.onPause();
	GrAPI.getInstance().grOnPause();
}

@Override
protected void onResume() {
	super.onResume();
	GrAPI.getInstance().grOnResume();
}

@Override
protected void onNewIntent(Intent intent) {
	super.onNewIntent(intent);
	GrAPI.getInstance().grOnNewIntent(intent);
}

@Override
protected void onStop() {
	super.onStop();
	GrAPI.getInstance().grOnStop();
}

@Override
protected void onDestroy() {
	super.onDestroy();
	GrAPI.getInstance().grOnDestroy();
}

@Override
protected void onRestart() {
	super.onRestart();
	GrAPI.getInstance().grOnRestart();
}

@Override
public void onConfigurationChanged(Configuration newConfig) {
	super.onConfigurationChanged(newConfig);
	GrAPI.getInstance().grOnConfigurationChanged(newConfig);
}

@Override
protected void onSaveInstanceState(Bundle outState) {
	super.onSaveInstanceState(outState);
	GrAPI.getInstance().grOnSaveInstanceState(outState);
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
	super.onActivityResult(requestCode, resultCode, data);
	GrAPI.getInstance().grOnActivityResult(requestCode, resultCode,data);
}
```
