from dotenv import dotenv_values

env_variables = dotenv_values('.env')

rabbitmq_user = env_variables['rabbitmq_user']
rabbitmq_password = env_variables['rabbitmq_password']
rabbitmq_host = env_variables['rabbitmq_host']
rabbitmq_port = env_variables['rabbitmq_port']
db_user = env_variables['db_user']
db_password = env_variables['db_password']
db_host = env_variables['db_host']
db_name = env_variables['db_name']