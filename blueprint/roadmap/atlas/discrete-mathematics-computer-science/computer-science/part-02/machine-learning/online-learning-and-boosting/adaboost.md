---
declaration: section
origin: cited
lean: Cslib.MachineLearning.AdaBoost.err, Cslib.MachineLearning.AdaBoost.alpha, Cslib.MachineLearning.AdaBoost.normalizer, Cslib.MachineLearning.AdaBoost.reweight, Cslib.MachineLearning.AdaBoost.normalizer_eq, Cslib.MachineLearning.AdaBoost.two_mul_sqrt_le_exp, Cslib.MachineLearning.AdaBoost.dist, Cslib.MachineLearning.AdaBoost.hyp
statement: formalized
proof: formalized
---

# AdaBoost

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html).

## Weighted training error

For labels $y$, weights $D$ and predictions $h$ on $m$ training
points, the weighted training error of $h$ under $D$ is $\sum_{i : h(i) \ne y(i)} D(i)$, the total
weight of the points that $h$ misclassifies.

Formalized by `Cslib.MachineLearning.AdaBoost.err`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#err).

## AdaBoost's hypothesis weight

A weak hypothesis with weighted error
$\varepsilon \in \mathbb{R}$ gets the weight
$\alpha(\varepsilon) = \frac{1}{2} \log \frac{1 - \varepsilon}{\varepsilon}$.

Formalized by `Cslib.MachineLearning.AdaBoost.alpha`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#alpha).

## Normalizer of a boosting round

For labels $y$, weights $D$ and predictions $h$ on $m$
training points, let $\varepsilon$ be the weighted training error of $h$ under $D$ and
$\alpha = \alpha(\varepsilon)$ the hypothesis weight. The normalizer of the round is

$$Z = \sum_i D(i) \exp(-\alpha\, y_i h_i),$$

where the label $y_i$ and the prediction $h_i$ are read as $\pm 1$.

Formalized by `Cslib.MachineLearning.AdaBoost.normalizer`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#normalizer).

## AdaBoost reweighting

For labels $y$, weights $D$ and predictions $h$ on $m$ training
points, let $\varepsilon$ be the weighted training error of $h$ under $D$,
$\alpha = \alpha(\varepsilon)$ the hypothesis weight and $Z$ the normalizer of the round. The
reweighted weight of point $i$ is

$$D'(i) = \frac{D(i) \exp(-\alpha\, y_i h_i)}{Z},$$

where the label $y_i$ and the prediction $h_i$ are read as $\pm 1$.

Formalized by `Cslib.MachineLearning.AdaBoost.reweight`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#reweight).

## The normalizer of a round is $2\sqrt{\varepsilon(1 - \varepsilon)}$

Let $y$ be labels on
$m$ training points, $D$ real weights on the points with $\sum_i D(i) = 1$, and $h$ predictions
whose weighted training error $\varepsilon$ under $D$ satisfies $0 < \varepsilon < 1$. Then the
normalizer of the round with weights $D$ and hypothesis $h$ equals
$2\sqrt{\varepsilon(1 - \varepsilon)}$.

Formalized by `Cslib.MachineLearning.AdaBoost.normalizer_eq`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#normalizer-eq).

## One round's factor is at most `exp (-2 γ²)`

For real numbers $\varepsilon$ and $\gamma$
with $\gamma \ge 0$ and $\varepsilon \le 1/2 - \gamma$, we have
$2\sqrt{\varepsilon (1 - \varepsilon)} \le e^{-2\gamma^2}$, where the square root of a negative
number is taken to be $0$.

Formalized by `Cslib.MachineLearning.AdaBoost.two_mul_sqrt_le_exp`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#two-mul-sqrt-le-exp).

## AdaBoost's weights

Given labels $y$ on $m$ training points and a weak learner
$\mathrm{wl}$, which maps weights on the points to a hypothesis's predictions on them,
AdaBoost's weights $D_t$ on the points are defined by $D_0(i) = 1/m$ for every point $i$, and
$D_{t+1}$ is the reweighting of $D_t$ by the hypothesis $\mathrm{wl}(D_t)$.

Formalized by `Cslib.MachineLearning.AdaBoost.dist`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#dist).

## Weak hypothesis of an AdaBoost round

The weak hypothesis $h_t$ of round $t$ is the weak
learner's output $\mathrm{wl}(D_t)$ on the weights $D_t$ of round $t$.

Formalized by `Cslib.MachineLearning.AdaBoost.hyp`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#hyp).

## Weighted error of an AdaBoost round

The weighted error $\varepsilon_t$ of round $t$ is the
weighted training error of the weak hypothesis $h_t$ of round $t$ under the weights $D_t$ of
round $t$.

Formalized by `Cslib.MachineLearning.AdaBoost.eps`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#eps).

## Normalizer of an AdaBoost round

Run AdaBoost on training points with labels $y$, and
read labels and predictions as $\pm 1$. The normalizer of round $t$ is
$Z_t = \sum_i D_t(i) \exp(-\alpha_t y_i h_t(i))$, where $D_t$ are AdaBoost's weights in round
$t$, $h_t$ is the weak hypothesis of round $t$, and $\alpha_t$ is its weight.

Formalized by `Cslib.MachineLearning.AdaBoost.zee`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#zee).

## AdaBoost's combined score

After $T$ rounds, the combined score of training point $i$ is

$$F_T(i) = \sum_{t < T} \alpha(\varepsilon_t)\, h_t(i),$$

where $\varepsilon_t$ is the weighted error and $h_t$ the weak hypothesis of round $t$,
$\alpha(\varepsilon) = \frac{1}{2} \log \frac{1 - \varepsilon}{\varepsilon}$ is the hypothesis
weight, and the prediction $h_t(i)$ is read as $\pm 1$. The final classifier is the sign of
$F_T$.

Formalized by `Cslib.MachineLearning.AdaBoost.score`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#score).

## Training error of AdaBoost

Let AdaBoost run on $m$ training points with labels $y$,
read labels and predictions as $\pm 1$, and let $F_T$ be the combined score after $T$ rounds.
The training error after $T$ rounds is the number of training points $i$ with
$y_i F_T(i) \le 0$, divided by $m$; in particular a zero score counts as an error.

Formalized by `Cslib.MachineLearning.AdaBoost.trainErr`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#train-err).

## Unrolling the weights

Run AdaBoost with labels $y$ on $m > 0$ training points and a
weak learner, and let $D_T$ be the weights on the points after $T$ rounds, $Z_t$ the normalizer
of round $t$, and $F_T$ the combined score after $T$ rounds. Then for every $T \in \mathbb{N}$ and
every training point $i$,

$$D_T(i) \cdot m \prod_{t < T} Z_t = \exp(-y_i F_T(i)),$$

where the label $y_i$ is read as $\pm 1$.

Formalized by `Cslib.MachineLearning.AdaBoost.dist_mul_prod`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#dist-mul-prod).

## The training error is at most the product of the normalizers

Let AdaBoost run on
$m > 0$ training points with labels $y$ and an arbitrary weak learner, and write $Z_t$ for the
normalizer of round $t$. Then for every number of rounds $T$, the training error after $T$ rounds
is at most $\prod_{t < T} Z_t$.

Formalized by `Cslib.MachineLearning.AdaBoost.trainErr_le_prod`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#train-err-le-prod).

## The weak-learning assumption

A weak learner, which maps weights on the $m$ training
points with labels $y$ to a hypothesis on those points, has edge $\gamma$ if for every weighting
$D$ of the training points with $D_i > 0$ for all $i$ and $\sum_i D_i = 1$, the hypothesis it
returns on $D$ has weighted error under $D$ in the interval $(0, 1/2 - \gamma]$.

Formalized by `Cslib.MachineLearning.AdaBoost.WeakLearner`, a definition declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#weak-learner).

## The Freund–Schapire bound on AdaBoost's training error

Let AdaBoost run on $m > 0$
training points with labels $y$ and a weak learner with edge $\gamma \ge 0$, that is, one that on
every weighting $D$ of the training points with $D_i > 0$ for all $i$ and $\sum_i D_i = 1$ returns
a hypothesis whose weighted error under $D$ lies in $(0, 1/2 - \gamma]$. Write $\varepsilon_t$ for
the weighted error of the weak hypothesis of round $t$ under AdaBoost's weights of that round.
Then for every number of rounds $T$, the training error after $T$ rounds is at most
$\prod_{t < T} 2\sqrt{\varepsilon_t (1 - \varepsilon_t)}$.

Formalized by `Cslib.MachineLearning.AdaBoost.trainErr_le_prod_sqrt`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#train-err-le-prod-sqrt).

## AdaBoost drives the training error down exponentially

Let AdaBoost run on $m > 0$
training points with labels $y$ and a weak learner with edge $\gamma \ge 0$, that is, one that on
every weighting $D$ of the training points with $D_i > 0$ for all $i$ and $\sum_i D_i = 1$ returns
a hypothesis whose weighted error under $D$ lies in $(0, 1/2 - \gamma]$. Then for every number of
rounds $T$, the training error after $T$ rounds is at most $e^{-2\gamma^2 T}$.

Formalized by `Cslib.MachineLearning.AdaBoost.trainErr_le_exp`, a theorem declared in [CSLibExt/MachineLearning/AdaBoost.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/AdaBoost.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html#train-err-le-exp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: AdaBoost](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/adaboost)
