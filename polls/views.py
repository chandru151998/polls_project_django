import json
from django.http import JsonResponse
from .models import Question, Choice
import logging

logging.basicConfig(filename='file.log', filemode='w', level=logging.DEBUG)


def create_quest(request):
    """Function to create question"""
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            quest = Question.objects.create(question_text=data.get('question_text'))
            return JsonResponse({"data": {"id": quest.id, "question_text": quest.question_text}, "message": "Created",
                                 "status": 201}, status=201)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def get_quest(request):
    """Function to view the questions data"""
    try:
        if request.method == "GET":
            question_list = Question.objects.all()
            result = [{"id": quest.id, "question": quest.question_text} for quest in question_list]
            return JsonResponse({"data": result, "message": "OK", "status": 200}, status=200)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def delete_quest(request):
    """Function to delete the question"""
    try:
        data = json.loads(request.body)
        if request.method == "DELETE":
            Question.objects.get(id=data.get('id')).delete()
            return JsonResponse({"data": {}, "message": "Deleted", "status": 204}, status=204)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def update_quest(request):
    """Function to update the question"""
    try:
        data = json.loads(request.body)
        if request.method == "PUT":
            quest = Question.objects.get(id=data.get('id'))
            quest.question_text = data.get("question_text")
            quest.save()
            result = {"id": quest.id, "question": quest.question_text}
            return JsonResponse({"data": result, "message": "Updated", "status": 200}, status=200)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def create_choice(request):
    """Function to create choice"""
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            quest = Question.objects.get(pk=data.get('id'))
            choice = quest.choice_set.create(choice_text=data.get('choice_text'), votes=0)
            result = {"id": choice.id, "choice_text": choice.choice_text}
            return JsonResponse({"data": result, "message": "Created", "status": 201}, status=201)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def get_choice(request):
    """Function to view the choice data"""
    try:
        data = json.loads(request.body)
        if request.method == "GET":
            quest = Question.objects.get(pk=data.get('id'))
            choice_list = quest.choice_set.all()
            result = [{"id": choice.id, "choice": choice.choice_text} for choice in choice_list]
            return JsonResponse({"data": result, "message": "OK", "status": 200}, status=200)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def update_choice(request):
    """Function to update choice"""
    try:
        data = json.loads(request.body)
        if request.method == "PUT":
            choice = Choice.objects.get(pk=data.get('id'))
            choice.choice_text = data.get("choice_text")
            choice.save()
            result = {"choice id": choice.id, "choice": choice.choice_text}
            return JsonResponse({"data": result, "message": "Updated", "status": 200}, status=200)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)


def delete_choice(request):
    """Function to delete the choice"""
    try:
        data = json.loads(request.body)
        if request.method == "DELETE":
            Choice.objects.get(pk=data.get('id')).delete()
            return JsonResponse({"data": {}, "message": "Deleted", "status": 204}, status=204)
        return JsonResponse({"data": {}, "message": "Method not allowed", "status": 405}, status=405)

    except Exception as e:
        logging.exception(e)
        return JsonResponse({"data": {}, "message": str(e), "status": 400}, status=400)
