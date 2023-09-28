from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot import types
from utils import HELP_TEXT, URL

start = InlineKeyboardBuilder()
start.row(InlineKeyboardButton(text='🚀START🚀', callback_data='menu'))

trial_button = InlineKeyboardBuilder()
trial_button.row(InlineKeyboardButton(text='✅3 DAYS FREE✅', callback_data='start_trial'))

make_money = InlineKeyboardBuilder()
make_money.row(InlineKeyboardButton(text='💵MAKE MONEY💵', callback_data='make_money'))
# make_money.row(InlineKeyboardButton(text='TEXT ME📲', url=HELP_TEXT))

register_button = InlineKeyboardBuilder()
register_button.row(InlineKeyboardButton(text='📲REGISTER', url=URL))
register_button.row(InlineKeyboardButton(text='TEXT ME📲', url=HELP_TEXT))

help_button = types.InlineKeyboardMarkup()
help_button.add(types.InlineKeyboardButton(text='HELP', url=HELP_TEXT))

res_of_game = InlineKeyboardBuilder()
res_of_game.row(
    InlineKeyboardButton(text='WIN', callback_data='game:win'),
    InlineKeyboardButton(text='LOSE', callback_data='game:lose')
)

contact_button = InlineKeyboardBuilder()
contact_button.row(InlineKeyboardButton(text='CONTACT ME', url=HELP_TEXT))

test_game = InlineKeyboardBuilder()
test_game.row(InlineKeyboardButton(text='NEW ROUND', callback_data='new_round_test'))

test_game_win_lose = InlineKeyboardBuilder()
test_game_win_lose.row(
    InlineKeyboardButton(text='WIN', callback_data='new_round_test'),
    InlineKeyboardButton(text='LOSE', callback_data='new_round_test')
)

welcome = InlineKeyboardBuilder()
welcome.row(InlineKeyboardButton(text='🚀START🚀', callback_data='menu'))
welcome.row(InlineKeyboardButton(text='💬CONTACT ME💬', url=HELP_TEXT))

reg_kb = InlineKeyboardBuilder()
reg_kb.row(InlineKeyboardButton(text='START DEMO BOT', callback_data='new_round_test'))
reg_kb.row(InlineKeyboardButton(text='💬HELP💬', url=HELP_TEXT))

help_button_aiogram = InlineKeyboardBuilder()
help_button_aiogram.row(InlineKeyboardButton(text='HELP', url=HELP_TEXT))

bro = InlineKeyboardBuilder()
bro.row(InlineKeyboardButton(text='📲REGISTER', url=URL))
bro.row(InlineKeyboardButton(text='TEXT ME📲', url=HELP_TEXT))
