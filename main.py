from openai import OpenAI
client = OpenAI()

topic = ["個人資訊", "日常生活", "家庭、朋友與周邊人際", "教育與學習", "工作與職場", "旅遊與交通", "購物與服務",
         "飲食與餐飲", "健康與身體照護", "休閒與娛樂", "運動", "自然與環境", "科技與媒體", "語言與溝通", "社會與文化", "思維與情感"]

for n, t in enumerate(topic):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # {"role": "system", "content": "你是一個臺灣人"},
            {
                "role": "user",
                "content": f"現在的聊天情境是「{t}」，請生成100句繁體中文句子，每個句子大概10到30個字，使用臺灣繁體中文用語，不要中國用語"
            }
        ]
    )

    try:
        strings = completion.choices[0].message.content.split("\n\n")[1].split("\n")
        with open("output.txt", "a", encoding="utf-8") as file:
            for s in strings:
                try:
                    file.write(s.split(". ")[1]+"\n")
                except:
                    pass
    except:
        pass
