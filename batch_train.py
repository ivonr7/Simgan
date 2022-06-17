from email.policy import default
import load_data as ld
import click


@click.command()
@click.option('--batch-size',default=100,help='How many images are passed into the discriminator')
def train_models(batch_size):
    real_data=ld.Data(batch_size//2)



if __name__ == "__main__":
    train_models()