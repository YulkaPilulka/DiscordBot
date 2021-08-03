import discord
from discord.ext import commands


TOKEN = 'NjcyMTMxNTkyMjM1NTE1OTQ1.XxfElA.I0BYyvEcxp0wthFz0Bt6TedAZCM' # token

POST_ID = 675680976617078784 # пост с которого получаются роли 
CHANNEL_ID = 675425591058759734 # ID канала на который заходит человек

ROLES = {
    '💟': 675411087033761852, #shunseisha
    '💗': 675411231191859201, #gurando masuta
    '💜': 675679046285131776, #masuta
    '💙': 675411429054218241, #Daiymaondo ji
    '💚': 675411482409959446, # purachina ji
    '💛': 675412854974840864, #kogane ji
    '🤍': 675412955055259652, #gin ji
    '🤎': 675413762358116362, #seidono ji
    '✅': 675699967075155968, #shin ju
    '🦄': 676904183101652994, #unranked
}
EXCROLES = (
    675387171443572777,
) # роли на которые не распростроняется подсчет

MAX_ROLES_PER_USER = 4