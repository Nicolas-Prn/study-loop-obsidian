### Supervised Classification

**Supervised Classification** is the most common machine learning task. It consists of learning a prediction function from **labelled** examples.

#### Principle

Unlike unsupervised learning, where the algorithm is left to its own devices when facing the data, here the algorithm has a "teacher" (the supervisor) who provides it with the correct answers for a set of training examples.

- **Data:** We use a [[Dataset | dataset]] $D_n$ made of pairs $(x_i, y_i)$ (see [[Data in Supervised Classification (Formalism)]]).
    
- **Goal:** Find the function $\hat{f}$ that correctly maps an input $x$ to its class $y$ (see [[Function Approximation (Machine Learning)]]).
    

#### Types of Classification

Depending on the nature of the output $y$ (the set $\mathcal{Y}$), we distinguish:

1. **Binary Classification:**
    
    - There are only **2 possible classes**.
        
    - $\mathcal{Y} = \{0, 1\}$ or $\{-1, +1\}$.
        
    - _Example:_ The Salmon vs Sea Bass case (see chart on slide 7) or spam detection (Yes/No).
        
2. **Multi-class Classification:**
    
    - There are **more than 2 classes** ($K$ classes).
        
    - $\mathcal{Y} = \{c_1, c_2, ..., c_K\}$.
        
    - _Example:_ Handwritten digit recognition (0 to 9), see slide 16.
        

#### Difference from Regression

The fundamental difference lies in the nature of the output variable $y$:

- **Classification:** $y$ is a **discrete** label (a category, a class).
    
- **Regression:** $y$ is a **continuous** value (a real number).
    

> [!note] Visual illustration
> 
> See the chart on slide 19, which visually compares the discrete output (Classification) and the continuous output (Regression).
> ![[Pasted image 20251221133447.png]]

#### Concrete example:
- [[Handwritten Digit Recognition Example]]

---
Second example note:
---
### The Reasoning Behind the Naive Bayes Classifier

In the context of [[Resources/Supervised Classification|Supervised Classification]], and more specifically of the [[Resources/Probabilistic Formalism (Machine Learning)|Probabilistic Formalism]], our goal is to estimate the probability that an observed data point $X$ belongs to a class $Y_k$.

Let a feature vector be $X = \{X_1, X_2, ..., X_p\}$ (see [[Resources/Data in Supervised Classification (Formalism)|Data in Supervised Classification]]). We seek to compute the **a posteriori** probability:

$$\mathbb{P}(Y_k | X)$$

#### 1. The Wall of Reality (Direct estimation problem)

If we tried to compute $\mathbb{P}(Y_k | X)$ directly through simple statistics on the [[Resources/Dataset|Dataset]], we would run into the **[[Resources/Curse of Dimensionality|Curse of Dimensionality]]**.

- To estimate this probability without bias, we would need to have observed the **exact combination** of all attributes simultaneously in the training set.
    
- Since the volume of the space of possibilities explodes exponentially with the number of attributes $p$, most combinations do not exist in the data (sparse data). The statistical computation is impossible (division by zero or unrepresentative sample). *In short, we do not have enough information to compute a statistic on $\mathbb{P}(Y_k | X)$.*
    

#### 2. Inverting the problem (Bayes' Theorem)

To get around this lack of data, we use the fundamental rule of the [[Resources/Bayes Classifier (Machine Learning)|Bayes Classifier]] to "flip" the conditional problem: 
>[!note] Note
>This is a first step; what interests us is what it will then allow us to do! See paragraph: [[The Reasoning Behind the Naive Bayes Classifier#3. The "Naive" Solution (Conditional Independence)|the naive solution]]

$$\underbrace{\mathbb{P}(Y=y|X=x)}_{\text{Posterior}} = \frac{\overbrace{\mathbb{P}(X=x|Y=y)}^{\text{Likelihood}} \times \overbrace{\mathbb{P}(Y=y)}^{\text{Prior}}}{\underbrace{\mathbb{P}(X=x)}_{\text{Evidence}}}$$

- **The benefit:** It is statistically more stable to model the distribution of the attributes for a given class (the _Likelihood_) than the reverse.
    
- **The remaining problem:** The likelihood term $\mathbb{P}(X=x|Y=y)$ is still a complex joint probability $\mathbb{P}(X_1, ..., X_p | Y_k)$ that still requires observing the complete combination.
    

#### 3. The "Naive" Solution (Conditional Independence)

This is where ==the major simplifying assumption== comes in. We **naively** assume that all attributes are **independent of one another conditionally on the class**.

This makes it possible to factorise the joint probability into a product of marginal probabilities (see [[Resources/Concept of Probability|Concept of Probability]]):

$$\mathbb{P}(X|Y_k) \approx \prod_{j=1}^{p} \mathbb{P}(X_{j}|Y_k)$$

**Impact on the [[Resources/Bias-Variance Tradeoff|Bias-Variance Tradeoff]]:**

- **Increased Bias:** The independence assumption is often false in reality (e.g. correlations between attributes), which moves the model away from the [[Resources/True Function vs Learned Model (f vs f_hat)|True Function]].
    
- **Drastic reduction in Variance:** Since each parameter $\mathbb{P}(X_{j}|Y_k)$ is estimated separately, the estimate is very stable even with little data. This makes the model highly resistant to [[Resources/Overfitting|Overfitting]].
    

#### 4. The Final Decision Rule (MAP)

To classify a new data point $X_i$, we look for the class $Y_k$ that maximises the a posteriori probability. Since the evidence term $\mathbb{P}(X_i)$ is constant for all classes, we ignore it.

The decision rule (Maximum A Posteriori) becomes:

$$y(X_i) = \arg \max_{k} \left( \mathbb{P}(Y_k) \times \prod_{j=1}^{p} \mathbb{P}(X_{ij}|Y_k) \right)$$

The performance of this classifier can then be evaluated using the [[Resources/Confusion Matrix (Machine Learning)|Confusion Matrix]] or the [[Resources/Accuracy and Error Rate (Machine Learning)|Error Rate]].
***
>[!tip] What's next?
>Now we need to decide how to estimate our famous $\mathbb{P}(X_{ij}|Y_k)$...
>For that, see: [[Estimation Methods for Naive Bayes (Attribute Types)]].
