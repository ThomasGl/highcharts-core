from typing import Optional
from decimal import Decimal

import datetime

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.cartesian import CartesianData
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.partial_fill import PartialFillOptions


class BarData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in a column or bar
    graph context."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._dash_style = None
        self._point_width = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.dash_style = kwargs.pop('dash_style', None)
        self.point_width = kwargs.pop('point_width', None)

        super().__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each column or bar. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for bar or column. Defaults to
        :obj:`None <python:None>`.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a recognized value'
                                                  f', but received: {value}')
            self._dash_style = value

    @property
    def point_width(self) -> Optional[int | float | Decimal]:
        """A pixel value specifying a fixed width for the column or bar. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If specified, overrides the :meth:`point_width <BaseBarOptions.point_width>`
          provided for the series as a whole.

        .. note::

          The ``point_width`` affects the dimension that is *not* based on the point
          value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_width

    @point_width.setter
    def point_width(self, value):
        self._point_width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'point_width': as_dict.pop('pointWidth', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'dashStyle': self.dash_style,
            'pointWidth': self.point_width,
        }

        parent_as_dict = super().to_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class WaterfallData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in a waterfall
    chart."""

    def __init__(self, **kwargs):
        self._is_intermediate_sum = None
        self._is_sum = None

        self.is_intermediate_sum = kwargs.pop('is_intermediate_sum', None)
        self.is_sum = kwargs.pop('is_sum', None)

        super().__init__(**kwargs)

    @property
    def is_intermediate_sum(self) -> Optional[bool]:
        """When ``True``, the point acts as a summary column for the values added or
        subtracted since the last intermediate sum, or since the start of the series.
        Defaults to :obj:`None <python:None>`, which is interpreted as ``False``.

        .. warning::

          The ``y`` value is ignored.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._is_intermediate_sum

    @is_intermediate_sum.setter
    def is_intermediate_sum(self, value):
        if value is None:
            self._is_intermediate_sum = None
        else:
            self._is_intermediate_sum = bool(value)

    @property
    def is_sum(self) -> Optional[bool]:
        """When ``True``, the point displays the total sum across the entire series.
        Defaults to :obj:`None <python:None>`, which is interpreted as ``False``.

        .. warning::

          The ``y`` value is ignored.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._is_sum

    @is_sum.setter
    def is_sum(self, value):
        if value is None:
            self._is_sum = None
        else:
            self._is_sum = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'is_intermediate_sum': as_dict.pop('isIntermediateSum', None),
            'is_sum': as_dict.pop('isSum', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'isIntermediateSum': self.is_intermediate_sum,
            'isSum': self.is_sum,
        }

        parent_as_dict = super().to_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class WindBarbData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in a windbarb
    chart."""

    def __init__(self, **kwargs):
        self._direction = None
        self._value = None

        self.direction = kwargs.pop('direction', None)
        self.value = kwargs.pop('value', None)

        super().__init__(**kwargs)

    @property
    def direction(self) -> Optional[int | float | Decimal]:
        """The windirection in degrees, where 0 is north (pointing towards south).
        Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = validators.numeric(value, allow_empty = True)

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The wind speed in meters per second. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`WindBarbData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :class:`WindBarbData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'WindBarbData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(x = None,
                             value = None,
                             direction = None,
                             y = None)
            elif checkers.is_iterable(item):
                if len(item) == 4:
                    as_dict = {
                        'x': item[0],
                        'value': item[1],
                        'direction': item[2],
                        'y': item[3]
                    }
                elif len(item) == 3:
                    as_dict = {
                        'x': item[0],
                        'value': item[1],
                        'direction': item[2]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 4D or 3D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a WindBarb Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')

            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'direction': as_dict.pop('direction', None),
            'value': as_dict.pop('value', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'direction': self.direction,
            'value': self.value,
        }

        parent_as_dict = super().to_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class XRangeData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in an X-Range
    series."""

    def __init__(self, **kwargs):
        self._partial_fill = None
        self._x2 = None

        self.partial_fill = kwargs.pop('partial_fill', None)
        self.x2 = kwargs.pop('x2', None)

        super().__init__(**kwargs)

    @property
    def partial_fill(self) -> Optional[PartialFillOptions]:
        """A partial fill for the data point, typically used to visualize how much of a
        task is performed. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`PartialFillOptions` or :obj:`None <python:None>`
        """
        return self._partial_fill

    @partial_fill.setter
    @class_sensitive(PartialFillOptions)
    def partial_fill(self, value):
        self._partial_fill = value

    @property
    def x(self) -> Optional[str | datetime.date | datetime.datetime | int | float | Decimal]:
        """The starting X-value of the range point. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the point's position on the x-axis will be
        automatically determined based on its position in the series'
        :meth:`data <SeriesBase.data>` array. The first point will be given an ``x`` value
        of ``0``, or the series' :meth:`point_start <SeriesBase.point_start>` value.
        Each subsequent point will be incremented either by ``1`` or the value of
        :meth:`point_interval <SeriesBase.point_interval>`.

        :rtype: numeric or :class:`str <python:str>` or
          :class:`date <python:datetime.date>` or
          :class:`datetime <python:datetime.datetime>` or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        if value is None:
            self._x = None
        else:
            if checkers.is_datetime(value):
                value = validators.datetime(value)
            elif checkers.is_date(value):
                value = validators.date(value)
            elif checkers.is_numeric(value):
                value = validators.numeric(value)
            else:
                value = validators.string(value)

            self._x = value

    @property
    def x2(self) -> Optional[str | datetime.date | datetime.datetime | int | float | Decimal]:
        """The ending X-value of the range point. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the point's position on the x-axis will be
        automatically determined based on its position in the series'
        :meth:`data <SeriesBase.data>` array. The first point will be given an ``x2`` value
        of ``0``, or the series' :meth:`point_start <SeriesBase.point_start>` value.
        Each subsequent point will be incremented either by ``1`` or the value of
        :meth:`point_interval <SeriesBase.point_interval>`.

        :rtype: numeric or :class:`str <python:str>` or
          :class:`date <python:datetime.date>` or
          :class:`datetime <python:datetime.datetime>` or :obj:`None <python:None>`
        """
        return self._x2

    @x2.setter
    def x2(self, value):
        if value is None:
            self._x2 = None
        else:
            if checkers.is_datetime(value):
                value = validators.datetime(value)
            elif checkers.is_date(value):
                value = validators.date(value)
            elif checkers.is_numeric(value):
                value = validators.numeric(value)
            else:
                value = validators.string(value)

            self._x2 = value

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`XRangeData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`XRangeData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'XRangeData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = None
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be an X-Range Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'partial_fill': as_dict.pop('partialFill', None),
            'x2': as_dict.pop('x2', None),

        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'partialFill': self.partial_fill,
            'x2': self.x2,
        }

        parent_as_dict = super().to_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
