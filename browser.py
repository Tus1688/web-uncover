from selenium import webdriver

from ui import print_info

def custom_profile(proxy:str = None, user_agent:str = None) -> webdriver.FirefoxProfile:
    profile = webdriver.FirefoxProfile()
    
    profile.set_preference('dom.webdriver.enabled', False)
    profile.set_preference('useAutomationExtension', False)

    # startup page
    profile.set_preference('browser.startup.page', 0)
    profile.set_preference('browser.startup.homepage', 'about:blank')
    profile.set_preference('browser.newtab.preload', False)
    
    # newtab page
    profile.set_preference('browser.newtabpage.activity-stream.feeds.telemetry', False)
    profile.set_preference('browser.newtabpage.activity-stream.telemetry', False)
    profile.set_preference('browser.newtabpage.activity-stream.feeds.snippets', False)
    profile.set_preference('browser.newtabpage.activity-stream.feeds.section.topstories', False)
    profile.set_preference('browser.newtabpage.activity-stream.section.highlights.includePocket', False)
    profile.set_preference('browser.newtabpage.activity-stream.showSponsored', False)
    profile.set_preference('browser.newtabpage.activity-stream.feeds.discoverystreamfeed', False)
    profile.set_preference('browser.newtabpage.activity-stream.showSponsoredTopSites', False)
    profile.set_preference('browser.newtabpage.activity-stream.default.sites', "")

    # disable geolocation
    profile.set_preference('geo.provider.ms-windows-location', False)
    profile.set_preference('geo.provider.use_corelocation', False)
    profile.set_preference('geo.provider.use_gpsd', False)
    profile.set_preference('geo.provider.use_geoclue', False)

    # disable region updates
    profile.set_preference('browser.region.network.url', '')
    profile.set_preference('browser.region.update.enabled', False)
    profile.set_preference('intl.accept_languages', 'en-US, en')
    profile.set_preference('javascript.use_us_english_locale', True)

    # addons 
    profile.set_preference('extensions.getAddons.showPane', False)
    profile.set_preference('extensions.htmlaboutaddons.recommendations.enabled', False)
    profile.set_preference('browser.discovery.enabled', False)

    # telemetry
    profile.set_preference('datareporting.policy.dataSubmissionEnabled', False)
    profile.set_preference('datareporting.healthreport.uploadEnabled', False)
    profile.set_preference('toolkit.telemetry.unified', False)
    profile.set_preference('toolkit.telemetry.enabled', False)
    profile.set_preference('toolkit.telemetry.server', 'data:,')
    profile.set_preference('toolkit.telemetry.archive.enabled', False)
    profile.set_preference('toolkit.telemetry.newProfilePing.enabled', False)
    profile.set_preference('toolkit.telemetry.shutdownPingSender.enabled', False)
    profile.set_preference('toolkit.telemetry.updatePing.enabled', False)
    profile.set_preference('toolkit.telemetry.bhrPing.enabled', False)
    profile.set_preference('toolkit.telemetry.firstShutdownPing.enabled', False)
    profile.set_preference('toolkit.telemetry.coverage.opt-out', True)
    profile.set_preference('toolkit.coverage.opt-out', True)
    profile.set_preference('toolkit.coverage.endpoint.base', '')
    profile.set_preference('browser.ping-centre.telemetry', False)
    profile.set_preference('app.shield.optoutstudies.enabled', False)
    profile.set_preference('app.normandy.enabled', False)
    profile.set_preference('app.normandy.api_url', '')
    profile.set_preference('breakpad.reportURL', '')
    profile.set_preference('browser.tabs.crashReporting.sendReport', False)
    profile.set_preference('browser.crashReports.unsubmittedCheck.autoSubmit2', False)
    profile.set_preference('captivedetect.canonicalURL', '')
    profile.set_preference('network.captive-portal-service.enabled', False)
    profile.set_preference('network.connectivity-service.enabled', False)

    # block implicit outbound
    profile.set_preference('network.prefetch-next', False)
    profile.set_preference('network.dns.disablePrefetch', True)
    profile.set_preference('network.predictor.enabled', False)
    profile.set_preference('network.predictor.enable-prefetch', False)
    profile.set_preference('network.http.speculative-parallel-limit', 0)
    profile.set_preference('browser.places.speculativeConnect.enabled', False)
    profile.set_preference('network.dns.disableIPv6', True)

    profile.set_preference('accessibility.force_disabled', 1)
    profile.set_preference('beacon.enabled', False)

    # disable cache
    profile.set_preference('browser.cache.disk.enable', False)
    profile.set_preference('browser.cache.memory.enable', False)
    profile.set_preference('browser.cache.offline.enable', False)
    profile.set_preference('network.http.use-cache', False)
    profile.set_preference('browser.shell.shortcutFavicons', False)

    # resist fingerprinting 
    profile.set_preference('privacy.resistFingerprinting', True)
    profile.set_preference('privacy.resistFingerprinting.block_mozAddonManager', True)
    profile.set_preference('privacy.resistFingerprinting.letterboxing', True)
    profile.set_preference('browser.startup.page', False)
    profile.set_preference('browser.display.use_system_colors', False)
    profile.set_preference('widget.non-native-theme.enabled', True)
    profile.set_preference('extensions.webcompat-reporter.enabled', False)

    profile.set_preference('browser.toolbars.bookmarks.visibility', "never")
    profile.set_preference('browser.newtabpage.activity-stream.feeds.favicon', False)
    profile.set_preference('browser.tabs.loadBookmarksInBackground', False)
    profile.set_preference('browser.newtabpage.activity-stream.section.highlights.includeBookmarks', False)

    # check if proxy is set
    if proxy:
        proxy_host = proxy.split(':')[0]
        proxy_port = proxy.split(':')[1]

        print_info("Setting proxy to {}:{}".format(proxy_host, proxy_port))

        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http",proxy_host)
        profile.set_preference("network.proxy.http_port",int(proxy_port))
        profile.set_preference("network.proxy.https",proxy_host)
        profile.set_preference("network.proxy.https_port",int(proxy_port))
        profile.set_preference("network.proxy.ssl",proxy_host)
        profile.set_preference("network.proxy.ssl_port",int(proxy_port))  
        profile.set_preference("network.proxy.ftp",proxy_host)
        profile.set_preference("network.proxy.ftp_port",int(proxy_port))   
        profile.set_preference("network.proxy.socks",proxy_host)
        profile.set_preference("network.proxy.socks_port",int(proxy_port))   
    
    if user_agent:
        profile.set_preference('general.useragent.override', user_agent)

    profile.update_preferences()
    return profile