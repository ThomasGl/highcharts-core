from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ScreenReaderSection(HighchartsMeta):
    """Accessibility options for the screen reader information sections added before
    and after the chart."""

    def __init__(self, **kwargs):
        self._after_chart_format = constants.DEFAULT_AFTER_CHART_FORMAT
        self._after_chart_formatter = None
        self._axis_range_date_format = constants.DEFAULT_AXIS_RANGE_DATE_FORMAT
        self._before_chart_format = constants.DEFAULT_BEFORE_CHART_FORMAT
        self._before_chart_formatter = None
        self._on_play_as_sound_click = None
        self._on_view_data_table_click = None

        self.after_chart_format = kwargs.pop('after_chart_format',
                                             constants.DEFAULT_AFTER_CHART_FORMAT)
        self.after_chart_formatter = kwargs.pop('after_chart_formatter', None)
        self.axis_range_date_format = kwargs.pop('axis_range_date_format',
                                                 constants.DEFAULT_AXIS_RANGE_DATE_FORMAT)
        self.before_chart_format = kwargs.pop('before_chart_format',
                                              constants.DEFAULT_BEFORE_CHART_FORMAT)
        self.before_chart_formatter = kwargs.pop('before_chart_formatter', None)
        self.on_play_as_sound_click = kwargs.pop('on_play_as_sound_click', None)
        self.on_view_data_table_click = kwargs.pop('on_view_data_table_click', None)

    @property
    def after_chart_format(self) -> Optional[str]:
        f"""Format for the screen reader information region after the chart. Defaults to
        ``'{constants.DEFAULT_AFTER_CHART_FORMAT}'``.

        Supported HTML tags are:
          * ``<h1-6>``
          * ``<p>``
          * ``<div>``
          * ``<a>``
          * ``<ul>``
          * ``<ol>``
          * ``<li>``
          * ``<button>``

        Attributes are not supported, except for ``id`` on ``<div>``, ``<a>``, and
        ``<button>``.

        ``id`` is required on ``<a>`` and ``<button>`` in the format
        ``<tag id="abcd">``. Numbers, lower- and uppercase letters, ``"-"`` and ``"#"``
        are valid characters in IDs.

        The ``headingTagName`` is an auto-detected heading (``h1-h6``) that corresponds to
        the heading level below the previous heading in the DOM.

        .. tip::

          Set to empty string to remove the region altogether.

        :returns: Content to render in the screen reader information region after the
          chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_chart_format

    @after_chart_format.setter
    def after_chart_format(self, value):
        if value is None:
            self._after_chart_format = None
        elif not value:
            self._after_chart_format = ''
        else:
            self._after_chart_format = validators.string(value, allow_empty = False)

    @property
    def after_chart_formatter(self) -> Optional[str]:
        """A JavaScript formatter function to create the HTML contents of the hidden
        screen reader information region after the chart.

        The formatter function should receive one argument, ``chart``, referring to the
        chart object. It should return a string with the HTML content of the region.

        If :obj:`None <python:None>`, will returns an automatic description of the chart
        based on :meth:`ScreenReaderSection.after_chart_format`.

        :returns: JavaScript formatter function for the screen reader information region
          after the chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_chart_formatter

    @after_chart_formatter.setter
    def after_chart_formatter(self, value):
        self._after_chart_formatter = validators.string(value, allow_empty = True)

    @property
    def axis_range_date_format(self) -> Optional[str]:
        f"""Date format to use to describe range of datetime axes. Defaults to
        ``{constants.DEFAULT_AXIS_RANGE_DATE_FORMAT}``.

        .. seealso::

          * Detailed documentation on supported format replacement codes:
            https://api.highcharts.com/class-reference/Highcharts.Time#dateFormat

        :returns: Date format to use to describe range of datetime axes.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._axis_range_date_format

    @axis_range_date_format.setter
    def axis_range_date_format(self, value):
        self._axis_range_date_format = validators.string(value, allow_empty = True)

    @property
    def before_chart_format(self) -> Optional[str]:
        f"""Format for the screen reader information region before the chart. Defaults to
        ``'{constants.DEFAULT_BEFORE_CHART_FORMAT}'``.

        Supported HTML tags are:
          * ``<h1-6>``
          * ``<p>``
          * ``<div>``
          * ``<a>``
          * ``<ul>``
          * ``<ol>``
          * ``<li>``
          * ``<button>``

        Attributes are not supported, except for ``id`` on ``<div>``, ``<a>``, and
        ``<button>``.

        ``id`` is required on ``<a>`` and ``<button>`` in the format
        ``<tag id="abcd">``. Numbers, lower- and uppercase letters, ``"-"`` and ``"#"``
        are valid characters in IDs.

        The ``headingTagName`` is an auto-detected heading (``h1-h6``) that corresponds to
        the heading level below the previous heading in the DOM.

        .. tip::

          Set to empty string to remove the region altogether.

        :returns: Content to render in the screen reader information region before the
          chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._before_chart_format

    @before_chart_format.setter
    def before_chart_format(self, value):
        if value is None:
            self._before_chart_format = None
        elif not value:
            self._before_chart_format = ''
        else:
            self._before_chart_format = validators.string(value, allow_empty = False)

    @property
    def before_chart_formatter(self) -> Optional[str]:
        """A JavaScript formatter function to create the HTML contents of the hidden
        screen reader information region before the chart.

        The formatter function should receive one argument, ``chart``, referring to the
        chart object. It should return a string with the HTML content of the region.

        If :obj:`None <python:None>`, will returns an automatic description of the chart
        based on :meth:`ScreenReaderSection.before_chart_format`.

        :returns: JavaScript formatter function for the screen reader information region
          before the chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._before_chart_formatter

    @before_chart_formatter.setter
    def before_chart_formatter(self, value):
        self._before_chart_formatter = validators.string(value, allow_empty = True)

    @property
    def on_play_as_sound_click(self) -> Optional[str]:
        """JavaScript function to run upon clicking the "Play as sound" button in the
        screen reader region.

        By default Highcharts will call the ``chart.sonify`` JavaScript function.

        :returns: JavaScript function to run upon clicking the "Play as sound" button in
          the screen reader region.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_play_as_sound_click

    @on_play_as_sound_click.setter
    def on_play_as_sound_click(self, value):
        self._on_play_as_sound_click = validators.string(value, allow_empty = True)

    @property
    def on_view_data_table_click(self) -> Optional[str]:
        """JavaScript function to run upon clicking the "View as Data Table" link in the
        screen reader region.

        By default Highcharts will insert and set focus to a data table representation of
        the chart.

        :returns: JavaScript function to run upon clicking the "View as Data Table" link
          in the screen reader region.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_view_data_table_click

    @on_view_data_table_click.setter
    def on_view_data_table_click(self, value):
        self._on_view_data_table_click = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'after_chart_format': as_dict.pop('afterChartFormat',
                                              constants.DEFAULT_AFTER_CHART_FORMAT),
            'after_chart_formatter': as_dict.pop('afterChartFormatter', None),
            'axis_range_date_format': as_dict.pop('axisRangeDateFormat',
                                                  constants.DEFAULT_AXIS_RANGE_DATE_FORMAT),
            'before_chart_format': as_dict.pop('beforeChartFormat',
                                               constants.DEFAULT_BEFORE_CHART_FORMAT),
            'before_chart_formatter': as_dict.pop('beforeChartFormatter', None),
            'on_play_as_sound_click': as_dict.pop('onPlayAsSoundClick', None),
            'on_view_data_table_click': as_dict.pop('onViewDataTableClick', None)
        }

        return cls(**kwargs)

    def to_json(self, encoding = 'utf-8'):
        untrimmed = {
            'afterChartFormat': self.after_chart_format,
            'afterChartFormatter': self.after_chart_formatter,
            'axisRangeDateFormat': self.axis_range_date_format,
            'beforeChartFormat': self.before_chart_format,
            'beforeChartFormatter': self.before_chart_formatter,
            'onPlayAsSoundClick': self.on_play_as_sound_click,
            'onViewDataTableClick': self.on_view_data_table_click
        }
        as_dict = self.trim_dict(untrimmed)

        return as_dict
