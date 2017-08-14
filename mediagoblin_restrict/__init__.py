import logging
import re

from mediagoblin.tools import pluginapi

_log = logging.getLogger(__name__)

def setup_plugin():
    _log.info("restrict plugin stated!")

def restrict_media_sidebar(context):
    print context
    return context



hooks = {
    'setup': setup_plugin,
    ("mediagoblin.user_pages.media_home", 
     "mediagoblin/media_displays/audio.html"): restrict_media_sidebar
}
