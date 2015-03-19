from django.conf.urls import patterns, url
 
from notes import views, forms
 
urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /archive.
    url(r'^archive/$', views.ArchiveIndexView.as_view(), name='archive'),
    # ex: /pinned/
    url(r'^pinned/$', views.PinnedIndexView.as_view(), name='pinned'),
    # ex: /create/
    url(r'^create$', views.NoteAction.as_view(), name='create_note'),
    url(r'^(?P<note_id>\d+)/update$', views.NoteAction.as_view(), name='update_note'),
    # ex: /5/edit
    url(r'^(?P<note_id>\d+)/edit$', views.EditFormView.as_view(), name='edit_note'),

)