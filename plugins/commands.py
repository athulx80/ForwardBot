#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📺 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/+jG8skQAT68I5MmRl'),
        InlineKeyboardButton('🔊 𝙶𝚁𝙾𝚄𝙿', url='https://t.me/+Ar6gmqeNjFRkYTRl')
    ],[
        InlineKeyboardButton('🌐 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴', url='https://github.com/athulx80/ForwardBot')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('🔒𝙲𝙻𝙾𝚂𝙴', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('📺𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/+jG8skQAT68I5MmRl'),
        InlineKeyboardButton('🔒𝙲𝙻𝙾𝚂𝙴', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode="html"
    )

        
