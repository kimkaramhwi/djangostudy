import json

from django.http  import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        # Json -> dictionary
        data      = json.loads(request.body)
        Owner.objects.create(
            id    = data['id'],
            name  = data['name'],
            email = data['email'],
            age   = data['age']
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results  = []

        for owner in owners:
           results.append(
               {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class DogsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        Dog.objects.create(
            owner_id = Owner.objects.get(id=int(data['owner'])).id,
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
                   "owner" : Owner.objects.get(id=dog.owner_id).id,
                   "name" : dog.name,
                   "age" : dog.age
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class OwnersDogsView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        results  = []

        for dog in dogs:
           results.append(
                {
                   "name" : Owner.objects.get(id=dog.owner_id).name,
                   "email" : Owner.objects.get(id=dog.owner_id).email,
                   "age" : Owner.objects.get(id=dog.owner_id).age,
                   "dog_name" : dog.name,
                   "dog_age" : dog.age
                }
            )
       
        return JsonResponse({'resutls':results}, status=200)