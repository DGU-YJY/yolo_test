from detect_ex import *
from sppeech.transcribe_streaming_mic import *
from utils.speak import *
from utils.weather import *

yes = {"응", "네", "맞아"}
no = {"아니야", "아니", "틀려"}
operation = {"날씨", "옷", "딩동", "종료", "끝", "도움","기능"}

if __name__ == '__main__':

    language_code = "ko-KR"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)


    user_data = "user.txt"
    if os.path.exists(user_data):
        Fp = open(user_data,"r")
        user = Fp.readline()
        talk = "안녕하세요 "+user+"님"
        speak(talk)
        talk = "딩동이 무엇을 알려드릴까요?"
        speak(talk)
    else:
        Fp = open(user_data, 'w', encoding='utf-8')
        talk = "안녕하세요. 저는 딩동이에요."
        talk += "당신의 이름은 무엇인가요?"
        speak(talk)
        
        while True:
            user = None
            while user is None:
                user = listen_print_loop(responses)
            talk = user+"님이 맞으신가요?"
            speak(talk)
            op = None
            while op is None:
                op = listen_print_loop(responses)

            if op in yes:
                Fp.writelines(user)
                break
            else:
                talk = "이름을 다시 한번 말씀해주세요."
                speak(talk)
                
        talk = "반가워요 "+user+"님"
        speak(talk)
        talk = "딩동이 무엇을 알려드릴까요?"
        speak(talk)
    
    Fp.close()
    while True:
        op = listen_print_loop(responses)

        for i in operation:
            if i in op:
                if i == "날씨":
                    data = get_weather()
                    talk = weather_speak(data)
                    speak(talk)
                    talk = cloth(data)
                    speak(talk)
                    break
                
                elif i == "옷" or i == "딩동":
                    talk = "주변을 밝게 유지해주세요"
                    speak(talk)
                    talk = "주변이 밝지 않으면 색이 정확히 보이지 않아요"
                    speak(talk)

                    parser = argparse.ArgumentParser()
                    #parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
                    parser.add_argument('--weights', nargs='+', type=str, default='weights/best.pt', help='model.pt path(s)')
                    parser.add_argument('--source', type=str, default='0', help='source')
                    #parser.add_argument('--source', type=str, default='data/images', help='source')  # file/folder, 0 for webcam
                    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
                    #parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
                    parser.add_argument('--conf-thres', type=float, default=0.4, help='object confidence threshold')
                    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
                    parser.add_argument('--max-det', type=int, default=1000, help='maximum number of detections per image')
                    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
                    parser.add_argument('--view-img', action='store_true', help='display results')
                    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
                    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
                    parser.add_argument('--save-crop', type=bool ,default=True, help='save cropped prediction boxes')
                    # parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
                    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
                    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
                    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
                    parser.add_argument('--augment', action='store_true', help='augmented inference')
                    parser.add_argument('--update', action='store_true', help='update all models')
                    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
                    parser.add_argument('--name', default='exp', help='save results to project/name')
                    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
                    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
                    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
                    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
                    opt = parser.parse_args()
                    print(opt)
                    check_requirements(exclude=('tensorboard', 'pycocotools', 'thop'))

                    if opt.update:  # update all models (to fix SourceChangeWarning)
                        for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                            detect(opt=opt)
                            strip_optimizer(opt.weights)
                    else:
                        detect(opt=opt)
                    
                    break
                elif i == "종료" or i == "끝":
                    talk = "딩동이를 종료합니다."
                    speak(talk)
                    talk = "다음에 또 봐요, "+user+"님"
                    speak(talk)
                    talk = "좋은 하루 되세요"
                    speak(talk)
                    os._exit(1)
                else:
                    talk = "딩동이의 명령어는"
                    speak(talk)
                    for talk in operation:
                        speak(talk)
                    talk = "이 있어요"
                    break
            
            else:
                talk = "모르는 단어예요"
                speak(talk)
                talk = "명령어가 궁금하시면, 도움 을 말해보세요"
                speak(talk)
                break