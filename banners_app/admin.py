from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget, DateWidget
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Event, Banner, Servant

class ServantResource(resources.ModelResource):
    jp_rateups = fields.Field(
        column_name='jp_rateups',
        attribute='jp_rateups',
        widget=ManyToManyWidget(Banner, field='slug', separator=',')
    )
    na_rateups = fields.Field(
        column_name='na_rateups',
        attribute='na_rateups',
        widget=ManyToManyWidget(Banner, field='slug', separator=',')
    )
    class Meta:
        model = Servant
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('id_num',)

class BannerResource(resources.ModelResource):
    event = fields.Field(
        column_name='event_id',
        attribute='event',
        widget=ForeignKeyWidget(Event, field='slug')
    )
    start_date = fields.Field(
        column_name='start_date',
        attribute='start_date',
        widget=DateWidget('%Y-%m-%d')
    )
    end_date = fields.Field(
        column_name='end_date',
        attribute='end_date',
        widget=DateWidget('%Y-%m-%d')
    )
    class Meta:
        model = Banner
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('slug',)

class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('slug',)

class ServantAdmin(ImportExportModelAdmin):
    resource_classes = [ServantResource]

class BannerAdmin(ImportExportModelAdmin):
    resource_classes = [BannerResource]

class EventAdmin(ImportExportModelAdmin):
    resource_classes = [EventResource]

admin.site.register(Event, EventAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Servant, ServantAdmin)