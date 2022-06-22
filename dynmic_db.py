import boto3

dynamo_client = boto3.resource(service_name='dynamodb', region_name='us-east-1',
                               aws_access_key_id='AKIAV3226N2I2P7VSO25',
                               aws_secret_access_key='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')
product_table = dynamo_client.Table('coin_project_telegram')


def get_coin_info(coin_name):
    coin_name = coin_name.upper()
    result = product_table.get_item(Key={'coin': coin_name})
    if len(result) == 2:
        return result['Item']['coin_info']
    return "العملة غير موجودة، تاكد من كتابة ا" \
           "لعملة بشكل صحيح"


def update_coin_info(coin_name, coin_info):
    coin_name = coin_name.upper()
    product_table.update_item(Key={'coin': coin_name},
                              UpdateExpression='set coin_info =:S',
                              ExpressionAttributeValues={":S": coin_info})


def delete_coin(coin_name):
    coin_name = coin_name.upper()
    product_table.delete_item(Key={'coin': coin_name})


def insert_coin(coin_name, coin_info):
    coin_name = coin_name.upper()
    product_table.put_item(Item={'coin': coin_name, "coin_info": coin_info})
