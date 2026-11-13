---
declaration: section
origin: cited
lean: PeriodicEntire.eq_const_of_periodic_one_of_norm_le_exp_abs_im, MathlibExt.Analysis.Complex.EntireSeriesInfiniteZerosWanted.exists_entire_powerSeries_infinite_zeros, MathlibExt.Analysis.Complex.EntireFermatCubicConstantWanted.entire_cube_add_cube_eq_one_const, MathlibExt.Analysis.Complex.InjectiveEntireIsAffineWanted.exists_affine_of_differentiable_injective, MathlibExt.Analysis.Complex.WeierstrassFactorizationWanted.weierstrass_factorization
statement: formalized
---

# Entire and meromorphic functions: its own results

5 results, 2 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html).

Growth and value distribution of entire and meromorphic functions: Wiman–Valiron theory and maximum term, Hayman admissibility, Weierstrass factorization, Mittag-Leffler, Liouville-type rigidity, preimages and zeros/ones on lines.

## A $1$-periodic entire function bounded by $C e^{|\operatorname{Im} s|}$ is constant

Let $f : \mathbb{C} \to \mathbb{C}$ be entire with $f(s + 1) = f(s)$ for all $s \in \mathbb{C}$,
and suppose there is a real constant $C$ such that $|f(s)| \le C e^{|\operatorname{Im} s|}$ for
every $s$ with $0 \le \operatorname{Re} s \le 1$. Then $f$ is constant.

The two-sided bound cannot be weakened to the one-sided $|f(s)| = O(e^{\operatorname{Im} s})$ as
$\operatorname{Im} s \to \infty$: the function $f(s) = e^{2 \pi i s}$ is entire and $1$-periodic,
satisfies $|f(s)| = e^{-2 \pi \operatorname{Im} s} \le e^{\operatorname{Im} s}$ for
$\operatorname{Im} s \ge 0$, and is not constant.

## Sources

- ATLAS `NumberTheoryI`, Lemma 17.14, corrected; the book prints the one-sided bound, under which the lemma is false.

Formalized by `PeriodicEntire.eq_const_of_periodic_one_of_norm_le_exp_abs_im`, a theorem declared in [MathlibExt/Analysis/Complex/PeriodicEntire.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/PeriodicEntire.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html#eq-const-of-periodic-one-of-norm-le-exp).

## A nonzero entire power series with infinitely many zeros

There is a sequence
$(a_k)_{k \ge 0}$ of complex numbers, not all zero, such that the power series
$\sum_{k=0}^{\infty} a_k z^k$ converges absolutely for every $z \in \mathbb{C}$ and its sum
vanishes at infinitely many points $z \in \mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l1_14`.

Stated but not proved: `MathlibExt.Analysis.Complex.EntireSeriesInfiniteZerosWanted.exists_entire_powerSeries_infinite_zeros` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/EntireSeriesInfiniteZerosWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/EntireSeriesInfiniteZerosWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html#exists-entire-power-series-infinite-zero).

## Entire solutions of the Fermat cubic are constant

Let $f$ and $g$ be entire functions
with $f(z)^3 + g(z)^3 = 1$ for every $z \in \mathbb{C}$. Then $f$ and $g$ are constant.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l2_61`.

Stated but not proved: `MathlibExt.Analysis.Complex.EntireFermatCubicConstantWanted.entire_cube_add_cube_eq_one_const` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/EntireFermatCubicConstantWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/EntireFermatCubicConstantWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html#entire-cube-add-cube-eq-one-const).

## Injective entire functions are affine

If $f : \mathbb{C} \to \mathbb{C}$ is entire and
injective, then there are $a, b \in \mathbb{C}$ with $a \ne 0$ such that $f(z) = az + b$ for all
$z \in \mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l1_37`.

Stated but not proved: `MathlibExt.Analysis.Complex.InjectiveEntireIsAffineWanted.exists_affine_of_differentiable_injective` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/InjectiveEntireIsAffineWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/InjectiveEntireIsAffineWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html#exists-affine-of-differentiable-injectiv).

## Weierstrass theorem on prescribed simple zeros

Let $S \subseteq \mathbb{C}$ be a closed set
all of whose points are isolated: for each $z \in S$ there is $\varepsilon > 0$ such that no point
$w \ne z$ of $S$ satisfies $|w - z| < \varepsilon$. Then there is an entire function $f$ whose zeros
are exactly the points of $S$, all of them simple: $f'(z) \ne 0$ for every $z \in S$.

## Sources

- Weierstrass factorization theorem 1876; see Rudin; Lean is simple-zero corollary with closed discrete prescribed zero set S and entire f with exact zeros S and nonvanishing derivative on S.

Formalized by `MathlibExt.Analysis.Complex.WeierstrassFactorizationWanted.weierstrass_factorization`, a theorem declared in [MathlibExt/Analysis/Complex/WeierstrassFactorization.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/WeierstrassFactorization.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html#weierstrass-factorization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Entire and meromorphic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions)
