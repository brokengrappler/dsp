[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Examples and Exercises from Think Stats, 2nd Edition\n",
    "\n",
    "http://thinkstats2.com\n",
    "\n",
    "Copyright 2016 Allen B. Downey\n",
    "\n",
    "MIT License: https://opensource.org/licenses/MIT\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import print_function, division\n",
    "\n",
    "%matplotlib inline\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "import brfss\n",
    "\n",
    "import thinkstats2\n",
    "import thinkplot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The estimation game\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Root mean squared error is one of several ways to summarize the average error of an estimation process."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def RMSE(estimates, actual):\n",
    "    \"\"\"Computes the root mean squared error of a sequence of estimates.\n",
    "\n",
    "    estimate: sequence of numbers\n",
    "    actual: actual value\n",
    "\n",
    "    returns: float RMSE\n",
    "    \"\"\"\n",
    "    e2 = [(estimate-actual)**2 for estimate in estimates]\n",
    "    mse = np.mean(e2)\n",
    "    return np.sqrt(mse)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following function simulates experiments where we try to estimate the mean of a population based on a sample with size `n=7`.  We run `iters=1000` experiments and collect the mean and median of each sample."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Experiment 1\n",
      "rmse xbar 0.38128583555697815\n",
      "rmse median 0.46077337078259245\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def Estimate1(n=7, iters=1000):\n",
    "    \"\"\"Evaluates RMSE of sample mean and median as estimators.\n",
    "\n",
    "    n: sample size\n",
    "    iters: number of iterations\n",
    "    \"\"\"\n",
    "    mu = 0\n",
    "    sigma = 1\n",
    "\n",
    "    means = []\n",
    "    medians = []\n",
    "    for _ in range(iters):\n",
    "        xs = [random.gauss(mu, sigma) for _ in range(n)]\n",
    "        xbar = np.mean(xs)\n",
    "        median = np.median(xs)\n",
    "        means.append(xbar)\n",
    "        medians.append(median)\n",
    "\n",
    "    print('Experiment 1')\n",
    "    print('rmse xbar', RMSE(means, mu))\n",
    "    print('rmse median', RMSE(medians, mu))\n",
    "    \n",
    "Estimate1()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using $\\bar{x}$ to estimate the mean works a little better than using the median; in the long run, it minimizes RMSE.  But using the median is more robust in the presence of outliers or large errors.\n",
    "\n",
    "\n",
    "## Estimating variance\n",
    "\n",
    "The obvious way to estimate the variance of a population is to compute the variance of the sample, $S^2$, but that turns out to be a biased estimator; that is, in the long run, the average error doesn't converge to 0.\n",
    "\n",
    "The following function computes the mean error for a collection of estimates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def MeanError(estimates, actual):\n",
    "    \"\"\"Computes the mean error of a sequence of estimates.\n",
    "\n",
    "    estimate: sequence of numbers\n",
    "    actual: actual value\n",
    "\n",
    "    returns: float mean error\n",
    "    \"\"\"\n",
    "    errors = [estimate-actual for estimate in estimates]\n",
    "    return np.mean(errors)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following function simulates experiments where we try to estimate the variance of a population based on a sample with size `n=7`.  We run `iters=1000` experiments and two estimates for each sample, $S^2$ and $S_{n-1}^2$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean error biased -0.12729700686855783\n",
      "mean error unbiased 0.01815349198668254\n"
     ]
    }
   ],
   "source": [
    "def Estimate2(n=7, iters=1000):\n",
    "    mu = 0\n",
    "    sigma = 1\n",
    "\n",
    "    estimates1 = []\n",
    "    estimates2 = []\n",
    "    for _ in range(iters):\n",
    "        xs = [random.gauss(mu, sigma) for i in range(n)]\n",
    "        biased = np.var(xs)\n",
    "        unbiased = np.var(xs, ddof=1)\n",
    "        estimates1.append(biased)\n",
    "        estimates2.append(unbiased)\n",
    "\n",
    "    print('mean error biased', MeanError(estimates1, sigma**2))\n",
    "    print('mean error unbiased', MeanError(estimates2, sigma**2))\n",
    "    \n",
    "Estimate2()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The mean error for $S^2$ is non-zero, which suggests that it is biased.  The mean error for $S_{n-1}^2$ is close to zero, and gets even smaller if we increase `iters`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The sampling distribution\n",
    "\n",
    "The following function simulates experiments where we estimate the mean of a population using $\\bar{x}$, and returns a list of estimates, one from each experiment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def SimulateSample(mu=90, sigma=7.5, n=9, iters=1000):\n",
    "    xbars = []\n",
    "    for j in range(iters):\n",
    "        xs = np.random.normal(mu, sigma, n)\n",
    "        xbar = np.mean(xs)\n",
    "        xbars.append(xbar)\n",
    "    return xbars\n",
    "\n",
    "xbars = SimulateSample()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here's the \"sampling distribution of the mean\" which shows how much we should expect $\\bar{x}$ to vary from one experiment to the next."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cdf = thinkstats2.Cdf(xbars)\n",
    "thinkplot.Cdf(cdf)\n",
    "thinkplot.Config(xlabel='Sample mean',\n",
    "                 ylabel='CDF')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The mean of the sample means is close to the actual value of $\\mu$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "90.01930955866159"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(xbars)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An interval that contains 90% of the values in the sampling disrtribution is called a 90% confidence interval."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(85.83081614723771, 94.1915010908011)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ci = cdf.Percentile(5), cdf.Percentile(95)\n",
    "ci"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And the RMSE of the sample means is called the standard error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.5544052063563902"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stderr = RMSE(xbars, 90)\n",
    "stderr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Confidence intervals and standard errors quantify the variability in the estimate due to random sampling."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Estimating rates\n",
    "\n",
    "The following function simulates experiments where we try to estimate the mean of an exponential distribution using the mean and median of a sample. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rmse L 1.1024518934895993\n",
      "rmse Lm 1.8522731565170116\n",
      "mean error L 0.34159943661654163\n",
      "mean error Lm 0.4431986076148987\n"
     ]
    }
   ],
   "source": [
    "def Estimate3(n=7, iters=1000):\n",
    "    lam = 2\n",
    "\n",
    "    means = []\n",
    "    medians = []\n",
    "    for _ in range(iters):\n",
    "        xs = np.random.exponential(1.0/lam, n)\n",
    "        L = 1 / np.mean(xs)\n",
    "        Lm = np.log(2) / thinkstats2.Median(xs)\n",
    "        means.append(L)\n",
    "        medians.append(Lm)\n",
    "\n",
    "    print('rmse L', RMSE(means, lam))\n",
    "    print('rmse Lm', RMSE(medians, lam))\n",
    "    print('mean error L', MeanError(means, lam))\n",
    "    print('mean error Lm', MeanError(medians, lam))\n",
    "    \n",
    "Estimate3()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The RMSE is smaller for the sample mean than for the sample median.\n",
    "\n",
    "But neither estimator is unbiased."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise:**  In this chapter we used $\\bar{x}$ and median to estimate µ, and found that $\\bar{x}$ yields lower MSE. Also, we used $S^2$ and $S_{n-1}^2$ to estimate σ, and found that $S^2$ is biased and $S_{n-1}^2$ unbiased.\n",
    "Run similar experiments to see if $\\bar{x}$ and median are biased estimates of µ. Also check whether $S^2$ or $S_{n-1}^2$ yields a lower MSE."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Solution goes here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Solution goes here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Solution goes here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise:** Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.\n",
    "\n",
    "Repeat the experiment with a few different values of `n` and make a plot of standard error versus `n`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7fa9a3ea37d0>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "m = 1000\n",
    "n = 10\n",
    "lam = 2\n",
    "\n",
    "# mean = 1/L, therefore L = 1/mean\n",
    "# median = ln(2) / m\n",
    "# xs = np.random.exponential\n",
    "\n",
    "means = []\n",
    "medians = []\n",
    "\n",
    "for _ in range(m):\n",
    "    xs = np.random.exponential(1/lam, n)\n",
    "    L = 1 / np.mean(xs)\n",
    "    Lm = math.log(2) / np.median(xs)\n",
    "    means.append(L)\n",
    "    medians.append(Lm)\n",
    "\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "sns.distplot(means)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8384459508537216\n",
      "0.6208791367354802 3.3791208632645198\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from scipy.stats import norm\n",
    "\n",
    "#standard error and CI of 90%\n",
    "MSE = [(estimate-lam)**2 for estimate in means]\n",
    "RSM = math.sqrt(np.mean(MSE))\n",
    "print(RSM)\n",
    "\n",
    "x = np.sort(means)\n",
    "y = np.arange(1, len(x)+1) / len(x)\n",
    "plt.plot(x,y)\n",
    "plt.xlabel('Means')\n",
    "plt.ylabel('CDF')\n",
    "\n",
    "#z-score of 90% is 1.645. you can use norm.ppf from scipy.stats to get the z-score.\n",
    "zscore = norm.ppf(.95)\n",
    "lowCI = lam - RSM*zscore\n",
    "upCI = lam + RSM*zscore\n",
    "print(lowCI,upCI)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise:** In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.\n",
    "\n",
    "Write a function that takes a goal-scoring rate, `lam`, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.\n",
    "\n",
    "Write another function that simulates many games, stores the estimates of `lam`, then computes their mean error and RMSE.\n",
    "\n",
    "Is this way of making an estimate biased?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def SimulateGame(lam):\n",
    "    \"\"\"Simulates a game and returns the estimated goal-scoring rate.\n",
    "\n",
    "    lam: actual goal scoring rate in goals per game\n",
    "    \"\"\"\n",
    "    goals = 0\n",
    "    t = 0\n",
    "    while True:\n",
    "        time_between_goals = random.expovariate(lam)\n",
    "        t += time_between_goals\n",
    "        if t > 1:\n",
    "            break\n",
    "        goals += 1\n",
    "\n",
    "    # estimated goal-scoring rate is the actual number of goals scored\n",
    "    L = goals\n",
    "    return L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "def multiple_games(m=1000, lam=2):\n",
    "    est_goals = []\n",
    "    \n",
    "    for _ in range(m):\n",
    "        goals = SimulateGame(lam)\n",
    "        est_goals.append(goals)\n",
    "        \n",
    "    e2 = [(estimate - lam)**2 for estimate in est_goals]\n",
    "    RSME = math.sqrt(np.mean(e2))\n",
    "    errors = [(estimate - lam) for estimate in est_goals]\n",
    "    mean_err = np.mean(errors)\n",
    "    print('Mean Error is: ' + str(mean_err))\n",
    "    print('Root Square ME is: ' + str(RSME))\n",
    "    return est_goals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Error is: -0.009\n",
      "Root Square ME is: 1.3809417076763233\n"
     ]
    }
   ],
   "source": [
    "est_goals = multiple_games()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "goals_df = pd.DataFrame(est_goals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "goal_counts = pd.DataFrame(goals_df[0].value_counts(), index=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "goal_counts.reset_index(level=0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "goal_counts.columns = ['goals','counts']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "goal_counts['prob'] = goal_counts['counts']/goal_counts['counts'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>goals</th>\n",
       "      <th>counts</th>\n",
       "      <th>prob</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>108</td>\n",
       "      <td>0.108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>320</td>\n",
       "      <td>0.320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>262</td>\n",
       "      <td>0.262</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>163</td>\n",
       "      <td>0.163</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>97</td>\n",
       "      <td>0.097</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>34</td>\n",
       "      <td>0.034</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>14</td>\n",
       "      <td>0.014</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0.001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>0.001</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   goals  counts   prob\n",
       "3      0     108  0.108\n",
       "0      1     320  0.320\n",
       "1      2     262  0.262\n",
       "2      3     163  0.163\n",
       "4      4      97  0.097\n",
       "5      5      34  0.034\n",
       "6      6      14  0.014\n",
       "8      7       1  0.001\n",
       "7      9       1  0.001"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "goal_counts.sort_values(by='goals',inplace=True)\n",
    "goal_counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 9 artists>"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = goal_counts['goals']\n",
    "y = goal_counts['prob']\n",
    "plt.bar(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

---
Code for simulating the games and printing the mean error and RSME.
```python
def multiple_games(m=1000, lam=2):
    est_goals = []
    
    for _ in range(m):
        goals = SimulateGame(lam)
        est_goals.append(goals)
        
    e2 = [(estimate - lam)**2 for estimate in est_goals]
    RSME = math.sqrt(np.mean(e2))
    errors = [(estimate - lam) for estimate in est_goals]
    mean_err = np.mean(errors)
    print('Mean Error is: ' + str(mean_err))
    print('Root Square ME is: ' + str(RSME))
    return est_goals
```

Run the simulation
```python
est_goals = multiple_games()
```

My results in Jupyter were: 
Mean Error is: -0.009
Root Square ME is: 1.3809417076763233

I graphed the PMF using the following code:

```python
import pandas as pd
goals_df = pd.DataFrame(est_goals)
goal_counts = pd.DataFrame(goals_df[0].value_counts(), index=None)
goal_counts.reset_index(level=0, inplace=True)
goal_counts.columns = ['goals','counts']
goal_counts['prob'] = goal_counts['counts']/goal_counts['counts'].sum()

goal_counts.sort_values(by='goals',inplace=True)

x = goal_counts['goals']
y = goal_counts['prob']
plt.bar(x,y)
```


---
