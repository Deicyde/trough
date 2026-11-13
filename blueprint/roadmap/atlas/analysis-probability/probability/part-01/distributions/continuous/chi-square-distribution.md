---
declaration: section
origin: cited
lean: ProbabilityTheory.chiSquareMeasure, ProbabilityTheory.mgf_sq_stdGaussian, ProbabilityTheory.integrable_exp_mul_sq_stdGaussian, ProbabilityTheory.Iio_subset_integrableExpSet_map_sq_stdGaussian, ProbabilityTheory.mgf_id_map_sq_stdGaussian, ProbabilityTheory.mgf_gammaMeasure_half_half_eq_sqrt, ProbabilityTheory.mgf_chiSquareMeasure_of_lt, ProbabilityTheory.integrable_exp_mul_chiSquareMeasure
statement: formalized
proof: formalized
---

# Chi-square distribution

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html).

## Chi-square distribution

For a natural number $p$, the chi-square law with $p$ degrees of
freedom is the gamma law on $\mathbb{R}$ with shape $p/2$ and rate $1/2$ (equivalently, scale $2$):
the measure with density $x \mapsto \frac{(1/2)^{p/2}}{\Gamma(p/2)} x^{p/2 - 1} e^{-x/2}$ for
$x > 0$ and $0$ for $x < 0$ with respect to Lebesgue measure.

For $p = 0$ the definition is degenerate: $\Gamma(0)$ is taken to be $0$ and division by $0$ gives
$0$, so the density vanishes and the measure is the zero measure rather than a point mass.

Formalized by `ProbabilityTheory.chiSquareMeasure`, a definition declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#chi-square-measure).

## Moment generating function of the square of a standard normal

Let $\gamma$ be the
standard Gaussian measure on $\mathbb{R}$ (mean $0$, variance $1$). For every real $t$,
$\int_{\mathbb{R}} e^{t x^2} \, d\gamma(x) = 1/\sqrt{1 - 2t}$.

For $t \ge 1/2$ the integral diverges; the identity still holds there with the conventions that the
integral of a non-integrable function is $0$, that $\sqrt{s} = 0$ for $s \le 0$ and that $1/0 = 0$,
which make both sides $0$.

Formalized by `ProbabilityTheory.mgf_sq_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#mgf-sq-std-gaussian).

## Exponential moments of the square of a standard normal

Let $\gamma$ be the standard
Gaussian measure on $\mathbb{R}$ (mean $0$, variance $1$). For every real $t < 1/2$, the
function $x \mapsto e^{t x^2}$ is integrable with respect to $\gamma$.

Formalized by `ProbabilityTheory.integrable_exp_mul_sq_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#integrable-exp-mul-sq-std-gaussian).

## Exponential moments of the law of the square of a standard normal

Let $\gamma$ be the
standard Gaussian measure on $\mathbb{R}$ (mean $0$, variance $1$) and let $\nu$ be its image under
$x \mapsto x^2$. For every real $t < 1/2$, the function $y \mapsto e^{t y}$ is integrable with
respect to $\nu$.

Formalized by `ProbabilityTheory.Iio_subset_integrableExpSet_map_sq_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#iio-subset-integrable-exp-set-map-sq-std).

## Moment generating function of the law of the square of a standard normal

Let $\gamma$
be the standard Gaussian measure on $\mathbb{R}$ (mean $0$, variance $1$) and let $\nu$ be its
image under $x \mapsto x^2$. For every real $t$, $\int_{\mathbb{R}} e^{t y} \, d\nu(y) =
1/\sqrt{1 - 2t}$.

For $t \ge 1/2$ the integral diverges; the identity still holds there with the conventions that the
integral of a non-integrable function is $0$, that $\sqrt{s} = 0$ for $s \le 0$ and that $1/0 = 0$,
which make both sides $0$.

Formalized by `ProbabilityTheory.mgf_id_map_sq_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#mgf-id-map-sq-std-gaussian).

## Moment generating function of the gamma law with shape and rate one half

Let $\mu$ be the
gamma law on $\mathbb{R}$ with shape $1/2$ and rate $1/2$. For every real $t < 1/2$,
$\int_{\mathbb{R}} e^{t x} \, d\mu(x) = 1/\sqrt{1 - 2t}$.

This is the moment generating function of the square of a standard normal variable.

Formalized by `ProbabilityTheory.mgf_gammaMeasure_half_half_eq_sqrt`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#mgf-gamma-measure-half-half-eq-sqrt).

## Moment generating function of the chi-square distribution

Let $p$ be a positive integer
and let $\chi^2_p$ be the chi-square law with $p$ degrees of freedom. For every real $t < 1/2$,
$\int_{\mathbb{R}} e^{t x} \, d\chi^2_p(x) = \left(\frac{1/2}{1/2 - t}\right)^{p/2}$.

Formalized by `ProbabilityTheory.mgf_chiSquareMeasure_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#mgf-chi-square-measure-of-lt).

## Exponential moments of the chi-square distribution

Let $p$ be a positive integer and let
$\chi^2_p$ be the chi-square law with $p$ degrees of freedom. For every real $t < 1/2$, the
function $x \mapsto e^{t x}$ is integrable with respect to $\chi^2_p$.

Formalized by `ProbabilityTheory.integrable_exp_mul_chiSquareMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#integrable-exp-mul-chi-square-measure).

## The square of a standard normal variable is chi-square with one degree of freedom

**The square of a standard normal variable is chi-square with one degree of freedom**, as
an identity of measures on `ℝ`. (Moved here from the likelihood-ratio development so that
both that development and Cochran's theorem reuse one declaration.)

Formalized by `ProbabilityTheory.gaussianReal_map_sq`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#gaussian-real-map-sq).

## Chi-square moment generating functions multiply by adding degrees

Chi-square MGFs multiply by adding degrees, below `1/2`. Requires a
nonempty index set so the summed degree stays positive.

Formalized by `ProbabilityTheory.prod_mgf_chiSquareMeasure_eq_mgf_sum`, a theorem declared in [MathlibExt/Probability/Distributions/ChiSquare.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/ChiSquare.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html#prod-mgf-chi-square-measure-eq-mgf-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chi-square distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/chi-square-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/continuous/chi-square-distribution)
