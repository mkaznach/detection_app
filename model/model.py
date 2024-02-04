from mmdet.apis import DetInferencer
import os

class model():
    def __init__(self):
        config_file = os.getcwd() + os.path.sep + "model" + os.path.sep + "rtmdet_tiny_8xb32-300e_coco.py"
        checkpoint_file = os.getcwd() + os.path.sep + "model" + os.path.sep + "rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth"
        self.inferencer = DetInferencer(config_file, checkpoint_file)

    def inference(self, path : str):
        return self.inferencer(path)
    
    def inference_with_show(self, path : str, out_dir : str):
        return self.inferencer(path, out_dir = out_dir, no_save_pred = False)