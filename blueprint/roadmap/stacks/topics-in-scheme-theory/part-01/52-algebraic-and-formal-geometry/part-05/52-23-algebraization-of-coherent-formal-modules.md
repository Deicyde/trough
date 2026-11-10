---
declaration: section
origin: cited
lean: Stacks.Algebraization.finite_globalSections_of_finite_idealPowerSections, Stacks.Algebraization.canonicallyExtends_of_finite_globalSections, Stacks.Algebraization.canonicallyExtends_of_finite_idealPowerSections, Stacks.Algebraization.HasRegularSequenceOnCompletedStalks, Stacks.Algebraization.HasFiniteLowDegreeCohomology, Stacks.Algebraization.canonicallyExtends_of_regularSequence, Stacks.Algebraization.essImage_completionFunctor_of_regularSequence, Stacks.Algebraization.hasFiniteLowDegreeCohomology_iff_hasDepthDimensionAt_two
statement: formalized
proof: formalized
---

# 52.23 Algebraization of coherent formal modules, VI

Section 52.23 of the Stacks Project, [Tag 0EJR](https://stacks.math.columbia.edu/tag/0EJR). 4 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EJS, a proposition

[Tag 0EJS](https://stacks.math.columbia.edu/tag/0EJS) in the Stacks Project.

**`Stacks.Algebraization.finite_globalSections_of_finite_idealPowerSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean#L185). The attribute's comment: “the induction giving finiteness of every H⁰(U, Fₙ), with the direct-sum decomposition of Iⁿ F₍ₙ₊₁₎ replaced by the hypothesis that its sections are finite”.

> **Stacks Project, Tag 0EJS (the induction of the proof).** If `H⁰(U, F_1)` is a finite
> `A`-module and every `H⁰(U, I^(n+1) F_(n+1))` is a finite `A`-module, then `H⁰(U, F_n)` is a
> finite `A`-module for every `n`.
>
> This is the step "using the assumption of finiteness of `H⁰(U, F_1)` and induction, we first
> conclude that `M_n = H⁰(U, F_n)` is a finite `A`-module for all `n`" of the source. The source
> gets finiteness of `H⁰(U, I^(n+1) F_(n+1))` from the stalkwise direct-sum decomposition of
> `I^(n+1) F_(n+1)` into copies of `F_1`, which is not available in this library; here it is a
> hypothesis.

```lean
theorem finite_globalSections_of_finite_idealPowerSections
    (h0 : Module.Finite S.A ((globalSectionsSystem S F).obj (op 0)))
    (hker : ∀ n, Module.Finite S.A (idealPowerSections S F n)) :
    ∀ n, Module.Finite S.A ((globalSectionsSystem S F).obj (op n))
```

**`Stacks.Algebraization.canonicallyExtends_of_finite_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean#L221). The attribute's comment: “the reduction to Tag 0EHH: condition (c) from finiteness of every H⁰(U, Fₙ), with conditions (a) and (b) as hypotheses”.

> **Stacks Project, Tag 0EJS (condition (c) of Tag 0EHH).** Finiteness of every `H⁰(U, F_n)`
> implies the finite-image condition (c) of the Mittag-Leffler criterion Stacks 0EHH, so together
> with the Mittag-Leffler condition (a) and the topology condition (b) it gives canonical
> extension.
>
> The source derives (a) and (b) from Cohomology 0GYK and 0GYM applied to the graded module
> `⨁_n H^p(U, IⁿF_(n+1))`; here they are hypotheses.

```lean
theorem canonicallyExtends_of_finite_globalSections
    (hML : IsMittagLefflerCategorical (globalSectionsSystem S F))
    (htop : (⨅ n : ℕ, TopologicalSpace.induced
      (fun x : limitGlobalSections S F =>
        (limit.π (globalSectionsSystem S F) (op n)).hom x) ⊥) =
        S.I.adicModuleTopology (limitGlobalSections S F))
    (hfin : ∀ n, Module.Finite S.A ((globalSectionsSystem S F).obj (op n))) :
    CanonicallyExtends S F
```

**`Stacks.Algebraization.canonicallyExtends_of_finite_idealPowerSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean#L240). The attribute's comment: “the finiteness half: conditions (a), (b) of Tag 0EHH and finiteness of the sections of Iⁿ F₍ₙ₊₁₎ are hypotheses instead of consequences of the regular sequence”.

> **Stacks Project, Tag 0EJS (the finiteness half).** A coherent adic system on the open
> complement extends canonically to `X` as soon as its system of global sections has
> Mittag-Leffler, the limit topology on the module of compatible sections is the `I`-adic topology,
> `H⁰(U, F_1)` is a finite `A`-module, and every `H⁰(U, I^(n+1) F_(n+1))` is a finite
> `A`-module.

```lean
theorem canonicallyExtends_of_finite_idealPowerSections
    (hML : IsMittagLefflerCategorical (globalSectionsSystem S F))
    (htop : (⨅ n : ℕ, TopologicalSpace.induced
      (fun x : limitGlobalSections S F =>
        (limit.π (globalSectionsSystem S F) (op n)).hom x) ⊥) =
        S.I.adicModuleTopology (limitGlobalSections S F))
    (h0 : Module.Finite S.A ((globalSectionsSystem S F).obj (op 0)))
    (hker : ∀ n, Module.Finite S.A (idealPowerSections S F n)) :
    CanonicallyExtends S F
```

**`Stacks.Algebraization.HasRegularSequenceOnCompletedStalks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean#L273). The attribute's comment: “hypothesis (1), as a predicate; not used by any result in this file”.

> **Stacks Project, Tag 0EJS, hypothesis (1).** There are `f₁, …, f_d ∈ I` such that at every
> point `y` of `U ∩ Y` the ideal `I 𝒪_{X,y}` is generated by the germs of `f₁, …, f_d` and those
> germs form an `F_y^∧`-regular sequence.
>
> The locus `U ∩ Y` is the support of the ideal sheaf `I 𝒪_U`, and `F_y^∧` is
> `Stacks.Algebraization.completedStalk`. The sequence is taken as a sequence of elements of the
> local ring `𝒪_{X,y}` acting on `F_y^∧`, which is how the source's `f_i ∈ I ⊆ A` act.

```lean
def HasRegularSequenceOnCompletedStalks : Prop
```

**`Stacks.Algebraization.HasFiniteLowDegreeCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequence.lean#L287). The attribute's comment: “hypothesis (2), as a predicate; not used by any result in this file”.

> **Stacks Project, Tag 0EJS, hypothesis (2).** `H⁰(U, F_1)` and `H¹(U, F_1)` are finite
> `A`-modules.
>
> Degree zero is the global-sections module of the system, and degree one is the first right
> derived functor of sections over the base, `Stacks.LocalCohomology.cohomologyOverBase`.

```lean
def HasFiniteLowDegreeCohomology : Prop
```

**`Stacks.Algebraization.canonicallyExtends_of_regularSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequenceCanonicalExtension.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequenceCanonicalExtension.lean#L407). The attribute's comment: “the system extends canonically to X”.

> **Stacks Project, Tag 0EJS.** In Situation 0EHC let `(F_n)` be an object of
> `Coh(U, I 𝒪_U)`. Assume that
>
> 1. there exist `f₁, …, f_d ∈ I` such that for `y ∈ U ∩ Y` the ideal `I 𝒪_{X,y}` is generated by
>    `f₁, …, f_d` and `f₁, …, f_d` form an `F_y^∧`-regular sequence
>    (`Stacks.Algebraization.HasRegularSequenceOnCompletedStalks`),
> 2. `H⁰(U, F_1)` and `H¹(U, F_1)` are finite `A`-modules
>    (`Stacks.Algebraization.HasFiniteLowDegreeCohomology`).
>
> Then `(F_n)` extends canonically to `X`.
>
> The proof is the source's: the decomposition
> `Stacks.Algebraization.exists_isIso_idealPowerDesc_of_regularSequence` of `Iⁿ F_(n+1)` into copies
> of `F_1` indexed by the monomials in the `fᵢ`, fed to
> `Stacks.Algebraization.canonicallyExtends_of_idealPowerDesc`, which verifies conditions (a), (b),
> (c) of Stacks 0EHH.

```lean
theorem canonicallyExtends_of_regularSequence (hreg : HasRegularSequenceOnCompletedStalks S F)
    (h2 : HasFiniteLowDegreeCohomology S F) : CanonicallyExtends S F
```

**`Stacks.Algebraization.essImage_completionFunctor_of_regularSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequenceCanonicalExtension.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/RegularSequenceCanonicalExtension.lean#L418). The attribute's comment: “in particular, if A is complete, the system is the completion of a coherent 𝒪\_U-module”.

> **Stacks Project, Tag 0EJS, the second sentence.** Under the hypotheses of Stacks 0EJS, if
> `A` is moreover `I`-adically complete, then `(F_n)` is the completion of a coherent
> `𝒪_U`-module.

```lean
theorem essImage_completionFunctor_of_regularSequence [IsAdicComplete S.I S.A]
    (hreg : HasRegularSequenceOnCompletedStalks S F) (h2 : HasFiniteLowDegreeCohomology S F) :
    (completionFunctor S.U.toScheme (idealOnOpen S)).essImage F
```

## Tag 0EJT, a remark

[Tag 0EJT](https://stacks.math.columbia.edu/tag/0EJT) in the Stacks Project.

**`Stacks.Algebraization.hasFiniteLowDegreeCohomology_iff_hasDepthDimensionAt_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterion.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterion.lean#L192). The attribute's comment: “the equivalence; only the formal-fibre step and an H^p(U, F₁) bridge are assumed”.

> **Stacks Project, Tag 0EJT (the equivalence).** Assume `A` has a dualizing complex. Then
> hypothesis (2) of Stacks 0EJS, that `H⁰(U, F_1)` and `H¹(U, F_1)` are finite `A`-modules, holds
> if and only if `depth(F_{1,y}) + dim(𝒪_{closure{y}, z}) > 2` for every `y ∈ U ∩ Y` and every
> `z ∈ Z ∩ closure{y}`.
>
> The right-hand side is `Stacks.Algebraization.HasDepthDimensionAt` at `2` for a finite
> `A`-module `M` whose associated sheaf restricts to `F_1` on `U`. The equivalence is the
> criterion of Stacks 0BJY at `n = 2`, which is proved here as
> `Stacks.Algebraization.affineDepthDimensionCriterion`; the dualizing complex discharges its
> catenarity assumption by Stacks 0A80 and enters the proof only through that and through
> `hformalOfDual`. The two comparison hypotheses are a bridge between two spellings of the same
> `A`-module `H^p(U, F_1)` and assume nothing about the situation, and the passage from
> `complementCohomologyBase` to coherence of the higher direct images is clause (3) of
> Stacks 0BK0 and is proved.

```lean
public theorem hasFiniteLowDegreeCohomology_iff_hasDepthDimensionAt_two
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (M : ModuleCat.{u} (CommRingCat.of S.A)) (hM : Module.Finite S.A M)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hformalOfDual :
      (∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K) →
        ∀ q : PrimeSpectrum S.A,
          Stacks.LocalCohomology.FormalFibersHavePropertySk
            (Localization.AtPrime q.asIdeal) 2)
    (hcompare₀ : Module.Finite S.A ((globalSectionsSystem S F).obj (op 0)) ↔
      Module.Finite S.A (complementCohomologyBase (A := CommRingCat.of S.A) S.a M 0))
    (hcompare₁ : Module.Finite S.A
        (Stacks.LocalCohomology.cohomologyOverBase.{u, u} S.A S.U.ι (F.obj.obj (op 0)) 1) ↔
      Module.Finite S.A (complementCohomologyBase (A := CommRingCat.of S.A) S.a M 1)) :
    HasFiniteLowDegreeCohomology S F ↔ HasDepthDimensionAt S M 2
```

**`Stacks.Algebraization.hasDepthDimensionAt_two_of_pointwiseBounds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterion.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterion.lean#L321). The attribute's comment: “the trailing sufficient condition, via the two pointwise bounds it yields”.

> **Stacks Project, Tag 0EJT (the sufficient condition).** The depth–dimension inequality at
> `2` holds when `F_1` is finite locally free on `𝒪_{U ∩ Y}`, `Y` is `(S₂)`, and
> `codim(Z', Y') ≥ 3` for every pair of irreducible components `Y'` of `Y` and `Z'` of `Z` with
> `Z' ⊆ Y'`.
>
> The two pointwise bounds that the condition yields are hypotheses, for one reason each.
> `PointwiseSerreTwoBound` would follow from `(S₂)` for `Y` by way of the depth of a finite
> locally free module over a local ring being the depth of that ring, and that statement has no
> public form in this library; the other two steps it needs do, namely
> `moduleDepth_eq_depth` and `Module.depth_eq_depth_map_algebraMap`.
> `PointwiseCodimensionThreeBound` would follow from the codimension clause by additivity of
> codimension along a chain, which is available as `catenary_height_add`, but in the direction
> required that needs `A` to be catenary, and catenarity is not part of the condition stated by
> the source. What is proved here is that those two bounds, together with the positivity of
> `dim(𝒪_{closure{y},z})` for `z` strictly above `y`, give the inequality.

```lean
public theorem hasDepthDimensionAt_two_of_pointwiseBounds
    (M : ModuleCat.{u} (CommRingCat.of S.A))
    (N : ModuleCat.{u} (CommRingCat.of (S.A ⧸ S.I)))
    (hcond : HasLocallyFreeCodimensionThreeCondition S N)
    (hserre : PointwiseSerreTwoBound S M N)
    (hcodim : PointwiseCodimensionThreeBound S M N) :
    HasDepthDimensionAt S M 2
```

**`Stacks.Algebraization.finite_lowDegreeCohomology_iff_depthDimension_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterionDualizing.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FinitenessDepthCriterionDualizing.lean#L572). The attribute's comment: “the equivalence and the sufficient condition”.

> **Stacks Project, Tag 0EJT.** In Situation 0EHC, let `(F_n)` be a coherent `I`-adic system on
> `U = Spec A ∖ V(𝔞)`, as in Stacks 0EJS, and assume `A` has a dualizing complex.
>
> * `H⁰(U, F₁)` and `H¹(U, F₁)` are finite `A`-modules if and only if
>   `depth(F_{1,y}) + dim(𝒪_{closure{y}, z}) > 2` for all `y ∈ U ∩ Y` and `z ∈ Z ∩ closure{y}`.
>   The depth is that of the stalk of `F₁` at `y` over `𝒪_{U,y}`; the point `z` is a prime `𝔮` of
>   `A` containing `𝔞` and the prime `𝔭` of `y`, and `dim(𝒪_{closure{y}, z})` is the height of the
>   image of `𝔮` in `A ⧸ 𝔭`.
> * This holds if `F₁` is a finite locally free `𝒪_{U ∩ Y}`-module, that is its pullback along the
>   closed immersion `U ∩ Y ⟶ U` is finite locally free, `Y = Spec(A ⧸ I)` is `(S₂)`, and
>   `codim(Z', Y') ≥ 3` for every pair of irreducible components `Y'` of `Y` and `Z'` of `Z` with
>   `Z' ⊆ Y'`. The components of `Y` and `Z` are the minimal primes of `I` and of `𝔞`, `Z' ⊆ Y'`
>   is the inclusion of those primes, and `codim(Z', Y')` is the height of the image of the prime
>   of `Z'` in the quotient by the prime of `Y'`.

```lean
theorem finite_lowDegreeCohomology_iff_depthDimension_of_isDualizingComplex
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (K : DerivedCategory (ModuleCat.{u} S.A)) (hK : Dualizing.IsDualizingComplex K) :
    (HasFiniteLowDegreeCohomology S F ↔
      ∀ y : S.U.toScheme, S.I ≤ (underlyingPrime S y).asIdeal →
        ∀ q : PrimeSpectrum S.A, S.a ≤ q.asIdeal → (underlyingPrime S y).asIdeal ≤ q.asIdeal →
          (2 : ℕ∞) < Module.depth (S.U.toScheme.presheaf.stalk y)
              (IsLocalRing.maximalIdeal (S.U.toScheme.presheaf.stalk y))
              ((F.obj.obj (op 0)).presheaf.stalk y) +
            (q.asIdeal.map (Ideal.Quotient.mk (underlyingPrime S y).asIdeal)).height) ∧
      (Scheme.Modules.IsFiniteLocallyFree
          ((Scheme.Modules.pullback (intersectionUYι S)).obj (F.obj.obj (op 0))) →
        PropertySkRing (S.A ⧸ S.I) 2 →
        (∀ p ∈ S.I.minimalPrimes, ∀ q ∈ S.a.minimalPrimes, p ≤ q →
          3 ≤ (q.map (Ideal.Quotient.mk p)).height) →
        HasFiniteLowDegreeCohomology S F ∧
          ∀ y : S.U.toScheme, S.I ≤ (underlyingPrime S y).asIdeal →
            ∀ q : PrimeSpectrum S.A, S.a ≤ q.asIdeal → (underlyingPrime S y).asIdeal ≤ q.asIdeal →
              (2 : ℕ∞) < Module.depth (S.U.toScheme.presheaf.stalk y)
                  (IsLocalRing.maximalIdeal (S.U.toScheme.presheaf.stalk y))
                  ((F.obj.obj (op 0)).presheaf.stalk y) +
                (q.asIdeal.map (Ideal.Quotient.mk (underlyingPrime S y).asIdeal)).height)
```

## Tag 0EJU, a proposition

[Tag 0EJU](https://stacks.math.columbia.edu/tag/0EJU) in the Stacks Project.

**`Stacks.Algebraization.canonicallyExtends_of_flatLocalBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FlatLocalBaseCanonicalExtension.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FlatLocalBaseCanonicalExtension.lean#L493).

> **Stacks Project, Tag 0EJU.** In Situation 0EHC let `(F_n)` be a coherent `I`-adic system on
> `U`, and let `(R, 𝔪)` be a Noetherian local ring with a ring map `R → A` such that `I = 𝔪 A` and
> the formal stalks `F_y^∧`, `y ∈ U ∩ Y`, are `R`-flat (both recorded by `B`), and suppose that
> `H⁰(U, F_1)` and `H¹(U, F_1)` are finite `A`-modules. Then `(F_n)` extends canonically to `X`.
>
> The proof verifies the three conditions of Stacks 0EHH: (a) is
> `Stacks.Algebraization.isMittagLeffler_globalSectionsSystem_of_flatLocalBase`, (b) is
> `Stacks.Algebraization.limitTopology_eq_adicModuleTopology_of_flatLocalBase`, and (c) comes from
> the finiteness of every `H⁰(U, Iⁿ F_(n+1))`, which the direct-sum decomposition
> `Stacks.Algebraization.exists_isoDirectSum_idealPowerSub` gives.

```lean
theorem canonicallyExtends_of_flatLocalBase (B : FlatLocalBase S F)
    (h3 : HasFiniteLowDegreeCohomology S F) : CanonicallyExtends S F
```

**`Stacks.Algebraization.essImage_completionFunctor_of_flatLocalBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FlatLocalBaseCanonicalExtension.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/FlatLocalBaseCanonicalExtension.lean#L505). The attribute's comment: “in particular, over an I-adically complete A the system is the completion of a coherent 𝒪\_U-module”.

> **Stacks Project, Tag 0EJU, the concluding sentence.** Under the hypotheses of Stacks 0EJU, if
> `A` is moreover `I`-adically complete, then `(F_n)` is the completion of a coherent
> `𝒪_U`-module.

```lean
theorem essImage_completionFunctor_of_flatLocalBase [IsAdicComplete S.I S.A]
    (B : FlatLocalBase S F) (h3 : HasFiniteLowDegreeCohomology S F) :
    (completionFunctor S.U.toScheme (idealOnOpen S)).essImage F
```

## Tag 0EJV, a remark

[Tag 0EJV](https://stacks.math.columbia.edu/tag/0EJV) in the Stacks Project.

**`Stacks.Algebraization.isCompletionOfCoherent_of_flat_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ProperLocalBaseAlgebraization.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ProperLocalBaseAlgebraization.lean#L82). The attribute's comment: “algebraization: a flat object of Coh(U, 𝔪𝒪\_U) with j\_*F₁ and R¹j\_*F₁ coherent is the completion of a coherent 𝒪\_U-module”.

> **Stacks 0EJV, algebraization over a complete local base.** Let `(R, 𝔪)` be a complete
> Noetherian local ring, let `p : X ⟶ Spec R` be proper, let `Z` be a closed subset of the special
> fibre `X_1`, let `U = X ∖ Z` with inclusion `j = U.ι`, and let `(F_n)` be an object of
> `Coh(U, 𝔪𝒪_U)`. Assume that `F_n` is flat over `R/𝔪ⁿ` for all `n`, and that `j_*F_1` and
> `R¹j_*F_1` are coherent. Then `(F_n)` is the completion of a coherent `𝒪_U`-module.

```lean
theorem isCompletionOfCoherent_of_flat_of_isCoherent
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of R)) [IsProper p]
    (Z : Closeds X) (hZ : Z ≤ (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).support)
    (U : X.Opens) (hU : (U : Set X) = (Z : Set X)ᶜ)
    (F : Stacks.Coherent.CoherentAdicSystems
      ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι))
    (hflat : ∀ n : ℕ, StalksFlatOverQuotient R (baseToStalk R (U.ι ≫ p))
      (IsLocalRing.maximalIdeal R ^ (n + 1)) (F.obj.obj (op n)))
    (h0 : ((Scheme.Modules.pushforward U.ι).obj (F.obj.obj (op 0))).IsCoherent)
    (h1 : (((Scheme.Modules.pushforward U.ι).rightDerived 1).obj (F.obj.obj (op 0))).IsCoherent) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian p
    IsCompletionOfCoherent ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι) F
```

**`Stacks.Algebraization.exists_specialFibre_directImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/SpecialFibreDirectImages.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/SpecialFibreDirectImages.lean#L116). The attribute's comment: “the closing paragraph: F₁ is a coherent sheaf on the special fibre U₁, and j\_*F₁ = j₁,*F₁ and R¹j\_*F₁ = R¹j₁,*F₁ for the special fibre j₁ : U₁ → X₁ of j”.

> **Stacks 0EJV, the closing paragraph: `j_*F_1` and `R¹j_*F_1` are conditions on the special
> fibre.** Let `(R, 𝔪)` be a Noetherian local ring, `p : X ⟶ Spec R` proper, `U ⊆ X` open with
> inclusion `j`, and `(F_n)` an object of `Coh(U, 𝔪𝒪_U)`. Write `i : X_1 ⟶ X` and `i_U : U_1 ⟶ U`
> for the special fibres and `j₁ : U_1 ⟶ X_1` for the special fibre of `j`. Then `F_1` is a coherent
> sheaf on `U_1`: there is a coherent `𝒪_{U_1}`-module `G` with `i_{U,*} G ≅ F_1`; and
> `j_*F_1 ≅ i_* j₁_* G` and `R¹j_*F_1 ≅ i_* R¹j₁_* G`.

```lean
theorem exists_specialFibre_directImage_iso
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of R)) [IsProper p] (U : X.Opens)
    (F : Stacks.Coherent.CoherentAdicSystems
      ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι)) :
    ∃ G : ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι).subscheme.Modules,
      G.IsCoherent ∧
      Nonempty ((Scheme.Modules.pushforward
        ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι).subschemeι).obj G ≅
          F.obj.obj (op 0)) ∧
      Nonempty ((Scheme.Modules.pushforward U.ι).obj (F.obj.obj (op 0)) ≅
        (Scheme.Modules.pushforward
          (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subschemeι).obj
          ((Scheme.Modules.pushforward
            (specialFibreMap (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p) U)).obj G)) ∧
      Nonempty (((Scheme.Modules.pushforward U.ι).rightDerived 1).obj (F.obj.obj (op 0)) ≅
        (Scheme.Modules.pushforward
          (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subschemeι).obj
          (((Scheme.Modules.pushforward
            (specialFibreMap (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p) U)).rightDerived
              1).obj G))
```

**`Stacks.Algebraization.isCoherent_specialFibre_directImages_of_hasPropertySk_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/SpecialFibreSerreCriterion.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/SpecialFibreSerreCriterion.lean#L255). The attribute's comment: “the closing paragraph: if X₁ is (S₂) and irreducible, dim(X₁) - dim(Z) ≥ 3 and F₁ is a locally free O\_\{U₁}-module, then j₁,*F₁ and R¹j₁,*F₁ are coherent”.

> **Stacks 0EJV, the closing paragraph: the `(S₂)` criterion on the special fibre.** Let
> `(R, 𝔪)` be a Noetherian local ring, `p : X ⟶ Spec R` locally of finite type, `Z ⊆ X` closed and
> `U = X ∖ Z`. Write `X₁` and `U₁` for the special fibres and `j₁ : U₁ ⟶ X₁` for the special fibre
> of the inclusion `U ⊆ X`. If `X₁` is `(S₂)` and irreducible, `dim(X₁) - dim(Z) ≥ 3`, and `G` is a
> finite locally free `𝒪_{U₁}`-module, then `j₁,*G` and `R¹j₁,*G` are coherent.
>
> The special fibre is locally of finite type over the residue field `R/𝔪`, being the base change
> `X ×_{Spec R} Spec(R/𝔪)`
> (`Stacks.PuncturedSpectrumPicard.baseIdealSubschemeIsoPullback`); `j₁` is an open immersion
> whose image is `X₁ ∖ Z`; and the closed subset `X₁ ∩ Z` of `X₁` has dimension at most `dim(Z)`.
> So `Stacks.Algebraization.isCoherent_pushforward_and_rightDerived_one_of_hasPropertySk_two`
> applies.

```lean
theorem isCoherent_specialFibre_directImages_of_hasPropertySk_two
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of R)) [LocallyOfFiniteType p]
    (Z : Closeds X) (U : X.Opens) (hU : (U : Set X) = (Z : Set X)ᶜ)
    [IrreducibleSpace (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subscheme]
    (hS₂ : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian p
      letI : IsLocallyNoetherian (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subscheme :=
        isLocallyNoetherian_of_isClosedImmersion
          (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subschemeι
      HasPropertySk (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subscheme 2)
    (hdim : topologicalKrullDim (Z : Set X) + 3 ≤
      topologicalKrullDim (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).subscheme)
    (G : ((baseIdealSheaf R (IsLocalRing.maximalIdeal R) p).comap U.ι).subscheme.Modules)
    (hG : Scheme.Modules.IsFiniteLocallyFree G) :
    ((Scheme.Modules.pushforward
        (specialFibreMap (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p) U)).obj G).IsCoherent ∧
      (((Scheme.Modules.pushforward
        (specialFibreMap (baseIdealSheaf R (IsLocalRing.maximalIdeal R) p) U)).rightDerived
          1).obj G).IsCoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.23, Tag 0EJR](https://stacks.math.columbia.edu/tag/0EJR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
