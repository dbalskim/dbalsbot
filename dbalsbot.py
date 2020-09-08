import discord
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("코딩")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("하이 드발스"):
        num = random.randint(1, 5)
        if num == 1:
            await message.channel.send("네")
        elif num == 2:
            await message.channel.send("ㅇ")
        elif num == 3:
            await message.channel.send("꺼지셈")
        elif num == 4:
            await message.channel.send("안물")
        elif num == 5:
            await message.channel.send("ㅗ")
    if message.content.endswith("잘했어"):
        await message.channel.send("감사합니다")
    if message.content.endswith("나 잘생김?"):
        await message.channel.send("ㄴ")
    if message.content.endswith("잘생김"):
        await message.channel.send("리랄 ㄴ")
    if message.content.endswith("잘생긴 듯"):
        await message.channel.send("ㅗ")
    if message.content.endswith("김유민은?"):
        await message.channel.send("IQ999999999")
    if message.content.endswith("유민선은?"):
        await message.channel.send("우리돼지한동")
    if message.content.endswith("이준서는?"):
        await message.channel.send("쿨찐")
    if message.content.endswith("김연성은?"):
        await message.channel.send("바보")
    if message.content.endswith("이동현은?"):
        await message.channel.send("공항동둑")
    if message.content.endswith("김태연은?"):
        await message.channel.send("난 한국인이야~")
    if message.content.endswith("김경빈은?"):
        await message.channel.send("난 삭발은 하지 않을거야")
    if message.content.endswith("김현진"):
        await message.channel.send("호주 13부리그 서드선수")
    if message.content.endswith("진은석은?"):
        await message.channel.send("정규짝사랑 10년차")
    if message.content.endswith("서태민은?"):
        await message.channel.send("ㅌㅈ")
    if message.content.endswith("최은서는?"):
        await message.channel.send("ㄱㅊㅇ")
    if message.content.endswith("최하린은?"):
        await message.channel.send("시미새(시미켄에 미친 새X)")
    if message.content.endswith("유태준은?"):
        await message.channel.send("He is K-gay")
    if message.content.endswith("이준아는?"):
        await message.channel.send("태주짝사랑러")

    try:
        if message.content.endswith("사진 보내줘"):
            pic = message.content.split(" ")[0]
            await message.channel.send(file=discord.File(pic))
    except FileNotFoundError:
        await message.channel.send("사진을 찾을 수 없습니다.")

    if message.content.endswith("보내줘"):
        channel = message.content[0: 18]
        msg = message.content[20:-4]
        await client.get_channel(int(channel)).send(msg)
    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
    if message.content.endswith("저새기 뮤트좀"):
        author = message.guild.get_member(int(message.content[0:18]))
        role = discord.utils.get(message.guild.roles, name="Muted")
        await author.add_roles(role)

    if message.content.endswith("뮤트해제"):
        author = message.guild.get_member(int(message.content[0:18]))
        role = discord.utils.get(message.guild.roles, name="Muted")
        await author.remove_roles(role)

    if message.content.endswith("사진 목록"):
        files = os.listdir("C:\\김유민 폴더\\파이참\\dbalsbot")
        for f in files:
            if f.endswith(".png"):
                await client.get_channel(726374006701293578).send(f)
    if message.content.startswith("도움말"):
        await message.channel.send("호출: \"하이 드발스\"")
        await message.channel.send("칭찬: \"잘했어\"")
        await message.channel.send("사진보내기: \"사진이름.png 사진 보내줘\"")
        await message.channel.send("사진목록 확인: \"사진 목록\"")
        await message.channel.send("특정 채널에 메시지: \"채널ID 내용 보내줘\"")
        await message.channel.send("개인 메시지: \"/DM 유저ID 내용\"")
        await message.channel.send("뮤트: \"유저ID 저새기 뮤트좀\"")
        await message.channel.send("언뮤트: \"유저ID 뮤트해제\"")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
