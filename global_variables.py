# global variables init
import dotenv, os

dotenv.load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
# TEST_GUILD_ID = os.getenv('DISCORD_TEST_GUILD_ID')
PROFESSOR_ROLE_NAME = os.getenv('PROFESSOR_ROLE_NAME')
HEAD_TA_ROLE_NAME = os.getenv('AUXILIAR_ROLE_NAME')
TA_ROLE_NAME = os.getenv('ASSISTANT_ROLE_NAME')
STUDENT_ROLE_NAME = os.getenv('STUDENT_ROLE_NAME')

DEFAULT_ENV_VALUES = {
    "GENERAL_TEXT_CHANNEL_NAME" : os.getenv('GENERAL_TEXT_CHANNEL_NAME'),
    "GENERAL_VOICE_CHANNEL_NAME" : os.getenv('GENERAL_VOICE_CHANNEL_NAME'),
    "PRIVATE_TEXT_CHANNEL_NAME" : os.getenv('PRIVATE_TEXT_CHANNEL_NAME'),
    "PRIVATE_VOICE_CHANNEL_NAME" : os.getenv('PRIVATE_VOICE_CHANNEL_NAME'),
    "LOG_TEXT_CHANNEL" : os.getenv('LOG_TEXT_CHANNEL'),
    "MAX_STUDENTS_PER_GROUP" : int(os.getenv('MAX_STUDENTS_PER_GROUP')),
    "REQUIRE_NICKNAME": bool(os.getenv('REQUIRE_NICKNAME')),
    "BROADCAST_TO_EMPTY_GROUPS": bool(os.getenv('BROADCAST_TO_EMPTY_GROUPS')),
    "TT_ROLES" : [PROFESSOR_ROLE_NAME, HEAD_TA_ROLE_NAME, TA_ROLE_NAME]
}