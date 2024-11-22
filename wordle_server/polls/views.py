from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from . import word_dictionary as wd
from enchant import Dict as enDict
#from random import randrange

WORD_LENGTH = 5
check_word = enDict("en_US")

# Create your views here.

def index(request):
    return HttpResponse("Index!")

def randomRange(request: HttpRequest):
    maxRange = 1000 + len(wd.word_dict) - 1
    result = {
        "data": {
            "minRange": 1000,
            "maxRange": maxRange
        },
        "message": "",
        "status": "success",
        "code": 200
    }
    return JsonResponse(result)

def randomWord(request: HttpRequest):
    guessWord = request.GET.get("word", "")

    result = {
        "data": [],
        "message": "",
        "status": "",
        "code": 200
    }

    if not guessWord:
        result["message"] = "Please input your word"
        result["status"] = "empty"
        result["code"] = 402
        return JsonResponse(result)
    
    if len(guessWord) != 5:
        result["message"] = "Please input 5 letters English word"
        result["status"] = "error"
        result["code"] = 402
        return JsonResponse(result)
    
    if not check_word.check(guessWord):
        result["message"] = guessWord.upper() + " is not an English word"
        result["status"] = "error"
        result["code"] = 402
        return JsonResponse(result)

    seed = int("1234" if not request.GET.get("seed", "1234") else request.GET.get("seed", "1234"))

    if seed < 1000 or seed >= (1000 + len(wd.word_dict)):
        seed = 1234

    word = wd.word_dict[str(seed)].lower()

    list_response = [
        {
            "slot": 0,
            "guess": guessWord[0],
            "result": ""
        },
        {
            "slot": 1,
            "guess": guessWord[1],
            "result": ""
        },
        {
            "slot": 2,
            "guess": guessWord[2],
            "result": ""
        },
        {
            "slot": 3,
            "guess": guessWord[3],
            "result": ""
        },
        {
            "slot": 4,
            "guess": guessWord[4],
            "result": ""
        }
    ]

    for i in range(0, len(guessWord)):
        if guessWord[i] == word[i]:
            list_response[i]["result"] = "correct"
        elif guessWord[i] in word:
            list_response[i]["result"] = "present"
        else:
            list_response[i]["result"] = "absent"
            

    result["data"] = list_response
    result["message"] = "Original word is " + word
    result["status"] = "success"
    return JsonResponse(result)