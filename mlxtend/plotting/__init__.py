# Sebastian Raschka 2014-2020
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

from .checkerboard import checkerboard_plot
from .decision_regions import plot_decision_regions
from .ecdf import ecdf
from .enrichment_plot import enrichment_plot
from .heatmap import heatmap
from .learning_curves import plot_learning_curves
from .pca_correlation_graph import plot_pca_correlation_graph
from .plot_confusion_matrix import plot_confusion_matrix
from .plot_linear_regression import plot_linear_regression
from .plot_sequential_feature_selection import plot_sequential_feature_selection
from .remove_chartjunk import remove_borders
from .scatter import category_scatter
from .scatter_hist import scatter_hist
from .scatterplotmatrix import scatterplotmatrix
from .stacked_barplot import stacked_barplot

__all__ = [
    "plot_learning_curves",
    "plot_decision_regions",
    "plot_confusion_matrix",
    "plot_sequential_feature_selection",
    "plot_linear_regression",
    "remove_borders",
    "category_scatter",
    "heatmap",
    "stacked_barplot",
    "enrichment_plot",
    "checkerboard_plot",
    "ecdf",
    "scatterplotmatrix",
    "plot_pca_correlation_graph",
    "scatter_hist",
]
