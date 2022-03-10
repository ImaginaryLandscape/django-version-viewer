try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from .utils import get_accessor_class


accessor = get_accessor_class()


@toolbar_pool.register
class DjangoViewerToolbar(CMSToolbar):
    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            return

        disabled = not accessor.allow_access(self.request)
        current_page_menu = self.toolbar.get_or_create_menu('page')

        current_page_menu.add_modal_item(
            _('View Pip Packages'),
            url=reverse('django_version_viewer_toolbar'),
            disabled=disabled
        )
