from typing import Any

from django.core.management.base import BaseCommand
from django_extensions.management.utils import signalcommand as signalcommand

class Command(BaseCommand):
    help: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(
        self, cache: Any, all_caches: Any, *args: Any, **kwargs: Any
    ) -> None: ...
