---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_dense_open_isRegular, AlgebraicGeometry.normalization_isFinite_of_regular_alteration, isNormalRing_adicCompletion_of_finite_injective, AlgebraicGeometry.exists_isRegularRing_localizationAway_of_regular_alteration, AlgebraicGeometry.module_finite_integralClosure_of_regular_alteration, AlgebraicGeometry.isNormalRing_adicCompletion_integralClosure_of_regular_alteration, AlgebraicGeometry.isRegularRing_genericFormalFibre_of_regular_alteration
statement: formalized
proof: formalized
---

# 54.13 Implied properties

Section 54.13 of the Stacks Project, [Tag 0BGF](https://stacks.math.columbia.edu/tag/0BGF). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BGG, a lemma

[Tag 0BGG](https://stacks.math.columbia.edu/tag/0BGG) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/Basic.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/Basic.lean#L45). The attribute's comment: “dense\_regular\_open”.

> An integral locally Noetherian scheme admitting an alteration by a regular scheme has a
> dense regular open subscheme.

```lean
theorem exists_dense_open_isRegular
    (Y : Scheme.{u}) [IsLocallyNoetherian Y] [IsIntegral Y]
    (X : Scheme.{u}) (f : X ⟶ Y) (hf : IsAlteration f)
    (hX : IsRegular X) :
    ∃ V : Y.Opens, Dense (V : Set Y) ∧ IsRegular V
```

**`AlgebraicGeometry.normalization_isFinite_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/FiniteNormalization.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/FiniteNormalization.lean#L207). The attribute's comment: “finiteness of the normalization”.

> **The normalization of an integral locally Noetherian scheme admitting an alteration by a
> regular scheme is finite.** This is the first assertion of [Stacks, Tag 0BGG]. The one input of
> the source's argument beyond this module is the degree-zero case of [Stacks, Tag 02O6] for the
> structure sheaf, which enters once as `AlgebraicGeometry.finiteGlobalSectionsOfProper`; the
> statement is therefore unconditional.
>
> The source assumes `Y` Noetherian, i.e. locally Noetherian and quasi-compact. Quasi-compactness
> is not used: finiteness is Zariski-local on the target, and the argument runs over one affine
> open at a time.

```lean
theorem normalization_isFinite_of_regular_alteration
    (Y : Scheme.{u}) [IsIntegral Y] [IsLocallyNoetherian Y]
    (X : Scheme.{u}) (f : X ⟶ Y)
    (hf : IsAlteration f) (hX : IsRegular X) :
    let hY : ∀ U : Y.Opens, IsCompact (U : Set Y) →
        (irreducibleComponents U).Finite := fun U hU ↦ by
      let : CompactSpace U := isCompact_iff_compactSpace.mp hU
      let : NoetherianSpace U :=
        noetherianSpace_of_isLocallyNoetherianSpace U
          (IsLocallyNoetherianSpace.subtype
            (isLocallyNoetherianSpace_of_isLocallyNoetherian Y) U)
      exact NoetherianSpace.finite_irreducibleComponents
    IsFinite (Scheme.normalization Y hY)
```

## Tag 0BGH, a lemma

[Tag 0BGH](https://stacks.math.columbia.edu/tag/0BGH) in the Stacks Project.

**`isNormalRing_adicCompletion_of_finite_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Normal.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Normal.lean#L253).

> **Stacks Project, Tag 0BGH.** Let `A` be a Noetherian local ring and `B ⊆ C` finite
> `A`-algebras. If `B` and the `m_A`-adic completion of `C` are normal, then the `m_A`-adic
> completion of `B` is normal.

```lean
theorem isNormalRing_adicCompletion_of_finite_injective
    (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [CommRing B] [CommRing C]
    [IsLocalRing A] [IsNoetherianRing A]
    [Algebra A B] [Algebra A C] [Algebra B C] [IsScalarTower A B C]
    [Module.Finite A B] [Module.Finite A C]
    (hBC : Function.Injective (algebraMap B C))
    (hB : IsNormalRing B)
    (hC : IsNormalRing (AdicCompletion ((IsLocalRing.maximalIdeal A).map (algebraMap A C)) C)) :
    IsNormalRing (AdicCompletion ((IsLocalRing.maximalIdeal A).map (algebraMap A B)) B)
```

## Tag 0BGI, a lemma

[Tag 0BGI](https://stacks.math.columbia.edu/tag/0BGI) in the Stacks Project.

**`AlgebraicGeometry.exists_isRegularRing_localizationAway_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean#L421). The attribute's comment: “part (1)”.

> **A Noetherian local domain admitting an alteration by a regular scheme is regular after
> inverting one nonzero element.** This is part (1) of [Stacks, Tag 0BGI]: the dense regular open
> of [Stacks, Tag 0BGG] contains a nonempty basic open `D(a)` of `Spec A`, and `Γ(D(a)) = A_a`.

```lean
theorem exists_isRegularRing_localizationAway_of_regular_alteration
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hf : IsAlteration f) (hX : IsRegular X) :
    ∃ a : A, a ≠ 0 ∧ IsRegularRing (Localization.Away a)
```

**`AlgebraicGeometry.module_finite_integralClosure_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean#L436). The attribute's comment: “part (2)”.

> **The integral closure of a Noetherian local domain admitting an alteration by a regular
> scheme is a finite module over it.** This is part (2) of [Stacks, Tag 0BGI]: the global sections
> `C` of the regular alteration are a finite `A`-module — by the degree-zero case of
> [Stacks, Tag 02O6], `AlgebraicGeometry.finiteGlobalSectionsOfProper` — and an integrally closed
> domain containing `A`, so the integral closure of `A` in `Frac(A)` embeds into `C` and is a
> submodule of a finite module over the Noetherian ring `A`.

```lean
theorem module_finite_integralClosure_of_regular_alteration
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hf : IsAlteration f) (hX : IsRegular X) :
    Module.Finite A ↥(integralClosure A (FractionRing A))
```

**`AlgebraicGeometry.isNormalRing_adicCompletion_integralClosure_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean#L456). The attribute's comment: “part (3)”.

> **The completion of the integral closure is normal.** This is part (3) of
> [Stacks, Tag 0BGI]. With `C = Γ(X, 𝒪_X)` and `B` the integral closure of `A` in `Frac(A)`, the
> inclusion `B ⊆ C` is a map of finite `A`-algebras, `B` is a normal domain, and the completion of
> `C` is normal because the base change of `X` to `Spec Aˆ` stays regular ([Stacks, Tag 0BG6]) and
> its global sections are `Aˆ ⊗_A C` ([Stacks, Tag 02KH]); [Stacks, Tag 0BGH] then gives normality
> of `Bˆ`.

```lean
theorem isNormalRing_adicCompletion_integralClosure_of_regular_alteration
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hf : IsAlteration f) (hX : IsRegular X) :
    IsNormalRing
      (AdicCompletion
        ((IsLocalRing.maximalIdeal A).map
          (algebraMap A ↥(integralClosure A (FractionRing A))))
        ↥(integralClosure A (FractionRing A)))
```

**`AlgebraicGeometry.isRegularRing_genericFormalFibre_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomain.lean#L501). The attribute's comment: “part (4)”. References: EGA IV (7.9.3), “domain case”.

> **The generic formal fibre of a Noetherian local domain admitting an alteration by a regular
> scheme is regular.** This is part (4) of [Stacks, Tag 0BGI]. Taking an affine open `U ⊆ X` around
> the generic point and `R = Γ(X, U)`, the scheme `Spec (R ⊗_A Aˆ)` is an open subscheme of the
> regular `X ×_{Spec A} Spec Aˆ` ([Stacks, Tag 0BG6]), so `Aˆ ⊗_A R` is regular; the generic formal
> fibre is recovered by inverting `A ∖ {0}` and descending along the faithfully flat
> `Frac(A)`-algebra `Frac(A) ⊗_A R`.

```lean
theorem isRegularRing_genericFormalFibre_of_regular_alteration
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hf : IsAlteration f) (hX : IsRegular X) :
    IsRegularRing ((AdicCompletion (IsLocalRing.maximalIdeal A) A) ⊗[A] (FractionRing A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.13, Tag 0BGF](https://stacks.math.columbia.edu/tag/0BGF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
