# -*- coding: utf-8 -*-

import re
import requests
from settings import *


def get_event_ids():
	""" Function for pulling event IDs from Facebook groups.
	"""

	# Regex for pulling event IDs from text.
	EVENT_REGEX = re.compile('facebook\.com/events/(\d+)/')

	result = []

	for group in FB_GROUPS:

		print("Requesting \"%s\" group." % group[0])

		# Prepare URL to request.
		api_url = ('https://graph.facebook.com/v2.10/{0}/feed?'
				   'fields=updated_time,message,link,story'
				   '&access_token={1}'.format(group[1], ACCESS_TOKEN))

		response = requests.get(api_url)

		try:
			for post in response.json()['data']:

				# Get event IDs from post message.
				try:
					from_message = re.findall(EVENT_REGEX, post['message'])
				except KeyError:
					from_message = []

				# Get event IDs from post link.
				try:
					from_link = re.findall(EVENT_REGEX, post['link'])
				except KeyError:
					from_link = []

				result.extend(from_message)
				result.extend(from_link)

		except:
			print("Couldn't fetch requested data.")
			print(response.content)

	# Remove duplicates.
	result = list(set(result))
	return result
