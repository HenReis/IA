README — Grupo 12
=================

Pacotes externos utilizados
----------------------------

numpy
pandas
matplotlib
seaborn
scikit-learn >= 1.5

Notas importantes
-----------------

O ficheiro G12_pipeline_classification.pkl contém um objecto
TunedThresholdClassifierCV, introduzido no scikit-learn 1.5.
É OBRIGATÓRIO ter scikit-learn 1.5 ou superior instalado;
caso contrário o pickle.load() falhará com AttributeError.

Para instalar/actualizar o scikit-learn:
    pip install "scikit-learn>=1.5"

Todos os outros pacotes (numpy, pandas, matplotlib, seaborn)
fazem parte do ambiente científico padrão do Python.
Se necessário, instalar com:
    pip install numpy pandas matplotlib seaborn

Ficheiros entregues
-------------------

G12_notebook.ipynb               — Notebook com toda a análise e treino
G12_pipeline_regression.pkl      — Pipeline de regressão (prever MonthlyIncome)
G12_pipeline_classification.pkl  — Pipeline de classificação (prever Attrition)
employee_data.csv                — Dataset utilizado
G12_relatorio.docx               — Relatório do grupo

Resultados obtidos
------------------

Regressão   — R² no teste : 0.9529  |  RMSE: 999.82
Classificação — F1-Score  : 0.5250  |  Threshold optimizado: 0.710