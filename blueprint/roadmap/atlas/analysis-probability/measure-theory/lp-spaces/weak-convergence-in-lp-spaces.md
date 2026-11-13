---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.WeakConvergenceOfBoundedAeNullLpWanted.μI01, MathlibExt.Analysis.FunctionalAnalysis.WeakConvergenceOfBoundedAeNullLpWanted.tendsto_integral_mul_of_ae_tendsto_zero_of_eLpNorm_le_one, MathlibExt.Analysis.FunctionalAnalysis.WeakLimitOfNonnegLpNonnegWanted.ae_nonneg_of_weak_tendsto_of_ae_nonneg, MathlibExt.MeasureTheory.WeakLpConvergenceOfAeConvergenceWanted.tendsto_integral_mul_of_ae_tendsto_of_eLpNorm_bounded
statement: formalized
---

# Weak convergence in Lp spaces

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html).

## Lebesgue measure on $(0,1)$

The measure on $\mathbb{R}$ obtained by restricting
Lebesgue measure to the open interval $(0, 1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.WeakConvergenceOfBoundedAeNullLpWanted.μI01`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/WeakConvergenceOfBoundedAeNullLpWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/WeakConvergenceOfBoundedAeNullLpWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html#i01).

## Bounded a.e.-null sequences in $L^p(0,1)$ converge weakly to zero

Let $1 < p < \infty$
and let $q$ be the conjugate exponent, so that $1/p + 1/q = 1$. Write $L^p(0,1)$ and $L^q(0,1)$
for the Lebesgue spaces of real functions on $(0,1)$ with Lebesgue measure. Let
$(f_n)_{n \in \mathbb{N}}$ be a sequence in $L^p(0,1)$ with $\|f_n\|_{L^p} \le 1$ for every $n$
and $f_n(x) \to 0$ for almost every $x \in (0,1)$. Then for every $g \in L^q(0,1)$,

$$
\int_0^1 f_n(x)\, g(x)\, dx \to 0 \quad (n \to \infty).
$$

Since $L^q(0,1)$ is the dual of $L^p(0,1)$, this says that $(f_n)$ converges weakly to $0$ in
$L^p(0,1)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Normed linear spaces and Banach spaces; Banach lattices), problem `ma_proofbench_l2_10`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.WeakConvergenceOfBoundedAeNullLpWanted.tendsto_integral_mul_of_ae_tendsto_zero_of_eLpNorm_le_one` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/WeakConvergenceOfBoundedAeNullLpWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/WeakConvergenceOfBoundedAeNullLpWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html#tendsto-integral-mul-of-ae-tendsto-zero).

## Weak $L^p$ limits of nonnegative functions are nonnegative

Let $1 < p < \infty$
and write $L^p([0,1])$ for the Lebesgue space of real functions on $[0,1]$ with Lebesgue measure.
Let $(f_n)_{n \in \mathbb{N}}$ be a sequence in $L^p([0,1])$ such that for each $n$,
$f_n(x) \ge 0$ for almost every $x \in [0,1]$, and let $f \in L^p([0,1])$. If $f_n$ converges
weakly to $f$, that is, $\ell(f_n) \to \ell(f)$ for every continuous linear functional
$\ell : L^p([0,1]) \to \mathbb{R}$, then $f(x) \ge 0$ for almost every $x \in [0,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Normed linear spaces and Banach spaces; Banach lattices), problem `ma_proofbench_l2_16`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.WeakLimitOfNonnegLpNonnegWanted.ae_nonneg_of_weak_tendsto_of_ae_nonneg` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/WeakLimitOfNonnegLpNonnegWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/WeakLimitOfNonnegLpNonnegWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html#ae-nonneg-of-weak-tendsto-of-ae-nonneg).

## Bounded almost everywhere convergent sequences in $L^p$, $1 < p < \infty$, converge weakly

**Bounded almost everywhere convergent sequences in $L^p$, $1 < p < \infty$, converge
weakly.** Let $1 < p < \infty$ and let $q$ be the conjugate exponent, $1/p + 1/q = 1$. Let $f$
and $f_0, f_1, f_2, \dots$ be real-valued functions in $L^p(\mathbb{R})$ such that $f_n \to f$
almost everywhere and $\sup_n \|f_n\|_{L^p} < \infty$. Then $f_n$ converges weakly to $f$: for
every $g \in L^q(\mathbb{R})$,

$$
\lim_{n\to\infty}\int_{\mathbb{R}} f_n g\,dx=\int_{\mathbb{R}} f g\,dx.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Normed linear spaces and Banach spaces; Banach lattices), problem `ma_proofbench_l2_82`.

Stated but not proved: `MathlibExt.MeasureTheory.WeakLpConvergenceOfAeConvergenceWanted.tendsto_integral_mul_of_ae_tendsto_of_eLpNorm_bounded` is written with `theorem_wanted` in [WantedExt/MeasureTheory/WeakLpConvergenceOfAeConvergenceWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/WeakLpConvergenceOfAeConvergenceWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html#tendsto-integral-mul-of-ae-tendsto-of-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weak convergence in Lp spaces](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/lp-spaces/weak-convergence-in-lp-spaces)
