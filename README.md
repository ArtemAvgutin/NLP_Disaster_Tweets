# NLP_Disaster_Tweets
## A binary classifier for identifying disaster tweets using various methods. / Бинарный классификатор для определения твитов о катастрофак с использованием различных методов.

#### Описание задачи и результатов:
* Имеются твиты пользователей о различных катастрофах. Каждому твиту присвоена метка 1 или 0, которая говорит, что твит описывает реальную катастрофу или нет. На основании этих данных необходимо построить классификатор.
* Была произведена подготовка данных: Избавление от лишних колонок, Очистка пунктуации, Удаление стоп-слов, Лемматизация (приведение к начальной форме слова).
* Была произведена токинезация и векторизация.
* Были использ-ованы такие методы как: XGBoostClassifier, AdaBoostClassifier, RandomForest и Deep Learning Model.
* Как резульат были получены модели с удовлетворяющей точностью работыю.

#### Точность классификаторов / Classifier accuracy
![image](https://github.com/ArtemAvgutin/NLP_Disaster_Tweets/assets/131138862/9c3d1255-137c-464a-9d20-f82822eabe64)

#### Точность Deep Learning Model / Deep Learning Model accuracy
![image](https://github.com/ArtemAvgutin/NLP_Disaster_Tweets/assets/131138862/fe940d0f-c230-44de-b538-03cc9f4d7bce)

#### Description of the task and results:
* There are user tweets about various disasters. Each tweet is given a label of 1 or 0, which indicates whether the tweet describes a real disaster or not. Based on this data, it is necessary to build a classifier.
* The data was prepared: Getting rid of extra columns, Cleaning up punctuation, Removing stop words, Lemmatization (reduction to the initial form of the word).
* Tokinesization and vectorization were performed.
* Methods such as XGBoostClassifier, AdaBoostClassifier, RandomForest and Deep Learning Model were used.
* As a result, models with satisfactory performance accuracy were obtained.
