from os import getenv # Give access to get environmental variables

from ricxappframe_oaict.xapp_frame import * # Get access to the RIC xApp framework

from handler import * # Imports the handlers
from manager import * # Imports the managers

from utils.constants import Constants


class Oaict_xApp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(
            self._default_handler,
            config_handler=self.config_handler,
            rmr_port = 4560,
            post_init = self._post_init,
            use_fake_sdl = bool(fake_sdl)
            )

    def _default_handler(self):
        print("Default handler")

    def config_handler(self, rmr_xapp, config):
        print("Handle config change")

    def _post_init(self, rmr_xapp):
        """
        Function that runs when xapp initialization is complete
        """
        rmr_xapp.logger.info("HWXapp.post_init :: post_init called")
        # self.sdl_alarm_mgr = SdlAlarmManager()
        sdl_mgr = SdlManager(rmr_xapp)
        # sdl_mgr.sdlGetGnbList()
        a1_mgr = A1PolicyManager(rmr_xapp)
        a1_mgr.startup()
        sub_mgr = SubscriptionManager(rmr_xapp)

    def createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        HealthCheckHandler(self._rmr_xapp, Constants.RIC_HEALTH_CHECK_REQ)
        A1PolicyHandler(self._rmr_xapp, Constants.A1_POLICY_REQ)
        SubscriptionHandler(self._rmr_xapp,Constants.SUBSCRIPTION_REQ)

    def start(self):
        self.createHandlers()
