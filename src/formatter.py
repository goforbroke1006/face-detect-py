def group_by_context(shape):
    res = {
        'face_contour': shape[0:17],
        'eyebrow_right': shape[17:22],
        'eyebrow_left': shape[22:27],
        'nose_median': shape[27:31],
        'nose_bottom': shape[31:36],
        'eye_right': shape[36:42],
        'eye_left': shape[42:48],
        'lips_outer': shape[48:60],
        'lips_inner': shape[60:],
    }
    return res
