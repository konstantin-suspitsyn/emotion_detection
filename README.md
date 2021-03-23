# emotion_detection
9 классов определения эмоций

Дипломная работа по определению эмоций
https://www.kaggle.com/c/skillbox-computer-vision-project

![Camera preview](https://github.com/konstantin-suspitsyn/emotion_detection/blob/main/emotions_camera.gif "Camera preview")

Весь путь обучения можно пройти в файле cv_emotions_Resnet_v1.ipynb
Ссылка на zip архивы с данными train/test:
https://www.kaggle.com/c/skillbox-computer-vision-project/data

Рабочая модель для веб-камеры в файле camera_action.py
Финальную модель можно скачать по ссылке:
https://drive.google.com/file/d/1_1Ew5soqEUQ0llVDFXuXKhJAqjMtVDYi/view?usp=sharing

Структура папок должна быть следующая:
BASE_PATH/ <br>
├─ dataset/                 Содержит изображения<br>
│  ├─ test_kaggle/          тестовые изображения<br>
│  └─ train/                изображения для обучения<br>
│     ├─ {эмоция_1}/<br>
│     ├─ {эмоция_2}/<br>
│     └─ ...<br>
└─ zip/                     Скачанные архивы<br>
└─ text_files/              Всякие *.csv<br>
└─ exported_models/         Готовые модели<br>
