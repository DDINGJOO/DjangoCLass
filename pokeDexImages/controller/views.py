from rest_framework.views import APIView

from pokeDexImages.service.PokeDexImageService import PokeDexImageService
from rest_framework.response import Response

class PokeDexImageView(APIView):
    def get(self, request, number):
        service = PokeDexImageService()
        pokemon_image = service.get_pokemon_image_by_id(int(number))
        return Response(pokemon_image)

