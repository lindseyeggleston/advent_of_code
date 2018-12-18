import os
import re
from collections import namedtuple, Counter
from datetime import datetime


def parse_logs(filename):
    def parse_log(log):
        Log = namedtuple('Log', ('datetime', 'time', 'msg', 'id'))
        log_pattern = r'\[(?P<datetime>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s(?P<msg>.*)'
        log_match = re.search(log_pattern, log)

        date_time = datetime.strptime(log_match.group('datetime'), '%Y-%m-%d %H:%M')
        msg = log_match.group('msg').strip()
        id_pattern = r'#(?P<id>\d{1,5})'
        id_match = re.search(id_pattern, log_match.group('msg'))
    
        if id_match:
            match_tup = Log(date_time, msg, id_match.group('id'))
        else:
            match_tup = Log(date_time, msg, '')
        return match_tup

    with open(filename) as f:
        logs = sorted(map(parse_log, f.readlines()), key = lambda x: x[0])

    return logs


def track_sleep_schedule(logs):
    guard_logs, on_duty = {}, None
    for i, log in enumerate(logs):
        if log.id:
            on_duty = log.id
            if log.id not in guard_logs:
                guard_logs[log.id] = {'minutes_asleep': 0, 'times': []}
        if log.msg == 'wakes up':
            guard_logs[on_duty]['minutes_asleep'] += int((log.time - logs[i-1].time).seconds / 60)
            guard_logs[on_duty]['times'].extend(range(logs[i-1].time.minute, log.time.minute))
    return guard_logs


def select_guard(guard_logs):
    max_hours_asleep, guard_id, times = 0, '', []
    for guard, sleep_log in guard_logs.items():
        if sleep_log['minutes_asleep'] > max_hours_asleep:
            max_hours_asleep = sleep_log['minutes_asleep']
            guard_id = guard
            times = sleep_log['times']
    freq_minutes_asleep = Counter(times)
    return int(guard_id), freq_minutes_asleep.most_common(1)[0][0]


if __name__ == '__main__':
    pardir = os.path.abspath(os.path.join(__file__, os.path.pardir))
    input = os.path.join(pardir, 'input.txt')

    logs = parse_logs(input)
    guard_logs = track_sleep_schedule(logs)
    guard_id, time = select_guard(guard_logs)
    print('Part 1:', guard_id * time)