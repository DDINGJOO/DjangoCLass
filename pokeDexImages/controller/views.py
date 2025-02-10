from rest_framework.views import APIView

from pokeDexImages.service.PokeDexImageService import PokeDexImageService
from rest_framework.response import Response

class PokeDexImageView(APIView):
    def get(self, request, number):
        service = PokeDexImageService()
        pokemon_image = service.get_pokemon_image_by_id(int(number))
        return Response(pokemon_image)

class PokeDexImagePostView(APIView):
    def post(self, request):
        service = PokeDexImageService()
        pokemon_image = service.get_pokemon_image_by_name(request.data['name'])
        return Response(pokemon_image)


class PokeDexImageDeleteView(APIView):
    def delete(self, request, number):
        service = PokeDexImageService()
        service.delete_pokemon_image_by_id(int(number))
        return Response(status=204)

