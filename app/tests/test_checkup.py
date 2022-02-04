from django.test import TestCase
from wagtail.core.models import Site
from wagtail_metrics.checkup import Checkup
from wagtail_metrics import constants
from app.models import HomePage


class TestCheckup(TestCase):
    def setUp(self):
        homepage = HomePage.objects.get(url_path='/home/')
        homepage.char_field = "Test char field"
        homepage.stream_field = [
            ('block', {
                'title': "generic title",
                'description': "different description 1",
            })
        ]
        homepage.save()

        homepage_child = HomePage(
            title="CMS",
            slug='cms',
            char_field="Test char field",
            stream_field=[
                ('block', {
                    'title': "generic title",
                    'description': "different description 2",
                })
            ]
        )
        homepage.add_child(instance=homepage_child)

        homepage_child_child = HomePage(
            title="Wagtail",
            slug='wagtail',
            char_field="Test char field",
            stream_field=[
                ('block', {
                    'title': "generic title",
                    'description': "different description 3",
                })
            ]
        )
        homepage_child.add_child(instance=homepage_child_child)

        site = Site.objects.get(hostname='localhost')
        site.port = 443
        site.hostname = 'www.snoweb.io'
        site.save()

        self.checkup = Checkup([
            'wagtail_page',
            'request',
            # 'google_page_speed'
        ])
        for site in Site.objects.all():
            self.checkup.add_site(site)
        self.checkup_dict = self.checkup.__dict__()

    def test_default_exclude_field(self):
        self.assertNotIn(constants.WAGTAIL_METRICS_DEFAULT_EXCLUDE[0], self.checkup_dict)

    def test_wagtail_page_field(self):
        self.assertIn('locale', self.checkup_dict)

    def test_wagtail_page_char_field(self):
        self.assertIn('char_field', self.checkup_dict)
        self.assertEqual(3, self.checkup_dict['char_field']['counter'])

    def test_wagtail_page_stream_field(self):
        field_title_name = 'stream_field%sblock%stitle' % (
            constants.WAGTAIL_METRICS_SEPARATOR,
            constants.WAGTAIL_METRICS_SEPARATOR
        )
        self.assertIn(field_title_name, self.checkup_dict)
        self.assertEqual(
            3,
            self.checkup_dict[field_title_name]['values']['generic title']['counter']
        )
        field_description_name = 'stream_field%sblock%sdescription' % (
            constants.WAGTAIL_METRICS_SEPARATOR,
            constants.WAGTAIL_METRICS_SEPARATOR
        )
        self.assertIn(field_description_name, self.checkup_dict)
        self.assertEqual(
            1,
            self.checkup_dict[field_description_name]['values']['different description 1']['counter']
        )

    def test_wagtail_page_stream_field_initialize(self):
        field_title_name = 'stream_field%sblock_never_used%stitle' % (
            constants.WAGTAIL_METRICS_SEPARATOR,
            constants.WAGTAIL_METRICS_SEPARATOR
        )
        self.assertIn(field_title_name, self.checkup_dict)
        self.assertEqual(
            0,
            self.checkup_dict[field_title_name]['counter']
        )

    def test_request_status_code(self):
        field_status_code_name = 'request%sstatus_code' % constants.WAGTAIL_METRICS_SEPARATOR
        self.assertIn(field_status_code_name, self.checkup_dict)
        self.assertEqual(
            3,
            self.checkup_dict[field_status_code_name]['counter']
        )

    def test_write_file_json(self):
        f = open("metrics.json", "w")
        f.write(self.checkup.to_json())
        f.close()
