---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteEigenvalues.norm_hasEigenvalue_le, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteEigenvalues.finite_eigenvalues_of_ge, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointNormEigenvalue.exists_hasEigenvalue_norm_eq, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointNormEigenvalue.exists_unit_eigenvector_real_eigenvalue, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointDeflation.exists_next_eigenvector_of_invariant, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointDeflation.exists_next_eigenvector_of_finite_eigenvectors, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteRankApprox.exists_finiteRank_approx, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointMaximumPrinciple.exists_nonzero_eigenvalue_enumeration
statement: formalized
proof: formalized
---

# Spectral theorem for compact self-adjoint operators

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html).

## Eigenvalues are bounded by the operator norm

Let $T$ be a bounded linear operator on an
inner product space over $\mathbb{R}$ or $\mathbb{C}$. Every eigenvalue $\mu$ of $T$ satisfies
$|\mu| \le \|T\|$.

Indeed, if $Tx = \mu x$ with $x \neq 0$, then $|\mu| \, \|x\| = \|Tx\| \le \|T\| \, \|x\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteEigenvalues.norm_hasEigenvalue_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteEigenvalues.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteEigenvalues.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#norm-has-eigenvalue-le).

## Finiteness of large eigenvalues of a compact self-adjoint operator

Let $T$ be a compact
self-adjoint operator on a Hilbert space over $\mathbb{R}$ or $\mathbb{C}$. For every
$\varepsilon > 0$, the set of eigenvalues $\mu$ of $T$ with $\varepsilon \le |\mu|$ is finite.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteEigenvalues.finite_eigenvalues_of_ge`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteEigenvalues.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteEigenvalues.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#finite-eigenvalues-of-ge).

## A nonzero compact self-adjoint operator has an eigenvalue of modulus equal to its norm

Let $T \neq 0$ be a compact self-adjoint operator on a Hilbert space $H$ over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Then $T$ has an eigenvalue $\mu \in \mathbb{K}$ with
$\mu \neq 0$ and $|\mu| = \|T\|$, where $\|T\|$ is the operator norm of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointNormEigenvalue.exists_hasEigenvalue_norm_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointNormEigenvalue.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointNormEigenvalue.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-has-eigenvalue-norm-eq).

## A nonzero compact self-adjoint operator has a real eigenvalue of modulus equal to its norm, with a unit eigenvector

**A nonzero compact self-adjoint operator has a real eigenvalue of modulus equal to its norm,
with a unit eigenvector.** Let $T \neq 0$ be a compact self-adjoint operator on a Hilbert space
$H$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Then there are a real number $r$ and a unit
vector $u \in H$ with $T u = r u$ and $|r| = \|T\|$, where $\|T\|$ is the operator norm of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointNormEigenvalue.exists_unit_eigenvector_real_eigenvalue`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointNormEigenvalue.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointNormEigenvalue.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-unit-eigenvector-real-eigenvalue).

## Deflation step

Let $T$ be a compact self-adjoint operator on a Hilbert space $H$ over
$\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of $H$ that admits an orthogonal
projection $P : H \to H$ onto $S$ and satisfies $T(S) \subseteq S$, and let $T_1 = PTP$ be the
compression of $T$ to $S$. If $T_1 \neq 0$, then there are a real number $r$ and a unit vector
$v \in S$ with $Tv = rv$, $|r| = \|T_1\|$ and $|r| \le \|T\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointDeflation.exists_next_eigenvector_of_invariant`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointDeflation.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointDeflation.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-next-eigenvector-of-invariant).

## Next eigenvalue after a finite family of eigenvectors

Let $T$ be a compact self-adjoint
operator on a Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$, let $u_1, \dots, u_n \in H$ and
scalars $\mu_1, \dots, \mu_n$ satisfy $T u_i = \mu_i u_i$ for every $i$, and let $S$ be the
orthogonal complement of the span of $u_1, \dots, u_n$. If $Tz \neq 0$ for some $z \in S$, then
there are a real number $r$ and a unit vector $v$ with $\langle v, u_i \rangle = 0$ for every $i$,
$Tv = rv$ and $\langle Tv, v \rangle = r$, such that $|\langle Tx, x \rangle| \le |r|$ for
every unit vector $x \in S$. In particular $v \in S$, so $|r|$ is the maximum of
$|\langle Tx, x \rangle|$ over unit vectors $x \in S$.

The vectors $u_i$ need not be orthonormal, or even nonzero.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointDeflation.exists_next_eigenvector_of_finite_eigenvectors`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointDeflation.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointDeflation.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-next-eigenvector-of-finite-eigenv).

## Finite-rank approximation of compact self-adjoint operators

Let $T$ be a compact
self-adjoint operator on a Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$. For every
$\varepsilon > 0$ there is a bounded self-adjoint operator $F$ on $H$ with finite-dimensional
range such that $\|T - F\| \le \varepsilon$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFiniteRankApprox.exists_finiteRank_approx`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteRankApprox.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFiniteRankApprox.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-finite-rank-approx).

## Maximum principle for compact self-adjoint operators

Let $T$ be a compact self-adjoint
operator on a Hilbert space $H$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Then one of the
following two alternatives holds.

Either there are $N \in \mathbb{N}$ (possibly $N = 0$, as for $T = 0$), nonzero real numbers
$s_0, \dots, s_{N-1}$ and an orthonormal family $u_0, \dots, u_{N-1}$ in $H$ such that
$T u_i = s_i u_i$ for every $i < N$, $|s_0| \ge |s_1| \ge \dots \ge |s_{N-1}|$, for every $i < N$
every unit vector $x \in H$ orthogonal to $u_0, \dots, u_{i-1}$ satisfies
$|\langle T x, x \rangle| \le |s_i|$ while $|\langle T u_i, u_i \rangle| = |s_i|$, and $T x = 0$
for every $x \in H$ orthogonal to all of $u_0, \dots, u_{N-1}$.

Or there are nonzero real numbers $s_0, s_1, s_2, \dots$ and an orthonormal sequence
$u_0, u_1, u_2, \dots$ in $H$ such that $T u_n = s_n u_n$ for every $n$, the sequence $|s_n|$ is
nonincreasing and tends to $0$ as $n \to \infty$, for every $n$ every unit vector $x \in H$
orthogonal to $u_0, \dots, u_{n-1}$ satisfies $|\langle T x, x \rangle| \le |s_n|$ while
$|\langle T u_n, u_n \rangle| = |s_n|$, and $T x = 0$ for every $x \in H$ orthogonal to every
$u_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointMaximumPrinciple.exists_nonzero_eigenvalue_enumeration`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-nonzero-eigenvalue-enumeration).

## Maximum principle for compact self-adjoint operators in finite dimension

Let $H$ be a
finite-dimensional Hilbert space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $T$ be a
compact self-adjoint operator on $H$. Then there are $N \in \mathbb{N}$, nonzero real numbers
$s_0, \dots, s_{N-1}$ and an orthonormal family $u_0, \dots, u_{N-1}$ in $H$ such that
$T u_i = s_i u_i$ for every $i < N$, $|s_0| \ge |s_1| \ge \dots \ge |s_{N-1}|$, and for every
$i < N$ every unit vector $x \in H$ orthogonal to $u_0, \dots, u_{i-1}$ satisfies
$|\langle T x, x \rangle| \le |s_i|$, while $|\langle T u_i, u_i \rangle| = |s_i|$. Moreover
$T x = 0$ for every $x \in H$ orthogonal to all of $u_0, \dots, u_{N-1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointMaximumPrinciple.exists_finite_eigenvalue_enumeration`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-finite-eigenvalue-enumeration).

## Maximum principle as a sequence in infinite dimension

Let $T$ be a compact self-adjoint
operator on an infinite-dimensional Hilbert space $H$ over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$. Then there are real numbers $s_0, s_1, s_2, \dots$ and an orthonormal sequence
$u_0, u_1, u_2, \dots$ in $H$ such that $T u_n = s_n u_n$ and $|s_{n+1}| \le |s_n|$ for every
$n$, $|s_n| \to 0$ as $n \to \infty$, and for every $n$ every unit vector $x \in H$ orthogonal to
$u_0, \dots, u_{n-1}$ satisfies $|\langle T x, x \rangle| \le |s_n|$, while
$|\langle T u_n, u_n \rangle| = |s_n|$.

Unlike the maximum principle for compact self-adjoint operators, the $s_n$ are not required to be
nonzero, and no claim is made that $T$ vanishes on the vectors orthogonal to every $u_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointMaximumPrinciple.exists_ordered_eigenvalue_sequence`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointMaximumPrinciple.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#exists-ordered-eigenvalue-sequence).

## Orthogonal complement of the nonzero-eigenvalue eigenspaces

Let $H$ be a Hilbert space
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $T : H \to H$ be a compact self-adjoint
bounded linear operator. Then the orthogonal complement of the subspace spanned by the
eigenspaces $\ker(T - \mu I)$ for all nonzero $\mu \in \mathbb{K}$ equals the kernel of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointRangeDecomposition.orthogonal_iSup_eigenspaces_ne_zero_eq_ker`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointRangeDecomposition.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointRangeDecomposition.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#orthogonal-i-sup-eigenspaces-ne-zero-eq).

## Spectral theorem for compact self-adjoint operators (range decomposition form)

**Spectral theorem for compact self-adjoint operators (range
decomposition form).** Let $H$ be a Hilbert space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$
and let $T : H \to H$ be a compact self-adjoint bounded linear operator. Then:
(1) the closure of the subspace spanned by the eigenspaces $\ker(T - \mu I)$ for all
nonzero $\mu \in \mathbb{K}$ equals the closure of the range of $T$;
(2) the closure of the range of $T$ and the kernel of $T$ are complementary subspaces: their
intersection is $\{0\}$ and their sum is $H$; and
(3) the eigenspaces $\ker(T - \mu I)$, $\mu \in \mathbb{K}$, are pairwise orthogonal for distinct
values of $\mu$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointRangeDecomposition.spectral_theorem_range_decomposition`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointRangeDecomposition.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointRangeDecomposition.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html#spectral-theorem-range-decomposition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectral theorem for compact self-adjoint operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-compact-self-adjoint-operat)
