import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO
from IPython.display import display
from IPython.core.display import Image as IPImage

class PokeDexImage:
    def __init__(self, pokemon_id):
        """
        - pokemon_id: 포켓몬 ID
        - save_directory: pokeDexImages/images/ 폴더에 저장
        """

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.save_directory = os.path.join(base_dir, "images")
        self.pokemon_id = pokemon_id
        self.image_path = None
        self.fetch_image()
        self.save_image_on_localPath()

    def fetch_image(self):
        load_dotenv()
        base_url = os.environ.get("POKEAPI_IMAGE_URL")
        if base_url is None:
            raise ValueError("환경 변수 POKEAPI_IMAGE_URL이 설정되지 않았습니다.")

        image_url = f"{base_url}/{self.pokemon_id}.png"
        print(f"Image URL: {image_url}")
        return image_url

    def save_image_on_localPath(self):
        # pokeDexImages/images 폴더가 없으면 생성
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)  # 폴더 자동 생성

        response = requests.get(self.fetch_image())
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            self.image_path = os.path.join(self.save_directory, f"{self.pokemon_id}.png")
            img.save(self.image_path)
            print(f"✅ 이미지가 저장됨: {self.image_path}")
        else:
            print(f"이미지를 가져오는 데 실패했습니다. HTTP 상태 코드: {response.status_code}")
        return self.image_path

    def display_image(self):
        if self.image_path and os.path.exists(self.image_path):
            display(IPImage(self.image_path))
        else:
            print("저장된 이미지가 없습니다. 먼저 `save_image_by_api()`를 실행하세요.")

if __name__ == "__main__":
    pokeimage = PokeDexImage(6)
    pokeimage.save_image_on_localPath()
    pokeimage.display_image()
