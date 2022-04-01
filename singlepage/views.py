from django.shortcuts import render
from django.http import HttpResponse, Http404
# import json


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

def section(request, num):
    if 1 <= num <= 3:
        output_dict = commentTreeRenderer(getData(num))
        # return render(request, 'singlepage/root_comments.html', {'comments': json.dumps(output_dict, indent = 3)})
        return render(request, 'singlepage/root_comments.html', {'comments': output_dict})
    else:
        raise Http404("No such section")
# Create your views here.

# format the comment tree structure dictionary
def commentTreeRenderer(comment_list):
    from collections import defaultdict

    comments_by_parent = defaultdict(list)
    # loop over the list of comments, collecting comments by their common parent into a comments_by_parent dictionary
    for comment in comment_list:
        comments_by_parent[comment['ParentComment']].append(comment)

    # loop over the same list to append children_comments from the comments_by_parent dictionary
    for comment in comment_list:
        comment['children_comments'] = comments_by_parent[comment['CommentID']]

    # Assign the root level comments to root_comments
    root_comments = comments_by_parent[None]
    return root_comments

#faking the model
def getData(post_id):
    comments_result = [
        {'postid' : 1,'CommentID': 1, 'CommentDescription': 'comment 1', 'ParentComment': None},
        {'postid' : 1,'CommentID': 2, 'CommentDescription': 'comment 2', 'ParentComment': 1},
        {'postid' : 1,'CommentID': 3, 'CommentDescription': 'comment 3', 'ParentComment': 2},
        {'postid' : 1,'CommentID': 4, 'CommentDescription': 'comment 4', 'ParentComment': 3},
        {'postid' : 1,'CommentID': 5, 'CommentDescription': 'comment 5', 'ParentComment': 1},
        {'postid' : 1,'CommentID': 6, 'CommentDescription': 'comment 6', 'ParentComment': 3},
        {'postid' : 1,'CommentID': 7, 'CommentDescription': 'comment 7', 'ParentComment': 6},
        {'postid': 2, 'CommentID': 8, 'CommentDescription': 'comment 8', 'ParentComment': None},
        {'postid': 2, 'CommentID': 9, 'CommentDescription': 'comment 9', 'ParentComment': 8},
        {'postid': 2, 'CommentID': 10, 'CommentDescription': 'comment 10', 'ParentComment': None},
        {'postid': 3, 'CommentID': 11, 'CommentDescription': 'comment 11', 'ParentComment': None},
        {'postid': 3, 'CommentID': 12, 'CommentDescription': 'comment 12', 'ParentComment': 11},
        {'postid': 3, 'CommentID': 13, 'CommentDescription': 'comment 13', 'ParentComment': 12},
        {'postid': 3, 'CommentID': 14, 'CommentDescription': 'comment 14', 'ParentComment': 12},
    ]

    filtered_dict = [d for d in comments_result if d['postid'] == post_id ]
    return filtered_dict


