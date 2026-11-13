---
declaration: section
origin: cited
lean: ProbabilityTheory.lintegral_Ioo_rpow_mul_rpow, ProbabilityTheory.dirichletDensity, ProbabilityTheory.multiBeta, ProbabilityTheory.lintegral_dirichletDensity_zero, ProbabilityTheory.lintegral_fin_succ, ProbabilityTheory.lintegral_comp_smul_fin, ProbabilityTheory.dirichletDensity_cons_smul, ProbabilityTheory.lintegral_dirichletDensity
statement: formalized
proof: formalized
---

# Dirichlet distribution

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html).

## The Beta integral

For real numbers $a > 0$ and $b > 0$, the integral over the open
interval $(0, 1)$, taken as a Lebesgue integral with values in $[0, \infty]$, is

$$\int_0^1 t^{a-1} (1 - t)^{b-1} \, dt = B(a, b),$$

where $B(a, b) = \Gamma(a) \Gamma(b) / \Gamma(a + b)$ is the Beta function.

Formalized by `ProbabilityTheory.lintegral_Ioo_rpow_mul_rpow`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-ioo-rpow-mul-rpow).

## Unnormalized Dirichlet density

For parameters
$\alpha = (\alpha_0, \dots, \alpha_n) \in \mathbb{R}^{n+1}$, the unnormalized Dirichlet density is
the function $D_\alpha \colon \mathbb{R}^n \to [0, \infty]$ defined by

$$D_\alpha(x) = \Bigl(\prod_{i=0}^{n-1} x_i^{\alpha_i - 1}\Bigr)
\Bigl(1 - \sum_{i=0}^{n-1} x_i\Bigr)^{\alpha_n - 1}$$

when $x$ lies in the open corner simplex, that is $x_i > 0$ for every $i$ and
$\sum_{i=0}^{n-1} x_i < 1$, and by $D_\alpha(x) = 0$ otherwise.

Here $x$ stands for the first $n$ coordinates of the probability vector
$(x_0, \dots, x_{n-1}, 1 - \sum_{i=0}^{n-1} x_i)$.

Formalized by `ProbabilityTheory.dirichletDensity`, a definition declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#dirichlet-density).

## Multivariate Beta function

For real parameters
$\alpha = (\alpha_0, \dots, \alpha_{n-1})$, the multivariate Beta function is

$$B(\alpha) = \frac{\prod_{i=0}^{n-1} \Gamma(\alpha_i)}{\Gamma(\sum_{i=0}^{n-1} \alpha_i)}.$$

It is the normalizing constant of the Dirichlet distribution.

Formalized by `ProbabilityTheory.multiBeta`, a definition declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#multi-beta).

## The Dirichlet integral for a single parameter

Let $\alpha = (\alpha_0) \in \mathbb{R}^1$
with $\alpha_0 > 0$, let $D_\alpha$ be the unnormalized Dirichlet density with parameters
$\alpha$, a function on $\mathbb{R}^0$, and let $B(\alpha)$ be the multivariate Beta function.
Then $\int_{\mathbb{R}^0} D_\alpha(x) \, dx = B(\alpha)$, the integral being taken with respect to
Lebesgue measure.

Both sides equal $1$: $\mathbb{R}^0$ is a single point of measure $1$, $D_\alpha$ equals $1$ there,
and $B(\alpha) = \Gamma(\alpha_0) / \Gamma(\alpha_0)$.

Formalized by `ProbabilityTheory.lintegral_dirichletDensity_zero`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-dirichlet-density-zero).

## Tonelli's theorem for the first coordinate

Let $G \colon \mathbb{R}^{n+1} \to [0, \infty]$
be measurable. Then

$$\int_{\mathbb{R}^{n+1}} G(x) \, dx = \int_{\mathbb{R}} \int_{\mathbb{R}^n} G(t, y) \, dy \, dt$$

where $(t, y) \in \mathbb{R}^{n+1}$ denotes the vector with first coordinate $t$ followed by the
coordinates of $y$, and all integrals are taken with respect to Lebesgue measure.

Formalized by `ProbabilityTheory.lintegral_fin_succ`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-fin-succ).

## Scaling the variable of a Lebesgue integral

Let $F \colon \mathbb{R}^n \to [0, \infty]$ be
measurable and let $c > 0$ be a real number. Then

$$\int_{\mathbb{R}^n} F(y) \, dy = c^n \int_{\mathbb{R}^n} F(c u) \, du$$

where both integrals are taken with respect to Lebesgue measure.

Formalized by `ProbabilityTheory.lintegral_comp_smul_fin`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-comp-smul-fin).

## Splitting off the first coordinate of the Dirichlet density

Let
$\alpha = (\alpha_0, \dots, \alpha_{n+1}) \in \mathbb{R}^{n+2}$, write $D_\alpha$ for the
unnormalized Dirichlet density with parameters $\alpha$ (a function on $\mathbb{R}^{n+1}$), and let
$\alpha' = (\alpha_1, \dots, \alpha_{n+1}) \in \mathbb{R}^{n+1}$. For every real $t$ with
$0 < t < 1$ and every $u \in \mathbb{R}^n$,

$$D_\alpha(t, (1 - t) u) = t^{\alpha_0 - 1} (1 - t)^{\alpha_1 + \dots + \alpha_{n+1} - 1 - n}
D_{\alpha'}(u)$$

where $(t, (1 - t) u) \in \mathbb{R}^{n+1}$ is the vector with first coordinate $t$ followed by the
coordinates of $(1 - t) u$.

Formalized by `ProbabilityTheory.dirichletDensity_cons_smul`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#dirichlet-density-cons-smul).

## The Dirichlet integral

Let $\alpha = (\alpha_0, \dots, \alpha_n) \in \mathbb{R}^{n+1}$ with
$\alpha_i > 0$ for every $i$, and let
$\Delta = \{x \in \mathbb{R}^n : x_i > 0 \text{ for all } i \text{ and } \sum_{i=0}^{n-1} x_i < 1\}$
be the open corner simplex. Then

$$\int_{\Delta} \Bigl(\prod_{i=0}^{n-1} x_i^{\alpha_i - 1}\Bigr)
\Bigl(1 - \sum_{i=0}^{n-1} x_i\Bigr)^{\alpha_n - 1} dx =
\frac{\prod_{i=0}^{n} \Gamma(\alpha_i)}{\Gamma\bigl(\sum_{i=0}^{n} \alpha_i\bigr)},$$

where $dx$ is Lebesgue measure. Equivalently, the integral of the unnormalized Dirichlet density
$D_\alpha$ over $\mathbb{R}^n$ equals the multivariate Beta function $B(\alpha)$.

Formalized by `ProbabilityTheory.lintegral_dirichletDensity`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-dirichlet-density).

## Simplex completion

For $x = (x_0, \dots, x_{n-1}) \in \mathbb{R}^n$, the simplex
completion of $x$ is the vector
$(x_0, \dots, x_{n-1}, 1 - \sum_{i=0}^{n-1} x_i) \in \mathbb{R}^{n+1}$, whose coordinates sum
to $1$.

Formalized by `ProbabilityTheory.simplexCompletion`, a definition declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#simplex-completion).

## Dirichlet distribution

Let $\alpha = (\alpha_0, \dots, \alpha_n) \in \mathbb{R}^{n+1}$, let
$D_\alpha$ be the unnormalized Dirichlet density on $\mathbb{R}^n$ with parameters $\alpha$, and let
$B(\alpha) = \prod_{i=0}^{n} \Gamma(\alpha_i) / \Gamma(\sum_{i=0}^{n} \alpha_i)$ be the
multivariate Beta function. The Dirichlet distribution $\mathrm{Dir}(\alpha)$ is the measure on
$\mathbb{R}^{n+1}$ obtained by pushing forward the measure on $\mathbb{R}^n$ with density
$D_\alpha(x) / B(\alpha)$ with respect to Lebesgue measure along the map
$x \mapsto (x_0, \dots, x_{n-1}, 1 - \sum_{i=0}^{n-1} x_i)$.

The quotient is taken in $[0, \infty]$, with a nonpositive $B(\alpha)$ read as $0$; this matters
only when some $\alpha_i \le 0$. For positive parameters $\mathrm{Dir}(\alpha)$ is a probability
measure concentrated on vectors with positive entries summing to $1$.

Formalized by `ProbabilityTheory.dirichletMeasure`, a definition declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#dirichlet-measure).

## The Dirichlet distribution is concentrated on the open simplex

For every $n$ and every
parameter vector $\alpha \in \mathbb{R}^{n+1}$, almost every $\theta \in \mathbb{R}^{n+1}$ with
respect to the Dirichlet distribution $\mathrm{Dir}(\alpha)$ is a probability vector with positive
entries: $\theta_i > 0$ for every $i$ and $\sum_{i=0}^{n} \theta_i = 1$.

Formalized by `ProbabilityTheory.ae_dirichletMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#ae-dirichlet-measure).

## Multiplying the Dirichlet density by a multinomial likelihood

Let
$\alpha = (\alpha_0, \dots, \alpha_n) \in \mathbb{R}^{n+1}$ and let $k = (k_0, \dots, k_n)$ be
natural numbers; write $D_\beta$ for the unnormalized Dirichlet density with parameters $\beta$.
For every $x \in \mathbb{R}^n$, let $\theta = (x_0, \dots, x_{n-1}, 1 - \sum_{i=0}^{n-1} x_i)$ be
its completion to a vector summing to $1$, and write $\theta_i^+ = \max(\theta_i, 0)$. Then

$$D_\alpha(x) \prod_{i=0}^{n} (\theta_i^+)^{k_i} = D_{\alpha + k}(x).$$

Both sides vanish unless $x$ lies in the open corner simplex, where every $\theta_i$ is positive and
$\theta_i^+ = \theta_i$.

Formalized by `ProbabilityTheory.dirichletDensity_mul_prod_pow`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#dirichlet-density-mul-prod-pow).

## Dirichlet–multinomial conjugacy

Let $\alpha = (\alpha_0, \dots, \alpha_n)$ have positive
real entries and let $k = (k_0, \dots, k_n)$ be natural numbers (counts). The measure with density
$\theta \mapsto \prod_{i=0}^{n} \max(\theta_i, 0)^{k_i}$ with respect to the Dirichlet distribution
$\mathrm{Dir}(\alpha)$, that is, $\mathrm{Dir}(\alpha)$ weighted by the likelihood of the counts
$k$, equals

$$\frac{B(\alpha + k)}{B(\alpha)} \, \mathrm{Dir}(\alpha + k),$$

where $B$ is the multivariate Beta function and $\alpha + k$ is taken entrywise.

Formalized by `ProbabilityTheory.withDensity_prod_pow_dirichletMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#with-density-prod-pow-dirichlet-measure).

## Mean of the Dirichlet distribution

Let
$\alpha = (\alpha_0, \dots, \alpha_n) \in \mathbb{R}^{n+1}$ with $\alpha_j > 0$ for every $j$. For
every $i$, the $i$-th coordinate of a random vector $\theta$ with the Dirichlet distribution
$\mathrm{Dir}(\alpha)$ has mean

$$\mathbb{E}[\theta_i] = \frac{\alpha_i}{\sum_{j=0}^{n} \alpha_j}.$$

Formally the left side is the integral of $\max(\theta_i, 0)$ with respect to
$\mathrm{Dir}(\alpha)$; this is the mean of $\theta_i$ because $\theta_i > 0$ almost surely.

Formalized by `ProbabilityTheory.lintegral_dirichletMeasure_apply`, a theorem declared in [MathlibExt/Probability/Distributions/Dirichlet.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Dirichlet.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html#lintegral-dirichlet-measure-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dirichlet distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/dirichlet-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/continuous/dirichlet-distribution)
