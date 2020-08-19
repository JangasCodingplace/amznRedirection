def redirect_page(request, key):
    try:
        fallback_key = FallbackKey.objects.get(key=key)
    except FallbackKey.DoesNotExist:
        raise Http404("Page not Found.")

    link_obj = fallback_key.link

    client = insert_client(request, link_obj)

    response = HttpResponse("", status=302)
    if 'Android' in client.os.family:
        return render(
                request, 'Redirection/android.html', {'link_obj': link_obj}
            )
    elif 'iOS' in client.os.family:
        if 'iPhone' in client.device.family:
            return render(
                request, 'Redirection/iPhone.html', {'link_obj': link_obj}
            )
        else:
            return render(
                request, 'Redirection/iPad.html', {'link_obj': link_obj}
            )
    else:
        response['Location'] = link_obj.desktop_link
    return response



def fallback(request, key):
    try:
        fallback_key = FallbackKey.objects.get(key=key)
    except FallbackKey.DoesNotExist:
        raise Http404("Page not Found.")

    link_obj = fallback_key.link

    response = HttpResponse("", status=302)
    response['Location'] = link_obj.desktop_link
    return response



def redirection2(request, key):
    try:
        fallback_key = FallbackKey.objects.get(key=key)
    except FallbackKey.DoesNotExist:
        raise Http404("No such affiliate.")

    link_obj = fallback_key.link

    return render(
        request, 'Redirection/fiverRedirect.html', {'link_obj': link_obj}
    )
