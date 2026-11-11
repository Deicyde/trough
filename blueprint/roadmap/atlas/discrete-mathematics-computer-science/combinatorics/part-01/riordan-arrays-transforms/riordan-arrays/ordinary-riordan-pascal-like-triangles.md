---
declaration: section
origin: cited
lean: MetaMathlibExt.ordinaryRiordanPascalLikeMatrix, MetaMathlibExt.ordinaryRiordanPascalLikeMatrix_def
statement: formalized
proof: formalized
---

# Ordinary Riordan Pascal-like triangles

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/ordinary-riordan-pascal-like-triangles/index.html).

## Ordinary Riordan Pascal-like triangle

For natural numbers $n, k$ and an integer $r$,
the entry $T(n, k; r)$ is the integer

$$T(n, k; r) = \sum_{j=0}^{k} \binom{k}{j} \binom{\max(n - j, 0)}{k} r^j.$$

This is the entry formula of the ordinary Riordan array
$\bigl(1/(1 - x),\ x(1 + rx)/(1 - x)\bigr)$, denoted $T(r)$. Terms with $j > n - k$ vanish,
because then $\max(n - j, 0) < k$. For $r = 0$ this is Pascal's triangle and for $r = 1$ the
Delannoy triangle.

Formalized by `MetaMathlibExt.ordinaryRiordanPascalLikeMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/OrdinaryRiordanPascalLikeMatrix.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/OrdinaryRiordanPascalLikeMatrix.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/ordinary-riordan-pascal-like-triangles/index.html#ordinary-riordan-pascal-like-matrix).

## Entry formula for the ordinary Riordan Pascal-like triangle

For natural numbers
$n, k$ and an integer $r$, the ordinary Riordan Pascal-like matrix entry $T(n, k; r)$ equals
$\sum_{j=0}^{k} \binom{k}{j} \binom{\max(n - j, 0)}{k} r^j$; this holds by definition.

Formalized by `MetaMathlibExt.ordinaryRiordanPascalLikeMatrix_def`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/OrdinaryRiordanPascalLikeMatrix.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/OrdinaryRiordanPascalLikeMatrix.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/ordinary-riordan-pascal-like-triangles/index.html#ordinary-riordan-pascal-like-matrix-def).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordinary Riordan Pascal-like triangles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/ordinary-riordan-pascal-like-triangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/ordinary-riordan-pascal-like-triangles)
