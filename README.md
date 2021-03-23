# emotion_detection
9 классов определения эмоций
<br>
Дипломная работа по определению эмоций<br>
https://www.kaggle.com/c/skillbox-computer-vision-project<br>
<br>
![Camera preview](https://github.com/konstantin-suspitsyn/emotion_detection/blob/main/emotions_camera.gif "Camera preview")<br>
<br>
Весь путь обучения можно пройти в файле cv_emotions_Resnet_v1.ipynb<br><br>
Ссылка на zip архивы с данными train/test:<br>
https://www.kaggle.com/c/skillbox-computer-vision-project/data<br>
<br>
Рабочая модель для веб-камеры в файле camera_action.py<br>
Финальную модель можно скачать по ссылке:<br>
https://drive.google.com/file/d/1_1Ew5soqEUQ0llVDFXuXKhJAqjMtVDYi/view?usp=sharing
<br>
Структура папок должна быть следующая:<br>
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
