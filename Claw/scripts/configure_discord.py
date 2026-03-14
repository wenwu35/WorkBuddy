import os
import requests
from dotenv import load_dotenv

load_dotenv("/Users/wenwu/WorkBuddy/Claw/.env")

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = os.getenv("DISCORD_GUILD_ID")

print(
    f"🔐 Using Discord Bot Token: {'***' + DISCORD_BOT_TOKEN[-4:] if DISCORD_BOT_TOKEN else 'Not Set'}"
)
BASE_URL = "https://discord.com/api/v10"

headers = {
    "Authorization": f"Bot {DISCORD_BOT_TOKEN}",
    "Content-Type": "application/json",
}


def create_role(name, color=0):
    url = f"{BASE_URL}/guilds/{DISCORD_GUILD_ID}/roles"
    data = {"name": name, "color": color, "hoist": True}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 201:
        role = resp.json()
        print(f"✅ Created role: {name} (ID: {role['id']})")
        return role["id"]
    else:
        print(f"❌ Failed to create role {name}: {resp.status_code} - {resp.text}")
        return None


def create_category(name):
    url = f"{BASE_URL}/guilds/{DISCORD_GUILD_ID}/channels"
    data = {"name": name, "type": 4}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 201:
        cat = resp.json()
        print(f"✅ Created category: {name} (ID: {cat['id']})")
        return cat["id"]
    else:
        print(f"❌ Failed to create category {name}: {resp.status_code} - {resp.text}")
        return None


def create_channel(name, category_id, channel_type=0):
    url = f"{BASE_URL}/guilds/{DISCORD_GUILD_ID}/channels"
    data = {"name": name, "type": channel_type, "parent_id": category_id}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 201:
        ch = resp.json()
        print(f"✅ Created channel: {name} (ID: {ch['id']})")
        return ch["id"]
    else:
        print(f"❌ Failed to create channel {name}: {resp.status_code} - {resp.text}")
        return None


def set_permission_overwrites(channel_id, overwrites):
    url = f"{BASE_URL}/channels/{channel_id}/permissions"
    for overwrite in overwrites:
        resp = requests.put(url, headers=headers, json=overwrite)
        if resp.status_code == 204:
            print(f"  ✅ Permission set for {overwrite.get('id', 'everyone')}")
        else:
            print(f"  ❌ Failed to set permission: {resp.status_code} - {resp.text}")


print("🎯 Starting Discord configuration...\n")

print("1️⃣ Creating roles...")
parent_role_id = create_role("Parent", color=0x3498DB)
elena_role_id = create_role("Elena", color=0xE91E63)

everyone_role_id = "@everyone"

print("\n2️⃣ Creating categories...")
learning_cat_id = create_category("📚-学习区")
parent_cat_id = create_category("👨‍👩‍👧-家长区")

print("\n3️⃣ Creating channels...")
chinese_channel_id = create_channel("chinese-practice", learning_cat_id)
parent_channel_id = create_channel("parent-dashboard", parent_cat_id)

print("\n4️⃣ Setting permissions for #chinese-practice...")
set_permission_overwrites(
    chinese_channel_id,
    [
        {"id": everyone_role_id, "type": "role", "allow": "0", "deny": "1024"},
        {"id": elena_role_id, "type": "role", "allow": "1024", "deny": "0"},
        {"id": parent_role_id, "type": "role", "allow": "1024", "deny": "0"},
    ],
)

print("\n5️⃣ Setting permissions for #parent-dashboard...")
set_permission_overwrites(
    parent_channel_id,
    [
        {"id": everyone_role_id, "type": "role", "deny": "1024"},
        {"id": parent_role_id, "type": "role", "allow": "1024"},
    ],
)

print("\n" + "=" * 50)
print("🎉 Configuration complete!")
print("=" * 50)
print(f"\n📋 Summary:")
print(f"  Parent Role ID:   {parent_role_id}")
print(f"  Elena Role ID:   {elena_role_id}")
print(f"  Chinese Channel: {chinese_channel_id}")
print(f"  Parent Channel:  {parent_channel_id}")
print("\n⚠️  Update your .claw/channels.toml with these IDs!")
