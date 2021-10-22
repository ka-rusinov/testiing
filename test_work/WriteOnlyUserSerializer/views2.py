@api_view(['GET', 'POST'])
def post_get(request):

    if request.method == 'GET':
        snippets = WriteOnlyUserSerializer.objects.all()
        serializer = WriteOnlyUserSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)