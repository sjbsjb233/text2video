'''本模块提供chatgpt的api接口'''
import openai
import tiktoken
from script import database


def get_key():
    """从数据库中获取key"""
    sql = '''SELECT key FROM setting WHERE id=1'''
    key = database.select_data(sql, (), 'data/setting.db')[0][0]
    return key


def generate_answer(question, system='', engine='gpt-3.5-turbo'):
    '''生成prompt并累计tokens数量'''

    openai.api_key = get_key()
    try:
        response = openai.ChatCompletion.create(
            model=engine,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": question}
            ])
        answer = response.get("choices")[0]["message"]["content"]
        total_tokens = response.get("usage")["total_tokens"]

        # print(response)

        # 增加数据库中的tokens数量
        sql = '''UPDATE refresh SET spend_tokens=spend_tokens+? WHERE id=1'''
        database.change_data(sql, (total_tokens,), 'data/database.db')

    except Exception as e:
        return False, e, 0

    return answer, total_tokens, response


def num_tokens_from_string(string: str, system='', encoding_name='gpt-3.5-turbo') -> int:
    """获取字符所需的tokens数量"""
    encoding = tiktoken.encoding_for_model(encoding_name)

    num_tokens_1 = len(encoding.encode(string))
    num_tokens_2 = len(encoding.encode(system))
    return num_tokens_1 + num_tokens_2
