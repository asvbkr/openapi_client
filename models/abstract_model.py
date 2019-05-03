# -*- coding: UTF-8 -*-


class AbstractModel(object):
    def __init__(self):
        self._extend_attr()

    openapi_types = {}

    attribute_map = {}

    def _extend_attr(self):
        """
        use
        self.openapi_types.update({...})
        self.attribute_map.update({...})
        """
        raise NotImplementedError('Method AbstractModel._extend_attr is abstract.')
