import json

from django.http  import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        try:
            # Json -> dictionary
            data      = json.loads(request.body)
            Owner.objects.create( # owner 객체 생성
#               id    = data['id'], 
                name  = data['name'], # 받은 데이터의 name을 name에 저장
                email = data['email'], # 받은 데이터의 email을 email에 저장
                age   = data['age'] # 받은 데이터의 age을 age에 저장
            )
            return JsonResponse({'messasge':'created'}, status=201) # 잘 생성되었을 때 반환되는 메시지
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400) # 키에러시 반환되는 메시지

    def get(self, request):
        owners = Owner.objects.all() # owner테이블의 모든 레코드를 불러온다.
        results  = [] # owner를 출력할 리스트

        for owner in owners:
           results.append(
               {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age
               }
           )
       
        return JsonResponse({'resutls':results}, status=200) # OK

class DogsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        if not Owner.objects.filter(id=data['owner_id']).exists(): 
            return JsonResponse({'MESSAGE': "Owner Does Not Exist"}, status=404)
            # 존재하지 않는 주인 아이디를 받았을 때 404 에러 반환

        Dog.objects.create(
            # 데이터를 받을 때 이미 존재하지 않는 주인값을 입력하면 위에서 오류가 반환되므로 아래와 같이 나타낼 필요가 없다.
#           owner_id = Owner.objects.get(id=int(data['owner'])).id,
            owner_id = data.owner.id, # 정참조
            name  = data['name'],
            age   = data['age']
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results  = []

        for dog in dogs:
           results.append(
               {
                   "owner" : dog.owner.id, # 정참조
                   "name" : dog.name,
                   "age" : dog.age
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class OwnersDogsView(View):
    def get(self, request):
        owners = Owner.objects.all() # owner테이블의 모든 레코드를 도는 owners
        results  = []

        for owner in owners:
            dog_list = []
            # 역참조 -> owners 안에 있는 각각의 owner에 맞는 dog 객체를 전부 가져온다.
            dogs = owner.dog_set.all() 
            # 같은 주인을 가진 강아지들의 이름과 나이를 강아지 리스트에 추가
            for dog in dogs: # 모든 주인을 다 돌때까지 리스트가 각각의 주인이 가진 강아지 리스트로 추가된다.
                dog_list.append({
                    "name" : dog.name,
                    "age" : dog.age
                })
            results.append(
                {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age,
                   "dog" : dog_list
                }
            )
       
        return JsonResponse({'resutls':results}, status=200)