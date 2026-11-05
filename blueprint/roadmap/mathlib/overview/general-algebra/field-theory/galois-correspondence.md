---
article_id: af_714e0da6589ec6693a6ae524
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsGalois.intermediateFieldEquivSubgroup
mathlib_file: Mathlib/FieldTheory/Galois/Basic.lean
---

# Galois correspondence

The **Galois correspondence**, also called the fundamental theorem of Galois theory,
says that for a finite Galois extension of [fields](field.md) $E/F$ the intermediate
fields of the extension are in one-to-one, inclusion-reversing correspondence with the
[subgroups](../group-theory/part-01/subgroup.md) of its Galois group. It turns questions about fields, which
can be infinite and hard to enumerate, into questions about a finite group, and it is the
basis of the classical applications of Galois theory, such as the
[insolvability of the general quintic by radicals](../../../hundred-theorems/part-01/insolvability-of-general-higher-degree-equations.md).

## Statement

Let $E/F$ be a field extension. Its Galois group $\mathrm{Gal}(E/F)$ is the group of
field automorphisms of $E$ that fix every element of $F$. The extension is Galois if it is
[normal and separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#isGalois_iff): every element of $E$ is algebraic over $F$, and its
minimal polynomial over $F$ splits into linear factors in $E$ and has no repeated roots. For an extension of
finite degree, [being Galois is equivalent](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.tfae) to each of: the elements of
$E$ fixed by all of $\mathrm{Gal}(E/F)$ are exactly those of $F$; the group has exactly
$[E:F]$ elements, where the degree $[E:F]$ is the dimension of $E$ as a vector space over $F$; $E$ is the [splitting field](splitting-field.md) of a
[separable polynomial](../polynomials-and-power-series/separable-polynomial.md) over $F$.

To a subgroup $H$ of $\mathrm{Gal}(E/F)$ attach its
[fixed field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixedField)
$E^H = \{x \in E : \sigma(x) = x \text{ for all } \sigma \in H\}$, and to an intermediate
field $F \subseteq K \subseteq E$ attach the
[subgroup of automorphisms fixing $K$ pointwise](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroup),
which is [isomorphic to $\mathrm{Gal}(E/K)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroupEquiv)
and is denoted that way. For any extension, $K \subseteq E^H$ holds
[exactly when $H \subseteq \mathrm{Gal}(E/K)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.le_fixedField_iff_le_fixingSubgroup),
so both maps reverse inclusions.

**Theorem.** If $E/F$ is a finite Galois extension, then $K \mapsto \mathrm{Gal}(E/K)$ and
$H \mapsto E^H$ are mutually inverse,
[inclusion-reversing bijections](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.intermediateFieldEquivSubgroup) between the
intermediate fields of $E/F$ and the subgroups of $\mathrm{Gal}(E/F)$. Moreover, if $K$
corresponds to $H$, then

$$|H| = [E:K], \qquad [K:F] = [\mathrm{Gal}(E/F) : H].$$

Both formulas are in Mathlib ([the first](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.card_fixingSubgroup_eq_finrank),
[the second](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.finrank_eq_fixingSubgroup_index)); the right-hand
side of the second is the [index](../group-theory/part-01/index-of-a-subgroup.md) of $H$. Finally, $K$ is Galois over
$F$ [if and only if $H$ is a normal subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Infinite.html#InfiniteGalois.normal_iff_isGalois) of
$\mathrm{Gal}(E/F)$, and in that case
[restriction to $K$ induces an isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.normalAutEquivQuotient) from the
[quotient group](../group-theory/part-01/quotient-group.md) $\mathrm{Gal}(E/F)/H$ onto $\mathrm{Gal}(K/F)$.

## Examples

- **A biquadratic field.** Let $E = \mathbb{Q}(\sqrt2, \sqrt3)$, the splitting field of
  $(x^2-2)(x^2-3)$ over $\mathbb{Q}$, of degree $4$. Its Galois group has four elements:
  the identity, $\sigma$ sending $\sqrt2$ to $-\sqrt2$ and fixing $\sqrt3$, $\tau$ sending
  $\sqrt3$ to $-\sqrt3$ and fixing $\sqrt2$, and $\sigma\tau$. It has five subgroups, and the correspondence pairs them with five
  fields: the trivial group with $E$, $\{1, \sigma\}$ with $\mathbb{Q}(\sqrt3)$,
  $\{1, \tau\}$ with $\mathbb{Q}(\sqrt2)$, $\{1, \sigma\tau\}$ with $\mathbb{Q}(\sqrt6)$,
  and the whole group with $\mathbb{Q}$. The group is abelian, so every intermediate field is
  Galois over $\mathbb{Q}$.
- **A cubic.** Let $E = \mathbb{Q}(\sqrt[3]{2}, \omega)$ with $\omega$ a primitive cube root
  of unity, the splitting field of $x^3 - 2$. It has degree $6$, and its Galois group permutes
  the three roots $\sqrt[3]{2}, \omega\sqrt[3]{2}, \omega^2\sqrt[3]{2}$ as the full symmetric
  group $S_3$. The three subgroups of order $2$ correspond to the cubic fields
  $\mathbb{Q}(\omega^i\sqrt[3]{2})$, none of them Galois over $\mathbb{Q}$, matching the fact
  that these subgroups are not normal. The normal subgroup of order $3$ corresponds to the
  quadratic field $\mathbb{Q}(\omega) = \mathbb{Q}(\sqrt{-3})$, which is Galois.

## Properties

- **Extreme cases.** The whole field $E$ corresponds to the
  [trivial subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroup_top) and $F$ to the
  [whole group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroup_bot); for a finite Galois extension the
  [fixed field of the whole group is $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.fixedField_top).
- **Lattice operations.** Since the bijection reverses order, it exchanges joins and meets:
  the subgroup fixing the compositum $KL$ is
  [the intersection of the subgroups fixing $K$ and $L$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroup_sup).
- **Conjugation.** For $\sigma$ in the Galois group, the subgroup fixing $\sigma(K)$ is
  [the conjugate $\sigma\,\mathrm{Gal}(E/K)\,\sigma^{-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.map_fixingSubgroup),
  so conjugate subgroups correspond to conjugate fields, as in the cubic example.

## Proof

The two halves use different hypotheses. Let $H$ be a subgroup of $\mathrm{Gal}(E/F)$ with
$E/F$ finite. Every element of $H$ fixes $E^H$, so $H \subseteq \mathrm{Gal}(E/E^H)$. A finite
extension has [at most as many automorphisms as its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Fixed.html#AlgEquiv.card_le); applied to
$E/E^H$, which is finite because $E/F$ is, this bounds $|\mathrm{Gal}(E/E^H)|$ by $[E:E^H]$.
Artin's theorem gives [$[E:E^H] = |H|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.finrank_fixedField_eq_card),
so $\mathrm{Gal}(E/E^H)$ has at most $|H|$ elements and
[equals $H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IntermediateField.fixingSubgroup_fixedField). This half needs no Galois
hypothesis.

Conversely, let $K$ be an intermediate field. Clearly $K \subseteq E^{\mathrm{Gal}(E/K)}$.
Since $E$ is Galois over $F$, it is
[also Galois over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.tower_top_of_isGalois), so
$|\mathrm{Gal}(E/K)| = [E:K]$ ([the count for Galois extensions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.card_aut_eq_finrank)).
By Artin's theorem $E$ has the same degree $[E:K]$ over the larger field
$E^{\mathrm{Gal}(E/K)}$, and the tower law forces the two fields to be equal:
[$K$ is the fixed field of $\mathrm{Gal}(E/K)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.fixedField_fixingSubgroup).
The two maps are therefore inverse, and they reverse inclusions.

## Generalizations

For a Galois extension of infinite degree, every intermediate field is still
[the fixed field of its subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Infinite.html#InfiniteGalois.fixedField_fixingSubgroup), but in general
not every subgroup arises this way. The Galois group carries a natural profinite topology, the
Krull topology, and intermediate fields correspond
[bijectively to the closed subgroups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Infinite.html#InfiniteGalois.IntermediateFieldEquivClosedSubgroup).

For an arbitrary extension the two maps still form a Galois connection between ordered sets,
as the inclusion criterion in the statement shows; for an extension of finite degree, the
Galois condition is what makes them inverse bijections. Among the uses of the correspondence is
[the theorem that a polynomial solvable by radicals has a solvable Galois group](abel-ruffini-theorem-one-direction.md).

## In Mathlib

Mathlib packages the correspondence as an order isomorphism between the lattice of
intermediate fields and the order dual of the lattice of subgroups of the Galois group,
which records in one object that the two maps are inverse and reverse inclusions. The
subgroup attached to an intermediate field $K$ is a subgroup of $\mathrm{Gal}(E/F)$, not the
group $\mathrm{Gal}(E/K)$ itself; a separate isomorphism identifies the two. A Galois extension
is defined as a normal and separable one, with no finiteness condition, and separability
includes algebraicity, so finite degree is a separate hypothesis wherever the theorem needs
it. Several statements hold more generally than the textbook version: the degree formula
$[K:F] = [\mathrm{Gal}(E/F):H]$ and the equivalence between normal subgroups and Galois
subextensions are proved for Galois extensions of any degree, with the convention that the
degree of an infinite extension and the index of an infinite-index subgroup are both $0$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Algebraic extension](algebraic-extension.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Index of a subgroup](../group-theory/part-01/index-of-a-subgroup.md)
- [Normal subgroup](../group-theory/part-01/normal-subgroup.md)
- [Quotient group](../group-theory/part-01/quotient-group.md)

## Sources

- [Mathlib documentation: `IsGalois.intermediateFieldEquivSubgroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.intermediateFieldEquivSubgroup)
- [Source of `IsGalois.intermediateFieldEquivSubgroup` in Mathlib/FieldTheory/Galois/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Galois/Basic.lean#L369)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L134)
