---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isSeparated_inf_locallyQuasiFinite_inf_lft, AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft, AlgebraicGeometry.DescentDatum.isEffective_of_isSeparated_of_locallyQuasiFinite, AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isSeparated_of_locallyQuasiFinite, AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveFlat_isSeparated_inf_locallyQuasiFinite_inf_lft, AlgebraicGeometry.FormalSpace.isEffectiveDescentAlongSurjectiveEtale_isThickening
statement: formalized
proof: formalized
---

# 37.57 Descending separated locally quasi-finite morphisms

Section 37.57 of the Stacks Project, [Tag 02W7](https://stacks.math.columbia.edu/tag/02W7). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02W8, a lemma

[Tag 02W8](https://stacks.math.columbia.edu/tag/02W8) in the Stacks Project.

**`AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isSeparated_inf_locallyQuasiFinite_inf_lft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineEtaleDescent.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineEtaleDescent.lean#L474). The attribute's comment: “effective descent along a surjective étale chart of the site”.

> Effective descent along the surjective étale morphisms of the big fppf site of `S` for the
> separated, locally quasi-finite morphisms which are locally of finite type.

```lean
theorem isEffectiveDescentAlongSurjectiveEtale_isSeparated_inf_locallyQuasiFinite_inf_lft
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    IsEffectiveDescentAlongSurjectiveEtale B S hS
      (@_root_.AlgebraicGeometry.IsSeparated.{u} ⊓ @LocallyQuasiFinite ⊓ @LocallyOfFiniteType :
        MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean#L519). The attribute's comment: “effective descent along the covering sieves of the site, at the monomorphisms locally of finite type”.

> **Effective descent along the covering sieves of the big fppf site of `S` at the
> monomorphisms locally of finite type**, unconditionally. This is
> `isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft_of_isQuasiAffineHom`
> with its hypothesis discharged, and it is the descent hypothesis which the diagonal of a quotient
> sheaf consumes. (The name of that conditional statement is too long to cite on one line here;
> it lives in `StacksFrontier.AlgebraicGeometry.Descent.CoveringSieveQuasiAffineDescent`.)
>
> No cardinal hypothesis and no hypothesis on the site's cutoff is used: the passage from affine to
> arbitrary base objects is paid for by `AlgebraicGeometry.Scheme.size_le_of_mono`, available
> because the property lies below the monomorphisms.

```lean
theorem isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft :
    IsEffectiveDescentAlongCoveringSieve B S hS
      (MorphismProperty.monomorphisms Scheme.{u} ⊓ @LocallyOfFiniteType)
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isSeparated_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean#L188). The attribute's comment: “the scheme-descent-datum form, for a single quasi-compact chart”. References: SGA 3 X (5.4), “special case”.

> **[Stacks, Tag 02W8](https://stacks.math.columbia.edu/tag/02W8) in the scheme-descent-datum
> form, for a single quasi-compact chart.** Let `f : X ⟶ S` be a surjective, flat, quasi-compact
> morphism of schemes and let `(V, φ)` be a descent datum relative to `X/S` whose structure
> morphism `V ⟶ X` is separated, locally quasi-finite and locally of finite type. Then `(V, φ)` is
> effective: it is isomorphic to the canonical descent datum of a scheme over `S`.
>
> Such a structure morphism is ind-quasi-affine by Stacks 0AP9, so this is Gabber's effectivity
> `AlgebraicGeometry.DescentDatum.isEffective_of_isIndQuasiAffineHom_of_quasiCompact`.

```lean
theorem isEffective_of_isSeparated_of_locallyQuasiFinite {S X : Scheme.{u}} {f : X ⟶ S}
    [Surjective f] [Flat f] [QuasiCompact f] (D : DescentDatum f)
    (hsep : IsSeparated D.over.hom) (hqf : LocallyQuasiFinite D.over.hom)
    (hft : LocallyOfFiniteType D.over.hom) : DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isSeparated_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean#L224). References: SGA 3 X (5.4), “more general”.

> **[Stacks, Tag 02W8](https://stacks.math.columbia.edu/tag/02W8).** Let `S` be a scheme, let
> `{X i ⟶ S}` be an fppf covering family and let `D = (V i / X i, φ i j)` be a descent datum
> relative to that family. If each morphism `V i ⟶ X i` is separated and locally quasi-finite, then
> the descent datum is effective: it is isomorphic to the canonical descent datum of a scheme over
> `S`.
>
> Quasi-finiteness is Stacks 02NG — `AlgebraicGeometry.LocallyQuasiFinite` together with
> `AlgebraicGeometry.LocallyOfFiniteType`, as in the formalization of Stacks 01TD, of Stacks 02LR
> and of Stacks 0AP9, Mathlib's `LocallyQuasiFinite` not itself asking for local finite type.
>
> Such a structure morphism is ind-quasi-affine by Stacks 0AP9,
> `AlgebraicGeometry.isIndQuasiAffineHom_of_isSeparated_of_locallyQuasiFinite`, and an fppf
> covering family is an fpqc covering family, so this is Gabber's effectivity
> `AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom_of_anyIndex`.

```lean
theorem isFamilyEffective_of_forall_isSeparated_of_locallyQuasiFinite {ι : Type v}
    {S : Scheme.{u}} {X : ι → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage S) (D : DescentData f)
    (hsep : ∀ i, IsSeparated (D.obj i).hom)
    (hqf : ∀ i, LocallyQuasiFinite (D.obj i).hom)
    (hft : ∀ i, LocallyOfFiniteType (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveFlat_isSeparated_inf_locallyQuasiFinite_inf_lft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SurjectiveFlatDescent.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SurjectiveFlatDescent.lean#L442). The attribute's comment: “effective descent along a single surjective flat chart of the site”.

> **Effective descent along a single surjective flat morphism of the site locally of finite
> presentation, for the separated locally quasi-finite morphisms locally of finite type**, over an
> arbitrary base object, unconditionally.
>
> This is the property of Stacks 02W8 descended along the one-element fppf coverings, which is the
> shape Stacks 046J consumes: that tag reduces to a covering `{F → G}` by a single surjective, flat
> morphism locally of finite presentation, not to a general covering sieve.
>
> All five steps of Stacks 02W8 are discharged. Steps 1, 2 and 5 over an affine base, together with
> steps 3 and 4, are
> `AlgebraicGeometry.Space.coveringSieveBody_affineBase_isSeparated_inf_locallyQuasiFinite_inf_lft`;
> the passage from an affine base object to an arbitrary one is
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveFlat_of_affineBase`, whose glueing is
> paid for by the size bound of the single flat covering morphism.
>
> Compare
> `isEffectiveDescentAlongCoveringSieve_isSeparated_inf_lqf_inf_lft_of_isRegular` in this namespace,
> the same property in the covering-sieve shape, which carries a regularity hypothesis on the
> site's cutoff. That hypothesis is not an artefact: a covering sieve supplies no single surjective
> morphism whose size bounds the glueing, and the property of Stacks 02W8 admits no size bound of
> its own, `∐_{i < κ} Spec A ⟶ Spec A` having it for every `κ`. Restricting to one-element
> coverings is exactly what removes the hypothesis.

```lean
theorem isEffectiveDescentAlongSurjectiveFlat_isSeparated_inf_locallyQuasiFinite_inf_lft
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    IsEffectiveDescentAlongSurjectiveFlat B S hS
      (@_root_.AlgebraicGeometry.IsSeparated.{u} ⊓ @LocallyQuasiFinite ⊓ @LocallyOfFiniteType :
        MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.FormalSpace.isEffectiveDescentAlongSurjectiveEtale_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionDescent.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionDescent.lean#L147). The attribute's comment: “effective descent along a surjective étale chart of the site, for thickenings”.

> Effective descent along a surjective étale morphism of the big fppf site of `S` holds for the
> thickenings.

```lean
theorem isEffectiveDescentAlongSurjectiveEtale_isThickening :
    Space.IsEffectiveDescentAlongSurjectiveEtale B S hS
      (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.57, Tag 02W7](https://stacks.math.columbia.edu/tag/02W7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
