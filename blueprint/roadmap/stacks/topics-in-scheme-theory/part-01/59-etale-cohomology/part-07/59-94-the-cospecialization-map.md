---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_pullback_cospecializationUnit, AlgebraicGeometry.isIso_pullback_cospecializationUnit_of_isGE, AlgebraicGeometry.specializationStalk_comp_baseChange_comp_cospecializationMap_of_isGE, AlgebraicGeometry.isIso_specializationStalk_and_cospecializationMap_of_isProper, AlgebraicGeometry.isIso_specializationMap_of_smooth_of_isProper_unconditional
statement: formalized
proof: formalized
---

# 59.94 The cospecialization map

Section 59.94 of the Stacks Project, [Tag 0GJT](https://stacks.math.columbia.edu/tag/0GJT). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GJU, a lemma

[Tag 0GJU](https://stacks.math.columbia.edu/tag/0GJU) in the Stacks Project.

**`AlgebraicGeometry.isIso_pullback_cospecializationUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/CospecializationMap.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/CospecializationMap.lean#L255). The attribute's comment: “modulo derived-stalk conservativity and the stalk computation”.

> Assume that isomorphy in unbounded derived categories of abelian sheaves on small étale sites
> is detected on stalks (`hcons`) and that the stalks of `i⁻¹β_{K,s,t}` are canonical maps of
> Tag 0GJN (`hcomp`). For a morphism of schemes `f : X ⟶ S` which is locally acyclic relative to an
> object `K` of `D(X_étale)`, the inverse image on the closed geometric fibre `X_s` of the
> comparison `β_{K,s,t} : K|_Y ⟶ Rh_*(K|_{X_t})` is an isomorphism.

```lean
theorem isIso_pullback_cospecializationUnit
    (hla : IsLocallyAcyclicRelative B hX hS f K)
    (hcons : HasDerivedStalkConservativity.{u})
    (hcomp : HasCospecializationStalkComparison B) :
    IsIso ((smallEtaleDerivedPullbackAb
      (geometricFibreToStrictHenselizationBaseChange B hS f s)).map
        (cospecializationUnit B hS f s t K))
```

**`AlgebraicGeometry.isIso_pullback_cospecializationUnit_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/ProperLocallyAcyclicSpecialization.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/ProperLocallyAcyclicSpecialization.lean#L76).

> **[Stacks, Tag 0GJU].** Let `f : X ⟶ S` be a morphism of schemes, `s` a geometric point of
> `S`, `t` a geometric point of `Spec 𝒪^{sh}_{S,s}`, and `K` an object of `D(X_étale)` which is
> bounded below and relative to which `f` is locally acyclic. Write `Y = X ×_S Spec 𝒪^{sh}_{S,s}`,
> `h : X_t ⟶ Y` for the fibre over `t` and `i : X_s ⟶ Y` for the closed geometric fibre. Then the
> inverse image `i⁻¹β_{K,s,t}` of the comparison `β_{K,s,t} : K|_Y ⟶ Rh_*(K|_{X_t})` is an
> isomorphism.

```lean
theorem isIso_pullback_cospecializationUnit_of_isGE (K : smallEtaleDerivedCategory X) (m : ℤ)
    (hK : K.IsGE m) (hla : IsLocallyAcyclicRelative B hX hS f K) :
    IsIso ((smallEtaleDerivedPullbackAb
      (geometricFibreToStrictHenselizationBaseChange B hS f s)).map
        (cospecializationUnit B hS f s t K))
```

## Tag 0GJV, a lemma

[Tag 0GJV](https://stacks.math.columbia.edu/tag/0GJV) in the Stacks Project.

**`AlgebraicGeometry.specializationStalk_comp_baseChange_comp_cospecializationMap_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/CospecializationSquareLocallyAcyclic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/CospecializationSquareLocallyAcyclic.lean#L92).

> **[Stacks, Tag 0GJV].** Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of
> schemes, `s` a geometric point of `S`, `t` a geometric point of `Spec 𝒪^{sh}_{S,s}`, and `K` an
> object of `D(X_étale)` which is bounded below and relative to which `f` is locally acyclic, so
> that the cospecialization map `cosp : RΓ(X_t, K) ⟶ RΓ(X_s, K)` is defined (Stacks 0GJU,
> `AlgebraicGeometry.isIso_pullback_cospecializationUnit_of_isGE`). Then the square
>
> ```
> (Rf_*K)_s ----------> RΓ(X_s, K)
>    | sp                    ^ cosp
>    v                       |
> (Rf_*K)_t ----------> RΓ(X_t, K)
> ```
>
> commutes: `sp` followed by the base change map of Stacks 0GIX at `t` and by `cosp` is the base
> change map of Stacks 0GIX at `s`. Here `X_s` and `X_t` are the geometric fibres of `f` at `s` and
> at the image of `t` in `S`, and the stalk of `Rf_*K` at `t` is taken at that image.

```lean
theorem specializationStalk_comp_baseChange_comp_cospecializationMap_of_isGE
    [QuasiCompact f] [QuasiSeparated f] (K : smallEtaleDerivedCategory X) (m : ℤ)
    (hK : K.IsGE m) (hla : IsLocallyAcyclicRelative B hX hS f K) :
    haveI := isIso_pullback_cospecializationUnit_of_isGE B hX hS f s t K m hK hla
    (smallEtaleDerivedSpecializationStalkAbAt B S hS s t).app
          ((smallEtaleDerivedPushforwardAb f).obj K) ≫
        (derivedPushforwardStalkToStrictHenselizationSections B hS f
          (t.map (strictHenselizationToBase B S hS s))).app K ≫
        (strictHenselizationSectionsToFibreSections B hS f
          (t.map (strictHenselizationToBase B S hS s))).app K ≫
        cospecializationMapGeometricFibre B hS f s t K =
      (derivedPushforwardStalkToStrictHenselizationSections B hS f s).app K ≫
        (strictHenselizationSectionsToFibreSections B hS f s).app K
```

## Tag 0GJW, a lemma

[Tag 0GJW](https://stacks.math.columbia.edu/tag/0GJW) in the Stacks Project.

**`AlgebraicGeometry.isIso_specializationStalk_and_cospecializationMap_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/ProperLocallyAcyclicSpecialization.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/ProperLocallyAcyclicSpecialization.lean#L127). References: SGA 4 XVI (2.3), “special case”; SGA 4½ Arcata (5.3.1), “more general”; SGA 4½ Th finitude (5.2.4), “for proper f”.

> **[Stacks, Tag 0GJW].** Let `f : X ⟶ S` be a morphism of schemes and `K` an object of
> `D(X_étale)` such that
>
> 1. `K` is bounded below,
> 2. `f` is locally acyclic relative to `K`,
> 3. `f` is proper, and
> 4. `K` has torsion cohomology sheaves.
>
> Then for every geometric point `s` of `S` and every geometric point `t` of `Spec 𝒪^{sh}_{S,s}`
> the specialization map `sp : (Rf_*K)_s ⟶ (Rf_*K)_t` is an isomorphism, and the cospecialization
> map `cosp : RΓ(X_t, K) ⟶ RΓ(X_s, K)` — defined because `i⁻¹β_{K,s,t}` is an isomorphism (Tag
> 0GJU) — is an isomorphism.
>
> The objects named in the statement, all defined in this library with no hypothesis beyond their
> data:
>
> * `smallEtaleDerivedCategory X` (`EtaleCohomology/DerivedEtale.lean`) is `D(X_étale)`, the derived
>   category of abelian sheaves on the small étale site; `K.IsGE m` says `K` is bounded below.
> * `IsLocallyAcyclicRelative B hX hS f K` (`LocalAcyclicity/Basic.lean`) is part (2) of
>   Definition 0GJP: at every geometric point `x` of `X` and every geometric point `t` of
>   `Spec 𝒪^{sh}_{S,f(x)}` the map `α_{K,x,t} : K_x ⟶ RΓ(F_{x,t}, K)` to the cohomology of the
>   variety of vanishing cycles is an isomorphism; `B` is a big étale site containing `X` and `S`, a
>   size device only.
> * `Stacks.Torsion.torsionCohomologyProperty` (`CategoryTheory/Sites/Cohomology/Torsion/
>   StacksFrontier/CategoryTheory/Sites/Cohomology/Torsion/DerivedCategoryOfTorsionSheaves.lean`) says every cohomology sheaf of `K` is torsion.
> * `smallEtaleDerivedPushforwardAb f` (`EtaleCohomology/StalkOfDerivedPushforward.lean`) is
>   `Rf_*`, the total right derived functor of direct image; its existence is the proved instance
>   `Stacks.EtaleCohomology.hasRightDerivedFunctor_smallEtalePushforwardAb`
>   (`EtaleCohomology/SmallEtaleUnboundedDerivations.lean`), and that of `RΓ` the proved instance
>   `Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor`
>   (`EtaleCohomology/SmallEtaleDerivedGlobalSectionsExistence.lean`).
> * `smallEtaleDerivedSpecializationStalkAbAt B S hS s t`
>   (`EtaleCohomology/SpecializationMapAndFibres.lean`) is the specialization map
>   `sp : (−)_s ⟶ (−)_t` on derived stalks, at the image of `t` in `S`.
> * `cospecializationUnit B hS f s t K` (`LocalAcyclicity/CospecializationMap.lean`) is
>   `β_{K,s,t} : K|_Y ⟶ Rh_*(K|_{X_t})`, and `geometricFibreToStrictHenselizationBaseChange B hS f s`
>   (`EtaleCohomology/StalkOfDerivedPushforward.lean`) is `i : X_s ⟶ Y`.
> * `cospecializationMap B hS f s t K` (`LocalAcyclicity/CospecializationMapDerived.lean`) is the
>   cospecialization map of Section 0GJT.

```lean
theorem isIso_specializationStalk_and_cospecializationMap_of_isProper [IsProper f]
    (K : smallEtaleDerivedCategory X) (m : ℤ) (hK : K.IsGE m)
    (hla : IsLocallyAcyclicRelative B hX hS f K)
    (hKt : Stacks.Torsion.torsionCohomologyProperty.{u + 1} (smallEtaleTopology X) K) :
    IsIso ((smallEtaleDerivedSpecializationStalkAbAt B S hS s t).app
        ((smallEtaleDerivedPushforwardAb f).obj K)) ∧
      ∃ _ : IsIso ((smallEtaleDerivedPullbackAb
          (geometricFibreToStrictHenselizationBaseChange B hS f s)).map
            (cospecializationUnit B hS f s t K)),
        IsIso (cospecializationMap B hS f s t K)
```

## Tag 0GKD, a lemma

[Tag 0GKD](https://stacks.math.columbia.edu/tag/0GKD) in the Stacks Project.

**`AlgebraicGeometry.isIso_specializationMap_of_smooth_of_isProper_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SmoothProperSpecializationUnconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SmoothProperSpecializationUnconditional.lean#L68). References: SGA 4 XVI (2.3), “special case”; SGA 4½ Th finitude (5.2.4), “partial”; SGA 7 I (2.1), “more general”.

> Let `f : X ⟶ S` be a morphism of schemes and `F` an abelian sheaf on `X_étale`. Assume
>
> 1. `f` is smooth and proper,
> 2. `F` is locally constant, and
> 3. for every geometric point `x̄` of `X` the stalk `F_{x̄}` is a torsion group all of whose
>    elements have order prime to the residue characteristic of `x̄`.
>
> Then for every geometric point `s̄` of `S` and every geometric point `t̄` of
> `Spec 𝒪^{sh}_{S,s̄}` the specialization map `sp : (Rf_*F)_{s̄} ⟶ (Rf_*F)_{t̄}` is an
> isomorphism; the stalk at `t̄` is taken at its image in `S`.
>
> The strict henselization is formed in a big étale site `B` containing `X` and `S`, which exists
> for every pair of schemes; the statement holds for every such `B`.

```lean
theorem isIso_specializationMap_of_smooth_of_isProper_unconditional (B : BigEtaleSite.{u})
    {X S : Scheme.{u}} (hX : B.Contains X) (hS : B.Contains S) (f : X ⟶ S) [Smooth f]
    [IsProper f] (F : Sheaf X.smallEtaleTopology Ab.{u + 1})
    (hFlc : Stacks.ConstantSheaf.IsLocallyConstant X.smallEtaleTopology F)
    (hFtors : ∀ (x : GeometricPoint X) (a : (smallEtaleStalkAb x.hom).obj F),
      ∃ n : ℕ, 0 < n ∧
        (ringChar x.residueField = 0 ∨ Nat.Coprime n (ringChar x.residueField)) ∧ n • a = 0)
    (s : GeometricPoint S) (t : GeometricPoint (strictHenselization B S hS s)) :
    IsIso ((smallEtaleDerivedSpecializationStalkAbAt B S hS s t).app
      ((smallEtaleDerivedPushforwardAb f).obj
        ((DerivedCategory.singleFunctor (Sheaf X.smallEtaleTopology Ab.{u + 1}) 0).obj F)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.94, Tag 0GJT](https://stacks.math.columbia.edu/tag/0GJT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
