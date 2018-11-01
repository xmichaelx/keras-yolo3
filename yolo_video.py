import argparse

from yolo import YOLO, detect_video

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--show_output', default=False, action="store_true",
        help='Show output in window'
    )

    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str, required=True,
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default=None,
        help = "[Optional] Video output path"
    )

    parser.add_argument(
        "--boxes", nargs='?', type=str, default=None,
        help="[Optional] Boxes output path"
    )


    FLAGS = parser.parse_args()
    detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output, FLAGS.boxes, FLAGS.show_output)
