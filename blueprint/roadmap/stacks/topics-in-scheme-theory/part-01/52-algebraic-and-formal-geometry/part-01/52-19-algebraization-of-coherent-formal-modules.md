---
declaration: section
origin: cited
lean: Stacks.Algebraization.SatisfiesDepthInequalities, Stacks.Algebraization.SatisfiesStrictDepthInequalities, Stacks.Algebraization.satisfiesDepthInequalities_of_annihilated, Stacks.Algebraization.satisfiesStrictDepthInequalities_of_succ, Stacks.Algebraization.satisfiesDepthInequalities_iff_bootstrapSituation, Stacks.Algebraization.satisfiesDepthInequalities_of_strict, Stacks.Algebraization.satisfiesDepthInequalities_elementary_properties, Stacks.Algebraization.satisfiesDepthInequalities_two_three_iff
statement: formalized
proof: formalized
---

# 52.19 Algebraization of coherent formal modules, III

Section 52.19 of the Stacks Project, [Tag 0EJ2](https://stacks.math.columbia.edu/tag/0EJ2). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EJ3, a definition

[Tag 0EJ3](https://stacks.math.columbia.edu/tag/0EJ3) in the Stacks Project.

**`Stacks.Algebraization.SatisfiesDepthInequalities`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalities.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalities.lean#L149). The attribute's comment: “the (a, b)-inequalities”.

> **Stacks Project, Tag 0EJ3.** A coherent `I`-adic system on `U` satisfies the
> `(a, b)`-inequalities when, at every point of `U ∩ Y` and every prime `𝔭` of the completed local
> ring not containing `I𝒪_{X,y}^∧`, the depth of the formal stalk at `𝔭` obeys the bound `a`
> strictly if `V(𝔭) ∩ V(I𝒪_{X,y}^∧) = {𝔪_y^∧}`, and in the remaining case obeys `a` weakly or
> else the bound `b` strictly after adding `dim(𝒪_{X,y}^∧/𝔭)`.

```lean
public abbrev SatisfiesDepthInequalities (a b : ℤ) : Prop
```

**`Stacks.Algebraization.SatisfiesStrictDepthInequalities`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalities.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalities.lean#L166). The attribute's comment: “the strict (a, b)-inequalities”.

> **Stacks Project, Tag 0EJ3.** A coherent `I`-adic system on `U` satisfies the strict
> `(a, b)`-inequalities when, at every point of `U ∩ Y` and every prime `𝔭` of the completed local
> ring not containing `I𝒪_{X,y}^∧`, the depth of the formal stalk at `𝔭` exceeds the bound `a`,
> or else exceeds the bound `b` after adding `dim(𝒪_{X,y}^∧/𝔭)`.

```lean
public abbrev SatisfiesStrictDepthInequalities (a b : ℤ) : Prop
```

## Tag 0EJ4, a lemma

[Tag 0EJ4](https://stacks.math.columbia.edu/tag/0EJ4) in the Stacks Project.

**`Stacks.Algebraization.satisfiesDepthInequalities_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean#L688). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0EJ4 (1).** A coherent `I`-adic system on `U` annihilated by a fixed
> power of `I` satisfies the `(a, b)`-inequalities for every pair of bounds, since every formal
> stalk then localizes to zero at a prime outside the adic locus and so has infinite depth.

```lean
public theorem satisfiesDepthInequalities_of_annihilated
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hF : ∃ c : ℕ, ∀ n : ℕ,
      _root_.Stacks.AlgebraicGeometry.IdealPower.idealPowerMultiple (idealOnOpen S) c
        (F.obj.obj (op n)) = ⊥)
    (a b : ℤ) :
    SatisfiesDepthInequalities S F a b
```

**`Stacks.Algebraization.satisfiesStrictDepthInequalities_of_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean#L748). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0EJ4 (2).** A coherent `I`-adic system on `U` satisfying the
> `(a + 1, b)`-inequalities satisfies the strict `(a, b)`-inequalities: in the case distinguished
> by the adic closed fibre the weak bound `a + 1` already beats `a` strictly.

```lean
public theorem satisfiesStrictDepthInequalities_of_succ
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (a b : ℤ)
    (hF : SatisfiesDepthInequalities S F (a + 1) b) :
    SatisfiesStrictDepthInequalities S F a b
```

**`Stacks.Algebraization.satisfiesDepthInequalities_iff_bootstrapSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean, line 1028](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean#L1028). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0EJ4 (3).** If `cd(A, I) ≤ d` and `A` has a dualizing complex, then a
> coherent `I`-adic system on `U` satisfies the `(s, s + d)`-inequalities exactly when, at every
> point `y` of `U ∩ Y` with `δ^Y_Z(y)` finite, the completed local ring, the ideal `I𝒪_{X,y}^∧`,
> the singleton `{𝔪_y^∧}`, the formal stalk `ℱ_y^∧` and the bounds `s - δ^Y_Z(y)` and `d` form a
> bootstrap situation.

```lean
public theorem satisfiesDepthInequalities_iff_bootstrapSituation
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (s d : ℤ)
    (hcd : _root_.Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (Ideal.fg_of_isNoetherianRing S.I) ≤ d)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{max u v} S.A),
      Dualizing.IsDualizingComplex K) :
    SatisfiesDepthInequalities S F s (s + d) ↔
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        S.distanceToZ z ≠ ⊤ →
        ∃ B : BootstrapSituation.{u, u, v},
          B.A = completedLocalRing (idealOnOpen S) y ∧
          HEq B.commRing
            (inferInstance : CommRing (completedLocalRing (idealOnOpen S) y)) ∧
          HEq B.I (completedLocalIdeal (idealOnOpen S) y) ∧
          B.M = completedStalk (idealOnOpen S) F y ∧
          HEq B.addCommGroup
            (inferInstance : AddCommGroup (completedStalk (idealOnOpen S) F y)) ∧
          HEq B.module (inferInstance : Module (completedLocalRing (idealOnOpen S) y)
            (completedStalk (idealOnOpen S) F y)) ∧
          HEq B.T {q : PrimeSpectrum (completedLocalRing (idealOnOpen S) y) |
            q.asIdeal = completedMaximalIdeal (idealOnOpen S) y} ∧
          B.s = s - ((S.distanceToZ z).toNat : ℤ) ∧ B.d = d
```

**`Stacks.Algebraization.satisfiesDepthInequalities_of_strict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean, line 1283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean#L1283). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 0EJ4 (4).** If `cd(A, I) ≤ d` and `A` has a dualizing complex, then
> the strict `(s, s + d)`-inequalities imply the ordinary `(s, s + d)`-inequalities: in the case
> distinguished by the adic closed fibre the prime is isolated in the adic locus, so
> `dim(𝒪_{X,y}^∧/𝔭) ≤ cd(𝒪_{X,y}^∧, I𝒪_{X,y}^∧) ≤ d` and the bound `s + d` on the sum implies
> the bound `s` on the depth alone. The isolated-prime bound used for this is
> `Stacks.LocalCohomology.ringKrullDim_quotient_le_cohomologicalDimension'`, which discharges the
> local case of Stacks 0BFR on the completion of `𝒪_{X,y}^∧/𝔭` itself rather than taking it as a
> hypothesis.

```lean
public theorem satisfiesDepthInequalities_of_strict
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (s d : ℤ)
    (hcd : _root_.Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (Ideal.fg_of_isNoetherianRing S.I) ≤ d)
    (_hdual : ∃ K : DerivedCategory (ModuleCat.{max u v} S.A),
      Dualizing.IsDualizingComplex K)
    (hF : SatisfiesStrictDepthInequalities S F s (s + d)) :
    SatisfiesDepthInequalities S F s (s + d)
```

**`Stacks.Algebraization.satisfiesDepthInequalities_elementary_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean, line 1411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesBootstrap.lean#L1411).

> **Stacks Project, Tag 0EJ4.** The four elementary properties of the depth–distance
> inequalities, as one statement about a coherent `I`-adic system `(ℱₙ)` on `U` in an
> algebraization situation.
>
> 1. If `(ℱₙ)` is annihilated by a power of `I`, it satisfies the `(a, b)`-inequalities for every
>    pair of bounds.
> 2. If `(ℱₙ)` satisfies the `(a + 1, b)`-inequalities, it satisfies the strict
>    `(a, b)`-inequalities.
>
> If moreover `cd(A, I) ≤ d` and `A` has a dualizing complex, then
>
> 3. `(ℱₙ)` satisfies the `(s, s + d)`-inequalities exactly when, at every point `y` of `U ∩ Y`
>    with `δ^Y_Z(y)` finite, the completed local ring, the ideal `I𝒪_{X,y}^∧`, the singleton
>    `{𝔪_y^∧}`, the formal stalk `ℱ_y^∧` and the bounds `s - δ^Y_Z(y)` and `d` form a bootstrap
>    situation, and
> 4. the strict `(s, s + d)`-inequalities imply the ordinary `(s, s + d)`-inequalities.
>
> Parts (1) and (2) are stated here under no hypothesis beyond the situation itself, exactly as
> the source states them; the hypotheses `cd(A, I) ≤ d` and the existence of a dualizing complex
> are carried only by parts (3) and (4), which is where the source introduces them. The four
> parts are `Stacks.Algebraization.satisfiesDepthInequalities_of_annihilated`,
> `Stacks.Algebraization.satisfiesStrictDepthInequalities_of_succ`,
> `Stacks.Algebraization.satisfiesDepthInequalities_iff_bootstrapSituation` and
> `Stacks.Algebraization.satisfiesDepthInequalities_of_strict`.

```lean
public theorem satisfiesDepthInequalities_elementary_properties
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) :
    ((∃ c : ℕ, ∀ n : ℕ,
        _root_.Stacks.AlgebraicGeometry.IdealPower.idealPowerMultiple (idealOnOpen S) c
          (F.obj.obj (op n)) = ⊥) →
      ∀ a b : ℤ, SatisfiesDepthInequalities S F a b) ∧
    (∀ a b : ℤ, SatisfiesDepthInequalities S F (a + 1) b →
      SatisfiesStrictDepthInequalities S F a b) ∧
    (∀ s d : ℤ,
      _root_.Stacks.LocalCohomology.cohomologicalDimension S.A S.I
          (Ideal.fg_of_isNoetherianRing S.I) ≤ d →
      (∃ K : DerivedCategory (ModuleCat.{max u v} S.A), Dualizing.IsDualizingComplex K) →
      (SatisfiesDepthInequalities S F s (s + d) ↔
          ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
            S.distanceToZ z ≠ ⊤ →
            ∃ B : BootstrapSituation.{u, u, v},
              B.A = completedLocalRing (idealOnOpen S) y ∧
              HEq B.commRing
                (inferInstance : CommRing (completedLocalRing (idealOnOpen S) y)) ∧
              HEq B.I (completedLocalIdeal (idealOnOpen S) y) ∧
              B.M = completedStalk (idealOnOpen S) F y ∧
              HEq B.addCommGroup
                (inferInstance : AddCommGroup (completedStalk (idealOnOpen S) F y)) ∧
              HEq B.module (inferInstance : Module (completedLocalRing (idealOnOpen S) y)
                (completedStalk (idealOnOpen S) F y)) ∧
              HEq B.T {q : PrimeSpectrum (completedLocalRing (idealOnOpen S) y) |
                q.asIdeal = completedMaximalIdeal (idealOnOpen S) y} ∧
              B.s = s - ((S.distanceToZ z).toNat : ℤ) ∧ B.d = d) ∧
        (SatisfiesStrictDepthInequalities S F s (s + d) →
          SatisfiesDepthInequalities S F s (s + d)))
```

## Tag 0EKW, a lemma

[Tag 0EKW](https://stacks.math.columbia.edu/tag/0EKW) in the Stacks Project.

**`Stacks.Algebraization.satisfiesDepthInequalities_two_three_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesCohomologicalDimensionOne.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesCohomologicalDimensionOne.lean#L423).

> In Situation 0EHC let `(ℱ_n)` be an object of
> `Coh(U, I𝒪_U)`. If `cd(A, I) = 1`, then `(ℱ_n)` satisfies the `(2, 3)`-inequalities if and only
> if `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) + δ^Y_Z(y) > 3` for all `y ∈ U ∩ Y` and all primes
> `𝔭 ⊆ 𝒪_{X,y}^∧` with `𝔭 ∉ V(I𝒪_{X,y}^∧)`.

```lean
public theorem satisfiesDepthInequalities_two_three_iff (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1) :
    SatisfiesDepthInequalities S F 2 3 ↔
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          depthAddDimAddDistance S F y z p > ((3 : ℤ) : EInt)
```

## Tag 0EJ5, a lemma

[Tag 0EJ5](https://stacks.math.columbia.edu/tag/0EJ5) in the Stacks Project.

**`Stacks.Algebraization.one_le_depth_stalk_of_mixed_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthMixedComponents.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthMixedComponents.lean#L136).

> **Stacks Project, Tag 0EJ5.** Let `A` be a Noetherian ring with ideals `I ⊆ 𝔞`, write
> `X = Spec(A)`, `Y = V(I)`, `Z = V(𝔞)`, `U = X ∖ Z`, and suppose `A` is `I`-adically complete,
> has a dualizing complex, and has `cd(A, I) ≤ d` with `d ≥ 1`. Let `ℱ` be a coherent
> `𝒪_U`-module whose completion along `I𝒪_U` satisfies the strict `(1, 1 + d)`-inequalities of
> [Stacks, Tag 0EJ3]. Let `x ∈ U` be a point such that the closed fibre
> `\overline{\{x\}} ∩ Y` has an irreducible component contained in `Z` and an irreducible
> component not contained in `Z`. Then
>
>   `depth_{𝒪_{U,x}}(ℱ_x) ≥ 1`.
>
> The source states this for `x ∈ X`; a point of `Z` never satisfies the hypothesis, its closure
> lying in `Z`, and `ℱ_x` is defined only on `U`, so `x` ranges over `U`.
>
> The components on both sides disconnect the closed fibre once their intersection is removed, so
> [Stacks, Tag 0EG5] produces a point `z` of the closed fibre inside `Z` with
> `dim(𝒪_{\overline{\{x\}}, z}) ≤ d + 1`; [Stacks, Tag 02IM] produces an immediate generalization
> `r` of `z` still in the closed fibre but outside `Z`, whose distance to `Z` is therefore exactly
> `1` and whose local dimension is at most `d`. At the point `y ∈ U` that `r` determines the
> strict inequalities, evaluated at a prime of `𝒪_{U,y}^∧` minimal over the extension of the prime
> of `x`, force `depth((ℱ_y^∧)_𝔭) ≥ 1`; and that depth is `depth(ℱ_x)`, by [Stacks, Tag 0338] and
> [Stacks, Tag 0EHW].

```lean
public theorem one_le_depth_stalk_of_mixed_irreducibleComponents
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf)
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      S.I.fg_of_isNoetherianRing ≤ d)
    (hstrict : SatisfiesStrictDepthInequalities S
      ((completionFunctor S.U.toScheme (idealOnOpen S)).obj F) 1 (1 + d))
    (x : S.U.toScheme)
    (hmixed :
      let W : Set S.Y := S.Yι.base ⁻¹' closure ({S.U.ι.base x} : Set S.X)
      let Z : Set W := {y | S.Yι.base y.1 ∈ Set.range S.Zι.base}
      (∃ C : Set W, C ∈ irreducibleComponents W ∧ C ⊆ Z) ∧
        (∃ C : Set W, C ∈ irreducibleComponents W ∧ ¬ C ⊆ Z)) :
    1 ≤ Module.depth (S.U.toScheme.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (S.U.toScheme.presheaf.stalk x))
      ((stalkModuleFunctor x).obj F.obj)
```

## Tag 0EJ6, a lemma

[Tag 0EJ6](https://stacks.math.columbia.edu/tag/0EJ6) in the Stacks Project.

**`Stacks.Algebraization.isIso_globalToFormalSections_of_satisfiesStrictDepthInequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthRecoverSections.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthRecoverSections.lean#L431). The attribute's comment: “H^0(U,F) = lim H^0(U,F/I^nF) under the strict (1,1+d)-inequalities and depth two off the formal locus”.

> **Stacks Project, Tag 0EJ6.** Let `A` be a Noetherian ring with ideals `I ⊆ 𝔞`, write
> `X = Spec(A)`, `Y = V(I)`, `Z = V(𝔞)`, `U = X ∖ Z`, and let `ℱ` be a coherent `𝒪_U`-module and
> `d ≥ 1`. Assume
>
> 1. `A` is `I`-adically complete, has a dualizing complex, and `cd(A, I) ≤ d`,
> 2. the completion `ℱ^∧` of `ℱ` along `I𝒪_U` satisfies the strict `(1, 1 + d)`-inequalities of
>    [Stacks, Tag 0EJ3], and
> 3. `depth(ℱ_x) ≥ 2` for every `x ∈ U` with `\overline{\{x\}} ∩ Y ⊆ Z`.
>
> Then
>
>   `H⁰(U, ℱ) ⟶ lim H⁰(U, ℱ/Iⁿℱ)`
>
> is an isomorphism. That arrow is
> `Stacks.Algebraization.FormalSectionsII.globalToFormalSections`, whose `n`-th component is
> reduction modulo `Iⁿ` by
> `Stacks.Algebraization.FormalSectionsII.globalToFormalSections_proj`.
>
> [Stacks, Tag 0EIG] supplies the conclusion from conditions (1), (3) and its own condition (2),
> the dimension bound at the associated points of `ℱ`; that bound is
> `Stacks.Algebraization.associatedPointsClosureDimensionBound_of_satisfiesStrictDepthInequalities`,
> which is where condition (2) here and [Stacks, Tag 0EJ5] are consumed.

```lean
public theorem isIso_globalToFormalSections_of_satisfiesStrictDepthInequalities
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf)
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : cohomologicalDimension S.A S.I S.I.fg_of_isNoetherianRing ≤ d)
    (hstrict : SatisfiesStrictDepthInequalities S
      ((completionFunctor S.U.toScheme (idealOnOpen S)).obj F) 1 (1 + d))
    (hdepth : FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a F.obj) :
    IsIso (FormalSectionsII.globalToFormalSections S.A S.I S.a F.obj)
```

## Tag 0EJ7, a lemma

[Tag 0EJ7](https://stacks.math.columbia.edu/tag/0EJ7) in the Stacks Project.

**`Stacks.Algebraization.completionFunctor_map_bijective_of_satisfiesStrictDepthInequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthFullyFaithful.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/StrictDepthFullyFaithful.lean#L336). The attribute's comment: “Hom_U(G,F) = Hom_{Coh(U,IO_U)}(G^∧,F^∧) for every coherent G, under the strict (1,1+d)-inequalities and depth two off the formal locus; 0EJ6 applied to F itself”.

> **Stacks Project, Tag 0EJ7.** Let `A` be a Noetherian ring with ideals `I ⊆ 𝔞`, write
> `X = Spec(A)`, `Y = V(I)`, `Z = V(𝔞)`, `U = X ∖ Z`, and let `ℱ` be a coherent `𝒪_U`-module and
> `d ≥ 1`. Assume
>
> 1. `A` is `I`-adically complete, has a dualizing complex, and `cd(A, I) ≤ d`,
> 2. the completion `ℱ^∧` of `ℱ` along `I𝒪_U` satisfies the strict `(1, 1 + d)`-inequalities of
>    [Stacks, Tag 0EJ3], and
> 3. `depth(ℱ_x) ≥ 2` for every `x ∈ U` with `\overline{\{x\}} ∩ Y ⊆ Z`.
>
> Then
>
>   `Hom_U(𝒢, ℱ) ⟶ Hom_{Coh(U, I𝒪_U)}(𝒢^∧, ℱ^∧)`
>
> is bijective for every coherent `𝒪_U`-module `𝒢`. The map is the action on morphisms of the
> completion functor `Stacks.Algebraization.completionFunctor` of [Stacks, Tag 0880].
>
> The hypotheses are those of [Stacks, Tag 0EJ6] —
> `Stacks.Algebraization.isIso_globalToFormalSections_of_satisfiesStrictDepthInequalities` — and
> that lemma is what is applied: it gives the theorem on formal functions in degree zero for `ℱ`,
> which already forces the conclusion for every coherent `𝒢` by
> `Stacks.Algebraization.completionFunctor_map_bijective_of_isIso_globalToFormalSections`. The
> source instead applies [Stacks, Tag 0EJ6] to `SheafHom(𝒢, ℱ)`, after a transport of conditions
> (2) and (3) to that module whose details it omits; no such transport is needed here.

```lean
public theorem completionFunctor_map_bijective_of_satisfiesStrictDepthInequalities
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf)
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : cohomologicalDimension S.A S.I S.I.fg_of_isNoetherianRing ≤ d)
    (hstrict : SatisfiesStrictDepthInequalities S
      ((completionFunctor S.U.toScheme (idealOnOpen S)).obj F) 1 (1 + d))
    (hdepth : FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a F.obj)
    (G : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf) :
    Function.Bijective ((completionFunctor S.U.toScheme (idealOnOpen S)).map :
      (G ⟶ F) →
        ((completionFunctor S.U.toScheme (idealOnOpen S)).obj G ⟶
          (completionFunctor S.U.toScheme (idealOnOpen S)).obj F))
```

## Tag 0EJ8, a lemma

[Tag 0EJ8](https://stacks.math.columbia.edu/tag/0EJ8) in the Stacks Project.

**`Stacks.Algebraization.existsUnique_completionCompatibleIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean#L161). The attribute's comment: “the uniqueness half: two depth-two algebraizations are isomorphic by a unique isomorphism compatible with the identifications of completions”.

> **The uniqueness half of [Stacks, Tag 0EJ8].** In an algebraization situation, let `(ℱ_n)` be a
> coherent `I𝒪_U`-adic system and let `d ≥ 1`. Assume
>
> 1. `A` is `I`-adically complete, has a dualizing complex, and `cd(A, I) ≤ d`,
> 2. `(ℱ_n)` satisfies the strict `(1, 1 + d)`-inequalities of [Stacks, Tag 0EJ3].
>
> Let `𝒢` and `ℋ` be coherent `𝒪_U`-modules with `depth(𝒢_x) ≥ 2` and `depth(ℋ_x) ≥ 2` for every
> `x ∈ U` with `closure {x} ∩ Y ⊆ Z`, and let `φ : 𝒢^∧ ≅ (ℱ_n)` and `ψ : ℋ^∧ ≅ (ℱ_n)`. Then there
> is a unique isomorphism `e : 𝒢 ≅ ℋ` with `e^∧ ≫ ψ = φ`.
>
> Together with the existence half this is the uniqueness of the algebraization asserted by the
> source: condition (2) of the source, that `(ℱ_n)` be the completion of a coherent module, is
> witnessed by `φ` (or by `ψ`).

```lean
public theorem existsUnique_completionCompatibleIso
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : cohomologicalDimension S.A S.I S.I.fg_of_isNoetherianRing ≤ d)
    (hstrict : SatisfiesStrictDepthInequalities S F 1 (1 + d))
    (G H : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf)
    (hG : FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a G.obj)
    (hH : FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a H.obj)
    (φ : (completionFunctor S.U.toScheme (idealOnOpen S)).obj G ≅ F)
    (ψ : (completionFunctor S.U.toScheme (idealOnOpen S)).obj H ≅ F) :
    ∃! e : G ≅ H,
      (completionFunctor S.U.toScheme (idealOnOpen S)).map e.hom ≫ ψ.hom = φ.hom
```

**`Stacks.Algebraization.exists_completionIso_depthTwoOffFormalLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean#L239). The attribute's comment: “the existence half: a depth-two algebraization exists”.

> **The existence half of [Stacks, Tag 0EJ8].** In an algebraization situation, let `(ℱ_n)` be a
> coherent `I𝒪_U`-adic system and let `d ≥ 1`. Assume
>
> 1. `A` is `I`-adically complete, has a dualizing complex, and `cd(A, I) ≤ d`,
> 2. `(ℱ_n)` is the completion of some coherent `𝒪_U`-module,
> 3. `(ℱ_n)` satisfies the strict `(1, 1 + d)`-inequalities of [Stacks, Tag 0EJ3].
>
> Then `(ℱ_n)` is the completion of a coherent `𝒪_U`-module `ℋ` with `depth(ℋ_x) ≥ 2` at every
> `x ∈ U` whose closure meets `Y` only inside `Z`.
>
> These are the source's three conditions: condition (2) is the hypothesis `halg`, which is the
> source's "`(ℱ_n)` is the completion of a coherent module", and the depth-two conclusion is
> `Stacks.Algebraization.FormalSectionsII.DepthTwoOffFormalLocus`, the transcription of the
> source's condition (3) already used by [Stacks, Tag 0EJ7] and by the uniqueness half.
>
> The proof is the source's: the depth-two locus `T = {x ∈ U : \overline{\{x\}} ∩ Y ⊆ Z}` is
> stable under specialization, the depth bound
> `Stacks.Algebraization.one_le_depth_stalk_of_isImmediateSpecialization_notMem_depthTwoLocus` is
> the source's second paragraph, and the existence half of [Stacks, Tag 0EI3] then extends the
> given algebraization `𝒢` to a coherent `ℋ` of depth at least two along `T`, by a morphism which
> is an isomorphism on the stalks off `T`. Since `T` misses the support of `I𝒪_U`, that morphism
> has an isomorphism for its completion
> (`Stacks.Algebraization.isIso_completionFunctor_map_of_isIso_stalkMap_on_support`), so `ℋ` is
> again an algebraization of `(ℱ_n)`.

```lean
public theorem exists_completionIso_depthTwoOffFormalLocus
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : cohomologicalDimension S.A S.I S.I.fg_of_isNoetherianRing ≤ d)
    (hstrict : SatisfiesStrictDepthInequalities S F 1 (1 + d))
    (halg : ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf,
      Nonempty ((completionFunctor S.U.toScheme (idealOnOpen S)).obj G ≅ F)) :
    ∃ H : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf,
      Nonempty ((completionFunctor S.U.toScheme (idealOnOpen S)).obj H ≅ F) ∧
        FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a H.obj
```

**`Stacks.Algebraization.existsUnique_depthTwoAlgebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/UniqueDepthTwoAlgebraization.lean#L298). The attribute's comment: “existence and uniqueness, up to unique isomorphism compatible with the identifications of completions, of the depth-two algebraization”.

> **Stacks Project, Tag 0EJ8.** In an algebraization situation, let `(ℱ_n)` be a coherent
> `I𝒪_U`-adic system, an object of `Coh(U, I𝒪_U)`, and let `d ≥ 1`. Assume
>
> 1. `A` is `I`-adically complete, has a dualizing complex, and `cd(A, I) ≤ d`,
> 2. `(ℱ_n)` is the completion of a coherent `𝒪_U`-module,
> 3. `(ℱ_n)` satisfies the strict `(1, 1 + d)`-inequalities of [Stacks, Tag 0EJ3].
>
> Then there exists a unique coherent `𝒪_U`-module `ℋ` whose completion is `(ℱ_n)` such that
> `depth(ℋ_x) ≥ 2` for every `x ∈ U` with `\overline{\{x\}} ∩ Y ⊆ Z`.
>
> "Unique" is read in the only sense in which a module "whose completion is `(ℱ_n)`" can be
> unique: the module comes with an isomorphism `ψ : ℋ^∧ ≅ (ℱ_n)`, and any other coherent `𝒢` of
> depth at least two off the formal locus, with any `φ : 𝒢^∧ ≅ (ℱ_n)`, is isomorphic to `ℋ` by a
> *unique* isomorphism `e : 𝒢 ≅ ℋ` with `e^∧ ≫ ψ = φ`.
>
> The existence is `Stacks.Algebraization.exists_completionIso_depthTwoOffFormalLocus` (the
> source's construction through [Stacks, Tag 0EI3]) and the uniqueness is
> `Stacks.Algebraization.existsUnique_completionCompatibleIso` (the source's appeal to the mapping
> property of [Stacks, Tag 0EJ7]).

```lean
public theorem existsUnique_depthTwoAlgebraization
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (d : ℤ) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K)
    (hcd : cohomologicalDimension S.A S.I S.I.fg_of_isNoetherianRing ≤ d)
    (halg : ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf,
      Nonempty ((completionFunctor S.U.toScheme (idealOnOpen S)).obj G ≅ F))
    (hstrict : SatisfiesStrictDepthInequalities S F 1 (1 + d)) :
    ∃ (H : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf)
      (ψ : (completionFunctor S.U.toScheme (idealOnOpen S)).obj H ≅ F),
      FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a H.obj ∧
      ∀ (G : AlgebraicGeometry.SheafOfModules.CoherentModules S.U.toScheme.ringCatSheaf),
        FormalSectionsII.DepthTwoOffFormalLocus S.A S.I S.a G.obj →
        ∀ φ : (completionFunctor S.U.toScheme (idealOnOpen S)).obj G ≅ F,
          ∃! e : G ≅ H,
            (completionFunctor S.U.toScheme (idealOnOpen S)).map e.hom ≫ ψ.hom = φ.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.19, Tag 0EJ2](https://stacks.math.columbia.edu/tag/0EJ2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
