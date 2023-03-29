import glob
from PIL import Image

def make_gif(frame_folder, format, gif_name):
    """Creates a gif out of a image folder
    
    Args:
        frame_folder: path to the folder containing the images
        format: source image file format (jpeg, png)
        gif_name: file name of the gif output
    
    Returns:
        Pandas dataframe containing a list of images for manual selection 
        and download.
    """
    frames = [Image.open(image) for image in sorted(glob.glob(f"{frame_folder}/*.{format}"))]
    frame_one = frames[0]
    frame_one.save(f'{gif_name}.gif', format="GIF", append_images=frames,
               save_all=True, duration=300, loop=0)
    

make_gif("/home/ehwaz/Documents/Spiced/celerleve-sentinel/data/images/Brazil_SP_PrecipitationViz", "png", "weather_viz")