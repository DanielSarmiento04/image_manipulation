import reflex as rx 
import replicate


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


class ImageGenState(rx.State):

    image_url = ""
    processing = False

    def get_image(self, form_data):
        prompt = form_data["prompt"]
        if prompt == "":
            return

        self.processing = True
        yield

        input = {"prompt": prompt}
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input=input,
        )
        self.image_url = output[0]
        self.processing = False

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=State.increment,
        ),
        spacing="4",
    )

app = rx.App()
app.add_page(index)