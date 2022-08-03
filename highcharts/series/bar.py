from typing import Optional, List

from highcharts import constants
from highcharts.series.base import SeriesBase
from highcharts.series.data.cartesian import CartesianData, Cartesian3DData
from highcharts.series.data.bar import BarData, WaterfallData, WindBarbData, XRangeData
from highcharts.series.data.range import RangeData
from highcharts.plot_options.bar import BaseBarOptions, BarOptions, WaterfallOptions, \
    WindBarbOptions, XRangeOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class BaseBarSeries(SeriesBase, BaseBarOptions):
    """Base class used for all bar/column series."""

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[BarData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`BarData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = BarSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`BarSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`BarSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = BarSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`BarData` objects.

        :rtype: :class:`list <python:list>` of :class:`BarData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = BarData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class BarSeries(BaseBarSeries, BarOptions):
    """Options to apply to a Bar series.

    .. note::

      A bar series is a special type of column series where the columns are horizontal.

    .. figure:: _static/bar-example.png
      :alt: Bar Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', 25),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', 1),
            'group_z_padding': as_dict.pop('groupZPadding', 1),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class ColumnSeries(BarSeries):
    """Options to apply to a Column series types.

    Column series display one column per value along an X axis.

    .. figure:: _static/column-example.png
      :alt: Column Example Chart
      :align: center

    """
    pass


class ColumnPyramidSeries(ColumnSeries):
    """Options to apply to a Column Pyramid series.

    Column Pyramid series display one pyramid per value along an X axis.

    .. hint::

      To display horizontal pyramids, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnpyramid-example.png
          :alt: ColumnPyramid Example Chart
          :align: center

      .. tab:: Stacked

        .. figure:: _static/columnpyramid-example-stacked.png
          :alt: Stacked Column Pyramid Example Chart
          :align: center

      .. tab:: Stacked + Inverted

        .. figure:: _static/columnpyramid-example-stacked-horizontal.png
          :alt: Stacked and Inverted Column Pyramid Example Chart
          :align: center

    """
    @property
    def data(self) -> Optional[List[CartesianData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`CartesianData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              area_series = AreaSeries()
              area_series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`AreaSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`AreaSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              area_series = AreaSeries()
              # Category X-axis
              area_series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              area_series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`CartesianData` objects.

        :rtype: :class:`list <python:list>` of :class:`CartesianData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = CartesianData.from_setter(value)


class ColumnRangeSeries(ColumnSeries):
    """Options to apply to a Column Range series.

    The column range is a cartesian series type with higher and lower Y values along
    an X axis.

    .. hint::

      To display horizontal bars, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnrange-example.png
          :alt: ColumnRange Example Chart
          :align: center

      .. tab:: Horizontal

        .. figure:: _static/columnrange-example-horizontal.png
          :alt: Inverted Column Range Example Chart
          :align: center

    """
    @property
    def data(self) -> Optional[List[RangeData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`RangeData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              area_series = AreaSeries()
              area_series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`AreaSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`AreaSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              area_series = AreaSeries()
              # Category X-axis
              area_series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              area_series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`RangeData` objects.

        :rtype: :class:`list <python:list>` of :class:`RangeData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = RangeData.from_setter(value)


class CylinderSeries(BarSeries):
    """Options to apply to a Cylinder series.

    A cylinder graph is a variation of a 3d column graph. The cylinder graph features
    cylindrical points.

    .. figure:: _static/cylinder-example.png
      :alt: Cylinder Example Chart
      :align: center

    """
    pass


class VariwideSeries(BaseBarSeries):
    """Options to apply to a Variwide series.

    A variwide chart (related to marimekko chart) is a column chart with a variable
    width expressing a third dimension.

    .. tabs::

      .. tab:: Standard Variwide

        .. figure:: _static/variwide-example.png
          :alt: Variwide Example Chart
          :align: center

      .. tab:: Inverted Variwide

        .. figure:: _static/variwide-example-inverted.png
          :alt: Variwide Example Chart
          :align: center

      .. tab:: with Datetime Axis

        .. figure:: _static/variwide-example-datetime.png
          :alt: Variwide Example Chart
          :align: center

    """
    @property
    def data(self) -> Optional[List[Cartesian3DData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`Cartesian3DData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 2D Collection

            .. code-block::

              series = VariwideSeries()
              series.data = [
                  [0, 2],
                  [5, 1],
                  [3, 7],
                  [5, 1]
              ]

            A two-dimensional collection of numerical values, where the dimensions
            correspond to the ``y`` and ``z`` values, respectively. This structure
            automatically infers the ``x`` value, such that if
            :meth:`VariwideSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`VariwideSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 3D Collection

            .. code-block::

              series = VariwideSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0, 2],
                  ['Category B', 5, 1],
                  ['Category C', 3, 7],
                  ['Category D', 5, 1]
              ]

              # Numerical X-axis
              series.data = [
                  [9, 0, 2],
                  [1, 5, 1],
                  [2, 3, 7],
                  [7, 5, 1]
              ]

            A three-dimensional collection of values. Each member of the collection will
            be interpreted as an ``x``, ``y``, and ``z`` value respectively. The ``x``
            value can be a :class:`str <python:str>`,
            :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`Cartesian3DData` objects.

        :rtype: :class:`list <python:list>` of :class:`Cartesian3DData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = Cartesian3DData.from_setter(value)


class WaterfallSeries(ColumnSeries, WaterfallOptions):
    """Options to apply to a Waterfall series.

    A waterfall chart displays sequentially introduced positive or negative values in
    cumulative columns.

    .. tabs::

      .. tab:: Standard Waterfall

        .. figure:: _static/waterfall-example.png
          :alt: Waterfall Example Chart
          :align: center

      .. tab:: Horizontal (Inverted) Waterfall

        .. figure:: _static/waterfall-example-inverted.png
          :alt: Waterfall Example Chart
          :align: center

      .. tab:: Stacked Waterfall

        .. figure:: _static/waterfall-example-stacked.png
          :alt: Waterfall Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[WaterfallData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`WaterfallData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = WaterfallSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`WaterfallSeries.point_start` is :obj:`None <python:None>`, ``x``
            values will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`WaterfallSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = WaterfallSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`WaterfallData` objects.

        :rtype: :class:`list <python:list>` of :class:`WaterfallData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = WaterfallData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', 25),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', 1),
            'group_z_padding': as_dict.pop('groupZPadding', 1),

            'up_color': as_dict.pop('upColor', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class WindBarbSeries(BarSeries, WindBarbOptions):
    """Options to apply to a Wind Barb series.

    Wind barbs are a convenient way to represent wind speed and direction in one
    graphical form. Wind direction is given by the stem direction, and wind speed by
    the number and shape of barbs.

    .. figure:: _static/windbarb-example.png
      :alt: Wind Barb Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[WindBarbData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`WindBarbData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 3D Collection

            .. code-block::

              series = WindBarbSeries()
              series.data = [
                  ['2022-01-01T00:00:00', 3.3, 90],
                  ['2022-01-01T01:00:00', 12.1, 180],
                  ['2022-01-01T02:00:00', 11.1, 270]
              ]

            A three-dimensional collection of numerical values, where the dimensions
            correspond to the :meth:`x <WindBarbData.x>`,
            :meth:`value <WindBarbData.value>`, and
            :meth:`direction <WindBarbData.direction>` values, respectively.

            .. warning::

              This structure assumes the chart is primarily intended to provide windspeed
              data, and does not feature a separate ``y`` value (``y`` will default to
              :obj:`None <python:None>`).

            .. note::

              The ``x`` value can be a :class:`str <python:str>`,
              :class:`date <python:datetime.date>`,
              :class:`datetime <python:datetime.datetime>`, or numeric value.

          .. tab:: 4D Collection

            .. code-block::

              series = WindBarbSeries()
              series.data = [
                  ['2022-01-01T00:00:00', 3.3, 90, 123],
                  ['2022-01-01T01:00:00', 12.1, 180, 456],
                  ['2022-01-01T02:00:00', 11.1, 270, 789]
              ]

            A four-dimensional collection of values, , where the dimensions
            correspond to the :meth:`x <WindBarbData.x>`,
            :meth:`value <WindBarbData.value>`,
            :meth:`direction <WindBarbData.direction>`, and
            :meth:`y <WindBarbData.y>` values, respectively.

            .. note::

              The ``x`` value can be a :class:`str <python:str>`,
              :class:`date <python:datetime.date>`,
              :class:`datetime <python:datetime.datetime>`, or numeric value.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`WindBarbData` objects.

        :rtype: :class:`list <python:list>` of :class:`WindBarbData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = WindBarbData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),

            'data_grouping': as_dict.pop('dataGrouping', None),
            'on_series': as_dict.pop('onSeries', None),
            'vector_length': as_dict.pop('vectorLength', None),
            'x_offset': as_dict.pop('xOffset', None),
            'y_offset': as_dict.pop('yOffset', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class XRangeSeries(BaseBarSeries, XRangeOptions):
    """Options to apply to an X-Range series.

    The X-range series displays ranges on the X axis, typically time intervals with a
    start and end date.

    .. tabs::

      .. tab:: Standard X-Range

        .. figure:: _static/xrange-example.png
          :alt: X-Range Example Chart
          :align: center

      .. tab:: Inverted X-Range

        .. figure:: _static/xrange-example-inverted.png
          :alt: Inverted X-Range Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[XRangeData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`XRangeData` instances,
        it accepts as input an iterable of :class:`XRangeData` instances or
        :class:`dict <python:dict>` instances that can be coerced to :class:`XRangeData`.

        :rtype: :class:`list <python:list>` of :class:`XRangeData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = XRangeData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'group_z_padding': as_dict.pop('groupZPadding', None),
            'partial_fill': as_dict.pop('partialFill', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)
