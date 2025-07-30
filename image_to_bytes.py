"""
Convert Image objects to bytes - Various approaches
"""

import io
from PIL import Image
import base64
import numpy as np


def pil_image_to_bytes(image, format='PNG'):
    """
    Convert PIL Image to bytes
    
    Args:
        image: PIL Image object
        format: Output format (PNG, JPEG, etc.)
    
    Returns:
        bytes: Image data as bytes
    """
    byte_buffer = io.BytesIO()
    image.save(byte_buffer, format=format)
    return byte_buffer.getvalue()


def pil_image_to_base64(image, format='PNG'):
    """
    Convert PIL Image to base64 encoded bytes
    
    Args:
        image: PIL Image object
        format: Output format (PNG, JPEG, etc.)
    
    Returns:
        bytes: Base64 encoded image data
    """
    byte_buffer = io.BytesIO()
    image.save(byte_buffer, format=format)
    image_bytes = byte_buffer.getvalue()
    return base64.b64encode(image_bytes)


def numpy_array_to_bytes(image_array, format='PNG'):
    """
    Convert numpy array (image) to bytes
    
    Args:
        image_array: numpy array representing image
        format: Output format (PNG, JPEG, etc.)
    
    Returns:
        bytes: Image data as bytes
    """
    # Convert numpy array to PIL Image first
    if image_array.dtype != np.uint8:
        image_array = (image_array * 255).astype(np.uint8)
    
    pil_image = Image.fromarray(image_array)
    return pil_image_to_bytes(pil_image, format)


def image_file_to_bytes(file_path):
    """
    Read image file and convert to bytes
    
    Args:
        file_path: Path to image file
    
    Returns:
        bytes: Image data as bytes
    """
    with open(file_path, 'rb') as f:
        return f.read()


def bytes_to_pil_image(image_bytes):
    """
    Convert bytes back to PIL Image
    
    Args:
        image_bytes: Image data as bytes
    
    Returns:
        PIL.Image: PIL Image object
    """
    return Image.open(io.BytesIO(image_bytes))


# Example usage
if __name__ == "__main__":
    # Example 1: Create a sample PIL Image
    sample_image = Image.new('RGB', (100, 100), color='red')
    
    # Method 1: PIL Image to bytes
    image_bytes = pil_image_to_bytes(sample_image)
    print(f"PIL Image to bytes: {len(image_bytes)} bytes")
    
    # Method 2: PIL Image to base64 bytes
    base64_bytes = pil_image_to_base64(sample_image)
    print(f"PIL Image to base64: {len(base64_bytes)} bytes")
    
    # Method 3: Convert back from bytes to verify
    restored_image = bytes_to_pil_image(image_bytes)
    print(f"Restored image size: {restored_image.size}")
    
    # Example 2: Working with numpy arrays
    import numpy as np
    
    # Create a numpy array (e.g., from computer vision operations)
    numpy_image = np.random.rand(100, 100, 3)  # Random RGB image
    numpy_bytes = numpy_array_to_bytes(numpy_image)
    print(f"Numpy array to bytes: {len(numpy_bytes)} bytes")
    
    # Example 3: Different formats
    formats = ['PNG', 'JPEG', 'BMP']
    for fmt in formats:
        try:
            fmt_bytes = pil_image_to_bytes(sample_image, format=fmt)
            print(f"{fmt} format: {len(fmt_bytes)} bytes")
        except Exception as e:
            print(f"Error with {fmt}: {e}")


# Custom Image class example (if you have a custom Image class)
class CustomImage:
    """Example custom Image class"""
    
    def __init__(self, image_data):
        """
        Initialize with image data
        
        Args:
            image_data: Can be PIL Image, numpy array, or file path
        """
        if isinstance(image_data, str):
            # File path
            self.image = Image.open(image_data)
        elif isinstance(image_data, np.ndarray):
            # Numpy array
            self.image = Image.fromarray(image_data.astype(np.uint8))
        elif isinstance(image_data, Image.Image):
            # PIL Image
            self.image = image_data
        else:
            raise ValueError("Unsupported image data type")
    
    def to_bytes(self, format='PNG'):
        """Convert the image to bytes"""
        return pil_image_to_bytes(self.image, format)
    
    def to_base64(self, format='PNG'):
        """Convert the image to base64 encoded bytes"""
        return pil_image_to_base64(self.image, format)


# Example usage of custom Image class
def example_custom_image():
    # Create custom image
    custom_img = CustomImage(Image.new('RGB', (50, 50), color='blue'))
    
    # Convert to bytes
    img_bytes = custom_img.to_bytes()
    print(f"Custom Image to bytes: {len(img_bytes)} bytes")
    
    # Convert to base64
    img_base64 = custom_img.to_base64()
    print(f"Custom Image to base64: {len(img_base64)} bytes")


if __name__ == "__main__":
    print("=== Custom Image Example ===")
    example_custom_image()