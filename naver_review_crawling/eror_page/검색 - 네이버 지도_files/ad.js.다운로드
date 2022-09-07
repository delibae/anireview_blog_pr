if (!adScriptInitialized) {
  var adScriptInitialized = true;

  var visitAllUrlsAndThenCall = function (element) {
    var href = element.href;
    var called = false;
    var expected = arguments.length - 1;

    var completed = 0;
    for (var i = 1; i < arguments.length; i++) {
      var url = arguments[i];

      var image = new Image();
      image.onerror = function (event) {
        completed += 1;
        if (completed == expected && !called) {
          called = true;
          document.location = href;
        }
      };
      image.src = url;
    }

    // Fallback.
    setTimeout(function () {
      if (!called) {
        called = true;
        document.location = href;
      }
    }, 1000);
  }

  var visitAllUrls = function (element) {
    for (var i = 1; i < arguments.length; i++) {
      var url = arguments[i];
      var image = new Image();
      image.src = url;
    }
  }

  var getBizCatcherUrl = function getBizCatcherUrl(element) {
    var BIZ_CATCHER_HTTP_SERVER = "http://api-biz-catcher.naver.com";
    var BIZ_CATCHER_HTTPS_SERVER = "https://api-biz-catcher.naver.com";
    var BIZ_CATCHER_URI_PREFIX = "/api/v1/callInfos/add?";

    var BIZ_CATCHER_SERVER = window.location.href.indexOf("http://") === 0 ? BIZ_CATCHER_HTTP_SERVER : BIZ_CATCHER_HTTPS_SERVER;
    var BIZ_CATCHER_URL_PREFIX = BIZ_CATCHER_SERVER + BIZ_CATCHER_URI_PREFIX;

    var parameters = encodeURI(element.getAttribute("data-for-biz-catcher"));
    var url = BIZ_CATCHER_URL_PREFIX + parameters;
    try {
      if (typeof (naverAppBizCatcher) !== "undefined") {
        var hashedDeviceCallNumber = naverAppBizCatcher.getHashedDeviceCallNumber();
        if (hashedDeviceCallNumber !== null) {
          url += "&hashedDeviceNumber=" + hashedDeviceCallNumber;
        }
      }
    }
    catch (ignored) {
    }
    return url;
  }

  var getAdcrUrl = function getAdcrUrl(adcrUrl, p) {
    return adcrUrl + "&p=" + p;
  }

  var sendToBizCatcher = function sendToBizCatcher(element, shouldCall) {
    var bizCatcherUrl = getBizCatcherUrl(element);
    if (shouldCall === false) {
      visitAllUrls(element, bizCatcherUrl);
    } else {
      visitAllUrlsAndThenCall(element, bizCatcherUrl);
    }
  }
}
