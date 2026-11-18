---
declaration: module
origin: cited
lean: CondensedMatter.Bloch.RegularRep.measurePreserving_addRight, CondensedMatter.Bloch.RegularRep.shift, CondensedMatter.Bloch.RegularRep.translations, CondensedMatter.Bloch.RegularRep.measurePreserving_translations, CondensedMatter.Bloch.RegularRep.Space, CondensedMatter.Bloch.RegularRep.translation, CondensedMatter.Bloch.RegularRep.pointwise, CondensedMatter.Bloch.RegularRep.pointwise_apply_ae
statement: formalized
proof: formalized
---

# The space of wavefunctions on a lattice with internal states

The module `PhyslibAlpha.CondensedMatter.Bloch.RegularRep`, [PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean): 24 declarations, 14 with a docstring.

> `ℓ²(G, ℂ^N)` with its translation representation and its internal matrix algebra.

## i. Overview

> The Hilbert space `ℓ²(G, ℂ^N)` of square-summable functions on a countable abelian group `G` with
> values in `ℂ^N` carries two commuting structures: the translations `(U_g ψ)(x) = ψ(x - g)`, a
> unitary representation of `G`, and the pointwise action of the matrices `M_N(ℂ)` on the internal
> index. This is the setting of band theory: `G` is the lattice of translations of a crystal, and `N`
> the number of internal states per primitive cell. The space is realized as `L²` of the counting
> measure so that the Koopman representation of the translation action applies.

## ii. Key results

> - `RegularRep.translation` : the translation representation on `ℓ²(G, ℂ^N)`.
> - `RegularRep.internal` : the internal ⋆-homomorphism `M_N(ℂ) → B(ℓ²)`.
> - `RegularRep.commute` : the translations commute with the internal algebra.

## iv. References

> * None.

## A. Counting measure and translations

**`CondensedMatter.Bloch.RegularRep.measurePreserving_addRight`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L67).

> Translation of a discrete group preserves the counting measure.

```lean
lemma measurePreserving_addRight (g : G) :
    MeasurePreserving (fun x : G => x + g) (Measure.count : Measure G) Measure.count
```

**`CondensedMatter.Bloch.RegularRep.shift`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L85).

> Translation by `a`, as a permutation of the group.

```lean
def shift (a : G) : Equiv.Perm G
```

**`CondensedMatter.Bloch.RegularRep.translations`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L92).

> The translation action of the group on itself, as permutations.

```lean
def translations : Multiplicative G →* Equiv.Perm G
```

**`CondensedMatter.Bloch.RegularRep.measurePreserving_translations`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L100).

```lean
lemma measurePreserving_translations (g : Multiplicative G) :
    MeasurePreserving (translations g) (Measure.count : Measure G) Measure.count
```

**`CondensedMatter.Bloch.RegularRep.Space`**, an abbrev, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L108).

> The Hilbert space `ℓ²(G, ℂ^N)` of square-summable functions on `G` with values in the internal
> space `ℂ^N`, as `L²` of the counting measure.

```lean
abbrev Space
```

**`CondensedMatter.Bloch.RegularRep.translation`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L111).

> **The translation representation** on `ℓ²(G, ℂ^N)`: `(U_g ψ)(x) = ψ(x - g)`.

```lean
def translation : Multiplicative G →* unitary (Space G N →L[ℂ] Space G N)
```

## B. The internal algebra

**`CondensedMatter.Bloch.RegularRep.pointwise`**, an abbrev, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L121).

> Pointwise action of an operator of the internal space on `ℓ²(G, ℂ^N)`.

```lean
abbrev pointwise (L : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N)) :
    Space G N →L[ℂ] Space G N
```

**`CondensedMatter.Bloch.RegularRep.pointwise_apply_ae`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L126).

```lean
lemma pointwise_apply_ae (L : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N))
    (f : Space G N) : pointwise G N L f =ᵐ[Measure.count] fun x => L (f x)
```

**`CondensedMatter.Bloch.RegularRep.pointwise_mul`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L131).

```lean
lemma pointwise_mul (A B : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N)) :
    pointwise G N (A * B) = pointwise G N A * pointwise G N B
```

**`CondensedMatter.Bloch.RegularRep.pointwise_one`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L143).

```lean
lemma pointwise_one : pointwise G N (1 : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N)) =
    1
```

**`CondensedMatter.Bloch.RegularRep.pointwise_star`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L153).

```lean
lemma pointwise_star (L : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N)) :
    pointwise G N (star L) = star (pointwise G N L)
```

**`CondensedMatter.Bloch.RegularRep.internal`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L166).

> **The internal algebra**: a matrix acts on the internal index of a wavefunction, pointwise.

```lean
def internal : Matrix (Fin N) (Fin N) ℂ →⋆ₐ[ℂ] (Space G N →L[ℂ] Space G N)
```

## C. The translation commutes with the internal algebra

**`CondensedMatter.Bloch.RegularRep.translation_apply`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L196).

```lean
lemma translation_apply (g : Multiplicative G) (f : Space G N) :
    ((translation G N g : unitary (Space G N →L[ℂ] Space G N)) : Space G N →L[ℂ] Space G N) f =
      Lp.compMeasurePreserving (translations g⁻¹) (measurePreserving_translations g⁻¹) f
```

**`CondensedMatter.Bloch.RegularRep.commute_translation_internal`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L203).

> The translations commute with the internal algebra: the matrices act on the internal index and
> the translations move the site.

```lean
lemma commute_translation_internal (g : Multiplicative G) (M : Matrix (Fin N) (Fin N) ℂ) :
    Commute ((translation G N g : unitary (Space G N →L[ℂ] Space G N)) :
      Space G N →L[ℂ] Space G N) (internal M)
```

## D. Localized states and their momentum distribution

**`CondensedMatter.Bloch.RegularRep.localized`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L227).

> The state localized at the origin with internal state `e`.

```lean
def localized (e : EuclideanSpace ℂ (Fin N)) : Space G N
```

**`CondensedMatter.Bloch.RegularRep.count_preimage_ne_top`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L230).

```lean
lemma count_preimage_ne_top (g : Multiplicative G) :
    (Measure.count : Measure G) ((translations g⁻¹) ⁻¹' {(0 : G)}) ≠ ⊤
```

**`CondensedMatter.Bloch.RegularRep.translation_localized`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L237).

> Translating a localized state moves it to the translated site.

```lean
lemma translation_localized (g : Multiplicative G) (e : EuclideanSpace ℂ (Fin N)) :
    ((translation G N g : unitary (Space G N →L[ℂ] Space G N)) : Space G N →L[ℂ] Space G N)
        (localized e) =
      indicatorConstLp 2 ((measurableSet_singleton (0 : G)).preimage
        (measurable_of_countable (translations g⁻¹))) (count_preimage_ne_top g) e
```

**`CondensedMatter.Bloch.RegularRep.inner_localized_translation`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L246).

> **The matrix coefficients of a localized state are the Kronecker delta.**

```lean
lemma inner_localized_translation (g : Multiplicative G) (e e' : EuclideanSpace ℂ (Fin N)) :
    ⟪localized (G := G) e, ((translation G N g : unitary (Space G N →L[ℂ] Space G N)) :
      Space G N →L[ℂ] Space G N) (localized e')⟫_ℂ = if g = 1 then ⟪e, e'⟫_ℂ else 0
```

**`CondensedMatter.Bloch.RegularRep.pointwise_localized`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L272).

```lean
lemma pointwise_localized (L : EuclideanSpace ℂ (Fin N) →L[ℂ] EuclideanSpace ℂ (Fin N))
    (e : EuclideanSpace ℂ (Fin N)) : pointwise G N L (localized e) = localized (L e)
```

**`CondensedMatter.Bloch.RegularRep.localized_add`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L286).

```lean
lemma localized_add (e e' : EuclideanSpace ℂ (Fin N)) :
    localized (G := G) (e + e') = localized e + localized e'
```

**`CondensedMatter.Bloch.RegularRep.localized_smul`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L305).

```lean
lemma localized_smul (c : ℂ) (e : EuclideanSpace ℂ (Fin N)) :
    localized (G := G) (c • e) = c • localized e
```

## E. The momentum distribution of localized states

**`CondensedMatter.Bloch.RegularRep.vectorMeasure_localized`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L330).

> **A localized state has a uniform momentum distribution**: its spectral measure for the
> translations is the Haar measure of the dual group, weighted by the squared norm of the internal
> state.

```lean
lemma vectorMeasure_localized (e : EuclideanSpace ℂ (Fin N)) :
    UnitaryRep.vectorMeasure (translation G N) (localized e) =
      ENNReal.ofReal (‖e‖ ^ 2) • dualHaar (G := G)
```

**`CondensedMatter.Bloch.RegularRep.projection_localized_ne_zero`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L351).

> The spectral projection of a nonempty open set of crystal momenta does not annihilate a
> localized state of nonzero internal state.

```lean
lemma projection_localized_ne_zero {U : Set (PontryaginDual (Multiplicative G))}
    (hU : IsOpen U) (hne : U.Nonempty) {e : EuclideanSpace ℂ (Fin N)} (he : e ≠ 0) :
    UnitaryRep.projection (translation G N) U (localized e) ≠ 0
```

**`CondensedMatter.Bloch.RegularRep.hasFullSupport`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean#L366).

> **The regular representation has full support**: every crystal momentum occurs in every
> internal state.

```lean
lemma hasFullSupport :
    UnitaryRep.HasFullSupport (translation G N) (internal (G := G) (N := N))
```

## Depends on

- [Bloch–Floquet theory for representations with a finite-dimensional internal space](../../probabilistictheory/representation/floquet.md)
- [The Koopman representation of a measure-preserving action](../../probabilistictheory/representation/koopman.md)
- [Orthogonality of characters](../../probabilistictheory/representation/orthogonality.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/RegularRep.lean)
