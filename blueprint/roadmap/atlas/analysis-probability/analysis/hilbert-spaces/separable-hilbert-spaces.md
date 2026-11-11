---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.SeparableHilbertBasis.separableSpace_of_countable_hilbertBasis, MathlibExt.Analysis.InnerProductSpace.SeparableHilbertCountableBasis.countable_of_orthonormal, MathlibExt.Analysis.InnerProductSpace.SeparableHilbertCountableBasis.exists_countable_hilbertBasis, MathlibExt.Analysis.InnerProductSpace.SeparableHilbertIsoL2.exists_hilbertBasis_nat, MathlibExt.Analysis.InnerProductSpace.SeparableHilbertIsoL2.separable_hilbert_iso_l2
statement: formalized
proof: formalized
---

# Separable Hilbert spaces

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html).

## A Hilbert space with a countable orthonormal basis is separable

If `H` admits a Hilbert basis indexed by a countable type, then `H` is
separable. No completeness hypothesis is needed: it is the density of the
span of the basis, not completeness, that is used.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SeparableHilbertBasis.separableSpace_of_countable_hilbertBasis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SeparableHilbertBasis.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SeparableHilbertBasis.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html#separable-space-of-countable-hilbert-bas).

## An orthonormal family in a separable space is countable

Let $H$ be a separable inner
product space over $\mathbb{R}$ or $\mathbb{C}$. If $(v_i)_{i \in \iota}$ is an orthonormal family
in $H$, then the index set $\iota$ is countable.

Distinct orthonormal vectors are at distance $\sqrt{2}$, so the open balls of radius $1/2$ around
them are pairwise disjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SeparableHilbertCountableBasis.countable_of_orthonormal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SeparableHilbertCountableBasis.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SeparableHilbertCountableBasis.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html#countable-of-orthonormal).

## A separable Hilbert space admits a countable Hilbert basis

Let $H$ be a separable Hilbert
space over $\mathbb{R}$ or $\mathbb{C}$. Then $H$ has a Hilbert basis $(e_i)_{i \in \iota}$ (an
orthonormal family whose linear span is dense in $H$) indexed by a countable set $\iota$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SeparableHilbertCountableBasis.exists_countable_hilbertBasis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SeparableHilbertCountableBasis.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SeparableHilbertCountableBasis.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html#exists-countable-hilbert-basis).

## An infinite-dimensional separable Hilbert space admits a Hilbert basis indexed by $\mathbb{N}$

**An infinite-dimensional separable Hilbert space admits a Hilbert basis indexed by
$\mathbb{N}$.** Let $H$ be a separable Hilbert space over $\mathbb{R}$ or $\mathbb{C}$ that is not
finite-dimensional. Then $H$ has a Hilbert basis $(e_n)_{n \in \mathbb{N}}$ indexed by the natural
numbers.

A countable Hilbert basis of $H$ has an infinite index set, which is therefore in bijection with
$\mathbb{N}$; reindexing along this bijection gives the basis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SeparableHilbertIsoL2.exists_hilbertBasis_nat`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SeparableHilbertIsoL2.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SeparableHilbertIsoL2.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html#exists-hilbert-basis-nat).

## An infinite-dimensional separable Hilbert space is isometrically isomorphic to $\ell^2$

**An infinite-dimensional separable Hilbert space is isometrically isomorphic to
$\ell^2$.** Let $H$ be a separable Hilbert space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$
that is not finite-dimensional. Then there is a $\mathbb{K}$-linear isometric isomorphism from
$H$ onto $\ell^2(\mathbb{N}, \mathbb{K})$, the space of square-summable sequences in $\mathbb{K}$.

The isomorphism sends a vector to its coefficients with respect to a Hilbert basis of $H$ indexed
by $\mathbb{N}$, so it preserves norms and inner products.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SeparableHilbertIsoL2.separable_hilbert_iso_l2`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SeparableHilbertIsoL2.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SeparableHilbertIsoL2.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html#separable-hilbert-iso-l2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separable Hilbert spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/separable-hilbert-spaces)
