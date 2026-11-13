---
declaration: section
origin: cited
lean: Stacks.KInjective.nonempty_candidateKInjectiveResolution, Stacks.KInjective.quasiIso_canonicalMap, Stacks.Cohomology.SpaceInverseSystems.homology_isLimit_of_local_rlim_vanishing, Stacks.Cohomology.SpaceInverseSystems.homology_limit_projection_isIso_of_local_rlim_vanishing
statement: formalized
proof: formalized
---

# 20.38 Producing K-injective resolutions

Section 20.38 of the Stacks Project, [Tag 0719](https://stacks.math.columbia.edu/tag/0719). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 071A, an equation

[Tag 071A](https://stacks.math.columbia.edu/tag/071A) in the Stacks Project.

**`Stacks.KInjective.nonempty_candidateKInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CandidateKInjectiveResolution.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CandidateKInjectiveResolution.lean#L97).

> Every complex of sheaves of modules on a topological space admits a candidate K-injective
> resolution.

```lean
theorem nonempty_candidateKInjectiveResolution
    {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (F : CochainComplex (SheafOfModules.{u} O) ℤ) :
    Nonempty (CandidateKInjectiveResolution O F)
```

## Tag 071B, a lemma

[Tag 071B](https://stacks.math.columbia.edu/tag/071B) in the Stacks Project.

**`Stacks.KInjective.quasiIso_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CandidateKInjectiveQuasiIso.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CandidateKInjectiveQuasiIso.lean#L97).

> **Stacks 071B.** Let `F` be a complex of `𝒪_X`-modules on a ringed space, with candidate
> K-injective resolution `F ⟶ lim_n I_n` as in Tag 071A, and write `ℋ^q = H^q(F)` for its
> cohomology sheaves. If a set `B` of opens of `X` covers every open of `X` and `H^p(U, ℋ^q) = 0`
> for every `U ∈ B`, every `p > d` and every `q < 0`, then that canonical map is a
> quasi-isomorphism.

```lean
theorem quasiIso_canonicalMap (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (F : CochainComplex (SheafOfModules.{u} O) ℤ)
    (R : CandidateKInjectiveResolution O F) (B : Set (Opens X)) (d : ℕ)
    (hB : ∀ V : Opens X, ∃ 𝒰 : Set (Opens X), 𝒰 ⊆ B ∧ (V : Set X) = ⋃ U ∈ 𝒰, (U : Set X))
    (hvan : ∀ U ∈ B, ∀ p : ℕ, d < p → ∀ q : ℤ, q < 0 →
      IsZero (((SheafOfModules.evaluation.{u} O (Opposite.op U)).rightDerived p).obj
        (F.homology q))) :
    QuasiIso R.canonicalMap
```

## Tag 08BY, a lemma

[Tag 08BY](https://stacks.math.columbia.edu/tag/08BY) in the Stacks Project.

**`Stacks.Cohomology.SpaceInverseSystems.homology_isLimit_of_local_rlim_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/InverseSystemsOnASpace.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/InverseSystemsOnASpace.lean#L95). The attribute's comment: “canonical cohomology-limit comparison”.

> **Stacks 08BY.** Cohomology of the termwise inverse limit is the inverse limit of the
> cohomology sheaves under local first-derived-limit vanishing and eventual stability.

```lean
theorem homology_isLimit_of_local_rlim_vanishing
    (X : RingedSpace.{u, u})
    (F : ℕᵒᵖ ⥤ CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (m : ℤ) (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B) (n₀ : ℕ)
    (hneg2 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ InverseLimits.sectionsComplexFunctor (structureSheafRing X) U ⋙
        HomologicalComplex.eval Ab.{u} (ComplexShape.up ℤ) (m - 2))))
    (hneg1 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ InverseLimits.sectionsComplexFunctor (structureSheafRing X) U ⋙
        HomologicalComplex.eval Ab.{u} (ComplexShape.up ℤ) (m - 1))))
    (hHneg1 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ InverseLimits.sectionsComplexFunctor (structureSheafRing X) U ⋙
        HomologicalComplex.homologyFunctor Ab.{u} (ComplexShape.up ℤ) (m - 1))))
    (hstable : ∀ U ∈ B, ∀ (n : ℕ) (hn : n₀ ≤ n), IsIso
      ((HomologicalComplex.homologyFunctor Ab.{u} (ComplexShape.up ℤ) m).map
        ((InverseLimits.sectionsComplexFunctor (structureSheafRing X) U).map
          (F.map (homOfLE hn).op)))) :
    Nonempty (IsLimit
      ((HomologicalComplex.homologyFunctor
        (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ) m).mapCone
          (limit.cone F)))
```

**`Stacks.Cohomology.SpaceInverseSystems.homology_limit_projection_isIso_of_local_rlim_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/InverseSystemsOnASpace.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/InverseSystemsOnASpace.lean#L123). The attribute's comment: “projection to the stable stage”.

> **Stacks 08BY.** The projection from the limit of degree-`m` cohomology sheaves to the
> stable stage is an isomorphism when the transition maps are locally isomorphisms on a
> basis.

```lean
theorem homology_limit_projection_isIso_of_local_rlim_vanishing
    (X : RingedSpace.{u, u})
    (F : ℕᵒᵖ ⥤ CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (m : ℤ) (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B) (n₀ : ℕ)
    (hstable : ∀ U ∈ B, ∀ (n : ℕ) (hn : n₀ ≤ n), IsIso
      ((HomologicalComplex.homologyFunctor Ab.{u} (ComplexShape.up ℤ) m).map
        ((InverseLimits.sectionsComplexFunctor (structureSheafRing X) U).map
          (F.map (homOfLE hn).op)))) :
    IsIso (limit.π (F ⋙ HomologicalComplex.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ) m) (op n₀))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.38, Tag 0719](https://stacks.math.columbia.edu/tag/0719)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
