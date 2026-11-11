---
declaration: section
origin: cited
lean: Cslib.MachineLearning.InformationTheory.crossEntropyLoss, Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq, Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq_top_iff, Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq_neg_logb_prod, Cslib.MachineLearning.InformationTheory.crossEntropyLoss_le_iff_of_ne_zero, Cslib.MachineLearning.InformationTheory.crossEntropyLoss_le_iff
statement: formalized
proof: formalized
---

# Cross-entropy loss

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html).

## Cross-entropy loss

Let $f$ be a probabilistic classifier, assigning to each input
$x \in X$ a probability distribution $f(x)$ on a finite set of labels, and let
$D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample. The cross-entropy (log) loss of $f$
on $D$, in bits, is the value in $[0, \infty]$

$$\Big(\sum_{n=1}^{N} H\big(\delta_{y_n}, f(x_n)\big)\Big) / N,$$

where $H$ is the cross-entropy and $\delta_y$ is the point mass at $y$; it is $0$ when $N = 0$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss`, a definition declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss).

## The cross-entropy loss is the average negative log-likelihood

Let $f$ be a probabilistic
classifier, assigning to each input $x \in X$ a probability distribution $f(x)$ on a finite set
of labels, and let $D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample. The cross-entropy
loss of $f$ on $D$ equals the average surprisal of the labels,

$$\Big(\sum_{n=1}^{N} s\big(f(x_n)(y_n)\big)\Big) / N,$$

where $s(q) = -\log_2 q$ is the surprisal of a probability $q$, with $s(0) = \infty$, and the
average is computed in $[0, \infty]$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss-eq).

## The cross-entropy loss is infinite exactly when a label is ruled out

Let $f$ be a
probabilistic classifier, assigning to each input $x \in X$ a probability distribution $f(x)$ on
a finite set of labels, and let $D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample with
$N \ge 1$. The cross-entropy loss of $f$ on $D$ is $\infty$ if and only if $f(x_n)(y_n) = 0$ for
some $n$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq_top_iff`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss-eq-top-iff).

## Cross-entropy loss via the likelihood

Let $f$ be a probabilistic classifier, assigning
to each input $x \in X$ a probability distribution $f(x)$ on a finite set of labels, and let
$D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample with $f(x_n)(y_n) \ne 0$ for every $n$.
Then the cross-entropy loss of $f$ on $D$ equals $-\log_2(L) / N$, where
$L = \prod_{n=1}^{N} f(x_n)(y_n)$ is the likelihood of the sample and the division is computed in
$[0, \infty]$, so that both sides are $0$ when $N = 0$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss_eq_neg_logb_prod`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss-eq-neg-logb-prod).

## Comparing cross-entropy losses of classifiers that rule out no label

Let $f$ and $g$ be
probabilistic classifiers, each assigning to every input $x \in X$ a probability distribution on
a finite set of labels, and let $D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample with
$N \ge 1$ such that $f(x_n)(y_n) \ne 0$ and $g(x_n)(y_n) \ne 0$ for every $n$. Then the
cross-entropy loss of $f$ on $D$ is at most that of $g$ if and only if
$\prod_{n=1}^{N} g(x_n)(y_n) \le \prod_{n=1}^{N} f(x_n)(y_n)$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss_le_iff_of_ne_zero`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss-le-iff-of-ne-zero).

## Minimizing cross-entropy is maximum likelihood

Let $f$ and $g$ be probabilistic
classifiers, each assigning to every input $x \in X$ a probability distribution on a finite set of
labels, and let $D = ((x_1, y_1), \dots, (x_N, y_N))$ be a labelled sample with $N \ge 1$. Then
the cross-entropy loss of $f$ on $D$ is at most that of $g$ if and only if
$\prod_{n=1}^{N} g(x_n)(y_n) \le \prod_{n=1}^{N} f(x_n)(y_n)$, that is, $f$ gives the labels at
least as large a likelihood as $g$.

A label predicted to be impossible gives likelihood $0$ and loss $\infty$.

Formalized by `Cslib.MachineLearning.InformationTheory.crossEntropyLoss_le_iff`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/LogLoss.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/LogLoss.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html#cross-entropy-loss-le-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cross-entropy loss](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/cross-entropy-loss)
