import humanize


def show_stars(score):
    return ''.join(['<i class="fa fa-star"></i>' for _ in range(score)])


def naturaltime(datetime):
    return humanize.naturaltime(datetime)
