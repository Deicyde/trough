---
declaration: section
origin: cited
lean: MathlibExt.Probability.pgf, MathlibExt.Probability.integrable_pow_of_abs_le_one, MathlibExt.Probability.pgf_one, MathlibExt.Probability.pgf_zero, MathlibExt.Probability.pgf_eq_tsum, MathlibExt.Probability.pgf_add_of_indepFun
statement: formalized
proof: formalized
---

# Probability generating functions

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html).

## Probability generating function

For a measure $\mu$ on $\Omega$ and a function
$X : \Omega \to \mathbb{N}$, the probability generating function of $X$ under $\mu$ is the function
$G_X : \mathbb{R} \to \mathbb{R}$ given by

$$G_X(s) = \int_\Omega s^{X(\omega)} \, d\mu(\omega),$$

which is the expectation $\mathbb{E}[s^X]$ when $\mu$ is a probability measure.

For a finite measure $\mu$ and measurable $X$ the integral converges whenever $|s| \le 1$. Where
$s^X$ is not integrable, the integral is taken to be $0$.

Formalized by `MathlibExt.Probability.pgf`, a definition declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#pgf).

## Integrability of $s^X$ for $|s| \le 1$

Let $\mu$ be a finite measure on $\Omega$, let
$X : \Omega \to \mathbb{N}$ be measurable, and let $s$ be a real number with $|s| \le 1$. Then the
function $\omega \mapsto s^{X(\omega)}$ is integrable with respect to $\mu$.

Formalized by `MathlibExt.Probability.integrable_pow_of_abs_le_one`, a theorem declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#integrable-pow-of-abs-le-one).

## The generating function at $s = 1$

For every probability measure $\mu$ on $\Omega$ and
every function $X : \Omega \to \mathbb{N}$, the probability generating function
$G_X(s) = \int_\Omega s^{X(\omega)} \, d\mu(\omega)$ of $X$ under $\mu$ satisfies $G_X(1) = 1$.

Formalized by `MathlibExt.Probability.pgf_one`, a theorem declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#pgf-one).

## The generating function at $s = 0$

Let $\mu$ be a measure on $\Omega$ and let
$X : \Omega \to \mathbb{N}$ be measurable. Then the probability generating function
$G_X(s) = \int_\Omega s^{X(\omega)} \, d\mu(\omega)$ of $X$ under $\mu$ satisfies
$G_X(0) = \mu(\lbrace \omega : X(\omega) = 0 \rbrace)$, where the measure of the event is read as
a real number, an infinite value being read as $0$.

When $\mu$ is a probability measure this is the probability that $X = 0$, and when $\mu$ is finite
it is the mass of that event.

Formalized by `MathlibExt.Probability.pgf_zero`, a theorem declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#pgf-zero).

## Series form of the probability generating function

Let $\mu$ be a finite measure on
$\Omega$, let $X : \Omega \to \mathbb{N}$ be measurable, and let $s$ be a real number with
$|s| \le 1$. Then the probability generating function
$G_X(s) = \int_\Omega s^{X(\omega)} \, d\mu(\omega)$ of $X$ under $\mu$ satisfies

$$G_X(s) = \sum_{k=0}^{\infty} s^k \, \mu(\{\omega \in \Omega : X(\omega) = k\}).$$

Formalized by `MathlibExt.Probability.pgf_eq_tsum`, a theorem declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#pgf-eq-tsum).

## Generating function of a sum of independent variables

Let $\mu$ be a finite measure on
$\Omega$, and for $Z : \Omega \to \mathbb{N}$ write
$G_Z(s) = \int_\Omega s^{Z(\omega)} \, d\mu(\omega)$ for the probability generating function of
$Z$ under $\mu$. If $X, Y : \Omega \to \mathbb{N}$ are measurable and independent under $\mu$,
then $G_{X+Y}(s) = G_X(s) \, G_Y(s)$ for every real $s$ with $|s| \le 1$.

Formalized by `MathlibExt.Probability.pgf_add_of_indepFun`, a theorem declared in [MathlibExt/Probability/ProbabilityGeneratingFunction.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityGeneratingFunction.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html#pgf-add-of-indep-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probability generating functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/probability-generating-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/characteristic-functions/probability-generating-functions)
