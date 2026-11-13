---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.SchurHorn.schur_diagonal_eigenvalues_doublyStochastic, MathlibExt.Analysis.InnerProductSpace.EckartYoungWanted.eckartYoung_best_rank_approx_operator_norm
statement: formalized
proof: formalized
---

# Eigenvalue inequalities and perturbation: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/index.html).

Courant–Fischer, Weyl, Ky Fan, Cauchy interlacing, Schur–Horn, Eckart–Young, Bauer–Fike, Peierls–Klein for self-adjoint operators; statements only about finite matrices move to LinearAlgebra.

## Schur's theorem on diagonals of self-adjoint operators

Let $E$ be a complex inner product
space of finite dimension $n$, let $T : E \to E$ be a linear operator that is symmetric, that is,
$\langle T x, y \rangle = \langle x, T y \rangle$ for all $x, y \in E$, let
$\lambda_1, \dots, \lambda_n$ be the eigenvalues of $T$ listed with multiplicity, and let
$b_1, \dots, b_n$ be an orthonormal basis of $E$. Then there is a doubly stochastic real
$n \times n$ matrix $D$ such that $\operatorname{Re} \langle b_i, T b_i \rangle =
\sum_{j=1}^n D_{ij} \lambda_j$ for every $i$.

## Sources

- I. Schur, 1923, Über eine Klasse von Mittelbildungen mit Anwendungen auf die Determinantentheorie; A. Horn, Doubly Stochastic Matrices and the Diagonal of a Rotation Matrix, Amer. J. Math. 76 (1954), 620–630, DOI 10.2307/2372705.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SchurHorn.schur_diagonal_eigenvalues_doublyStochastic`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SchurHorn.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/SchurHorn.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/index.html#schur-diagonal-eigenvalues-doubly-stocha).

## Eckart–Young theorem in operator norm

Let $E$ and $F$ be finite-dimensional inner product
spaces over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T : E \to F$ be a linear map and let
$k \ge 0$ be an integer. The infimum of the operator norms $\|T - S\|$ over all linear maps
$S : E \to F$ whose range has dimension at most $k$ equals $\sigma_k(T)$, where
$\sigma_0(T) \ge \sigma_1(T) \ge \cdots$ are the singular values of $T$ listed with multiplicity
and indexed from $0$, and $\sigma_j(T) = 0$ for $j \ge \dim E$.

## Sources

- C. Eckart and G. Young, The Approximation of One Matrix by Another of Lower Rank, Psychometrika 1 (1936), 211-218, DOI 10.1007/BF02288367; unitary-invariant extension L. Mirsky, QJM 11 (1960), DOI 10.1093/qmath/11.1.50.

Formalized by `MathlibExt.Analysis.InnerProductSpace.EckartYoungWanted.eckartYoung_best_rank_approx_operator_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/EckartYoung.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/EckartYoung.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/index.html#eckart-young-best-rank-approx-operator-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigenvalue inequalities and perturbation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities)
