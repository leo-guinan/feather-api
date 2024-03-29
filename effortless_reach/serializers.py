from rest_framework import serializers

from effortless_reach.models import PodcastEpisode, Podcast, Transcript, Summary, KeyPoints, PodcastNotes, \
    PodcastEpisodeNotes


class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = [
            'id',
            'text',
        ]

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = [
            'id',
            'text',
        ]

class KeyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPoints
        fields = [
            'text',
        ]

class PodcastNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastNotes
        fields = [
            'text',
        ]
class PodcastEpisodeNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastEpisodeNotes
        fields = [
            'text',
        ]
class PodcastEpisodeSerializer(serializers.ModelSerializer):
    transcript_status = serializers.SerializerMethodField('get_transcript_status')
    transcript = TranscriptSerializer(many=False, read_only=True)
    summary = SummarySerializer(many=False, read_only=True)
    key_points = KeyPointSerializer(many=False, read_only=True)
    notes = PodcastEpisodeNotesSerializer(many=True, read_only=True)
    def get_transcript_status(self, obj):
        try:
            if not obj.transcript.exists():
                return 'Not Started'
            elif obj.transcript.text is None:
                return 'In Progress'
            else:
                return 'Complete'
        except:
            return 'Not Started'

    class Meta:
        model = PodcastEpisode
        fields = [
            'id',
            'title',
            'link',
            'description',
            'published_at',
            'transcript',
            'transcript_status',
            'image',
            'summary',
            'key_points',
            'notes',
        ]

class PodcastSerializer(serializers.ModelSerializer):
    notes = PodcastNotesSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = [
            'id',
            'title',
            'link',
            'description',
            'image',
            'notes'
        ]

class PodcastWithEpisodeSerializer(serializers.ModelSerializer):
    episodes = PodcastEpisodeSerializer(many=True)


    class Meta:
        model = Podcast
        fields = [
            'id',
            'title',
            'link',
            'description',
            'episodes',
            'image',
        ]



# const podcasts = [
#   {
#     id: 1,
#     title: "The Daily",
#     link: "https://www.nytimes.com/column/the-daily",
#     description: "The Daily is a news podcast hosted by Michael Barbaro. It is produced by The New York Times and WNYC Studios.",
#     image: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png",
#     processed: false,
#     type: "guest_interview",
#     guests: [
#       {
#         name: "Michael Barbaro",
#         link: "https://www.nytimes.com/column/the-daily",
#         imageUrl: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png"
#       }
#     ],
#     publishedDate: "2021-01-01T00:00:00.000Z",
#     tags: [
#       {
#         name: "Transcript",
#         color: "bg-rose-500",
#         href: "https://www.nytimes.com/column/the-daily"
#
#       },
#       {
#         name: "Key Points",
#         color: "bg-indigo-500",
#         href: "https://www.nytimes.com/column/the-daily"
#       }
#     ]
#   },
#   {
#     id: 2,
#     title: "The Daily",
#     link: "https://www.nytimes.com/column/the-daily",
#     description: "The Daily is a news podcast hosted by Michael Barbaro. It is produced by The New York Times and WNYC Studios.",
#     image: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png",
#     processed: false,
#     type: "solo",
#     guests: [],
#     publishedDate: "2021-01-01T00:00:00.000Z",
#     tags: [
#       {
#         name: "Transcript",
#         color: "bg-rose-500",
#         href: "https://www.nytimes.com/column/the-daily"
#
#       },
#       {
#         name: "Key Points",
#         color: "bg-indigo-500",
#         href: "https://www.nytimes.com/column/the-daily"
#       }
#     ]
#   },
#   {
#     id: 3,
#     title: "The Daily",
#     link: "https://www.nytimes.com/column/the-daily",
#     description: "The Daily is a news podcast hosted by Michael Barbaro. It is produced by The New York Times and WNYC Studios.",
#     image: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png",
#     processed: false,
#     type: "solo",
#     guests: [],
#     publishedDate: "2021-01-01T00:00:00.000Z",
#     tags: [
#       {
#         name: "Transcript",
#         color: "bg-rose-500",
#         href: "https://www.nytimes.com/column/the-daily"
#
#       },
#       {
#         name: "Key Points",
#         color: "bg-indigo-500",
#         href: "https://www.nytimes.com/column/the-daily"
#       }
#     ]
#   },
#   {
#     id: 4,
#     title: "The Daily",
#     link: "https://www.nytimes.com/column/the-daily",
#     description: "The Daily is a news podcast hosted by Michael Barbaro. It is produced by The New York Times and WNYC Studios.",
#     image: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png",
#     processed: false,
#     type: "solo",
#     guests: [],
#     publishedDate: "2021-01-01T00:00:00.000Z",
#     tags: [
#       {
#         name: "Transcript",
#         color: "bg-rose-500",
#         href: "https://www.nytimes.com/column/the-daily"
#
#       },
#       {
#         name: "Key Points",
#         color: "bg-indigo-500",
#         href: "https://www.nytimes.com/column/the-daily"
#       }
#     ]
#   },
#   {
#     id: 5,
#     title: "The Daily",
#     link: "https://www.nytimes.com/column/the-daily",
#     description: "The Daily is a news podcast hosted by Michael Barbaro. It is produced by The New York Times and WNYC Studios.",
#     image: "https://static01.nyt.com/images/misc/NYT_podcasts_logo.png",
#     processed: false,
#     type: "solo",
#     guests: [],
#     publishedDate: "2021-01-01T00:00:00.000Z",
#     tags: [
#       {
#         name: "Transcript",
#         color: "bg-rose-500",
#         href: "https://www.nytimes.com/column/the-daily"
#
#       },
#       {
#         name: "Key Points",
#         color: "bg-indigo-500",
#         href: "https://www.nytimes.com/column/the-daily"
#       }
#     ]
#   }
# ]