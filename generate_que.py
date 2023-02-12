import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def design_prompt(keyword,para):
    prompt = '''Write 5 question based on {keyword} that the following article is the answer to: \n
                {para}
    '''.format(keyword=keyword,para=para)
    return prompt


def GenerateParQuestions(keyword,para):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= design_prompt(keyword=keyword, para=para),
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
        return response['choices'][0]['text']
