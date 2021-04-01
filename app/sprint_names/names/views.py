import json

from datetime import datetime
from django.http import HttpResponseForbidden, JsonResponse
from django.views.generic import DetailView, ListView

from names.models import Names


class NamesDetailView(DetailView):
    model = Names


class NamesListView(ListView):
    context_object_name = 'latest_sprint_name_list'
    model = Names
    paginate_by = 25
    template_name = 'names/list.html'

    def get_queryset(self):
        """Return sprint-names ordered by creation date"""
        return Names.objects.order_by('-created_at')


# API calls
def create_sprintname(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        name = Names(
            author=body_data.get('author'),
            description=body_data.get('description'),
            name=body_data.get('name')
        )
        name.save()

        return JsonResponse(
            body_data,
            status=200
        )
    else:
        return HttpResponseForbidden()


def delete_sprintname(request, sprint_id):
    if request.method == 'DELETE':
        Names.objects.get(pk=sprint_id).delete()

        return JsonResponse(
            {"id": sprint_id, "message": "deleted"},
            status=200
        )
    elif request.method == 'PUT':  # use sprint-name
        Names.objects.filter(pk=sprint_id).update(
            used=True, used_at=datetime.now()
        )

        return JsonResponse(
            {"id": sprint_id, "message": "used"},
            status=200
        )
    else:
        return HttpResponseForbidden()


def search_sprintname(request, query):
    if request.method == 'GET':
        results = Names.objects.filter(name__icontains=query).values()

        return JsonResponse(
            {'results': list(results)},
            status=200
        )
    else:
        return HttpResponseForbidden()
