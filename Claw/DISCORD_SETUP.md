# Discord 搭建步骤

为 Elena 的中文学习系统搭建 Discord，大约需要 15-20 分钟。

---

## 第一步：创建 Discord Bot

### 1.1 前往开发者控制台
打开浏览器，访问：
👉 https://discord.com/developers/applications

登录你的 Discord 账号（如果没有账号先注册一个）。

### 1.2 创建新应用
- 点击右上角 **「New Application」**
- 名称填写：`Elena的中文老师`（或你喜欢的名字）
- 勾选同意条款，点击 **「Create」**

### 1.3 创建 Bot
- 左侧菜单点击 **「Bot」**
- 点击 **「Add Bot」** → 确认 **「Yes, do it!」**
- 在 Bot 页面，找到 **「Username」**，可以改成 `中文老师` 或 `Elena的中文小助手`
- 可以上传一个头像（比如一个可爱的中文书本图标）

### 1.4 开启必要权限
在 Bot 页面，往下找到 **「Privileged Gateway Intents」**，开启以下两项：
- ✅ **MESSAGE CONTENT INTENT**（读取消息内容，必须开启）
- ✅ **SERVER MEMBERS INTENT**（管理成员，建议开启）

点击 **「Save Changes」**。

### 1.5 复制 Bot Token
- 在 Bot 页面，点击 **「Reset Token」** → 确认
- 复制显示的 Token（格式类似：`MTxxxxxx.Gxxxxx.xxxxxxxxx`）
- **妥善保存，不要分享给任何人！**
- 将 Token 填入 `.claw/channels.toml` 的 `bot_token` 字段

---

## 第二步：创建 Discord 服务器

### 2.1 新建服务器
打开 Discord 客户端（或网页版 https://discord.com/app）：
- 点击左侧栏底部的 **「+」** 按钮
- 选择 **「亲自创建」** → **「仅供我和我的朋友使用」**
- 服务器名称填写：`Elena学中文`
- 点击 **「创建」**

### 2.2 删除默认频道（可选）
默认会有 `#general` 频道，可以先留着，等配置好再删除。

---

## 第三步：创建角色

### 3.1 进入角色设置
- 点击服务器名称（左上角）→ **「服务器设置」**
- 左侧菜单选择 **「身份组」**（Roles）

### 3.2 创建 Parent 角色
- 点击 **「创建身份组」**
- 名称：`Parent`
- 颜色：选一个颜色（比如蓝色）
- 权限：保持默认（管理员权限**不要**开）
- 点击 **「保存更改」**
- 复制这个角色的 ID（开启开发者模式后右键角色 → 复制 ID）

### 3.3 创建 Child 角色
- 再次点击 **「创建身份组」**
- 名称：`Elena`
- 颜色：选一个颜色（比如粉色或绿色）
- 权限：保持默认
- 点击 **「保存更改」**
- 同样复制这个角色的 ID

### 3.4 开启开发者模式（获取 ID 必须）
- 打开 Discord **「设置」**（左下角齿轮图标）
- 左侧菜单 → **「进阶」**（Advanced）
- 开启 **「开发者模式」**

开启后，右键点击任何服务器、频道、角色、用户，都会出现「复制 ID」选项。

---

## 第四步：创建频道

### 4.1 创建学习区分类
- 右键服务器左侧空白处 → **「创建分类」**
- 名称：`📚 学习区`
- 点击 **「创建分类」**

### 4.2 创建 #chinese-practice 频道
- 右键 `📚 学习区` → **「创建频道」**
- 频道类型：**文字频道**
- 频道名称：`chinese-practice`
- 点击 **「创建频道」**

进入频道权限设置：
- 点击频道右边的齿轮图标 → **「权限」**
- 确认 `@everyone` 有读写权限（默认）
- `Elena` 角色：有读写权限 ✅
- `Parent` 角色：有读写权限 ✅

复制这个频道的 ID（右键频道 → 复制 ID），填入 `.claw/channels.toml`。

### 4.3 创建家长区分类
- 右键左侧空白处 → **「创建分类」**
- 名称：`👨‍👩‍👧 家长区`
- 点击 **「创建分类」**

**设置家长区权限（关键步骤）：**
- 点击 `👨‍👩‍👧 家长区` 旁边的齿轮图标
- 选择 **「权限」**
- 点击 **「@everyone」** → 关闭 **「查看频道」**（这样默认所有人看不到）
- 点击 **「+」** 添加 `Parent` 角色 → 开启 **「查看频道」**
- 点击 **「保存更改」**

### 4.4 创建 #parent-dashboard 频道
- 右键 `👨‍👩‍👧 家长区` → **「创建频道」**
- 频道名称：`parent-dashboard`
- 点击 **「创建频道」**
- 因为继承了分类权限，这个频道 Elena 已经看不到了 ✅

复制这个频道的 ID，填入 `.claw/channels.toml`。

---

## 第五步：邀请 Bot 进入服务器

### 5.1 生成邀请链接
回到 Discord 开发者控制台：
- 左侧菜单 → **「OAuth2」** → **「URL Generator」**
- **SCOPES** 勾选：`bot`
- **BOT PERMISSIONS** 勾选以下权限：
  - ✅ Read Messages / View Channels（查看频道）
  - ✅ Send Messages（发送消息）
  - ✅ Read Message History（读取历史消息）
  - ✅ Attach Files（发送文件）
  - ✅ Manage Messages（管理消息，用于置顶等）

### 5.2 邀请 Bot
- 复制页面底部生成的 URL
- 在浏览器打开这个 URL
- 选择你刚刚创建的服务器 `Elena学中文`
- 点击 **「授权」**
- 完成验证码

Bot 现在应该已经出现在服务器成员列表里了。

---

## 第六步：分配角色给成员

### 6.1 给自己分配 Parent 角色
- 在服务器右侧成员列表，右键点击自己的名字
- 选择 **「身份组」**
- 勾选 **「Parent」**

### 6.2 邀请 Elena 加入服务器
- 点击服务器名称 → **「邀请成员」**
- 复制邀请链接，发给 Elena
- Elena 加入后，右键她的名字 → **「身份组」** → 勾选 **「Elena」**

---

## 第七步：填写配置文件

打开 `/Users/wenwu/WorkBuddy/Claw/.claw/channels.toml`，填入你收集到的所有 ID：

```toml
[channels.discord]
bot_token = "你的Bot Token"      # 第一步复制的 Token
guild_id  = "你的服务器ID"        # 右键服务器名称 → 复制 ID

[channels.discord.child_channel]
channel_id = "chinese-practice的频道ID"

[channels.discord.parent_channel]
channel_id = "parent-dashboard的频道ID"

[channels.discord.roles.child]
role_id = "Elena角色的ID"

[channels.discord.roles.parent]
role_id = "Parent角色的ID"
```

---

## 第八步：在 Claw 中启用 Discord

1. 打开 Claw 设置
2. 进入 **「Channels」** → **「Add Channel」**
3. 选择 **「Discord」**
4. 选择配置文件路径：`.claw/channels.toml`
5. 点击 **「Connect」**
6. 如果连接成功，Bot 会在 `#chinese-practice` 发送一条欢迎消息

---

## 验证一切正常

配置完成后，做以下检查：

| 测试项 | 方法 | 预期结果 |
|--------|------|---------|
| Elena 能看到 #chinese-practice | 用 Elena 的账号登录 | ✅ 可见 |
| Elena 看不到 #parent-dashboard | 用 Elena 的账号登录 | ❌ 不可见 |
| 家长能看到两个频道 | 用家长账号登录 | ✅ 两个都可见 |
| Bot 能回复消息 | 在 #chinese-practice 发「开始学习」| Bot 有回应 |
| 提醒正常发送 | 等到下午5点（悉尼时间）| Bot 发送提醒 |

---

## 常见问题

**Q: Bot 没有回应怎么办？**
检查：1）Bot Token 是否正确；2）MESSAGE CONTENT INTENT 是否开启；3）Bot 是否已邀请进服务器

**Q: Elena 能看到家长频道怎么办？**
检查 `👨‍👩‍👧 家长区` 分类的权限设置，确认 `@everyone` 的「查看频道」是关闭的

**Q: Bot Token 泄露了怎么办？**
立刻回到开发者控制台 → Bot → 「Reset Token」，生成新的 Token，更新配置文件

**Q: 需要 Elena 有 Discord 账号吗？**
是的，她需要一个 Discord 账号。Elena 已有邮箱 elena.jy.wu@gmail.com，用这个邮箱在 https://discord.com/register 注册即可。注册时出生年份填写实际年份，Discord 会提示需要家长同意（Family Center 功能）——按提示操作，或直接跳过即可正常使用。

---

完成以上步骤后，就可以让 Elena 在 `#chinese-practice` 发送「**开始学习**」，开始她的第一次中文练习了！🎉
