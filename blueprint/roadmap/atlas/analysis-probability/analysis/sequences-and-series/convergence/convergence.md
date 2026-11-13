---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SpecificLimits.AlternatingPairWeightedSeriesConvergesWanted.exists_tendsto_sum_inv_sq_smul_alternating_pair, MathlibExt.Analysis.Calculus.MonotonePointwiseUniformWanted.monotone_and_tendstoUniformly_of_monotone_tendsto_continuous, MathlibExt.Analysis.SpecificLimits.PowerSeriesCoeffEqOfAgreeOnReciprocalsWanted.coeff_eq_of_tsum_eq_on_inv_nat_add_two, MetaMathlibExt.stolz_cesaro, Complex.summable_neg_pow_mul_pow_div_prod_add_mul, MathlibExt.Analysis.SpecificLimits.OneSubCosDivSeriesUniformWanted.tendstoUniformlyOn_sum_one_sub_cos_div, MetaMathlibExt.contFract_tendsto_of_pringsheim
statement: formalized
---

# Convergence of sequences and series: its own results

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html).

Convergence tests (root test, rearrangement theorem, Stolz–Cesàro), normal and uniform convergence of series of functions, and specific limits of sequences and partial sums.

## Convergence of an alternating weighted series in the plane

Let $\alpha$ and $\beta$ be
real numbers. For $k \in \mathbb{N}$ let $x_k = (\alpha, \beta) \in \mathbb{R} \times \mathbb{R}$
if $k$ is even and $x_k = (\beta, \alpha)$ if $k$ is odd. For $n \in \mathbb{N}$ let
$s_n = \sum_{k=1}^{n} k^{-2} x_k$ (so $s_0 = 0$). Then the sequence $(s_n)$ converges in
$\mathbb{R} \times \mathbb{R}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Sequences, series, summability; Convergence and divergence of infinite limiting processes), problem `ma_proofbench_l1_46`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.AlternatingPairWeightedSeriesConvergesWanted.exists_tendsto_sum_inv_sq_smul_alternating_pair` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/AlternatingPairWeightedSeriesConvergesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/AlternatingPairWeightedSeriesConvergesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#exists-tendsto-sum-inv-sq-smul-alternati).

## Monotone functions on a closed interval with a continuous pointwise limit converge uniformly

**Monotone functions on a closed interval with a continuous pointwise limit converge
uniformly.** Let $a < b$ be real numbers, let $f_n : [a, b] \to \mathbb{R}$, $n \in \mathbb{N}$,
be nondecreasing functions, and let $g : [a, b] \to \mathbb{R}$ be continuous with
$f_n(x) \to g(x)$ for every $x \in [a, b]$. Then $g$ is nondecreasing and $f_n \to g$ uniformly
on $[a, b]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_07`.

Stated but not proved: `MathlibExt.Analysis.Calculus.MonotonePointwiseUniformWanted.monotone_and_tendstoUniformly_of_monotone_tendsto_continuous` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/MonotonePointwiseUniformWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/MonotonePointwiseUniformWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#monotone-and-tendsto-uniformly-of-monoto).

## Power series agreeing at $1/2, 1/3, 1/4, \dots$ have equal coefficients

Let $(a_k)$ and
$(b_k)$ be real sequences such that the series $\sum_{k=0}^{\infty} a_k x^k$ and
$\sum_{k=0}^{\infty} b_k x^k$ converge absolutely for every real $x$ with $|x| < 1$. If
$\sum_{k=0}^{\infty} a_k x^k = \sum_{k=0}^{\infty} b_k x^k$ for $x = 1/2, 1/3, 1/4, \dots$, then
$a_k = b_k$ for all $k \ge 0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_24`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.PowerSeriesCoeffEqOfAgreeOnReciprocalsWanted.coeff_eq_of_tsum_eq_on_inv_nat_add_two` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/PowerSeriesCoeffEqOfAgreeOnReciprocalsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/PowerSeriesCoeffEqOfAgreeOnReciprocalsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#coeff-eq-of-tsum-eq-on-inv-nat-add-two).

## Stolz–Cesàro theorem

Let $(a_n)_{n \ge 0}$ and $(b_n)_{n \ge 0}$ be sequences of
real numbers such that $(b_n)$ is strictly increasing and $b_n \to +\infty$ as $n \to \infty$,
and let $L$ be a real number. If
$\frac{a_{n+1} - a_n}{b_{n+1} - b_n} \to L$ as $n \to \infty$, then
$\frac{a_n}{b_n} \to L$ as $n \to \infty$.

## Sources

- https://en.wikipedia.org/wiki/Stolz%E2%80%93Ces%C3%A0ro_theorem.

Formalized by `MetaMathlibExt.stolz_cesaro`, a theorem declared in [MathlibExt/Analysis/Series/StolzCesaro.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/StolzCesaro.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#stolz-cesaro).

## Summability of a rising-product series

Let $b$, $c$ and $x$ be complex numbers such
that $c + kb \neq 0$ for every integer $k \ge 1$. Then the series
$\sum_{j=0}^{\infty} \frac{(-b)^j x^{j+1}}{\prod_{k=1}^{j+1} (c + kb)}$ is summable.

Formalized by `Complex.summable_neg_pow_mul_pow_div_prod_add_mul`, a theorem declared in [MathlibExt/Analysis/SpecificLimits/RisingProductSeries.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecificLimits/RisingProductSeries.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#summable-neg-pow-mul-pow-div-prod-add-mu).

## Uniform convergence of $\sum (1 - \cos(x/n))$ on compact intervals

For all real numbers
$a < b$ there is a function $g : \mathbb{R} \to \mathbb{R}$ such that the partial sums
$\sum_{n=1}^{N} \bigl(1 - \cos(x/n)\bigr)$ converge to $g(x)$ uniformly for $x \in [a, b]$ as
$N \to \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Sequences, series, summability; Convergence and divergence of infinite limiting processes), problem `ma_proofbench_l1_05`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.OneSubCosDivSeriesUniformWanted.tendstoUniformlyOn_sum_one_sub_cos_div` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/OneSubCosDivSeriesUniformWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/OneSubCosDivSeriesUniformWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#tendsto-uniformly-on-sum-one-sub-cos-div).

## Śleszyński–Pringsheim convergence criterion

Let $a_0, a_1, a_2, \dots$ and
$b_0, b_1, b_2, \dots$ be complex numbers with $1 + |a_k| \le |b_k|$ for every $k$. For $n \ge 0$
let $f_n$ be the $n$-th approximant of the continued fraction $a_0 / (b_0 + a_1 / (b_1 + \cdots))$,
that is $f_0 = 0$ and $f_n = a_0 / (b_0 + a_1 / (b_1 + \cdots + a_{n-1} / b_{n-1}))$ for $n \ge 1$.
Then there is a complex number $v$ with $|v| \le 1$ such that $f_n \to v$ as $n \to \infty$.

Zero partial numerators are admitted.

## Sources

- Carminda M. Mennen, *Möbius Maps and Continued Fractions*, INTEGERS 24 (2024), Article A52, Theorem 1.

Stated but not proved: `MetaMathlibExt.contFract_tendsto_of_pringsheim` is written with `theorem_wanted` in [WantedExt/Algebra/ContinuedFractions/MobiusContinuedFractionsWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/ContinuedFractions/MobiusContinuedFractionsWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html#cont-fract-tendsto-of-pringsheim).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence of sequences and series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/convergence)
