---
declaration: section
origin: cited
lean: Dualizing.derivedInclusion_adj_derivedPowerTorsion, Stacks.LocalCohomology.localCohomologyHomologyIsoColimitExt, Stacks.LocalCohomology.localCohomology_isHomotopyColimit_derivedHomPowers, Dualizing.derivedPowerTorsion_isZero_of_isIso_smul, Dualizing.powerTorsionComparison, Dualizing.bijective_derivedInclusion_map_singleFunctor, Dualizing.bijective_mapExt_one_powerTorsionModule, Dualizing.exists_not_surjective_mapExt_two_powerTorsionModule
statement: formalized
proof: formalized
---

# 47.8 Deriving torsion

Section 47.8 of the Stacks Project, [Tag 0BJA](https://stacks.math.columbia.edu/tag/0BJA). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A6L, a lemma

[Tag 0A6L](https://stacks.math.columbia.edu/tag/0A6L) in the Stacks Project.

**`Dualizing.derivedInclusion_adj_derivedPowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean, line 878](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean#L878).

> **Stacks 0A6L.** Local cohomology `RΓ_I`, as the named total right derived functor of
> the `I`-power-torsion-submodule functor, is right adjoint to the derived inclusion of the
> category of `I`-power-torsion modules into `D(A)`. Its counit is induced by the underived
> torsion-submodule inclusion, compatibly with the total right derived unit.

```lean
theorem derivedInclusion_adj_derivedPowerTorsion
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    let P : ObjectProperty (ModuleCat.{max u v} A) := fun M ↦ IsIPowerTorsion A M I
    letI : P.IsSerreClass := isSerreClass_isIPowerTorsion I hI
    letI : PreservesFiniteLimits P.ι :=
      ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass P
    letI : PreservesFiniteColimits P.ι :=
      ObjectProperty.preservesFiniteColimits_ι_of_isWeakSerreClass P
    ∃ adj : P.ι.mapDerivedCategory ⊣ derivedPowerTorsion.{u, v} A I hI,
      IsCanonicalDerivedPowerTorsionCounit.{u, v} A I hI adj.counit
```

## Tag 0954, a lemma

[Tag 0954](https://stacks.math.columbia.edu/tag/0954) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyHomologyIsoColimitExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TorsionColimit.lean, line 609](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TorsionColimit.lean#L609). The attribute's comment: “cohomology-module identification”.

> **Stacks 0954.** In every degree, local cohomology is the filtered colimit of the Ext modules
> from the quotients by powers of the ideal.

```lean
noncomputable def localCohomologyHomologyIsoColimitExt (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{u} R)) (q : ℤ) :
    (ModuleCat.uliftFunctor.{u + 1} R).obj
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) q).obj (localCohomology R I K)) ≅
      colimit (extPowers R I K q)
```

**`Stacks.LocalCohomology.localCohomology_isHomotopyColimit_derivedHomPowers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TorsionColimit.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TorsionColimit.lean#L640). The attribute's comment: “derived-category identification”.

> **Stacks 0954.** Local cohomology is the homotopy colimit of the derived Hom complexes from
> the powers of the ideal.

```lean
theorem localCohomology_isHomotopyColimit_derivedHomPowers (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{u} R)) :
    IsHomotopyColimit (derivedHomPowersOf R I K) (localCohomology R I K)
```

## Tag 0A6M, a lemma

[Tag 0A6M](https://stacks.math.columbia.edu/tag/0A6M) in the Stacks Project.

**`Dualizing.derivedPowerTorsion_isZero_of_isIso_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivingTorsion/DerivedVanishing.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivingTorsion/DerivedVanishing.lean#L64).

> **Stacks 0A6M.** Let `I` be a finitely generated ideal of `A` and let `K ∈ D(A)` be such that
> multiplication by some `f ∈ I` is an isomorphism of `K` (e.g. `K` is a complex of
> `A_f`-modules). Then `RΓ_I(K) = 0`, where `RΓ_I` is the derived functor of `H^0_I` with values
> in the derived category of `I`-power-torsion modules.

```lean
theorem derivedPowerTorsion_isZero_of_isIso_smul
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (f : A) (hf : f ∈ I) (hiso : IsIso (f • 𝟙 K)) :
    IsZero ((derivedPowerTorsion.{u, v} A I hI).obj K)
```

## Tag 0A6N, an equation

[Tag 0A6N](https://stacks.math.columbia.edu/tag/0A6N) in the Stacks Project.

**`Dualizing.powerTorsionComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean#L222).

> **Stacks 0A6N.** The canonical functor from the derived category of `I`-power-torsion
> `A`-modules to the full subcategory of `D(A)` on the objects with `I`-power-torsion cohomology.

```lean
noncomputable def powerTorsionComparison
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    DerivedCategory (PowerTorsionModule A I hI) ⥤
      PowerTorsionDerivedCategory A I hI
```

## Tag 0A6P, a lemma

[Tag 0A6P](https://stacks.math.columbia.edu/tag/0A6P) in the Stacks Project.

**`Dualizing.bijective_derivedInclusion_map_singleFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean#L246). The attribute's comment: “part (1), the Hom comparison”.

> The inclusion of power-torsion modules induces a bijection on derived
> morphisms between modules concentrated in degree zero.

```lean
theorem bijective_derivedInclusion_map_singleFunctor
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M N : PowerTorsionModule.{u, v} A I hI) :
    let F := (powerTorsionModuleProperty A I hI).ι.mapDerivedCategory
    let X := (DerivedCategory.singleFunctor
      (PowerTorsionModule.{u, v} A I hI) 0).obj M
    let Y := (DerivedCategory.singleFunctor
      (PowerTorsionModule.{u, v} A I hI) 0).obj N
    Function.Bijective (fun f : X ⟶ Y ↦ F.map f)
```

**`Dualizing.bijective_mapExt_one_powerTorsionModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedTorsion.lean#L361). The attribute's comment: “part (2), the Ext¹ comparison”.

> **Stacks 0A6P, Ext¹ comparison.** The exact inclusion of the category of
> `I`-power-torsion modules into all `A`-modules induces a bijection on Ext¹.

```lean
theorem bijective_mapExt_one_powerTorsionModule
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M N : PowerTorsionModule.{u, v} A I hI) :
    Function.Bijective
      ((powerTorsionModuleProperty A I hI).ι.mapExtAddHom M N 1)
```

**`Dualizing.exists_not_surjective_mapExt_two_powerTorsionModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean#L344). The attribute's comment: “part (3)”.

> **Stacks 0A6P (3).** The comparison map
> `Ext²_{D(I^∞-torsion)}(M, N) ⟶ Ext²_{D(A)}(M, N)` between `I`-power-torsion modules is not
> surjective in general: there is a commutative ring `A`, a finitely generated (indeed principal)
> ideal `I`, and `I`-power-torsion modules `M` and `N` for which the inclusion of the torsion
> category does not hit every class of `Ext²_A(M, N)`.
>
> Parts (1) and (2) of the source, that the comparison is bijective on `Hom` and on `Ext¹`, are
> `Dualizing.bijective_derivedInclusion_map_singleFunctor` and
> `Dualizing.bijective_mapExt_one_powerTorsionModule`.

```lean
theorem exists_not_surjective_mapExt_two_powerTorsionModule :
    ∃ (A : Type) (_ : CommRing A) (I : Ideal A) (hI : I.FG)
      (M N : PowerTorsionModule.{0, 0} A I hI),
      ¬ Function.Surjective
        ((powerTorsionModuleProperty A I hI).ι.mapExtAddHom M N 2)
```

**`Dualizing.exists_not_isEquivalence_powerTorsionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean#L361). The attribute's comment: “part (4)”.

> **Stacks 0A6P (4).** The comparison functor of Stacks 0A6N,
> `D(I^∞-torsion) ⟶ D_{I^∞-torsion}(A)`, is not an equivalence in general.
>
> This is part (3) together with
> `Dualizing.not_isEquivalence_powerTorsionComparison_of_not_surjective_mapExt`: an equivalence
> would be bijective on `Extⁿ` in every degree.

```lean
theorem exists_not_isEquivalence_powerTorsionComparison :
    ∃ (A : Type) (_ : CommRing A) (I : Ideal A) (hI : I.FG),
      ¬ (powerTorsionComparison.{0, 0} A I hI).IsEquivalence
```

**`Dualizing.bijective_hom_and_ext_one_and_exists_not_surjective_ext_two_and_not_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionExtCounterexample.lean#L385). The attribute's comment: “all four parts conjoined”.

> **Stacks 0A6P, all four parts.** For every ring `A`, every finitely generated ideal
> `I ⊆ A` and all `I`-power-torsion `A`-modules `M` and `N`:
>
> 1. `Hom_{D(A)}(M, N) = Hom_{D(I^∞-torsion)}(M, N)`;
> 2. `Ext¹_{D(A)}(M, N) = Ext¹_{D(I^∞-torsion)}(M, N)`;
> 3. `Ext²_{D(I^∞-torsion)}(M, N) ⟶ Ext²_{D(A)}(M, N)` is not surjective in general;
> 4. the comparison functor `D(I^∞-torsion) ⟶ D_{I^∞-torsion}(A)` of Stacks 0A6N is not an
>    equivalence in general.
>
> Parts (1) and (2) are universally quantified and parts (3) and (4) are existential, exactly as
> in the source. The four conjuncts are
> `Dualizing.bijective_derivedInclusion_map_singleFunctor`,
> `Dualizing.bijective_mapExt_one_powerTorsionModule`,
> `Dualizing.exists_not_surjective_mapExt_two_powerTorsionModule` and
> `Dualizing.exists_not_isEquivalence_powerTorsionComparison`, each of which carries the tag for
> its own clause.

```lean
theorem bijective_hom_and_ext_one_and_exists_not_surjective_ext_two_and_not_isEquivalence :
    (∀ (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
        (M N : PowerTorsionModule.{u, v} A I hI),
        Function.Bijective fun f :
            (DerivedCategory.singleFunctor (PowerTorsionModule.{u, v} A I hI) 0).obj M ⟶
              (DerivedCategory.singleFunctor (PowerTorsionModule.{u, v} A I hI) 0).obj N ↦
          (powerTorsionModuleProperty A I hI).ι.mapDerivedCategory.map f) ∧
      (∀ (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
        (M N : PowerTorsionModule.{u, v} A I hI),
        Function.Bijective ((powerTorsionModuleProperty A I hI).ι.mapExtAddHom M N 1)) ∧
      (∃ (A : Type) (_ : CommRing A) (I : Ideal A) (hI : I.FG)
        (M N : PowerTorsionModule.{0, 0} A I hI),
        ¬ Function.Surjective
          ((powerTorsionModuleProperty A I hI).ι.mapExtAddHom M N 2)) ∧
      (∃ (A : Type) (_ : CommRing A) (I : Ideal A) (hI : I.FG),
        ¬ (powerTorsionComparison.{0, 0} A I hI).IsEquivalence)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.8, Tag 0BJA](https://stacks.math.columbia.edu/tag/0BJA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
