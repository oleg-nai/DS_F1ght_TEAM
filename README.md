# DS_F1ght_TEAM

Updates 06.11:
At the moment we are at the research stage for the best approches for recsys (chech clusterization folder), so we do not provide train-test splits. 
For the DE part, we worked on adding FastApi (before that and at the moment we have a telegram bot)
All gelstalts that we did not close for the 3rd sprint we will close by 16.11.


Updates 19.11:
1. Topic modeling presented.
    * Research path was long and thorny but we found the best way of choosing the best topic for any paper. 
    * Research located in topic_modeling folder and here: https://www.kaggle.com/code/olegnai/topic-modeling
    * Main approach is: 
        1. Take articles
        2. Filter them(by title, n_citation >= 25, lang=='en', ... )
        2. Process/clean titles from stopwords, html tabs, ...
        3. Create emdedding with `distilbert-base-nli-mean-tokens` transformer
        4. Save emdedding
        5. Use `UMAP` for generating low dim (for next step)
        5. Clusterise received values from emdedding with `KMEANS` alg -> get 30 clusters
        6. Go though 30 clusters, take top 5 words from each cluster and create mapping for each topic (create real articles)
        7. Create 10 multiclasstes basing on 30 prev clusters (for API and back-end)
        8. Create Train/Test dataset: features - emdedding from 4th step, target - clusterized value.
        9. Create basic model, save it and save metrics, provide model and transformer alg. to back-end team

2. Research reqsys topic (in progress)
    * https://docs.google.com/document/d/1ZVEmShjWnnpT0xg1RIIHsEsNuUdaBXIX7GXZyEecrNA/edit?usp=sharing



Presentation_sptint_1: https://docs.google.com/presentation/d/1XF_roi04KlJn944wHrQipxE4XbZ-tBvIlCMZ4bMPT4k/edit?usp=sharing

Feature investigation: https://docs.google.com/spreadsheets/d/1Kozi-46nwjQniTNHKUy4KZZGlSVF5Lf_F73CJp_qaZ8/edit#gid=0
