---
declaration: section
origin: cited
lean: Fourier.RootData, Fourier.principalMinorMatrix, Fourier.principalMinorDet, Fourier.principalMinorMatrix_apply, Fourier.principalMinorDet_empty, Fourier.principalMinorDet_singleton
statement: formalized
proof: formalized
---

# Principal minors of the Fourier matrix

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html).

## Primitive root of unity data

For a natural number $M$ and a commutative ring $R$, root
data of order $M$ in $R$ consists of an element $\zeta \in R$ that is a primitive $M$-th root of
unity, together with the condition $M \ge 2$.

Formalized by `Fourier.RootData`, a structure declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#root-data).

## Principal Fourier minor

Let $M \ge 2$, let $R$ be a commutative ring, let $\zeta \in R$
be a primitive $M$-th root of unity, and let $S$ be a finite subset of $\mathbb{Z}/M\mathbb{Z}$.
The principal Fourier minor indexed by $S$ is the $S \times S$ matrix over $R$ whose $(i, j)$
entry is $\zeta^{n}$, where $n \in \{0, \dots, M-1\}$ is the representative of the product $ij$
in $\mathbb{Z}/M\mathbb{Z}$.

Formalized by `Fourier.principalMinorMatrix`, a definition declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#principal-minor-matrix).

## Determinant of a principal Fourier minor

Let $M \ge 2$, let $R$ be a commutative ring,
let $\zeta \in R$ be a primitive $M$-th root of unity, and let $S$ be a finite subset of
$\mathbb{Z}/M\mathbb{Z}$. The principal Fourier minor determinant of $S$ is the determinant in $R$
of the principal Fourier minor indexed by $S$.

Formalized by `Fourier.principalMinorDet`, a definition declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#principal-minor-det).

## Entries of a principal Fourier minor

Let $M \ge 2$, let $R$ be a commutative ring, let
$\zeta \in R$ be a primitive $M$-th root of unity, and let $S$ be a finite subset of
$\mathbb{Z}/M\mathbb{Z}$. For all $i, j \in S$, the $(i, j)$ entry of the principal Fourier minor
indexed by $S$ equals $\zeta^{n}$, where $n \in \{0, \dots, M-1\}$ is the representative of $ij$
in $\mathbb{Z}/M\mathbb{Z}$.

Formalized by `Fourier.principalMinorMatrix_apply`, a theorem declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#principal-minor-matrix-apply).

## Determinant of the empty principal Fourier minor

Let $M \ge 2$, let $R$ be a commutative
ring and let $\zeta \in R$ be a primitive $M$-th root of unity. The determinant of the principal
Fourier minor indexed by the empty subset of $\mathbb{Z}/M\mathbb{Z}$ equals $1$.

Formalized by `Fourier.principalMinorDet_empty`, a theorem declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#principal-minor-det-empty).

## Determinant of a singleton principal Fourier minor

Let $M \ge 2$, let $R$ be a
commutative ring, let $\zeta \in R$ be a primitive $M$-th root of unity, and let
$a \in \mathbb{Z}/M\mathbb{Z}$. The determinant of the principal Fourier minor indexed by $\{a\}$
equals $\zeta^{n}$, where $n \in \{0, \dots, M-1\}$ is the representative of $a^2$ in
$\mathbb{Z}/M\mathbb{Z}$.

Formalized by `Fourier.principalMinorDet_singleton`, a theorem declared in [MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Fourier/PrincipalMinor.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html#principal-minor-det-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Principal minors of the Fourier matrix](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/special-matrices/principal-minors-of-the-fourier-matrix)
