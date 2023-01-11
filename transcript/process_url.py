import sys
from urllib.parse import urlparse
from urllib.parse import parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import re


def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
 
    return ''

def concatenate_list_data(list):
	result= ''
	for element in list:
		f=re.sub('[^A-Za-z0-9]+', ' ', str(element))
		result += f+' '
	return result


def transcriptYoutube(url):
    dataset=YouTubeTranscriptApi.get_transcript(url)
    text_list=[d['text'] for d in dataset]
    return concatenate_list_data(text_list)


