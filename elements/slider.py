from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class SliderElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._slider = page.locator('#slider')

    @property
    def active_slide(self) -> Locator:
        return self._slider.locator('.item.active')

    @property
    def heading(self) -> Locator:
        return self.active_slide.get_by_role('heading', name='AutomationExercise')

    @property
    def subheading(self) -> Locator:
        return self.active_slide.get_by_role('heading', name='Full-Fledged practice website for Automation Engineers')

    @property
    def test_cases_button(self) -> Locator:
        return self.active_slide.get_by_role('link', name='Test Cases')

    @property
    def apis_list_button(self) -> Locator:
        return self.active_slide.get_by_role('link', name='APIs list for practice')

    @property
    def prev_button(self) -> Locator:
        return self._slider.locator('.left.carousel-control')

    @property
    def next_button(self) -> Locator:
        return self._slider.locator('.right.carousel-control')
