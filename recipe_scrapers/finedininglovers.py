# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def title(self):
        return self.schema.title()

    def author(self):
        container = self.soup.find("div", {"class": "author-name"})
        if container:
            return container.find("a").get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
<<<<<<< HEAD
        return self.schema.instructions()
=======
        instructions_parent = self.soup.find(
            "div", {"class": "field--name-field-recipe-para-steps"}
        )

        if instructions_parent is not None:
            instructions = instructions_parent.findAll(
                "div", {"class": "paragraph--type--recipe-step"}
            )
        else:
            instructions_parent = self.soup.find(
                "div", {"class": "ante-body"}
            )
            instructions = instructions_parent.findAll({"li", "p"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
>>>>>>> fix finedininglovers.com instruction parsing

    def image(self):
        return self.schema.image()
