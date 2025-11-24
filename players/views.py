import json

from django.views import View
from django.http import HttpRequest,JsonResponse

from .models import Player

class PlayerView(View):
    def get(self,request:HttpRequest)->JsonResponse:
        country = request.GET.get('country')
        min_rating = request.GET.get('min_rating')
        search = request.GET.get('search')

        players = Player.objects.all()

        if country:
            players = players.filter(country__icontains=country)
        if min_rating:
            players = players.filter(rating__gte=min_rating)
        if search:
            players = players.filter(nickname__icontains=search)


        data = [player.to_dict_score() for player in players]
        return JsonResponse({"results":data})
    
    def post(self,request:HttpRequest)->JsonResponse:
        data = json.loads(request.body.decode()) 

        nickname = data.get('nickname')
        country = data.get('country')
        rating = data.get('rating')


        if not nickname:
            return JsonResponse({'nickname':'Requires'},status = 400)
        if len(nickname) > 50:
            return JsonResponse({'nickname':'max length 50'})
        
        try:
            Player.objects.get(nickname = nickname)
            return JsonResponse({'nickname':'unique'},status = 400)

        except Player.DoesNotExist:
            if not country:
                return JsonResponse({'country':'Requires'},status = 400)
            if len(country) > 50:
                return JsonResponse({'country':'max length 50'})

            new_player = Player(
                nickname = nickname,
                country = country,
                rating = rating if rating else 0
            )
            new_player.save()

            return JsonResponse(new_player.to_dict(),status = 201)
        
     