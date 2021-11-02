# 1 集成步骤

## 1.1 导入aar包

将物料中的将gaoreSDK_***.aar拷贝至游戏工程中，同时在build.gradle配置上。

```gradle
implementation(name: 'gaoreSDK_***', ext: 'aar')
implementation'com.android.support:support-v4:28.0.0'
```

## 1.2 Application配置

### 1.2.1 自定义Application

游戏内自定义一个类继承Application类，然后在该类的相应方法调用如下代码：

```java
GrAPI.getInstance().grOnAppCreate(this);
GrAPI.getInstance().grOnAppAttachBaseContext(this, base);
GrAPI.getInstance().grOnAppConfigurationChanged(this, newConfig);
```

### 1.2.2 示例

```xml

public class GRApplication extends Application {
	private static Application instance;

	public static Application getApplication() {
		return instance;
	}

	@SuppressLint("NewApi")
	@Override
	public void onCreate() {
		super.onCreate();
		GrAPI.getInstance().grOnAppCreate(this);
		instance = this;
	}

	@Override
	public void attachBaseContext(Context base) {
		super.attachBaseContext(base);
		GrAPI.getInstance().grOnAppAttachBaseContext(this, base);
	}

	@Override
	public void onConfigurationChanged(Configuration newConfig) {
		super.onConfigurationChanged(newConfig);
		GrAPI.getInstance().grOnAppConfigurationChanged(this, newConfig);
	}
}
```



### 1.2.3 注册Application

在AndroidManifest.xml中注册

**注意：application类路径名写绝对路径，不可依赖包名**


## 1.3 混淆声明(非必接)

**Proguard****配置****(****混淆非必接，不需要可不进行混淆****)**

```
-optimizationpasses 5
-dontusemixedcaseclassnames
-dontskipnonpubliclibraryclasses
-dontpreverify
-verbose
-keepattributes Signature
-keepattributes *Annotation*,InnerClasses
-optimizations !code/simplification/arithmetic,!code/simplification/cast,!field/*,!class/merging/*
-keepattributes *Annotation*,InnerClasses,Signature,EnclosingMethod
-renamesourcefileattribute SourceFile
-keepattributes SourceFile,LineNumberTable
-dontnote android.support.**
-dontwarn android.support.**
-keep public class * extends android.support.v4.**
-keep public class * extends android.support.v7.**
-keep public class * extends android.support.annotation.**
-keep class **.R$* {*;}
-keep public class * extends android.app.Activity
-keep public class * extends android.app.Appliction
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep public class * extends android.content.ContentProvider
-keep public class * extends android.preference.Preference
-keep public class com.android.vending.licensing.ILicensingService
-keepclassmembers class * extends android.app.Activity{
    public void *(android.view.View);
}
-keepclassmembers class * {
    void *(**On*Event);
    void *(**On*Listener);
}
-keepclasseswithmembernames class * {
    native <methods>;
}
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}
-keep class * implements android.os.Parcelable {
    public static final android.os.Parcelable$Creator *;
}
-keepclassmembers class * implements java.io.Serializable {
   static final long serialVersionUID;
   private static final java.io.ObjectStreamField[]   serialPersistentFields;
   private void writeObject(java.io.ObjectOutputStream);
   private void readObject(java.io.ObjectInputStream);
   java.lang.Object writeReplace();
   java.lang.Object readResolve();
}
-keep,allowobfuscation @interface android.support.annotation.Keep
-keep @android.support.annotation.Keep class *
-keepclassmembers class * {
    @android.support.annotation.Keep *;
}

-keep class android.support.v4.**{
    public *;
}
-keep class android.support.v7.**{
    public *;
}
-dontwarn dalvik.**
-dontwarn com.gaore.**
-keep class com.gaore.** { *;}
-dontwarn com.gr.sdk.**
-keep class com.gr.sdk.** { *;}
-dontwarn org.apache.commons.net.**
-keep class org.apache.commons.net.** { *;}
-keep class org.chromium.** { *; }
-keep class aegon.chrome.** { *; }
-dontwarn aegon.chrome.**



```


![](pic/p1.png)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.jpg)![](pic/p1.png)![](pic/p1.jpg)
