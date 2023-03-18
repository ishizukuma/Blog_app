# 辞書型の会話の応答をしてくれる辞書を返す関数
def response():
    res = {
        "はじめまして": ["はじめまして！", "チャットボットです！", "何かご用件はありますか？"],
        "初めまして": ["はじめまして！", "チャットボットです！", "何かご用件はありますか？"],
        "こんにちは": ["こんにちは！", "やあ！", "こんにちは。"],
        "こんにちわ": ["こんにちは！", "やあ！", "こんにちは。"],
        "おはよう": ["おはようございます！", "おはよう！", "朝だー！"],
        "こんばんは": ["こんばんは！", "こんばんはー！", "夜だー！"],
        "こんばんわ": ["こんばんは！", "こんばんはー！", "夜だー！"],
        "ありがとう": ["どういたしまして！", "いいえ、こちらこそ！", "何でもおっしゃってください。"],
        "天気": ["晴れです。", "雨です。", "曇りです。", "雪です。", "嵐です。", "雷です。"],
        "日記": ["日記を作成しよう！", "MYAPP LISTから日記の作成ができます。", "今日の出来事を書き残そう！"],
        "何": ["日記を作成ができるよ。", "日記の作成ができます。", "日記の作成ができます。！"],
        "スポーツ": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "旅行": ["日記を書こう！", "楽しかった？", "次はどこに行こうか。"],
        "行った": ["日記を書こう！", "楽しかった？", "次はどこに行こうか。"],
        "家族": ["何があった？", "日記に残そう。", "よかったですね。"],
        "食べ": ["おいしそうですね。", "お味はいかがでした？", "よかったですね。"],
        "食事": ["おいしそうですね。", "私も食べたい。", "いいね！"],
        "サッカー": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "野球": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "バスケ": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "バレー": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "テニス": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "水泳": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "プール": ["楽しかった？", "日記に残そう", "また行きたいね！"],
        "海": ["楽しかった？", "日記に残そう", "また行きたいね！"],
        "する": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "やる": ["楽しかった？", "日記に残そう", "またやりたいね！"],
        "ゲーム": ["楽しかった？", "日記に残そう", "またやりたいね！"],
    }
    return res

bye = ["バイバイ","さようなら","またね"]
no = ["理解できませんでした。","理解不能！","もう一回言ってくれますか？"]