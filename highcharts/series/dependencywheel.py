from typing import Optional, List

from highcharts.decorators import class_sensitive
from highcharts.series.base import SeriesBase
from highcharts.series.data.connections import WeightedConnectionData
from highcharts.plot_options.dependencywheel import DependencyWheelOptions
from highcharts.utility_functions import mro_init, mro_to_dict
from highcharts.utility_classes.nodes import DependencyWheelNodeOptions


class DependencyWheelSeries(SeriesBase, DependencyWheelOptions):
    """Options to configure a Dependency Wheel series.

    A dependency wheel chart is a type of flow diagram, where all nodes are laid out
    in a circle, and the flow between the are drawn as link bands.

    .. figure:: _static/dependencywheel-example.png
      :alt: Dependency Wheel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._nodes = None

        self.nodes = kwargs.pop('nodes', None)

        self.__mro_init__(kwargs)

    @property
    def data(self) -> Optional[List[WeightedConnectionData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`WeightedConnectionData`
        instances, it accepts as input:

        .. tabs::

          .. tab:: Object Collection

            A one-dimensional collection of :class:`WeightedConnectionData` objects or
            :class:`dict <python:dict>` that are coercable to
            :class:`WeightedConnectionData` instances.

        :rtype: :class:`list <python:list>` of :class:`WeightedConnectionData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = WeightedConnectionData.from_setter(value)

    @property
    def nodes(self) -> Optional[List[DependencyWheelNodeOptions]]:
        """Collection of nodes for a Dependency Wheel that are associated with a
        specific :class:`DependencyWheelSeries` by the :meth:`DependencyWheelSeries.id`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`DependencyWheelNodeOptions` or
          :obj:`None <python:None>`
        """
        return self._nodes

    @nodes.setter
    @class_sensitive(DependencyWheelNodeOptions, force_iterable = True)
    def nodes(self, value):
        self._nodes = value

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
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'curve_factor': as_dict.pop('curveFactor', None),
            'levels': as_dict.pop('levels', None),
            'link_opacity': as_dict.pop('linkOpacity', None),
            'min_link_width': as_dict.pop('minLinkWidth', None),
            'node_padding': as_dict.pop('nodePadding', None),
            'node_width': as_dict.pop('nodeWidth', None),
            'start_angle': as_dict.pop('startAngle', None),

            'nodes': as_dict.pop('nodes', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = mro_to_dict(self)

        untrimmed['nodes'] = self.nodes

        return untrimmed