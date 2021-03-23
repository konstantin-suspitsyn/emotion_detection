class CamereAction:
    '''
    Распознаем эмоции онлайн. Нужна веб-камер
    '''
    import cv2
    import tensorflow as tf
    import numpy as np

    # Линк на .h5 модель по распознаванию эмоций
    # Скачайте из Google Disk: https://drive.google.com/file/d/1_1Ew5soqEUQ0llVDFXuXKhJAqjMtVDYi/view?usp=sharing
    MODEL_LINK = 'exported_models\\resnet_finetuned.h5'
    # Линк на стандартную haarcascade_frontalface_default.xml из Из OpenCV
    H_LINK = 'exported_models\\haarcascade_frontalface_default.xml'
    # Эмоции - выход из модели
    EMOTIONS = ['Злость', 'Презрение', 'Отвращение', 'Страх', 'Счастье', 'Нейтрально', 'Грусть', 'Удивление', 'Неуверенность']

    def __init__(self):
        self.model = self.tf.keras.models.load_model(self.MODEL_LINK)
        self.face_detector = self.cv2.CascadeClassifier(self.H_LINK)

    def decode_img(self, file, img_height=224, img_width=224):
        # Поменять размер картинки до нужного
        return self.tf.image.resize(file, [img_height, img_width])

    def run_camera(self):

        font_family = self.cv2.FONT_HERSHEY_COMPLEX
        font_scale = 0.5
        font_width = 2

        # Сделаем разные цвета для разных эмоций
        # [(цвет фона), (цвет текста)]
        color_list = [[(0, 0, 255), (255, 255, 255)],
                      [(124, 47, 124), (255, 255, 255)],
                      [(145, 81, 102), (255, 255, 255)],
                      [(149, 160, 81), (0, 0, 0)],
                      [(0, 255, 166), (0, 0, 0)],
                      [(135, 212, 80), (0, 0, 0)],
                      [(106, 93, 249), (0, 0, 0)],
                      [(67, 255, 124), (0, 0, 0)],
                      [(91, 222, 66), (0, 0, 0)]]

        cam = self.cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Не удалось открыть камеру")
        else:
            print("Камера запущена. Чтобы выключить ее, нажмите кнопку q")

        while (True):
            ret, frame = cam.read()

            rgb_image = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2RGB)
            gray = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                face_boundingbox_rgb = rgb_image[y:y + h, x:x + w]

                # Номер эмоции
                i = self.np.argmax(self.model.predict(self.decode_img(face_boundingbox_rgb)[None, :, :, :]))
                # Эмоция текст
                emotion = self.EMOTIONS[i]
                # Цвет текста
                text_color = color_list[i][1]
                # Цвет фона и рамок
                color_bg = color_list[i][0]

                # Рамка вокруг лица
                self.cv2.rectangle(frame, (x, y), (x + w, y + h), color_bg, 2)
                # Определяем размер текста, чтобы нарисовать под ним фон
                text_size = self.cv2.getTextSize(emotion, font_family, font_scale, font_width)
                self.cv2.rectangle(frame, (x, y), (x + text_size[0][0] + 7, y - text_size[0][1] - 10), color_bg, -1)
                # Помещаем текст эмоции
                self.cv2.putText(frame, emotion, (x + 7, y - 7), font_family, font_scale, text_color, font_width)

            self.cv2.imshow("Facial emotion recognition", frame)

            if self.cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    a = CamereAction()
    a.run_camera()