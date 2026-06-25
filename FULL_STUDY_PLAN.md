# Python AI/ML — Full 3-4 Month Study Plan

> **Start Date:** February 21, 2026  
> **End Date:** ~June 15, 2026 (16 weeks)  
> **Pace:** 2-3 hours/day (weekdays), 4-5 hours (weekends)  
> **Your Current Level:** NumPy ✅ | Pandas 🔶 | Matplotlib 🔶 | Sklearn Basics ✅

---

## Phase Overview

| Phase | Weeks | Focus | Outcome |
|-------|-------|-------|---------|
| **Phase 1** | Week 1-2 | Pandas Mastery + Matplotlib OOP | Can wrangle any dataset |
| **Phase 2** | Week 3-4 | Supervised ML Deep Dive | Master classification & regression |
| **Phase 3** | Week 5-6 | Unsupervised ML + Feature Engineering | Clustering, PCA, pipelines |
| **Phase 4** | Week 7-8 | End-to-End ML Projects | 3 portfolio projects |
| **Phase 5** | Week 9-10 | Deep Learning Foundations (Neural Nets) | Build basic NNs from scratch + Keras |
| **Phase 6** | Week 11-12 | CNNs + Computer Vision | Image classification |
| **Phase 7** | Week 13-14 | NLP + Text Processing | Sentiment analysis, text classification |
| **Phase 8** | Week 15-16 | Advanced Topics + Final Capstone | Deployment, Transformers intro, capstone |

---

## PHASE 1 — Pandas Mastery + Matplotlib OOP (Week 1-2)
**Feb 21 – Mar 6**

### Week 1: Pandas DataFrame Deep Dive

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 1** | Reading Data | `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`, explore Kaggle datasets | CampusX Pandas Playlist #5-6 |
| **Day 2** | DataFrame Operations | `sort_values()`, `value_counts()`, `nunique()`, `apply()`, `map()` | CampusX Pandas Playlist #7-8 |
| **Day 3** | Filtering & Selection | Boolean indexing, `.query()`, `.isin()`, conditional column creation | CampusX Pandas Playlist #9-10 |
| **Day 4** | GroupBy & Aggregation | `groupby()`, `agg()`, `transform()`, `pivot_table()`, multi-level grouping | CampusX Pandas Playlist #11-13 |
| **Day 5** | Merging & Joining | `merge()` (inner/outer/left/right), `concat()`, `join()`, multi-key merges | CampusX Pandas Playlist #14-15 |
| **Day 6** | Missing Data & Cleaning | `fillna()`, `dropna()`, `duplicated()`, `drop_duplicates()`, string methods `.str` | CampusX Pandas Playlist #16-17 |
| **Day 7** | **Mini Project** | Exploratory Data Analysis on Titanic OR Netflix dataset — full EDA notebook | Practice day |

**Deliverable:** Complete `pandas/dataframe.ipynb` with all operations + 1 EDA project notebook

### Week 2: Matplotlib OOP + Seaborn

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 8** | Matplotlib OOP API | `fig, ax = plt.subplots()`, multiple axes, `fig.add_subplot()`, styling axes | Corey Schafer Matplotlib Playlist |
| **Day 9** | Subplots & Layouts | `plt.subplots(2,3)`, `GridSpec`, shared axes, `tight_layout()`, `suptitle()` | Corey Schafer Matplotlib #3-4 |
| **Day 10** | Annotations & Customization | `ax.annotate()`, `ax.text()`, arrows, custom ticks, `savefig()`, DPI | Matplotlib docs + practice |
| **Day 11** | Seaborn Essentials | `sns.heatmap()`, `sns.pairplot()`, `sns.catplot()`, `sns.violinplot()`, themes | StatQuest + Seaborn docs |
| **Day 12** | Seaborn Advanced | `sns.FacetGrid()`, `sns.jointplot()`, `sns.regplot()`, color palettes | CampusX Seaborn session |
| **Day 13** | Plotly Interactive (Intro) | `plotly.express` basics: scatter, bar, line, hover, `fig.show()` | Plotly Express quickstart |
| **Day 14** | **Mini Project** | Full EDA Report with 10+ visualizations on a dataset (auto-sales, housing, etc.) | Practice day |

**Deliverable:** `matplotlib/advanced_matplotlib.ipynb` + `seaborn/seaborn_eda.ipynb`

---

## PHASE 2 — Supervised ML Deep Dive (Week 3-4)
**Mar 7 – Mar 20**

### Week 3: Classification Algorithms

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 15** | K-Nearest Neighbors (KNN) | Theory (distance metrics, K selection), `KNeighborsClassifier`, Iris/Wine dataset | StatQuest KNN video |
| **Day 16** | KNN Tuning + Evaluation | Hyperparameter tuning (`n_neighbors`, `weights`), `GridSearchCV` on KNN, confusion matrix | CampusX KNN session |
| **Day 17** | Support Vector Machine (SVM) | Linear SVM theory (margin, support vectors), `SVC(kernel='linear')`, decision boundary plot | StatQuest SVM videos (2 parts) |
| **Day 18** | SVM Kernels | RBF, polynomial kernels, `gamma`, `C` parameter, `GridSearchCV` on SVM | CampusX SVM session |
| **Day 19** | Naive Bayes | Bayes theorem, `GaussianNB`, `MultinomialNB`, text classification intro | StatQuest Naive Bayes |
| **Day 20** | Ensemble: Random Forest | Bagging concept, `RandomForestClassifier`, feature importance, `n_estimators` | StatQuest Random Forest (2 parts) |
| **Day 21** | **Weekend Project** | Heart Disease Prediction — full pipeline: EDA → preprocess → train 5 models → compare | Kaggle Heart Disease dataset |

**Deliverable:** `scikitlearn/classification_algorithms.ipynb` + `projects/heart_disease.ipynb`

### Week 4: Regression Algorithms + Model Selection

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 22** | Polynomial Regression | `PolynomialFeatures`, overfitting visualization, degree tuning | CampusX Polynomial Regression |
| **Day 23** | Regularization | Ridge (`L2`), Lasso (`L1`), ElasticNet, `alpha` tuning, coefficient shrinkage plot | StatQuest Ridge/Lasso videos |
| **Day 24** | Decision Tree Regressor | `DecisionTreeRegressor`, `max_depth`, pruning, overfitting vs underfitting | StatQuest Decision Tree Regression |
| **Day 25** | Gradient Boosting | `GradientBoostingRegressor`, XGBoost intro (`pip install xgboost`), `learning_rate` | StatQuest Gradient Boost (4 parts) |
| **Day 26** | Model Selection & Pipelines | `Pipeline`, `ColumnTransformer`, `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV` | Sklearn docs + CampusX Pipeline session |
| **Day 27** | Model Saving & Loading | `joblib.dump()`, `joblib.load()`, `pickle`, model versioning best practices | Sklearn docs |
| **Day 28** | **Weekend Project** | House Price Prediction (Kaggle) — full pipeline with feature engineering + model comparison | Kaggle House Prices dataset |

**Deliverable:** `scikitlearn/regression_advanced.ipynb` + `projects/house_price.ipynb`

---

## PHASE 3 — Unsupervised ML + Feature Engineering (Week 5-6)
**Mar 21 – Apr 3**

### Week 5: Unsupervised Learning

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 29** | K-Means Clustering | Theory (centroids, inertia), `KMeans`, Elbow method, `silhouette_score` | StatQuest K-Means |
| **Day 30** | K-Means Projects | Customer segmentation (Mall Customers dataset), cluster visualization | CampusX K-Means |
| **Day 31** | Hierarchical Clustering | Agglomerative clustering, dendrograms, `scipy.cluster.hierarchy`, linkage methods | StatQuest Hierarchical Clustering |
| **Day 32** | DBSCAN | Density-based clustering, `eps`, `min_samples`, noise handling, comparison with K-Means | CampusX DBSCAN session |
| **Day 33** | PCA (Principal Component Analysis) | Dimensionality reduction theory, `PCA(n_components)`, variance explained, scree plot | StatQuest PCA (5 parts — essential!) |
| **Day 34** | PCA Application | PCA on MNIST/faces dataset, visualization in 2D/3D, PCA + classification pipeline | 3Blue1Brown Linear Algebra essence |
| **Day 35** | **Weekend Project** | Customer Segmentation Project — PCA → K-Means → visualization → business insights | Practice day |

**Deliverable:** `scikitlearn/unsupervised.ipynb` + `projects/customer_segmentation.ipynb`

### Week 6: Feature Engineering & Advanced Preprocessing

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 36** | Feature Engineering Basics | Creating new features, binning, log transforms, interaction features | CampusX Feature Engineering |
| **Day 37** | Encoding Strategies | `OrdinalEncoder`, `TargetEncoder`, frequency encoding, binary encoding | Sklearn docs + CampusX |
| **Day 38** | Feature Selection | `SelectKBest`, `RFE` (Recursive Feature Elimination), correlation analysis, VIF | CampusX Feature Selection |
| **Day 39** | Handling Imbalanced Data | SMOTE (`imblearn`), class weights, `RandomOverSampler`, `RandomUnderSampler` | Krish Naik Imbalanced Data |
| **Day 40** | Outlier Detection | Z-score, IQR method, `IsolationForest`, `LocalOutlierFactor` | CampusX Outlier Detection |
| **Day 41** | Time Series Basics | `pd.to_datetime()`, resampling, rolling averages, trend/seasonality | CampusX Time Series intro |
| **Day 42** | **Weekend Review** | Revise Weeks 1-6, make flashcards of key concepts, clean up all notebooks | Review day |

**Deliverable:** `scikitlearn/feature_engineering.ipynb`

---

## PHASE 4 — End-to-End ML Projects (Week 7-8)
**Apr 4 – Apr 17**

### Week 7: Project Week 1

| Day | Topic | Project |
|-----|-------|---------|
| **Day 43** | Project 1 — EDA | **Loan Default Prediction**: Load data, EDA, 15+ visualizations |
| **Day 44** | Project 1 — Preprocessing | Feature engineering, encoding, scaling, handling missing data |
| **Day 45** | Project 1 — Modeling | Train 6+ models, cross-validation, hyperparameter tuning |
| **Day 46** | Project 1 — Finalize | Best model selection, classification report, save model, write README |
| **Day 47** | Project 2 Start | **Spam Email Detector**: Load SMS/email data, text preprocessing (`CountVectorizer`, `TfidfVectorizer`) |
| **Day 48** | Project 2 Finish | Naive Bayes + Logistic Regression, evaluation, confusion matrix |
| **Day 49** | **Portfolio** | Push both projects to GitHub with proper README, requirements.txt |

### Week 8: Project Week 2

| Day | Topic | Project |
|-----|-------|---------|
| **Day 50** | Project 3 Start | **Movie Recommendation System**: Load MovieLens data, EDA |
| **Day 51** | Project 3 | Content-based filtering (cosine similarity, TF-IDF on genres/descriptions) |
| **Day 52** | Project 3 Finish | Collaborative filtering intro, evaluation, deploy as function |
| **Day 53** | Streamlit Intro | `pip install streamlit`, basic app: title, input, output, `st.dataframe()` |
| **Day 54** | Streamlit ML App | Deploy House Price Predictor as a Streamlit web app |
| **Day 55** | Flask API (Intro) | Build a simple REST API serving ML predictions (`flask`, `jsonify`) |
| **Day 56** | **Portfolio Review** | Clean all GitHub repos, write LinkedIn post about ML journey so far |

**Deliverable:** 3 complete projects on GitHub + 1 Streamlit app + 1 Flask API

---

## PHASE 5 — Deep Learning Foundations (Week 9-10)
**Apr 18 – May 1**

### Week 9: Neural Networks from Scratch + Keras

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 57** | Perceptron & Activation Functions | Sigmoid, ReLU, Tanh, Softmax — math + plots, single neuron implementation | 3Blue1Brown Neural Networks Ch.1 |
| **Day 58** | Forward Propagation | Build a 2-layer NN from scratch (NumPy only), matrix multiplication | 3Blue1Brown Neural Networks Ch.2 |
| **Day 59** | Backpropagation | Chain rule, gradient descent, loss functions (MSE, Cross-Entropy) | 3Blue1Brown Neural Networks Ch.3-4 |
| **Day 60** | Keras/TensorFlow Setup | `pip install tensorflow`, `Sequential` model, `Dense` layers, `.compile()`, `.fit()` | TensorFlow official tutorials |
| **Day 61** | Keras Classification | MNIST digit classification, `categorical_crossentropy`, `accuracy`, training curves | CampusX Deep Learning sessions |
| **Day 62** | Keras Regression | Boston/California housing with neural net, compare with sklearn models | Practice |
| **Day 63** | **Weekend Project** | Fashion MNIST classification — build, train, evaluate, plot confusion matrix | Kaggle Fashion MNIST |

**Deliverable:** `deep_learning/nn_from_scratch.ipynb` + `deep_learning/keras_basics.ipynb`

### Week 10: Improving Neural Networks

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 64** | Optimizers | SGD, Adam, RMSProp, learning rate schedules, comparison on same dataset | StatQuest Adam Optimizer |
| **Day 65** | Regularization in DL | Dropout, L2 regularization, Batch Normalization, Early Stopping | CampusX Regularization |
| **Day 66** | Hyperparameter Tuning DL | `keras_tuner`, epochs, batch size, learning rate, number of layers | Keras Tuner docs |
| **Day 67** | Callbacks & Monitoring | `EarlyStopping`, `ModelCheckpoint`, `TensorBoard`, training visualization | TensorFlow docs |
| **Day 68** | Data Augmentation Intro | `ImageDataGenerator`, random flips/rotations/zoom, augmented training | Keras docs |
| **Day 69** | Review & Consolidate | Revisit all DL concepts, create a cheat sheet | Review day |
| **Day 70** | **Weekend Project** | Binary classification on Tabular data with fully connected NN (Churn prediction) | Practice |

**Deliverable:** `deep_learning/improving_nn.ipynb` + `projects/churn_nn.ipynb`

---

## PHASE 6 — CNNs + Computer Vision (Week 11-12)
**May 2 – May 15**

### Week 11: Convolutional Neural Networks

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 71** | CNN Theory | Convolution operation, filters, stride, padding, feature maps — visual understanding | 3Blue1Brown + StatQuest CNN |
| **Day 72** | Pooling & Architecture | MaxPooling, AveragePooling, Flatten, building CNN in Keras | CampusX CNN session |
| **Day 73** | CIFAR-10 Classification | Build CNN for CIFAR-10, training curves, data augmentation | Practice |
| **Day 74** | Transfer Learning Theory | Pre-trained models (VGG16, ResNet50, MobileNet), feature extraction vs fine-tuning | CampusX Transfer Learning |
| **Day 75** | Transfer Learning Practice | `tf.keras.applications.VGG16`, freeze layers, fine-tune on custom dataset | TensorFlow Transfer Learning tutorial |
| **Day 76** | Image Classification Project | Cats vs Dogs classifier using transfer learning, save model | Kaggle Cats vs Dogs |
| **Day 77** | **Weekend Project** | Plant Disease Detection OR X-Ray classification (medical imaging) | Kaggle dataset |

**Deliverable:** `deep_learning/cnn.ipynb` + `projects/image_classifier.ipynb`

### Week 12: Advanced CV Concepts

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 78** | Object Detection Intro | YOLO concept, bounding boxes, IoU, pre-trained YOLO with OpenCV | YouTube YOLO tutorials |
| **Day 79** | OpenCV Basics | `cv2.imread()`, resize, crop, color spaces, edge detection, face detection | OpenCV Python tutorials |
| **Day 80** | Image Preprocessing | Normalization, resizing strategies, handling different image sizes | Practice |
| **Day 81** | GANs Intro (Theory) | Generator vs Discriminator concept, GAN training loop diagram | StatQuest + 3Blue1Brown |
| **Day 82** | Simple GAN | Build a basic GAN for MNIST digit generation in Keras | TensorFlow GAN tutorial |
| **Day 83** | Review CV | Consolidate all CV concepts, review architectures | Review day |
| **Day 84** | **Weekend Project** | Real-time Object Detection App using YOLO + OpenCV + webcam | Practice |

**Deliverable:** `deep_learning/object_detection.ipynb` + `deep_learning/gan_basic.ipynb`

---

## PHASE 7 — NLP + Text Processing (Week 13-14)
**May 16 – May 29**

### Week 13: NLP Foundations

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 85** | Text Preprocessing | Tokenization, stopwords, stemming, lemmatization (`nltk`, `spacy`) | CampusX NLP sessions |
| **Day 86** | Bag of Words & TF-IDF | `CountVectorizer`, `TfidfVectorizer`, document-term matrix | CampusX BOW/TF-IDF |
| **Day 87** | Text Classification (ML) | Sentiment analysis with Logistic Regression + TF-IDF on IMDB reviews | Practice |
| **Day 88** | Word Embeddings | Word2Vec theory, `gensim` Word2Vec, word similarity, analogy tasks | StatQuest Word2Vec |
| **Day 89** | Pre-trained Embeddings | GloVe embeddings, loading pre-trained vectors, embedding layer in Keras | TensorFlow Embedding tutorial |
| **Day 90** | RNN & LSTM Theory | Sequence models, vanishing gradient, LSTM gates, GRU | StatQuest LSTM |
| **Day 91** | **Weekend Project** | Sentiment Analysis on Twitter/Amazon Reviews — TF-IDF vs LSTM comparison | Kaggle dataset |

**Deliverable:** `nlp/text_preprocessing.ipynb` + `nlp/sentiment_analysis.ipynb`

### Week 14: Advanced NLP

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 92** | LSTM in Keras | Build LSTM for text classification, `Embedding` → `LSTM` → `Dense` | CampusX LSTM |
| **Day 93** | Sequence-to-Sequence | Encoder-decoder concept, simple text generation | Practice |
| **Day 94** | Attention Mechanism | Attention theory, self-attention, why transformers replaced RNNs | StatQuest Attention |
| **Day 95** | Transformers Intro | Transformer architecture (encoder-decoder), positional encoding | "Attention Is All You Need" summary |
| **Day 96** | Hugging Face Basics | `pip install transformers`, `pipeline()` for sentiment, NER, summarization, QA | Hugging Face course (free) |
| **Day 97** | Fine-tuning BERT | Fine-tune `bert-base-uncased` on custom text classification task | Hugging Face fine-tuning tutorial |
| **Day 98** | **Weekend Project** | News Article Classifier OR Fake News Detector using BERT/DistilBERT | Kaggle dataset |

**Deliverable:** `nlp/lstm_text.ipynb` + `nlp/transformers_intro.ipynb` + `projects/news_classifier.ipynb`

---

## PHASE 8 — Advanced Topics + Capstone (Week 15-16)
**May 30 – Jun 15**

### Week 15: Deployment & MLOps Basics

| Day | Topic | Tasks | Resources |
|-----|-------|-------|-----------|
| **Day 99** | Streamlit Advanced | Multi-page apps, file upload, charts, caching, session state | Streamlit docs |
| **Day 100** | FastAPI for ML | Build ML API with FastAPI, request/response models, auto docs | FastAPI tutorial |
| **Day 101** | Docker Basics | Dockerfile for ML app, `docker build`, `docker run`, containerize Streamlit app | Docker for Data Science tutorial |
| **Day 102** | Cloud Deployment | Deploy Streamlit app to Streamlit Cloud OR Hugging Face Spaces | Platform docs |
| **Day 103** | MLflow Intro | Experiment tracking, model registry, `mlflow.log_param()`, `mlflow.log_metric()` | MLflow quickstart |
| **Day 104** | SQL for Data Science | `SELECT`, `JOIN`, `GROUP BY`, `HAVING`, subqueries — SQLite with Python (`sqlite3`) | Mode Analytics SQL tutorial |
| **Day 105** | **Weekend** | Revise deployment pipeline, prepare for capstone | Review |

### Week 16: Capstone Project

| Day | Topic | Tasks |
|-----|-------|-------|
| **Day 106** | Capstone Planning | Choose project, define scope, collect data, create GitHub repo |
| **Day 107** | Data Collection & EDA | Web scraping / Kaggle API, thorough EDA with 20+ visualizations |
| **Day 108** | Feature Engineering | Domain-specific features, encoding, scaling, pipeline setup |
| **Day 109** | Model Training | Train 5+ models (ML + DL), cross-validation, hyperparameter tuning |
| **Day 110** | Model Evaluation | Comprehensive evaluation, model interpretability (SHAP/LIME intro) |
| **Day 111** | Deployment | Streamlit/FastAPI app, Docker container, deploy to cloud |
| **Day 112** | **Documentation & Portfolio** | README, demo video, LinkedIn post, update resume |

---

## Capstone Project Ideas (Pick 1)

1. **End-to-End Disease Prediction System** — Tabular data → ML models → Streamlit app → deployed
2. **Image-based Food Calorie Estimator** — CNN + transfer learning → Streamlit with image upload
3. **Resume Screening System** — NLP + BERT → classify resumes by job role → FastAPI
4. **Stock Price Dashboard** — Time series + LSTM → Streamlit interactive dashboard
5. **Multi-language Sentiment Analyzer** — Hugging Face transformers → Streamlit app

---

## Weekly Checkpoint System

At the end of every week, answer these:
- [ ] Did I complete all notebooks for this week?
- [ ] Can I explain every concept I learned without looking at notes?
- [ ] Did I push code to GitHub?
- [ ] Did I complete the mini project?
- [ ] What was the hardest concept, and do I need to revisit it?

---

## Recommended YouTube Channels & Playlists

| Channel | Best For | Playlist |
|---------|----------|----------|
| **CampusX** (Hindi) | Pandas, Sklearn, Full ML | "100 Days of ML" |
| **StatQuest** (English) | ML/DL theory (visual) | All ML/DL videos |
| **3Blue1Brown** | Linear Algebra, Neural Nets | "Essence of Linear Algebra", "Neural Networks" |
| **Krish Naik** (Hindi) | End-to-end projects, deployment | ML + DL playlists |
| **Corey Schafer** | Matplotlib, Pandas, Python | Individual topic playlists |
| **Sentdex** | Practical Python ML/DL | ML with Python series |
| **freeCodeCamp** | Long-form courses | TensorFlow, Scikit-learn full courses |
| **Hugging Face** | NLP, Transformers | Official free course |

---

## Books (Optional, for deeper understanding)

1. **"Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow"** — Aurélien Géron (THE best book)
2. **"Python Data Science Handbook"** — Jake VanderPlas (free online)
3. **"Deep Learning with Python"** — François Chollet (Keras creator)

---

## Tools to Install Along the Way

```
# Phase 1-4
pip install numpy pandas matplotlib seaborn plotly scikit-learn jupyter

# Phase 5-6
pip install tensorflow keras keras-tuner opencv-python

# Phase 7
pip install nltk spacy gensim transformers datasets

# Phase 8
pip install streamlit fastapi uvicorn mlflow docker shap lime xgboost lightgbm
```

---

## GitHub Repository Structure (End Goal)

```
Python_AIML/
├── numpy/                  # ✅ Done
├── pandas/                 # Phase 1
├── matplotlib/             # Phase 1
├── seaborn/                # Phase 1
├── scikitlearn/            # Phase 2-3
│   ├── classification/
│   ├── regression/
│   ├── unsupervised/
│   └── feature_engineering/
├── deep_learning/          # Phase 5-6
│   ├── nn_from_scratch/
│   ├── keras_basics/
│   ├── cnn/
│   └── gan/
├── nlp/                    # Phase 7
├── projects/               # Phase 4, 7-8
│   ├── heart_disease/
│   ├── house_price/
│   ├── spam_detector/
│   ├── image_classifier/
│   ├── sentiment_analysis/
│   └── capstone/
├── deployment/             # Phase 8
├── mini projects/          # ✅ Existing
└── README.md
```

---

## Summary Timeline

```
Feb 21 ─── Phase 1: Pandas + Matplotlib ──── Mar 6
Mar 7  ─── Phase 2: Supervised ML ────────── Mar 20
Mar 21 ─── Phase 3: Unsupervised + FE ────── Apr 3
Apr 4  ─── Phase 4: ML Projects ──────────── Apr 17
Apr 18 ─── Phase 5: Deep Learning Basics ─── May 1
May 2  ─── Phase 6: CNNs + CV ────────────── May 15
May 16 ─── Phase 7: NLP + Transformers ───── May 29
May 30 ─── Phase 8: Deploy + Capstone ────── Jun 15
```

> **By June 15, you will have:** 6+ portfolio projects on GitHub, experience with ML + DL + NLP + CV, a deployed web app, and strong foundations to pursue ML Engineer / Data Scientist roles or advanced topics like Reinforcement Learning, MLOps, or LLMs.

---

*Generated on Feb 21, 2026 — Good luck! 🚀*
