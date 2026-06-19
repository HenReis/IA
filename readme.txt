README — Grupo 12
=================

Pacotes externos utilizados
----------------------------

numpy
pandas
matplotlib
seaborn
scikit-learn >= 1.0

Notas importantes
-----------------

O ficheiro G12_pipeline_classification.pkl contém um objecto
ThresholdClassifier, definido em G12_model.py (incluído na entrega).

Para carregar qualquer um dos pkl, G12_model.py deve estar no mesmo
directório que o script/notebook que faz pickle.load(). Não é necessária
nenhuma versão específica do scikit-learn — o ThresholdClassifier
é compatível com qualquer versão >= 1.0.

Exemplo de carregamento correcto:

    import pickle
    from G12_model import ThresholdClassifier   # G12_model.py no mesmo directório

    with open('G12_pipeline_classification.pkl', 'rb') as f:
        clf = pickle.load(f)
    preds = clf.predict(X)   # threshold optimizado aplicado automaticamente

Para instalar/actualizar o scikit-learn (se necessário):
    pip install scikit-learn

Ficheiros entregues
-------------------

G12_notebook.ipynb               — Notebook com toda a análise e treino
G12_pipeline_regression.pkl      — Pipeline de regressão (prever MonthlyIncome)
G12_pipeline_classification.pkl  — Pipeline de classificação (prever Attrition)
G12_model.py                     — Classe ThresholdClassifier (necessária para carregar o pkl)
employee_data.csv                — Dataset utilizado
G12_relatorio.docx               — Relatório do grupo

Resultados obtidos
------------------

Regressão   — R² no teste : 0.9529  |  RMSE: 999.82
Classificação — F1-Score  : >= 0.52  |  Threshold optimizado (via CV): ~0.7
