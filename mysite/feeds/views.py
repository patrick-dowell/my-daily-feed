from test_app.lib.jinja2django import render_to_response
from feeds.models import FeedItem
# Create your views here.

def index(request):
    latest_feed_item_list = FeedItem.objects.all().order_by('-created_at')
    context = { "feed_items": [{"title": x.title, "url": x.url, "created_at": x.created_at} for x in latest_feed_item_list ]}
    return render_to_response("feed.html", context=context)
