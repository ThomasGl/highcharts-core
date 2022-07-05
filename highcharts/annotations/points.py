from typing import Optional, Any
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.metaclasses import HighchartsMeta


class AnnotationPoint(HighchartsMeta):
    """Object representation of a shape point."""

    def __init__(self, **kwargs):
        self._x = None
        self._x_axis = None
        self._y = None
        self._y_axis = None

        self.x = kwargs.pop('x', None)
        self.x_axis = kwargs.pop('x_axis', None)
        self.y = kwargs.pop('y', None)
        self.y_axis = kwargs.pop('y_axis', None)

    @property
    def x(self) -> Optional[Any[int, float, Decimal]]:
        """The x position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def x_axis(self) -> Optional[Any[str, int]]:
        """This number defines which xAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the xAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's x coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None or value == '':
            self._x_axis = None
        else:
            try:
                try:
                    self._x_axis = validators.integer(value)
                except ValueError:
                    self._x_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @property
    def y(self) -> Optional[Any[int, float, Decimal]]:
        """The y position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @property
    def y_axis(self) -> Optional[Any[str, int]]:
        """This number defines which yAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the yAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's y coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None or value == '':
            self._y_axis = None
        else:
            try:
                try:
                    self._y_axis = validators.integer(value)
                except ValueError:
                    self._y_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'x': as_dict.pop('x', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y': as_dict.pop('y', None),
            'y_axis': as_dict.pop('yAxis', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        return {
            'x': self.x,
            'xAxis': self.x_axis,
            'y': self.y,
            'yAxis': self.y_axis
        }
