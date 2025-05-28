def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    start, end = sorted_intervals[0]
    
    for interval in sorted_intervals[1:]:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            merged.append((start, end))
            start, end = interval
    
    merged.append((start, end))
    return merged

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    
    pupil_intervals = []
    for i in range(0, len(pupil), 2):
        start = max(pupil[i], lesson_start)
        end = min(pupil[i+1], lesson_end)
        if start < end:
            pupil_intervals.append((start, end))
    
    tutor_intervals = []
    for i in range(0, len(tutor), 2):
        start = max(tutor[i], lesson_start)
        end = min(tutor[i+1], lesson_end)
        if start < end:
            tutor_intervals.append((start, end))
    
    # Объединяем пересекающиеся интервалы
    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)
    
    # Находим общее время присутствия
    total_time = 0
    i, j = 0, 0
    while i < len(pupil_merged) and j < len(tutor_merged):
        start_overlap = max(pupil_merged[i][0], tutor_merged[j][0])
        end_overlap = min(pupil_merged[i][1], tutor_merged[j][1])
        
        if start_overlap < end_overlap:
            total_time += end_overlap - start_overlap
        
        if pupil_merged[i][1] < tutor_merged[j][1]:
            i += 1
        else:
            j += 1
    
    return total_time