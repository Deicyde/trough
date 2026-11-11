---
declaration: section
origin: cited
lean: LinearMap.IsPerfPair.dualBasis, LinearMap.IsPerfPair.dualBasis_apply, LinearMap.IsPerfPair.eq_dualBasis_of, LinearMap.IsPerfPair.exists_dualBasis, LinearMap.IsPerfPair.existsUnique_dualBasis
statement: formalized
proof: formalized
---

# Dual bases of perfect pairings

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html).

## Dual basis with respect to a perfect pairing

Let $A$ be a commutative ring, let $M$
and $N$ be $A$-modules, and let $B : M \times N \to A$ be a perfect pairing, that is, an
$A$-bilinear map such that $x \mapsto B(x, \cdot)$ is a linear isomorphism $M \to N^*$ and
$y \mapsto B(\cdot, y)$ is a linear isomorphism $N \to M^*$. Let $b = (b_i)_{i \in \iota}$ be
a basis of $N$ indexed by a finite type $\iota$, and let $(b_i^*)_{i \in \iota}$ be its dual
basis of $N^*$, where $b_i^*(b_j)$ is $1$ if $j = i$ and $0$ otherwise. The dual basis of $b$
with respect to $B$ is the basis of $M$ whose $i$-th vector is the image of $b_i^*$ under the
inverse of the isomorphism $M \to N^*$, $x \mapsto B(x, \cdot)$.

Formalized by `LinearMap.IsPerfPair.dualBasis`, a definition declared in [MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html#dual-basis).

## Evaluation of the dual basis

Let $A$ be a commutative ring, let $M$ and $N$ be
$A$-modules, let $B : M \times N \to A$ be a perfect pairing, and let $b = (b_i)_{i \in \iota}$
be a basis of $N$ indexed by a finite type $\iota$. Write $(b_i^\vee)_{i \in \iota}$ for the
dual basis of $b$ with respect to $B$, a basis of $M$. Then for all $i, j \in \iota$, the value
$B(b_i^\vee, b_j)$ equals $1$ if $j = i$ and $0$ otherwise.

Formalized by `LinearMap.IsPerfPair.dualBasis_apply`, a theorem declared in [MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html#dual-basis-apply).

## Uniqueness of the dual basis

Let $A$ be a commutative ring, let $M$ and $N$ be
$A$-modules, let $B : M \times N \to A$ be a perfect pairing, and let $b = (b_i)_{i \in \iota}$
be a basis of $N$ indexed by a finite type $\iota$. If $b' = (b'_i)_{i \in \iota}$ is a basis
of $M$ such that for all $i, j \in \iota$ the value $B(b'_i, b_j)$ equals $1$ if $j = i$ and
$0$ otherwise, then $b'$ is the dual basis of $b$ with respect to $B$.

Formalized by `LinearMap.IsPerfPair.eq_dualBasis_of`, a theorem declared in [MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html#eq-dual-basis-of).

## Existence of a dual basis for a perfect pairing

Let $A$ be a commutative ring, let $M$
and $N$ be $A$-modules, let $B : M \times N \to A$ be a perfect pairing, and let
$b = (b_i)_{i \in \iota}$ be a basis of $N$ indexed by a finite type $\iota$. Then there is a
basis $(b'_i)_{i \in \iota}$ of $M$ such that for all $i, j \in \iota$ the value $B(b'_i, b_j)$
equals $1$ if $j = i$ and $0$ otherwise.

Formalized by `LinearMap.IsPerfPair.exists_dualBasis`, a theorem declared in [MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html#exists-dual-basis).

## Existence and uniqueness of the dual basis for a perfect pairing

Let $A$ be a
commutative ring, let $M$ and $N$ be $A$-modules, let $B : M \times N \to A$ be a perfect
pairing, and let $b = (b_i)_{i \in \iota}$ be a basis of $N$ indexed by a finite type $\iota$.
Then there is exactly one basis $(b'_i)_{i \in \iota}$ of $M$ such that for all
$i, j \in \iota$ the value $B(b'_i, b_j)$ equals $1$ if $j = i$ and $0$ otherwise.

Formalized by `LinearMap.IsPerfPair.existsUnique_dualBasis`, a theorem declared in [MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/PerfectPairing/DualBasis.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html#exists-unique-dual-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual bases of perfect pairings](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/linear-maps-and-duality/dual-bases-of-perfect-pairings)
