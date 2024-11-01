# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================

from ricxappframe_ID.xapp_frame import RMRXapp
from abc import ABC, abstractmethod


class _BaseHandler(ABC):
    """
    Represents base Abstract Handler class
    Here initialize variables which will be common to all xapp

    Parameters:
        rmr_xapp: Reference to original RMRxappframe object
        msgtype: Integer specifying messagetype
    """

    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        self._rmr_xapp = rmr_xapp
        self.logger = self._rmr_xapp.logger
        self.msgtype = msgtype
        self._rmr_xapp.register_callback(self.request_handler, msgtype)

    @abstractmethod
    def request_handler(self, rmr_xapp, summary, sbuf):
        pass
