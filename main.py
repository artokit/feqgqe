import asyncio
import os
import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery, ChatMemberUpdated
import keyboards
from utils import CODE, URL
import db_api
import sender
token = '6035818558:AAHPUE5KNaCjpXbwXGLwad-eI_9qSM6Vj2I'
bot = Bot(token)
dp = Dispatcher()
sender.set_bot(dp, bot)
sender.init_handlers()
VIDEO_PATH = os.path.join(os.path.dirname(__file__), 'videos')
PHOTOS_PATH = os.path.join(os.path.dirname(__file__), 'photos')
ADMINS = [6076339332, 5833820044]
media_hash = {

}


@dp.my_chat_member()
async def test_chat_member(chat_member_updated: ChatMemberUpdated):
    if chat_member_updated.new_chat_member.status == 'kicked':
        await db_api.add_block_user(chat_member_updated.chat.id)


@dp.message(Command('stat'))
async def get_stat(message: Message):
    if message.chat.id not in ADMINS:
        return

    s = datetime.datetime.now().strftime('%Y-%m-%d')
    users = await db_api.get_users_info()
    count = 0
    blocked_count = 0

    for user in users:
        if user[1].split()[0] == s:
            count += 1
        if user[2]:
            if user[2].split()[0] == s:
                blocked_count += 1
    # for user in users:
    #     if user[2].split()[0] == s:
    #         blocked_count += 1

    await message.answer(
        f'Общее количество пользователей: {len(users)}\n'
        f'Новых пользователей за сегодня: {count}\n'
        f'Заблочили бота за сегодня: {blocked_count}'
    )


async def send_video(user_id, video_name, **kwargs):
    if video_name not in media_hash:
        message = await bot.send_video(
            user_id,
            FSInputFile(os.path.join(VIDEO_PATH, video_name), filename=video_name),
            **kwargs
        )
        media_hash[video_name] = message.video.file_id
    else:
        await bot.send_video(user_id, media_hash[video_name], **kwargs)


async def send_photo(user_id, photo_name, **kwargs):
    if photo_name not in media_hash:
        message = await bot.send_photo(
            user_id,
            FSInputFile(os.path.join(PHOTOS_PATH, photo_name), filename=photo_name),
            **kwargs
        )
        media_hash[photo_name] = message.photo[-1].file_id
    else:
        await bot.send_photo(user_id, media_hash[photo_name], **kwargs)


@dp.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await db_api.add_user(message.chat.id, message.from_user.username)
    await db_api.add_user_info(message.chat.id)
    await state.clear()
    await send_video(
        message.chat.id,
        'start.mp4',
        caption='🤑Is video ko dekho aur samjho ki yeh BOT kaise kaam karta hai \n\n'
                '<b>usne AVIATOR game ke sambhavanon ko samjha. Tumhe bas activate karne ki jarurat hai</b>',
        parse_mode='html',
        reply_markup=keyboards.start.as_markup()
    )


@dp.callback_query(F.data == 'menu')
async def get_menu(call: CallbackQuery):
    await send_photo(
        call.message.chat.id,
        'start_trial.png',
        caption='<b>ℹ️  APNE ACTIVATION KA EK TARIFF SELECT KARE</b>\n\n'
                '💰Tumhare pass is BOT ko free mein pane ka ek acha mauka hai!\n\n'
                '👉3 din ka tarrif choose kare vo bhi bilkul free ya phir ek mahine ka access kharid le.\n\n'
                '(😍 100% se jada subscribers ne in 3 dino mein monthly wala access earn kiya hai)\n\n',
        reply_markup=keyboards.trial_button.as_markup(),
        parse_mode='html'
    )


@dp.callback_query(F.data == 'start_trial')
async def start_trial(call: CallbackQuery):
    await send_video(
        call.message.chat.id,
        'trial.mp4',
        caption='<b>❗️Apke Pass Apka Last Mauka Hai!</b>\n\n'
                'Aap aram se 5,000 se 20,000rs har din kama sakte ho! Par aap is mauke ko miss kar rahe ho\n\n'
                '📹 Is video ko dobara dekho taki aap ache se samaj pao ki yeh BOT kaise work karta hai\n\n'
                '<b>✍️Apko Bas"</b>\n\n'
                '1)  "📲REGISTER" Par click karna hai aur 1WIN par ek account '
                'banana hai jisme bas 10 sec lagenge\n\n'
                '2) Iske baad BOT apne aap hi activate ho jayega\n\n'
                'Main Apka Wait Kar Raha Hoon!\n\n',
        parse_mode='html',
        reply_markup=keyboards.make_money.as_markup()
    )


@dp.callback_query(F.data == 'make_money')
async def make_money(call: CallbackQuery):
    await send_photo(
        call.message.chat.id,
        'reg.png',
        caption='✅ <b>BADHIYA!</b>✅\n\n'
                '1) Click <b>"📲REGISTER" aur 1WIN mein register kare</b>\n'
                f'<b>LINK</b>: {URL}\n'
                '<b>PROMOCODE</b>: \n'
                f'<b>{CODE}</b>\n'
                'Use promocode it’s very important for activation bot\n\n'
                '<b>❓Is registration ki jarurat kyu hai'
                '- Registration isliye jaruri hai taki apka yaha account ho aur aap Aviator khel paye</b>',
        parse_mode='html',
        reply_markup=keyboards.register_button.as_markup()
    )

    await asyncio.sleep(3)

    await send_video(
        call.message.chat.id,
        'bro.mp4',
        caption='🔥🔥Bro, here\'s the proof 💯💯\n'
                '💵Hurry up write ME to get the bot and start earning🤑🤑',
        reply_markup=keyboards.bro.as_markup()
    )


asyncio.run(dp.start_polling(bot))
