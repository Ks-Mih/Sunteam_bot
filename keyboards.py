from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import texts

menuKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menuBtn1 = KeyboardButton(texts.MENU_TEST)
menuBtn2 = KeyboardButton(texts.MENU_PEOPLE_INFO)
menuBtn3 = KeyboardButton(texts.MENU_ABOUT_US)
menuBtn4 = KeyboardButton(texts.MENU_RATES)
menuBtn5 = KeyboardButton(texts.MENU_ACCOUNT)
menuKeyboard.row(menuBtn1, menuBtn2)
menuKeyboard.row(menuBtn3, menuBtn4, menuBtn5)

inTestKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menuBtnTest = KeyboardButton('Прервать')
inTestKeyboard.add(menuBtnTest)
