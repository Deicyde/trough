---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Hedge.update, Cslib.MachineLearning.Hedge.weights, Cslib.MachineLearning.Hedge.total, Cslib.MachineLearning.Hedge.roundLoss, Cslib.MachineLearning.Hedge.algLoss, Cslib.MachineLearning.Hedge.expertLoss, Cslib.MachineLearning.Hedge.exp_neg_mul_le, Cslib.MachineLearning.Hedge.total_update_le
statement: formalized
proof: formalized
---

# Hedge algorithm

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html).

## Hedge weight update

After a round with losses `ℓ`, each expert's weight is multiplied by `exp (-η ℓ i)`.

Formalized by `Cslib.MachineLearning.Hedge.update`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#update).

## Hedge weights after a sequence of rounds

Let $\eta \in \mathbb{R}$ be a learning rate,
let $w \in \mathbb{R}^n$ be initial weights on $n$ experts, and let $\ell_1, \dots, \ell_T \in
\mathbb{R}^n$ be the loss vectors of $T$ rounds, given as a list. The weights after these rounds
are obtained from $w$ by applying the Hedge update once per round, in the order of the list:
round $t$ multiplies the weight of each expert $i$ by $e^{-\eta \ell_t(i)}$. For the empty list
of rounds the weights are $w$.

Formalized by `Cslib.MachineLearning.Hedge.weights`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#weights).

## Total weight of the Hedge experts

The total weight of weights $w$ on $n$ experts is
$\sum_i w_i$.

Formalized by `Cslib.MachineLearning.Hedge.total`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#total).

## Loss of a Hedge round

For weights $w$ and losses $\ell$ on $n$ experts, the algorithm's
loss in the round is $\left(\sum_i w_i \ell_i\right) / W$, where $W = \sum_i w_i$ is the total
weight. This is its expected loss when it follows expert $i$ with probability $w_i / W$.

Formalized by `Cslib.MachineLearning.Hedge.roundLoss`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#round-loss).

## Loss of the Hedge algorithm

Let $\eta$ be a learning rate, $w \in \mathbb{R}^n$ initial
weights on $n$ experts and $\ell_1, \dots, \ell_T \in \mathbb{R}^n$ the losses of $T$ rounds. Set
$w_1 = w$ and $w_{t+1}(j) = w_t(j) e^{-\eta \ell_t(j)}$. The algorithm's total loss is
$\sum_{t=1}^T \bigl(\sum_j w_t(j) \ell_t(j)\bigr) / \sum_j w_t(j)$, the sum over the rounds of
the weighted average of that round's losses; a round whose total weight is $0$ contributes
$0$.

Formalized by `Cslib.MachineLearning.Hedge.algLoss`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-loss).

## Total loss of an expert

For an expert $i$ among $n$ experts and a finite sequence of loss
vectors $\ell_1, \dots, \ell_T \in \mathbb{R}^n$, the total loss of expert $i$ is
$\sum_{t=1}^T \ell_t(i)$.

Formalized by `Cslib.MachineLearning.Hedge.expertLoss`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#expert-loss).

## The exponential lies below its chord on the unit interval

For every real $\eta$ and
every $x \in [0, 1]$, $e^{-\eta x} \le 1 - (1 - e^{-\eta}) x$.

Formalized by `Cslib.MachineLearning.Hedge.exp_neg_mul_le`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#exp-neg-mul-le).

## A round costs weight in proportion to the algorithm's loss

Let $n > 0$, let $w$ be
positive weights on $n$ experts, let $\ell$ be losses with $0 \le \ell_i \le 1$ for every $i$, and
let $\eta$ be a real number. Let $w'$ be the Hedge update of $w$ with learning rate $\eta$, so that
$w'_i = w_i e^{-\eta \ell_i}$, and let $W$ and $W'$ be the total weights of $w$ and $w'$. Then
$W' \le W \exp(-(1 - e^{-\eta}) L)$, where $L$ is the round's loss under the weights $w$.

Formalized by `Cslib.MachineLearning.Hedge.total_update_le`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#total-update-le).

## Losses in the unit interval

A finite sequence of loss vectors
$\ell_1, \dots, \ell_T \in \mathbb{R}^n$ on $n$ experts has losses in $[0, 1]$ when
$0 \le \ell_t(i) \le 1$ for every round $t$ and every expert $i$.

Formalized by `Cslib.MachineLearning.Hedge.Bounded`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#bounded).

## Weight decay over a Hedge run

Let $n > 0$ and let $\eta$ be a real number. For every
sequence of rounds with losses in $[0, 1]$ and all positive initial weights $w$ on $n$ experts,
the total weight after running Hedge with learning rate $\eta$ from $w$ is at most
$W \exp(-(1 - e^{-\eta}) L)$, where $W$ is the total weight of $w$ and $L$ is the algorithm's
total loss over the rounds for the run from $w$ with learning rate $\eta$.

Formalized by `Cslib.MachineLearning.Hedge.total_weights_le`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#total-weights-le).

## Closed form of the Hedge weights

For every learning rate $\eta$, sequence of rounds,
initial weights $w$ and expert $i$, the weight of expert $i$ after running Hedge on the rounds from
$w$ is $w_i e^{-\eta L_i}$, where $L_i$ is expert $i$'s total loss over the rounds.

Formalized by `Cslib.MachineLearning.Hedge.weights_apply`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#weights-apply).

## The Hedge loss bound

Let $\eta$ be a real number, and let $\ell_1, \dots, \ell_T$ be loss
vectors in $[0, 1]^n$ for $n$ experts. Run Hedge with learning rate $\eta$ from unit weights, that
is $w_1(j) = 1$ and $w_{t+1}(j) = w_t(j) e^{-\eta \ell_t(j)}$, and let
$x_t(j) = w_t(j) / \sum_k w_t(k)$ be the distribution played in round $t$. Then for every
expert $i$,

$$(1 - e^{-\eta}) \sum_{t=1}^T \sum_j x_t(j) \ell_t(j) \le \eta \sum_{t=1}^T \ell_t(i) + \log n.$$

For $\eta > 0$, writing $L$ for the algorithm's loss and $L_i$ for expert $i$'s loss, this is
the bound $L \le (\log n + \eta L_i) / (1 - e^{-\eta})$ of Freund and Schapire (after
Littlestone and Warmuth).

Formalized by `Cslib.MachineLearning.Hedge.algLoss_le`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-loss-le).

## Weighted second moment of a Hedge round

For weights $w$ and losses $\ell$ on $n$
experts, the round's weighted second moment is $\left(\sum_i w_i \ell_i^2\right) / W$, where
$W = \sum_i w_i$ is the total weight; that is, $\sum_i x_i \ell_i^2$ for the played distribution
$x = w / W$.

Formalized by `Cslib.MachineLearning.Hedge.roundSq`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#round-sq).

## Summed second moments of the Hedge losses

Let $\eta$ be a learning rate,
$w \in \mathbb{R}^n$ initial weights on $n$ experts and $\ell_1, \dots, \ell_T \in \mathbb{R}^n$
the losses of $T$ rounds. Set $w_1 = w$ and $w_{t+1}(j) = w_t(j) e^{-\eta \ell_t(j)}$. The summed
second moment is $\sum_{t=1}^T \bigl(\sum_j w_t(j) \ell_t(j)^2\bigr) / \sum_j w_t(j)$, the sum over
the rounds of the weighted second moment of that round's losses; a round whose total weight is
$0$ contributes $0$.

Formalized by `Cslib.MachineLearning.Hedge.algSq`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-sq).

## Nonnegative losses

A finite sequence of loss vectors
$\ell_1, \dots, \ell_T \in \mathbb{R}^n$ on $n$ experts has nonnegative losses when
$\ell_t(i) \ge 0$ for every round $t$ and every expert $i$.

Formalized by `Cslib.MachineLearning.Hedge.Nonneg`, a definition declared in [CSLibExt/MachineLearning/Hedge.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#nonneg).

## A round costs weight in proportion to the algorithm's loss, up to a second-order term

Let $n > 0$, let $w$ be positive weights on $n$ experts, let $\ell$ be nonnegative losses, and let
$\eta \ge 0$. Let $w'$ be the Hedge update of $w$ with learning rate $\eta$, so that
$w'_i = w_i e^{-\eta \ell_i}$, and let $W$ and $W'$ be the total weights of $w$ and $w'$. Then
$W' \le W \exp(-\eta L + \eta^2 Q)$, where $L$ is the round's loss and $Q$ its weighted second
moment under the weights $w$.

Formalized by `Cslib.MachineLearning.Hedge.total_update_le_sq`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#total-update-le-sq).

## Weight decay over a Hedge run, second-order form

Let $n > 0$ and $\eta \ge 0$. For every
sequence of rounds with nonnegative losses and all positive initial weights $w$ on $n$ experts,
the total weight after running Hedge with learning rate $\eta$ from $w$ is at most
$W \exp(-\eta L + \eta^2 Q)$. Here $W$ is the total weight of $w$, $L$ is the algorithm's total
loss over the rounds and $Q$ is the sum of the rounds' weighted second moments, both for the run
from $w$ with learning rate $\eta$.

Formalized by `Cslib.MachineLearning.Hedge.total_weights_le_sq`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#total-weights-le-sq).

## The second-order Hedge bound

Let $\eta > 0$, and let $\ell_1, \dots, \ell_T$ be loss
vectors in $\mathbb{R}^n$ for $n$ experts with $\ell_t(j) \ge 0$ for all $t$ and $j$. Run Hedge
with learning rate $\eta$ from unit weights, that is $w_1(j) = 1$ and
$w_{t+1}(j) = w_t(j) e^{-\eta \ell_t(j)}$, and let $x_t(j) = w_t(j) / \sum_k w_t(k)$ be the
distribution played in round $t$. Then for every expert $i$,

$$\sum_{t=1}^T \sum_j x_t(j) \ell_t(j) \le \sum_{t=1}^T \ell_t(i) +
\eta \sum_{t=1}^T \sum_j x_t(j) \ell_t(j)^2 + \frac{\log n}{\eta}.$$

This is Theorem 1.3 of Hazan, *Introduction to Online Convex Optimization*. Unlike the
first-order Hedge loss bound, the losses need not be at most $1$.

Formalized by `Cslib.MachineLearning.Hedge.algLoss_le_sq`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-loss-le-sq).

## A Hedge run splits at any round

For every learning rate $\eta$, sequences of rounds
$\lambda$ and $\lambda'$, and initial weights $w$, the weights after running Hedge on the rounds of
$\lambda$ followed by those of $\lambda'$, starting from $w$, equal the weights after running it on
$\lambda'$ starting from the weights reached after $\lambda$ from $w$.

Formalized by `Cslib.MachineLearning.Hedge.weights_append`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#weights-append).

## The Hedge loss splits at any round

Fix a learning rate $\eta$ and $n$ experts. For a
finite sequence $\sigma$ of loss vectors in $\mathbb{R}^n$ and weights $w \in \mathbb{R}^n$, write
$L(\sigma, w)$ for the algorithm's total loss over $\sigma$ started from $w$, and $W(\sigma, w)$
for the weights after the rounds of $\sigma$ started from $w$. Then for all such sequences
$\sigma, \sigma'$ and all weights $w$, the loss over the concatenation $\sigma\sigma'$ satisfies
$L(\sigma\sigma', w) = L(\sigma, w) + L(\sigma', W(\sigma, w))$.

Formalized by `Cslib.MachineLearning.Hedge.algLoss_append`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-loss-append).

## The summed second moments split at any round

Fix a learning rate $\eta$ and $n$ experts.
For a finite sequence $\sigma$ of loss vectors in $\mathbb{R}^n$ and weights $w \in \mathbb{R}^n$,
write $Q(\sigma, w)$ for the sum over the rounds of $\sigma$ of the weighted second moments of the
losses, started from $w$, and $W(\sigma, w)$ for the weights after the rounds of $\sigma$ started
from $w$. Then for all such sequences $\sigma, \sigma'$ and all weights $w$,
$Q(\sigma\sigma', w) = Q(\sigma, w) + Q(\sigma', W(\sigma, w))$.

Formalized by `Cslib.MachineLearning.Hedge.algSq_append`, a theorem declared in [CSLibExt/MachineLearning/Hedge.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Hedge.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html#alg-sq-append).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hedge algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/hedge-algorithm)
