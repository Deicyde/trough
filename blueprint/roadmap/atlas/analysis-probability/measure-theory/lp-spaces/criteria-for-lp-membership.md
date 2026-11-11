---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Function.MemLpTruncation.lintegral_eq_iSup_lintegral_Icc_inter, MathlibExt.MeasureTheory.Function.MemLpTruncation.memLp_iff_iSup_lintegral_Icc_inter_lt_top, MathlibExt.MeasureTheory.Function.PolynomialDecay.memLp_of_polynomial_decay_ae, MathlibExt.MeasureTheory.Function.PolynomialDecay.memLp_of_polynomial_decay, MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.IsPartition01, MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.partitionAverageSum, MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.memLp_iff_bddAbove_partitionAverageSum
statement: formalized
---

# Criteria for Lp membership

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html).

## Lebesgue integrals over truncations of a set

Let $\lambda$ be Lebesgue measure on
$\mathbb{R}$, let $S \subseteq \mathbb{R}$ be measurable, and let $g : \mathbb{R} \to [0, \infty]$
be measurable. Then

$$\int_S g \, d\lambda = \sup_{n \in \mathbb{N}} \int_{[-n, n] \cap S} g \, d\lambda.$$

This is monotone convergence applied to the indicators of the truncations.

Formalized by `MathlibExt.MeasureTheory.Function.MemLpTruncation.lintegral_eq_iSup_lintegral_Icc_inter`, a theorem declared in [MathlibExt/MeasureTheory/Function/MemLpTruncation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/MemLpTruncation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#lintegral-eq-i-sup-lintegral-icc-inter).

## Characterization of $L^p$ membership via truncated integrals

Let $\lambda$ be Lebesgue
measure on $\mathbb{R}$, let $F$ be a second-countable normed additive commutative group with its
Borel $\sigma$-algebra, let $0 < p < \infty$, let $S \subseteq \mathbb{R}$ be measurable, and let
$f : \mathbb{R} \to F$ be measurable. Then $f$ belongs to $L^p$ of $\lambda$ restricted to $S$ if
and only if

$$\sup_{n \in \mathbb{N}} \int_{[-n, n] \cap S} \|f(x)\|^p \, d\lambda(x) < \infty,$$

where the integrals are taken in $[0, \infty]$.

Formalized by `MathlibExt.MeasureTheory.Function.MemLpTruncation.memLp_iff_iSup_lintegral_Icc_inter_lt_top`, a theorem declared in [MathlibExt/MeasureTheory/Function/MemLpTruncation.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/MemLpTruncation.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#mem-lp-iff-i-sup-lintegral-icc-inter-lt).

## Polynomial decay implies $L^p$ membership

Let $E$ be a normed additive commutative group
and let $f : \mathbb{R} \to E$ be almost everywhere strongly measurable. Suppose there are real
numbers $C \ge 0$ and $q > 1$ such that $\|f(x)\| \le C (1 + |x|)^{-q}$ for almost every
$x \in \mathbb{R}$. Then $f \in L^p(\mathbb{R})$, with respect to Lebesgue measure, for every
$p \in [1, \infty]$.

Formalized by `MathlibExt.MeasureTheory.Function.PolynomialDecay.memLp_of_polynomial_decay_ae`, a theorem declared in [MathlibExt/MeasureTheory/Function/PolynomialDecayMemLp.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/PolynomialDecayMemLp.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#mem-lp-of-polynomial-decay-ae).

## Pointwise polynomial decay implies $L^p$ membership

Let $E$ be a normed additive
commutative group and let $f : \mathbb{R} \to E$ be almost everywhere strongly measurable. Suppose
there are real numbers $C \ge 0$ and $q > 1$ such that $\|f(x)\| \le C (1 + |x|)^{-q}$ for every
$x \in \mathbb{R}$. Then $f \in L^p(\mathbb{R})$, with respect to Lebesgue measure, for every
$p \in [1, \infty]$.

Formalized by `MathlibExt.MeasureTheory.Function.PolynomialDecay.memLp_of_polynomial_decay`, a theorem declared in [MathlibExt/MeasureTheory/Function/PolynomialDecayMemLp.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/PolynomialDecayMemLp.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#mem-lp-of-polynomial-decay).

## Partitions of the unit interval

For a natural number $n$, real numbers
$t_0, t_1, \dots, t_n$ form a partition of $[0, 1]$ when $0 = t_0 < t_1 < \dots < t_n = 1$.

Formalized by `MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.IsPartition01`, a definition declared in [WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#is-partition01).

## Partition average sum

For a function $f : \mathbb{R} \to \mathbb{R}$, a real number $p$
and real numbers $t_0, t_1, \dots, t_n$, the partition average sum is

$$\sum_{i=0}^{n-1} (t_{i+1} - t_i)
\left(\frac{1}{t_{i+1} - t_i} \int_{[t_i, t_{i+1}]} |f(x)|\,dx\right)^p,$$

where the integrals are Lebesgue integrals over the closed intervals $[t_i, t_{i+1}]$ (empty when
$t_{i+1} < t_i$), the integral of a function that is not integrable there counts as $0$, $1/0 = 0$,
and $0^p$ is taken to be $1$ when $p = 0$ and $0$ when $p \ne 0$.

Formalized by `MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.partitionAverageSum`, a definition declared in [WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#partition-average-sum).

## $L^p$ on $(0,1)$ via averages over partitions

Let $f : \mathbb{R} \to \mathbb{R}$ be in
$L^1([0, 1])$ and let $p > 1$ be a real number. Then $f \in L^p([0, 1])$ if and only if there is
a real number $C$ such that

$$\sum_{i=0}^{n-1} (t_{i+1} - t_i)
\left(\frac{1}{t_{i+1} - t_i} \int_{t_i}^{t_{i+1}} |f(x)|\,dx\right)^p \le C$$

for every partition $0 = t_0 < t_1 < \dots < t_n = 1$ of $[0, 1]$. Here $L^1([0, 1])$ and
$L^p([0, 1])$ are taken with respect to Lebesgue measure restricted to $[0, 1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_02`.

Stated but not proved: `MathlibExt.MeasureTheory.LpCharacterizationPartitionAveragesWanted.memLp_iff_bddAbove_partitionAverageSum` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpCharacterizationPartitionAveragesWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html#mem-lp-iff-bdd-above-partition-average-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Criteria for Lp membership](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces/criteria-for-lp-membership)
