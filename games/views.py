import json

from django.http import HttpRequest,JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Game


class GameView(View):
    def get(self,request:HttpRequest,id)->JsonResponse:
        get_game = get_object_or_404(Game,pk = id)
        return JsonResponse(get_game.to_dict())
    
    def post(self,request:HttpRequest)->JsonResponse:
        data = json.loads(request.body.decode())

        title = data.get('title')
        location = data.get('location')
        start_date = data.get('start_date')
        description = data.get('description')

        if title is None:
            return JsonResponse({'title':'Required'},status = 400)
        if location is None:
            return JsonResponse({'location':'Required'},status = 400)
        if start_date is None:
            return JsonResponse({'start_date':'Required'},status = 400)
        if len(title) > 200:
            return JsonResponse({'length':200},status = 400)
        if len(location) > 100:
            return JsonResponse({'length':100},status = 400)
        
        new_game_data = Game(
            title = title,
            location = location,
            start_date = start_date,
            description = description
        )

        new_game_data.save()
        return JsonResponse(data=new_game_data.to_dict(),status = 201)
    
    def patch(self,request:HttpRequest,id)->JsonResponse:
        get_game = get_object_or_404(Game,pk=id)
        data = json.loads(request.body.decode())

        get_game.title = data.get('title',get_game.title)
        get_game.location = data.get('location',get_game.location)
        get_game.start_date = data.get('start_date',get_game.start_date)
        get_game.description = data.get('description',get_game.description)
        
        get_game.save()
        return JsonResponse({
            "description": "Updated tournament info"
        })
    
    def delete(self,request:HttpRequest,id)->JsonResponse:
        get_game = get_object_or_404(Game,pk = id)

        if get_game.score:
            return JsonResponse({
                    "error": "Cannot delete game with existing scores. Tournament has active games."
                    },status = 400)
                            