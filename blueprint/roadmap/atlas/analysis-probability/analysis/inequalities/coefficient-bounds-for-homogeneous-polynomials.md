---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook74Wanted.EvalPoly, MathlibExt.Analysis.ScottishBook74Wanted.ScottishBookProblem74Claim, MathlibExt.Analysis.ScottishBook74Wanted.scottishBook74_holds
statement: formalized
---

# Coefficient bounds for homogeneous polynomials

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials/index.html).

## Evaluation of a homogeneous polynomial

Given a natural number $n$, real coefficients
$a_k$ indexed by multi-indices $k = (k_1, \dots, k_n) \in \mathbb{N}^n$, and a point
$t = (t_1, \dots, t_n) \in \mathbb{R}^n$, the value is

$$\sum_{k_1 + \cdots + k_n = n} a_k \, t_1^{k_1} \cdots t_n^{k_n},$$

the value at $t$ of the homogeneous polynomial of degree $n$ in $n$ variables with these
coefficients. The sum runs over all $k \in \mathbb{N}^n$ with $k_1 + \cdots + k_n = n$;
coefficients of other multi-indices do not enter.

## Sources

- Scottish Book Problem 74.

Formalized by `MathlibExt.Analysis.ScottishBook74Wanted.EvalPoly`, a definition declared in [WantedExt/Analysis/ScottishBook74Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook74Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials/index.html#eval-poly).

## The coefficient bound of Scottish Book Problem 74

This is the statement that for every
$n \ge 1$ and all real coefficients $a_k$ indexed by multi-indices
$k = (k_1, \dots, k_n) \in \mathbb{N}^n$ the following holds. Let
$P(t) = \sum_{k_1 + \cdots + k_n = n} a_k \, t_1^{k_1} \cdots t_n^{k_n}$ be the corresponding
homogeneous polynomial of degree $n$ on $\mathbb{R}^n$. If $|P(t)| \le 1$ for every
$t \in \mathbb{R}^n$ with $|t_1| + \cdots + |t_n| \le 1$, then
$|a_k| \le n^n / (k_1! \cdots k_n!)$ for every $k \in \mathbb{N}^n$ with
$k_1 + \cdots + k_n = n$.

This is only the upper-bound part of Problem 74; the best constant is an open question.

Formalized by `MathlibExt.Analysis.ScottishBook74Wanted.ScottishBookProblem74Claim`, a definition declared in [WantedExt/Analysis/ScottishBook74Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook74Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials/index.html#scottish-book-problem74-claim).

## Scottish Book Problem 74: the coefficient bound holds

Let $n \ge 1$, let $a_k$ be real
coefficients indexed by multi-indices $k = (k_1, \dots, k_n) \in \mathbb{N}^n$, and let
$P(t) = \sum_{k_1 + \cdots + k_n = n} a_k \, t_1^{k_1} \cdots t_n^{k_n}$ be the corresponding
homogeneous polynomial of degree $n$ on $\mathbb{R}^n$. If $|P(t)| \le 1$ for every
$t \in \mathbb{R}^n$ with $|t_1| + \cdots + |t_n| \le 1$, then
$|a_k| \le n^n / (k_1! \cdots k_n!)$ for every $k \in \mathbb{N}^n$ with
$k_1 + \cdots + k_n = n$.

## Sources

- S. Mazur and W. Orlicz, Problem 74 of the Scottish Book; typescript PDF p.36, printed p.33; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015). Proved by the classical polarization identity; the Rademacher form is Lemma 12 of M. Chatzakou and Y. Sarantopoulos, "Estimates for polynomial norms on Banach spaces", arXiv:2107.05993. Sketch: let `P` be `n`-homogeneous with `|P(t)| ≤ 1` for `‖t‖₁ ≤ 1`, and let `L` be its symmetric `n`-linear polar form. Polarization gives `L(x₁, …, xₙ) = (1/(2ⁿ n!)) Σ_{ε ∈ {±1}ⁿ} ε₁⋯εₙ P(Σᵢ εᵢ xᵢ)`. Take the multiset `x₁, …, xₙ` to be `e₁` with multiplicity `k₁`, …, `eₙ` with multiplicity `kₙ`, so `Σ kᵢ = n`. Then `a_k = (n! / ∏ kᵢ!) · L(e₁^{k₁}, …, eₙ^{kₙ})`, and `‖Σᵢ εᵢ xᵢ‖₁ ≤ Σⱼ kⱼ = n`, so by homogeneity `|P(Σᵢ εᵢ xᵢ)| ≤ nⁿ`. Hence `|L(e₁^{k₁}, …, eₙ^{kₙ})| ≤ (1/(2ⁿ n!)) · 2ⁿ · nⁿ = nⁿ / n!`, and `|a_k| ≤ (n! / ∏ kᵢ!) · (nⁿ / n!) = nⁿ / ∏ kᵢ!`. The open content of Problem 74 is the exact best constant `C*(n, k) = sup { |a_k| : ‖P‖ ≤ 1 }`, for which no closed form is known. The bound here is not sharp for all `k`: for `k = (n, 0, …, 0)` with `n ≥ 2`, the best constant is `1` (since `|a_k| = |P(e₁)| ≤ 1`) while the bound is `nⁿ / n! > 1`. The monomial gives the lower bound `C*(n, k) ≥ nⁿ / ∏ kᵢ^{kᵢ}` (with `0^0 := 1`).

Stated but not proved: `MathlibExt.Analysis.ScottishBook74Wanted.scottishBook74_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook74Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook74Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials/index.html#scottish-book74-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coefficient bounds for homogeneous polynomials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/inequalities/coefficient-bounds-for-homogeneous-polynomials)
