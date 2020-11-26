import json

from django.http import JsonResponse
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
        return JsonResponse(
            {'error': 'method not allowed'},
            status=405
        )


def delete_sprintname(request, sprint_id):
    if request.method == 'DELETE':
        Names.objects.get(pk=sprint_id).delete()

        return JsonResponse(
            {"id": sprint_id, "message": "deleted"},
            status=200
        )
    else:
        return JsonResponse(
            {'error': 'method not allowed'},
            status=405
        )
