##### インポート #####
from discord.ext import commands
from discord.ext import tasks
from datetime import time
from collections import Counter
import discord
import random
import asyncio
import aiohttp
import json
import os
import subprocess
import sys
import datetime
import time
import ast
import re
import zlib
import io
import execjs
import requests
import calendar
import xml.etree.ElementTree as ET
import locale;locale.setlocale(locale.LC_CTYPE, "English_United States.932")

##### 変数 #####
no = '👎'
ok = '👍'
left = '⏪'
right = '⏩'
yl = "⬅"
yr = "➡"
counts = 0
col = random.randint(0, 0xFFFFFF)
role = discord.Role
dicenum = random.randint(0, 6)
token = "YuMe'sToken"
ver = "1.9β"
release = "0.1"
status = "Beta"
updateinfos = "・コマンド追加"

##### 最初の定義 #####
bot = commands.Bot(command_prefix="y>")

##### 設定 #####
bot.remove_command('help')

bot.load_extension("jishaku")

##### 最初の処理 #####
@bot.event
async def on_ready():
    print("ログインに成功しました")
    await bot.change_presence(activity = discord.Game(name="起動しています…｜y>help｜YuMe Project"),status =discord.Status.idle)
    print(bot.user.name)
    print(bot.user.id)

    print("起動時の情報を送信しています… / Owner")
    ch = bot.get_channel(675906231394762762)
    e = discord.Embed(title="起動成功 - 詳細情報", description="起動処理が正常に終了しました。")
    e.add_field(name="バージョン情報", value=f"Ver:{ver}\nRelease:{release}\nStatus:{status}")
    e.add_field(name="更新情報", value=f"```\n{updateinfos}```")
    e.add_field(name="導入サーバー数", value=len(bot.guilds), inline=False)
    pingtime = bot.latency * 1000
    e.add_field(name="応答速度", value=pingtime)
    await ch.send(embed=e)

    print("起動時の情報を送信しています… / User")
    for ready_channel in bot.get_all_channels():
        if ready_channel.name == "yui_ready":
            e = discord.Embed(title="起動成功", description="起動処理が正常に終了しました。")
            await ready_channel.send(embed=e)
        elif ready_channel.name == "yui_advance_ready":
            e = discord.Embed(title="起動成功 - 詳細情報", description="起動処理が正常に終了しました。")
            e.add_field(name="バージョン情報", value=f"Ver:{ver}\nRelease:{release}\nStatus:{status}")
            e.add_field(name="更新情報", value=f"```\n{updateinfos}```")

    print("最終処理を実行しています…")
    await bot.change_presence(activity = discord.Game(name=f"y>help｜Ver:{ver}｜Release:{release}｜{len(bot.guilds)}Guilds & {len(bot.users)}Users｜discord.py rewrite"),status =discord.Status.online)
    print("Debug Console.")
    for allguild in bot.guilds:
        print(allguild)
    print("正常に起動しました。")
##### グローバルチャット #####
#現在無し
##### デバッグ系コード #####
@bot.command(name="eval",description="Pythonのソースを評価するよ！\n一部の人だけ使用できるね！")
async def eval_(ctx, *, cmd):
    if ctx.author.id in[584008752005513216,539787492711464960,631786733511376916,563172752555638794,561000119495819290,345342072045174795]:
        try:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            env = {
                "client": bot,
                "discord": discord,
                "commands": commands,
                "ctx": ctx,
                "__import__": __import__,
                "bot": bot,
                "_message": ctx.message,
                "_guild": ctx.guild,
                "_author": ctx.author,
                "_channel": ctx.channel,
                "_msg": ctx.message,
                "_mes": ctx.message,
                "tasks": tasks,
                "re": re,
                "os": os,
                "subprocess": subprocess,
                "asyncio": asyncio
            }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)
            await eval(f"{fn_name}()", env)
            if ctx.message is not None:await ctx.message.add_reaction("🆗")
        except Exception as e:
            await ctx.send([e])
            if ctx.message is not None:await ctx.message.add_reaction("🆖")
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)

@bot.command(aliases=["evaljs"],description="JavaScriptのソースを評価するよ！")
async def evalnode(ctx, *, code):
    cmd = code.strip("")
    default = execjs.get()
    try:
        result = default.eval(cmd)

    except Exception as er:
        e = discord.Embed(title="Eval JavaScript Code",color=ctx.author.color)
        e.add_field(name="入力",value=f'```js\n{str(cmd)}\n```',inline=False)
        e.add_field(name="出力", value=f'```js\n{str(er).replace(token,"Token(Hide)")}\n```',inline=False)
        await ctx.send(embed=e)
        try:await ctx.message.add_reaction("🆖")
        except:return
    else:
        e = discord.Embed(title="Eval JavaScript",color=ctx.author.color)
        e.add_field(name="入力",value=f'```js\n{str(cmd)}\n```',inline=False)
        e.add_field(name="出力", value=f'```js\n{str(result).replace(token,"Token(Hide)")}\n```',inline=False)
        await ctx.send(embed=e)
        try:await ctx.message.add_reaction("🆗")
        except:return
@bot.command(description="コマンドプロンプトのコマンドを実行するよ！\n製作者しか使えないね！")
async def cmd(ctx, *, command):
    try:
        if ctx.author.id == 584008752005513216:
            os.system(command)
            e = discord.Embed(title="Command", description="操作は正常に終了しました。",color=0x5dc7fc)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="Command", description="あなたはこのコマンドを実行する権限を持っていません。",color=0xff0000)
            await ctx.send(embed=e)




    except Exception as error:
        e = discord.Embed(title="Command", description=f"Error\n```\n{error}\n```",color=0xff0000)
        await ctx.send(embed=e)

@bot.command(aliases=["end","shutdown","close"],description="BOTをシャットダウンするよ！\n製作者しか使えないね！")
async def down(ctx):
    if ctx.message.author.id == 584008752005513216:
        await ctx.send(embed=discord.Embed(title="シャットダウン", description="BOTをシャットダウンするよ～！", color=ctx.author.color))
        await bot.close()
    else:
        await ctx.send(embed=discord.Embed(title="終了できないよ？", description="君霜月君なの～？", color=0xff0000))
@bot.command(aliases=["restart","run","reload"],description="BOTを再起動するよ！\n制作者しか使えないね！\n※何故か使えません。")
async def reboot(ctx):
    if ctx.message.author.id == 584008752005513216:
        e = discord.Embed(title="再起動", description="BOTを再起動するよ～！", color=ctx.author.color)
        await ctx.send(embed=e)
        os.system("python YuMe.py")
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)
@bot.command(aliases=["changeact","cact"],description="BOTのアクティビティを変更するよ！\n制作者しか使えないね！")
async def changeactivity(ctx, status):
    if ctx.message.author.id == 584008752005513216:
        await bot.change_presence(activity = discord.Game(name=f"{status}"),status=discord.Status.online)
        e = discord.Embed(title="操作成功", description=f"アクティビティを変更したよ～\n現在のアクテビティ:{status}", color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)
@bot.command(aliases=["resetact","ract"],description="アクティビティをリセットするよ！\n制作者しか使えないね！")
async def resetactivity(ctx):
    if ctx.message.author.id == 584008752005513216:
        await bot.change_presence(activity = discord.Game(name=f"y>help｜Ver:{ver}｜Release:{release}｜{len(bot.guilds)}Guilds & {len(bot.users)}Users｜discord.py rewrite"),status=discord.Status.online)
        e = discord.Embed(title="操作成功", description="アクティビティをデフォルトに戻したよ～", color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)
@bot.command(aliases=["changesto","csto"],description="BOTのステータスをオンラインにするよ！\n制作者しか使えないね！")
async def chengestatusonline(ctx):
    if ctx.message.author.id == 584008752005513216:
        await bot.change_presence(activity = discord.Game(name=f"y>help｜Ver:{ver}｜Release:{release}｜{len(bot.guilds)}Guilds & {len(bot.users)}Users｜discord.py rewrite"),status=discord.Status.online)
        e = discord.Embed(title="操作成功", description="ステータスをオンラインにしたよ～", color=0x5eff00)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)
@bot.command(aliases=["changesti","csti"],description="BOTのステータスを退席中にするよ！\n制作者しか使えないね！")
async def changestatusidle(ctx):
    if ctx.message.author.id == 584008752005513216:
        await bot.change_presence(activity = discord.Game(name=f"y>help｜Ver:{ver}｜Release:{release}｜{len(bot.guilds)}Guilds & {len(bot.users)}Users｜discord.py rewrite"),status=discord.Status.idle)
        e = discord.Embed(title="操作成功", description="ステータスを退席中にしたよ～", color=0xff9500)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)
@bot.command(aliases=["changestd","cstd"],description="BOTのステータスを取り込み中にするよ！\n制作者しか使えないね！")
async def changestatusdnd(ctx):
    if ctx.message.author.id == 584008752005513216:
        await bot.change_presence(activity = discord.Game(name=f"y>help｜Ver:{ver}｜Release:{release}｜{len(bot.guilds)}Guilds & {len(bot.users)}Users｜discord.py rewrite"),status=discord.Status.dnd)
        e = discord.Embed(title="操作成功", description="ステータスを取り込み中にしたよ～", color=0xff0000)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー", description="あなたはこのコマンドを実行する権限を持っていません", color=ctx.author.color)
        await ctx.send(embed=e)

##### BAN&KICK #####
@bot.command(description="指定したユーザーをBANするよ！\nユーザーをKICK出来る人のみ！")
async def kick(ctx, user: discord.User=None):
    no = '👎'
    ok = '👍'
    if ctx.guild.get_member(user.id).top_role < ctx.author.top_role and ctx.author.guild_permissions.kick_members:
        if user is None:
            e = discord.Embed(title="実行エラー",description="名前を指定してね～",color=0xff0000)
            await ctx.send(embed=e)
        else:
            embeds = discord.Embed(
                title=f"**「@{user.name}」KICKしちゃう？**",color=0xC41415)
            msg = await ctx.send(embed=embeds)
            await msg.add_reaction(no)
            await msg.add_reaction(ok)
            try:
                def predicate1(message,author):
                    def check(reaction,users):
                        if reaction.message.id != message.id or users == ctx.bot.user or author != users:
                            return False
                        if reaction.emoji == ok or reaction.emoji == no:
                            return True
                        return False
                    return check
                react = await ctx.bot.wait_for('reaction_add',timeout=20,check=predicate1(msg,ctx.message.author))
                if react[0].emoji == ok:
                    await ctx.guild.kick(user)
                    print(f"{user.name}が{ctx.message.author.name}によってKICKされたよ～。")
                    embed = discord.Embed(title=f"{user.name}はKICKされたよ～。",color=0xC41415)
                    embed.add_field(name="-------------------------", value=f"名前: **{user.name}**\nID: **{user.id}**", inline=False)

                    return await ctx.send(embed=embed)
                elif react[0].emoji == no:
                    embeds = discord.Embed(
                        title=f"{user.name}はKICKされなかったよ～。",color=0x10cfee)
                    return await ctx.send(embed=embeds)
            except asyncio.TimeoutError:
                embeds = discord.Embed(
                    title=f"{user.name}はKICKされなかったよ～。",color=0x10cfee)
                return await ctx.send(embed=embeds)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(description="指定したユーザーをBANするよ！\nユーザーをBAN出来る人のみ！")
async def ban(ctx, user: discord.User=None):
    no = '👎'
    ok = '👍'
    if ctx.guild.get_member(user.id).top_role < ctx.author.top_role and ctx.author.guild_permissions.ban_members:
        if user is None:
            e = discord.Embed(title="実行エラー",description="名前を指定してね～",color=0xff0000)
            await ctx.send(embed=e)
        else:
            embeds = discord.Embed(
                title=f"**「@{user.name}」BANしちゃう？**",color=0xC41415)
            msg = await ctx.send(embed=embeds)
            await msg.add_reaction(no)
            await msg.add_reaction(ok)
            try:
                def predicate1(message,author):
                    def check(reaction,users):
                        if reaction.message.id != message.id or users == ctx.bot.user or author != users:
                            return False
                        if reaction.emoji == ok or reaction.emoji == no:
                            return True
                        return False
                    return check
                react = await ctx.bot.wait_for('reaction_add',timeout=20,check=predicate1(msg,ctx.message.author))
                if react[0].emoji == ok:
                    await ctx.guild.ban(user)
                    print(f"{user.name}が{ctx.message.author.name}によってBANされたよ～。")
                    embed = discord.Embed(title=f"{user.name}はBANされたよ～。",color=0xC41415)
                    embed.add_field(name="-------------------------", value=f"名前: **{user.name}**\nID: **{user.id}**", inline=False)

                    return await ctx.send(embed=embed)
                elif react[0].emoji == no:
                    embeds = discord.Embed(
                        title=f"{user.name}はBANされなかったよ～。",color=0x10cfee)
                    return await ctx.send(embed=embeds)
            except asyncio.TimeoutError:
                embeds = discord.Embed(
                    title=f"{user.name}はBANされなかったよ～。",color=0x10cfee)
                return await ctx.send(embed=embeds)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)

##### 役職系コード #####
@bot.command(aliases=["radd"],description="指定したユーザーに役職を付与するよ！\n役職を管理できる人のみ！")
async def roleadd(ctx, member: discord.Member, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await member.add_roles(role)
        e = discord.Embed(title="操作成功", description=f'{member.mention}さんに{role.mention}を付与したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["rre"],description="指定したユーザーから役職を削除するよ！\n役職を管理できる人のみ！")
async def roleremove(ctx, member: discord.Member, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await member.remove_roles(role)
        e = discord.Embed(title="操作成功", description=f'{member.mention}さんから{role.mention}を剥奪したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["rdel"],description="役職を削除するよ！\n役職を管理できる人のみ！")
async def roledelete(ctx, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await role.delete()
        e = discord.Embed(title="操作成功", description=f'{role.name}を削除したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["rcr"],description="役職を作成するよ！\n役職を管理できる人のみ！")
async def rolecreate(ctx, rolename):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        role = await ctx.guild.create_role(name=rolename)
        e = discord.Embed(title="操作成功", description=f'{role.mention}を作成したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私は役職を作成する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["rusers","ru"],description="役職を持つメンバー一覧を表示するよ！")
async def roleusers(ctx,role:discord.Role):
    e = discord.Embed(title=f"{role}を持つメンバー一覧",description=f"{role.members}",color=ctx.author.color)
    await ctx.send(embed=e)
@bot.command(aliases=["rcol"],description="役職の色を変更するよ！\n役職を管理できる人のみ！\n※未実装")
async def rolecolor(ctx,role:discord.Role,color):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await role.edit(color)
        e = discord.Embed(title="操作成功", description=f'{role.mention}の色を変更したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私は役職の色を変更する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["roleallmemadd","rama"],description="指定した役職を全メンバーに付与するよ！\n役職を管理できる人のみ！\n※BOT含む")
async def roleallmembersadd(ctx, role:discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        embed = discord.Embed(title="操作開始", description=f"全員に{role}を付与するよ～", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=ctx.author.name)
        await ctx.send(embed=embed)
        [await member.add_roles(role) for member in ctx.guild.members]
        embed = discord.Embed(title="操作成功", description=f"{role}を全員に付与したよ～", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=ctx.author.name)
        await ctx.send(embed=embed)   
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["roleallmemremove","roleallmemr","ramr"],description="指定した役職を全メンバーから削除するよ！\n役職を管理できる人のみ！\n※BOT含む")
async def roleallmembersremove(ctx, role:discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        embed = discord.Embed(title="操作開始", description=f"全員から{role}を剥奪するよ～", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=ctx.author.name)
        await ctx.send(embed=embed)
        [await member.remove_roles(role) for member in ctx.guild.members]
        embed = discord.Embed(title="操作成功", description=f"{role}を全員から剥奪したよ～", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=ctx.author.name)
        await ctx.send(embed=embed)
    else:
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
##### チャンネル&カテゴリー系コード #####
@bot.command(aliases=["textchannelcr","textchcr","tchc"],description="指定した名前のテキストチャンネルを作成するよ！\nチャンネルを管理できる人のみ！")
async def textchannelcreate(ctx,channel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        channel = await ctx.channel.category.create_text_channel(name=channel)
        e = discord.Embed(title="操作成功", description=f'テキストチャンネル:{channel.mention}を作成したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はチャンネルを作成する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["textchanneldel","textchdel","tchd"],description="指定した名前のチャンネルを削除するよ！\nチャンネルを管理できる人のみ！")
async def textchanneldelete(ctx,channel:discord.TextChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await channel.delete()
        e = discord.Embed(title="操作成功", description=f'テキストチャンネル:{channel.name}を削除したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はチャンネルを削除する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["voicechannelcr","voicechcr","vchc"],description="指定した名前のボイスチャンネルを作成するよ！\nチャンネルを管理できる人のみ！")
async def voicechannelcreate(ctx,channel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        channel = await ctx.channel.category.create_voice_channel(name=channel)
        e = discord.Embed(title="操作成功", description=f'ボイスチャンネル:{channel.name}を作成したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はチャンネルを作成する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["voicechanneldel","voicechdel","vchd"],description="指定した名前のボイスチャンネルを作成するよ！\nチャンネルを管理できる人のみ！")
async def voicechanneldelete(ctx,channel:discord.VoiceChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await channel.delete()
        e = discord.Embed(title="操作成功", description=f'ボイスチャンネル:{channel.name}を削除したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はチャンネルを削除する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["categorycr","ctc"],description="指定した名前のカテゴリーを作成するよ！\nチャンネルを管理できる人のみ！")
async def categorycreate(ctx,category):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        category = await ctx.guild.create_category(name=category)
        e = discord.Embed(title="操作成功", description=f'カテゴリー:{category}を作成したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はカテゴリーを作成する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["categorydel","ctd"],description="指定した名前のカテゴリーを削除するよ！\nチャンネルを管理できる人のみ！")
async def categorydelete(ctx,category:discord.CategoryChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await category.delete()
        e = discord.Embed(title="操作成功", description=f'カテゴリー:{category}を削除したよ～',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はカテゴリーを削除する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["chedit","che"],description="コマンドを実行したチャンネル名を変更するよ！\nチャンネルを管理できる人のみ！")
async def channeledit(ctx,channelname):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channelss) or ctx.guild.owner == ctx.author:
        await ctx.channel.edit(name=f"{channelname}")
        e = discord.Embed(title="操作成功", description=f'チャンネル名を変更したよ～\n現在のチャンネル名:{channelname}',color=ctx.author.color)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title="実行エラー",description="私はチャンネル名を変更する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
##### メッセージ系コード #####
@bot.command(aliases=["cl","clean","purge","pu"],description="指定した件数のメッセージを削除するよ！\nメッセージを管理できる人のみ！")
async def clear(ctx, num:int):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_messages) or ctx.guild.owner == ctx.author:
        try:
            await ctx.channel.purge(limit=num)
            e = discord.Embed(title="メッセージ削除", description=f"{num}件のメッセージを削除したよ～",color=ctx.author.color)
            l = await ctx.send(embed=e)
            await asyncio.sleep(3)
            await l.delete()
        except IndexError:
            e = discord.Embed(title="メッセージ削除", description="引数が不正です。",color=0xff0000)
            await ctx.send(embed=e)
    else:
        e= discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["acl","allclean","allpurge","apu"],description="チャンネル内のメッセージを全て削除するよ！\nメッセージを管理できる人のみ！\n※誤爆注意")
async def allclear(ctx):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_messages) or ctx.guild.owner == ctx.author:
        await ctx.channel.purge(limit=999999999999999999999999999999999)
        e = discord.Embed(title="全メッセージ削除", description=f"チャンネルのメッセージを全て削除したよ～",color=ctx.author.color)
        l = await ctx.send(embed=e)
        await asyncio.sleep(3)
        await l.delete()
    else:
        e= discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await ctx.send(embed=e)
@bot.command(aliases=["messagehis","mhis"],description="指定した数のメッセージの履歴を表示するよ！")
async def messagehistory(ctx, num:int):
    async for i in ctx.channel.history(limit=num):
        await ctx.send(f"{i.author.name}#{i.author.discriminator}: {i.content}")
##### 情報系コード #####
@bot.command(description="BOTの情報を表示するよ！\n※`userinfo`とは異なるよ！")
async def info(ctx):
    supporters = [345342072045174795,586157827400400907,631786733511376916,561000119495819290]
    fist = discord.Embed(title="「結芽/ゆめ」の情報", description=f"製作者:{bot.get_user(584008752005513216).name}\nDiscord ADMIN Bot\ndiscord.py",color=ctx.author.color)
    fist.set_thumbnail(url=ctx.bot.user.avatar_url)
    e1 = discord.Embed(title="「結芽/ゆめ」の情報 - Info", color=ctx.author.color)
    e1.set_thumbnail(url=ctx.bot.user.avatar_url)
    e1.add_field(name="サポーター",value="\n".join(bot.get_user(s).name for s in supporters), inline=False)
    e1.add_field(name="導入サーバー数", value=f"{len(bot.guilds)}", inline=False)
    e1.add_field(name="利用ユーザー数", value=f"{len(bot.users)}", inline=False)
    e2 = discord.Embed(title="「結芽/ゆめ」の情報 - System", color=ctx.author.color)
    e2.set_thumbnail(url=ctx.bot.user.avatar_url)
    e2.add_field(name="言語", value="Python", inline=False)
    e2.add_field(name="バージョン情報", value=f"Ver:{ver}\nRelese:{release}\nStatus:{status}", inline=False)
    e2.add_field(name="現在合計コマンド数", value=f"{len(bot.commands)}", inline=False)
    e3 = discord.Embed(title="「結芽/ゆめ」の情報 - URL", color=ctx.author.color)
    e3.set_thumbnail(url=ctx.bot.user.avatar_url)
    e3.add_field(name="BOTを導入する", value=f"[結芽を導入](https://discordapp.com/api/oauth2/authorize?client_id=657936162966601740&permissions=8&scope=bot)｜[参照BOT「{bot.get_user(641121614129266729).name}」](https://discordapp.com/oauth2/authorize?client_id=641121614129266729&permissions=2146958847&scope=bot)｜[{bot.get_user(553841194699063319).name}](https://discordapp.com/oauth2/authorize?client_id=553841194699063319&scope=bot&permissions=775286087)", inline=False)
    e3.add_field(name="参考サイト", value="[APIリファレンス](https://discordpy.readthedocs.io/en/latest/api.html)｜[Python-izm 基礎編](https://www.python-izm.com/basic/)", inline=False)
    page_count = 0 #ヘルプの現在表示しているページ数
    page_content_list = [fist, e1, e2, e3] #ヘルプの各ページ内容
    send_message = await ctx.send(embed=page_content_list[0]) #最初のページ投稿
    await send_message.add_reaction("➡")

    def help_react_check(reaction,user):
        emoji = str(reaction.emoji)
        if reaction.message.id != send_message.id:
            return 0
        if emoji == "➡" or emoji == "⬅":
            if user != ctx.author:
                return 0
            else:
                return 1
    while not bot.is_closed():
        try:
            reaction,user = await bot.wait_for('reaction_add',check=help_react_check,timeout=20.0)
        except asyncio.TimeoutError:
            await send_message.clear_reactions()
            await send_message.add_reaction("❌")
            return #時間制限が来たら、それ以降は処理しない
        else:
            emoji = str(reaction.emoji)
            if emoji == "➡":
                page_count += 1
            if emoji == "⬅":
                page_count -= 1
            await send_message.clear_reactions() #事前に消去する
            await send_message.edit(embed=page_content_list[page_count])

            if page_count == 0:
                await send_message.add_reaction("➡")

            if page_count == 1:
                await send_message.add_reaction("⬅")
                await send_message.add_reaction("➡")

            if page_count == 2:
                await send_message.add_reaction("⬅")
                await send_message.add_reaction("➡")

            if page_count == 3:
                await send_message.add_reaction("⬅")

            if page_count == 4:
                await send_message.add_reaction("⬅")

@bot.command(aliases=["rolei","ri"],description="指定した役職の情報を表示するよ！\n※役職IDでやるのがいいよ！")
async def roleinfo(ctx, role:discord.Role):
    e = discord.Embed(title=f"役職情報 - {role.name}", description="",color=ctx.author.color)
    e.add_field(name="名前", value=role.name)
    e.add_field(name="ID", value=role.id)
    e.add_field(name="所属サーバー", value=role.guild.name+f"({role.guild.id})")
    e.add_field(name="他のメンバーと別に表示するか？", value=role.hoist)
    e.add_field(name="その他サービスによって管理されているか？", value=role.managed)
    e.add_field(name="メンション可能か？", value=role.mentionable)
    e.add_field(name="役職順位(一番下を0としたとき)", value=role.position)
    e.add_field(name="役職の色", value=role.color)
    e.add_field(name="役職作成日(UTC)", value=role.created_at)
    e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
    await ctx.send(embed=e)
@bot.command(aliases=["chinfo","chi","ci"],description="指定したチャンネルの情報を表示するよ！")
async def channelinfo(ctx, channelid=None):
        if channelid == None:
            e = discord.Embed(title="チャンネル情報")
            e.add_field(name="チャンネル名", value=ctx.channel.name)
            e.add_field(name="チャンネルID", value=ctx.channel.id)
            e.add_field(name="所属サーバー", value=ctx.channel.guild.name+f"({ctx.channel.guild.id})")
            e.add_field(name="トピック", value=ctx.channel.topic)
            e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
            await ctx.send(embed=e)

        else:
            try:
                await bot.wait_until_ready()
                channel = bot.get_channel(channelid)

                e = discord.Embed(title="チャンネル情報", description="")
                e.add_field(name="チャンネル名", value=channel.name)
                e.add_field(name="チャンネルID", value=channel.id)
                e.add_field(name="所属サーバー", value=channel.guild.name+f"({channel.guild.id})")
                e.add_field(name="トピック", value=channel.topic)
                e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
                await ctx.send(embed=e)
            except Exception:
                try:
                    await bot.wait_until_ready()
                    channel = await bot.fetch_channel(channelid)

                    e = discord.Embed(title="チャンネル情報", description="")
                    e.add_field(name="チャンネル名", value=channel.name)
                    e.add_field(name="チャンネルID", value=channel.id)
                    e.add_field(name="所属サーバー", value=channel.guild.name+f"({channel.guild.id})")
                    e.add_field(name="トピック", value=channel.topic)
                    e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
                    await ctx.send(embed=e)

                except discord.NotFound:
                    e = discord.Embed(title="チャンネル情報", description="指定されたチャンネルは存在しません。")
                    await ctx.send(embed=e)

                except discord.Forbidden:
                    e = discord.Embed(title="チャンネル情報", description="指定されたチャンネルへアクセスできませんでした。")
                    await ctx.send(embed=e)
@bot.command(aliases=["userse","use"],description="指定したユーザーの情報を表示するよ！\nサーバーに居ない人の情報も検索できるね！\nでもID限定、表示できる情報がuserinfoより少ないよ")
async def userserch(ctx, user_id=""):
    try:user = await bot.fetch_user(int(user_id))
    except:await ctx.send(embed=discord.Embed(description="ユーザーが見つかりませんでした…。",color=ctx.author.color))
    else:
        member = discord.utils.get(bot.get_all_members(),id=int(user_id))
        g_m = discord.utils.get(ctx.guild.members, id=int(user_id))
        embed = discord.Embed(title=f"ユーザーサーチ - {user.name}",color=col)
        embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前#タグ",value=f"{user}", inline=False)
        embed.add_field(name="ID",value=f"{user.id}", inline=False)
        embed.add_field(name="BOT?",value={"True":"はい","False":"いいえ"}.get(str(user.bot)))
        if g_m is not None:embed.add_field(name="サーバー上の名前",value=f"{member.nick}", inline=False)
        if member is not None:
            if member.activity != None:embed.add_field(name="アクティビティ", value=member.activity, inline=False)
            embed.add_field(name="ステータス",value={"online":"オンライン","idle":"退席中","dnd":"取り込み中","offline":"オフライン"}.get(str(member.status)), inline=False)
            embed.add_field(name="アカウント作成日",value=f"{user.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
            await ctx.send(embed=embed)
@bot.command(aliases=["useri","ui"],description="指定したユーザーの情報を表示するよ！")
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title=f"ユーザー情報 - {user.name}",color=ctx.author.color)
    embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
    embed.add_field(name="名前#タグ",value=f"{user}")
    embed.add_field(name="ID",value=f"{user.id}")
    embed.add_field(name="ステータス",value={"online":"オンライン","idle":"退席中","dnd":"取り込み中","offline":"オフライン"}.get(str(user.status)))
    embed.add_field(name="BOT?",value={"True":"はい","False":"いいえ"}.get(str(user.bot)))
    if user.activity != None:embed.add_field(name="アクティビティ", value=user.activity.name)
    if user.activity != None:embed.add_field(name="サーバー上の名前", value=user.nick)
    embed.add_field(name="サーバー参加時間",value=f"{user.joined_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
    embed.add_field(name="アカウント作成日",value=f"{user.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
    embed.add_field(name="権限",value=f'`{",".join([row[0] for row in list(user.guild_permissions) if row[1]])}`', inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")

    await ctx.send(embed=embed)

@bot.command(aliases=["serveri","si"],description="指定したサーバーの情報を表示するよ！\n※サーバーIDでやってね！")
async def serverinfo(ctx,guild_id=None):
    ch_tcount =len(guild.text_channels)
    ch_vcount =len(guild.voice_channels)
    ch_count =len(guild.channels)
    kt_count =len(guild.categories)
    guild = discord.utils.get(bot.guilds,id=int(guild_id))
    embed = discord.Embed(title=f"サーバー情報 - {guild.name}",color=ctx.author.color)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="名前",value=f"{guild.name}",inline=False)
    embed.add_field(name="ID",value=f"{guild.id}",inline=False)
    embed.add_field(name="サーバー地域",value=f"{guild.region}",inline=False)
    embed.add_field(name="作成日",value=f"{guild.created_at}",inline=False)
    embed.add_field(name="オーナー",value=f"{guild.owner.name}",inline=False)
    embed.add_field(name="テキストチャンネル数",value=f"{ch_tcount}")
    embed.add_field(name="ボイスチャンネル数",value=f"{ch_vcount}")
    embed.add_field(name="カテゴリー数",value=f"{kt_count}")
    embed.add_field(name="合計チャンネル数(カテゴリー含む)",value=f"{ch_count}")
    embed.add_field(name="サーバー承認レベル",value=f"{guild.mfa_level}")
    embed.add_field(name="サーバー検証レベル",value=f"{guild.verification_level}")
    embed.add_field(name="サーバーブーストレベル",value=f"{guild.premium_tier}")
    embed.add_field(name="サーバーをブーストしたユーザー数",value=f"{guild.premium_subscription_count}")
    embed.add_field(name="サーバーは大きい？",value=f"{guild.large}")
    embed.set_footer(text="サーバー大きさ基準:250人以上")

    await ctx.send(embed=embed)
@bot.command(aliases=["joinserverl","joins"],description="Botが導入されているサーバーを表示するよ！")
async def joinserverlist(ctx):
    await ctx.send(embed=discord.Embed(description=",".join([guild.name for guild in bot.guilds])))
##### 一般ユーザー系コマンド #####
@bot.command(description="BOTの反応速度を測定するよ！")
async def ping(ctx):
    before = time.monotonic()

    msg = await ctx.send(
         embed=discord.Embed(
            title="結芽BOTの反応速度", description="計測中・・・", color=0x0080FF
        )
    )

    return await msg.edit(
        embed=discord.Embed(
            title="結芽BOTの反応速度", description=f"Ping:`{int((time.monotonic() - before) * 1000)}ms`\nWebSocket:`{round(ctx.bot.latency * 1000, 2)}ms`", color=ctx.author.color
        )
    )
##### メッセージ #####
@bot.command(description="指定したユーザーに結芽からDMを送信するよ！")
async def senddm(ctx, userid, title, desc):
    try:
        user = await bot.fetch_user(userid)
        e = discord.Embed(title=title, description=desc)
        e.set_author(name=ctx.author.name)
        await user.send(embed=e)

        c = discord.Embed(title="Senddm", description=f"{user.mention}にDMを送信しました。")
        await ctx.send(embed=c)

    except discord.NotFound:
        e = discord.Embed(title="Senddm", description="指定されたユーザーは存在しません")
    
    except discord.Forbidden:
        e = discord.Embed(title="Senddm", description="指定されたユーザーにDMを送信できませんでした。")
        await ctx.send(embed=e)
@bot.command(description="指定した文章を送信するよ！")
async def say(ctx, message=""):
    await ctx.send(message)
    await ctx.message.delete()
@bot.command(description="指定したチャンネルに文章を送信するよ！")
async def send(ctx, ch:discord.TextChannel, txt):
    try:
        await ch.send(txt)

        e = discord.Embed(title="Send", description=f"{ch.mention}に{txt}を送信しました。")
        await ctx.send(embed=e)

    except discord.NotFound:
        e = discord.Embed(title="Send", description="指定されたチャンネルが存在しません")
        await ctx.send(embed=e)
    except discord.Forbidden:
        e = discord.Embed(title="Send", description="指定されたチャンネルにアクセスできません")
        await ctx.send(embed=e)
##### 計算 #####
@bot.command(description="足し算をするよ！")
async def plus(ctx, tasi1, tasi2):
    keisantyuu1 = int(tasi1)
    keisantyuu2 = int(tasi2)
    kekkadayo = keisantyuu1 + keisantyuu2
    await ctx.send(kekkadayo)
@bot.command(description="引き算をするよ！")
async def minus(ctx, tasi1, tasi2):
    keisantyuu1 = int(tasi1)
    keisantyuu2 = int(tasi2)
    kekkadayo = keisantyuu1 - keisantyuu2
    await ctx.send(kekkadayo)
@bot.command(description="割り算をするよ！")
async def dby(ctx, tasi1, tasi2):
    keisantyuu1 = int(tasi1)
    keisantyuu2 = int(tasi2)
    kekkadayo = keisantyuu1 / keisantyuu2
    await ctx.send(kekkadayo)
@bot.command(description="掛け算をするよ！")
async def times(ctx, tasi1, tasi2):
    keisantyuu1 = int(tasi1)
    keisantyuu2 = int(tasi2)
    kekkadayo = keisantyuu1 * keisantyuu2
    await ctx.send(kekkadayo)
    
##### 遊び #####
@bot.command(aliases=["mkembed"],description="embed(埋め込み表示)を作成するよ！")
async def makeembed(ctx, title, *, word):
    e = discord.Embed(title=title, description=word, color=ctx.author.color)
    await ctx.send(embed=e)
@bot.command(aliases=["randomnum","rnum"],description="ランダムな数(乱数)を出すよ！")
async def randomnumber(ctx, startnum:int, endnum:int):
    randomnumgen = random.randint(startnum, endnum)
    await ctx.send(randomnumgen)
@bot.command(description="サイコロを振るよ！")
async def dice(ctx):
    dicenum = random.randint(0, 6)
    await ctx.send(dicenum)
@bot.command(name="time",description="現在時刻を表示するよ！")
async def time_(ctx):
    import locale
    locale.setlocale(locale.LC_CTYPE, "English_United States.932")
    await ctx.send(datetime.datetime.now().strftime("%Y年%m月%d日 %H時%M分%S秒"))
@bot.command(description="おみくじを引くよ！")
async def omikuji(ctx):
    embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの今日の運勢は！\nｼﾞｬｶｼﾞｬｶｼﾞｬｶｼﾞｬｶｼﾞｬｶ…ｼﾞｬﾝ!",color=0x5dc7fc)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="[運勢] ", value=random.choice(('福沢諭吉\nお～！福沢ゆきｔ・・・え？(笑)','大吉！\nすごいね！大吉だよ？！', '吉\nいいね～！', '凶\nそんなこともあるさ！', '大凶\nあ、ありゃりゃ・・・')), inline=False)
    await ctx.send(embed=embed)
@bot.command(aliases=["vote"],description="投票を作成するよ！")
async def poll(ctx,*content):
    if len(content) == 1:
        msg = await ctx.send(content[:1][0])
        [await msg.add_reaction(emoji) for emoji in ["👍","👎"]]
    elif len(content) > 1:
        title = content[:1][0]
        answers = content[1:]
        emojis = [chr(127462 + i) for i in range(len(answers))]
        answer = "\n".join(emoji + answer for emoji,answer in zip(emojis,answers))
        col = random.randint(0, 0xFFFFFF)
        embed = discord.Embed(title=title,description=answer,color=col,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=ctx.author.name)
        msg = await ctx.send(embed=embed)
        [await msg.add_reaction(emoji) for emoji in emojis]
##### 報告 #####
@bot.command(description="BOTの感想を送るよ！")
async def feedback(ctx, text):
    await bot.wait_until_ready()
    ch = bot.get_channel(675971969816068107)
    r = discord.Embed(title="FeedBack", description=text)
    r.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} / {ctx.author.id}", icon_url=ctx.author.avatar_url)
    await ch.send(embed=r)


    e = discord.Embed(title="FeedBack", description="Botの感想を送信しました！ご利用ありがとうございます！", color=ctx.author.color)
    await ctx.send(embed=e)

@bot.command(description="BOTのバグを報告するよ！")
async def report(ctx, text):
    await bot.wait_until_ready()
    ch = bot.get_channel(675972021166931968)
    r = discord.Embed(title="Report", description=text)
    r.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} / {ctx.author.id}", icon_url=ctx.author.avatar_url)
    await ch.send(embed=r)

    e = discord.Embed(title="Report", description="Botのバグを報告しました。", color=ctx.author.color)
    await ctx.send(embed=e)

@bot.command(description="BOTのリクエストを送るよ！")
async def request(ctx, text):
    await bot.wait_until_ready()
    ch = bot.get_channel(675972112636444682)
    r = discord.Embed(title="Request", description=text)
    r.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} / {ctx.author.id}", icon_url=ctx.author.avatar_url)
    await ch.send(embed=r)

    e = discord.Embed(title="Request", description="リクエストを送信しました。Botの開発者が詳細を訪ねるため、DMに行く可能性があります。", color=ctx.author.color)
    await ctx.send(embed=e)

##### ログ #####
@bot.event
async def on_member_join(member):
    ch = bot.get_channel(675930097328324667)
    e = discord.Embed(title="入室",description=f"{member}さんが、{member.guild}に参加しました。",color=col,timestamp=datetime.datetime.utcnow())
    e.set_thumbnail(url=f'{member.avatar_url_as(static_format="png")}')
    await ch.send(embed=e)
    print(f'{member}さんが{member.guild}に参加しました。')
@bot.event
async def on_member_remove(member):
    ch = bot.get_channel(675930097328324667)
    e = discord.Embed(title="退出",description=f"{member}さんが、{member.guild}から退出しました。",color=col,timestamp=datetime.datetime.utcnow())
    e.set_thumbnail(url=f'{member.avatar_url_as(static_format="png")}')
    await ch.send(embed=e)
    print(f'{member}さんが{member.guild}から退出しました。')

##### エラー系コード #####
@bot.event
async def on_command_error(context,exception):
    if isinstance(exception, commands.CommandNotFound):
        word = context.message.content.split(" ")[0].strip("y>")
        des = ",".join(c.name for c in bot.commands if word in c.name or c.name in word)
        embed = discord.Embed(title="コマンドエラー",description=f"{context.author.name}さん！`{context.message.content}`っていうコマンドは無いよ！\n`y>help`で確認してね！\nもしかして:`{des}`", color=0xff0000)
        await context.send(embed=embed)
    elif isinstance(exception, commands.MissingRequiredArgument):
        e = discord.Embed(title="コマンドエラー",description="パラメーターが不足してるみたい・・・", color=0xff0000)
        await context.send(embed=e)
    elif isinstance(exception,commands.NotOwner):
        e = discord.Embed(title="実行エラー",description="君はコマンドを実行する権限を持ってないよ～",color=0xff0000)
        await context.send(embed=e)
    else:
        e = discord.Embed(title="‼Exception Occurred‼", description=f"例外が発生しました。\n```{exception}```\n", color=0xff0000)
        print (f"{exception}")
        await context.send(embed=e)
        ch = 684612890489257984
        embed = discord.Embed(title="エラー情報", description=f"\n```{exception}```", color=0xff0000)
        embed.add_field(name="発生サーバー名", value=context.guild.name)
        embed.add_field(name="発生ユーザー名", value=context.author.name)
        embed.add_field(name="発生コマンド", value=context.message.content)
        await bot.get_channel(ch).send(embed=embed)
##### その他のコード #####
@bot.command(description="最近の地震情報を表示するよ！")
async def jishin(ctx):
    er = e()
    embed = discord.Embed(title='**地震情報**', description='', color=er['color'])
    embed.set_thumbnail(url=er['icon'])
    embed.add_field(name='発生時刻', value=er['time'], inline=True)
    embed.add_field(name='震源地', value=er['epicenter'], inline=True)
    embed.add_field(name='最大震度', value=er['intensity'], inline=True)
    embed.add_field(name='マグニチュード', value=er['magnitude'], inline=True)
    embed.add_field(name='震度1以上を観測した地域', value=er['e_1'], inline=False)
    embed.set_image(url=er['map'])
    await ctx.channel.send(embed=embed)
def e():
    xml_data_module = requests.get('https://www3.nhk.or.jp/sokuho/jishin/data/JishinReport.xml')
    xml_data_module.encoding = "Shift_JIS"
    root = ET.fromstring(xml_data_module.text)
    for item in root.iter('item'):
       deta_url = (item.attrib['url'])
       break
    deta = requests.get(deta_url)
    deta.encoding = "Shift_JIS"
    root = ET.fromstring(deta.text)
    e_1 = ''
    for Earthquake in root.iter('Earthquake'):
        time = (Earthquake.attrib['Time'])
        Intensity = (Earthquake.attrib['Intensity'])
        Epicenter = (Earthquake.attrib['Epicenter'])
        Magnitude = (Earthquake.attrib['Magnitude'])
        Depth = (Earthquake.attrib['Depth'])
        map_url = 'https://www3.nhk.or.jp/sokuho/jishin/'
        count = 1
    for Area in root.iter('Area'):
        e_1 += '\n' + Area.attrib['Name']
        if count == 10:
            e_1 += '\n他'
            break
        count = count + 1
    for Detail in root.iter('Detail'):
        map = map_url + Detail.text
        edic = {'time': time, 'epicenter': Epicenter, "intensity": Intensity, "depth": Depth, "magnitude": Magnitude, "map": map, "icon": eicon(Intensity), "color": eicolor(Intensity), 'e_1': e_1}
        return edic
def eicon(i):
    if i == '1':
        return('https://i.imgur.com/yalXlue.png')
    elif i == '2':
        return('https://i.imgur.com/zPSFvj6.png')
    elif i == '3':
        return('https://i.imgur.com/1DVoItF.png')
    elif i == '4':
        return("https://i.imgur.com/NqC3CE0.png")
    elif i == '5-':
        return("https://i.imgur.com/UlFLa3G.png")
    elif i == '5+':
        return("https://i.imgur.com/hExQwf2.png")
    elif i == '6-':
        return("https://i.imgur.com/p9RrO96.png")
    elif i == '6+':
        return("https://i.imgur.com/pNaFJ2Y.png")
    elif i == '7':
        return("https://i.imgur.com/ZoOhL4v.png")
def eicolor(i):
    if i == '1':
        return(0x51b3fc)
    elif i == '2':
        return(0x7dd45a)
    elif i == '3':
        return(0xf0ed7e)
    elif i == '4':
        return(0xfa782c)
    elif i == '5-':
        return(0xb30f20)
    elif i == '5+':
        return(0xb30f20)
    elif i == '6-':
        return(0xffcdde)
    elif i == '6+':
        return(0xffcdde)
    elif i == '7':
        return(0xffff6c)
##### ヘルプ #####
@bot.command(description="制作者用コマンドヘルプを表示するよ！")
async def helpowner(ctx):
    e = discord.Embed(title="Command Help Owner - コマンドヘルプ",description="コマンドの先頭には、必ず`y>`がいるよ～！",color=0x5dc7fc)
    e.add_field(name="Debug commands/デバッグコマンド",value="`reboot`,`down`,`cmd`,`jishaku`",inline=False)
    e.add_field(name="Status&Activity commands/ステータス&アクテビティコマンド",value="`changeactivity`,`resetactivity`,`changestatusonline`,`changestatusidle`,`changestatusdnd`",inline=False)
    
    await ctx.send(embed=e)
@bot.command(description="コマンドヘルプを表示するよ！\n引数はあってもなくてもOK！")
async def help(ctx,name=None):
    if name is not None:
        if [c for c in bot.commands if c.name == name or name in c.aliases]:
            command = [c for c in bot.commands if c.name == name or name in c.aliases][0]
            embed = discord.Embed(title=f"Command Help - 『{command.name}』",description=command.description,color=0x5dc7fc)
            embed.add_field(name="使い方",value=f"y>{command.name} {((' '.join(f'[{c}]' for c in command.clean_params.keys())) if len(command.clean_params) > 0 else '')}")
            if command.aliases:embed.add_field(name="エイリアス",value=",".join(c for c in command.aliases))
            else:embed.add_field(name="エイリアス",value="エイリアスはないよ")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Command Help - Error",description=f"『{name}っていうコマンドは存在しないよ！\n`help`で確認してね！", color=0xff0000)
            await ctx.send(embed=embed)
    else:
        fist = discord.Embed(title="Command Help - All (⬅/➡でページ切り替え)",description="コマンドの先頭には、必ず`y>`がいるよ～！\nhelpの後に引数としてコマンド名を入力すると、コマンドヘルプが表示されるよ～！\n例:`y>help info`\nBOTの役職の位置を変えないと使えないものがあるかも・・・\n線が引かれているコマンドは使えないよ～",color=0x5dc7fc)
        fist.set_footer(text="HelpPage(1/8)")
        e1 = discord.Embed(title="ボット情報系コマンド",description="`info`,`help`,`ping`,`joinserverlist`",color=0x5dc7fc)
        e1.set_footer(text="HelpPage(2/8)")
        e2 = discord.Embed(title="一般ユーザー向けコマンド",description="Message:`makeembed`,`say`,`send`,`senddm`\nVote:`poll`\nInfo:`time`\nPlay:`randomnumber`,`dice`,`omikuji`\nCalculation:`plus`,`minus`,`times`,`dby`",color=0x5dc7fc)
        e2.set_footer(text="HelpPage(3/8)")
        e3 = discord.Embed(title="報告コマンド",description="`feedback`,`report`,`request`",color=0x5dc7fc)
        e3.set_footer(text="HelpPage(4/8)")
        e4 = discord.Embed(title="情報コマンド",description="`userinfo`,`userserch`,`serverinfo`,`roleinfo`,`channelinfo`",color=0x5dc7fc)
        e4.set_footer(text="HelpPage(5/8)")
        e5 = discord.Embed(title="役職コマンド",description="`rolecreat`,`roledelete`,`roleadd`,`roleremove`,~~`roleusers`~~,~~`rolecolor`~~,`roleallmembersadd`,`roleallmembersremove`",color=0x5dc7fc)
        e5.set_footer(text="HelpPage(6/8)")
        e6 = discord.Embed(title="サーバー管理コマンド",description="User:`ban`,`kick`\nMessage:`clear`,`allclear`,`messagehistory`\nChannel:`textchannelcreate`,`textchanneldelete`,`voicechannelcreate`,`voicechanneldelete`,`categorycreate`,`categorydelete`,`channeledit`",color=0x5dc7fc)
        e6.set_footer(text="HelpPage(7/8)")
        e7 = discord.Embed(title="その他のコマンド",description=f"`jishin`,`eval`,`evalnode`",color=0x5dc7fc)
        e7.set_footer(text="HelpPage(8/8)")
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = [fist, e1, e2, e3, e4 ,e5, e6, e7] #ヘルプの各ページ内容
        send_message = await ctx.send(embed=page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")

        def help_react_check(reaction,user):
            emoji = str(reaction.emoji)
            if reaction.message.id != send_message.id:
                return 0
            if emoji == "➡" or emoji == "⬅":
                if user != ctx.author:
                    return 0
                else:
                    return 1
        while not bot.is_closed():
            try:
                reaction,user = await bot.wait_for('reaction_add',check=help_react_check,timeout=20.0)
            except asyncio.TimeoutError:
                await send_message.clear_reactions()
                await send_message.add_reaction("❌")
                return #時間制限が来たら、それ以降は処理しない
            else:
                emoji = str(reaction.emoji)
                if emoji == "➡":
                    page_count += 1
                if emoji == "⬅":
                    page_count -= 1
                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(embed=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")

                if page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")

                if page_count == 2:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")

                if page_count == 3:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")

                if page_count == 4:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
            
                if page_count == 5:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")

                if page_count == 6:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")

                if page_count == 7:
                    await send_message.add_reaction("⬅")
        
##### 重大コマンド #####
@bot.command(aliases=["dl"],description="重大コマンドです！\n結芽のソースダウンロードリンクを表示します。")
async def download(ctx):
    if ctx.message.author.id == 584008752005513216:
        e = discord.Embed(title="ファイルをダウンロード",description="[ソースをダウンロード](https://www.mediafire.com/file/vlg2sye8556pn46/YuMe%60sbot-source.zip/file)\nMediaFireでダウンロードします。\n(上の青い文をクリック、タップするとサイトに飛びます。)",color=0x5dc7fc)
    
        await ctx.send(embed=e)
    else:
        await ctx.send("霜月君はまだ引退しないよ()")
    
bot.run("NjU3OTM2MTYyOTY2NjAxNzQw.XnbG2w.rQZONwOjBHtmWdWb9e4F4mxIphM")