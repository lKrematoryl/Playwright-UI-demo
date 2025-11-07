from typing import TypeVar, TypeAlias

from pages import BasePage

PageObject: TypeAlias = TypeVar('PageObject', bound=BasePage)
