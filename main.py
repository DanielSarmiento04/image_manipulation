import reflex as rx
import replicate

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

def image_gen():
    return rx.vstack(
        rx.skeleton(
            rx.flex(
                rx.cond(
                    ImageGenState.image_url,
                    rx.image(
                        src=ImageGenState.image_url,
                    ),
                    rx.flex(
                        rx.icon("image", size=26, color=rx.color("slate", 7)),
                    ),
                ),
            ),
            loading=ImageGenState.processing,
        ),
        rx.form(
            rx.input(
                placeholder="What do you want to see?",
                name="prompt"
            ),
            rx.button(
                "Generate",
                loading=ImageGenState.processing,
                type="submit",
            ),
            reset_on_submit=True,
            on_submit=ImageGenState.get_image,
        )
    )

app = rx.App()
app.add_page(image_gen)