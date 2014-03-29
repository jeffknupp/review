import humanize
def show_stars(score):
    return '<i class="fa fa-star"></i>' * score

def naturaltime(datetime):
    return humanize.naturaltime(datetime)
