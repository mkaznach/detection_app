from PIL import Image

def find_best_box(preds, apple_label = 47) -> list:
    max_score = 0
    item = -1
    for i, label in enumerate(preds['labels']):
        if label == apple_label and preds['scores'][i] > max_score:
            max_score = preds['scores'][i]
            item = i
    return max_score, preds['bboxes'][item]

def crop_apple(input_path : str, output_path : str, box) -> None:
    original_image = Image.open(input_path)
    cropped_image = original_image.crop(box)
    cropped_image.save(output_path)
