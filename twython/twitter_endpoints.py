"""
    A huge map of every Twitter API endpoint to a function definition in Twython.

    Parameters that need to be embedded in the URL are treated with mustaches, e.g:

    {{version}}, etc

    When creating new endpoint definitions, keep in mind that the name of the mustache
    will be replaced with the keyword that gets passed in to the function at call time.

    i.e, in this case, if I pass version = 47 to any function, {{version}} will be replaced
    with 47, instead of defaulting to 1 (said defaulting takes place at conversion time).
"""

# Base Twitter API url, no need to repeat this junk...
base_url = 'http://api.twitter.com/{{version}}'

api_table = {
    # Timeline methods
    'getMentionsTimeline' : {
        'url' : '/statuses/mentions_timeline.json',
        'method' : 'GET',
    },
    'getUserTimeline': {
        'url': '/statuses/user_timeline.json',
        'method': 'GET',
    },
    'getHomeTimeline': {
        'url': '/statuses/home_timeline.json',
        'method': 'GET',
    },
    'getRetweetsOfMe' : {
        'url' : '/statuses/retweets_of_me.json',
        'method' : 'GET',
    },

    # Tweet methods
    'getRetweets': {
        'url': '/statuses/retweets/{{id}}.json',
        'method': 'GET',
    },
    'showStatus': {
        'url': '/statuses/show.json',
        'method': 'GET',
    },
    'destroyStatus': {
        'url': '/statuses/destroy/{{id}}.json',
        'method': 'POST',
    },
    'updateStatus': {
        'url': '/statuses/update.json',
        'method': 'POST',
    },
    'reTweet': {
        'url': '/statuses/retweet/{{id}}.json',
        'method': 'POST',
    },
    # update_with_media
    'getOembedTweet': {
        'url': '/statuses/oembed.json',
        'method': 'GET',
    },

    # Search methods
    # search tweets

    # Direct Messages - getting, sending, effing, etc.
    'getDirectMessages': {
        'url': '/direct_messages.json',
        'method': 'GET',
    },
    'getSentMessages': {
        'url': '/direct_messages/sent.json',
        'method': 'GET',
    },
    'showDirectMessages' : {
        'url' : '/direct_messages/show.json',
        'method' : 'GET',
    },
    'sendDirectMessage': {
        'url': '/direct_messages/new.json',
        'method': 'POST',
    },
    'destroyDirectMessage': {
        'url': '/direct_messages/destroy/{{id}}.json',
        'method': 'POST',
    },

    # Friends & Followers
    'getFriendsIDs': {
        'url': '/friends/ids.json',
        'method': 'GET',
    },
    'getFollowersIDs': {
        'url': '/followers/ids.json',
        'method': 'GET',
    },
    'lookupFriendships' : {
        'url' : '/friendships/lookup.json',
        'method' : 'GET',
    },
    'getIncomingFriendshipIDs': {
        'url': '/friendships/incoming.json',
        'method': 'GET',
    },
    'getOutgoingFriendshipIDs': {
        'url': '/friendships/outgoing.json',
        'method': 'GET',
    },
    'createFriendship': {
        'url': '/friendships/create.json',
        'method': 'POST',
    },
    'destroyFriendship': {
        'url': '/friendships/destroy.json',
        'method': 'POST',
    },
    'updateFriendship' : {
        'url' : '/friendships/update.json',
        'method' : 'POST',
    },
    'showFriendship': {
        'url': '/friendships/show.json',
        'method': 'GET',
    },
    'getFriendsList': {
        'url': '/friends/list.json',
        'method': 'GET',
    },
    'getFollowersList' : {
        'url': '/followers/list.json',
        'method': 'GET',
    },

    # Users
    'getAccountSettings' : {
        'url' : '/account/settings.json',
        'method' : 'GET',
    },
    'verifyCredentials': {
        'url': '/account/verify_credentials.json',
        'method': 'GET',
    },
    'updateAccountSettings' : {
        'url' : '/account/settings.json',
        'method' : 'POST',
    },
    'updateDeliveryDevice' : {
        'url' : '/account/update_delivery_device.json',
        'method' : 'POST',
    },
    'updateProfile': {
        'url': '/account/update_profile.json',
        'method': 'POST',
    },
    # updateProfileBackgroundImage
    'updateProfileColors': {
        'url': '/account/update_profile_colors.json',
        'method': 'POST',
    },
    # updateProfileImage
    # getBlocksIds
    'getBlockedIDs': {
        'url': '/blocks/blocking/ids.json',
        'method': 'GET',
    },
    'createBlock': {
        'url': '/blocks/create/{{id}}.json',
        'method': 'POST',
    },
    'destroyBlock': {
        'url': '/blocks/destroy/{{id}}.json',
        'method': 'POST',
    },
    'lookupUser': {
        'url': '/users/lookup.json',
        'method': 'GET',
    },
    'showUser': {
        'url': '/users/show.json',
        'method': 'GET',
    },
    'searchUsers': {
        'url': '/users/search.json',
        'method': 'GET',
    },
    'getUserContributees' : {
        'url' : '/users/contributees.json',
        'method' : 'POST',
    },
    'getUserContributors' : {
        'url' : '/users/contributors.json',
        'method' : 'POST',
    },
    'removeProfileBanner' : {
        'url': '/account/remove_profile_banner.json',
        'method': 'POST',
    },
    'updateProfileBanner' : {
        'url' : '/account/update_profile_banner.json',
        'method' : 'POST',
    },
    'getProfileBanner' : {
        'url' : '/users/profile_banner.json',
        'method' : 'GET',
    }, 

    # Suggested Users
    'getSuggestionsByCategory' : {
        'url' : '/users/suggestions/{{slug}}.json',
        'method' : 'GET',
    },
    'getSuggestions' : {
        'url' : '/users/suggestions',
        'method' : 'GET',
    },
    'getSuggestionStatusesByCategory' : {
        'url' : '/users/suggestions/{{slug}}/members.json',
        'method' : 'GET',
    },

    # Favorites
    'getFavoritesList' : {
        'url' : '/favorites/list.json',
        'method' : 'GET',
    },
    'destroyFavorite' : {
        'url' : '/favorites/destroy.json',
        'method' : 'GET',
    },
    'createFavorite' : {
        'url' : '/favorites/create.json',
        'method' : 'GET',
    },

    # List API methods/endpoints. Fairly exhaustive and annoying in general. ;P
    'showLists': {
        'url': '/lists/list.json',
        'method': 'GET',
    },
    'getListStatuses': {
        'url': '/lists/statuses.json',
        'method': 'GET'
    },
    'deleteListMember': {
        'url': '/lists/members/destroy.json',
        'method': 'POST',
    },
    'getListMemberships': {
        'url': '/lists/memberships.json',
        'method': 'GET',
    },
    'getListSubscribers': {
        'url': '/lists/subscribers.json',
        'method': 'GET',
    },
    'subscribeToList': {
        'url': '/lists/subscribers/create.json',
        'method': 'POST',
    },
    'isListSubscriber': {
        'url': '/lists/subscribers/show.json',
        'method': 'GET',
    },
    'unsubscribeFromList': {
        'url': '/lists/subscribers/destroy.json',
        'method': 'POST',
    },
    'addListMembers' : {
        'url' : '/lists/members/create_all.json',
        'method' : 'POST',
    },
    'isListMember': {
        'url': '/lists/members/show.json',
        'method': 'GET',
    },
    'getListMembers': {
        'url': '/lists/members.json',
        'method': 'GET',
    },
    'addListMember': {
        'url': '/lists/members/create.json',
        'method': 'POST',
    },
    'deleteList': {
        'url': '/lists/destroy.json',
        'method': 'POST',
    },
    'updateList': {
        'url': '/lists/update.json',
        'method': 'POST',
    },
    'createList': {
        'url': '/lists/create.json',
        'method': 'POST',
    },
    'getSpecificList': {
        'url': '/lists/show.json',
        'method': 'GET',
    },
    'getListSubscriptions': {
        'url': '/lists/subscriptions.json',
        'method': 'GET',
    },
    'destroyListMembers' : {
        'url' : '/lists/members/destroy_all.json',
        'method' : 'GET',
    },


    'getListTimeline': {
        'url': '/{{username}}/lists/{{list_id}}/statuses.json',
        'method': 'GET',
    },

    # Saved Searches
    'getSavedSearches': {
        'url': '/saved_searches/list.json',
        'method': 'GET',
    },
    'showSavedSearch': {
        'url': '/saved_searches/show/{{id}}.json',
        'method': 'GET',
    },
    'createSavedSearch': {
        'url': '/saved_searches/create.json',
        'method': 'GET',
    },
    'destroySavedSearch': {
        'url': '/saved_searches/destroy/{{id}}.json',
        'method': 'GET',
    },

    # Places & Geo
    #getGeoPlace
    #reverseGeocode
    #geoSearch
    #getSimilarPlaces
    #createGeoPlace

    # Trends
    #getTrendsForPlace
    #getAvailableTrendLocations
    #getClosestTrendLocations

    # Spam Reporting
    'reportSpam': {
        'url': '/report_spam.json',
        'method': 'POST',
    },


    # Help
    #getConfiguration
    #getLanguages
    #getPrivacy
    #getTOS
    'getRateLimitStatus': {
        'url': '/account/rate_limit_status.json',
        'method': 'GET',
    },
}

# from https://dev.twitter.com/docs/error-codes-responses
twitter_http_status_codes = {
    200: ('OK', 'Success!'),
    304: ('Not Modified', 'There was no new data to return.'),
    400: ('Bad Request', 'The request was invalid. An accompanying error message will explain why. This is the status code will be returned during rate limiting.'),
    401: ('Unauthorized', 'Authentication credentials were missing or incorrect.'),
    403: ('Forbidden', 'The request is understood, but it has been refused. An accompanying error message will explain why. This code is used when requests are being denied due to update limits.'),
    404: ('Not Found', 'The URI requested is invalid or the resource requested, such as a user, does not exists.'),
    406: ('Not Acceptable', 'Returned by the Search API when an invalid format is specified in the request.'),
    420: ('Enhance Your Calm', 'Returned by the Search and Trends API when you are being rate limited.'),
    500: ('Internal Server Error', 'Something is broken. Please post to the group so the Twitter team can investigate.'),
    502: ('Bad Gateway', 'Twitter is down or being upgraded.'),
    503: ('Service Unavailable', 'The Twitter servers are up, but overloaded with requests. Try again later.'),
}
