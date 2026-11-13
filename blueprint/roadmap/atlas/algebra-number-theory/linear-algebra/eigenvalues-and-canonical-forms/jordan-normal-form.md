---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.jordanBlock, MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.jordanBlock_apply, LinearMap.toMatrix_eq_jordanBlock, LinearMap.toMatrix_eq_blockDiagonal_jordanBlock, Module.End.exists_jordanBasis_of_isNilpotent, Module.End.exists_jordanBasis_of_charpoly_splits, MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.exists_jordan_normal_form_of_splits
statement: formalized
proof: formalized
---

# Jordan normal form

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html).

## Jordan blocks

## Jordan block

For a natural number $s$ and a scalar $\mu$ in a field $K$, the Jordan block of
size $s$ with eigenvalue $\mu$ is the $s \times s$ matrix over $K$, with rows and columns indexed
by $\{0, \dots, s-1\}$, whose $(i, j)$ entry is $1$ if $j = i + 1$, $\mu$ if $i = j$, and $0$
otherwise: it has $\mu$ on the diagonal, $1$ on the first superdiagonal and $0$ elsewhere.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Section 3.4.

Formalized by `MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.jordanBlock`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#jordan-block).

## Entries of a Jordan block

For a natural number $s$, a scalar $\mu$ in a field $K$ and indices
$i, j \in \{0, \dots, s-1\}$, the $(i, j)$ entry of the Jordan block of size $s$ with eigenvalue
$\mu$ is $1$ if $j = i + 1$, is $\mu$ if $i = j$, and is $0$ otherwise.

## Sources

- https://en.wikipedia.org/wiki/Jordan_normal_form.

Formalized by `MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.jordanBlock_apply`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#jordan-block-apply).

## Matrix of an endomorphism on a Jordan chain

Let $V$ be a vector space over a field $K$,
let $f$ be a linear endomorphism of $V$, let $\mu \in K$, and let $b_0, \dots, b_d$ be a basis of
$V$ such that $f(b_0) = \mu b_0$ and $f(b_{j+1}) = \mu b_{j+1} + b_j$ for every $j < d$. Then the
matrix of $f$ with respect to the basis $(b_0, \dots, b_d)$ is the Jordan block of size $d + 1$
with eigenvalue $\mu$.

Formalized by `LinearMap.toMatrix_eq_jordanBlock`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#to-matrix-eq-jordan-block).

## Matrix of an endomorphism on a basis of Jordan chains

Let $V$ be a vector space over a
field $K$, let $f$ be a linear endomorphism of $V$, and let $\iota$ be a finite set. For each
$i \in \iota$ let $d_i \in \mathbb{N}$ and $\mu_i \in K$, and let $(b_{i,r})$, indexed by
$i \in \iota$ and $0 \le r \le d_i$, be a basis of $V$ such that $f(b_{i,0}) = \mu_i b_{i,0}$ and
$f(b_{i,j+1}) = \mu_i b_{i,j+1} + b_{i,j}$ for every $i \in \iota$ and every $j < d_i$. Then the
matrix of $f$ with respect to $b$ is the block-diagonal matrix whose $i$-th diagonal block is the
Jordan block of size $d_i + 1$ with eigenvalue $\mu_i$.

Formalized by `LinearMap.toMatrix_eq_blockDiagonal_jordanBlock`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#to-matrix-eq-block-diagonal-jordan-block).

## Jordan chain basis for a nilpotent endomorphism

Let $V$ be a finite-dimensional vector
space over a field $K$ and let $f$ be a nilpotent linear endomorphism of $V$. Then there are
$k \in \mathbb{N}$, natural numbers $d_0, \dots, d_{k-1}$ and a basis $(b_{i,r})$ of $V$, indexed
by $i < k$ and $0 \le r \le d_i$, such that $f(b_{i,0}) = 0$ and $f(b_{i,j+1}) = b_{i,j}$ for
every $i < k$ and every $j < d_i$, and such that the matrix of $f$ with respect to $b$ is the
block-diagonal matrix whose $i$-th diagonal block is the Jordan block of size $d_i + 1$ with
eigenvalue $0$.

Formalized by `Module.End.exists_jordanBasis_of_isNilpotent`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#exists-jordan-basis-of-is-nilpotent).

## Jordan chain basis for an endomorphism with split characteristic polynomial

Let $V$ be
a finite-dimensional vector space over a field $K$ and let $f$ be a linear endomorphism of $V$
whose characteristic polynomial splits into linear factors over $K$. Then there are
$k \in \mathbb{N}$, natural numbers $d_0, \dots, d_{k-1}$, scalars $\mu_0, \dots, \mu_{k-1} \in K$
and a basis $(b_{i,r})$ of $V$, indexed by $i < k$ and $0 \le r \le d_i$, such that
$f(b_{i,0}) = \mu_i b_{i,0}$ and $f(b_{i,j+1}) = \mu_i b_{i,j+1} + b_{i,j}$ for every $i < k$ and
every $j < d_i$, and such that the matrix of $f$ with respect to $b$ is the block-diagonal matrix
whose $i$-th diagonal block is the Jordan block of size $d_i + 1$ with eigenvalue $\mu_i$.

Formalized by `Module.End.exists_jordanBasis_of_charpoly_splits`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#exists-jordan-basis-of-charpoly-splits).

## Jordan normal form

Let $A$ be a square matrix over a field $K$, with rows and columns indexed
by a finite set $N$, whose characteristic polynomial splits into linear factors over $K$. Then $A$
is similar to a block-diagonal matrix of Jordan blocks: there are $k \in \mathbb{N}$, positive
integers $s_0, \dots, s_{k-1}$, scalars $\mu_0, \dots, \mu_{k-1} \in K$, an invertible matrix $P$
with rows and columns indexed by $N$, and a bijection $e$ from the set of pairs $(i, r)$ with
$i < k$ and $r < s_i$ onto $N$, such that $A = P J P^{-1}$, where $J$ is the block-diagonal
matrix whose $i$-th diagonal block is the Jordan block of size $s_i$ with eigenvalue $\mu_i$,
with its rows and columns relabelled by $e$.

Proof: Decompose into the maximal generalized eigenspaces (Axler, Linear Algebra Done Right,
4th ed., 8.22), take a Jordan-chain basis of each nilpotent restriction, and collect them as in
the proof of Axler 8.46. The nilpotent case is proved by induction on the range, extending chains
by preimages and adding kernel vectors, as in Wikipedia, "Jordan normal form", section "A proof".

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 3.4.1.

Formalized by `MathlibExt.LinearAlgebra.Matrix.JordanNormalFormWanted.exists_jordan_normal_form_of_splits`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/JordanNormalForm.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html#exists-jordan-normal-form-of-splits).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jordan normal form](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/jordan-normal-form)
