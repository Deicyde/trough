---
declaration: section
origin: cited
lean: Stacks.Chow.exists_splittingMorphism, Stacks.Chow.exists_splittingMorphism_basechange, Stacks.Chow.exists_splittingMorphism_unconditional, Stacks.Chow.exists_splittingMorphism_basechange_uniform, Stacks.Chow.exists_splittingMorphism_isProjective, Stacks.Chow.exists_splittingMorphism_isProjective_ofInvertible, Stacks.Chow.exists_splittingMorphism_universal, Stacks.Chow.exists_splittingMorphism_isBundleTower
statement: formalized
proof: formalized
---

# 42.43 The splitting principle

Section 42.43 of the Stacks Project, [Tag 02UK](https://stacks.math.columbia.edu/tag/02UK). 6 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02UL, a lemma

[Tag 02UL](https://stacks.math.columbia.edu/tag/02UL) in the Stacks Project.

**`Stacks.Chow.exists_splittingMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundle.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundle.lean#L461). The attribute's comment: “clauses (1) and (2) over X itself, for a finite collection of finite locally free modules of constant ranks, with relative dimension d = sum of binom(r\_i, 2). Carries the projective bundle of a finite locally free module of rank m+1 as a BundleStep, i.e. as Stacks 02TX for flatness, properness (Stacks 0800) and relative dimension m, Stacks 02S1 for the descent of flat pullback to Chow groups, Stacks 01O4, 02SO and 02TI for c\_1(O\_P(1)) cap -, the injectivity half of Stacks 02TX for the projective space bundle map, and Stacks 0B3V for the tautological short exact sequence with locally free kernel of rank m. Injectivity of pi^* itself is NOT carried: it is derived from the 02TX bundle map. The source says projective; only properness is carried through the tower, because IsProjectiveMorphism of the identity needs the identification of P^0\_X with X, which this repository lacks. Clause (1) after a base change is exists\_splittingMorphism\_basechange”.

> **Stacks 02UL, the splitting principle.** Let `(S, δ)` be the situation of Stacks 02QL, let
> `X` be locally of finite type over `S` and let `ℰ_i`, `i ∈ I` finite, be finite locally free
> `𝒪_X`-modules of ranks `r_i`. There is a flat proper morphism `π : P ⟶ X` of relative dimension
> `d = ∑_i binom(r_i, 2)` such that
>
> 1. the flat pullback `π^* : A_k(X) ⟶ A_{k+d}(P)` of Stacks 0FVK is injective in every degree, and
> 2. each `π^*ℰ_i` has a filtration of length `r_i` whose successive quotients are invertible
>    `𝒪_P`-modules.
>
> The relative dimension is `∑_i binom(r_i, 2)` and not `∑_i (r_i - 1)`: splitting a rank-`r`
> module takes `r - 1` layers, of relative dimensions `r - 1, r - 2, …, 1`.

```lean
theorem exists_splittingMorphism (C : ChowSituation.{u})
    (step : ∀ {Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (F : Y.Modules) (m : ℕ),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F (m + 1) →
        BundleStep C sY F m)
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I]
    (E : I → X.Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)
```

**`Stacks.Chow.exists_splittingMorphism_basechange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundle.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundle.lean#L495). The attribute's comment: “clause (1) after a base change, in the WEAKENED form that for EACH f : Y -> X there is a morphism P\_Y -> Y with the same relative dimension, the same filtrations and injectivity in every degree. It is NOT asserted that P\_Y is the fibre product Y x\_X P of the single morphism delivered by exists\_splittingMorphism, so this is weaker than clause (1) of the source. The reason is NOT that the base-change comparison of projective bundles is missing: the comparison projectiveBundleBaseChange and the cartesianness of its square (isPullback\_projectiveBundleBaseChange) are both proved in this repository, untagged, and relative dimension is stable under base change by Stacks 02NK. What is missing is Stacks 02S1 for the base-changed projections (never derived for a base change here), base-change compatibility of the carried BundleStep, and the identification of the base change of the tower with the tower of base changes. Carries the same BundleStep operator as exists\_splittingMorphism”.

> **Stacks 02UL, clause (1) after an arbitrary base change.** For every `f : Y ⟶ X` with `Y`
> locally of finite type over the base there is a flat proper morphism `π_Y : P_Y ⟶ Y` of the same
> relative dimension `d = ∑_i binom(r_i, 2)` along which flat pullback on Chow groups is injective
> in every degree, and such that each `π_Y^* f^* ℰ_i` has a filtration of length `r_i` with
> invertible successive quotients.
>
> This is the splitting principle run over `Y` on the modules `f^*ℰ_i`, whose ranks are the `r_i`
> because finite local freeness of given rank is stable under pullback. **It does not assert that
> `P_Y` is `Y ×_X P` for the `P` of `Stacks.Chow.exists_splittingMorphism`**, and that is a genuine
> weakening of clause (1).

```lean
theorem exists_splittingMorphism_basechange (C : ChowSituation.{u})
    (step : ∀ {Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (F : Y.Modules) (m : ℕ),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F (m + 1) →
        BundleStep C sY F m)
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I]
    (E : I → X.Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i))
    {Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : Y ⟶ X) :
    ∃ T : SplittingMorphism C sY (∑ i, (r i).choose 2),
      ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj ((Scheme.Modules.pullback f).obj (E i))) (r i)
```

**`Stacks.Chow.exists_splittingMorphism_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundleUnconditional.lean, line 564](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundleUnconditional.lean#L564). The attribute's comment: “clauses (1) and (2) over X itself, for a finite collection of finite locally free modules of constant ranks r\_i, with relative dimension d = sum of binom(r\_i, 2), and NOTHING CARRIED: the only hypotheses are that each module is finite locally free of constant rank r\_i. The layer of the tower is the projective bundle of the module itself, Stacks.Chow.bundleStep, so every fact about it that the parametrised form exists\_splittingMorphism takes in its step argument is PROVED here: Stacks 02TX for flatness and relative dimension m of the projection (Stacks.Chow.flat\_bundleProj, Stacks.Chow.relativeDimension\_bundleProj -- for an arbitrary module of constant rank, not only for a free one), Stacks 0800 for properness (Stacks.Chow.isProper\_bundleProj), Stacks 02S1 for the descent of flat pullback to Chow groups (Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence\_general, with nothing carried), Stacks 01O4, 02SO and 02TI for c\_1(O\_P(1)) cap - (Stacks.Chow.bundleTwist with Stacks.Chow.invCap), the injectivity half of Stacks 02TX for the projective space bundle map (Stacks.Chow.projectiveBundleRelationInjective\_of\_bundleMap at Stacks.Chow.projectiveBundle\_formula), and Stacks 0B3V for the tautological short exact sequence with locally free kernel of rank m (Stacks.Chow.shortExact\_bundleTautological, Stacks.Chow.isFiniteLocallyFreeOfRank\_kernel\_bundleTautological, including the rank-one end m = 0 where the kernel has rank zero). Injectivity of pi^* itself is derived from the 02TX bundle map, not assumed. WEAKENED IN ONE WORD: the source says the morphism is projective and only properness is delivered, because IsProjectiveMorphism of the identity of X needs the identification of P^0\_X with X, which this repository lacks. Clause (1) of the source quantifies over every f : Y -> X, and that full form is exists\_splittingMorphism\_basechange\_uniform, which is about the single morphism this theorem delivers”.

> The splitting principle. Let `X` be locally of finite type over the base `S` of `C` and let
> `ℰ_i`, `i ∈ I` finite, be finite locally free `𝒪_X`-modules of constant ranks `r_i`. There is a
> flat proper morphism `π : P ⟶ X` of relative dimension `d = ∑_i binom(r_i, 2)` such that
>
> 1. the flat pullback `π^* : A_k(X) ⟶ A_{k+d}(P)` is injective in every degree, and
> 2. each `π^*ℰ_i` has a filtration of length `r_i` whose successive quotients are invertible
>    `𝒪_P`-modules.

```lean
theorem exists_splittingMorphism_unconditional (C : ChowSituation.{u}) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I] (E : I → X.Modules)
    (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)
```

**`Stacks.Chow.exists_splittingMorphism_basechange_uniform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundleUnconditional.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FlagBundleUnconditional.lean#L614). The attribute's comment: “clauses (1) and (2) for a finite collection of finite locally free modules of constant ranks r\_i, with relative dimension d = sum of binom(r\_i, 2), and with clause (1) in the form the source states it: ONE morphism pi : P -> X, and for EVERY f : Y -> X injectivity in every degree of the flat pullback along the base change of that pi, which is Stacks.Chow.BaseChangeInjective quantified over every cartesian square over pi and f. The only hypotheses are the source's: each module finite locally free of constant rank r\_i. Clause (1) is proved through the iteration -- base case the identity of X, whose base change is an isomorphism; inductive step the splitting of the base change of a composite by CategoryTheory.IsPullback.of\_bot together with Stacks 02RD for a composite pullback, the base-changed layer being the projective bundle of the pulled-back module by Stacks.ProjectiveBundle.isPullback\_baseChangeHom and its pullback injective by the injectivity half of Stacks 02TX. The single word of the tag delivered more weakly is projective, delivered as proper: IsProjectiveMorphism of the identity of X needs the identification of P^0\_X with X, which this repository lacks”.

> The splitting principle with injectivity after every base change. Let `X` be locally of
> finite type over the base `S` of `C` and let `ℰ_i`, `i ∈ I` finite, be finite locally free
> `𝒪_X`-modules of constant ranks `r_i`. There is a single flat proper morphism `π : P ⟶ X` of
> relative dimension `d = ∑_i binom(r_i, 2)` such that
>
> 1. for any `f : Y ⟶ X` with `Y` locally of finite type over the base, the flat pullback
>    `π_Y^* : A_k(Y) ⟶ A_{k+d}(Y ×_X P)` along the base change of `π` is injective in every
>    degree, and
> 2. each `π^*ℰ_i` has a filtration of length `r_i` whose successive quotients are invertible
>    `𝒪_P`-modules.

```lean
theorem exists_splittingMorphism_basechange_uniform (C : ChowSituation.{u}) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I] (E : I → X.Modules)
    (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      BaseChangeInjective C sX T.π (∑ i, (r i).choose 2) ∧
        ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
          ((Scheme.Modules.pullback T.π).obj (E i)) (r i)
```

**`Stacks.Chow.exists_splittingMorphism_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingProjective.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingProjective.lean#L181).

> **Stacks 02UL (the splitting principle).** Let `(S, δ)` be as in Situation 02QL, `X` locally
> of finite type over `S` and `ℰ_i` (`i ∈ I`, `I` finite) finite locally free `𝒪_X`-modules of
> ranks `r_i`. There is a morphism `π : P ⟶ X` which is
>
> * projective (Stacks 01W8), flat, and of relative dimension `d = ∑_i binom(r_i, 2)`,
>
> such that
>
> 1. for every morphism `f : Y ⟶ X` with `Y` locally of finite type over `S`, the flat pullback
>    `π_Y^* : CH_k(Y) ⟶ CH_{k+d}(Y ×_X P)` along the base change of `π` is injective for every
>    `k` (`Stacks.Chow.UniversallyChowInjective`), and
> 2. each `π^*ℰ_i` has a filtration whose successive quotients `ℒ_{i,1}, …, ℒ_{i,r_i}` are
>    invertible `𝒪_P`-modules;
>
> moreover the restriction map `A^*(X) ⟶ A^*(P)` of Stacks 0B7F is injective.

```lean
theorem exists_splittingMorphism_isProjective (C : ChowSituation.{u}) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I] (E : I → X.Modules)
    (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      IsProjective T.π ∧ Flat T.π ∧
      AlgebraicGeometry.RelativeDimension T.π (∑ i, (r i).choose 2) ∧
      UniversallyChowInjective C T.π (∑ i, (r i).choose 2) T.relDim ∧
      (∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)) ∧
      ∀ (G : GysinSystem C) (hgys : G.IsNaturalUnderBaseChangeIso),
        Function.Injective (chowCohomologyTotalRestriction C G sX T.π hgys)
```

**`Stacks.Chow.exists_splittingMorphism_isProjective_ofInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingProjectiveOfInvertible.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingProjectiveOfInvertible.lean#L77).

> **Stacks 02UL (the splitting principle).** Let `(S, δ)` be as in Situation 02QL, `X` locally
> of finite type over `S` and `ℰ_i` (`i ∈ I`, `I` finite) finite locally free `𝒪_X`-modules of
> ranks `r_i`. There is a morphism `π : P ⟶ X` which is
>
> * projective (Stacks 01W8), flat, and of relative dimension `d = ∑_i binom(r_i, 2)`,
>
> such that
>
> 1. for every morphism `f : Y ⟶ X` with `Y` locally of finite type over `S`, the flat pullback
>    `π_Y^* : CH_k(Y) ⟶ CH_{k+d}(Y ×_X P)` along the base change of `π` is injective for every
>    `k` (`Stacks.Chow.UniversallyChowInjective`), and
> 2. each `π^*ℰ_i` has a filtration whose successive quotients `ℒ_{i,1}, …, ℒ_{i,r_i}` are
>    invertible `𝒪_P`-modules;
>
> moreover the restriction map `res : A^*(X) ⟶ A^*(P)` of Stacks 0B7F,
> `Stacks.Chow.chowCohomologyTotalRestrictionRingOfInvertible`, is injective. Nothing is assumed
> beyond the hypotheses of the tag.

```lean
theorem exists_splittingMorphism_isProjective_ofInvertible (C : ChowSituation.{u})
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I]
    (E : I → X.Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      IsProjective T.π ∧ Flat T.π ∧
      AlgebraicGeometry.RelativeDimension T.π (∑ i, (r i).choose 2) ∧
      UniversallyChowInjective C T.π (∑ i, (r i).choose 2) T.relDim ∧
      (∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)) ∧
      Function.Injective (chowCohomologyTotalRestrictionRingOfInvertible C sX T.π)
```

**`Stacks.Chow.exists_splittingMorphism_universal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/Unconditional.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/Unconditional.lean#L439). The attribute's comment: “both clauses, clause (1) in the source's form: for every f : Y -> X, with Y locally of finite type over S by an arbitrary structure morphism, flat pullback along the base change Y x\_X P -> Y is injective in every degree. Relative dimension d = sum of binom(r\_i, 2). The source says projective; the morphism delivered is flat and proper (each layer is a projective bundle, proper by Stacks 0800), but H-projectivity of the tower is not proved”.

> **Stacks 02UL, the splitting principle.** Let `(S, δ)` be the situation of Stacks 02QL, let
> `X` be locally of finite type over `S` and let `ℰ_i`, `i ∈ I` finite, be finite locally free
> `𝒪_X`-modules of ranks `r_i`. There is a flat proper morphism `π : P ⟶ X` of relative dimension
> `d = ∑_i binom(r_i, 2)`, along which flat pullback on Chow groups is injective in every degree,
> such that
>
> 1. for every morphism `f : Y ⟶ X` with `Y` locally of finite type over `S` the flat pullback
>    `π_Y^* : A_k(Y) ⟶ A_{k+d}(Y ×_X P)` along the base change `π_Y : Y ×_X P ⟶ Y` is injective in
>    every degree, and
> 2. each `π^*ℰ_i` has a filtration of length `r_i` whose successive quotients are invertible
>    `𝒪_P`-modules.
>
> The morphism is the iterated projective bundle
> (`Stacks.Chow.BundleStep.ofProjectiveBundle`); clause (1) is carried through the iteration as
> `Stacks.Chow.UniversallyInjectiveFlatPullback`.

```lean
theorem exists_splittingMorphism_universal (C : ChowSituation.{u}) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I] (E : I → X.Modules)
    (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      (∀ {Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : Y ⟶ X) (k : ℤ),
        Function.Injective (flatPullbackChow C (pullback.fst f T.π ≫ sY) sY (pullback.fst f T.π)
          rfl (∑ i, (r i).choose 2)
          (AlgebraicGeometry.RelativeDimension.of_isPullback
            (IsPullback.of_hasPullback f T.π).flip T.relDim) k
          (flatPullbackFactorsThroughRationalEquivalence_general C _ _ _ _ _ _ _))) ∧
      ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)
```

## Tag 0FVE, a remark

[Tag 0FVE](https://stacks.math.columbia.edu/tag/0FVE) in the Stacks Project.

**`Stacks.Chow.exists_splittingMorphism_isBundleTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ProjectiveBundleTower.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ProjectiveBundleTower.lean#L174). The attribute's comment: “clause (1) only: the 02UL morphism is a constant-rank projective bundle tower”.

> The morphism `π : P ⟶ X` of Stacks 02UL is a finite composition of projective space bundles
> associated to locally free modules of finite constant rank.
>
> Let `(S, δ)` be the situation of Stacks 02QL, let `X` be locally of finite type over `S` and let
> `ℰ_i`, `i ∈ I` finite, be finite locally free `𝒪_X`-modules of ranks `r_i`. Then there is a
> splitting morphism `T`, flat and proper of relative dimension `d = ∑_i binom(r_i, 2)`, with
> injective flat pullback on Chow groups in every degree, splitting every `ℰ_i`, and satisfying
> `Stacks.Chow.IsBundleTower`: it is the identity of `X` or the projection of one layer `𝐏(ℰ)` with
> `ℰ` finite locally free of constant rank, composed with such a tower over `𝐏(ℰ)`.

```lean
theorem exists_splittingMorphism_isBundleTower (C : ChowSituation.{u})
    (step : ∀ {Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (F : Y.Modules) (m : ℕ),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F (m + 1) →
        BundleStep C sY F m)
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I]
    (E : I → X.Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      IsBundleTower C sX (∑ i, (r i).choose 2) T ∧
        ∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
          ((Scheme.Modules.pullback T.π).obj (E i)) (r i)
```

**`Stacks.Chow.exists_splittingMorphism_isProjectiveBundleTower_recoversByCaps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingTowerRecovery.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/SplittingTowerRecovery.lean#L590).

> **Stacks 0FVE.** Let `(S, δ)` be as in Situation 02QL, `X` locally of finite type over `S`
> and `ℰ_i` (`i ∈ I`, finite) finite locally free `𝒪_X`-modules of ranks `r_i`. The morphism
> `π : P ⟶ X` built in the proof of Stacks 02UL — flat and proper of relative dimension
> `d = ∑_i binom(r_i, 2)`, with injective flat pullback on Chow groups, such that each `π^*ℰ_i` has
> a filtration with invertible successive quotients — has the further properties
>
> 1. `π` is a finite composition of projective space bundles associated to finite locally free
>    modules of constant rank (`Stacks.Chow.IsProjectiveBundleTower`, whose layers are the actual
>    projective bundles `Stacks.Chow.bundle`), and
> 2. there are invertible `𝒪_P`-modules `L_1, …, L_d` such that, with `ξ_j = c₁(L_j)`, every
>    `α ∈ CH_k(X)` satisfies `α = π_*(ξ_1 ∩ ⋯ ∩ ξ_d ∩ π^*α)`.

```lean
theorem exists_splittingMorphism_isProjectiveBundleTower_recoversByCaps (C : ChowSituation.{u})
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (I : Type) [Fintype I]
    (E : I → X.Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ T : SplittingMorphism C sX (∑ i, (r i).choose 2),
      (∀ i, Stacks.WeilCohomology.HasInvertibleFiltration T.P
        ((Scheme.Modules.pullback T.π).obj (E i)) (r i)) ∧
      IsProjectiveBundleTower C sX (∑ i, (r i).choose 2) T ∧
      ∃ (Ls : List (InvertibleModule T.P)) (hLs : Ls.length = ∑ i, (r i).choose 2),
        ∀ (k : ℤ) (α : chowGroup C sX k),
          properChowPushforward C T.sP sX T.π T.hsP k
              (properPushforwardFactorsThroughRationalEquivalence_of_isProper C T.sP sX T.π
                T.hsP k)
              (iteratedChernCapOnChow C T.sP (invCapList C T.sP Ls) k
                (chowGroupCast C T.sP (by rw [length_invCapList, hLs])
                  (T.pullbackChow k α))) = α
```

## Tag 0FA5, a lemma

[Tag 0FA5](https://stacks.math.columbia.edu/tag/0FA5) in the Stacks Project.

**`Stacks.Chow.GenuineChern.chernClass_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/ChernClassDual.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/ChernClassDual.lean#L396). The attribute's comment: “THE BIVARIANT AND UNCONDITIONAL FORM, an ADDITIONAL carrier -- the registration that already stood, Stacks.Chow.chernClassCapExt\_eq\_zsmul\_of\_dualFiltration, states the rule in the cycle vocabulary and carries two complete filtrations plus six further hypotheses, and Stacks.Chow.HasDualChernSignRule (which carries no attribute) states it as an assumed Prop on a carried total Chern class series; neither is superseded, because the three speak about three different renderings of c\_i in this repository. WHAT IS PROVED HERE: for every scheme X locally of finite type over the base of chapter 42, every finite locally free O\_X-module E of rank r, and every i with 0 <= i <= r, the equality c\_i(E^dual) = (-1)^i c\_i(E) of BIVARIANT CLASSES in A^i(X) -- the group of bivariant classes of degree i for the identity of X, Tag 0B76 -- at the Chern classes Stacks.Chow.GenuineChern.chernClass of Tag 0B7H. HYPOTHESES: exactly the rank, i.e. E is finite locally free of rank r, plus X locally of finite type over the base. NOTHING ELSE IS CARRIED: no filtration of E and no filtration of E^dual, no splitting datum, no normalisation c\_0 = 1, no binomial-transform equality, and no assumed compatibility of the cap products with flat pullback -- the last of these is now proved in this repository (Stacks.Chow.GenuineChern.intertwines\_chernFamily, Tag 02U8), which is what makes the source's reduction performable. The source's first paragraph -- choose pi : P -> X as in Tag 02UL, use injectivity of pi^* to reduce to a filtered E, dualise the filtration -- is replaced by an induction on r through the projective bundle P(E) of E alone: the tautological sequence 0 -> F -> pi^*E -> O(1) -> 0 has F finite locally free of rank r-1, its dual is short exact by the exactness of duality (Tag 0FV8), and the Whitney sum formula of Tag 02UI (unconditional here) computes both total Chern classes upstairs. This avoids the obstruction recorded at Stacks.Chow.chernClassCapExt\_eq\_zsmul\_of\_dualFiltration, namely that the filtration delivered by Tag 02UL is an inductive Prop from which the tower of modules Tag 02UJ takes as input cannot be eliminated: no filtration is ever needed, only one short exact sequence per inductive step. The rank of the dual is Stacks.AlgebraicGeometry.ReflexiveModules.isFiniteLocallyFreeOfRank\_dualSheaf (the dual-at-a-constant-rank clause of Tag 0FA7), which is what lets c\_i(E^dual) be written at all. The dual is Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf, SheafHom(E, O\_X) itself, and not a chosen tensor inverse. Also proved here, degreewise on cap products, is Stacks.Chow.GenuineChern.chernCap\_dualSheaf, the same identity for the cap products of Tag 02U6”.

> **Stacks 0FA5, bivariantly and unconditionally.** For a finite locally free `𝒪_X`-module `ℰ`
> of rank `r` on a scheme `X` locally of finite type over the base and every `0 ≤ i ≤ r`,
>
>   `c_i(ℰ^∨) = (-1)^i c_i(ℰ)`
>
> in `A^i(X)`, the group of bivariant classes of degree `i` for `𝟙 X` of Stacks 0B76, for the Chern
> classes `Stacks.Chow.GenuineChern.chernClass` of Stacks 0B7H.
>
> A bivariant class satisfying the characterization of Stacks 0B7H is unique
> (`Stacks.Chow.eq_of_isChernClassBivariant`), so it suffices to check that `(-1)^i c_i(ℰ)` caps by
> `c_i(g^*(ℰ^∨)) ∩ -` on every test scheme `g : T ⟶ X`. Integer multiples of bivariant classes are
> pointwise on cap products, so the left side is `(-1)^i (c_i(g^*ℰ) ∩ -)`, and that is
> `c_i(g^*(ℰ^∨)) ∩ -` by `Stacks.Chow.GenuineChern.chernCap_dualSheaf` applied to `g^*ℰ`, once the
> base-change isomorphism of Tag 0GMX identifies `g^*(ℰ^∨)` with `(g^*ℰ)^∨`.

```lean
theorem chernClass_dualSheaf {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (E : X.Modules) (r : ℕ)
    [hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    (j : Fin (r + 1)) :
    haveI := Stacks.AlgebraicGeometry.ReflexiveModules.isFiniteLocallyFreeOfRank_dualSheaf E r hE
    chernClass C sX (dualSheaf E) r j = ((-1 : ℤ) ^ (j : ℕ)) • chernClass C sX E r j
```

**`Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SectionZeroScheme/ArbitraryRankDual.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SectionZeroScheme/ArbitraryRankDual.lean#L151). The attribute's comment: “c\_i(E^dual) = (-1)^i c\_i(E) in A^i(X) for every finite locally free E (rank not necessarily constant) and every i >= 0, at the Chern classes of Tag 0ESW built from those of Tag 0B7H”.

> **Stacks 0FA5.** For a finite locally free `𝒪_X`-module `ℰ` on a scheme `X` locally of finite
> type over the base, of rank not necessarily constant, and every `i ≥ 0`,
>
>   `c_i(ℰ^∨) = (-1)^i c_i(ℰ)`
>
> in `A^i(X)`, for the Chern classes `Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree` of
> Stacks 0ESW, built from the bivariant Chern classes of Stacks 0B7H on the rank loci.
>
> Both sides are compared on the rank loci of `ℰ`, which are those of `ℰ^∨`
> (`Stacks.Chow.SectionZeroScheme.rankLocus_dualSheaf`); on `X_r` the identity is the constant-rank
> case `Stacks.Chow.GenuineChern.chernClass_dualSheaf` together with `(ℰ^∨)|_{X_r} ≅ (ℰ|_{X_r})^∨`,
> and for `i > r` both sides restrict to zero.

```lean
theorem chernClassOfLocallyFree_dualSheaf (i : ℕ) :
    haveI := isFiniteLocallyFree_dualSheaf E hE
    chernClassOfLocallyFree (dualSheaf E) C sX i =
      ((-1 : ℤ) ^ i) • chernClassOfLocallyFree E C sX i
```

**`Stacks.Chow.chernClassCapExt_eq_zsmul_of_dualFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualChernClasses.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualChernClasses.lean#L248). The attribute's comment: “CORRECTION OF FORM: the source states c\_i(E^dual) = (-1)^i c\_i(E) in the bivariant ring A^i(X). This development has no bivariant ring and no total Chern class, for the reason recorded in the Stacks 02UH clause of StacksFrontier.AlgebraicGeometry.Chow.ChernWhitney.CapProductRelation, so -- exactly as for Stacks 02UJ, which this result is read on top of -- the identity is stated degree by degree as cap products against a fixed cycle: for every n, every alpha in CycleGroup C p n and every i >= 0, c\_i(E^dual) cap alpha = (-1)^i times (c\_i(E) cap alpha) in A\_\{n-i}(X). It holds for EVERY i and EVERY rank r; no degree and no rank is special-cased. WHAT IS CARRIED: the reduction of the source's first paragraph, i.e. the two filtrations themselves, as the towers of short exact sequences that Stacks 02UJ consumes -- for E with invertible quotients L\_j, and for E^dual with quotients M\_j satisfying L\_j tensor M\_j iso O\_X, which is the source's E\_\{i-1}^perp/E\_i^perp iso L\_i^\{tensor -1}. The source gets these from Stacks 02UL and the injectivity of pi^*. That reduction CANNOT be performed in this repository, for two independent reasons: (1) Stacks 02UL is Stacks.Chow.exists\_splittingMorphism and the filtration it delivers is Stacks.WeilCohomology.HasInvertibleFiltration, an inductive Prop, from which the tower of modules and maps that Stacks 02UJ needs -- which is data -- cannot be eliminated; (2) nothing in this repository states that the Chern class cap product commutes with flat pullback (the clause of Stacks 02U0 quoted as Stacks 02U1), so injectivity of pi^* has no identity on P to descend to X. ALSO CARRIED, each of them an input of Stacks 02UJ itself and carried there for the same reason: chern and chernDual, the Stacks 02U0 component data in every rank; hnorm and hnormDual, the Stacks 02U0 normalisation c\_0 = 1 along each tower; hbinom and hbinomDual, the equality of binomial transforms that Stacks 02UD gives once Stacks 02UG is applied, neither of which is proved here; and hfacL, hfacM, Stacks 02TI for c\_1 of each quotient. NOT CARRIED, i.e. proved here: the line-bundle case c\_1(L^\{tensor -1}) = -c\_1(L), deduced from the two clauses of Stacks 02SP as firstChernCapStep\_eq\_neg\_of\_tensorObj\_iso\_unit and absent from this repository before this file; and the formal computation the source omits, e\_k(-x) = (-1)^k e\_k(x), proved for every degree and every length as elemSymmChernCap\_eq\_zsmul\_of\_neg\_steps. The dual is given as a tensor inverse rather than as Stacks.SheafOfModules.dualSheaf; by Stacks 0B8K the two agree up to isomorphism and c\_1 depends only on the isomorphism class (firstChernClassCapOfInvertible\_congr), so this is a change of spelling and not a weakening”.

> **Stacks 0FA5, componentwise on cap products.** Let `ℰ` be finite locally free of rank `r`
> with a filtration whose successive quotients are the invertible modules `ℒ_0, …, ℒ_{r-1}`, and
> let `ℰ^∨` be finite locally free of rank `r` with the dual filtration, whose successive quotients
> `ℳ_j` are tensor inverses of the `ℒ_j`. Both filtrations are presented as the towers of short
> exact sequences `0 ⟶ ℒ_j ⟶ ℰ_{j+1} ⟶ ℰ_j ⟶ 0` and `0 ⟶ ℳ_j ⟶ ℰ^∨_{j+1} ⟶ ℰ^∨_j ⟶ 0` that
> Stacks 02UJ consumes. Then for every `n`-cycle `α` and every `i`
>
>   `c_i(ℰ^∨) ∩ α = (-1)^i • (c_i(ℰ) ∩ α)`
>
> in `A_{n-i}(X)`, which is the sign rule of the source read degree by degree against `α`.

```lean
theorem chernClassCapExt_eq_zsmul_of_dualFiltration
    (hdual : ∀ j, Scheme.Modules.tensorObj (L j) (M j) ≅ SheafOfModules.unit X.ringCatSheaf)
    (E EDual : ℕ → X.Modules)
    (sub : ∀ j : Fin r, L j ⟶ E ((j : ℕ) + 1)) (proj : ∀ j : Fin r, E ((j : ℕ) + 1) ⟶ E (j : ℕ))
    (hzero : ∀ j : Fin r, sub j ≫ proj j = 0)
    (hexact : ∀ j : Fin r, (ShortComplex.mk (sub j) (proj j) (hzero j)).ShortExact)
    (hrank : ∀ m : ℕ, m ≤ r → PullbackPreservesRank (E m) m)
    (subDual : ∀ j : Fin r, M j ⟶ EDual ((j : ℕ) + 1))
    (projDual : ∀ j : Fin r, EDual ((j : ℕ) + 1) ⟶ EDual (j : ℕ))
    (hzeroDual : ∀ j : Fin r, subDual j ≫ projDual j = 0)
    (hexactDual : ∀ j : Fin r,
      (ShortComplex.mk (subDual j) (projDual j) (hzeroDual j)).ShortExact)
    (hrankDual : ∀ m : ℕ, m ≤ r → PullbackPreservesRank (EDual m) m)
    (chern chernDual : ∀ m : ℕ, ChernClassCycleRule C m) (α : CycleGroup C p n)
    (hnorm : ∀ (m : ℕ) (hm : m ≤ r),
      chernClassCapExt C p n (E m) m (hrank m hm) (chern m) 0 α = cycleClassDegreeZero C p n α)
    (hnormDual : ∀ (m : ℕ) (hm : m ≤ r),
      chernClassCapExt C p n (EDual m) m (hrankDual m hm) (chernDual m) 0 α =
        cycleClassDegreeZero C p n α)
    (hbinom : ∀ j : Fin r, ∀ i ≤ (j : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (L j) (hfacL j)) ((j : ℕ) + 1)
          (chernCapFamily C p n (E ((j : ℕ) + 1)) ((j : ℕ) + 1) (hrank ((j : ℕ) + 1) j.isLt)
            (chern ((j : ℕ) + 1)) α) i =
        binomialTransform (inverseFirstChernCapStep C p n (L j) (hfacL j)) (j : ℕ)
          (chernCapFamily C p n (E (j : ℕ)) (j : ℕ) (hrank (j : ℕ) j.isLt.le)
            (chern (j : ℕ)) α) i)
    (hbinomDual : ∀ j : Fin r, ∀ i ≤ (j : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (M j) (hfacM j)) ((j : ℕ) + 1)
          (chernCapFamily C p n (EDual ((j : ℕ) + 1)) ((j : ℕ) + 1)
            (hrankDual ((j : ℕ) + 1) j.isLt) (chernDual ((j : ℕ) + 1)) α) i =
        binomialTransform (inverseFirstChernCapStep C p n (M j) (hfacM j)) (j : ℕ)
          (chernCapFamily C p n (EDual (j : ℕ)) (j : ℕ) (hrankDual (j : ℕ) j.isLt.le)
            (chernDual (j : ℕ)) α) i)
    (k : ℕ) :
    chernClassCapExt C p n (EDual r) r (hrankDual r le_rfl) (chernDual r) k α =
      ((-1 : ℤ) ^ k) • chernClassCapExt C p n (E r) r (hrank r le_rfl) (chern r) k α
```

**`Stacks.Chow.homPart_totalChern_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualTotalChern.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualTotalChern.lean#L283). The attribute's comment: “constant rank: for every X locally of finite type over S, every finite locally free E of rank r and every i, with no further hypothesis. c\_i(E) is the degree-i part TotalChowClass.homComponent i (totalChern C sX E r) of the total Chern class in the ring TotalChowClass C sX of total Chow cohomology classes, the bivariant Chern class of Stacks 0B7H, and E^dual is the dual sheaf Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf E = SheafHom(E, O\_X)”.

> **Stacks 0FA5**, constant rank: for `ℰ` finite locally free of rank `r` on `X`,
>
>   `c_i(ℰ^∨) = (-1)^i c_i(ℰ)`
>
> in `A^i(X)`, for every `i`, where `c_i(-)` is the degree-`i` part of the total Chern class, the
> bivariant Chern class of Stacks 0B7H, and `ℰ^∨` is the dual sheaf `SheafHom(ℰ, 𝒪_X)`.

```lean
theorem homPart_totalChern_dualSheaf (E : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (i : ℕ) :
    TotalChowClass.homComponent i (totalChern C sX (dualSheaf E) r) =
      ((-1 : ℤ) ^ i) • TotalChowClass.homComponent i (totalChern C sX E r)
```

**`Stacks.Chow.homPart_totalChernOfFiniteLocallyFree_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualTotalChern.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/DualTotalChern.lean#L321). The attribute's comment: “the lemma as stated, for every X locally of finite type over S, every finite locally free E (rank not assumed constant) and every i, with no further hypothesis. c\_i(E) is the degree-i part of totalChernOfFiniteLocallyFree C sX E, the total Chern class of Stacks 0ESW in the ring TotalChowClass C sX of total Chow cohomology classes, and E^dual is the dual sheaf Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf E = SheafHom(E, O\_X)”.

> **Stacks 0FA5**: for `ℰ` finite locally free on `X`, of arbitrary rank,
>
>   `c_i(ℰ^∨) = (-1)^i c_i(ℰ)`
>
> in `A^i(X)`, for every `i`, where `c_i(-)` is the degree-`i` part of the total Chern class of
> Stacks 0ESW, which on the locus where `ℰ` has rank `r` is the bivariant Chern class of
> Stacks 0B7H.

```lean
theorem homPart_totalChernOfFiniteLocallyFree_dualSheaf (E : X.Modules)
    [hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] (i : ℕ) :
    haveI := Stacks.AlgebraicGeometry.ReflexiveModules.isFiniteLocallyFree_dualSheaf E hE
    TotalChowClass.homComponent i (totalChernOfFiniteLocallyFree C sX (dualSheaf E)) =
      ((-1 : ℤ) ^ i) • TotalChowClass.homComponent i (totalChernOfFiniteLocallyFree C sX E)
```

## Tag 0FA6, a lemma

[Tag 0FA6](https://stacks.math.columbia.edu/tag/0FA6) in the Stacks Project.

**`Stacks.Chow.chernClass_tensorObj_one_chowCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesBivariant.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesBivariant.lean#L308). The attribute's comment: “first displayed identity: for X locally of finite type over the base and finite locally free E, F of ranks r and s, c\_1(E ⊗ F) = r c\_1(F) + s c\_1(E) in the Chow cohomology ring A^*(X) (Stacks 0B7E), c\_1 the bivariant Chern class of Stacks 0B7H and E ⊗ F the module Scheme.Modules.tensorObj E F of rank r*s (Stacks 02U9)”.

> **Stacks 0FA6, the first displayed identity.** Let `X` be locally of finite type over the base
> and `ℰ`, `ℱ` finite locally free `𝒪_X`-modules of ranks `r` and `s`. Then
>
>   `c₁(ℰ ⊗ ℱ) = r c₁(ℱ) + s c₁(ℰ)`
>
> in the Chow cohomology ring `A^*(X)` of Stacks 0B7E, `c₁` being the bivariant Chern class of
> Stacks 0B7H.

```lean
theorem chernClass_tensorObj_one_chowCohomology (E F : X.Modules) (r s : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F s] :
    chernClassChowCohomology C sX (Scheme.Modules.tensorObj E F) (r * s) 1
      = r • chernClassChowCohomology C sX F s 1 + s • chernClassChowCohomology C sX E r 1
```

**`Stacks.Chow.chernClass_tensorObj_two_chowCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesBivariant.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesBivariant.lean#L331). The attribute's comment: “second displayed identity: for X locally of finite type over the base and finite locally free E, F of ranks r and s, c\_2(E ⊗ F) = r c\_2(F) + s c\_2(E) + binom(r,2) c\_1(F)^2 + (rs - 1) c\_1(F) c\_1(E) + binom(s,2) c\_1(E)^2 in the Chow cohomology ring A^*(X) (Stacks 0B7E), with its multiplication, c\_i the bivariant Chern classes of Stacks 0B7H, rs - 1 taken in ℤ, and E ⊗ F the module Scheme.Modules.tensorObj E F”.

> **Stacks 0FA6, the second displayed identity.** Let `X` be locally of finite type over the
> base and `ℰ`, `ℱ` finite locally free `𝒪_X`-modules of ranks `r` and `s`. Then
>
>   `c₂(ℰ ⊗ ℱ) = r c₂(ℱ) + s c₂(ℰ) + C(r,2) c₁(ℱ)² + (rs − 1) c₁(ℱ) c₁(ℰ) + C(s,2) c₁(ℰ)²`
>
> in the Chow cohomology ring `A^*(X)` of Stacks 0B7E, `c_i` being the bivariant Chern classes of
> Stacks 0B7H and the products those of the ring `A^*(X)`.

```lean
theorem chernClass_tensorObj_two_chowCohomology (E F : X.Modules) (r s : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F s] :
    letI := chowCohomologyRingOfInvertible C sX
    chernClassChowCohomology C sX (Scheme.Modules.tensorObj E F) (r * s) 2
      = r • chernClassChowCohomology C sX F s 2 + s • chernClassChowCohomology C sX E r 2
        + r.choose 2 • chernClassChowCohomology C sX F s 1 ^ 2
        + ((r * s : ℤ) - 1) •
            (chernClassChowCohomology C sX F s 1 * chernClassChowCohomology C sX E r 1)
        + s.choose 2 • chernClassChowCohomology C sX E r 1 ^ 2
```

**`Stacks.Chow.chernClassSub_tensorObj_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesTotal.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesTotal.lean#L330). The attribute's comment: “the first displayed identity, with nothing assumed beyond the two ranks. CORRECTION OF FORM: the source states c\_1(E tensor F) = r c\_1(F) + s c\_1(E) in the bivariant ring A^*(X). Here the identity is stated in Stacks.Chow.chernSubring, the commutative ring generated by the Chern classes inside the ring of graded cap families, in which Stacks.Chow.chernClassSub C sX E r i is c\_i(E); it is the same identity read in that realisation, and both sides are elements of one commutative ring, so the coefficients r and s are ring elements and not scalar actions. The module on the left is the library's canonical tensor product AlgebraicGeometry.Scheme.Modules.tensorObj. The source's reduction to the filtered case is PERFORMED, not assumed: Stacks 02UL is Stacks.Chow.exists\_splittingMorphism\_unconditional, proved from the flag bundle of StacksFrontier.AlgebraicGeometry.Chow.SplittingPrinciple.FlagBundle; the Chern roots of the three modules on the bundle are Stacks.Chow.hasChernRoots\_of\_hasQuotients and Stacks.Chow.hasChernRoots\_tensorObj\_of\_hasQuotients, which get their filtrations from Stacks.Chow.exists\_hasQuotients\_of\_hasInvertibleFiltration; and the descent along the flat pullback, injective by clause (1) of Stacks 02UL, is Stacks.Chow.eq\_of\_intertwines, fed by Stacks 02U8 in the form Stacks.Chow.GenuineChern.intertwines\_chernFamily. The formal computation the source omits is proved in full, for every r and every s, as Stacks.Chow.esymmOfRoots\_lex\_one, via the bridge Stacks.Chow.esymmOfRoots\_eq\_esymRec from the unordered families of AlgebraicGeometry.HasChernRoots to the Pascal recursion Stacks.Chow.esymRec. Stacks 02TJ is not needed in degree one: Stacks.Chow.sum\_range\_lexFamily is proved for an arbitrary ring”.

> **Stacks 0FA6, the first displayed identity.** For `ℰ` and `ℱ` finite locally free of
> constant ranks `r` and `s`,
>
>   `c₁(ℰ ⊗_{𝒪_X} ℱ) = r·c₁(ℱ) + s·c₁(ℰ)`
>
> in the commutative ring `Stacks.Chow.chernSubring` generated by the Chern classes. Nothing is
> assumed beyond the two ranks: the source's reduction to a pair of filtrations with invertible
> quotients is performed, by the flag bundle of Stacks 02UL and the injectivity of the flat
> pullback it provides.

```lean
theorem chernClassSub_tensorObj_one (E F : X.Modules) (r s : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F s] :
    chernClassSub C sX (Scheme.Modules.tensorObj E F) (r * s) 1
      = (s : chernSubring C sX) * chernClassSub C sX E r 1
        + (r : chernSubring C sX) * chernClassSub C sX F s 1
```

**`Stacks.Chow.chernClassSub_tensorObj_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesTotal.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernClassesTotal.lean#L438). The attribute's comment: “the second displayed identity, with nothing assumed beyond the two ranks. CORRECTION OF FORM: the source states c\_2(E tensor F) = r c\_2(F) + s c\_2(E) + binom(r,2) c\_1(F)^2 + (r*s - 1) c\_1(F) c\_1(E) + binom(s,2) c\_1(E)^2 in the bivariant ring A^*(X). Here the identity is stated in Stacks.Chow.chernSubring, the commutative ring generated by the Chern classes inside the ring of graded cap families, in which Stacks.Chow.chernClassSub C sX E r i is c\_i(E); it is the same identity read in that realisation, and because that ring is commutative the two squares and the cross term are honest products of classes rather than composites of operations. The cross-term coefficient is r*s - 1, as in the source, and NOT r*s; the five summands appear in a different order from the source's, and addition is commutative. The module on the left is the library's canonical tensor product AlgebraicGeometry.Scheme.Modules.tensorObj. The source's reduction to the filtered case is PERFORMED, not assumed, by exactly the route recorded on Stacks.Chow.chernClassSub\_tensorObj\_one: the flag bundle of Stacks 02UL as Stacks.Chow.exists\_splittingMorphism\_unconditional, the Chern roots on the bundle as Stacks.Chow.hasChernRoots\_tensorObj\_of\_hasQuotients, and the descent along the injective flat pullback as Stacks.Chow.eq\_of\_intertwines fed by Stacks 02U8. Stacks 02TJ, the commutativity the degree-two collapse needs -- the cancellation turning the block-dependent coefficient s*(i+1) - 1 into the constant r*s - 1 -- comes from the ring Stacks.Chow.chernSubring being commutative, which is Stacks.Chow.isMulCommutative\_chernSubring, and is not an input here. The formal computation the source omits is proved in full, for every r and every s, as Stacks.Chow.esymmOfRoots\_lex\_two, which reads Stacks.Chow.esymRec\_two\_tensor through the bridge Stacks.Chow.esymmOfRoots\_eq\_esymRec”.

> **Stacks 0FA6, the second displayed identity.** For `ℰ` and `ℱ` finite locally free of
> constant ranks `r` and `s`,
>
>   `c₂(ℰ ⊗\_\{𝒪\_X} ℱ) = r·c₂(ℱ) + s·c₂(ℰ) + C(r,2)·c₁(ℱ)² + (r·s − 1)·c₁(ℰ)·c₁(ℱ)
>       + C(s,2)·c₁(ℰ)²`
>
> in the commutative ring `Stacks.Chow.chernSubring` generated by the Chern classes, the squares
> and the cross term being honest products there. The cross-term coefficient is `r·s − 1`. Nothing
> is assumed beyond the two ranks.

```lean
theorem chernClassSub_tensorObj_two (E F : X.Modules) (r s : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F s] :
    chernClassSub C sX (Scheme.Modules.tensorObj E F) (r * s) 2
      = (s : chernSubring C sX) * chernClassSub C sX E r 2
        + (r : chernSubring C sX) * chernClassSub C sX F s 2
        + (r.choose 2 : chernSubring C sX) * chernClassSub C sX F s 1 ^ 2
        + ((r : chernSubring C sX) * s - 1) *
            (chernClassSub C sX E r 1 * chernClassSub C sX F s 1)
        + (s.choose 2 : chernSubring C sX) * chernClassSub C sX E r 1 ^ 2
```

**`Stacks.Chow.totalChern_sheafTensor_degree_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernRelations.lean, line 728](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernRelations.lean#L728). The attribute's comment: “the first displayed identity, for every X locally of finite type over S and all finite locally free E and F of ranks r and s, with no further hypothesis. The identity is read in the ring TotalChowClass C sX of total Chow cohomology classes, the product over p of the A^p(X) of Stacks 0B7E with the product of Stacks 0B75; every term of the identity is homogeneous, so it lies in the source's A^*(X). c\_1(E) is the degree-one part TotalChowClass.homComponent 1 (totalChern C sX E r) of the total Chern class, the bivariant Chern class of Stacks 0B7H in degree one, and E tensor F is the sheaf tensor product Stacks.SheafOfModules.Tensor.sheafTensor, of rank r * s”.

> **Stacks 0FA6, the first displayed identity.** For `ℰ` and `ℱ` finite locally free of ranks
> `r` and `s` on `X` locally of finite type over `S`,
>
>   `c₁(ℰ ⊗ ℱ) = r·c₁(ℱ) + s·c₁(ℰ)`
>
> in the ring of total Chow cohomology classes of `X`, where `c₁(-)` is the degree-one part of the
> total Chern class, the first Chern class of Stacks 0B7H.

```lean
theorem totalChern_sheafTensor_degree_one :
    letI : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (R := X.ringCatSheaf) _ _ :=
        isFiniteLocallyFreeOfRank_tensor hE hF
    TotalChowClass.homComponent 1 (totalChern C sX (((sheafTensor X.sheaf).obj E).obj F) (r * s)) =
      (r : ℤ) • TotalChowClass.homComponent 1 (totalChern C sX F s) +
        (s : ℤ) • TotalChowClass.homComponent 1 (totalChern C sX E r)
```

**`Stacks.Chow.totalChern_sheafTensor_degree_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernRelations.lean, line 755](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorChernRelations.lean#L755). The attribute's comment: “the second displayed identity, for every X locally of finite type over S and all finite locally free E and F of ranks r and s, with no further hypothesis, the cross-term coefficient being r*s - 1 as in the source. The identity is read in the ring TotalChowClass C sX of total Chow cohomology classes, the product over p of the A^p(X) of Stacks 0B7E with the product of Stacks 0B75; every term of the identity is homogeneous, so it lies in the source's A^*(X). c\_i(E) is the degree-i part TotalChowClass.homComponent i (totalChern C sX E r) of the total Chern class, the bivariant Chern class of Stacks 0B7H in degree i, the squares and the product are products in that ring, and E tensor F is the sheaf tensor product Stacks.SheafOfModules.Tensor.sheafTensor, of rank r * s”.

> **Stacks 0FA6, the second displayed identity.** For `ℰ` and `ℱ` finite locally free of ranks
> `r` and `s` on `X` locally of finite type over `S`,
>
>   `c₂(ℰ ⊗ ℱ) = r·c₂(ℱ) + s·c₂(ℰ) + C(r,2)·c₁(ℱ)² + (r·s − 1)·c₁(ℱ)·c₁(ℰ) + C(s,2)·c₁(ℰ)²`
>
> in the ring of total Chow cohomology classes of `X`, where `c_i(-)` is the degree-`i` part of the
> total Chern class, the Chern class of Stacks 0B7H. The coefficient of the cross term is
> `r·s − 1`.

```lean
theorem totalChern_sheafTensor_degree_two :
    letI : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (R := X.ringCatSheaf) _ _ :=
        isFiniteLocallyFreeOfRank_tensor hE hF
    TotalChowClass.homComponent 2 (totalChern C sX (((sheafTensor X.sheaf).obj E).obj F) (r * s)) =
      (r : ℤ) • TotalChowClass.homComponent 2 (totalChern C sX F s) +
        (s : ℤ) • TotalChowClass.homComponent 2 (totalChern C sX E r) +
        (r.choose 2 : ℤ) • TotalChowClass.homComponent 1 (totalChern C sX F s) ^ 2 +
        ((r : ℤ) * s - 1) • (TotalChowClass.homComponent 1 (totalChern C sX F s) *
          TotalChowClass.homComponent 1 (totalChern C sX E r)) +
        (s.choose 2 : ℤ) • TotalChowClass.homComponent 1 (totalChern C sX E r) ^ 2
```

## Tag 0FA7, a remark

[Tag 0FA7](https://stacks.math.columbia.edu/tag/0FA7) in the Stacks Project.

**`Stacks.Chow.chernPolynomialClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean#L446). The attribute's comment: “the class P(E) = P(r(E), c\_1(E), c\_2(E), ...) for P in Z[r, c\_1, c\_2, ...] and E finite locally free of rank not necessarily constant, at the rank and Chern classes of Tag 0ESW; it lies in A^p(X) for P homogeneous of degree p by Stacks.Chow.chernPolynomialClass\_isHomogeneous”.

> **Stacks 0FA7, the class `P(ℰ)`.** For `ℰ` finite locally free on `X`, of rank not necessarily
> constant, and `P ∈ 𝐙[r, c₁, c₂, c₃, …]`,
>
>   `P(ℰ) = P(r(ℰ), c₁(ℰ), c₂(ℰ), c₃(ℰ), …)`,
>
> the evaluation of `P` at the rank `r(ℰ)` and the Chern classes `c_i(ℰ)` of Stacks 0ESW in the
> ring `∏_{q ≥ 0} A^q(X)` of total classes. These classes commute pairwise
> (`Stacks.Chow.commute_chernVariable`), so the evaluation is a ring homomorphism; for `P`
> homogeneous of degree `p` the class lies in `A^p(X)`
> (`Stacks.Chow.chernPolynomialClass_isHomogeneous`).

```lean
def chernPolynomialClass : ChernPolynomial →+* TotalChowClass C sX
```

**`Stacks.Chow.chernPolynomialClass_isHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean#L468). The attribute's comment: “P(E) lies in A^p(X) for P homogeneous of degree p in the graded ring Z[r, c\_1, c\_2, ...] (r of degree 0, c\_i of degree i), for every finite locally free E of rank not necessarily constant”.

> **Stacks 0FA7, `P(ℰ) ∈ A^p(X)`.** For `P ∈ 𝐙[r, c₁, c₂, …]` homogeneous of degree `p` for the
> grading in which `r` has degree `0` and `c_i` has degree `i`, the class `P(ℰ)` is homogeneous of
> degree `p`: all its components outside `A^p(X)` vanish.

```lean
theorem chernPolynomialClass_isHomogeneous {p : ℕ} {P : ChernPolynomial}
    (hP : P ∈ ChernPolynomial.homogeneousSubmodule p) :
    (chernPolynomialClass C sX E P).IsHomogeneous p
```

**`Stacks.Chow.res_chernPolynomialClass_of_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernPolynomial.lean#L519). The attribute's comment: “relations among the P(E) may be proved locally on X: along a morphism over which E has constant rank s, P(E) restricts to P(s, c\_1, c\_2, ...) of the pullback, at the Chern classes of Tag 0B7H”.

> **Stacks 0FA7, working locally on `X`.** Along a morphism `h : Y' ⟶ X` over which `h^*ℰ` has
> constant rank `s` — for instance the inclusion of a piece where the rank of `ℰ` is `s` — the class
> `P(ℰ)` restricts to `P` evaluated at the integer `s` and the Chern classes of Stacks 0B7H of the
> module `h^*ℰ` of rank `s`. Relations among the classes `P(ℰ)` may therefore be checked on the
> pieces of constant rank, as the remark says.

```lean
theorem res_chernPolynomialClass_of_rank {Y' : Scheme.{u}} {sY' : Y' ⟶ C.S}
    [LocallyOfFiniteType sY'] (h : Y' ⟶ X) [LocallyOfFiniteType h] (hs : h ≫ sX = sY') (s : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback h).obj E) s] (P : ChernPolynomial) :
    TotalChowClass.res h hs (chernPolynomialClass C sX E P) =
      chernPolynomialClassOfRank C sY' ((Scheme.Modules.pullback h).obj E) s P
```

**`Stacks.Chow.homComponent_totalChernClassOfModule_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean#L238). The attribute's comment: “the identity of Tag 0FA5 for modules of nonconstant rank: c\_i(E^dual) = (-1)^i c\_i(E), at the Chern classes of Tag 0ESW, read in the ring of total classes; the same identity in A^i(X) is Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree\_dualSheaf”.

> **Stacks 0FA5 in nonconstant rank, in the ring of total classes**: `c_i(ℰ^∨) = (-1)^i c_i(ℰ)`
> for the Chern classes of Stacks 0ESW. This is
> `Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree_dualSheaf`.

```lean
theorem homComponent_totalChernClassOfModule_dualSheaf (i : ℕ) :
    haveI := isFiniteLocallyFree_dualSheaf E hE
    TotalChowClass.homComponent i (totalChernClassOfModule C sX (dualSheaf E)) =
      ((-1 : ℤ) ^ i) • TotalChowClass.homComponent i (totalChernClassOfModule C sX E)
```

**`Stacks.Chow.chernClassOfLocallyFree_sheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean#L342). The attribute's comment: “the example c\_2(SheafHom(E, E)) = P(E) with P = 2 r c\_2 - (r - 1) c\_1^2, in A^2(X), for E finite locally free of rank not necessarily constant, at the Chern classes of Tag 0ESW”.

> **The example of Stacks 0FA7**: for `ℰ` finite locally free on `X`, of rank not necessarily
> constant,
>
>   `c₂(𝓗om(ℰ, ℰ)) = P(ℰ)`,  `P = 2 r c₂ - (r - 1) c₁²`,
>
> in `A^2(X)`, where `c₂` is the Chern class of Stacks 0ESW and `P(ℰ)` the class of Stacks 0FA7.
> The proof is the source's: `𝓗om(ℰ, ℰ) ≅ ℰ ⊗ ℰ^∨` (Stacks 0FNV), and Stacks 0FA5 and 0FA6 on the
> parts of `X` where the rank of `ℰ` is constant.

```lean
theorem chernClassOfLocallyFree_sheafHom :
    haveI := isFiniteLocallyFree_sheafHom E
    SectionZeroScheme.chernClassOfLocallyFree
        (Stacks.SheafOfModules.OnSpace.sheafHom X.toRingedSpace E E) C sX 2 =
      chernPolynomialComponent C sX E 2 sheafEndChernPolynomial
```

**`Stacks.Chow.chernClassOfLocallyFree_tensorObj_one_chowCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean#L437). The attribute's comment: “the first identity of Tag 0FA6 for modules of nonconstant rank, in the Chow cohomology ring A^*(X): c\_1(E tensor F) = r(E) c\_1(F) + r(F) c\_1(E), at the rank and Chern classes of Tag 0ESW”.

> **Stacks 0FA6, the first identity, in nonconstant rank, in `A^*(X)`** (Stacks 0FA7). For `ℰ`,
> `ℱ` finite locally free on `X`, of ranks not necessarily constant,
>
>   `c₁(ℰ ⊗ ℱ) = r(ℰ) c₁(ℱ) + r(ℱ) c₁(ℰ)`
>
> in the Chow cohomology ring `A^*(X)` of Stacks 0B7E, at the rank classes and Chern classes of
> Stacks 0ESW.

```lean
theorem chernClassOfLocallyFree_tensorObj_one_chowCohomology :
    letI := chowCohomologyRingOfInvertible C sX
    chernClassOfLocallyFreeChowCohomology C sX (Scheme.Modules.tensorObj E F) 1 =
      rankChowCohomology C sX E * chernClassOfLocallyFreeChowCohomology C sX F 1 +
        rankChowCohomology C sX F * chernClassOfLocallyFreeChowCohomology C sX E 1
```

**`Stacks.Chow.chernClassOfLocallyFree_tensorObj_two_chowCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/NonconstantRankRelations.lean#L468). The attribute's comment: “the second identity of Tag 0FA6 for modules of nonconstant rank, in the Chow cohomology ring A^*(X): c\_2(E tensor F) = r(E) c\_2(F) + r(F) c\_2(E) + binom(r(E),2) c\_1(F)^2 + (r(E) r(F) - 1) c\_1(F) c\_1(E) + binom(r(F),2) c\_1(E)^2, at the rank and Chern classes of Tag 0ESW, binom(r(E),2) being the class which is binom(r,2) where the rank is r”.

> **Stacks 0FA6, the second identity, in nonconstant rank, in `A^*(X)`** (Stacks 0FA7). For `ℰ`,
> `ℱ` finite locally free on `X`, of ranks not necessarily constant,
>
>   `c₂(ℰ ⊗ ℱ) = r(ℰ) c₂(ℱ) + r(ℱ) c₂(ℰ) + (r(ℰ) choose 2) c₁(ℱ)² + (r(ℰ) r(ℱ) - 1) c₁(ℱ) c₁(ℰ)
>     + (r(ℱ) choose 2) c₁(ℰ)²`
>
> in the Chow cohomology ring `A^*(X)` of Stacks 0B7E, at the rank classes and Chern classes of
> Stacks 0ESW, `(r(ℰ) choose 2)` being the class which is `(r choose 2)` where the rank is `r`.

```lean
theorem chernClassOfLocallyFree_tensorObj_two_chowCohomology :
    letI := chowCohomologyRingOfInvertible C sX
    chernClassOfLocallyFreeChowCohomology C sX (Scheme.Modules.tensorObj E F) 2 =
      rankChowCohomology C sX E * chernClassOfLocallyFreeChowCohomology C sX F 2 +
        rankChowCohomology C sX F * chernClassOfLocallyFreeChowCohomology C sX E 2 +
        rankChooseTwoChowCohomology C sX E * chernClassOfLocallyFreeChowCohomology C sX F 1 ^ 2 +
        (rankChowCohomology C sX E * rankChowCohomology C sX F - 1) *
          (chernClassOfLocallyFreeChowCohomology C sX F 1 *
            chernClassOfLocallyFreeChowCohomology C sX E 1) +
        rankChooseTwoChowCohomology C sX F *
          chernClassOfLocallyFreeChowCohomology C sX E 1 ^ 2
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.isFiniteLocallyFree_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/DualFiniteLocallyFree.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Modules/DualFiniteLocallyFree.lean#L92). The attribute's comment: “dual\_nonconstant\_rank”.

> **Stacks Project, Tag 0FA7, the clause on the dual.** The dual `ℰ^∨ = SheafHom(ℰ, 𝒪_X)` of a
> finite locally free module on a scheme is finite locally free. The rank of `ℰ` is not assumed
> constant.
>
> Every point has a neighbourhood `U` on which a local free presentation of `ℰ` trivialises it on
> a finite index set, and there `ℰ^∨` is free on the same index set by `freeIsoDualSheafOver`.

```lean
theorem isFiniteLocallyFree_dualSheaf {X : Scheme.{u}} (E : X.Modules)
    (hE : SheafOfModules.IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E) :
    SheafOfModules.IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) (dualSheaf E)
```

## Tag 0F9B, an example

[Tag 0F9B](https://stacks.math.columbia.edu/tag/0F9B) in the Stacks Project.

**`AlgebraicGeometry.degreeZeroPowerSum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ChernGrading.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/ChernGrading.lean#L69). The attribute's comment: “degree\_zero\_power\_sum”.

> The zeroth power-sum polynomial is the rank variable `r`.

```lean
noncomputable abbrev degreeZeroPowerSum : ChernPolynomial
```

**`AlgebraicGeometry.coe_powerSumPolynomial_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean#L38). The attribute's comment: “first\_four\_power\_sums”.

> The first power-sum polynomial is `c₁`.

```lean
theorem coe_powerSumPolynomial_one :
    (powerSumPolynomial 1 : MvPolynomial ℕ+ ℤ) = X (1 : ℕ+)
```

**`AlgebraicGeometry.coe_powerSumPolynomial_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean#L44). The attribute's comment: “first\_four\_power\_sums”.

> The second power-sum polynomial is `c₁² - 2c₂`.

```lean
theorem coe_powerSumPolynomial_two :
    (powerSumPolynomial 2 : MvPolynomial ℕ+ ℤ) =
      X (1 : ℕ+) ^ 2 - 2 * X (2 : ℕ+)
```

**`AlgebraicGeometry.coe_powerSumPolynomial_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean#L52). The attribute's comment: “first\_four\_power\_sums”.

> The third power-sum polynomial is `c₁³ - 3c₁c₂ + 3c₃`.

```lean
theorem coe_powerSumPolynomial_three :
    (powerSumPolynomial 3 : MvPolynomial ℕ+ ℤ) =
      X (1 : ℕ+) ^ 3 - 3 * X (1 : ℕ+) * X (2 : ℕ+) + 3 * X (3 : ℕ+)
```

**`AlgebraicGeometry.coe_powerSumPolynomial_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/FirstFourPowerSums.lean#L60). The attribute's comment: “first\_four\_power\_sums”.

> The fourth power-sum polynomial is `c₁⁴ - 4c₁²c₂ + 4c₁c₃ + 2c₂² - 4c₄`.

```lean
theorem coe_powerSumPolynomial_four :
    (powerSumPolynomial 4 : MvPolynomial ℕ+ ℤ) =
      X (1 : ℕ+) ^ 4 - 4 * X (1 : ℕ+) ^ 2 * X (2 : ℕ+) +
        4 * X (1 : ℕ+) * X (3 : ℕ+) + 2 * X (2 : ℕ+) ^ 2 - 4 * X (4 : ℕ+)
```

**`AlgebraicGeometry.log_one_add_universalChernClassSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/LogarithmicIdentity.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/LogarithmicIdentity.lean#L592). The attribute's comment: “logarithmic\_identity”.

> In the completed rational graded ring, the logarithm of the universal total Chern class
> is the signed generating series of the universal power-sum polynomials.

```lean
public theorem log_one_add_universalChernClassSum :
    PowerSeries.subst universalChernClassSum (PowerSeries.log ℚ) = powerSumSeries
```

**`AlgebraicGeometry.eq_powerSumPolynomial_iff_eval_esymm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCharacterization.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCharacterization.lean#L127). The attribute's comment: “power\_sum\_characterization”.

> A weighted-homogeneous integral polynomial of positive degree `p` is the universal
> power-sum polynomial precisely when substituting elementary symmetric polynomials in any
> `n ≥ p` variables gives the sum of their `p`th powers.

```lean
public theorem eq_powerSumPolynomial_iff_eval_esymm
    (p : ℕ) (hp : 1 ≤ p)
    (Q : weightedHomogeneousSubmodule ℤ (fun i : ℕ+ => (i : ℕ)) p) :
    Q = powerSumPolynomial p ↔
      ∀ n : ℕ, p ≤ n →
        eval₂Hom C (fun i : ℕ+ => esymm (Fin n) ℤ (i : ℕ))
            (Q : MvPolynomial ℕ+ ℤ) =
          psum (Fin n) ℤ p
```

**`AlgebraicGeometry.powerSumPolynomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumPolynomials.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumPolynomials.lean#L58). The attribute's comment: “power\_sum\_polynomials”.

> The universal power-sum polynomial `Pₚ` in the Chern-class variables `cᵢ`.
>
> The variable indexed by `i : ℕ+` has weight `i`. Thus the value is packaged as a
> weighted-homogeneous polynomial of degree `p`. For `p + 1`, the displayed recursion is
> Newton's formula
> `Pₚ₊₁ = ∑ᵢ₌₁ᵖ (-1)ⁱ⁻¹ cᵢ Pₚ₊₁₋ᵢ + (-1)ᵖ (p + 1) cₚ₊₁`.

```lean
noncomputable def powerSumPolynomial (p : ℕ) :
    weightedHomogeneousSubmodule ℤ (fun i : ℕ+ => (i : ℕ)) p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.43, Tag 02UK](https://stacks.math.columbia.edu/tag/02UK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
