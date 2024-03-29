def get_app_name(package):
    """
    Get the app name.

    Example:
    Input: __package__
    Output: users
    """

    return package.rsplit('.', 1)[-1]

def get_client_ip_address(request):
    """
    Get the client's ip address.

    This function is considered dangerous.
    Any client can send a X_FORWARDED_FOR header manually with any value
    So we first check if there's a valid for REMOTE_ADDR
    Otherwise we're behind a reverse proxy and the value for X_FORWARDED_FOR must be safe
    Which is forced by the proxy.
    """

    ip = request.META.get('REMOTE_ADDR')

    if len(ip) > 0:
        return ip

    return request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0].strip()