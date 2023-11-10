import json
import base64
# import boto3
import time


def lambda_handler(event, context):
    print(event)
    data_list = base64.b64decode(event["body"]).decode().split('&')
    data = {}
    for a in data_list:
        data[a.split("=")[0]] = int(a.split("=")[1])
    print(data)
    # boto3クライアントでテーブルデータを更新する。
    # table_gameから。

    dynamoDB_client = boto3.client('dynamodb')
    responce = dynamoDB_client.put_item(
        TableName='game_table',
        Item={
            'time': {"N": str(round(time.time()))},
            'result': {"M": {
                '1st': {"M": {
                    'player_id': {"N": str(data['player1st'])},
                    'score': {"N": str(data['score1st'])}
                }},
                '2nd': {"M": {
                    'player_id': {"N": str(data['player2nd'])},
                    'score': {"N": str(data['score2nd'])}
                }},
                '3rd': {"M": {
                    'player_id': {"N": str(data['player3rd'])},
                    'score': {"N": str(data['score3rd'])}
                }},
                '4th': {"M": {
                    'player_id': {"N": str(data['player4th'])},
                    'score': {"N": str(data['score4th'])}
                }}
            }}
        }
    )

    # できたらtrue、だめならfalse
    return True


data = {'player1st': 1, 'player2nd': 2, 'player3rd': 3, 'player4th': 4,
        'score1st': 0, 'score2nd': 0, 'score3rd': 0, 'score4th': 0}
players_id_list = [
    [data['player1st'],data['score1st']],
    [data['player2nd'],data['score2nd']],
    [data['player3rd'],data['score3rd']],
    [data['player4th'],data['score4th']]
]
print(players_id_list)