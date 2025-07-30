from PIL import Image

def make_thumb(image):
    """
    Create a high-quality thumbnail from a PIL Image.
    
    Args:
        image (PIL.Image.Image): Input image
        
    Returns:
        PIL.Image.Image: High-quality thumbnail with size 100x100
    """
    # Create a copy to avoid modifying the original image
    thumb = image.copy()
    
    # Create thumbnail with size 100x100, maintaining aspect ratio
    # LANCZOS provides high-quality resampling
    thumb.thumbnail((100, 100), Image.Resampling.LANCZOS)
    
    return thumb