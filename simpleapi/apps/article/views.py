from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment

class ArticleView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ArticleSerializer

    @action(detail=True)
    def get_comments_by_article(self, request, pk=None):
        article = Article.objects.filter(id=pk).first()
        if article:
            comments = article.comment_set.filter(inclusion_level__lte = 3)
            return Response(CommentSerializer(comments, many=True).data)
        else:
            return Response({'error': "Doesn't exist article with this id"},
                                status=status.HTTP_400_BAD_REQUEST)

class CommentView(viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    
    @action(detail=False)
    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            val_data = serializer.validated_data
            if val_data.get('parent_comment'):
                par_comment = val_data['parent_comment']
                if par_comment.article != val_data.get('article'):
                    return Response({'errors': "The current article must be equal to parent comment's article"},
                            status=status.HTTP_400_BAD_REQUEST) 
                if par_comment:
                    val_data['inclusion_level'] = par_comment.inclusion_level + 1 
                    if par_comment.third_level_comment:
                        val_data['third_level_comment'] = par_comment.third_level_comment 
                    elif val_data['inclusion_level'] == 4:
                        val_data['third_level_comment'] = par_comment
                else:
                    return Response({'error': "Doesn't exist this parent comment"},
                            status=status.HTTP_400_BAD_REQUEST)
            else:
                val_data['inclusion_level'] = 0
            cmnt = Comment(**val_data)
            cmnt.save()
            return Response(CommentSerializer(cmnt).data)
        else:
            return Response({
                'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    @action(detail=True)
    def get_all_comments_wth_incl_level(self, request, pk=None):
        comment = Comment.objects.filter(id=pk).first()
        if not comment:
            return Response({'error': "Doesn't exist comment with this pk"},
                             status=status.HTTP_400_BAD_REQUEST)
        if comment.inclusion_level == 3:
            cmnts = Comment.objects.filter(third_level_comment=comment).all()
            return Response(CommentSerializer(cmnts, many=True).data)
        else:
            return Response({'error': 'Inclusion level must be equal 3 '},
                        status=status.HTTP_400_BAD_REQUEST)