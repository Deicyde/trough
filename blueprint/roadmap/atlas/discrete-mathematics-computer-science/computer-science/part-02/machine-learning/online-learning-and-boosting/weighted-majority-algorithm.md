---
declaration: section
origin: cited
lean: Cslib.MachineLearning.WeightedMajority.Round, Cslib.MachineLearning.WeightedMajority.weightOn, Cslib.MachineLearning.WeightedMajority.predict, Cslib.MachineLearning.WeightedMajority.update, Cslib.MachineLearning.WeightedMajority.weights, Cslib.MachineLearning.WeightedMajority.mistakes, Cslib.MachineLearning.WeightedMajority.expertMistakes, Cslib.MachineLearning.WeightedMajority.total
statement: formalized
proof: formalized
---

# Weighted majority algorithm

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html).

## Round of prediction with expert advice

A round with $n$ experts is a pair $(a, y)$, where
$a$ assigns to each expert $i \in \{0, \dots, n - 1\}$ its binary advice (true or false) and the
binary value $y$ is the true outcome.

Formalized by `Cslib.MachineLearning.WeightedMajority.Round`, an abbreviation declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#round).

## Weight on an answer

Given weights $w_0, \dots, w_{n-1}$ in a field $K$, advice
$a \in \{\mathrm{true}, \mathrm{false}\}^n$ and an answer $b \in \{\mathrm{true}, \mathrm{false}\}$,
the weight on $b$ is $\sum_{i : a_i = b} w_i$, the total weight of the experts advising $b$.

Formalized by `Cslib.MachineLearning.WeightedMajority.weightOn`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#weight-on).

## Weighted majority vote

Let $K$ be a field with a linear order. Given weights in $K$ on
$n$ experts and a binary advice (true or false) from each expert, the weighted majority vote is
true when the total weight of the experts advising false is at most the total weight of the
experts advising true, and false otherwise. In particular ties go to true.

Formalized by `Cslib.MachineLearning.WeightedMajority.predict`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#predict).

## Weighted majority update

Given a penalty factor $\beta$ and weights $w_0, \dots, w_{n-1}$
in a field $K$, and a round with advice $a \in \{\mathrm{true}, \mathrm{false}\}^n$ and outcome
$y$, the updated weight of expert $i$ is $w_i$ if $a_i = y$ and $\beta w_i$ otherwise: after the
outcome is revealed, every expert that was wrong has its weight multiplied by $\beta$.

Formalized by `Cslib.MachineLearning.WeightedMajority.update`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#update).

## Weights after a run

For a penalty factor $\beta$ in a field $K$, the weights after a
sequence of rounds $r_1, \dots, r_k$ starting from weights $w$ in $K$ are obtained by applying the
weighted majority update with penalty $\beta$ for $r_1$, then for $r_2$, and so on up to $r_k$;
for the empty sequence they are $w$.

Formalized by `Cslib.MachineLearning.WeightedMajority.weights`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#weights).

## Mistakes of the weighted majority algorithm

Let $K$ be a field with a linear order, let
$\beta \in K$ be a penalty and let $w$ be initial weights in $K$ on $n$ experts. The weighted
majority algorithm processes a list of rounds in order: in each round it predicts the weighted
majority vote of the experts' advice under the current weights, and then multiplies the weight of
every expert whose advice differed from the true outcome by $\beta$. Its number of mistakes is the
number of rounds in which its prediction differs from the true outcome.

Formalized by `Cslib.MachineLearning.WeightedMajority.mistakes`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#mistakes).

## Mistakes of an expert

Given a list of rounds with $n$ experts and an expert $i$, the
number of mistakes of $i$ is the number of rounds in the list in which the advice of expert $i$
differs from the true outcome.

Formalized by `Cslib.MachineLearning.WeightedMajority.expertMistakes`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#expert-mistakes).

## Total weight

The total weight of weights $w_0, \dots, w_{n-1}$ in a field $K$ is
$\sum_{i < n} w_i$.

Formalized by `Cslib.MachineLearning.WeightedMajority.total`, a definition declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#total).

## Total weight after an update

Let $\beta$ be an element of a linearly ordered field $K$,
let $w_0, \dots, w_{n-1} \in K$ be weights on $n$ experts, and let $r$ be a round with advice
$a \in \{\mathrm{true}, \mathrm{false}\}^n$ and outcome $y$. If $w'$ are the weights after the
update with penalty $\beta$ on $r$, then
$\sum_{i < n} w'_i = \sum_{i < n} w_i - (1 - \beta) \sum_{i : a_i = \lnot y} w_i$: the experts
that advised wrongly keep a $\beta$ fraction of their weight.

Formalized by `Cslib.MachineLearning.WeightedMajority.total_update`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#total-update).

## A mistake costs weight

Let $K$ be a linearly ordered field, let $\beta \in K$ with
$\beta \le 1$, let $w$ be weights in $K$ on $n$ experts, and let $r$ be a round on which the
weighted majority vote under $w$ differs from the true outcome. If $W$ is the total weight of $w$
and $W'$ is the total weight after updating $w$ on $r$ with penalty $\beta$, then
$2 W' \le (1 + \beta) W$.

At least half of the weight was on the wrong side, and that side keeps only a $\beta$ fraction of
its weight.

Formalized by `Cslib.MachineLearning.WeightedMajority.total_update_of_mistake`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#total-update-of-mistake).

## An update never increases the total weight

Let $K$ be a linearly ordered field, let
$\beta \in K$ with $\beta \le 1$, and let $w$ be nonnegative weights in $K$ on $n$ experts. For
every round $r$, the total weight after updating $w$ on $r$ with penalty $\beta$ is at most the
total weight of $w$.

Formalized by `Cslib.MachineLearning.WeightedMajority.total_update_le`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#total-update-le).

## Total weight bound in terms of mistakes

Let $0 \le \beta \le 1$ in a linearly ordered
field $K$, let $w$ be nonnegative weights in $K$ on $n$ experts, and let $\rho$ be a sequence of
rounds. Let $M$ be the number of mistakes the weighted majority algorithm with penalty $\beta$
makes on $\rho$ starting from $w$, and let $W$ and $W'$ be the total weights before and after
$\rho$. Then $W' \cdot 2^M \le (1 + \beta)^M \cdot W$.

Formalized by `Cslib.MachineLearning.WeightedMajority.total_weights_mul_le`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#total-weights-mul-le).

## Final weight of an expert

For a penalty factor $\beta$ in a field $K$, initial weights
$w_0, \dots, w_{n-1} \in K$ and a sequence of rounds, the weight of expert $i$ after these rounds
is $w_i \beta^{m_i}$, where $m_i$ is the number of rounds in which the advice of expert $i$
differs from the outcome.

Formalized by `Cslib.MachineLearning.WeightedMajority.weights_apply`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#weights-apply).

## Littlestone–Warmuth mistake bound

Let $K$ be a linearly ordered field and let
$\beta \in K$ with $0 \le \beta \le 1$. Run the weighted majority algorithm with penalty $\beta$
on a list of rounds with $n$ experts, starting from weight $1$ on every expert, and let $M$ be its
number of mistakes. Then every expert $i$, with $m$ mistakes on these rounds, satisfies
$\beta^m 2^M \le n (1 + \beta)^M$.

Formalized by `Cslib.MachineLearning.WeightedMajority.mistake_bound_general`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#mistake-bound-general).

## Mistake bound for the penalty $1/2$

Run the weighted majority algorithm with rational
weights and penalty $1/2$ on a list of rounds with $n$ experts, starting from weight $1$ on every
expert, and let $M$ be its number of mistakes. Then every expert $i$, with $m$ mistakes on these
rounds, satisfies $(4/3)^M \le n \cdot 2^m$.

Formalized by `Cslib.MachineLearning.WeightedMajority.mistake_bound`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#mistake-bound).

## Mistake bound for the penalty $1/2$ in integers

Run the weighted majority algorithm
with rational weights and penalty $1/2$ on a list of rounds with $n$ experts, starting from
weight $1$ on every expert, and let $M$ be its number of mistakes. Then every expert $i$, with
$m$ mistakes on these rounds, satisfies $4^M \le n \cdot 3^M \cdot 2^m$ in the natural numbers.

Taking logarithms, $M \le (m + \log_2 n) / \log_2 (4/3) \approx 2.41 (m + \log_2 n)$.

Formalized by `Cslib.MachineLearning.WeightedMajority.mistake_bound_nat`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#mistake-bound-nat).

## Weights over a concatenated run

For a penalty factor $\beta$ in a field $K$, initial
weights $w$ in $K$ and sequences of rounds $\rho$ and $\rho'$, the weights after running $\rho$
followed by $\rho'$ from $w$ equal the weights after running $\rho'$ from the weights obtained by
running $\rho$ from $w$.

Formalized by `Cslib.MachineLearning.WeightedMajority.weights_append`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#weights-append).

## Mistakes split over concatenated runs

Let $K$ be a field with a linear order, let
$\beta \in K$ be a penalty, let $w$ be weights in $K$ on $n$ experts, and let $R$ and $R'$ be
lists of rounds. The number of mistakes of the weighted majority algorithm with penalty $\beta$
on $R$ followed by $R'$, starting from $w$, equals its number of mistakes on $R$ starting from
$w$ plus its number of mistakes on $R'$ starting from the weights reached after $R$.

Formalized by `Cslib.MachineLearning.WeightedMajority.mistakes_append`, a theorem declared in [CSLibExt/MachineLearning/WeightedMajority.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/WeightedMajority.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html#mistakes-append).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted majority algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/weighted-majority-algorithm)
