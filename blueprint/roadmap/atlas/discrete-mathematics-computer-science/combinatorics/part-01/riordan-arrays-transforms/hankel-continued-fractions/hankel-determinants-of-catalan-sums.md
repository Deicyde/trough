---
declaration: section
origin: cited
lean: MetaMathlibExt.layman_catalan_sum_hankel_det_unrestricted, MetaMathlibExt.layman_catalan_sum_hankel_det
statement: formalized
proof: formalized
---

# Hankel determinants of Catalan sums

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-determinants-of-catalan-sums/index.html).

## Layman's Catalan-sum Hankel determinant, including the empty matrix

Let $C_m$ denote the
$m$-th Catalan number and $F_m$ the $m$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. For
every natural number $n$, the determinant of the $n \times n$ integer matrix whose $(i, j)$ entry
is $C_{i+j+1} + C_{i+j+2}$ for $0 \le i, j \le n-1$ equals $F_{2n+2}$. For $n = 0$ the matrix is
empty and both sides equal $1$.

Formalized by `MetaMathlibExt.layman_catalan_sum_hankel_det_unrestricted`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LaymanCatalanHankel.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LaymanCatalanHankel.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-determinants-of-catalan-sums/index.html#layman-catalan-sum-hankel-det-unrestrict).

## Layman's Catalan-sum Hankel determinant

Let $C_m$ denote the $m$-th Catalan number and
$F_m$ the $m$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. For every integer $n \ge 1$, the
determinant of the $n \times n$ integer matrix whose $(i, j)$ entry is $C_{i+j+1} + C_{i+j+2}$ for
$0 \le i, j \le n-1$ equals $F_{2n+2}$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL16/Bouras/bouras4.tex>, lines 109–117.

Formalized by `MetaMathlibExt.layman_catalan_sum_hankel_det`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LaymanCatalanHankel.lean, line 766](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LaymanCatalanHankel.lean#L766). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-determinants-of-catalan-sums/index.html#layman-catalan-sum-hankel-det).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hankel determinants of Catalan sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-determinants-of-catalan-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-determinants-of-catalan-sums)
