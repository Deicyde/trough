---
declaration: section
origin: cited
lean: Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_one_iff_two, Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_two_iff_three, Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_four_imp_three, Stacks.Cohomology.InverseSystems.range_pow_eq_ker_limitProjection, Stacks.Cohomology.InverseSystems.range_pow_eq_ker_limitProjection_and_limitTopology_eq_adic, Stacks.Modules.PrincipalAdicInverseSystem.isSMulRegular_limit, Stacks.Modules.PrincipalAdicInverseSystem.finite_limitGlobalSections, Stacks.Modules.PrincipalAdicInverseSystem.quotientEquivRange_firstProjection
statement: formalized
proof: formalized
---

# 20.36 Inverse systems and cohomology, II

Section 20.36 of the Stacks Project, [Tag 0H38](https://stacks.math.columbia.edu/tag/0H38). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H39, a lemma

[Tag 0H39](https://stacks.math.columbia.edu/tag/0H39) in the Stacks Project.

**`Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_one_iff_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean, line 1419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean#L1419). The attribute's comment: “(1)⇔(2)”.

> Conditions (1) and (2) on an inverse system are equivalent.

```lean
theorem stacks0H39_one_iff_two
    (f : End (𝟭 (SheafOfModules.{max u v} R)))
    (obj : ℕ → SheafOfModules.{max u v} R) (map : ∀ n, obj (n + 1) ⟶ obj n) :
    Condition1 f obj map ↔ Condition2 f obj map
```

**`Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_two_iff_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean, line 1427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean#L1427). The attribute's comment: “(2)⇔(3)”.

> Conditions (2) and (3) on an inverse system are equivalent.

```lean
theorem stacks0H39_two_iff_three
    (f : End (𝟭 (SheafOfModules.{max u v} R)))
    (obj : ℕ → SheafOfModules.{max u v} R) (map : ∀ n, obj (n + 1) ⟶ obj n) :
    Condition2 f obj map ↔ Condition3 f obj map
```

**`Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.stacks0H39_four_imp_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean, line 1435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/TorsionFreeAndDivisibleSystems.lean#L1435). The attribute's comment: “(4)⇒(3)”.

> Condition (4) on an inverse system implies condition (3).

```lean
theorem stacks0H39_four_imp_three
    (f : End (𝟭 (SheafOfModules.{max u v} R)))
    (obj : ℕ → SheafOfModules.{max u v} R) (map : ∀ n, obj (n + 1) ⟶ obj n) :
    Condition4 f obj map → Condition3 f obj map
```

## Tag 0EHA, a lemma

[Tag 0EHA](https://stacks.math.columbia.edu/tag/0EHA) in the Stacks Project.

**`Stacks.Cohomology.InverseSystems.range_pow_eq_ker_limitProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/AdicTopologyOnLimitCohomology.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/AdicTopologyOnLimitCohomology.lean#L355).

> Let `f` be a global section of `O` and let `… → 𝓕₂ → 𝓕₁` be an inverse system of `O`-modules
> satisfying condition (1) of Stacks 0H39 for multiplication by `f`. For every `c = n + 1 ≥ 1` the
> submodule `f^c · lim Hᵖ(C, 𝓕ₙ)` of `lim Hᵖ(C, 𝓕ₙ)` is the kernel of the projection to
> `Hᵖ(C, 𝓕_c)`.

```lean
theorem range_pow_eq_ker_limitProjection (f : ↥(GlobalSectionRing O))
    (obj : ℕ → SheafOfModules.{max u v} O) (map : ∀ n, obj (n + 1) ⟶ obj n)
    (h : Condition1 (Stacks.SheafOfModules.globalSectionToEnd O ⟨f.1, f.2⟩) obj map) (p n : ℕ) :
    LinearMap.range (LinearMap.lsmul ↥(GlobalSectionRing O)
        (limit (Functor.ofOpSequence map ⋙ globalModuleCohomology.{u, v, max u v, max u v} O p) :
          ModuleCat.{max u v} ↥(GlobalSectionRing O)) (f ^ (n + 1))) =
      LinearMap.ker (limit.π (Functor.ofOpSequence map ⋙
        globalModuleCohomology.{u, v, max u v, max u v} O p) (op n)).hom
```

**`Stacks.Cohomology.InverseSystems.range_pow_eq_ker_limitProjection_and_limitTopology_eq_adic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/AdicTopologyOnLimitCohomology.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/AdicTopologyOnLimitCohomology.lean#L396). The attribute's comment: “both conclusions: `f^c Hᵖ` is the kernel of `Hᵖ → Hᵖ(X, 𝓕_c)` for all `c ≥ 1`, and the limit topology on `Hᵖ` is the `f`-adic topology”.

> Let `f` be a global section of `O` and let `… → 𝓕₂ → 𝓕₁` be an inverse system of `O`-modules
> satisfying condition (1) of Stacks 0H39 for multiplication by `f`, and let `p ≥ 0`. Put
> `Hᵖ = lim Hᵖ(C, 𝓕ₙ)`. Then for every `c = n + 1 ≥ 1` the submodule `f^c Hᵖ` is the kernel of
> `Hᵖ → Hᵖ(C, 𝓕_c)`, and the limit topology on `Hᵖ` (the infimum of the topologies induced by the
> projections to the discrete `Hᵖ(C, 𝓕_c)`) is the `f`-adic topology.

```lean
theorem range_pow_eq_ker_limitProjection_and_limitTopology_eq_adic
    (f : ↥(GlobalSectionRing O))
    (obj : ℕ → SheafOfModules.{max u v} O) (map : ∀ n, obj (n + 1) ⟶ obj n)
    (h : Condition1 (Stacks.SheafOfModules.globalSectionToEnd O ⟨f.1, f.2⟩) obj map) (p : ℕ) :
    (∀ n : ℕ, LinearMap.range (LinearMap.lsmul ↥(GlobalSectionRing O)
        (limit (Functor.ofOpSequence map ⋙ globalModuleCohomology.{u, v, max u v, max u v} O p) :
          ModuleCat.{max u v} ↥(GlobalSectionRing O)) (f ^ (n + 1))) =
      LinearMap.ker (limit.π (Functor.ofOpSequence map ⋙
        globalModuleCohomology.{u, v, max u v, max u v} O p) (op n)).hom) ∧
    (⨅ n : ℕ, TopologicalSpace.induced
        (fun y : (limit (Functor.ofOpSequence map ⋙
            globalModuleCohomology.{u, v, max u v, max u v} O p) :
          ModuleCat.{max u v} ↥(GlobalSectionRing O)) =>
          (limit.π (Functor.ofOpSequence map ⋙
            globalModuleCohomology.{u, v, max u v, max u v} O p) (op n)).hom y) ⊥) =
      (Ideal.span {f}).adicModuleTopology
        (limit (Functor.ofOpSequence map ⋙ globalModuleCohomology.{u, v, max u v, max u v} O p) :
          ModuleCat.{max u v} ↥(GlobalSectionRing O))
```

## Tag 0BLB, a lemma

[Tag 0BLB](https://stacks.math.columbia.edu/tag/0BLB) in the Stacks Project.

**`Stacks.Modules.PrincipalAdicInverseSystem.isSMulRegular_limit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/PrincipalAdicNonzerodivisor.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/PrincipalAdicNonzerodivisor.lean#L39). The attribute's comment: “nonzerodivisor”.

> The distinguished element of a principal-adic inverse system is a nonzerodivisor on the
> limit of its global sections.

```lean
lemma isSMulRegular_limit (S : PrincipalAdicInverseSystem.{u, w}) :
    IsSMulRegular S.M S.f
```

**`Stacks.Modules.PrincipalAdicInverseSystem.finite_limitGlobalSections`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitFinite.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitFinite.lean#L38). The attribute's comment: “finite”.

> The limit of global sections of a principal-adic inverse system is finite over its base
> ring.

```lean
lemma finite_limitGlobalSections (S : PrincipalAdicInverseSystem.{u, w}) :
    Module.Finite S.A S.M
```

**`Stacks.Modules.PrincipalAdicInverseSystem.quotientEquivRange_firstProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitImage.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitImage.lean#L64). The attribute's comment: “image”.

> The quotient of the inverse limit by `f` maps isomorphically onto its image in the first
> term, by the map induced by the first projection.

```lean
def quotientEquivRange_firstProjection (S : PrincipalAdicInverseSystem.{u, w}) :
    (S.M ⧸ (LinearMap.lsmul S.A S.M S.f).range) ≃ₗ[S.A]
      LinearMap.range ((limit.π S.globalSectionsSystem (op 0)).hom)
```

**`Stacks.Modules.PrincipalAdicInverseSystem.quotientEquivRange_firstProjection_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitImage.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/PrincipalAdicLimitImage.lean#L73). The attribute's comment: “image”.

> The canonical equivalence sends a class to the first projection of a representative.

```lean
theorem quotientEquivRange_firstProjection_mk (S : PrincipalAdicInverseSystem.{u, w})
    (x : S.M) :
    quotientEquivRange_firstProjection S (Submodule.Quotient.mk x) =
      ⟨(limit.π S.globalSectionsSystem (op 0)).hom x,
        LinearMap.mem_range_self _ x⟩
```

## Tag 0BLC, a lemma

[Tag 0BLC](https://stacks.math.columbia.edu/tag/0BLC) in the Stacks Project.

**`Stacks.Cohomology.InverseSystems.isMittagLefflerCategorical_of_finite_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCriteria.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCriteria.lean#L461).

> **Stacks 0BLC.** Let `A` be a ring, `f ∈ A`, `X` a topological space and `… → ℱ₂ → ℱ₁` an
> inverse system of sheaves of `A`-modules satisfying condition (1) of Stacks 0H39. If
> `H^{p+1}(X, ℱ₁)` has finite length over `A`, or `A` is Noetherian and `H^{p+1}(X, ℱ₁)` is a
> finite `A`-module, then the inverse system `n ↦ H^p(X, ℱ_n)` satisfies the Mittag-Leffler
> condition.

```lean
theorem isMittagLefflerCategorical_of_finite_cohomology
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [∀ U, IsMulCommutative (R.obj.obj U)]
    (A : Type u) [CommRing A]
    [Algebra A (R.obj.obj (op (⊤ : Opens X)))] (f : A)
    (obj : ℕ → SheafOfModules.{u} R)
    (map : ∀ n, obj (n + 1) ⟶ obj n) (p : ℕ) :
    let E := SheafOfModules.evaluation R (op (⊤ : Opens X))
    let G := E.rightDerived (p + 1)
    letI : Module A (G.obj (obj 0)) :=
      Module.compHom (G.obj (obj 0)) (algebraMap A (R.obj.obj (op (⊤ : Opens X))))
    ((IsFiniteLength A (G.obj (obj 0))) ∨
      (IsNoetherianRing A ∧ Module.Finite A (G.obj (obj 0)))) →
    Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.Condition1
      (Stacks.SheafOfModules.terminalSectionToEnd R (⊤ : Opens X) isTerminalTop
        (algebraMap A (R.obj.obj (op (⊤ : Opens X))) f)) obj map →
    IsMittagLefflerCategorical
      (Functor.ofOpSequence map ⋙ E.rightDerived p)
```

## Tag 0DXG, a lemma

[Tag 0DXG](https://stacks.math.columbia.edu/tag/0DXG) in the Stacks Project.

**`Stacks.Cohomology.InverseSystems.isMittagLefflerCategorical_of_finite_cohomology_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCriteria.lean, line 786](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCriteria.lean#L786).

> **Stacks 0DXG.** Let `A` be a ring, `f ∈ A`, `X` a topological space and `… → ℱ₂ → ℱ₁` an
> inverse system of sheaves of `A`-modules satisfying condition (1) of Stacks 0H39. If for some
> `m` the image of `H^{p+1}(X, ℱ_m) → H^{p+1}(X, ℱ₁)` has finite length over `A`, or `A` is
> Noetherian and the intersection of all those images is a finite `A`-module, then the inverse
> system `n ↦ H^p(X, ℱ_n)` satisfies the Mittag-Leffler condition.

```lean
theorem isMittagLefflerCategorical_of_finite_cohomology_image
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [∀ U, IsMulCommutative (R.obj.obj U)]
    (A : Type u) [CommRing A]
    [Algebra A (R.obj.obj (op (⊤ : Opens X)))] (f : A)
    (obj : ℕ → SheafOfModules.{u} R)
    (map : ∀ n, obj (n + 1) ⟶ obj n) (p : ℕ) :
    let E := SheafOfModules.evaluation R (op (⊤ : Opens X))
    let G := E.rightDerived (p + 1)
    letI : Module A (G.obj (obj 0)) :=
      Module.compHom (G.obj (obj 0)) (algebraMap A (R.obj.obj (op (⊤ : Opens X))))
    letI : IsScalarTower A (R.obj.obj (op (⊤ : Opens X))) (G.obj (obj 0)) :=
      ⟨fun a b x => by
        rw [Algebra.smul_def]
        change (algebraMap A (R.obj.obj (op (⊤ : Opens X))) a * b) • x =
          (algebraMap A (R.obj.obj (op (⊤ : Opens X))) a) • (b • x)
        exact mul_smul _ _ _⟩
    ((∃ n : ℕ, IsFiniteLength A
        (↥((LinearMap.range (G.map (Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.proj obj
          map n)).hom).restrictScalars A))) ∨
      (IsNoetherianRing A ∧ Module.Finite A
        (↥(⨅ n : ℕ,
          (LinearMap.range (G.map (Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.proj obj
            map n)).hom).restrictScalars A)))) →
      Stacks.Cohomology.InverseSystems.TorsionFreeDivisible.Condition1
        (Stacks.SheafOfModules.terminalSectionToEnd R (⊤ : Opens X) isTerminalTop
          (algebraMap A (R.obj.obj (op (⊤ : Opens X))) f)) obj map →
      IsMittagLefflerCategorical
        (Functor.ofOpSequence map ⋙ E.rightDerived p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.36, Tag 0H38](https://stacks.math.columbia.edu/tag/0H38)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
