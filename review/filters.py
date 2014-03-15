import humanize
def show_stars(score):
    return ''.join(['<img data-src="/static/svg/smart/star.svg" class="iconic iconic-sm">' for _ in range(score)])

def naturaltime(datetime):
    return humanize.naturaltime(datetime)
