---
declaration: section
origin: cited
lean: Cslib.MachineLearning.BayesClassifier.zeroOneLoss, Cslib.MachineLearning.BayesClassifier.lintegral_zeroOneLoss, Cslib.MachineLearning.BayesClassifier.lintegral_zeroOneLoss_right, Cslib.MachineLearning.BayesClassifier.avgRisk_zeroOneLoss_deterministic, Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax, Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax.isArgminEstimator, Cslib.MachineLearning.BayesClassifier.isPosteriorArgmax_iff_isArgminEstimator, Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax.isBayesEstimator
statement: formalized
proof: formalized
---

# Bayes classifier

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html).

## The 0-1 loss

For elements $c$ and $y$ of a type $C$ of classes, the 0-1 loss of
predicting $y$ when the true class is $c$ is the extended nonnegative real number that equals
$0$ if $y = c$ and $1$ if $y \ne c$.

Formalized by `Cslib.MachineLearning.BayesClassifier.zeroOneLoss`, a definition declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#zero-one-loss).

## Expected 0-1 loss of a fixed prediction

Let $C$ be a measurable space in which every
singleton is measurable, let $\nu$ be a measure on $C$, and let $y \in C$. Writing $\ell(c, y)$
for the 0-1 loss of predicting $y$ when the true class is $c$, we have
$\int \ell(c, y) \, d\nu(c) = \nu(C \setminus \{y\})$.

Formalized by `Cslib.MachineLearning.BayesClassifier.lintegral_zeroOneLoss`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#lintegral-zero-one-loss).

## Integrating the 0-1 loss over the prediction

Let $C$ be a measurable space with
measurable singletons, $\nu$ a measure on $C$ and $c \in C$, and let $\ell(c, y)$ be the 0-1
loss of predicting $y$ when the true class is $c$ ($0$ if $y = c$, $1$ otherwise). Then
$\int_C \ell(c, y)\,\nu(dy) = \nu(C \setminus \{c\})$.

When $\nu$ is the law of a random prediction, this is its expected 0-1 loss when the true class
is $c$.

Formalized by `Cslib.MachineLearning.BayesClassifier.lintegral_zeroOneLoss_right`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#lintegral-zero-one-loss-right).

## The 0-1 risk of a deterministic classifier

Let $C$ be a measurable space of classes with
measurable singletons, $P$ a kernel from $C$ to the observation space $\mathcal X$, $\pi$ a
measure on $C$, $f : \mathcal X \to C$ a measurable map, and $\ell(c, y)$ the 0-1 loss ($0$ if
$y = c$, $1$ otherwise). Then the average 0-1 risk of the deterministic kernel
$\delta_f : x \mapsto \delta_{f(x)}$,
$\int_C \int_C \ell(c, y)\,(\delta_f \circ P)(c)(dy)\,\pi(dc)$ with
$(\delta_f \circ P)(c) = \int_{\mathcal X} \delta_{f(x)}\,P(c)(dx)$, equals
$\int_C P(c)(\{x \in \mathcal X : f(x) \ne c\})\,\pi(dc)$.

When each $P(c)$ is a probability measure, $P(c)(\{x : f(x) \ne c\})$ is the probability that
$f$ misclassifies an observation of class $c$.

Formalized by `Cslib.MachineLearning.BayesClassifier.avgRisk_zeroOneLoss_deterministic`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#avg-risk-zero-one-loss-deterministic).

## Posterior argmax classifier

Let the set $C$ of classes be countable and nonempty with
measurable singletons, let $P$ be a finite kernel from $C$ to the observation space $\mathcal X$
and $\pi$ a finite measure on $C$, write $P \circ \pi$ for the marginal measure on $\mathcal X$
and $P^\dagger_\pi$ for the posterior kernel from $\mathcal X$ to $C$. A map
$f : \mathcal X \to C$ is a posterior argmax classifier for $P$ and $\pi$ if $f$ is measurable
and, for $(P \circ \pi)$-almost every $x$,
$P^\dagger_\pi(x)(\{y\}) \le P^\dagger_\pi(x)(\{f(x)\})$ for every $y \in C$.

Countably many classes with measurable singletons make the posterior masses of classes
meaningful, and give the standard Borel structure the posterior needs.

Formalized by `Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax`, a structure declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#is-posterior-argmax).

## A posterior argmax classifier is an argmin estimator for the 0-1 loss

Let the set $C$ of
classes be countable and nonempty with measurable singletons, let $P$ be a finite kernel from $C$
to the observation space $\mathcal X$ and $\pi$ a finite measure on $C$, write $P \circ \pi$ for
the marginal measure on $\mathcal X$, $P^\dagger_\pi$ for the posterior kernel from $\mathcal X$
to $C$, and $\ell(c, y)$ for the 0-1 loss ($0$ if $y = c$, $1$ otherwise). If
$f : \mathcal X \to C$ is a posterior argmax classifier for $P$ and $\pi$, then $f$ is an argmin
estimator for $\ell$: it is measurable and, for $(P \circ \pi)$-almost every $x$,
$\int_C \ell(c, f(x))\,P^\dagger_\pi(x)(dc)$ equals
$\inf_{y \in C} \int_C \ell(c, y)\,P^\dagger_\pi(x)(dc)$.

Formalized by `Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax.isArgminEstimator`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#is-argmin-estimator).

## Posterior argmax classifiers are exactly the argmin estimators for the 0-1 loss

Let the
set $C$ of classes be countable and nonempty with measurable singletons, let $P$ be a finite
kernel from $C$ to the observation space $\mathcal X$ and $\pi$ a finite measure on $C$, write
$P \circ \pi$ for the marginal measure on $\mathcal X$, $P^\dagger_\pi$ for the posterior kernel
from $\mathcal X$ to $C$, and $\ell(c, y)$ for the 0-1 loss ($0$ if $y = c$, $1$ otherwise). A
map $f : \mathcal X \to C$ is a posterior argmax classifier for $P$ and $\pi$ if and only if it
is an argmin estimator for $\ell$: $f$ is measurable and, for $(P \circ \pi)$-almost every $x$,
$\int_C \ell(c, f(x))\,P^\dagger_\pi(x)(dc)$ equals
$\inf_{y \in C} \int_C \ell(c, y)\,P^\dagger_\pi(x)(dc)$.

Formalized by `Cslib.MachineLearning.BayesClassifier.isPosteriorArgmax_iff_isArgminEstimator`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#is-posterior-argmax-iff-is-argmin-estima).

## The Bayes classifier is optimal

A posterior argmax classifier attains the Bayes risk
for the 0-1 loss.

Formalized by `Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax.isBayesEstimator`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#is-bayes-estimator).

## A posterior argmax classifier has minimal 0-1 risk

Let the set $C$ of classes be countable
and nonempty with measurable singletons, let $P$ be a finite kernel from $C$ to the observation
space $\mathcal X$ and $\pi$ a finite measure on $C$, and let $\ell(c, y)$ be the 0-1 loss
($0$ if $y = c$, $1$ otherwise). For a kernel $\kappa$ from $\mathcal X$ to $C$, its average 0-1
risk is $\int_C \int_C \ell(c, y)\,(\kappa \circ P)(c)(dy)\,\pi(dc)$, where
$(\kappa \circ P)(c) = \int_{\mathcal X} \kappa(x)\,P(c)(dx)$. If $f : \mathcal X \to C$ is a
posterior argmax classifier for $P$ and $\pi$, then for every Markov kernel $\kappa$ from
$\mathcal X$ to $C$ (a randomized classifier), the average 0-1 risk of the deterministic kernel
$x \mapsto \delta_{f(x)}$ is at most the average 0-1 risk of $\kappa$.

Formalized by `Cslib.MachineLearning.BayesClassifier.IsPosteriorArgmax.avgRisk_le`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#avg-risk-le).

## MAP classifiers are posterior argmax classifiers

Let the set $C$ of classes be countable
and nonempty with measurable singletons, let the observation space $\mathcal X$ be countable with
measurable singletons, let $P$ be a Markov kernel from $C$ to $\mathcal X$ and $\pi$ a finite
measure on $C$, and write $P \circ \pi$ for the marginal measure on $\mathcal X$. If
$f : \mathcal X \to C$ assigns to every observation $x$ with $(P \circ \pi)(\{x\}) \ne 0$ a
maximum a posteriori class for $x$ under $P$ and $\pi$, then $f$ is a posterior argmax
classifier for $P$ and $\pi$.

Since posterior argmax classifiers attain the Bayes risk for the 0-1 loss, MAP classification is
Bayes optimal; observations of zero evidence may be classified arbitrarily.

Formalized by `Cslib.MachineLearning.BayesClassifier.isPosteriorArgmax_of_isMAP`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#is-posterior-argmax-of-is-map).

## Existence of a posterior argmax classifier

Let the set $C$ of classes be finite and
nonempty with measurable singletons, let $P$ be a finite kernel from $C$ to the observation space
$\mathcal X$ and $\pi$ a finite measure on $C$. Then there is a posterior argmax classifier
$f : \mathcal X \to C$ for $P$ and $\pi$.

The classifier constructed takes, at each observation, the first maximizer of the posterior
probability in an enumeration of the classes.

Formalized by `Cslib.MachineLearning.BayesClassifier.exists_isPosteriorArgmax`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#exists-is-posterior-argmax).

## The Bayes risk for the 0-1 loss

Let the set $C$ of classes be finite and nonempty with
measurable singletons, let $P$ be a finite kernel from $C$ to the observation space $\mathcal X$
and $\pi$ a finite measure on $C$, and let $\ell(c, y)$ be the 0-1 loss ($0$ if $y = c$, $1$
otherwise). Write $P \circ \pi$ for the marginal measure on $\mathcal X$ and $P^\dagger_\pi$ for
the posterior kernel from $\mathcal X$ to $C$. For a kernel $\kappa$ from $\mathcal X$ to $C$,
write $(\kappa \circ P)(c) = \int_{\mathcal X} \kappa(x)\,P(c)(dx)$. Then the Bayes risk for the
0-1 loss, the infimum over all Markov kernels $\kappa$ from $\mathcal X$ to $C$ of the average
0-1 risk $\int_C \int_C \ell(c, y)\,(\kappa \circ P)(c)(dy)\,\pi(dc)$, equals
$\int_{\mathcal X} \inf_{y \in C} P^\dagger_\pi(x)(C \setminus \{y\})\,(P \circ \pi)(dx)$: the
average over the observations of the posterior probability of error of the best guess.

Formalized by `Cslib.MachineLearning.BayesClassifier.bayesRisk_zeroOneLoss`, a theorem declared in [CSLibExt/MachineLearning/Generative/BayesClassifier.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Generative/BayesClassifier.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html#bayes-risk-zero-one-loss).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayes classifier](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-classifier)
