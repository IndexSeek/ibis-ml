import ibis.expr.datatypes as dt


def accuracy_score(y_true: dt.Integer, y_pred: dt.Integer) -> float:
    """Calculate the accuracy score of predicted values against true values.

    Parameters
    ----------
    y_true
        Table expression column containing the true labels.
    y_pred
        Table expression column containing the predicted labels.

    Returns
    -------
    float
        The accuracy score, representing the fraction of correct predictions.

    Examples
    --------
    >>> from ibis_ml.metrics import accuracy_score
    >>> import ibis
    >>> ibis.options.interactive = True
    >>> t = ibis.memtable(
    ...     {
    ...         "id": range(1, 13),
    ...         "actual": [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    ...         "prediction": [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    ...     }
    ... )
    >>> accuracy_score(t.actual, t.prediction)
    0.5833333333333334
    """
    return (y_true == y_pred).mean().to_pyarrow().as_py()


def precision_score(y_true: dt.Integer, y_pred: dt.Integer) -> float:
    """Calculate the precision score of predicted values against true values.
    Parameters
    ----------
    y_true
        Table expression column containing the true labels.
    y_pred
        Table expression column containing the predicted labels.

    Returns
    -------
    float
        The precision score, representing the fraction of true positive predictions.
    Examples
    --------
    >>> from ibis_ml.metrics import precision_score
    >>> import ibis
    >>> ibis.options.interactive = True
    >>> t = ibis.memtable(
    ...     {
    ...         "id": range(1, 13),
    ...         "actual": [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    ...         "prediction": [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    ...     }
    ... )
    >>> precision_score(t.actual, t.prediction)
    0.6666666666666666
    """
    true_positive = (y_true & y_pred).sum()
    predicted_positive = y_pred.sum()
    return (true_positive / predicted_positive).to_pyarrow().as_py()


def recall_score(y_true: dt.Integer, y_pred: dt.Integer) -> float:
    """Calculate the recall score of predicted values against true values.
    Parameters
    ----------
    y_true
        Table expression column containing the true labels.
    y_pred
        Table expression column containing the predicted labels.

    Returns
    -------
    float
        The recall score, representing the fraction of true positive predictions.
    Examples
    --------
    >>> from ibis_ml.metrics import recall_score
    >>> import ibis
    >>> ibis.options.interactive = True
    >>> t = ibis.memtable(
    ...     {
    ...         "id": range(1, 13),
    ...         "actual": [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    ...         "prediction": [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    ...     }
    ... )
    >>> recall_score(t.actual, t.prediction)
    0.5714285714285714
    """
    true_positive = (y_true & y_pred).sum()
    actual_positive = y_true.sum()
    return (true_positive / actual_positive).to_pyarrow().as_py()


def f1_score(y_true: dt.Integer, y_pred: dt.Integer) -> float:
    """Calculate the F1 score of predicted values against true values.
    Parameters
    ----------
    y_true
        Table expression column containing the true labels.
    y_pred
        Table expression column containing the predicted labels.

    Returns
    -------
    float
        The F1 score, representing the harmonic mean of precision and recall.

    Examples
    --------
    >>> from ibis_ml.metrics import f1_score
    >>> import ibis
    >>> ibis.options.interactive = True
    >>> t = ibis.memtable(
    ...     {
    ...         "id": range(1, 13),
    ...         "actual": [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    ...         "prediction": [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    ...     }
    ... )
    >>> f1_score(t.actual, t.prediction)
    0.6153846153846154
    """
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    return (2 * precision * recall) / (precision + recall)
