def group_by_context(shape):
    res = {
        'face_contour': shape[0:17].tolist(),
        'eyebrow_right': shape[17:22].tolist(),
        'eyebrow_left': shape[22:27].tolist(),
        'nose_median': shape[27:31].tolist(),
        'nose_bottom': shape[31:36].tolist(),
        'eye_right': shape[36:42].tolist(),
        'eye_left': shape[42:48].tolist(),
        'lips_outer': shape[48:60].tolist(),
        'lips_inner': shape[60:].tolist(),
    }
    return res
