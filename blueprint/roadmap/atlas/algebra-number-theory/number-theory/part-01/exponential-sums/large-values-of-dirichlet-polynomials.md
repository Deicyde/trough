---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LargeValueEstimatesWanted.LargeValueEstimates.bound, MathlibExt.NumberTheory.LargeValueEstimatesWanted.LargeValueEstimates.theorem_1_1
statement: formalized
---

# Large values of Dirichlet polynomials

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/large-values-of-dirichlet-polynomials/index.html).

## The Guth–Maynard large values bound

For a natural number $N$ and real numbers $V$ and
$T$, this is the real number $N^2 V^{-2} + N^{18/5} V^{-4} + T N^{12/5} V^{-4}$, the factor
multiplying $T^{o(T)}$ on the right-hand side of the Guth–Maynard large values estimate for
Dirichlet polynomials. Here $V^{-2}$ and $V^{-4}$ are read as $0$ when $V = 0$.

Formalized by `MathlibExt.NumberTheory.LargeValueEstimatesWanted.LargeValueEstimates.bound`, a definition declared in [WantedExt/NumberTheory/LargeValueEstimatesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeValueEstimatesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/large-values-of-dirichlet-polynomials/index.html#bound).

## Guth–Maynard large values estimate

There is a function $o : \mathbb{R} \to \mathbb{R}$
with $o(T) \to 0$ as $T \to \infty$ such that the following holds. Let $(b_n)_{n \ge 0}$ be
complex numbers with $|b_n| \le 1$ for all $n$, let $N \ge 1$ and $R$ be natural numbers,
let $V > 0$ and $T > 1$ be real numbers, and let $t_0, \dots, t_{R-1}$ be points of $[0, T]$
with $|t_r - t_s| \ge 1$ whenever $r \ne s$. Suppose that, with $i$ the imaginary unit,

$$\left|\sum_{n=N}^{2N} b_n n^{i t_r}\right| \ge V$$

for every $r < R$. Then

$$R \le T^{o(T)} \left(N^2 V^{-2} + N^{18/5} V^{-4} + T N^{12/5} V^{-4}\right).$$

The hypotheses $N \ge 1$, $V > 0$ and $T > 1$ are not stated in the paper; the inequality may
be false at $T = 1$.

## Sources

- L. Guth and J. Maynard, `New large value estimates for Dirichlet polynomials`, Annals of Math, 203 (2) 2026. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_large_value_estimates` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.LargeValueEstimatesWanted.LargeValueEstimates.theorem_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeValueEstimatesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeValueEstimatesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/large-values-of-dirichlet-polynomials/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large values of Dirichlet polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/large-values-of-dirichlet-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/exponential-sums/large-values-of-dirichlet-polynomials)
