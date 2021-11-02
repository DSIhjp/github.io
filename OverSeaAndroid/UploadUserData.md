## 数据上报接口（必接）

### 1 接口定义

```java
/**
 * 数据上报接口
 * @param activity 游戏的主activity
 * @param extraData 上报信息
 */
GrAPI.getInstance().grSubmitExtendData(Activity activity, GRUserExtraData extraData);
```

### 2 示例

```java
GRUserExtraData extraData = new GRUserExtraData();
extraData.setDataType(7); // 调用时机，具体见下表
extraData.setServerID(1 + ""); // 未获取到服务器时传0
extraData.setServerName("伺服器名稱"); // 未获取到服务器名称时传null
extraData.setRoleName("角色名名稱"); // 角色未获取或未创建时传null
extraData.setRoleLevel("1"); // 当前角色等级,未获取到角色等级时传null
extraData.setRoleID("123456789"); // 当前角色id,未获取角色id时传null
extraData.setMoneyNum(0 + ""); // 玩家身上元宝数量，拿不到或者未获取时传0
extraData.setRoleCreateTime(System.currentTimeMillis() / 1000);// 角色创建时间，未获取或未创建角色时传0
extraData.setGuildId("GH10001");// 公会id，无公会或未获取时传null
extraData.setGuildName("公會名稱");// 公会名称，无公会或未获取时传null
extraData.setGuildLevel(100 + "");// 公会等级，无公会或未获取时传0
extraData.setGuildLeader("公會會長名");// 公会会长名称，无公会或未获取时传null
extraData.setPower(123123); // 角色战斗力, 不能为空，必须是数字，不能为null,若无,传0
extraData.setProfessionid(123);// 职业ID，不能为空，必须为数字，若无，传入 0
extraData.setProfession("職業名稱");// 职业名称，不能为空，不能为 null，若无，传入 “无”
extraData.setGender("性别");// 角色性别，不能为空，不能为 null，可传入参数“ 男、女、无”
extraData.setProfessionroleid(123);// 职业称号ID，不能为空，不能为 null，若无，传入 0
extraData.setProfessionrolename("職業稱號");// 职业称号，不能为空，不能为 null，若无，传入“ 无”
extraData.setVip(9);// 玩家VIP等级，不能为空，必须为数字,若无，传入 0
extraData.setSignday(2);// 玩家签到天数，不能为空，必须为数字,若无，传入 0
extraData.setAchievementId("富可敵國");// 玩家解鎖成就，不能为空，不能为 null，若无，传入“ 无”
extraData.setGuildroleid(123);// 帮派称号 ID，帮派会长/帮主必传 1，其他可自定义，不能为空，不能为
// null，若无，传入 0
extraData.setGuildrolename("幫派稱號名稱");// 帮派称号名称，不能为空，不能为 null，若无，传入“无”
   
GrAPI.getInstance().grSubmitExtendData(MainActivity.this, extraData);
```

### 3 调用的时机

extraData中的dataType的值:

| dataType的值 | 时机         |
| ------------ | ------------ |
| 1            | 选择服务器   |
| 2            | 创建角色     |
| 3            | 进入游戏     |
| 4            | 等级提升     |
| 5            | 新手教程开始 |
| 6            | 新手教程结束 |
| 7            | 签到天数     |
| 8            | 获得成就     |
| 9            | 退出游戏     |

### 4 上报参数说明

| 参数               | 类型   | 含义                    | 未获取时传入 |
| ------------------ | ------ | ----------------------- | ------------ |
| dataType           | int    | 调用时机                |              |
| serverID           | int    | 服务器ID                | 0            |
| serverName         | String | 服务器名称              | null         |
| roleName           | String | 角色名字                | null         |
| roleLevel          | String | 角色等级                | null         |
| roleId             | String | 角色Id                  | null         |
| moneyNum           | int    | 角色身上游戏币数量      | 0            |
| roleCreateTime     | long   | 角色创建时间            | 0            |
| guildId            | Sting  | 角色所在公会id          | null         |
| guildName          | Sting  | 角色所在公会名称        | null         |
| guildLevel         | int    | 角色所在公会等级        | 0            |
| guildLeader        | Sting  | 角色所在公会会长        | null         |
| Power              | long   | 角色战斗力              | 0            |
| professionid       | int    | 职业ID                  | 0            |
| profession         | String | 职业名称                | “无”       |
| gender             | String | 角色性别(“男”,“女”) | “无”       |
| professionroleid   | int    | 职业称号ID              | 0            |
| professionrolename | String | 职业称号                | “无”       |
| vip                | int    | 玩家VIP等级             | 0            |
| signday            | int    | 玩家签到天数            | 0            |
| achievementId      | String | 玩家获得成就            | “无”       |
| guildroleid        | int    | 帮派称号 ID             | 0            |
| guildrolename      | String | 帮派称号名称            | “无”       |
