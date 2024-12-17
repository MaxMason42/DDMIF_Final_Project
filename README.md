# Trading with the Momentum Transformer
## About
This code is from the paper [Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture](https://arxiv.org/pdf/2112.08534.pdf) and additionally provides an implementation for the paper [Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and Changepoint Detection](https://arxiv.org/pdf/2105.13727.pdf). 

## Using the code
1. Create a WRDS account.
2. Download the WRDS data with: `python -m data.download_wrds_data` and input your username and password when prompted
3. Create Momentum Transformer input features with: `python -m examples.create_features_wrds`. In this example we use the top 5 stocks from each sector as of 2017.
4. Run one of the Momentum Transformer or Slow Momentum with Fast Reversion experiments with `python -m examples.run_dmn_experiment <<EXPERIMENT_NAME>>`
5. 

## Results 
The results from all the tests done in the paper Enhanced Momentum with Momentum Transformers can be found in the results folder.

## References
```bib
@article{wood2021trading,
  title={Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture},
  author={Wood, Kieran and Giegerich, Sven and Roberts, Stephen and Zohren, Stefan},
  journal={arXiv preprint arXiv:2112.08534},
  year={2021}
}

@article {Wood111,
	author = {Wood, Kieran and Roberts, Stephen and Zohren, Stefan},
	title = {Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and Changepoint Detection},
	volume = {4},
	number = {1},
	pages = {111--129},
	year = {2022},
	doi = {10.3905/jfds.2021.1.081},
	publisher = {Institutional Investor Journals Umbrella},
	issn = {2640-3943},
	URL = {https://jfds.pm-research.com/content/4/1/111},
	eprint = {https://jfds.pm-research.com/content/4/1/111.full.pdf},
	journal = {The Journal of Financial Data Science}
}
```
