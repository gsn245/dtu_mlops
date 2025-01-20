import torch
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def show_image_and_target(images: torch.Tensor, target: torch.Tensor, show: bool = True) -> None:
    """
    Plot images and their labels in a grid.

        Args:
            images (torch.Tensor): images to plot
            target (torch.Tensor): labels of the images

        Returns:
            None
    PROVIDED
    TODO: Implement self
    TODO: add comments
    """
    row_col = int(len(images) ** 0.5)
    fig = plt.figure(figsize=(10.0, 10.0))
    grid = ImageGrid(fig, 111, nrows_ncols=(row_col, row_col), axes_pad=0.3)
    for ax, im, label in zip(grid, images, target):
        ax.imshow(im.squeeze(), cmap="gray")
        ax.set_title(f"Label: {label.item()}")
        ax.axis("off")
    if show:
        plt.show()