"""Pre-built movie materials (video + SRT file IDs) for task creation."""

from typing import Optional

import typer

from narrator_ai.output import console, print_error, print_json, print_table

app = typer.Typer(
    help=(
        "Pre-built movie materials for task creation.\n\n"
        "These are ready-to-use video and SRT files. Use the file IDs directly\n"
        "in episodes_data when creating generate-writing or fast-clip-data tasks.\n\n"
        "View material previews: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc"
    ),
)

MOVIE_MATERIALS = [
    {"name": "这个杀手不太冷", "video_id": "37d5331b-d772-4bdf-b394-df8e8102205c", "srt_id": "23bdfa4b-0ab3-4d90-8977-076286f5f681", "genre": "剧情片"},
    {"name": "人生一世", "video_id": "3dfc2aee-141e-4e47-bec0-536802985dda", "srt_id": "62a9bc8a-346e-4ae1-98d2-02e4a23b10c0", "genre": "剧情片"},
    {"name": "关于约会的一切", "video_id": "05ddd622-0ffe-48a9-a91b-a3a5e8c62c36", "srt_id": "fd0fff5c-66e1-4669-982b-55071aeb3259", "genre": "爱情"},
    {"name": "墙外之音", "video_id": "150db418-b3fa-451a-8c1e-3e397b3f47b8", "srt_id": "ba1d3233-0138-451a-b2d9-e01dcd25029c", "genre": "恐怖惊悚"},
    {"name": "好东西", "video_id": "1fe99214-c208-408d-aabc-28a590b62195", "srt_id": "299bdd6f-2768-444a-b7d2-be2c82320965", "genre": "剧情片"},
    {"name": "孤注一掷", "video_id": "5e978623-f88e-4138-84f7-526d613ad81a", "srt_id": "51718ed0-eaf7-484c-a224-7927cbe1202d", "genre": "犯罪"},
    {"name": "山楂树之恋", "video_id": "c76531e4-498e-4b03-8f5c-613a056f6303", "srt_id": "fc7aca22-fdbf-4eed-9147-503df2900766", "genre": "爱情"},
    {"name": "热辣滚烫", "video_id": "bb89b277-5e25-4cb1-8fff-7608fe2dec92", "srt_id": "3cb8c4da-6d35-48e1-aaec-6d1c3d8a9c1b", "genre": "励志"},
    {"name": "焚城", "video_id": "9eb6601e-f2c3-4851-ae26-dba0bb1ea2eb", "srt_id": "9bd6ae4d-d918-4d86-9762-f7e3b28522d2", "genre": "灾难片"},
    {"name": "猎金游戏", "video_id": "45a748c1-5b25-4b33-9815-bae4fa3219ab", "srt_id": "60d5de22-f7cc-43db-b834-afcd386d704c", "genre": "剧情片"},
    {"name": "白蛇:浮生", "video_id": "b420211d-8a05-440f-af14-c7bedc8a2266", "srt_id": "e9fb1857-7fce-41b0-b4cb-b544cbd77d7c", "genre": "动漫"},
    {"name": "误判", "video_id": "cb72b929-878c-41f8-89e7-01f062fb7951", "srt_id": "4bed0263-9b5b-4fd2-b3fb-7db3d06d393b", "genre": "犯罪"},
    {"name": "长津湖之水门桥", "video_id": "ca7c95f1-dff6-40cc-bbd4-493b4fa99737", "srt_id": "7f0d316e-ccc1-4ad9-9821-d75daf33aba5", "genre": "战争"},
    {"name": "你Y闭嘴", "video_id": "310eb540-0a0e-46f8-a25d-78c3ccbf9905", "srt_id": "76a7edda-6af6-458c-a7ba-9c8fca237a27", "genre": "喜剧片"},
    {"name": "丑女大翻身", "video_id": "ca79f99d-5ad9-4375-a26a-d43923bb481e", "srt_id": "bedd0328-bf99-4745-9f74-d479fef49e26", "genre": "喜剧片"},
    {"name": "北京遇上西雅图", "video_id": "6bf05ddf-8d9b-4830-855b-7651ac882219", "srt_id": "a644db59-dc97-4578-a9dc-5c595e95c3d5", "genre": "爱情"},
    {"name": "一个都不能少", "video_id": "c914fe5b-83b9-452d-b2bd-bbb17db89590", "srt_id": "868ab09a-6ac8-4d96-8308-334c84aeb515", "genre": "剧情片"},
    {"name": "你好，之华", "video_id": "115376f4-f5d0-4a18-815f-0f2c402626ad", "srt_id": "daeb2041-9e78-40df-a798-8f05e37fe32f", "genre": "爱情"},
    {"name": "隐入尘烟", "video_id": "4250b0df-efce-4990-9dfa-a7dfe52852a8", "srt_id": "78107405-661f-4174-b818-d41ce7756831", "genre": "爱情"},
    {"name": "关于我和鬼变成家人的那件事", "video_id": "e90c0466-0ec4-42cc-adeb-cae4c3bed808", "srt_id": "55462639-62a3-4126-9b65-5053cb06e276", "genre": "亲情感人"},
    {"name": "周处除三害", "video_id": "19ad291e-5c1f-4eb3-8ea7-7d5806913f51", "srt_id": "a4564f6d-5656-4b2f-8fa0-22481e585c95", "genre": "动作片"},
    {"name": "长安三万里", "video_id": "0cee0631-3ab8-4650-9950-0041cbce5b8a", "srt_id": "a9d4ab6c-7e69-41db-b3fc-9cd24e904dcf", "genre": "动漫"},
    {"name": "暗杀风暴", "video_id": "980a1c42-f0c1-47a9-a845-2b4c5c0c90d8", "srt_id": "73c81e0f-4742-4580-927e-b96e9eb28a1d", "genre": "警匪"},
    {"name": "坚如磐石", "video_id": "e112ed05-d643-40d1-b904-0df0bf6fa5aa", "srt_id": "727cdf9f-d3a7-430d-b765-707f80c29012", "genre": "警匪"},
    {"name": "傲慢与偏见", "video_id": "8b7ccd9e-2910-4925-9aea-72be833bfc15", "srt_id": "f939ce49-070f-4f7e-baf4-b712df676334", "genre": "爱情"},
    {"name": "唐探1990", "video_id": "ea15d28a-94cc-4f76-89ec-520fad585e41", "srt_id": "bbcd97ee-b66a-4903-be56-193bcc302b38", "genre": "喜剧片"},
    {"name": "我要我们在一起", "video_id": "720e4dc4-9f95-4660-9ef4-31608a41f2a7", "srt_id": "f1d4111a-613a-4d74-b07b-99f1e469c3e3", "genre": "爱情"},
    {"name": "剑雨", "video_id": "910285bb-ccf6-4431-a220-24bbb9729339", "srt_id": "1ec46d8c-d2cb-491a-b4e1-b2497355556b", "genre": "动作片"},
    {"name": "不能说的秘密", "video_id": "7d8710ab-b5b2-40f8-b8e1-243cf8271d19", "srt_id": "894c3b66-eaf7-4d81-8cef-03203a4cb897", "genre": "爱情"},
    {"name": "八角笼中", "video_id": "7a370b69-c17f-48b6-937b-522fe97beac8", "srt_id": "5e510575-e01b-4d66-b701-2604899be38e", "genre": "励志"},
    {"name": "危机航线", "video_id": "776317b6-47ce-4427-8492-5cb99ab8a302", "srt_id": "d21dad71-0384-4114-86c9-aa48a02829d6", "genre": "灾难片"},
    {"name": "万里归途", "video_id": "634706b4-ea2f-413b-a591-7eb2ce53f3b4", "srt_id": "c0836f1c-d521-4903-894c-18a0bd50bccc", "genre": "剧情片"},
    {"name": "晴雅集", "video_id": "b1fe778f-49c1-48c9-8388-896a79a1ee64", "srt_id": "e8d7d70f-fdd8-4843-aa94-51098164d1fa", "genre": "奇幻"},
    {"name": "画皮2", "video_id": "1b746675-a9d7-4b0f-81d5-b93bbb152e43", "srt_id": "74bb4ef3-7617-4280-8c16-bcccebd6cd7d", "genre": "奇幻"},
    {"name": "龙门飞甲", "video_id": "67b34262-0bc4-4e43-9b5c-d50fb6012708", "srt_id": "782ee8fc-7209-4952-8790-a96a34bb267a", "genre": "动作片"},
    {"name": "飞驰人生", "video_id": "7da54c2e-c805-4513-bf6f-90a3384e1c5b", "srt_id": "5905d9fe-a9f0-4dcc-b70d-ff750b41b524", "genre": "喜剧片"},
    {"name": "中国医生", "video_id": "414b31af-a4ce-4792-82c3-3198ba473471", "srt_id": "e44355ba-e0a7-4ac5-9b46-5aa5c4c5f09e", "genre": "剧情片"},
    {"name": "悬崖之上", "video_id": "51f8cc8f-bdd3-4e64-9e99-d33ab2fb79c1", "srt_id": "96e33104-842e-4ae6-b634-13dc44d1f649", "genre": "悬疑片"},
    {"name": "后会无期", "video_id": "d18e8ad5-b286-4177-8c87-97c0a7878bb2", "srt_id": "c85234c0-9c17-4d71-a7d1-653e945de8c7", "genre": "剧情片"},
    {"name": "大话西游之月光宝盒", "video_id": "7ee78a51-6a09-4bed-9b92-290c60a2d720", "srt_id": "861a2f42-5d26-425d-811c-4f7fd36b6956", "genre": "奇幻喜剧"},
    {"name": "大话西游之大圣娶亲", "video_id": "416060c5-3d25-4813-9e5a-0540861550ac", "srt_id": "76c8397e-301c-4699-8d75-6bea9eef16e7", "genre": "奇幻喜剧"},
    {"name": "误杀", "video_id": "7330e2a4-c78f-44ea-b9a2-0abaee2489aa", "srt_id": "cb71bce3-3e59-4bfb-9cfd-8a140bc5f3c7", "genre": "悬疑片"},
    {"name": "三傻大闹宝莱坞", "video_id": "8f4b069e-365b-48c9-9e58-09c7f9980865", "srt_id": "3b9006a6-9d01-4935-a54a-f39f251c890b", "genre": "喜剧片"},
    {"name": "看不见的客人", "video_id": "8a86ff12-da7a-40b2-8eff-c83db7f0a132", "srt_id": "5f56c74c-a857-4203-962a-6d44b0b83941", "genre": "悬疑片"},
    {"name": "战争之王", "video_id": "893dbe3b-5003-4282-bb74-a4e7b6d74115", "srt_id": "829e92de-fcb3-495c-9d5d-9b8143eda954", "genre": "犯罪"},
    {"name": "我的野蛮女友", "video_id": "35d9e11f-8514-42d6-999a-eb42c5f0b886", "srt_id": "4b04d618-2bee-4e18-a9e1-98a0dc6168db", "genre": "爱情"},
    {"name": "沙漠之花", "video_id": "96c8b471-3d20-434e-9977-0c8c28fee054", "srt_id": "79125274-f76c-49a2-a56a-15b2ab69eb93", "genre": "剧情片"},
    {"name": "拆弹专家", "video_id": "bb3d10ee-7f32-47ba-9ae7-913b678641ad", "srt_id": "9ee18333-2bbb-4269-b756-e2854a23783e", "genre": "警匪"},
    {"name": "风暴突击者", "video_id": "052339b3-9858-4393-a884-969846471b9c", "srt_id": "022a9f15-3088-438b-b9cc-86a7ce5ab1a0", "genre": "动作片"},
    {"name": "商海通牒", "video_id": "881f0e06-f1f8-4396-a9e7-dea2625ea5f9", "srt_id": "5bad738d-5e49-415d-80e2-b9ce24459e48", "genre": "剧情片"},
    {"name": "最佳出价", "video_id": "272499bf-0a5a-4eec-96c0-59ee630b7f09", "srt_id": "17203967-6762-4453-93e8-a3db23e25e13", "genre": "爱情"},
    {"name": "无名之辈", "video_id": "0c540131-dedd-479a-8f97-8cfe794ddbfc", "srt_id": "01415c3e-b337-4c5d-9087-f9117ca578d0", "genre": "剧情片"},
    {"name": "审死官", "video_id": "6274069e-5c5c-459c-b895-3ef33ed32d7e", "srt_id": "cdbf44e7-af53-4760-bc14-c424abe4d381", "genre": "喜剧片"},
    {"name": "杀破狼", "video_id": "d3be08a0-5adf-4fdf-a333-d3134aec8ba5", "srt_id": "9ee66c15-e8b1-4f3a-b9ca-948458fa13ec", "genre": "动作片"},
    {"name": "家有喜事", "video_id": "330a3898-0418-4a79-ad97-3bdb8f89eed4", "srt_id": "18ec4041-40a5-4d26-b4ec-86ee3f25881b", "genre": "喜剧片"},
    {"name": "谜一样的双眼", "video_id": "1518a82d-c656-4bac-a1f8-1bf2cc8ce04c", "srt_id": "e5c486e3-c63b-4d58-a6d7-4031c95a9b76", "genre": "悬疑片"},
    {"name": "忠犬帕尔玛", "video_id": "ae45d190-f1f6-4a47-9bca-293f021b6ee6", "srt_id": "3ba3abb5-e87d-4f62-9aa5-5c01fec708a9", "genre": "剧情片"},
    {"name": "金蝉脱壳2", "video_id": "e29ee9f1-c341-42eb-bb68-1f3d0174a70a", "srt_id": "8acc19f1-29f7-43d0-b38c-e0cc27c154a9", "genre": "动作片"},
    {"name": "喜欢你", "video_id": "a6c4dfee-ce02-49f2-9abe-47e584cd35a9", "srt_id": "73f4d70f-e801-4130-b0b0-5650feda1b12", "genre": "爱情"},
    {"name": "春江水暖", "video_id": "c915a1c6-9e9a-4a6d-9f36-694d3fd01d3c", "srt_id": "f420ff55-f4cb-479e-a184-f7cbade39ec1", "genre": "剧情片"},
    {"name": "魔法老师", "video_id": "ccf88900-aa18-4f70-8bf4-2cb5c2a26722", "srt_id": "84bc9124-46bf-4dfe-a60c-9e3a541fd5d4", "genre": "喜剧片"},
    {"name": "爱你就捧你", "video_id": "e304302e-ed7f-4507-b093-f78bcd7f6701", "srt_id": "f4283a9d-6adc-4cdc-aa06-0bb2b1b953bd", "genre": "喜剧片"},
    {"name": "春娇救志明", "video_id": "12778e00-43c7-41b6-9af6-f9657cc79cf6", "srt_id": "53cb5036-fc65-4689-b0ea-b872aa511520", "genre": "爱情"},
    {"name": "功夫瑜伽", "video_id": "f4ad1945-36c3-4329-8128-9c10c20ea7b8", "srt_id": "801370dd-ac17-400a-ae00-b0de1ab3f226", "genre": "喜剧片"},
    {"name": "反贪风暴2", "video_id": "5cb9090f-edb6-4d28-b763-f87e528bf557", "srt_id": "85667929-e691-4876-844d-463c91f1c210", "genre": "动作片"},
    {"name": "反贪风暴", "video_id": "2a6e11ef-d936-4fab-87c3-ab5254fbdc5d", "srt_id": "06c736e6-afa7-41b0-8387-9ac2def0759f", "genre": "动作片"},
    {"name": "毒。诫", "video_id": "d0ef2f04-df54-49a7-9ce6-ef3a33ce4c7c", "srt_id": "2682c720-8ceb-48b1-ba61-4c92ba8f8175", "genre": "犯罪"},
    {"name": "黑雀特工", "video_id": "3e8f67fb-2a6e-4d5e-8bcc-916826ffaf21", "srt_id": "eefaa6b7-fd90-418b-a0e5-d985fdca4162", "genre": "动作片"},
    {"name": "惊天破", "video_id": "c9e69d24-706c-41bf-aa1e-5d528dc57bfe", "srt_id": "2e6f8a1a-613a-4521-97ef-1c0f2b49ee0a", "genre": "警匪"},
    {"name": "师父", "video_id": "2baebc50-527c-4bd6-88fe-58a8830d1644", "srt_id": "4c2d2a58-0050-4841-9cce-7beb2f6db981", "genre": "武侠片"},
    {"name": "致命追击", "video_id": "6777fde8-ae86-491d-b54d-0ac0df4f79eb", "srt_id": "64912f3e-b982-4d49-80be-45bd01a7cf3b", "genre": "动作片"},
    {"name": "金蝉脱壳3：恶魔车站", "video_id": "46ced23e-c8b7-4f59-addb-886c1dc5722e", "srt_id": "e5b7c298-4662-459b-8837-07818be791a7", "genre": "动作片"},
    {"name": "12勇士", "video_id": "e79958db-7e07-4d7b-a090-37561e5f2cc7", "srt_id": "a962c9a1-6e68-44ff-9731-33fb890523b5", "genre": "战争"},
    {"name": "苏乞儿", "video_id": "af5d5211-da53-478c-9e86-28a6909642c0", "srt_id": "4b10bd92-100c-4044-af92-74280286bf9d", "genre": "动作片"},
    {"name": "寄生异形", "video_id": "b8518406-30de-488c-a6a4-8309c35c96fa", "srt_id": "877b4f9d-5405-40ea-964c-3399d49c7631", "genre": "科幻片"},
    {"name": "麦路人", "video_id": "8b6dc917-9ddb-4a59-9c29-cc784a8f6da8", "srt_id": "ca05e2dc-8e86-4681-b98b-e20e229a1e12", "genre": "剧情片"},
    {"name": "狂兽", "video_id": "53727984-eed1-4d81-a582-29821a7a821f", "srt_id": "3fadb40e-0544-4640-9df5-844c41c94cf4", "genre": "动作片"},
    {"name": "大话西游3", "video_id": "c931c5c5-0bb1-4017-89ba-3e85cc864060", "srt_id": "237e3937-9305-45de-9539-58cae0843aef", "genre": "喜剧片"},
    {"name": "赌城大亨2之至尊无敌", "video_id": "383c41c6-a48c-4832-a8b2-5dc91a7d5658", "srt_id": "44bd51fc-3785-47cb-a6ab-e2a47a55c897", "genre": "剧情片"},
    {"name": "七剑", "video_id": "fdfc3d1f-024f-4f8a-ba21-db5e4d7fc77e", "srt_id": "397975cf-5027-4132-a330-a33c92740d38", "genre": "武侠片"},
    {"name": "同谋", "video_id": "8d69069e-4907-499d-b0df-5078e64fac5f", "srt_id": "eb8c71a0-602c-4fcc-820b-e9855f1a6bdc", "genre": "悬疑片"},
    {"name": "浓情酒乡", "video_id": "2252d479-1629-4c10-a504-9a4412edbdcf", "srt_id": "9cbbedc2-a060-4d70-afd1-59be00e64f1a", "genre": "剧情片"},
    {"name": "萨米大冒险", "video_id": "40c19bb5-0833-4fdb-96fb-20b8f3e57d6a", "srt_id": "b86160cc-e1d9-40dc-9876-7275a5563af2", "genre": "冒险片"},
    {"name": "八面埋伏", "video_id": "03379b1253d945a7935d303f6c06500c", "srt_id": "3149b81afc764a5288bc1605636b0a16", "genre": "犯罪悬疑"},
    {"name": "多力特的奇幻冒险", "video_id": "67b838dee3d248edb01865640ad5e459", "srt_id": "e1e169eb75d44dbb854b2b23eddc8776", "genre": "奇幻"},
    {"name": "前程似锦的女孩", "video_id": "29099a68c1374b639af8aa21b7b77a64", "srt_id": "7a788bc99e5f4a379c55d285c3acb72b", "genre": "犯罪悬疑"},
    {"name": "三十极夜", "video_id": "291f5fa0a32d47ca8eae636681a7d45a", "srt_id": "011b199a4dbe45aa8a6f72bc01342dc9", "genre": "恐怖惊悚"},
    {"name": "速度与激情9", "video_id": "4b8258d8754647d6925eece31e3fb256", "srt_id": "960bafaec43c4e2480993c4a7b8ad2e3", "genre": "动作片"},
    {"name": "消失的西德尼·豪尔", "video_id": "d81ea4adabc94bd49c6906c1d755fed7", "srt_id": "c5cf79dc25e4458d9a5213cec4da2fd7", "genre": "剧情片"},
    {"name": "尖头外星族", "video_id": "784dfce79e4a4fc5b05f5b508c413958", "srt_id": "44278074ea654225ab57b3cc5abec1c8", "genre": "奇幻喜剧"},
    {"name": "五路追杀令", "video_id": "8991cb3692a34edfbf02361a3ac92393", "srt_id": "2cf3d2bd166e40cfbdeea9f17a79b54c", "genre": "动作片"},
    {"name": "浪漫鼠德佩罗", "video_id": "b63ee4fb511d4a22923fca9d5ef2c76c", "srt_id": "b718cac5d1504ce3a9b8125a2a9095d5", "genre": "动漫"},
    {"name": "老爸当家", "video_id": "190f17975551422b95807a176e9911a2", "srt_id": "0d34f936e02d420cb018523fbc604317", "genre": "喜剧片"},
]


@app.command("list")
def list_materials(
    genre: Optional[str] = typer.Option(None, "--genre", "-g", help="Filter by genre"),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search by movie name"),
    json_mode: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """List pre-built movie materials (video + SRT file IDs).

    Use these file IDs directly in episodes_data for task creation.
    The video_id is used as both video_oss_key and negative_oss_key,
    and srt_id is used as srt_oss_key.

    View material previews: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc
    """
    items = MOVIE_MATERIALS
    if genre:
        items = [m for m in items if genre in m["genre"]]
    if search:
        items = [m for m in items if search.lower() in m["name"].lower()]

    if not items:
        genres = sorted(set(m["genre"] for m in MOVIE_MATERIALS))
        print_error(f"No materials found. Available genres: {', '.join(genres)}")
        raise typer.Exit(1)

    if json_mode:
        print_json(items)
    else:
        title = f"Movie Materials ({len(items)})"
        if genre:
            title = f"Movie Materials - {genre} ({len(items)})"
        columns = [("name", "Movie"), ("video_id", "Video ID"), ("srt_id", "SRT ID"), ("genre", "Genre")]
        print_table(items, columns, title=title)
        console.print(f"\n[dim]View previews: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc[/dim]")


@app.command("genres")
def list_genres(
    json_mode: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """List available movie genres with counts."""
    genre_counts = {}
    for m in MOVIE_MATERIALS:
        genre_counts[m["genre"]] = genre_counts.get(m["genre"], 0) + 1
    items = [{"genre": g, "count": c} for g, c in sorted(genre_counts.items())]

    if json_mode:
        print_json(items)
    else:
        print_table(items, [("genre", "Genre"), ("count", "Count")], title=f"Movie Genres ({len(MOVIE_MATERIALS)} total)")
