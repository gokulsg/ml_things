# coding=utf-8
# Copyright 2020 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Functions related to plotting"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def plot_array(array, step_size=1, use_label=None, use_title=None, use_xlabel=None, use_ylabel=None,
               style_sheet='ggplot', use_grid=True, width=3, height=1, use_linestyle='-', use_dpi=20, path=None,
               show_plot=True):
    """Create plot from a single array of values.

    :param array: list of values. Can be of type list or np.ndarray.
    :param step_size: steps shows on x-axis. Change if each steps is different than 1.
    :param use_label: display label of values from array.
    :param use_title: title on top of plot.
    :param use_xlabel: horizontal axis label.
    :param use_ylabel: vertical axis label.
    :param style_sheet: style of plot. Use plt.style.available to show all styles.
    :param use_grid: show grid on plot or not.
    :param width: horizontal length of plot.
    :param height: vertical length of plot.
    :param use_linestyle: what array of styles to use on lines from ['-', '--', '-.', ':'].
    :param use_dpi: quality of image saved from plot. 100 is prety high.
    :param path: path where to save the plot as an image - if set to None no image will be saved.
    :param show_plot: if you want to call `plt.show()`. or not (if you run on a headless server).
    :return:
    """
    # check if `array` is correct format
    if not isinstance(array, list) or isinstance(array, np.ndarray):
        # raise value error
        raise ValueError("`array` needs to be a list of values!")

    if style_sheet in plt.style.available:
        # set style of plot
        plt.style.use(style_sheet)
    else:
        # style is not correct
        raise ValueError("`style_sheet=%s` is not in the supported styles: %s" % (str(style_sheet),
                                                                                  str(plt.style.available)))
    # all linestyles
    linestyles = ['-', '--', '-.', ':']

    # check if linestyle is set right
    if use_linestyle not in linestyles:
        # raise error
        raise ValueError("`linestyle=%s` is not in the styles: %s!" % (str(use_linestyle), str(linestyles)))

    # set steps plotted on x-axis - we can use step if 1 unit has different value
    steps = np.array(range(1, len(array) + 1)) * step_size
    # single plot figure
    plt.subplot(1, 2, 1)
    # plot array as a single line
    plt.plot(steps, array, linestyle=use_linestyle, label=use_label)
    # set title of figure
    plt.title(use_title)
    # set horizontal axis name
    plt.xlabel(use_xlabel)
    # set vertical axis name
    plt.ylabel(use_ylabel)
    # place legend best position
    plt.legend(loc='best') if use_label is not None else None
    # display grid depending on `use_grid`
    plt.grid(use_grid)
    # make figure nice
    plt.tight_layout()
    # get figure object from plot
    fig = plt.gcf()
    # get size of figure
    figsize = fig.get_size_inches()
    # change size depending on height and width variables
    figsize = [figsize[0] * width, figsize[1] * height]
    # set the new figure size
    fig.set_size_inches(figsize)
    # save figure to image if path is set
    fig.savefig(path, dpi=use_dpi) if path is not None else None
    # show plot
    plt.show() if show_plot is True else None

    return


def plot_dict(dict_arrays, step_size=1, use_title=None, use_xlabel=None, use_ylabel=None,
              style_sheet='ggplot', use_grid=True, width=3, height=1, use_linestyles=None, use_dpi=20, path=None,
              show_plot=True):
    """Create plot from a dictionary of lists.
    :param dict_arrays: dictionary of lists or np.array
    :param step_size: steps shows on x-axis. Change if each steps is different than 1.
    :param use_title: title on top of plot.
    :param use_xlabel: horizontal axis label.
    :param use_ylabel: vertical axis label.
    :param style_sheet: style of plot. Use plt.style.available to show all styles.
    :param use_grid: show grid on plot or not.
    :param width: horizontal length of plot.
    :param height: vertical length of plot.
    :param use_linestyles: array of styles to use on line from ['-', '--', '-.', ':'].
    :param use_dpi: quality of image saved from plot. 100 is pretty high.
    :param path: path where to save the plot as an image - if set to None no image will be saved.
    :param show_plot: if you want to call `plt.show()`. or not (if you run on a headless server).
    :return:
    """
    # check if `dict_arrays` is correct format
    if not isinstance(dict_arrays, dict):
        # raise value error
        raise ValueError("`array` needs to be a dictionary of values!")
    for label, array in dict_arrays.items():
        # check if format is correct
        if not isinstance(label, str):
            # raise value error
            raise ValueError("`dict_arrays` needs string keys!")
        if not isinstance(array, list) or isinstance(array, np.ndarray):
            # raise value error
            raise ValueError("`dict_arrays` needs lists values!")
    # make sure style sheet is correct
    if style_sheet in plt.style.available:
        # set style of plot
        plt.style.use(style_sheet)
    else:
        # style is not correct
        raise ValueError("`style_sheet=%s` is not in the supported styles: %s" % (str(style_sheet),
                                                                                  str(plt.style.available)))
    # all linestyles
    linestyles = ['-', '--', '-.', ':']

    if use_linestyles is None:
        # if linestyles is non create same style array
        use_linestyles = ['-'] * len(dict_arrays)
    else:
        # check if linestyle is set right
        for use_linestyle in use_linestyles:
            # check each linestyle
            if use_linestyle not in linestyles:
                # raise error
                raise ValueError("`linestyle=%s` is not in the styles: %s!" % (str(use_linestyle), str(linestyles)))

    # single plot figure
    plt.subplot(1, 2, 1)
    for index, (use_label, array) in enumerate(dict_arrays.items()):
        # set steps plotted on x-axis - we can use step if 1 unit has different value
        steps = np.array(range(1, len(array) + 1)) * step_size
        # plot array as a single line
        plt.plot(steps, array, linestyle=use_linestyles[index], label=use_label)
    # set title of figure
    plt.title(use_title)
    # set horizontal axis name
    plt.xlabel(use_xlabel)
    # set vertical axis name
    plt.ylabel(use_ylabel)
    # place legend best position
    plt.legend(loc='best')
    # display grid depending on `use_grid`
    plt.grid(use_grid)
    # make figure nice
    plt.tight_layout()
    # get figure object from plot
    fig = plt.gcf()
    # get size of figure
    figsize = fig.get_size_inches()
    # change size depending on height and width variables
    figsize = [figsize[0] * width, figsize[1] * height]
    # set the new figure size
    fig.set_size_inches(figsize)
    # save figure to image if path is set
    fig.savefig(path, dpi=use_dpi) if path is not None else None
    # show plot
    plt.show() if show_plot is True else None

    return


def plot_confusion_matrix(y_true, y_pred, classes='', normalize=False, title=None, cmap=plt.cm.Blues, image=None,
                          verbose=0, magnify=1.2, dpi=50):
    """This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    y_true needs to contain all possible labels.

    :param y_true: array labels values.
    :param y_pred: array predicted label values.
    :param classes: array list of label names.
    :param normalize: bool normalize confusion matrix or not.
    :param title: str string title of plot.
    :param cmap: plt.cm plot theme
    :param image: str path to save plot in an image.
    :param verbose: int print confusion matrix when calling function.
    :param magnify: int zoom of plot.
    :param dpi: int clarity of plot.
    :return: array confusion matrix used to plot.

    Note:
        - Plot themes:
        cmap=plt.cm.Blues - used as default.
        cmap=plt.cm.BuPu
        cmap=plt.cm.GnBu
        cmap=plt.cm.Greens
        cmap=plt.cm.OrRd
    """
    if len(y_true) != len(y_pred):
        # make sure lengths match
        raise ValueError("`y_true` needs to have same length as `y_pred`!")

    # Class labels setup. If none, generate from y_true y_pred
    classes = list(classes)
    if classes:
        assert len(set(y_true)) == len(classes)
    else:
        classes = set(y_true)
    # Title setup
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Normalize setup
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    # Print if verbose
    if verbose > 0:
        print(cm)
    # Plot setup
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    plt.grid(False)
    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    fig = plt.gcf()
    figsize = fig.get_size_inches()
    fig.set_size_inches(figsize * magnify)
    if image:
        fig.savefig(image, dpi=dpi)
    return cm
