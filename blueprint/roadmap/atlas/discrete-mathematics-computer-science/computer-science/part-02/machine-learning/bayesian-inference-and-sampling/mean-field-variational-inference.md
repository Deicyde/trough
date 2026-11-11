---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Variational.evidence, Cslib.MachineLearning.Variational.posterior, Cslib.MachineLearning.Variational.elbo, Cslib.MachineLearning.Variational.kl, Cslib.MachineLearning.Variational.kl_nonneg, Cslib.MachineLearning.Variational.elbo_eq_log_evidence_sub_kl, Cslib.MachineLearning.Variational.elbo_le_log_evidence, Cslib.MachineLearning.Variational.kl_posterior_nonneg
statement: formalized
proof: formalized
---

# Mean-field variational inference

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html).

## The ELBO and the KL divergence

## Evidence of an unnormalized posterior

Let $Z$ be a finite set and let
$p : Z \to \mathbb{R}$ give the joint values $p(z) = p(x, z)$ of a fixed observation $x$ with each
latent value $z \in Z$ (an unnormalized posterior). The evidence is
$p(x) = \sum_{z \in Z} p(z)$.

Formalized by `Cslib.MachineLearning.Variational.evidence`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#evidence).

## Posterior of an unnormalized joint

Let $Z$ be a finite set and let
$p : Z \to \mathbb{R}$ give the joint values $p(z) = p(x, z)$ of a fixed observation $x$ with each
latent value $z \in Z$. The posterior of $z$ is $p(z \mid x) = p(z) / p(x)$, where
$p(x) = \sum_{z' \in Z} p(z')$ is the evidence (the quotient is read as $0$ when $p(x) = 0$).

Formalized by `Cslib.MachineLearning.Variational.posterior`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#posterior).

## Evidence lower bound of a single observation

Let $Z$ be a finite set, let
$p : Z \to \mathbb{R}$ give the joint values $p(z) = p(x, z)$ of a fixed observation $x$ with each
latent value $z \in Z$, and let $q : Z \to \mathbb{R}$. The evidence lower bound of $q$ is
$\mathrm{ELBO}(p, q) = \sum_{z \in Z} q(z) \bigl(\log p(z) - \log q(z)\bigr)$.

Formalized by `Cslib.MachineLearning.Variational.elbo`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo).

## Finite Kullback–Leibler formula

Let $Z$ be a finite set and let $q, r : Z \to \mathbb{R}$.
The Kullback–Leibler formula of $q$ against $r$ is
$\mathrm{KL}(q \,\|\, r) = \sum_{z \in Z} q(z) \bigl(\log q(z) - \log r(z)\bigr)$; terms with
$q(z) = 0$ vanish.

This is the Kullback–Leibler divergence of $q$ from $r$ when $r(z) > 0$ for every $z$, the only
case used here (where $r$ is the posterior of a positive joint). If $r$ vanishes where $q$ does
not, the divergence is infinite, but this real-valued formula is finite, since it reads $\log 0$
as $0$.

Formalized by `Cslib.MachineLearning.Variational.kl`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#kl).

## Gibbs' inequality

Let $Z$ be a finite set, let $q$ be a probability distribution on $Z$,
and let $r : Z \to \mathbb{R}$ satisfy $r(z) > 0$ for every $z \in Z$ and
$\sum_{z \in Z} r(z) = 1$. Then
$\mathrm{KL}(q \,\|\, r) = \sum_{z \in Z} q(z) \bigl(\log q(z) - \log r(z)\bigr) \ge 0$.

Formalized by `Cslib.MachineLearning.Variational.kl_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#kl-nonneg).

## The ELBO is the log evidence minus the KL divergence

Let $Z$ be a nonempty finite set
and let $p : Z \to \mathbb{R}$ give the joint values $p(z) = p(x, z)$ of a fixed observation $x$
with each latent value $z \in Z$, where $p(z) > 0$ for every $z \in Z$. Let
$p(x) = \sum_{z \in Z} p(z)$ be the evidence and $p(z \mid x) = p(z) / p(x)$ the posterior. For
$q, r : Z \to \mathbb{R}$ write
$\mathrm{ELBO}(p, q) = \sum_{z \in Z} q(z) \bigl(\log p(z) - \log q(z)\bigr)$ and
$\mathrm{KL}(q \,\|\, r) = \sum_{z \in Z} q(z) \bigl(\log q(z) - \log r(z)\bigr)$. Then for every
probability distribution $q$ on $Z$,
$\mathrm{ELBO}(p, q) = \log p(x) - \mathrm{KL}\bigl(q \,\|\, p(\cdot \mid x)\bigr)$.

Formalized by `Cslib.MachineLearning.Variational.elbo_eq_log_evidence_sub_kl`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-eq-log-evidence-sub-kl).

## The ELBO is a lower bound

Let $Z$ be a finite set and let $p : Z \to \mathbb{R}$ satisfy
$p(z) > 0$ for all $z$, with evidence $p(x) = \sum_{z \in Z} p(z)$. Then for every probability
distribution $q$ on $Z$,

$$\mathrm{ELBO}(p, q) = \sum_{z \in Z} q(z) (\log p(z) - \log q(z)) \le \log p(x).$$

This is Gibbs' inequality.

Formalized by `Cslib.MachineLearning.Variational.elbo_le_log_evidence`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-le-log-evidence).

## The KL divergence to the posterior is nonnegative

Let $Z$ be a nonempty finite set, let
$p : Z \to \mathbb{R}$ satisfy $p(z) > 0$ for every $z \in Z$, and let $q$ be a probability
distribution on $Z$. Let $\pi(z) = p(z) / \sum_{z' \in Z} p(z')$ be the posterior of $p$. Then
$\mathrm{KL}(q \,\|\, \pi) = \sum_{z \in Z} q(z) \bigl(\log q(z) - \log \pi(z)\bigr) \ge 0$.

Formalized by `Cslib.MachineLearning.Variational.kl_posterior_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#kl-posterior-nonneg).

## The ELBO bound is attained at the posterior

Let $Z$ be a nonempty finite set and let
$p : Z \to \mathbb{R}$ satisfy $p(z) > 0$ for all $z$, with evidence $p(x) = \sum_{z \in Z} p(z)$
and posterior $p(z \mid x) = p(z) / p(x)$. Then $\mathrm{ELBO}(p, p(\cdot \mid x)) = \log p(x)$,
where $\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$.

Formalized by `Cslib.MachineLearning.Variational.elbo_posterior`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-posterior).

## The EM evidence lower bound is a sum of per-point ELBOs

Let $Z$ be a finite set, let
$p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent values
$z \in Z$, let $x_1, \dots, x_N$ be data, let $\theta$ be a parameter and let
$q_1, \dots, q_N : Z \to \mathbb{R}$. Then the evidence lower bound of expectation-maximization,
$\sum_{n=1}^N \sum_{z \in Z} q_n(z) \bigl(\log p_\theta(x_n, z) - \log q_n(z)\bigr)$, equals
$\sum_{n=1}^N \mathrm{ELBO}(p_\theta(x_n, \cdot), q_n)$, the sum over the data points of the
single-observation evidence lower bound of $q_n$ for the joint values
$z \mapsto p_\theta(x_n, z)$.

Formalized by `Cslib.MachineLearning.Variational.em_elbo_eq`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#em-elbo-eq).

## Mean-field product distribution

Let $A$ and $B$ be finite sets and let
$q_1 : A \to \mathbb{R}$ and $q_2 : B \to \mathbb{R}$. Their mean-field (product) distribution is
the function on $A \times B$ given by $q(a, b) = q_1(a) \, q_2(b)$.

Formalized by `Cslib.MachineLearning.Variational.prodDist`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#prod-dist).

## Expected log-joint

Let $A$ and $B$ be finite sets and let $p : A \times B \to \mathbb{R}$
and $q_2 : B \to \mathbb{R}$. For $a \in A$, the expected log-joint of $a$ under $q_2$ is
$\mathbb{E}_{q_2}[\log p(a, \cdot)] = \sum_{b \in B} q_2(b) \log p(a, b)$.

Formalized by `Cslib.MachineLearning.Variational.expectedLog`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#expected-log).

## Mean-field (CAVI) update of the first factor

Let $A$ and $B$ be finite sets, let
$p : A \times B \to \mathbb{R}$ be a joint and let $q_2 : B \to \mathbb{R}$. The
coordinate-ascent update of the first factor is the function $q_1 : A \to \mathbb{R}$ given by

$$q_1(a) = \frac{\exp E(a)}{\sum_{a' \in A} \exp E(a')},$$

where $E(a) = \sum_{b \in B} q_2(b) \log p(a, b)$ is the expected log-joint of $a$ under $q_2$.
That is, $q_1(a) \propto \exp \mathbb{E}_{q_2}[\log p(a, \cdot)]$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.cavi`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#cavi).

## ELBO of a product distribution

Let $A$ and $B$ be finite sets, let
$p : A \times B \to \mathbb{R}$ be a joint, and let $q_1$ and $q_2$ be probability distributions
on $A$ and $B$, with product $(q_1 q_2)(a, b) = q_1(a) q_2(b)$. Then

$$\mathrm{ELBO}(p, q_1 q_2) = \sum_{a \in A} q_1(a) \bigl(E(a) - \log q_1(a)\bigr) -
\sum_{b \in B} q_2(b) \log q_2(b),$$

where $E(a) = \sum_{b \in B} q_2(b) \log p(a, b)$ is the expected log-joint of $a$ under $q_2$
and $\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$. So the ELBO splits into a
$q_1$-term and the entropy of $q_2$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.elbo_prodDist`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-prod-dist).

## The CAVI update maximizes the ELBO over the first factor

Let $A$ and $B$ be finite sets
with $A$ nonempty, let $p : A \times B \to \mathbb{R}$ be a joint, and let $q_1$ and $q_2$ be
probability distributions on $A$ and $B$. Let $q_1^*$ be the CAVI update of the first factor
given $q_2$, $q_1^*(a) = \exp E(a) / \sum_{a' \in A} \exp E(a')$ with
$E(a) = \sum_{b \in B} q_2(b) \log p(a, b)$. Then
$\mathrm{ELBO}(p, q_1 q_2) \le \mathrm{ELBO}(p, q_1^* q_2)$, where
$(q_1 q_2)(a, b) = q_1(a) q_2(b)$ and
$\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.elbo_le_elbo_cavi`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-le-elbo-cavi).

## Swapped joint

Let $A$ and $B$ be finite sets and let $p : A \times B \to \mathbb{R}$. The
swapped joint of $p$ is the function on $B \times A$ given by $(b, a) \mapsto p(a, b)$.

Formalized by `Cslib.MachineLearning.Variational.swapJoint`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#swap-joint).

## Mean-field (CAVI) update of the second factor

Let $A$ and $B$ be finite sets, let
$p : A \times B \to \mathbb{R}$ be a joint and let $q_1 : A \to \mathbb{R}$. The
coordinate-ascent update of the second factor is the function $q_2 : B \to \mathbb{R}$ given by

$$q_2(b) = \frac{\exp F(b)}{\sum_{b' \in B} \exp F(b')},$$

where $F(b) = \sum_{a \in A} q_1(a) \log p(a, b)$. That is,
$q_2(b) \propto \exp \mathbb{E}_{q_1}[\log p(\cdot, b)]$; it is the update of the first factor
applied to the joint with its two factors swapped.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.cavi₂`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#cavi-2).

## The CAVI update of the second factor does not decrease the ELBO

Let $A$ and $B$ be finite
sets with $B$ nonempty, let $p : A \times B \to \mathbb{R}$ be a joint, and let $q_1$ and $q_2$ be
probability distributions on $A$ and $B$. Let $q_2^*$ be the CAVI update of the second factor
given $q_1$, $q_2^*(b) = \exp F(b) / \sum_{b' \in B} \exp F(b')$ with
$F(b) = \sum_{a \in A} q_1(a) \log p(a, b)$. Then
$\mathrm{ELBO}(p, q_1 q_2) \le \mathrm{ELBO}(p, q_1 q_2^*)$, where
$(q_1 q_2)(a, b) = q_1(a) q_2(b)$ and
$\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.elbo_le_elbo_cavi₂`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-le-elbo-cavi-2).

## Mean-field coordinate-ascent sweep

Let $A$ and $B$ be finite sets and
$p : A \times B \to \mathbb{R}$. One sweep of coordinate ascent (CAVI) sends a pair of factors
$(q_1, q_2)$, with $q_1 : A \to \mathbb{R}$ and $q_2 : B \to \mathbb{R}$, to $(q_1', q_2')$, where
$q_1'$ is the CAVI update of the first factor given $q_2$,
$q_1'(a) = \exp(\sum_b q_2(b) \log p(a, b)) / \sum_{a'} \exp(\sum_b q_2(b) \log p(a', b))$, and
$q_2'$ is the CAVI update of the second factor given the new first factor $q_1'$,
$q_2'(b) = \exp(\sum_a q_1'(a) \log p(a, b)) / \sum_{b'} \exp(\sum_a q_1'(a) \log p(a, b'))$.
The old first factor $q_1$ is not used.

Here $\log x$ means $\log |x|$ for $x \ne 0$ and $\log 0 = 0$, so $p$ need not be positive.

Formalized by `Cslib.MachineLearning.Variational.sweep`, a definition declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#sweep).

## A sweep of coordinate ascent does not decrease the ELBO

Let $A$ and $B$ be nonempty
finite sets, let $p : A \times B \to \mathbb{R}$ be a joint, and let $q_1$ and $q_2$ be probability
distributions on $A$ and $B$. One sweep replaces $q_1$ by its CAVI update $q_1'$ given $q_2$ and
then $q_2$ by its CAVI update $q_2'$ given $q_1'$, where
$q_1'(a) \propto \exp \sum_{b} q_2(b) \log p(a, b)$ and
$q_2'(b) \propto \exp \sum_{a} q_1'(a) \log p(a, b)$, each normalized to sum to $1$. Then
$\mathrm{ELBO}(p, q_1 q_2) \le \mathrm{ELBO}(p, q_1' q_2')$, where
$(q_1 q_2)(a, b) = q_1(a) q_2(b)$ and
$\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.elbo_le_elbo_sweep`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-le-elbo-sweep).

## Mean-field coordinate ascent never decreases the ELBO

Let $A$ and $B$ be nonempty finite
sets, let $p : A \times B \to \mathbb{R}$ be a joint, and let $q_1^{(0)}$ and $q_2^{(0)}$ be
probability distributions on $A$ and $B$. A sweep of coordinate ascent replaces $q_1$ by its CAVI
update $q_1'(a) \propto \exp \sum_{b} q_2(b) \log p(a, b)$ and then $q_2$ by its CAVI update
$q_2'(b) \propto \exp \sum_{a} q_1'(a) \log p(a, b)$, each normalized to sum to $1$. Let
$(q_1^{(t)}, q_2^{(t)})$ be the result of $t$ sweeps from $(q_1^{(0)}, q_2^{(0)})$. Then
$t \mapsto \mathrm{ELBO}(p, q_1^{(t)} q_2^{(t)})$ is monotone on $\mathbb{N}$, where
$(q_1 q_2)(a, b) = q_1(a) q_2(b)$ and
$\mathrm{ELBO}(p, q) = \sum_{z} q(z) (\log p(z) - \log q(z))$.

Here $\log$ is the real logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$.

Formalized by `Cslib.MachineLearning.Variational.elbo_iterate_sweep_monotone`, a theorem declared in [CSLibExt/MachineLearning/Variational/MeanField.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Variational/MeanField.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html#elbo-iterate-sweep-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mean-field variational inference](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mean-field-variational-inference)
