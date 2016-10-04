from django import template
from datetime import datetime

register = template.Library()

# 自定义一个过滤器
@register.filter(is_safe=True)
def post_time(value):
    return timebefore(value)

# 判断时间离当前时间是多少间隔
def timebefore(d):

    chunks = (
        (60 * 60 * 24 * 365, '年'),
        (60 * 60 * 24 * 30, '月'),
        (60 * 60 * 24 * 7, '周'),
        (60 * 60 * 24, '天'),
        (60 * 60, '小时'),
        (60, '分钟'),
    )

    # 如果不是datetime类型转换后与datetime比较
    if not isinstance(d, datetime):
        d = datetime(d.year, d.month, d.day)
    now = datetime.now()
    delta = now - d
    # 忽略毫秒
    before = delta.days * 24 * 60 * 60 + delta.seconds
    # 刚刚过去的1分钟
    if before <= 60:
        return '一分钟内'
    for seconds, unit in chunks:
        count = before // seconds
        if count != 0:
            return str(count) + str(unit) + "前"

