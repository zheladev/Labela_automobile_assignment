def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    #homepage
    config.add_route('home', '/')

    #users
    config.add_route('user.list', '/user', request_method="GET")
    config.add_route('user.find_by_email', '/user/email', request_method="GET")
    #parts
    config.add_route('part.list', '/part', request_method="GET")
    config.add_route('part.find_by_vendor_id', '/part/detail', request_method="GET")
    config.add_route('part.add_part', '/part/add', request_method="GET") #should be POST, just for testing purposes
    config.add_route('part.delete_part', '/part/delete', request_method="GET")
    #cart
    config.add_route('cart.add_to_cart', '/cart/add', request_method="GET")
    config.add_route('cart.remove_from_cart', 'cart/delete', request_method="GET")
    config.add_route('cart.order_cart', 'cart/order')
    config.add_route('cart.empty_cart', 'cart/empty')
