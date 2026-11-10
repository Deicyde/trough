---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormallyEtale, AlgebraicGeometry.FormallyEtale.existsUnique_lift, AlgebraicGeometry.FormallyEtale.comp, AlgebraicGeometry.FormallyEtale.pullback_snd, AlgebraicGeometry.FormallyEtale.resLE, AlgebraicGeometry.formallyEtale_iff_isIso_inclusion, AlgebraicGeometry.formallyEtale_iff_isZero_universalConormalSheaf, AlgebraicGeometry.formallyEtale_iff_isZero_relativeDifferentials_and_universalConormalSheaf
statement: formalized
proof: formalized
---

# 37.8 Formally étale morphisms

Section 37.8 of the Stacks Project, [Tag 02HF](https://stacks.math.columbia.edu/tag/02HF). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02HG, a definition

[Tag 02HG](https://stacks.math.columbia.edu/tag/02HG) in the Stacks Project.

**`AlgebraicGeometry.FormallyEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleScheme.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleScheme.lean#L118). References: EGA IV (17.1.1); SGA 3 XI (1.1).

> A morphism of schemes `f : X ⟶ S` is **formally étale** when it has the unique infinitesimal
> lifting property: for every first-order thickening `i : T ⟶ T'` of affine schemes, every
> commutative square
> ```
> T  --g--→ X
> |         |
> i         f
> ↓         ↓
> T' --p--→ S
> ```
> has exactly one diagonal filler `h : T' ⟶ X`, that is exactly one morphism with `i ≫ h = g` and
> `h ≫ f = p`.

```lean
abbrev FormallyEtale {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 04FD, a lemma

[Tag 04FD](https://stacks.math.columbia.edu/tag/04FD) in the Stacks Project.

**`AlgebraicGeometry.FormallyEtale.existsUnique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Lifting.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Lifting.lean#L78).

> A formally étale morphism admits a unique lift across any first-order
> thickening of schemes over its base, without affineness assumptions.

```lean
theorem FormallyEtale.existsUnique_lift
    {X S T T' : Scheme.{u}} (f : X ⟶ S) (hf : FormallyEtale f)
    (i : T ⟶ T') (hi : IsFirstOrderThickening i)
    (p : T' ⟶ S) (g : T ⟶ X) (hg : g ≫ f = i ≫ p) :
    ∃! h : T' ⟶ X, i ≫ h = g ∧ h ≫ f = p
```

## Tag 02HI, a lemma

[Tag 02HI](https://stacks.math.columbia.edu/tag/02HI) in the Stacks Project.

**`AlgebraicGeometry.FormallyEtale.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean#L51).

> A composition of formally étale morphisms is formally étale.

```lean
theorem FormallyEtale.comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    (hf : FormallyEtale f) (hg : FormallyEtale g) :
    FormallyEtale (f ≫ g)
```

## Tag 02HJ, a lemma

[Tag 02HJ](https://stacks.math.columbia.edu/tag/02HJ) in the Stacks Project.

**`AlgebraicGeometry.FormallyEtale.pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean#L63).

> A base change of a formally étale morphism is formally étale.

```lean
theorem FormallyEtale.pullback_snd {X S S' : Scheme.{u}}
    (f : X ⟶ S) (g : S' ⟶ S) (hf : FormallyEtale f) :
    FormallyEtale (pullback.snd f g)
```

## Tag 02HK, a lemma

[Tag 02HK](https://stacks.math.columbia.edu/tag/02HK) in the Stacks Project.

**`AlgebraicGeometry.FormallyEtale.resLE`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean#L85).

> Formal étaleness is preserved when a morphism is restricted to compatible open subschemes of
> its source and target.

```lean
lemma FormallyEtale.resLE {X S : Scheme.{u}} (f : X ⟶ S)
    (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V)
    (hf : FormallyEtale f) :
    FormallyEtale (f.resLE V U hUV)
```

## Tag 04FE, a lemma

[Tag 04FE](https://stacks.math.columbia.edu/tag/04FE) in the Stacks Project.

**`AlgebraicGeometry.formallyEtale_iff_isIso_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean#L95). The attribute's comment: “equivalence of (1) and (2)”.

> **Stacks Project, Tag 04FE, equivalence of (1) and (2).** A morphism of schemes is formally
> étale if and only if it is formally unramified and the inclusion of its source into its universal
> first-order thickening is an isomorphism, that is, the universal first-order thickening of `X`
> over `S` is `X` itself.
>
> Formal unramifiedness is part of the right-hand side because the universal first-order
> thickening is only defined under it; for a formally étale morphism it comes from
> [Stacks Project, Tag 02HH].
>
> Forwards, the unique lifting property of [Stacks Project, Tag 04FD] applied to the thickening
> itself produces a retraction of the inclusion, and the universal property of the thickening
> identifies the other composite with the identity. Backwards, a lifting problem for `f` is
> transported along the isomorphism and solved by the universal property, uniquely because the
> universal property's lift is unique.

```lean
public theorem formallyEtale_iff_isIso_inclusion (f : X ⟶ S) :
    FormallyEtale f ↔
      ∃ hf : FormallyUnramified f,
        letI : FormallyUnramified f := hf
        IsIso (universalFirstOrderThickening f).inclusion
```

**`AlgebraicGeometry.formallyEtale_iff_isZero_universalConormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean#L159). The attribute's comment: “equivalence of (1) and (3)”.

> **Stacks Project, Tag 04FE, equivalence of (1) and (3).** A morphism of schemes is formally
> étale if and only if it is formally unramified and its conormal sheaf `𝒞_{X/S}` vanishes.
>
> This is the equivalence of (1) and (2) combined with
> `AlgebraicGeometry.isIso_inclusion_iff_isZero_universalConormalSheaf`.

```lean
public theorem formallyEtale_iff_isZero_universalConormalSheaf (f : X ⟶ S) :
    FormallyEtale f ↔
      ∃ hf : FormallyUnramified f,
        letI : FormallyUnramified f := hf
        IsZero (universalConormalSheaf f)
```

**`AlgebraicGeometry.formallyEtale_iff_isZero_relativeDifferentials_and_universalConormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleConormal.lean#L176). The attribute's comment: “equivalence of (1) and (4)”.

> **Stacks Project, Tag 04FE, equivalence of (1) and (4).** A morphism of schemes is formally
> étale if and only if both its sheaf of relative differentials `Ω_{X/S}` and its conormal sheaf
> `𝒞_{X/S}` vanish.
>
> The formal unramifiedness needed to form the conormal sheaf is supplied by the vanishing of the
> differentials, through [Stacks Project, Tag 02H9].

```lean
public theorem formallyEtale_iff_isZero_relativeDifferentials_and_universalConormalSheaf
    (f : X ⟶ S) :
    FormallyEtale f ↔
      ∃ hΩ : IsZero (Scheme.Hom.relativeDifferentials f),
        letI : FormallyUnramified f :=
          (Scheme.Hom.formallyUnramified_iff_isZero_relativeDifferentials f).mpr hΩ
        IsZero (universalConormalSheaf f)
```

## Tag 04FF, a lemma

[Tag 04FF](https://stacks.math.columbia.edu/tag/04FF) in the Stacks Project.

**`AlgebraicGeometry.formallyEtale_of_unramified_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleScheme.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleScheme.lean#L214).

> **An unramified flat morphism of schemes is formally étale.** Existence of the filler is
> local on the thickening by `AlgebraicGeometry.exists_isAffineOpen_lift_of_unramified_flat`; the
> local fillers agree on overlaps by `Stacks.Smooth.lift_unique` applied to the restricted
> thickening, so they glue by `Stacks.Smooth.exists_lift_of_isOpenCover`; and that same uniqueness
> is the `∃!`.

```lean
theorem formallyEtale_of_unramified_flat {X S : Scheme.{u}} (f : X ⟶ S) [Unramified f] [Flat f] :
    FormallyEtale f
```

## Tag 02HL, a lemma

[Tag 02HL](https://stacks.math.columbia.edu/tag/02HL) in the Stacks Project.

**`AlgebraicGeometry.formallyEtale_iff_globalSectionsMap_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleAffine.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleAffine.lean#L38).

> A morphism of affine schemes is formally étale if and only if its pullback map on global
> functions is a formally étale ring map.

```lean
theorem formallyEtale_iff_globalSectionsMap_formallyEtale
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S) :
    FormallyEtale f ↔ (Scheme.Γ.map f.op).hom.FormallyEtale
```

## Tag 02HM, a lemma

[Tag 02HM](https://stacks.math.columbia.edu/tag/02HM) in the Stacks Project.

**`AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/EtaleIffFormallyEtale.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/EtaleIffFormallyEtale.lean#L46). References: EGA IV (17.3.2), “(ii) etale”; EGA IV (17.6.1), “a) <=> d)”; EGA IV (17.3.1); SGA 3 XI (1.6), “étale case”; SGA 4 VII (1.1), “functorial criterion”; SGA 3 XI (1.1); SGA 4½ Arcata (2.1.1), “more general”.

> A morphism of schemes is étale exactly when it is locally of finite presentation and formally
> étale.

```lean
theorem etale_iff_locallyOfFinitePresentation_and_formallyEtale
    {X S : Scheme.{u}} (f : X ⟶ S) :
    Etale f ↔ (LocallyOfFinitePresentation f ∧ FormallyEtale f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.8, Tag 02HF](https://stacks.math.columbia.edu/tag/02HF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
