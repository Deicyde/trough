---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.SystemsBiology.exists_symmetric_balancing_of_hasTotalSupport, MathlibExt.Biology.Dynamics.SystemsBiology.exists_symmetric_balancing_iff_hasTotalSupport, MathlibExt.LinearAlgebra.Matrix.SinkhornWanted.sinkhorn_scaling
statement: formalized
proof: formalized
---

# Matrix scaling to doubly stochastic form

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form/index.html).

## Csima–Datta: sufficiency of total support

A symmetric nonnegative matrix with total
support has a positive vector `d` with `diag(d) A diag(d)` doubly stochastic.

## Sources

- Csima & Datta (1972); Sinkhorn & Knopp (1967).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_symmetric_balancing_of_hasTotalSupport`, a theorem declared in [MathlibExt/Biology/Dynamics/TotalSupportBalancing.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/TotalSupportBalancing.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form/index.html#exists-symmetric-balancing-of-has-total).

## Csima–Datta theorem

For `0 < n`, a symmetric nonnegative matrix has a positive vector
`d` with `diag(d) A diag(d)` doubly stochastic if and only if it has total support.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_symmetric_balancing_iff_hasTotalSupport`, a theorem declared in [MathlibExt/Biology/Dynamics/TotalSupportBalancing.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/TotalSupportBalancing.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form/index.html#exists-symmetric-balancing-iff-has-total).

## Sinkhorn's scaling theorem

Let $n \ge 1$ and let $A$ be a real $n \times n$ matrix all of
whose entries are strictly positive. Then there are vectors $r, c \in \mathbb{R}^n$ with strictly
positive entries such that the matrix with entries $r_i A_{ij} c_j$ is doubly stochastic, that is,
its entries are nonnegative and each of its rows and each of its columns sums to $1$.

## Sources

- R. Sinkhorn, Ann. Math. Statist. 35 (1964), 876-879, DOI 10.1214/aoms/1177703591.

Formalized by `MathlibExt.LinearAlgebra.Matrix.SinkhornWanted.sinkhorn_scaling`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Sinkhorn.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/Sinkhorn.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form/index.html#sinkhorn-scaling).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix scaling to doubly stochastic form](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/matrix-scaling-to-doubly-stochastic-form)
