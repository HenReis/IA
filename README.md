G12 — Modelação Preditiva de Funcionários
Tecnologias e Sistemas de Informação para a Web · 2025/26

Duas pipelines scikit-learn para prever comportamento de funcionários a partir do dataset employee_data.csv (1249 registos, 35 atributos).

---

Tarefas
| Tarefa | Alvo | Métrica |
|--------|------|---------|
| Regressão | MonthlyIncome — salário mensal | R² / RMSE |
| Classificação | Attrition — saída da empresa (Yes/No) | F1-Score |

---

Resultados
| Tarefa | Métrica | Valor |
|--------|---------|-------|
| Regressão | R² no teste | 0.9529 |
| Regressão | RMSE no teste | 999.82 |
| Classificação | F1-Score no teste | 0.5250 |
| Classificação | Threshold optimizado | 0.710 |

---

Algoritmos escolhidos
Regressão — GradientBoostingRegressor (scikit-learn), afinado com RandomizedSearchCV (40 iterações, 5-fold CV)
Classificação — LogisticRegression com class_weight='balanced', threshold optimizado via TunedThresholdClassifierCV (5-fold CV estratificado no treino)

---

Dependências
scikit-learn >= 1.5   # obrigatório — TunedThresholdClassifierCV só existe a partir desta versão
numpy
pandas
matplotlib
seaborn


Instalar:
pip install "scikit-learn>=1.5" numpy pandas matplotlib seaborn


---

Ficheiros
G12_notebook.ipynb                — análise exploratória, treino e avaliação
G12_pipeline_regression.pkl       — pipeline de regressão serializada
G12_pipeline_classification.pkl   — pipeline de classificação serializada
employee_data.csv                 — dataset
G12_relatorio.docx                — relatório do grupo
README.txt                        — lista de dependências (formato Moodle)


---

Utilização das pipelines
import pickle

with open("G12_pipeline_regression.pkl", "rb") as f:
    reg = pickle.load(f)

with open("G12_pipeline_classification.pkl", "rb") as f:
    clf = pickle.load(f)

# X é um DataFrame com as colunas originais do dataset (sem os targets)
y_income   = reg.predict(X)   # salário mensal previsto
y_attrition = clf.predict(X)  # 0 = fica, 1 = sai (threshold=0.710 já incorporado)