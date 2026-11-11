---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.DiagonalizationWanted.exists_eigenbasis_of_isSemisimple_of_splits, MathlibExt.LinearAlgebra.DiagonalizationWanted.exists_diagonal_similar_of_splits_of_squarefree_minpoly
statement: formalized
proof: formalized
---

# Diagonalization

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/diagonalization/index.html).

## Eigenbasis of a semisimple endomorphism with split characteristic polynomial

Let $V$ be a
finite-dimensional vector space over a field $K$ and let $f$ be a semisimple endomorphism of $V$
(every $f$-invariant subspace has an $f$-invariant complement) whose characteristic polynomial
splits over $K$. Then for every finite type $\iota$ with exactly $\dim_K V$ elements there are a
basis $(b_i)_{i \in \iota}$ of $V$ and scalars $(\mu_i)_{i \in \iota}$ in $K$ such that each $b_i$
is an eigenvector of $f$ with eigenvalue $\mu_i$.

Proof: The minimal polynomial is squarefree and splits, so it is a product of distinct factors
$X - \mu$. The kernels lemma for these factors, proved by induction from the two-factor case,
shows that the eigenspaces span $V$, and bases of the eigenspaces are collected and reindexed.
This is the diagonalizability criterion derived from the kernels lemma in the French Wikipedia
article *Lemme des noyaux*, <https://fr.wikipedia.org/wiki/Lemme_des_noyaux>.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 1.3.12.

Formalized by `MathlibExt.LinearAlgebra.DiagonalizationWanted.exists_eigenbasis_of_isSemisimple_of_splits`, a theorem declared in [MathlibExt/LinearAlgebra/Diagonalization.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Diagonalization.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/diagonalization/index.html#exists-eigenbasis-of-is-semisimple-of-sp).

## Diagonalizability from a split characteristic polynomial and a squarefree minimal polynomial

Let $K$ be a field and let $A$ be a square matrix over $K$ with rows and columns indexed by a
finite type $n$. If the characteristic polynomial of $A$ splits over $K$ and the minimal
polynomial of $A$ (that is, of the linear map $x \mapsto Ax$ on $K^n$) is squarefree, then there
are matrices $P$ and $D$ over $K$ indexed by $n$, with $D$ diagonal and $P$ invertible, such that
$A = P D P^{-1}$.

Proof: A squarefree minimal polynomial makes the linear map $x \mapsto Ax$ semisimple, so it has a
basis of eigenvectors by the eigenbasis theorem for semisimple endomorphisms; conjugating by the
change-of-basis matrix from the standard basis gives the diagonal form.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 1.3.12.

Formalized by `MathlibExt.LinearAlgebra.DiagonalizationWanted.exists_diagonal_similar_of_splits_of_squarefree_minpoly`, a theorem declared in [MathlibExt/LinearAlgebra/Diagonalization.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Diagonalization.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/diagonalization/index.html#exists-diagonal-similar-of-splits-of-squ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diagonalization](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/diagonalization/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/diagonalization)
