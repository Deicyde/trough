---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.CoherentBaseCohomology.isCoherent_cohomology_of_isPerfect_derivedGlobalSections, Stacks.AlgebraicGeometry.CoherentBaseCohomology.isCoherent_rightDerived_moduleGlobalSections, Stacks.Cohomology.CountableSections.countable_cohomology_derivedTensor_and_ext_of_isCompact, Stacks.Cohomology.CountableSections.countable_cohomology_derivedTensor_of_isCompact, Stacks.Cohomology.CountableSections.exists_isHomotopyColimit_isPerfect_iff_countable, Stacks.Cohomology.CountableSections.exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedSheafHom, Stacks.Cohomology.CountableSections.exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedTensor
statement: formalized
proof: formalized
---

# 36.33 Other applications

Section 36.33 of the Stacks Project, [Tag 0CRN](https://stacks.math.columbia.edu/tag/0CRN). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EX6, a lemma

[Tag 0EX6](https://stacks.math.columbia.edu/tag/0EX6) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentBaseCohomology.isCoherent_cohomology_of_isPerfect_derivedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentBaseCohomology.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/CoherentBaseCohomology.lean#L168). The attribute's comment: “carrying as an explicit hypothesis Tag 0A1H: RΓ(X, G) is perfect over the base”.

> **[Stacks, Tag 0EX6].** Let `R` be a coherent ring, let `f : X ⟶ Spec R` be of finite
> presentation ([Stacks, Tag 01TP] (3), spelled out as its three constituent properties) and let `G`
> be an `𝒪_X`-module of finite presentation, flat over `R`, whose support is proper over `R`. Then
> `Hⁱ(X, G)`, with its `R`-action restricted along `R ⟶ Γ(X, 𝒪_X)`, is a coherent `R`-module in
> every degree.
>
> The proof is the source's: `RΓ(X, G)` is a perfect object of `D(R)` ([Stacks, Tag 0A1H] for
> `E = 𝒪_X` and the one-term complex `G`, carried here as the hypothesis `hperf`), a perfect object
> is pseudo-coherent ([Stacks, Tag 0658]), and over a coherent ring the cohomology modules of a
> bounded above pseudo-coherent object are coherent ([Stacks, Tag 0EWZ]); `cohomologyIso` identifies
> the cohomology of `RΓ(X, G)` with `Hⁱ(X, G)`.
>
> **Carried hypothesis.** `hperf : StacksDraft.Perfect.IsPerfect (derivedGlobalSectionsOverBase f G)`
> is Tag 0A1H over the affine base, the one input of the source's proof that this library does not
> prove. It is a statement about the complex `RΓ(X, G)`, proved by Noetherian approximation, and not
> the conclusion — which is coherence of the single module `Hⁱ(X, G)` — restated. The source's own
> hypotheses are all present; when Tag 0A1H lands, `hperf` discharges by application.

```lean
theorem isCoherent_cohomology_of_isPerfect_derivedGlobalSections
    {R : Type u} [CommRing R] [IsCoherentRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (G : X.Modules) [G.IsFinitePresentation]
    (_hflat : IsFlatOver f.toLRSHom.toShHom G)
    (_hsupp : ∃ Z : TopologicalSpace.Closeds X,
      (Z : Set X) = SheafOfModules.supp G ∧ IsProperOver f Z)
    (hperf : StacksDraft.Perfect.IsPerfect (derivedGlobalSectionsOverBase f G))
    (i : ℕ) :
    Module.IsCoherent R
      ((ModuleCat.restrictScalars (Stacks.Cech.globalRingHom f).hom).obj
        (((AlgebraicGeometry.moduleGlobalSections X).rightDerived i).obj G))
```

**`Stacks.AlgebraicGeometry.CoherentBaseCohomology.isCoherent_rightDerived_moduleGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentBaseCohomologyUnconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/CoherentBaseCohomologyUnconditional.lean#L68).

> **[Stacks, Tag 0EX6].** Let `R` be a coherent ring, let `f : X ⟶ Spec R` be of finite
> presentation and let `G` be an `𝒪_X`-module of finite presentation, flat over `R`, whose support
> is proper over `R`. Then for every `i` the cohomology module `Hⁱ(X, G)`, with its `R`-action
> restricted along `R ⟶ Γ(X, 𝒪_X)`, is a coherent `R`-module.
>
> The source's proof: `RΓ(X, G)` is a perfect object of `D(R)` by [Stacks, Tag 0A1H]
> (`…ProperSupportGlobalSectionsPerfect.isPerfect_derivedGlobalSectionsOverBase_of_properSupport`),
> and over a coherent ring the cohomology modules of a perfect complex are coherent by
> [Stacks, Tag 0658] and [Stacks, Tag 0EWZ]
> (`isCoherent_cohomology_of_isPerfect_derivedGlobalSections`).

```lean
theorem isCoherent_rightDerived_moduleGlobalSections
    {R : Type u} [CommRing R] [IsCoherentRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (G : X.Modules) [G.IsFinitePresentation]
    (hflat : IsFlatOver f.toLRSHom.toShHom G)
    (hsupp : ∃ Z : TopologicalSpace.Closeds X,
      (Z : Set X) = SheafOfModules.supp G ∧ IsProperOver f Z)
    (i : ℕ) :
    Module.IsCoherent R
      ((ModuleCat.restrictScalars (Stacks.Cech.globalRingHom f).hom).obj
        (((AlgebraicGeometry.moduleGlobalSections X).rightDerived i).obj G))
```

## Tag 0CRP, a lemma

[Tag 0CRP](https://stacks.math.columbia.edu/tag/0CRP) in the Stacks Project.

**`Stacks.Cohomology.CountableSections.countable_cohomology_derivedTensor_and_ext_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CountableExtAndTensor.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/CountableExtAndTensor.lean#L336).

> **[Stacks, Tag 0CRP].** Let `X` be a quasi-compact and quasi-separated scheme. Let `K` be an
> object of `D_QCoh(𝒪_X)` such that the cohomology sheaves `H^i(K)` have countable sets of
> sections over affine opens. Then for any quasi-compact open `U ⊆ X` and any perfect object `E`
> of `D(𝒪_X)` the sets `H^i(U, K ⊗^L E)` and `Ext^i(E|_U, K|_U)` are countable.
>
> Quasi-compactness of `X` is not used, so it is not assumed: the statement holds on every
> quasi-separated scheme. `H^i(U, -)` is the cohomology of the right derived functor of sections
> over `U` (`derivedSectionsOpen`), `⊗^L` is the derived tensor product of `D(𝒪_X)`, perfectness
> is that of [Stacks, Tag 08CM], `E|_U` and `K|_U` are the restrictions along the open immersion
> `U ⟶ X`, and `Ext^i` is the group of degree-`i` morphisms in `D(𝒪_U)`.

```lean
theorem countable_cohomology_derivedTensor_and_ext_of_isCompact [QuasiSeparatedSpace X]
    (K : DerivedCategory X.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsQuasicoherent)
    (hKc : ∀ V : X.Opens, IsAffineOpen V → ∀ i : ℤ,
      Countable Γ((DerivedCategory.homologyFunctor X.Modules i).obj K, V))
    (U : X.Opens) (hU : IsCompact (U : Set X)) (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) (i : ℤ) :
    Countable ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
        ((derivedSectionsOpen X.toRingedSpace U).obj
          (((Stacks.SheafOfModules.derivedTensor X.sheaf).obj K).obj E))) ∧
      Countable (ShiftedHom ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj E)
        ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj K) i)
```

**`Stacks.Cohomology.CountableSections.countable_cohomology_derivedTensor_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CountableOverQuasiCompactOpens.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/CountableOverQuasiCompactOpens.lean#L178). The attribute's comment: “countability of H^i(U, K ⊗^L E) over every quasi-compact open, from countable sections of the cohomology sheaves of K ⊗^L E over affine opens. Two inputs are hypotheses rather than proved. First, that the cohomology of an affine open is the sections of the cohomology sheaves there: the library has this only at another model of the derived category. Second, that the cohomology sheaves of K ⊗^L E inherit countable sections over affine opens from those of K when E is perfect, which is why perfectness of E does not appear. The Ext^i(E|\_U, K|\_U) half is not covered: it needs the isomorphism K ⊗^L E^∨ ≅ RHom(E, K) for perfect E, which is unproved here”.

> Let `X` be a quasi-separated scheme and let `K` and `E` be objects of `D(𝒪_X)`. Suppose the
> cohomology sheaves of `K ⊗^L E` have countable sets of sections over affine opens, and that over
> an affine open the cohomology of `K ⊗^L E` is computed by those sections. Then for every
> quasi-compact open `U` the set `H^i(U, K ⊗^L E)` is countable.

```lean
theorem countable_cohomology_derivedTensor_of_isCompact (X : Scheme.{u}) [QuasiSeparatedSpace X]
    (K E : DerivedCategory (ModuleSheaves X.toRingedSpace))
    (hsections : ∀ (V : X.Opens), IsAffineOpen V → ∀ i : ℤ,
      Countable ((cohomologySheafSectionsOpen X.toRingedSpace V i).obj
        (((Stacks.Cohomology.TorAmplitude.derTensor X.toRingedSpace).tensor.obj K).obj E)))
    (hcomparison : ∀ (V : X.Opens), IsAffineOpen V → ∀ i : ℤ,
      Nonempty ((cohomologyOpen X.toRingedSpace V i).obj
          (((Stacks.Cohomology.TorAmplitude.derTensor X.toRingedSpace).tensor.obj K).obj E) ≅
        (cohomologySheafSectionsOpen X.toRingedSpace V i).obj
          (((Stacks.Cohomology.TorAmplitude.derTensor X.toRingedSpace).tensor.obj K).obj E)))
    (U : X.Opens) (hU : IsCompact (U : Set X)) (i : ℤ) :
    Countable ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
      ((derivedSectionsOpen X.toRingedSpace U).obj
        (((Stacks.Cohomology.TorAmplitude.derTensor X.toRingedSpace).tensor.obj K).obj E)))
```

## Tag 0CRQ, a lemma

[Tag 0CRQ](https://stacks.math.columbia.edu/tag/0CRQ) in the Stacks Project.

**`Stacks.Cohomology.CountableSections.exists_isHomotopyColimit_isPerfect_iff_countable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CountablePerfectHomotopyColimit.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/CountablePerfectHomotopyColimit.lean#L395).

> **[Stacks, Tag 0CRQ].** Let `X` be a quasi-compact and quasi-separated scheme such that the
> sets of sections of `𝒪_X` over affine opens are countable. Let `K` be an object of
> `D_QCoh(𝒪_X)`. The following are equivalent:
>
> 1. `K = hocolim Eₙ` with `Eₙ` a perfect object of `D(𝒪_X)`, and
> 2. the cohomology sheaves `H^i(K)` have countable sets of sections over affine opens.
>
> `hocolim` is the derived colimit of [Stacks, Tag 090Z], perfectness is that of
> [Stacks, Tag 08CM], and the derived category is an arbitrary model of `D(𝒪_X)`.

```lean
theorem exists_isHomotopyColimit_isPerfect_iff_countable {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] [h : HasDerivedCategory.{w} X.Modules]
    (hO : ∀ V : X.Opens, IsAffineOpen V → Countable Γ(X, V))
    (K : DerivedCategory X.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsQuasicoherent) :
    (∃ F : ℕ ⥤ DerivedCategory X.Modules,
      (∀ n, @Stacks.Cohomology.PerfectComplexes.IsPerfect X.toRingedSpace h (F.obj n)) ∧
        IsHomotopyColimit F K) ↔
      ∀ V : X.Opens, IsAffineOpen V → ∀ i : ℤ,
        Countable Γ((DerivedCategory.homologyFunctor X.Modules i).obj K, V)
```

## Tag 0CRR, a lemma

[Tag 0CRR](https://stacks.math.columbia.edu/tag/0CRR) in the Stacks Project.

**`Stacks.Cohomology.CountableSections.exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/FlatPushforwardHomHomotopyColimit.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/FlatPushforwardHomHomotopyColimit.lean#L107). The attribute's comment: “(1)”.

> Let `A` be a ring, `X` a scheme of finite presentation over `A` (`p : X ⟶ Spec A`) and
> `f : U ⟶ X` flat of finite presentation. There are an inverse system `L : ℕᵒᵖ ⥤ D(𝒪_X)` of perfect
> objects and maps
>
> `dₙ : RΓ(X, R𝓗om(Lₙ, -)) ⟶ RΓ(U, Lf^* -)`
>
> of functors `D(𝒪_X) ⥤ D(A)`, compatible with the transition maps, such that for every `K` in
> `D_QCoh(𝒪_X)` the maps `dₙ` at `K` exhibit
>
> `RΓ(U, Lf^* K) = hocolim RΓ(X, R𝓗om(Lₙ, K)) = hocolim R Hom_X(Lₙ, K)`
>
> in `D(A)`. The system `L` and the maps `dₙ` do not depend on `K`, and `dₙ` is natural in `K`:
> this is the source's "functorially in `K` in `D_QCoh(𝒪_X)`". Here `RΓ(X, -)` is the derived
> global sections functor into `D(A)`, `R𝓗om` the derived internal Hom, `Lf^*` the derived pullback
> of [Stacks, Tag 06YJ], and `hocolim` the derived colimit of [Stacks, Tag 090Z].
>
> Stated at `HasDerivedCategory.standard`, scoped to this declaration: part (2), biduality and
> [Stacks, Tag 08DQ] exist only at that model.

```lean
theorem exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedSheafHom
    [LocallyOfFinitePresentation p] [QuasiCompact p] [QuasiSeparated p]
    [Flat f] [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f] :
    ∃ (L : ℕᵒᵖ ⥤ DerivedCategory X.Modules)
      (d : ∀ n, (Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op (L.obj (op n))) ⋙
          derivedGlobalSectionsOver p ⟶
        Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f.toLRSHom.toShHom ⋙
          derivedGlobalSectionsOver (f ≫ p)),
      (∀ n, Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) (L.obj (op n))) ∧
      (∀ n, Functor.whiskerRight ((Stacks.SheafOfModules.derivedSheafHom X.sheaf).map
          (L.map (homOfLE (Nat.le_succ n)).op).op) (derivedGlobalSectionsOver p) ≫ d (n + 1) =
          d n) ∧
      ∀ K : DerivedCategory X.Modules,
        (∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsQuasicoherent) →
        IsHomotopyColimitWith
          (L.rightOp ⋙ (Stacks.SheafOfModules.derivedSheafHom X.sheaf).flip.obj K ⋙
            derivedGlobalSectionsOver p)
          ((derivedGlobalSectionsOver (f ≫ p)).obj
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
              f.toLRSHom.toShHom).obj K))
          (fun n => (d n).app K)
```

**`Stacks.Cohomology.CountableSections.exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/FlatPushforwardSectionsHomotopyColimit.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/FlatPushforwardSectionsHomotopyColimit.lean#L306). The attribute's comment: “(2)”.

> **[Stacks, Tag 0CRR] (2).** Let `A` be a ring, `X` a scheme of finite presentation over `A`
> and `f : U ⟶ X` a flat morphism of finite presentation. Then there is a system `E : ℕ ⥤ D(𝒪_X)`
> of perfect objects such that
>
> `RΓ(U, Lf^* K) = hocolim RΓ(X, K ⊗^𝐋 Eₙ)`
>
> in `D(A)`, functorially in `K` in `D_QCoh(𝒪_X)`: there are maps
> `cₙ : RΓ(X, - ⊗^𝐋 Eₙ) ⟶ RΓ(U, Lf^* -)`, natural in `K` and compatible with the transitions of the
> system, which for every `K` with quasi-coherent cohomology are the coprojections of a derived
> colimit. One system `E` serves every `K`.
>
> `RΓ(X, -)` and `RΓ(U, -)` are the `A`-linear derived global sections along `X ⟶ Spec A` and
> `U ⟶ X ⟶ Spec A`, `⊗^𝐋` is the derived tensor product of [Stacks, Tag 06YU], `Lf^*` the derived
> pullback of [Stacks, Tag 06YJ], and `hocolim` the derived colimit of [Stacks, Tag 090Z].
>
> Stated at `HasDerivedCategory.standard`, scoped to this declaration: the projection formula
> ([Stacks, Tag 08EU]), Tor independent base change ([Stacks, Tag 08IB]) and the Leray isomorphism
> exist only at that model.

```lean
theorem exists_isHomotopyColimitWith_derivedGlobalSectionsOver_derivedTensor
    [LocallyOfFinitePresentation p] [QuasiCompact p] [QuasiSeparated p]
    [Flat f] [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f] :
    ∃ (E : ℕ ⥤ DerivedCategory X.Modules)
      (c : ∀ n, (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
          X.toRingedSpace.sheaf).flip.obj (E.obj n) ⋙ derivedGlobalSectionsOver p ⟶
        Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f.toLRSHom.toShHom ⋙
          derivedGlobalSectionsOver (f ≫ p)),
      (∀ n, Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) (E.obj n)) ∧
      (∀ n, Functor.whiskerRight ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
          X.toRingedSpace.sheaf).flip.map (E.map (homOfLE (Nat.le_succ n))))
          (derivedGlobalSectionsOver p) ≫ c (n + 1) = c n) ∧
      ∀ K : DerivedCategory X.Modules,
        (∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsQuasicoherent) →
        IsHomotopyColimitWith
          (E ⋙ (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
            X.toRingedSpace.sheaf).obj K ⋙ derivedGlobalSectionsOver p)
          ((derivedGlobalSectionsOver (f ≫ p)).obj
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
              f.toLRSHom.toShHom).obj K))
          (fun n => (c n).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.33, Tag 0CRN](https://stacks.math.columbia.edu/tag/0CRN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
