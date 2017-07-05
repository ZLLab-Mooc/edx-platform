"""
Django management command to generate a test course in a specific modulestore
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from contentstore.management.commands.utils import user_from_str
from contentstore.views.course import create_new_course_in_store
from xmodule.modulestore import ModuleStoreEnum

import json
import random


class Command(BaseCommand):
    """ Generate a basic course """
    help = 'Generate a course with settings on studio'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json',
            action='store',
            dest='json',
            type=str,
            default=None,
            help='A json object with the following fields: store, user, name, organization, number, run'
        )

    def handle(self, *args, **options):
        # Set default course settings
        store = "split"
        user = user_from_str("edx@example.com")
        name = "test-course"
        org = "test-course-generator"
        num = str(random.randint(0, 100))  # Random course number
        run = "1"

        # Set json settings if provided
        if options["json"] is not None:
            settings = json.loads(options["json"])
            if settings["store"] is not None:
                store = settings["store"]
            if settings["user"] is not None:
                user = user_from_str(settings["user"])
            if settings["name"] is not None:
                name = settings["name"]
            if settings["organization"] is not None:
                org = settings["organization"]
            if settings["number"] is not None:
                num = settings["number"]
            if settings["run"] is not None:
                run = settings["run"]

        # Create the course
        new_course = create_new_course_in_store(store, user, org, num, run, {'display_name': name})
        self.stdout.write(u"Created {}".format(unicode(new_course.id)))
