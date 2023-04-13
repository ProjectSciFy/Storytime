from diffusers import DiffusionPipeline
import torch

pipeline = 0

if pipeline == 0:

    generator = DiffusionPipeline.from_pretrained("./stable-diffusion-v1-5")

    generator.to("cuda")

    image = generator("An image of a squirrel in Picasso style").images[0]
    image.save("image_of_squirrel_painting.png")


if pipeline == 1:
    pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

    pipeline.to("cuda")

    image = pipeline("An image of a squirrel in Picasso style").images[0]
    image.save("image_of_squirrel_painting.png")
