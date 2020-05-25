import time

from config.config import Config


def wait_until(predicate, error_msg, *args, **kwargs):
    time_to_end = time.time() + Config['conditions_wait_time']
    while time.time() < time_to_end:
        result = predicate(*args, **kwargs)
        if result:
            return result
        time.sleep(Config['polling_interval'])
        print('waiting condition')

    raise Exception(f'Time was exceeded waiting. {error_msg}')
