[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

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
![Probability Mass Function](https://github.com/brokengrappler/dsp/lessons/statistics/8.3PMF.png)

---
