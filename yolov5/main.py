user = ""
yes = {"응", "네", "맞아"}
no = {"아니야", "아니", "틀려"}
operation = {
    0:{"날씨","9시","아이싱","알송"}, 
    1:{"옷", "딩동", "띵동", "인동","의류","운동"}, 
    2:{"종료", "끝"}, 
    3:{"도움", "기능","돈"}
    }

helper = [
    "오늘의 날씨와 추천 옷차림이 궁금하시면", "날씨",
    "옷을 구별하고 싶으시면", "띵동",
    "딩동이를 종료하고 싶으시면", "종료",
    "를 말하세요."
]

from detect_e import *
from utils.speech2text import *
from utils.speak import *
from utils.weather import *


if __name__ == '__main__':
    global stop

    newUser = False

    user_file = "user.txt"
    if os.path.exists(user_file):
        Fp = open(user_file,"r", encoding='utf-8')
        user = Fp.readline()
        if user == "":
            newUser = True
    else:
        newUser = True
    
    if newUser:
        Fp = open(user_file, 'w', encoding='utf-8')
        talk = "안녕하세요. 저는 딩동이에요."
        speak(talk)
        talk = "당신의 이름은 무엇인가요?"
        speak(talk)
        
        while True:
            while user == "":
                user = listening()
            talk = user+"님이 맞으신가요?"
            speak(talk)
            op = ""
            while op == "":
                op = listening()

            if op in yes:
                Fp.writelines(user)
                break
            else:
                talk = "이름을 다시 한번 말씀해주세요."
                speak(talk)

    Fp.close()

    talk = "반가워요 "+user+"님"
    speak(talk)


    while True:
        talk = "딩동이 무엇을 알려드릴까요?"
        speak(talk)
        op = listening()
        get_op = False
        for i in operation:
            for j in operation[i]:
                if j in op: get_op = True; break
            if get_op: break
        
        if get_op:
            if i<1:
                data = get_weather()
                talk = weather_talk(data)
                speak(talk)
                talk = cloth(data)
                speak(talk)

            elif i<2:
            
                talk = "딩동이가 옷 구별을 시작합니다"
                speak(talk)
                talk = "주변을 밝게 유지해주세요"
                speak(talk)
                talk = "주변이 밝지 않으면 색이 정확히 보이지 않아요"
                speak(talk)


                parser = argparse.ArgumentParser()
                parser.add_argument('--weights', nargs='+', type=str, default='weights/best.pt', help='model.pt path(s)')
                parser.add_argument('--source', type=str, default='0', help='source')
                parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
                parser.add_argument('--conf-thres', type=float, default=0.4, help='object confidence threshold')
                parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
                parser.add_argument('--max-det', type=int, default=1000, help='maximum number of detections per image')
                parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
                parser.add_argument('--view-img', action='store_true', help='display results')
                parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
                parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
                parser.add_argument('--save-crop', type=bool ,default=True, help='save cropped prediction boxes')
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
            
            elif i<3:
                talk = user+'님 오늘도 좋은 하루 보내세요'
                speak(talk)
                break
            
            else:
                for j in helper:
                    speak(j)

                    

        elif op != "":
            talk = "모르는 단어예요"
            speak(talk)
            talk = "명령어가 궁금하시면, 도움 을 말해보세요"
            speak(talk)
            

