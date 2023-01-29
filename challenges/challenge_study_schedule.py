def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    try:
        return sum(
            target_time in range(_in, out + 1)
            for _in, out in permanence_period
        )
    except TypeError:
        return None
