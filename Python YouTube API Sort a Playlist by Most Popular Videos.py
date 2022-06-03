from apiclient.discovery import build

api_key = "YOUR_API_KEY"

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'YOUR_ID_PLAYLIST'

videos = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="snippet, statistics",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        vid_views = "Views: " + item['statistics']['viewCount']
        vid_title = "Title: " + item['snippet']['title']
        vid_description = item['snippet']['description']
        like = "Like: " + item['statistics']['likeCount']
        yt_link = "https://youtu.be/" + item['id']
        Image_url = "URL Image: " + item['snippet']['thumbnails']['default']['url']
        
        videos.append(
            {
                'view':  vid_views,
                'title': vid_title,
                'url': yt_link,
                'likeCount': like,
                'description': vid_description,
                'imageURL':Image_url
            }
        )

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

videos.sort(key=lambda vid: vid['view'], reverse=True) #sap xep theo video pho bien nhat

for video in videos[:50]:
    print('*'*100)
    print(video['url'])
    print(video['title'])
    print(video['view'])
    print(video['likeCount'])
    print(video['description'])
    print(video['imageURL'])
   



   
