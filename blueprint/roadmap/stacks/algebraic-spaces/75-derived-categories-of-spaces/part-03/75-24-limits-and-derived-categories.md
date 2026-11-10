---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.DescentSituation, AlgebraicGeometry.Space.DescentSituation.isHomColimit_of_ringModel, AlgebraicGeometry.Space.DescentSituation.isHomColimit_canonicalDerivedPullbackSystem_of_isPerfect_or_isPseudoCoherent_of_mk_lt_cof_ord, AlgebraicGeometry.Space.DescentSituation.isHomColimit_canonicalDerivedPullbackSystem_of_isPseudoCoherent_of_hasFiniteTorDimension, AlgebraicGeometry.Space.DescentSituation.exists_descendedHom, AlgebraicGeometry.Space.DescentSituation.eventually_map_eq, AlgebraicGeometry.Space.DescentSituation.exists_descendedHom_of_isPerfect, AlgebraicGeometry.Space.DescentSituation.eventually_map_eq_of_isPerfect
statement: formalized
proof: formalized
---

# 75.24 Limits and derived categories

Section 75.24 of the Stacks Project, [Tag 09RG](https://stacks.math.columbia.edu/tag/09RG). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09RH, a situation

[Tag 09RH](https://stacks.math.columbia.edu/tag/09RH) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Limits.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Limits.lean#L53).

> **Stacks 09RH.** A directed inverse system of quasi-compact and quasi-separated algebraic
> spaces over `S` whose transition morphisms are affine, equipped with a chosen limit cone and a
> chosen index.

```lean
structure DescentSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u})) (I : Type v) [Preorder I] [IsDirected I (· ≤ ·)]
```

## Tag 09RI, a lemma

[Tag 09RI](https://stacks.math.columbia.edu/tag/09RI) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.isHomColimit_of_ringModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHom.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHom.lean#L420). The attribute's comment: “the affine ring-translation dictionary `model` is carried as an explicit hypothesis: the reduction of the sheaf-level statement to the ring-level colimit computation of Stacks 09RE, which runs through the induction principle 08GP, Mayer-Vietoris 08H9 and the small-etale-to-Zariski comparison 071Q, is not available in this library”.

> **Stacks 09RI.**  In Situation 09RH, let `E₀` and `K₀` be objects of `D(𝒪_{X₀})`, put
> `E_i = Lf_{i0}^*E₀`, `K_i = Lf_{i0}^*K₀` for `i ≥ 0` and `E = Lf_0^*E₀`, `K = Lf_0^*K₀`.  If
> either `E₀` is perfect and `K₀` lies in `D_QCoh(𝒪_{X₀})`, or `E₀` is pseudo-coherent and `K₀`
> lies in `D_QCoh(𝒪_{X₀})` and has finite Tor dimension, then
>
> `colim_{i ≥ 0} Hom_{D(𝒪_{X_i})}(E_i, K_i) ⟶ Hom_{D(𝒪_X)}(E, K)`
>
> is an isomorphism.
>
> The affine translation dictionary `model` is carried as an explicit hypothesis rather than
> discharged; see "The carried hypothesis" in this file's module documentation for what it is and
> why it is an input of the source's proof and not its conclusion.
>
> The three clauses are read off the ring-level colimit computation of Stacks 09RE, which this
> library proves: surjectivity is
> `Stacks.FilteredColimitHom.exists_descends_derived`, eventual injectivity is
> `Stacks.FilteredColimitHom.exists_le_eq_of_eq_derived`, and the cocone identity is the
> compatibility of the dictionary with `RingModel.hcompat`.

```lean
theorem isHomColimit_of_ringModel
    [∀ U : (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property).C,
      HasSheafify ((smallEtaleRingedSite B S hS (D.stage D.base).obj
        (D.stage D.base).property).J.over U) AddCommGrpCat.{u}]
    [∀ U : (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property).C,
      ((smallEtaleRingedSite B S hS (D.stage D.base).obj
        (D.stage D.base).property).J.over U).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [∀ U : (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property).C,
      ((smallEtaleRingedSite B S hS (D.stage D.base).obj
        (D.stage D.base).property).J.over U).HasSheafCompose
          (forget₂ RingCat.{u} AddCommGrpCat.{u})]
    [(Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property).O).Additive]
    [∀ M, ((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
      (smallEtaleRingedSite B S hS (D.stage D.base).obj
        (D.stage D.base).property).O).obj M).Additive]
    [∀ (M N : CochainComplex
        (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property) ℤ),
      HomologicalComplex.HasMapBifunctor M N
        (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
          (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property).O)
        (ComplexShape.up ℤ)]
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (hcase :
      ((smallEtaleRingedSite B S hS (D.stage D.base).obj
            (D.stage D.base).property).IsPerfect E₀ ∧
          ∀ n : ℤ, ((DerivedCategory.homologyFunctor
            (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property)
              n).obj K₀).IsQuasicoherentOnSite) ∨
        ((smallEtaleRingedSite B S hS (D.stage D.base).obj
            (D.stage D.base).property).IsPseudoCoherent E₀ ∧
          (∀ n : ℤ, ((DerivedCategory.homologyFunctor
            (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property)
              n).obj K₀).IsQuasicoherentOnSite) ∧
          Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension T K₀))
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (model : RingModel sys E₀ K₀ R) :
    IsHomColimit sys E₀ K₀
```

**`AlgebraicGeometry.Space.DescentSituation.isHomColimit_canonicalDerivedPullbackSystem_of_isPerfect_or_isPseudoCoherent_of_mk_lt_cof_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHomPerfectQcohLeaf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHomPerfectQcohLeaf.lean#L110). The attribute's comment: “both clauses, at the tag's own hypotheses”.

> **Stacks 09RI.**  In Situation 09RH, let `E₀` and `K₀` be objects of `D(𝒪_{X₀})`, put
> `E_i = Lf_{i0}^*E₀`, `K_i = Lf_{i0}^*K₀` for `i ≥ 0` and `E = Lf_0^*E₀`, `K = Lf_0^*K₀`.  If
> either `E₀` is perfect and `K₀` lies in `D_QCoh(𝒪_{X₀})`, or `E₀` is pseudo-coherent and `K₀`
> lies in `D_QCoh(𝒪_{X₀})` and has finite Tor dimension, then
>
> `colim_{i ≥ 0} Hom_{D(𝒪_{X_i})}(E_i, K_i) ⟶ Hom_{D(𝒪_X)}(E, K)`
>
> is an isomorphism.
>
> This is
> `isHomColimit_canonicalDerivedPullbackSystem_of_isPerfect_or_isPseudoCoherent_of_qcohUnit`
> with its hypothesis `hunit` discharged by
> `shiftedIsColim_baseChangeSystem_unit_of_isQuasicoherentOnSite`,
> so both clauses of the tag are proved at its own hypotheses.
>
> The two restrictions beyond the tag are counterexample-forced for this formalization:
> `I : Type u` is refuted beyond it by
> `StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent/Counterexample.lean`, and
> `#I < B.cutoff.ord.cof` by
> `StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitLargeIndexCounterexample.lean`.  `T`
> is the derived tensor product the Tor condition of clause (2) is predicated on, not an added
> assumption.

```lean
theorem isHomColimit_canonicalDerivedPullbackSystem_of_isPerfect_or_isPseudoCoherent_of_mk_lt_cof_ord
    (E₀ K₀ : derivedModules B S hS (D.stage D.base))
    (hI : Cardinal.mk I < B.cutoff.ord.cof)
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (hcase :
      ((smallEtaleRingedSite B S hS (D.stage D.base).obj
            (D.stage D.base).property).IsPerfect E₀ ∧
          ∀ n : ℤ, ((DerivedCategory.homologyFunctor
            (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property)
              n).obj K₀).IsQuasicoherentOnSite) ∨
        ((smallEtaleRingedSite B S hS (D.stage D.base).obj
            (D.stage D.base).property).IsPseudoCoherent E₀ ∧
          (∀ n : ℤ, ((DerivedCategory.homologyFunctor
            (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property)
              n).obj K₀).IsQuasicoherentOnSite) ∧
          Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension T K₀)) :
    IsHomColimit D.canonicalDerivedPullbackSystem E₀ K₀
```

**`AlgebraicGeometry.Space.DescentSituation.isHomColimit_canonicalDerivedPullbackSystem_of_isPseudoCoherent_of_hasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHomTorBridge09RI.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitDerivedHomTorBridge09RI.lean#L140). The attribute's comment: “clause (2); clause (1) not included”.

> **The pseudo-coherent case of Stacks 09RI at the spelling of the tag, in the `IsHomColimit`
> form of the tag's conclusion**: `Hom_{D(𝒪_X)}(E, K)` is the filtered colimit of the
> `Hom_{D(𝒪_{X_i})}(E_i, K_i)` for the system of derived pullbacks of Situation 09RH with the
> canonical comparisons.
>
> This carries `@[stacks 09RI]` for **clause (2) of the tag** — `E₀` pseudo-coherent, every
> cohomology sheaf of `K₀` quasi-coherent, `K₀` of finite Tor dimension — at exactly those
> hypotheses, which is one half of the tag's covering set.  Clause (1), `E₀` perfect with `K₀` only
> in `D_QCoh`, is **not** included here and is not a consequence of Stacks 0DKV.
>
> The two restrictions beyond the tag are counterexample-forced for this formalization, not
> conveniences: `I : Type u` is refuted beyond it by
> `StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent/Counterexample.lean`, and
> `#I < B.cutoff.ord.cof` by
> `StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitLargeIndexCounterexample.lean`.  `T`
> is the derived tensor product the Tor condition is predicated on, not an added assumption.

```lean
theorem isHomColimit_canonicalDerivedPullbackSystem_of_isPseudoCoherent_of_hasFiniteTorDimension
    (hI : Cardinal.mk I < B.cutoff.ord.cof)
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (hcase :
      ((smallEtaleRingedSite B S hS (D.stage D.base).obj
          (D.stage D.base).property).IsPseudoCoherent E₀ ∧
        (∀ n : ℤ, ((DerivedCategory.homologyFunctor
          (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property)
            n).obj K₀).IsQuasicoherentOnSite) ∧
        Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension T K₀)) :
    IsHomColimit D.canonicalDerivedPullbackSystem E₀ K₀
```

## Tag 09RJ, a lemma

[Tag 09RJ](https://stacks.math.columbia.edu/tag/09RJ) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.exists_descendedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjects.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjects.lean#L242). The attribute's comment: “fullness of the comparison out of the colimit of the categories of perfect objects, which the source's proof takes from Stacks 09RI; essential surjectivity, the other half of that proof, is not included”.

> **Fullness of the comparison out of the colimit, Stacks 09RJ.**  In Situation 09RH, let `E₀`
> and `K₀` be perfect objects of `D(𝒪_{X₀})` and put `E_i = Lf_{i0}^*E₀`, `K_i = Lf_{i0}^*K₀` for
> `i ≥ 0` and `E = Lf_0^*E₀`, `K = Lf_0^*K₀`.  Then every morphism `E ⟶ K` of `D(𝒪_X)` is the
> image, under the map of Stacks 09RI, of a morphism `E_i ⟶ K_i` at some stage `i ≥ 0`.
>
> The categories of perfect objects are full subcategories of the ambient derived categories, so
> this is fullness of the comparison functor out of the colimit of the `D_perf(𝒪_{X_i})`.
>
> This is the first half of the full faithfulness that the source's proof of Stacks 09RJ takes
> from Stacks 09RI, and it is deduced from Stacks 09RI here.  The hypotheses `model`
> and `hqcK₀` are carried; see "The carried hypotheses" in this file's module documentation.

```lean
theorem exists_descendedHom
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (hqcK₀ : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property) n).obj
        K₀.obj).IsQuasicoherentOnSite)
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (model : RingModel sys E₀.obj K₀.obj R)
    (φ : limitObj sys E₀.obj ⟶ limitObj sys K₀.obj) :
    ∃ (i : D.Stages) (g : stageObj sys E₀.obj i ⟶ stageObj sys K₀.obj i),
      homProjection sys E₀.obj K₀.obj i g = φ
```

**`AlgebraicGeometry.Space.DescentSituation.eventually_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjects.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjects.lean#L270). The attribute's comment: “faithfulness of the comparison out of the colimit of the categories of perfect objects, which the source's proof takes from Stacks 09RI; essential surjectivity, the other half of that proof, is not included”.

> **Faithfulness of the comparison out of the colimit, Stacks 09RJ.**  In Situation 09RH, with
> `E₀` and `K₀` perfect objects of `D(𝒪_{X₀})` as above, two morphisms `E_i ⟶ K_i` at a stage
> `i ≥ 0` whose images `E ⟶ K` in `D(𝒪_X)` agree already have equal images at some later stage.
>
> Together with `AlgebraicGeometry.Space.DescentSituation.exists_descendedHom` this says that the
> hom-sets of `D_perf(𝒪_X)` between objects coming from the system are the filtered colimits of
> the hom-sets at the stages, which is full faithfulness of the comparison out of the colimit of
> the `D_perf(𝒪_{X_i})`.
>
> This is the second half of the full faithfulness that the source's proof of Stacks 09RJ takes
> from Stacks 09RI, and it is deduced from Stacks 09RI here.  The hypotheses `model`
> and `hqcK₀` are carried; see "The carried hypotheses" in this file's module documentation.

```lean
theorem eventually_map_eq
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (hqcK₀ : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS (D.stage D.base).obj (D.stage D.base).property) n).obj
        K₀.obj).IsQuasicoherentOnSite)
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (model : RingModel sys E₀.obj K₀.obj R) (i : D.Stages)
    (g g' : stageObj sys E₀.obj i ⟶ stageObj sys K₀.obj i)
    (hgg : homProjection sys E₀.obj K₀.obj i g = homProjection sys E₀.obj K₀.obj i g') :
    ∃ (j : D.Stages) (h : i ≤ j), homTransition sys E₀.obj K₀.obj i j h g =
      homTransition sys E₀.obj K₀.obj i j h g'
```

**`AlgebraicGeometry.Space.DescentSituation.exists_descendedHom_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjectsPerfectTarget.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjectsPerfectTarget.lean#L116). The attribute's comment: “fullness of the comparison out of the colimit of the categories of perfect objects, which the source's proof takes from Stacks 09RI; essential surjectivity, the other half of that proof, is not included”.

> **Fullness of the comparison out of the colimit, Stacks 09RJ.**  In Situation 09RH, let `E₀`
> and `K₀` be perfect objects of `D(𝒪_{X₀})` and put `E_i = Lf_{i0}^*E₀`, `K_i = Lf_{i0}^*K₀` for
> `i ≥ 0` and `E = Lf_0^*E₀`, `K = Lf_0^*K₀`.  Then every morphism `E ⟶ K` of `D(𝒪_X)` is the
> image, under the map of Stacks 09RI, of a morphism `E_i ⟶ K_i` at some stage `i ≥ 0`.
>
> This is fullness of the comparison functor out of the colimit of the `D_perf(𝒪_{X_i})`.

```lean
theorem exists_descendedHom_of_isPerfect
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (model : RingModel sys E₀.obj K₀.obj R)
    (φ : limitObj sys E₀.obj ⟶ limitObj sys K₀.obj) :
    ∃ (i : D.Stages) (g : stageObj sys E₀.obj i ⟶ stageObj sys K₀.obj i),
      homProjection sys E₀.obj K₀.obj i g = φ
```

**`AlgebraicGeometry.Space.DescentSituation.eventually_map_eq_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjectsPerfectTarget.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/LimitPerfectObjectsPerfectTarget.lean#L134). The attribute's comment: “faithfulness of the comparison out of the colimit of the categories of perfect objects, which the source's proof takes from Stacks 09RI; essential surjectivity, the other half of that proof, is not included”.

> **Faithfulness of the comparison out of the colimit, Stacks 09RJ.**  In Situation 09RH, with
> `E₀` and `K₀` perfect objects of `D(𝒪_{X₀})` as above, two morphisms `E_i ⟶ K_i` at a stage
> `i ≥ 0` whose images `E ⟶ K` in `D(𝒪_X)` agree already have equal images at some later stage.
>
> This is faithfulness of the comparison functor out of the colimit of the `D_perf(𝒪_{X_i})`.

```lean
theorem eventually_map_eq_of_isPerfect
    (T : Stacks.SheafOfModules.DerivedTensorProduct
      (smallEtaleRingedSite B S hS (D.stage D.base).obj (D.stage D.base).property))
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (model : RingModel sys E₀.obj K₀.obj R) (i : D.Stages)
    (g g' : stageObj sys E₀.obj i ⟶ stageObj sys K₀.obj i)
    (hgg : homProjection sys E₀.obj K₀.obj i g = homProjection sys E₀.obj K₀.obj i g') :
    ∃ (j : D.Stages) (h : i ≤ j), homTransition sys E₀.obj K₀.obj i j h g =
      homTransition sys E₀.obj K₀.obj i j h g'
```

**`AlgebraicGeometry.Space.DescentSituation.perfectObjectsDescend_and_perfectHomsDescend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictedPerfectDescentOverIntegers.lean, line 960](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictedPerfectDescentOverIntegers.lean#L960). The attribute's comment: “Under the size bound `ChartsBounded` on the chart systems of the stages, which the source does not state (the sites are size-bounded models of the big fppf site).”.

> **Stacks 09RJ.** In Situation 09RH (`X = lim Xᵢ` along affine transition morphisms of
> quasi-compact quasi-separated algebraic spaces) the category of perfect objects of `D(𝒪_X)` is the
> colimit of the categories of perfect objects of `D(𝒪_{Xᵢ})`: every perfect object on `X` is
> `Lfᵢ^*Eᵢ` for some stage `i` and some perfect `Eᵢ`
> (`AlgebraicGeometry.Space.DescentSituation.PerfectObjectsDescend`), and for perfect `Eᵢ`, `Kᵢ`
> on `Xᵢ` the map `colim_{j ≥ i} Hom(Lf_{ji}^*Eᵢ, Lf_{ji}^*Kᵢ) ⟶ Hom(Lfᵢ^*Eᵢ, Lfᵢ^*Kᵢ)` is
> bijective (`AlgebraicGeometry.Space.DescentSituation.PerfectHomsDescend`).
>
> **Correction.** The statement carries the hypothesis `ChartsBounded` (the size bound
> `AlgebraicGeometry.Space.ChartsBounded` on the chart systems of the stages), which the source does
> not state: the sites here are `u`-small models of the big fppf site with a size cutoff, and the
> bound is what keeps the limits of the affine charts of the stages inside the site
> (`AlgebraicGeometry.Space.ChartsBounded.sizeBound`). It holds for instance when `#I` is below the
> cofinality of the cutoff (`AlgebraicGeometry.Space.chartsBounded_of_lt_cof_ord`).

```lean
theorem perfectObjectsDescend_and_perfectHomsDescend (hb : ChartsBounded B S hS D.system) :
    D.PerfectObjectsDescend ∧ D.PerfectHomsDescend
```

**`AlgebraicGeometry.Space.DescentSituation.perfectObjectsDescend_and_perfectHomsDescend_of_mk_lt_cof_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictedPerfectDescentUnbounded.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictedPerfectDescentUnbounded.lean#L143). The attribute's comment: “both halves, at the tag's own hypotheses”.

> **Stacks 09RJ at the hypotheses of Situation 09RH, with no bounded-charts hypothesis.** In
> Situation 09RH, indexed by a directed set in the universe of the site with fewer elements than
> the cofinality of the site's size cutoff, the category of perfect objects of `D(𝒪_X)` is the
> colimit of the categories of perfect objects of `D(𝒪_{Xᵢ})`: essential surjectivity
> (`AlgebraicGeometry.Space.DescentSituation.PerfectObjectsDescend`) and full faithfulness
> (`AlgebraicGeometry.Space.DescentSituation.PerfectHomsDescend`).
>
> The size bound `AlgebraicGeometry.Space.ChartsBounded` that
> `AlgebraicGeometry.Space.DescentSituation.perfectObjectsDescend_and_perfectHomsDescend` assumes,
> and that the source does not state, is discharged here by
> `AlgebraicGeometry.Space.DescentSituation.chartsBounded_of_mk_lt_cof_ord`.  What is left is
> `#I < B.cutoff.ord.cof`, which is not a weakening: it is refuted beyond that bound by
> `StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitLargeIndexCounterexample.lean`, and
> `I : Type u` is refuted beyond it by
> `StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent/Counterexample.lean`.
>
> This carries `@[stacks 09RJ]` for **both halves** — essential surjectivity
> (`AlgebraicGeometry.Space.DescentSituation.PerfectObjectsDescend`) and full faithfulness
> (`AlgebraicGeometry.Space.DescentSituation.PerfectHomsDescend`) — at Situation 09RH's own
> hypotheses.  The only restriction beyond the tag's is `#I < B.cutoff.ord.cof`, which this
> formalization is counterexample-forced to carry.
>
> The `AlgebraicGeometry.Space.ChartsBounded` bound that
> `AlgebraicGeometry.Space.DescentSituation.perfectObjectsDescend_and_perfectHomsDescend` assumes,
> and which the source does not state, is discharged here.  That statement keeps its own
> registration: `hI` implies `ChartsBounded` but not conversely, so it remains the more general
> conditional form.

```lean
theorem perfectObjectsDescend_and_perfectHomsDescend_of_mk_lt_cof_ord
    (hI : Cardinal.mk I < B.cutoff.ord.cof) :
    D.PerfectObjectsDescend ∧ D.PerfectHomsDescend
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.24, Tag 09RG](https://stacks.math.columbia.edu/tag/09RG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
