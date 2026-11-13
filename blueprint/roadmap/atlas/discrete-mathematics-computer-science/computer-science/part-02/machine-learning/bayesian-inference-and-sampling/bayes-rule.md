---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Bayesian.bayesPosterior, Cslib.MachineLearning.Bayesian.comp_apply_singleton, Cslib.MachineLearning.Bayesian.comp_mul_bayesPosterior, Cslib.MachineLearning.Bayesian.IsMLE, Cslib.MachineLearning.Bayesian.IsMAP, Cslib.MachineLearning.Bayesian.bayesKernel, Cslib.MachineLearning.Bayesian.posterior_eq_bayesPosterior, Cslib.MachineLearning.Bayesian.comp_apply_singleton_eq_tsum
statement: formalized
proof: formalized
---

# Bayes' rule

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html).

## Bayes posterior

Let $\kappa$ be a kernel from a measurable space $\Theta$ of hypotheses to
a measurable space $\mathcal X$ of observations (the likelihood) and $\mu$ a measure on $\Theta$
(the prior). The Bayes posterior after observing $x \in \mathcal X$ is the measure $\pi_x$ on
$\Theta$ with

$$\pi_x(s) = E(x)^{-1} \int_s \kappa_\theta(\{x\}) \, d\mu(\theta)$$

for every measurable $s \subseteq \Theta$, where $E(x) = (\kappa \circ \mu)(\{x\})$ is the evidence
of $x$: the mass of $\{x\}$ under the composition $\kappa \circ \mu$ of $\mu$ with $\kappa$, the
marginal law of the observation. The inverse is taken in $[0, \infty]$, with $0^{-1} = \infty$,
$\infty^{-1} = 0$ and $\infty \cdot 0 = 0$; in particular $\pi_x$ is the zero measure when the
evidence is zero.

Formalized by `Cslib.MachineLearning.Bayesian.bayesPosterior`, a definition declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#bayes-posterior).

## The evidence is the integral of the likelihood

Let $\kappa$ be a kernel from a measurable
space $\Theta$ to a measurable space $\mathcal X$ with measurable singletons, and $\mu$ a measure on
$\Theta$. For every $x \in \mathcal X$,

$$(\kappa \circ \mu)(\{x\}) = \int_\Theta \kappa_\theta(\{x\}) \, d\mu(\theta),$$

where $\kappa \circ \mu$ is the composition of $\mu$ with $\kappa$ (the marginal law of the
observation) and the right side is the Lebesgue integral of a $[0, \infty]$-valued function.

Formalized by `Cslib.MachineLearning.Bayesian.comp_apply_singleton`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#comp-apply-singleton).

## Evidence times posterior is the joint mass

Let $\mathcal X$ be a measurable space with
measurable singletons, $\kappa$ a Markov kernel from a measurable space $\Theta$ to $\mathcal X$
and $\mu$ a finite measure on $\Theta$. Let $x \in \mathcal X$ and write $\pi_x$ for the Bayes
posterior of $\mu$ after observing $x$ under $\kappa$. Then for every measurable set
$s \subseteq \Theta$,

$$(\kappa \circ \mu)(\{x\}) \cdot \pi_x(s) = \int_s \kappa_\theta(\{x\}) \, d\mu(\theta),$$

where $\kappa \circ \mu$ is the composition of $\mu$ with $\kappa$, so that the first factor is the
evidence of $x$.

Formalized by `Cslib.MachineLearning.Bayesian.comp_mul_bayesPosterior`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#comp-mul-bayes-posterior).

## Maximum-likelihood hypothesis for a discrete observation

Let $\kappa$ be a kernel from a
parameter space $\Theta$ to a countable observation space $\mathcal X$ with measurable singletons,
assigning to each hypothesis $\theta$ a measure $\kappa_\theta$ on $\mathcal X$. A hypothesis
$\theta \in \Theta$ is a maximum-likelihood hypothesis for the observation $x \in \mathcal X$ when
no hypothesis gives $x$ higher likelihood: $\kappa_{\theta'}(\{x\}) \le \kappa_\theta(\{x\})$ for
every $\theta' \in \Theta$.

Formalized by `Cslib.MachineLearning.Bayesian.IsMLE`, a definition declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#is-mle).

## Maximum a posteriori hypothesis

Let $\Theta$ and $\mathcal X$ be countable measurable
spaces with measurable singletons, $\kappa$ a kernel from $\Theta$ to $\mathcal X$ and $\mu$ a
measure on $\Theta$, and write $\pi_x$ for the Bayes posterior of the prior $\mu$ after observing
$x \in \mathcal X$ under the likelihood $\kappa$. A hypothesis $\theta \in \Theta$ is a maximum a
posteriori (MAP) hypothesis for $x$ when $\pi_x(\{\theta'\}) \le \pi_x(\{\theta\})$ for every
$\theta' \in \Theta$.

Formalized by `Cslib.MachineLearning.Bayesian.IsMAP`, a definition declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#is-map).

## Bayes posterior kernel

Let $\mathcal X$ be a countable measurable space with measurable
singletons, $\kappa$ a kernel from a measurable space $\Theta$ to $\mathcal X$, and $\mu$ a measure
on $\Theta$. The Bayes posterior kernel is the kernel from $\mathcal X$ to $\Theta$ that sends each
observation $x \in \mathcal X$ to the Bayes posterior of the prior $\mu$ after observing $x$ under
the likelihood $\kappa$.

Formalized by `Cslib.MachineLearning.Bayesian.bayesKernel`, a definition declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#bayes-kernel).

## Bayes' rule for discrete observations

Let the parameter space $\Theta$ be a nonempty
standard Borel space and the observation space $\mathcal X$ be countable with measurable
singletons. Let $\kappa$ be a Markov kernel from $\Theta$ to $\mathcal X$ (the likelihood),
writing $\kappa_\theta$ for the probability measure it assigns to $\theta \in \Theta$, let $\mu$
be a finite measure on $\Theta$ (the prior), and let $\kappa^\dagger\mu$ be Mathlib's posterior
kernel from $\mathcal X$ to $\Theta$. If the observation $x \in \mathcal X$ has nonzero evidence
$(\kappa \circ \mu)(\{x\})$, where $\kappa \circ \mu$ is the law of the observation under the
prior, then the posterior measure $\kappa^\dagger\mu(x)$ equals the Bayes posterior after
observing $x$: the prior $\mu$ reweighted by the likelihood $\theta \mapsto \kappa_\theta(\{x\})$
and divided by the evidence.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_eq_bayesPosterior`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#posterior-eq-bayes-posterior).

## The evidence as a sum over hypotheses

Let $\Theta$ be a countable measurable space and
$\mathcal X$ a measurable space, both with measurable singletons, let $\kappa$ be a kernel from
$\Theta$ to $\mathcal X$ and $\mu$ a measure on $\Theta$. For every $x \in \mathcal X$,

$$(\kappa \circ \mu)(\{x\}) = \sum_{\theta \in \Theta} \mu(\{\theta\}) \, \kappa_\theta(\{x\}),$$

where $\kappa \circ \mu$ is the composition of $\mu$ with $\kappa$ (the marginal law of the
observation) and the sum is taken in $[0, \infty]$.

Formalized by `Cslib.MachineLearning.Bayesian.comp_apply_singleton_eq_tsum`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#comp-apply-singleton-eq-tsum).

## Bayes' rule for countably many hypotheses

Let $\Theta$ be a countable measurable space and
$\mathcal X$ a measurable space, both with measurable singletons, let $\kappa$ be a kernel from
$\Theta$ to $\mathcal X$ (the likelihood) and $\mu$ a measure on $\Theta$ (the prior). For every
observation $x \in \mathcal X$ and every $\theta \in \Theta$, the Bayes posterior $\pi_x$ of $\mu$
after observing $x$ satisfies

$$\pi_x(\{\theta\}) = \frac{\mu(\{\theta\}) \, \kappa_\theta(\{x\})}
{\sum_{\theta' \in \Theta} \mu(\{\theta'\}) \, \kappa_{\theta'}(\{x\})},$$

where the quotient is taken in $[0, \infty]$ with $0 / 0 = 0$ and $a / \infty = 0$ for every $a$.
The denominator is the evidence of $x$.

Formalized by `Cslib.MachineLearning.Bayesian.bayesPosterior_apply_singleton`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#bayes-posterior-apply-singleton).

## Bayes' rule for Mathlib's posterior kernel with countably many hypotheses and observations

**Bayes' rule for Mathlib's posterior kernel with countably many hypotheses and
observations.** Let the parameter space $\Theta$ be a nonempty countable standard Borel space and
the observation space $\mathcal X$ be countable, both with measurable singletons. Let $\kappa$ be
a Markov kernel from $\Theta$ to $\mathcal X$ (the likelihood), writing $\kappa_\theta$ for the
probability measure it assigns to $\theta \in \Theta$, let $\mu$ be a finite measure on $\Theta$
(the prior), and let $\kappa^\dagger\mu$ be Mathlib's posterior kernel from $\mathcal X$ to
$\Theta$. If the observation $x \in \mathcal X$ has nonzero evidence $(\kappa \circ \mu)(\{x\})$,
where $\kappa \circ \mu$ is the law of the observation under the prior, then for every
$\theta \in \Theta$

$$
\kappa^\dagger\mu(x)(\{\theta\}) = \frac{\mu(\{\theta\})\,\kappa_\theta(\{x\})}
{\sum_{\theta' \in \Theta} \mu(\{\theta'\})\,\kappa_{\theta'}(\{x\})}.
$$

Formalized by `Cslib.MachineLearning.Bayesian.posterior_apply_singleton`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#posterior-apply-singleton).

## MAP hypotheses maximize prior times likelihood

Let $\Theta$ and $\mathcal X$ be countable
measurable spaces with measurable singletons, $\kappa$ a Markov kernel from $\Theta$ to
$\mathcal X$, $\mu$ a finite measure on $\Theta$, and $x \in \mathcal X$ an observation with
$(\kappa \circ \mu)(\{x\}) \neq 0$, where $\kappa \circ \mu$ is the composition of $\mu$ with
$\kappa$. Then $\theta \in \Theta$ is a MAP hypothesis for $x$ under the prior $\mu$ and the
likelihood $\kappa$ if and only if
$\mu(\{\theta'\}) \, \kappa_{\theta'}(\{x\}) \le \mu(\{\theta\}) \, \kappa_\theta(\{x\})$ for every
$\theta' \in \Theta$.

The evidence $(\kappa \circ \mu)(\{x\})$ is a common factor of all posterior masses.

Formalized by `Cslib.MachineLearning.Bayesian.isMAP_iff`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#is-map-iff).

## Under a uniform prior, MAP is maximum likelihood

Let $\Theta$ and $\mathcal X$ be countable
measurable spaces with measurable singletons, $\kappa$ a Markov kernel from $\Theta$ to
$\mathcal X$, and $\mu$ a finite measure on $\Theta$ that is uniform: there is $c \in [0, \infty]$,
$c \neq 0$, with $\mu(\{\theta\}) = c$ for every $\theta \in \Theta$. Let $x \in \mathcal X$ be an
observation with $(\kappa \circ \mu)(\{x\}) \neq 0$, where $\kappa \circ \mu$ is the composition of
$\mu$ with $\kappa$. Then a hypothesis $\theta \in \Theta$ is a MAP hypothesis for $x$ under the
prior $\mu$ and the likelihood $\kappa$ if and only if it is a maximum-likelihood hypothesis for
$x$ under $\kappa$.

Formalized by `Cslib.MachineLearning.Bayesian.isMAP_iff_isMLE_of_uniform`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#is-map-iff-is-mle-of-uniform).

## MAP hypotheses through the posterior kernel

Let $\Theta$ be a nonempty countable standard
Borel space, $\mathcal X$ a countable measurable space with measurable singletons, $\kappa$ a Markov
kernel from $\Theta$ to $\mathcal X$, $\mu$ a finite measure on $\Theta$, and $x \in \mathcal X$ an
observation with $(\kappa \circ \mu)(\{x\}) \neq 0$, where $\kappa \circ \mu$ is the composition of
$\mu$ with $\kappa$. Write $\kappa^\dagger_\mu$ for the posterior kernel from $\mathcal X$ to
$\Theta$, the fixed disintegration of the joint law of hypothesis and observation along the
observation. Then $\theta \in \Theta$ is a MAP hypothesis for $x$ under the prior $\mu$ and the
likelihood $\kappa$ if and only if
$\kappa^\dagger_\mu(x)(\{\theta'\}) \le \kappa^\dagger_\mu(x)(\{\theta\})$ for every
$\theta' \in \Theta$.

Formalized by `Cslib.MachineLearning.Bayesian.isMAP_iff_posterior`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Basic.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Basic.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#is-map-iff-posterior).

## The evidence from a factorization of densities

Let $\nu$ be an s-finite measure on a
measurable space $\Theta$ and $\rho$ an s-finite measure on a measurable space $\mathcal{X}$. Let
$p : \Theta \to [0, \infty]$, $q : \Theta \times \mathcal{X} \to [0, \infty]$,
$c : \mathcal{X} \to [0, \infty]$ and $r : \mathcal{X} \times \Theta \to [0, \infty]$ be measurable
functions such that $\int r(x, \theta) \, d\nu(\theta) = 1$ for every $x \in \mathcal{X}$ and
$p(\theta) \, q(\theta, x) = c(x) \, r(x, \theta)$ for all $\theta \in \Theta$ and
$x \in \mathcal{X}$. If the prior $\mu$ is the measure on $\Theta$ with density $p$ with respect
to $\nu$, and the likelihood $\kappa$ is a kernel from $\Theta$ to $\mathcal{X}$ such that each
$\kappa(\theta)$ has density $q(\theta, \cdot)$ with respect to $\rho$, then the marginal law of
the data, the measure $\kappa \circ \mu$ on $\mathcal{X}$ given by
$(\kappa \circ \mu)(s) = \int \kappa(\theta)(s) \, d\mu(\theta)$ for measurable $s$, has density
$c$ with respect to $\rho$.

Formalized by `Cslib.MachineLearning.Bayesian.comp_eq_withDensity_of_mul_eq`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Density.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Density.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#comp-eq-with-density-of-mul-eq).

## Disintegration of the joint law from a factorization of densities

Let $\nu$ be an
s-finite measure on a measurable space $\Theta$ and $\rho$ an s-finite measure on a measurable
space $\mathcal{X}$. Let $p : \Theta \to [0, \infty]$,
$q : \Theta \times \mathcal{X} \to [0, \infty]$, $c : \mathcal{X} \to [0, \infty]$ and
$r : \mathcal{X} \times \Theta \to [0, \infty]$ be measurable functions such that
$\int r(x, \theta) \, d\nu(\theta) = 1$ for every $x \in \mathcal{X}$ and
$p(\theta) \, q(\theta, x) = c(x) \, r(x, \theta)$ for all $\theta \in \Theta$ and
$x \in \mathcal{X}$. Let the prior $\mu$ be an s-finite measure on $\Theta$ with density $p$ with
respect to $\nu$, let the likelihood $\kappa$ be an s-finite kernel from $\Theta$ to $\mathcal{X}$
such that each $\kappa(\theta)$ has density $q(\theta, \cdot)$ with respect to $\rho$, and let
$\eta$ be an s-finite kernel from $\mathcal{X}$ to $\Theta$ such that each $\eta(x)$ has density
$r(x, \cdot)$ with respect to $\nu$. Write $\kappa \circ \mu$ for the marginal law of the data,
$(\kappa \circ \mu)(s) = \int \kappa(\theta)(s) \, d\mu(\theta)$, and $\mu \otimes \kappa$ for the
joint law on $\Theta \times \mathcal{X}$,
$(\mu \otimes \kappa)(t) = \int \kappa(\theta)(\{x : (\theta, x) \in t\}) \, d\mu(\theta)$, and
similarly $(\kappa \circ \mu) \otimes \eta$ on $\mathcal{X} \times \Theta$. Then
$(\kappa \circ \mu) \otimes \eta$ is the image of $\mu \otimes \kappa$ under the swap
$(\theta, x) \mapsto (x, \theta)$.

Formalized by `Cslib.MachineLearning.Bayesian.compProd_eq_of_mul_eq`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Density.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Density.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#comp-prod-eq-of-mul-eq).

## Bayes' rule for densities

Let $\Theta$ be a nonempty standard Borel space, $\nu$ an
s-finite measure on $\Theta$ and $\rho$ an s-finite measure on a measurable space $\mathcal{X}$.
Let $p : \Theta \to [0, \infty]$, $q : \Theta \times \mathcal{X} \to [0, \infty]$,
$c : \mathcal{X} \to [0, \infty]$ and $r : \mathcal{X} \times \Theta \to [0, \infty]$ be measurable
functions such that $\int r(x, \theta) \, d\nu(\theta) = 1$ for every $x \in \mathcal{X}$ and
$p(\theta) \, q(\theta, x) = c(x) \, r(x, \theta)$ for all $\theta \in \Theta$ and
$x \in \mathcal{X}$. Let the prior $\mu$ be a finite measure on $\Theta$ with density $p$ with
respect to $\nu$, and let the likelihood $\kappa$ be a Markov kernel from $\Theta$ to
$\mathcal{X}$ such that each $\kappa(\theta)$ has density $q(\theta, \cdot)$ with respect to
$\rho$. Then for almost every $x$ with respect to the marginal law of the data
$\kappa \circ \mu$, given by $(\kappa \circ \mu)(s) = \int \kappa(\theta)(s) \, d\mu(\theta)$, the
posterior $\kappa^\dagger_\mu(x)$ of $\kappa$ with respect to $\mu$ is the measure with density
$r(x, \cdot)$ with respect to $\nu$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_ae_eq_of_mul_eq`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/Density.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/Density.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html#posterior-ae-eq-of-mul-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayes' rule](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayes-rule)
