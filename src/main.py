from ollama import chat

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': '''
請分析下面這句話：

提醒我明天下午三點找老師討論論文

請只輸出JSON：

{
  "title":"待辦事項名稱",
  "time":"時間"
}
'''
        }
    ]
)

print(response['message']['content'])