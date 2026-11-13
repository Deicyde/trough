---
declaration: section
origin: cited
lean: Stacks.Algebraization.AdicInverseSystem.isZero_cohomology_limitModule_of_affineOpen, Stacks.Algebraization.AdicInverseSystem.isDerivedLimit_single_limitModule, Stacks.Algebraization.AdicInverseSystem.exists_shortExact_cohomology_limitModule, Stacks.Algebraization.AdicInverseSystem.idealPowerMultiple_limit, Stacks.Algebraization.AdicInverseSystem.surjective_limitComparison_moduleCohomologyFunctor, Stacks.Algebraization.AdicInverseSystem.exists_idealPowerQuotientIso
statement: formalized
proof: formalized
---

# 52.2 Formal sections, I

Section 52.2 of the Stacks Project, [Tag 0EH3](https://stacks.math.columbia.edu/tag/0EH3). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EI8, a lemma

[Tag 0EI8](https://stacks.math.columbia.edu/tag/0EI8) in the Stacks Project.

**`Stacks.Algebraization.AdicInverseSystem.isZero_cohomology_limitModule_of_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/AffineVanishing.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/AffineVanishing.lean#L107). The attribute's comment: “affine\_vanishing”.

> The positive-degree cohomology of the inverse limit of an adic inverse system vanishes on
> every affine open.

```lean
public theorem isZero_cohomology_limitModule_of_affineOpen (U : S.X.affineOpens) (p : ℕ)
    (hp : 0 < p) :
    IsZero (Hgroup S.X.ringCatSheaf U.1 p S.limitModule)
```

**`Stacks.Algebraization.AdicInverseSystem.isDerivedLimit_single_limitModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/DerivedLimitMilnorSequence.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/DerivedLimitMilnorSequence.lean#L69). The attribute's comment: “part (1)”.

> The inverse limit of an adic inverse system **is** its derived inverse limit: placed in
> degree zero, `F = lim F_n` sits in the defining distinguished triangle
> `F ⟶ ∏ F_n ⟶ ∏ F_n ⟶ F[1]` of `R lim F_n`.
>
> The terms are quasi-coherent, hence acyclic on the affine opens, and the transitions are
> surjective on affine sections, so `R¹ lim` of the sections vanishes there; those are exactly
> the two hypotheses under which the ordinary limit computes the derived one.

```lean
public theorem isDerivedLimit_single_limitModule :
    ∃ h : HasProduct (fun n : ℕ =>
        (S.system ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) 0).obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)))
        _ _ _ _ _ _
        (S.system ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) 0) h
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) 0).obj S.limitModule)
```

**`Stacks.Algebraization.AdicInverseSystem.exists_shortExact_cohomology_limitModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/DerivedLimitMilnorSequence.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/DerivedLimitMilnorSequence.lean#L105). The attribute's comment: “part (3)”.

> **The Milnor short exact sequence of an adic inverse system.** For every degree `p` the
> cohomology of `F = lim F_n` sits in a short exact sequence
>
> `0 ⟶ R¹ lim H^(p-1)(X, F_n) ⟶ H^p(X, F) ⟶ lim H^p(X, F_n) ⟶ 0`.
>
> Cohomology is read over a base ring `A` mapping to `Γ(X, 𝒪_X)` by `ρ`, as the degree-`p`
> cohomology of `RΓ(X, -)` applied to a module placed in degree zero; for `A = Γ(X, 𝒪_X)` and
> `ρ` the identity this is sheaf cohomology with its module structure, the identification being
> `Stacks.Cohomology.ModuleComparison.hfunctorIsoHomologyDerivedSectionsOver`. `R¹ lim` is the
> cokernel of the difference map `1 - shift` on the product of the groups `H^(p-1)(X, F_n)`.
>
> The sequence comes from the Milnor triangle of `RΓ(X, F)`: the ordinary limit is a derived
> limit of the system by `isDerivedLimit_single_limitModule`, and derived sections commute with
> derived limits. The inclusion descends the connecting morphism of that triangle and the
> projection is characterized by its composites with the limit projections.

```lean
public theorem exists_shortExact_cohomology_limitModule {A : Type u} [CommRing A]
    (ρ : A →+* (structureSheafRing S.X.toRingedSpace).obj.obj
      (op (⊤ : Opens S.X.toRingedSpace.carrier))) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) :=
      S.system ⋙ DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) 0
    let L : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) :=
      (DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing S.X.toRingedSpace)) 0).obj S.limitModule
    let F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      K ⋙ derivedSectionsOver S.X.toRingedSpace ρ
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    ∃ (a : (derivedSectionsOver S.X.toRingedSpace ρ).obj L ⟶ ∏ᶜ Y)
      (b : (∏ᶜ Y) ⟶ ((derivedSectionsOver S.X.toRingedSpace ρ).obj L)⟦(1 : ℤ)⟧),
      let T := Triangle.mk a d b
      T ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
        ∀ p : ℤ,
          let H := DerivedCategory.homologyFunctor (ModuleCat.{u} A) p
          let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{u} A) (p - 1)
          let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H
          let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H₁
          let P : ModuleCat.{u} A :=
            ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (op n)
          let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) n -
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) (n + 1) ≫
                shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
          ∃ (e : H₁.obj (∏ᶜ Y) ≅ P)
            (i : cokernel δ ⟶ H.obj ((derivedSectionsOver S.X.toRingedSpace ρ).obj L))
            (q : H.obj ((derivedSectionsOver S.X.toRingedSpace ρ).obj L) ⟶
              limit homologySystem)
            (w : i ≫ q = 0),
            e.hom = piComparison H₁ Y ∧
              cokernel.π δ ≫ i = e.inv ≫
                DerivedCategory.HomologySequence.δ T (p - 1) p ∧
              (∀ n : ℕ, q ≫ limit.π homologySystem (op n) =
                H.map a ≫ H.map (Pi.π Y n)) ∧
              (ShortComplex.mk i q w).ShortExact
```

**`Stacks.Algebraization.AdicInverseSystem.idealPowerMultiple_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/IdealPowers.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/IdealPowers.lean#L160). The attribute's comment: “ideal\_powers”.

> A morphism into the inverse limit factors through `I ^ n` of the limit if and only if all
> its projections to the terms `F_m`, for `m ≥ n`, factor through `I ^ n F_m`. This is the
> canonical limit description of the ideal-power submodule.

```lean
public theorem idealPowerMultiple_limit (hI : Scheme.IdealSheafData.IsFiniteType S.I) (n : ℕ)
    (T : S.X.Modules) (f : T ⟶ S.limitModule) :
    (∃ g : T ⟶ (idealPowerMultiple S.I n S.limitModule).toSheafOfModules,
      g ≫ (idealPowerMultiple S.I n S.limitModule).ι = f) ↔
    (∀ m : ℕ, n ≤ m + 1 →
      ∃ g : T ⟶ (idealPowerMultiple S.I n (S.system.obj (op m))).toSheafOfModules,
        g ≫ (idealPowerMultiple S.I n (S.system.obj (op m))).ι =
          f ≫ limit.π S.system (op m))
```

**`Stacks.Algebraization.AdicInverseSystem.surjective_limitComparison_moduleCohomologyFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/MilnorSurjection.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/MilnorSurjection.lean#L240). The attribute's comment: “surjectivity of the comparison onto the limit, module-valued cohomology”.

> **The Milnor surjection of an adic inverse system, in module-valued cohomology.** For an
> adic inverse system `(Fₙ)` of quasi-coherent modules on a scheme `X`, with inverse limit
> `F = lim Fₙ`, the canonical comparison map
>
> `H^p(X, F) ⟶ lim_n H^p(X, Fₙ)`
>
> is surjective. Here `H^p(X, -)` is `moduleCohomologyFunctor X p`, the `p`-th right derived
> functor of global sections taken in `Γ(X, 𝒪_X)`-modules, and the comparison map is
> `limitComparison`.

```lean
public theorem surjective_limitComparison_moduleCohomologyFunctor (S : AdicInverseSystem.{u})
    (p : ℕ) :
    Function.Surjective (limitComparison S (moduleCohomologyFunctor S.X p)).hom
```

**`Stacks.Algebraization.AdicInverseSystem.exists_idealPowerQuotientIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/Reduction.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/Reduction.lean#L363). The attribute's comment: “reduction”.

> Reduction of the limit of an adic inverse system modulo `I^{n+1}` recovers its `n`-th
> (zero-indexed) term, compatibly with the canonical limit projection.

```lean
public theorem exists_idealPowerQuotientIso
    (hI : Scheme.IdealSheafData.IsFiniteType S.I) (n : ℕ) :
    ∃ e : idealPowerQuotient S.I (n + 1) S.limitModule ≅ S.system.obj (op n),
      cokernel.π ((idealPowerMultiple S.I (n + 1) S.limitModule).ι) ≫ e.hom =
        limit.π S.system (op n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.2, Tag 0EH3](https://stacks.math.columbia.edu/tag/0EH3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
