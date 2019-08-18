def trunc(content, num):
    t = content
    if len(t) > num:
        return t[:num] + '...'
    return t
