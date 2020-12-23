import discord
import random
import os

client = discord.Client()

IDdict = ({"김유민": 717621111214571610, "최하린": 550961525473542174, "이준서": 717614640913186836, "김태연": 726595497543860235,
           "봉근우": 642301945452822538, "서태민": 717613221770690623, "이동현": 715749223366393897, "유민선": 717629684950630451,
           "김경빈": 689092210318245910, "신우혁": 680304262466764806, "진은석": 717618852569022488, "김현진": 707067588164976731,
           "김준우": 582110896747446272, "유태준": 496917071377072138, "김민우": 718374376566816799, "최은서부계정": 620896283846246400,
           "김현진부계정": 722717936854237234, "최시훈": 720936406922559529, "김연성": 688650734232928265, "전지홍": 559203766608592896,
           "이재환": 648886048054837278, "최은서": 717680925214900264, "이준아": 695485985718272020, "채팅": 724763202625470477,
           "파티원모집": 748052499159580774, "명령어": 726374006701293578, "머가리전용채널": 733133750954885193,
           "국민청원": 747989168340074608, "건의사항": 729553118320132197, "투표게시판": 747989212254699670,
           "포토샵해드림": 752685911778656436, "신고게시판": 748142921911631913, "로우패밀리전용채널": 736590900871823421})
musicList = []
for i in range(100):
    musicList.append(list())


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("거확찢")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="🤝Friends")
    await member.add_roles(role)

@client.event
async def on_message(message):
    if message.content.startswith("하이 드발스"):
        num = random.randint(1, 10)
        if num == 1:
            await message.channel.send("네")
        elif num == 2:
            await message.channel.send("ㅇ")
        elif num == 3:
            await message.channel.send("꺼지셈")
        elif num == 4:
            await message.channel.send("안물")
        elif num == 5:
            await message.channel.send("으찌라구요")
        elif num == 6:
            await message.channel.send("함바이")
        elif num == 7:
            await message.channel.send("국적 ㅊㅇ")
        elif num == 8:
            await message.channel.send("븅")
        elif num == 9:
            await message.channel.send("넹 주인님")
        else:
           await message.channel.send("느그")
    if message.content.endswith("잘했어"):
        await message.channel.send("감사합니다")
    if message.content.endswith("조용히좀"):
        await message.channel.send("ㅂ")
    if message.content.endswith("못했어"):
        await message.channel.send("ㄹㅇ ㅂ")
    if message.content.endswith("야 드발스"):
        await message.channel.send("왜불러 이새끼야")
    if message.content.endswith("개발련"):
        await message.channel.send("응 닥쳐")
    if message.content.endswith("바보"):
        await message.channel.send("김연성 킥한다 ㅂ")
    if message.content.endswith("아니 ㅋㅋ"):
        await message.channel.send("김연성 귀척ㄴ 킥한다 ㅂ")
    if message.content.endswith("나 잘생김?"):
        await message.channel.send("ㄴ")
    if message.content.endswith("잘생김"):
        await message.channel.send("리랄 ㄴ")
    if message.content.endswith("잘생긴 듯"):
        await message.channel.send("ㅈㄹ")
    if message.content.endswith("김유민은?"):
        await message.channel.send("IQ999999999")
    if message.content.endswith("유민선은?"):
        await message.channel.send("박쥐먹방")
    if message.content.endswith("이준서는?"):
        await message.channel.send("이집트 스핑크스")
    if message.content.endswith("김연성은?"):
        await message.channel.send("-잼-")
    if message.content.endswith("이동현은?"):
        await message.channel.send("노인정 34년차")
    if message.content.endswith("김태연은?"):
        await message.channel.send("이슬람모태신앙아랍인")
    if message.content.endswith("김경빈은?"):
        await message.channel.send("난 삭발은 하지 않을거야")
    if message.content.endswith("김현진은?"):
        await message.channel.send("좆스윌스")
    if message.content.endswith("진은석은?"):
        await message.channel.send("양궁부에서 추방")
    if message.content.endswith("서태민은?"):
        await message.channel.send("점때문에 차임")
    if message.content.endswith("최은서는?"):
        await message.channel.send("게이샘기")
    if message.content.endswith("최하린은?"):
        await message.channel.send("시미새(시미켄에 미친 새X)")
    if message.content.endswith("유태준은?"):
        await message.channel.send("함바이")
    if message.content.endswith("이준아는?"):
        await message.channel.send("어묵")
    if message.content.endswith("드발스봇은?"):
        await message.channel.send("천재의 창작물")
    if message.content.endswith("꽃미남"):
        await message.channel.send("집에 거울이 ")

    try:
        if message.content.endswith("사진 보내줘"):
            pic = message.content.split(" ")[0]
            await message.channel.send(file=discord.File(pic))
    except FileNotFoundError:
        await message.channel.send("사진을 찾을 수 없습니다.")


    if message.content.endswith("라고 보내줘"):
        message_split = message.content.split("채널에 ")
        channel = message_split[0].strip()
        if "이라고" in message_split[1]:
            msg = message_split[1][:-7]
        else:
            msg = message_split[1][:-6]
        await client.get_channel(IDdict[channel]).send(msg)
        embed = discord.Embed(title="성공적으로 실행되었습니다.", description=channel + "에 " + msg + "를 보냈습니다.", color=0x62c1cc)
        await message.channel.send(embed=embed)

    if message.content.endswith("에게 보내줘"):
        if "이라고" in message.content:
            message_split = message.content.split("이라고")
        else:
            message_split = message.content.split("라고")
        name = message_split[1][:-6]
        author = message.guild.get_member(IDdict[name.strip()])
        msg = message_split[0]
        await author.send(msg)
        embed = discord.Embed(title="성공적으로 실행되었습니다.", description=name + "에게 " + msg + "를 보냈습니다.", color=0x62c1cc)
        await message.channel.send(embed=embed)




    if message.content.endswith("저새기 뮤트좀"):
        name = message.content[0:-8]
        muteauthor = message.guild.get_member(IDdict[message.content[0:-8]])
        role = discord.utils.get(message.guild.roles, name="Muted")
        if message.author.id == IDdict["김유민"]:
            await muteauthor.add_roles(role)
            embed = discord.Embed(title="뮤트.", description=name + "이/가 뮤트 되었습니다.", color=0x62c1cc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("관리자 미만잡.")

    if message.content.endswith("뮤트 해제"):
        name = message.content[0:-6]
        muteauthor = message.guild.get_member(IDdict[message.content[0:-6]])
        role = discord.utils.get(message.guild.roles, name="Muted")
        if message.author.id == IDdict["김유민"]:
            await muteauthor.remove_roles(role)
            embed = discord.Embed(title="뮤트.", description=name + "이/가 뮤트 해제 되었습니다.", color=0x62c1cc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("관리자 미만 잡")

    if message.content.endswith("사진 목록"):
        await message.channel.send("공지사항을 참고하세요.")

    if message.content.startswith("/투표"):
        vote = message.content[4:].split("|")
        await message.channel.send("__**⭐" + vote[0] + "**__")
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('✅')





    if message.content.startswith("도움말"):
        await message.channel.send("""호출: \"하이 드발스\", \"야 드발스\"
칭찬: \"잘했어\"
물어보기: \"이름은/는?\"
사진보내기: \"사진이름.png 사진 보내줘\"
사진목록 확인: \"사진 목록\"
투표: \"/투표 주제|내용1|내용2...\"
특정 채널에 메시지: \"OOO 채널에 메시지(이)라고 보내줘\"
개인 메시지: \"메시지(이)라고 OOO에게 보내줘\"
뮤트: \"이름 저새기 뮤트좀\"
언뮤트: \"이름 뮤트 해제\"""")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
