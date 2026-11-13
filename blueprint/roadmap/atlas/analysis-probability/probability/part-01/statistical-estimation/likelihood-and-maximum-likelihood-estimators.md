---
declaration: section
origin: cited
lean: ProbabilityTheory.NormalizedDensityFamily, ProbabilityTheory.NormalizedDensityFamily.ext, ProbabilityTheory.NormalizedDensityFamily.law, ProbabilityTheory.NormalizedDensityFamily.isProbabilityMeasure_law, ProbabilityTheory.NormalizedDensityFamily.iidLikelihood, ProbabilityTheory.NormalizedDensityFamily.iidLikelihood_nil, ProbabilityTheory.NormalizedDensityFamily.IsMaximumLikelihoodEstimator, ProbabilityTheory.NormalizedDensityFamily.isMaximumLikelihoodEstimator_iff
statement: formalized
proof: formalized
---

# Likelihood and maximum likelihood estimators

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html).

## Probability Theory

## Normalized density family

Let $\Omega$ be a measurable space with a measure $\mu$ and
let $\Theta$ be a set of parameters. A normalized density family on $\Omega$ indexed by $\Theta$
with dominating measure $\mu$ consists of a function $f_\theta : \Omega \to [0, \infty]$ for
each $\theta \in \Theta$ such that $f_\theta$ is $\mu$-almost everywhere measurable and
$\int_\Omega f_\theta \, d\mu = 1$.

Taking $\mu$ to be counting measure gives probability mass functions, and taking $\mu$ to be
volume gives probability density functions. The densities may take the value $\infty$.

Formalized by `ProbabilityTheory.NormalizedDensityFamily`, a structure declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#normalized-density-family).

## Normalized density families are determined by their densities

Let $F$ and $G$ be
normalized density families on a measurable space $\Omega$ with the same parameter set
$\Theta$ and the same dominating measure $\mu$. If for every $\theta \in \Theta$ and every
$x \in \Omega$ the density of $F$ at $\theta$ and the density of $G$ at $\theta$ take the same
value at $x$, then $F = G$.

Only the densities are compared; the measurability and normalization conditions are
propositions.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.ext`, a theorem declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#ext).

## Population law

Let $F$ be a normalized density family on a measurable space $\Omega$
with parameter set $\Theta$, dominating measure $\mu$ and densities $f_\theta$. The population
law at $\theta \in \Theta$ is the measure $P_\theta$ on $\Omega$ with density $f_\theta$ with
respect to $\mu$, so that $P_\theta(A) = \int_A f_\theta \, d\mu$ for every measurable set
$A \subseteq \Omega$.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.law`, a definition declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#law).

## Population laws are probability measures

Let $F$ be a normalized density family on
$\Omega$ with parameter set $\Theta$, dominating measure $\mu$ and densities $f_\theta$. For
every $\theta \in \Theta$, the population law $P_\theta$, the measure with density $f_\theta$
with respect to $\mu$, is a probability measure.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.isProbabilityMeasure_law`, a theorem declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#is-probability-measure-law).

## Likelihood of an iid sample

Let $F$ be a normalized density family on $\Omega$ with
parameter set $\Theta$ and densities $f_\theta$ for $\theta \in \Theta$. For a sample size $n$,
a parameter $\theta \in \Theta$ and a sample $x = (x_0, \dots, x_{n-1}) \in \Omega^n$, the iid
likelihood of $\theta$ at $x$ is $L_n(\theta; x) = \prod_{i < n} f_\theta(x_i)$, a value in
$[0, \infty]$. For $n = 0$ this is the empty product $1$.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.iidLikelihood`, a definition declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#iid-likelihood).

## Likelihood of the empty sample

For a normalized density family $F$, every parameter
$\theta$ and the empty sample $x$ (sample size $n = 0$), the iid likelihood of $\theta$ at $x$
equals $1$, the empty product.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.iidLikelihood_nil`, a theorem declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#iid-likelihood-nil).

## Maximum likelihood estimator

Let $F$ be a normalized density family on $\Omega$ with
parameter set $\Theta$, let $n$ be a sample size, and let $L_n(\theta; x)$ denote the iid
likelihood of $\theta \in \Theta$ at a sample $x \in \Omega^n$. A map $\hat\theta$ from
$\Omega^n$ to $\Theta$ is a maximum likelihood estimator for samples of size $n$ if for every
sample $x \in \Omega^n$ the parameter $\hat\theta(x)$ maximizes $\theta \mapsto L_n(\theta; x)$
over all of $\Theta$.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.IsMaximumLikelihoodEstimator`, a definition declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#is-maximum-likelihood-estimator).

## Characterization of maximum likelihood estimators

Let $F$ be a normalized density
family on $\Omega$ with parameter set $\Theta$, let $n$ be a sample size, let $L_n(\theta; x)$
denote the iid likelihood of $\theta \in \Theta$ at a sample $x \in \Omega^n$, and let
$\hat\theta$ be a map from $\Omega^n$ to $\Theta$. Then $\hat\theta$ is a maximum likelihood
estimator for samples of size $n$ if and only if $L_n(\theta; x) \le L_n(\hat\theta(x); x)$
for every sample $x \in \Omega^n$ and every $\theta \in \Theta$.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.isMaximumLikelihoodEstimator_iff`, a theorem declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#is-maximum-likelihood-estimator-iff).

## Induced likelihood

Let $F$ be a normalized density family on $\Omega$ with parameter
set $\Theta$, let $n$ be a sample size, let $\tau : \Theta \to H$ be a map into a set $H$, and
let $x \in \Omega^n$ be a sample. For $\eta$ in the image of $\tau$, the induced likelihood of
$\eta$ at $x$ is the supremum, in $[0, \infty]$, of the iid likelihood $L_n(\theta; x)$ over
the fiber of $\tau$ above $\eta$:

$$L^*_n(\eta; x) = \sup_{\theta \in \Theta,\ \tau(\theta) = \eta} L_n(\theta; x).$$

Since $\eta$ lies in the image of $\tau$, the fiber is nonempty; no inverse of $\tau$ is
chosen.

Formalized by `ProbabilityTheory.NormalizedDensityFamily.inducedLikelihood`, a definition declared in [MathlibExt/Probability/Statistics/Likelihood.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Likelihood.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html#induced-likelihood).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Likelihood and maximum likelihood estimators](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/statistical-estimation/likelihood-and-maximum-likelihood-estimators)
