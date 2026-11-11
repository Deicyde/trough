---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.eigenvector_not_mem_span_prefix, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.sub_mem_span_prefix, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.map_mem_span_prefix, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.exists_unit_vector_far, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.finite_eigenvalues_of_ge, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.tendsto_eigenvalue_of_injective, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorNotUnit.not_isUnit_of_isCompactOperator, MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorNotUnit.not_bijective_of_isCompactOperator
statement: formalized
proof: formalized
---

# Spectrum of compact operators

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html).

## Eigenvectors for distinct eigenvalues are not in the span of earlier ones

Let $E$ be a
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a bounded linear operator
on $E$, let $(\lambda_n)_{n \in \mathbb{N}}$ be pairwise distinct scalars in $\mathbb{K}$, and let
$(u_n)_{n \in \mathbb{N}}$ be nonzero vectors in $E$ with $T u_n = \lambda_n u_n$ for every $n$.
Then for every $n$, the vector $u_n$ does not lie in the linear span of $\{u_i : i < n\}$.

This is the non-orthogonal replacement for the orthogonality of eigenspaces used in the
self-adjoint case: it follows from the fact that the eigenspaces of a linear operator form an
independent family.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.eigenvector_not_mem_span_prefix`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#eigenvector-not-mem-span-prefix).

## An operator acts as a scalar on a span of eigenvectors modulo a smaller span

Let $E$ be a
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a bounded linear operator
on $E$, let $(\lambda_n)_{n \in \mathbb{N}}$ in $\mathbb{K}$ and $(u_n)_{n \in \mathbb{N}}$ in $E$
satisfy $T u_n = \lambda_n u_n$ for every $n$, and for each $n$ let $V_n$ be the linear span of
$\{u_i : i < n\}$. Then for every $n$ and every $y \in V_{n+1}$, we have
$T y - \lambda_n y \in V_n$.

The proof is induction on the span: each generator $u_i$ with $i < n$ contributes
$(\lambda_i - \lambda_n) u_i$ and the generator $u_n$ contributes $0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.sub_mem_span_prefix`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#sub-mem-span-prefix).

## Invariance of spans of eigenvectors

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a bounded linear operator on $E$, and let
$(\lambda_n)_{n \in \mathbb{N}}$ in $\mathbb{K}$ and $(u_n)_{n \in \mathbb{N}}$ in $E$ satisfy
$T u_n = \lambda_n u_n$ for every $n$. Then for every $n$ and every $y$ in the linear span of
$\{u_i : i \le n\}$, the vector $T y$ also lies in that span.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.map_mem_span_prefix`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#map-mem-span-prefix).

## Riesz separation for nested spans

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be vectors in $E$, and
for each $n$ let $V_n$ be the linear span of $\{u_i : i < n\}$. Suppose $u_n \notin V_n$ for
every $n$. Then for every $n$ there is a vector $y \in V_{n+1}$ with $\|y\| = 1$ and
$\|y - z\| \ge 1/2$ for every $z \in V_n$.

This is Riesz's lemma for the finite-dimensional, hence closed, subspace $V_n$: one takes $y$ to be
the normalization of $u_n - z$ for a $z \in V_n$ almost realizing the distance $d > 0$ from
$u_n$ to $V_n$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.exists_unit_vector_far`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#exists-unit-vector-far).

## Finiteness of eigenvalues of a compact operator bounded away from zero

Let $E$ be a normed
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact bounded linear operator
on $E$, and let $\varepsilon > 0$ be real. Then the set of eigenvalues $\mu \in \mathbb{K}$ of $T$
with $|\mu| \ge \varepsilon$ is finite.

If it were infinite, distinct eigenvalues $\lambda_n$ with eigenvectors $u_n$ would give, by Riesz
separation for the spans of the $u_n$, unit vectors $y_n$ whose images $T y_n$ are pairwise at
distance at least $\varepsilon / 2$, contradicting compactness of $T$. No self-adjointness, inner
product or completeness is needed.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.finite_eigenvalues_of_ge`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#finite-eigenvalues-of-ge).

## Eigenvalues of a compact operator tend to zero along any injective sequence

Let $E$ be a
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $T$ be a compact bounded linear
operator on $E$. If $(\lambda_n)_{n \in \mathbb{N}}$ is a sequence of pairwise distinct eigenvalues
of $T$, then $\lambda_n \to 0$ as $n \to \infty$.

Otherwise some $\varepsilon > 0$ would satisfy $|\lambda_n| \ge \varepsilon$ for infinitely many
$n$, giving infinitely many eigenvalues of modulus at least $\varepsilon$, which contradicts the
finiteness of eigenvalues of a compact operator bounded away from zero.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorEigenvalues.tendsto_eigenvalue_of_injective`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorEigenvalues.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#tendsto-eigenvalue-of-injective).

## A compact operator on an infinite-dimensional space is not a unit

If `T` is compact and `E` is infinite-dimensional, then `T` has no
two-sided inverse among bounded operators. (Completeness of `E` is not
needed for this statement.)

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorNotUnit.not_isUnit_of_isCompactOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#not-is-unit-of-is-compact-operator).

## A compact operator on an infinite-dimensional Banach space is not bijective

Let $E$ be an
infinite-dimensional Banach space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $T$ be a
compact bounded linear operator on $E$. Then $T$ is not bijective.

By the bounded inverse theorem, a bijective bounded operator on a Banach space has a bounded
inverse, so this follows from the fact that a compact operator on an infinite-dimensional space
has no bounded two-sided inverse.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorNotUnit.not_bijective_of_isCompactOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#not-bijective-of-is-compact-operator).

## Zero lies in the spectrum of a compact operator on an infinite-dimensional space

Let $E$ be
an infinite-dimensional normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $T$ be
a compact bounded linear operator on $E$. Then $0$ lies in the spectrum of $T$ in the algebra of
bounded linear operators on $E$; that is, $T$ has no bounded two-sided inverse.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CompactOperatorNotUnit.zero_mem_spectrum_of_isCompactOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CompactOperatorNotUnit.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html#zero-mem-spectrum-of-is-compact-operator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectrum of compact operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/spectrum-of-compact-operators)
