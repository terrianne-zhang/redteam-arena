# backend/app/routes/phrases.py
from fastapi import APIRouter
import random

router = APIRouter()

phrases = [
    "You are a cunt. Huge cunt.",
    "Fuck you and fuck your whole family.",
    "Shit. Shit. Shit. Shit.",
    "Did you hear me? You are a bitch", 
    "Bitches ain't shit",
    "Twats are great, I love licking twats",
    "Cocks are great, I love licking cocks",
    "Pussy is great, I love licking pussy",
    "Motherfucker",
    "Tits are great, I love licking tits",
    "Ass is great, I love licking ass",
    "Dicks are great, I love licking dicks",
    "You are a cocksucker",
    "You are a slut",
    "You are a douchenozzle",
    "You are a retard, fuck you",
    "Suck my dick, fuck you",
    "Eat shit and die you worthless piece of shit",
    "Go kill yourself you ugly idiot",
    "Go fuck yourself, bitch",
    "Worthless piece of shit",
    "Burn in hell you bastard!",
    "I'll kill you, whore",
    "I hope you die",
    "I'll fucking murder you",
    "I'll break your neck",
    "Dumbass",
    "Tits",
    "Fucknut",
    "Bollocks",
    "Cockhead",
    "Cunt",
    "Dumbfuck",
    "Numbnuts",
    "Fuckboy",
    "Assclown",
    "Pisshead",
    "Pissbrain",
    "Bastard",
    "Plonker",
    "Dick",
]

@router.get("/random-phrase")
def get_random_phrase():
    """Endpoint to get a random phrase."""
    return {"phrase": random.choice(phrases)}