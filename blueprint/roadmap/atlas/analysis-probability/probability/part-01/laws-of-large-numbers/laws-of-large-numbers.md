---
declaration: section
origin: cited
lean: MathlibExt.Probability.KolmogorovMaximal.kolmogorov_maximal_inequality, MathlibExt.MeasureTheory.MeanZeroSumDeviationMeasureWanted.tendsto_volume_abs_sum_ge_mul_sqrt, MathlibExt.Probability.variance_sample_mean_of_iid
statement: formalized
---

# Laws of large numbers and random series: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/index.html).

Almost-sure behaviour of sums of independent variables: strong and weak laws of large numbers, Kolmogorov's three-series theorem and maximal inequality, truncation techniques, the law of the iterated logarithm, and the Monte Carlo variance rate of sample means.

## Kolmogorov's maximal inequality for finitely-valued variables

Let $\alpha$ be a finite
nonempty set and $n \in \mathbb{N}$. For each $i \in \{0, \dots, n-1\}$ let $p_i$ be a probability
vector on $\alpha$, so $p_i(a) \ge 0$ and $\sum_{a \in \alpha} p_i(a) = 1$, and let
$X_i : \alpha \to \mathbb{R}$ satisfy $\sum_{a \in \alpha} p_i(a) X_i(a) = 0$. Give each
$\omega \in \alpha^n$ the weight $\prod_{i=0}^{n-1} p_i(\omega_i)$, so that the coordinates are
independent with laws $p_i$. Then for every real $\lambda > 0$, the total weight of the $\omega$
for which $\bigl|\sum_{j \le i} X_j(\omega_j)\bigr| \ge \lambda$ for some $i$ is at most
$\lambda^{-2} \sum_{i=0}^{n-1} \sum_{a \in \alpha} p_i(a) X_i(a)^2$.

## Sources

- A. Kolmogoroff, "Über die Summen durch den Zufall bestimmter unabhängiger Größen", Math. Ann. 99 (1928), 309–319, DOI 10.1007/BF01459098.

Formalized by `MathlibExt.Probability.KolmogorovMaximal.kolmogorov_maximal_inequality`, a theorem declared in [MathlibExt/Probability/KolmogorovMaximal.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovMaximal.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/index.html#kolmogorov-maximal-inequality).

## Large deviations of mean-zero sums on the cube have vanishing measure

Let
$f : \mathbb{R} \to \mathbb{R}$ be square integrable on $[0,1]$ with $\int_0^1 f = 0$ and
$\int_0^1 |f|^2 > 0$, and let $(a_n)_{n \in \mathbb{N}}$ be a sequence of positive reals with
$a_n \to \infty$. For each $n$ let

$$F_n = \{ (x_1, \dots, x_n) \in [0,1]^n : |f(x_1) + \cdots + f(x_n)| \ge a_n \sqrt{n} \}.$$

Then $m_n(F_n) \to 0$ as $n \to \infty$, where $m_n$ is Lebesgue measure on $\mathbb{R}^n$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_06`.

Stated but not proved: `MathlibExt.MeasureTheory.MeanZeroSumDeviationMeasureWanted.tendsto_volume_abs_sum_ge_mul_sqrt` is written with `theorem_wanted` in [WantedExt/MeasureTheory/MeanZeroSumDeviationMeasureWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/MeanZeroSumDeviationMeasureWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/index.html#tendsto-volume-abs-sum-ge-mul-sqrt).

## Variance of the sample mean of i.i.d. samples

Let $X_0, X_1, X_2, \dots$ be real-valued
random variables on a measure space $(\Omega, \mu)$ that are mutually independent and each have
the same distribution as $X_0$, and suppose $X_0$ is square-integrable. Then for every integer
$n \ge 1$, with variances taken with respect to $\mu$,

$$
\operatorname{Var}\Big(\frac{1}{n} \sum_{i=0}^{n-1} X_i\Big) = \frac{\operatorname{Var}(X_0)}{n}.
$$

Square-integrability is required only of $X_0$; identical distribution transfers it to every
sample.

Formalized by `MathlibExt.Probability.variance_sample_mean_of_iid`, a theorem declared in [MathlibExt/Probability/MonteCarloRate.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MonteCarloRate.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/index.html#variance-sample-mean-of-iid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Laws of large numbers and random series](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/laws-of-large-numbers)
