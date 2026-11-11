---
declaration: section
origin: cited
lean: AlgebraicGeometry.GrothendieckExistence.ExistenceSituation, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.nonempty_derivedLimitQCoh_and_isDerivedLimit_isGE_isLE, AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_coherator_obj_pushforwardSystem, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPerfect_and_isIso_sheafHomBaseChange, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPerfect_and_isIso_tensorBaseChange, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPseudoCoherent, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.isIso_sectionsOverComparison, AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.exists_open_isZero_homology_isFinitePresentation_isIso
statement: formalized
proof: formalized
---

# 38.28 Grothendieck's Existence Theorem, IV

Section 38.28 of the Stacks Project, [Tag 0CTB](https://stacks.math.columbia.edu/tag/0CTB). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CTC, a situation

[Tag 0CTC](https://stacks.math.columbia.edu/tag/0CTC) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceSituation.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceSituation.lean#L60).

> The standing data of Grothendieck's existence theorem for modules: an inverse system of rings
> with surjective, locally nilpotent transitions, a separated scheme of finite presentation over the
> inverse-limit ring, and a compatible system of finitely presented sheaves on its base changes
> which are flat over, and have proper support over, the affine base at their level.

```lean
structure ExistenceSituation
```

## Tag 0CTD, a lemma

[Tag 0CTD](https://stacks.math.columbia.edu/tag/0CTD) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.nonempty_derivedLimitQCoh_and_isDerivedLimit_isGE_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceCoheratorLimit.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceCoheratorLimit.lean#L462).

> **Stacks Project, Tag 0CTD.** In Situation [Stacks, Tag 0CTC] consider
> `K = R lim_{D_QCoh(𝒪_X)}(Fₙ) = DQ_X(R lim_{D(𝒪_X)} Fₙ)`. Then `K` is in `D^b_QCoh(𝒪_X)` and in
> fact `K` has nonzero cohomology sheaves only in degrees `≥ 0`.
>
> Here, at any model of `D(𝒪_X)`, the data `d` of
> `AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh` are a derived limit
> `L = R lim_{D(𝒪_X)} Fₙ` and `K = DQ_X(L)`, characterized by its universal property; such data
> exist (first conjunct). For any of them, `K` is also a derived limit
> `R lim_{D_QCoh(𝒪_X)}(Fₙ)` of the system read in `D_QCoh(𝒪_X)`, which is the displayed equality,
> and its cohomology sheaves vanish outside `[0, c]` for some `c`.

```lean
theorem nonempty_derivedLimitQCoh_and_isDerivedLimit_isGE_isLE :
    Nonempty S.DerivedLimitQCoh ∧ ∀ d : S.DerivedLimitQCoh,
      (∃ _hp : HasProduct fun n : ℕ => S.quasiCoherentPushforwardSystem.obj ⟨n⟩,
        IsDerivedLimit S.quasiCoherentPushforwardSystem ⟨d.K, d.quasicoherent⟩) ∧
      d.K.IsGE 0 ∧ ∃ c : ℤ, d.K.IsLE c
```

**`AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_coherator_obj_pushforwardSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceDerivedLimit.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceDerivedLimit.lean#L259). The attribute's comment: “the displayed equality only; the coherator of Stacks 0CR0 is an argument, as in Stacks 0CSA and 0CR2”.

> **[Stacks, Tag 0CTD], the displayed equality.** In Situation [Stacks, Tag 0CTC], if `K` is a
> derived limit in `D(𝒪_X)` of the system `(iₙ,* Fₙ)` of
> `AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.derivedPushforwardSystem`, then
> `DQ_X(K)` is a derived limit of the system `(DQ_X(iₙ,* Fₙ))` in `D_QCoh(𝒪_X)`. This is the
> equality `R lim_{D_QCoh(𝒪_X)}(Fₙ) = DQ_X(R lim_{D(𝒪_X)} Fₙ)` of the statement of the tag; the
> existence of the product of the images is part of the conclusion.
>
> The reason is the source's: `DQ_X` is a right adjoint, so it commutes with the countable product
> occurring in a derived-limit triangle, and it is exact because the adjunction `ι ⊣ DQ_X` is
> triangulated.

```lean
theorem isDerivedLimit_coherator_obj_pushforwardSystem (adj : quasiCoherentι S.X.left ⊣ DQ)
    [DQ.CommShift ℤ] [adj.IsTriangulated]
    [HasProduct fun n : ℕ => S.derivedPushforwardSystem.obj ⟨n⟩]
    (K : DerivedCategory S.X.left.Modules)
    (hK : IsDerivedLimit S.derivedPushforwardSystem K) :
    ∃ h : HasProduct fun n : ℕ => DQ.obj (S.derivedPushforwardSystem.obj ⟨n⟩),
      @IsDerivedLimit (quasiCoherentDerivedCategory S.X.left) _ _ _ _ _ _
        (S.derivedPushforwardSystem ⋙ DQ) h (DQ.obj K)
```

## Tag 0CTE, a lemma

[Tag 0CTE](https://stacks.math.columbia.edu/tag/0CTE) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPerfect_and_isIso_sheafHomBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePerfectSheafHom.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePerfectSheafHom.lean#L204). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0CTE, part (2).** In Situation [Stacks, Tag 0CTC] let `K` be as in
> [Stacks, Tag 0CTD] and let `E` be a perfect object of `D(𝒪_X)`. Then
> `N = RHom_X(E, K) = RΓ_A(X, R𝓗om(E, K))` is a perfect object of `D(A)`, and there is a canonical
> isomorphism `N ⊗^𝐋_A Aₙ ≅ RHom_{Xₙ}(E|_{Xₙ}, ℱₙ)` in `D(Aₙ)` for every `n`, with `E|_{Xₙ}` the
> derived pullback: the derived base change of
> `AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.sheafHomLevelMap`,
> built from a cone `p` exhibiting `L = R lim ℱₙ`, is invertible.
>
> As in the source, part (2) and part (1) are translated into each other by
> [Stacks, Tag 08DQ]; here part (2) is read off part (1) at `E^∨`. Stated at
> `HasDerivedCategory.standard` (scoped to this declaration).

```lean
theorem DerivedLimitQCoh.isPerfect_and_isIso_sheafHomBaseChange (d : S.DerivedLimitQCoh)
    (E : DerivedCategory S.X.left.Modules)
    (hE : RingedSpace.IsPerfect (X := S.X.left.toRingedSpace) E) :
    StacksDraft.Perfect.IsPerfect ((derivedGlobalSectionsOver S.X.hom).obj
        (((derivedSheafHom S.X.left.sheaf).obj (op E)).obj d.K)) ∧
      ∀ (p : d.L ⟶ ∏ᶜ fun n : ℕ => S.derivedPushforwardSystemOfModel.obj ⟨n⟩),
        S.IsDerivedLimitCone p → ∀ n : ℕ,
          IsIso (derivedBaseChangeComparison (S.limitProjection n)
            (DerivedLimitQCoh.sheafHomLevelMap S d E hE p n))
```

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPerfect_and_isIso_tensorBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePerfectTensor.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePerfectTensor.lean#L377). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0CTE, part (1).** In Situation [Stacks, Tag 0CTC] let `K` be as in
> [Stacks, Tag 0CTD] and let `E` be a perfect object of `D(𝒪_X)`. Then
> `M = RΓ(X, K ⊗^𝐋 E)` is a perfect object of `D(A)`, and the canonical map
> `M ⊗^𝐋_A Aₙ ⟶ RΓ(Xₙ, ℱₙ ⊗^𝐋 E|_{Xₙ})` is an isomorphism in `D(Aₙ)` for every `n`, with
> `E|_{Xₙ}` the derived pullback.
>
> Here `K` is given by the data `d` of
> `AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh`, the canonical map is
> `(DerivedLimitQCoh.tensorBaseChange S d p n).app E`, built from a cone `p` exhibiting
> `L = R lim ℱₙ`, and the index `n` stands for the level `n + 1` of the source. Stated at
> `HasDerivedCategory.standard` (scoped to this declaration).

```lean
theorem DerivedLimitQCoh.isPerfect_and_isIso_tensorBaseChange (d : S.DerivedLimitQCoh)
    (E : DerivedCategory S.X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.X.left.toRingedSpace) E) :
    StacksDraft.Perfect.IsPerfect ((derivedGlobalSectionsOver S.X.hom).obj
        (((derivedTensorProductFunctor S.X.left.toRingedSpace.sheaf).obj d.K).obj E)) ∧
      ∀ (p : d.L ⟶ ∏ᶜ fun n : ℕ => S.derivedPushforwardSystemOfModel.obj ⟨n⟩),
        S.IsDerivedLimitCone p → ∀ n : ℕ,
          IsIso ((DerivedLimitQCoh.tensorBaseChange S d p n).app E)
```

## Tag 0CTF, a lemma

[Tag 0CTF](https://stacks.math.columbia.edu/tag/0CTF) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.DerivedLimitQCoh.isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePseudoCoherent.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistencePseudoCoherent.lean#L64).

> **[Stacks, Tag 0CTF].** In Situation [Stacks, Tag 0CTC], let `K` be as in
> [Stacks, Tag 0CTD], i.e. `K = DQ_X(R lim_{D(𝒪_X)} iₙ,* ℱₙ)`. Then `K` is pseudo-coherent relative
> to `A = lim Aₙ`: relatively pseudo-coherent ([Stacks, Tag 09UI]) for the structure morphism
> `X ⟶ Spec A`. Stated at the standard model.

```lean
theorem DerivedLimitQCoh.isPseudoCoherent (d : S.DerivedLimitQCoh) :
    S.X.hom.IsPseudoCoherent d.K
```

## Tag 0CTG, a lemma

[Tag 0CTG](https://stacks.math.columbia.edu/tag/0CTG) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.isIso_sectionsOverComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean#L54).

> **[Stacks, Tag 0CTG].** In Situation [Stacks, Tag 0CTC], let `K` be as in
> [Stacks, Tag 0CTD], with a derived-limit cone `p` of `R lim (iₙ,* ℱₙ)`. For every quasi-compact
> open `U ⊆ X`, the canonical map `RΓ(U, K) ⊗_A^𝐋 Aₙ ⟶ RΓ(Uₙ, ℱₙ)` of `D(Aₙ)`, `Uₙ = U ∩ Xₙ`, is an
> isomorphism. Stated at the standard model.

```lean
theorem isIso_sectionsOverComparison (d : S.DerivedLimitQCoh)
    (p : d.L ⟶ ∏ᶜ fun n : ℕ => S.derivedPushforwardSystemOfModel.obj ⟨n⟩)
    (hp : S.IsDerivedLimitCone p) (U : S.X.left.Opens) (hU : IsCompact (U : Set S.X.left))
    (n : ℕ) : IsIso (S.sectionsOverComparison d p U n)
```

## Tag 0CTH, a lemma

[Tag 0CTH](https://stacks.math.columbia.edu/tag/0CTH) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.exists_open_isZero_homology_isFinitePresentation_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean#L69).

> **[Stacks, Tag 0CTH].** In Situation [Stacks, Tag 0CTC], let `K` be as in
> [Stacks, Tag 0CTD], with a derived-limit cone `p`. There is an open `W ⊆ X` containing `X₀` such
> that `Hⁱ(K)|_W = 0` for `i ≠ 0`, `ℱ = H⁰(K)|_W` is of finite presentation, and
> `ℱₙ = ℱ ⊗_{𝒪_X} 𝒪_{Xₙ}`: the canonical maps `iₙ^* H⁰(K) ⟶ ℱₙ`, adjoint to the maps
> `H⁰(K) ⟶ iₙ,* ℱₙ` induced by `K ⟶ iₙ,* ℱₙ`, are isomorphisms. Stated at the standard model.

```lean
theorem exists_open_isZero_homology_isFinitePresentation_isIso (d : S.DerivedLimitQCoh)
    (p : d.L ⟶ ∏ᶜ fun n : ℕ => S.derivedPushforwardSystemOfModel.obj ⟨n⟩)
    (hp : S.IsDerivedLimitCone p) :
    ∃ W : S.X.left.Opens, Set.range (S.closedImmersion 0) ⊆ W ∧
      (∀ j : ℤ, j ≠ 0 →
        IsZero (((DerivedCategory.homologyFunctor S.X.left.Modules j).obj d.K).restrict W.ι)) ∧
      (((DerivedCategory.homologyFunctor S.X.left.Modules 0).obj d.K).restrict
        W.ι).IsFinitePresentation ∧
      ∀ n : ℕ, IsIso
        (((Scheme.Modules.pullbackPushforwardAdjunction (S.closedImmersion n)).homEquiv _ _).symm
          (S.zerothLevelMap d p n))
```

## Tag 0CTI, a lemma

[Tag 0CTI](https://stacks.math.columbia.edu/tag/0CTI) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.exists_open_isProperOver_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean#L90).

> **[Stacks, Tag 0CTI].** In Situation [Stacks, Tag 0CTC], with `K` as in [Stacks, Tag 0CTD]
> and `W` as in [Stacks, Tag 0CTH]: after shrinking `W`, the support of `ℱ = H⁰(K)|_W` is proper over
> `A`. The open produced keeps the three properties of [Stacks, Tag 0CTH]. Stated at the standard
> model.

```lean
theorem exists_open_isProperOver_supp (d : S.DerivedLimitQCoh)
    (p : d.L ⟶ ∏ᶜ fun n : ℕ => S.derivedPushforwardSystemOfModel.obj ⟨n⟩)
    (hp : S.IsDerivedLimitCone p) :
    ∃ W : S.X.left.Opens, Set.range (S.closedImmersion 0) ⊆ W ∧
      (∀ j : ℤ, j ≠ 0 →
        IsZero (((DerivedCategory.homologyFunctor S.X.left.Modules j).obj d.K).restrict W.ι)) ∧
      (((DerivedCategory.homologyFunctor S.X.left.Modules 0).obj d.K).restrict
        W.ι).IsFinitePresentation ∧
      (∀ n : ℕ, IsIso
        (((Scheme.Modules.pullbackPushforwardAdjunction (S.closedImmersion n)).homEquiv _ _).symm
          (S.zerothLevelMap d p n))) ∧
      ∃ Z : Closeds W.toScheme, (Z : Set W.toScheme) = SheafOfModules.supp
          (((DerivedCategory.homologyFunctor S.X.left.Modules 0).obj d.K).restrict W.ι) ∧
        IsProperOver (W.ι ≫ S.X.hom) Z
```

## Tag 0CTJ, a lemma

[Tag 0CTJ](https://stacks.math.columbia.edu/tag/0CTJ) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_forall_spec_factors_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Monomorphism.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Monomorphism.lean#L101).

> Let `A` be the limit of a sequence of rings whose transition maps are surjective with locally
> nilpotent kernels. A monomorphism `f : T ⟶ Spec A` locally of finite type through which every
> `Spec Aₙ ⟶ Spec A` factors is an isomorphism.

```lean
theorem isIso_of_forall_spec_factors_of_isLimit (hc : IsLimit c)
    (hF : ∀ n : ℕ, Function.Surjective (F.map (homOfLE (Nat.le_succ n)).op).hom ∧
      RingHom.ker (F.map (homOfLE (Nat.le_succ n)).op).hom ≤ nilradical (F.obj (.op (n + 1))))
    {T : Scheme.{u}} (f : T ⟶ Spec c.pt) [Mono f] [LocallyOfFiniteType f]
    (hfac : ∀ n : ℕ, ∃ g : Spec (F.obj (.op n)) ⟶ T, g ≫ f = Spec.map (c.π.app (.op n))) :
    IsIso f
```

## Tag 0CTK, a theorem

[Tag 0CTK](https://stacks.math.columbia.edu/tag/0CTK) in the Stacks Project.

**`AlgebraicGeometry.GrothendieckExistence.ExistenceSituation.exists_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/GrothendieckExistenceTheorem.lean#L113).

> **[Stacks, Tag 0CTK], Grothendieck's existence theorem for flat modules.** In Situation
> [Stacks, Tag 0CTC] there is a finitely presented `𝒪_X`-module `ℱ`, flat over `A`, with support
> proper over `A`, such that `ℱₙ = ℱ ⊗_{𝒪_X} 𝒪_{Xₙ}` for all `n` compatibly with the maps `φₙ`.
> The derived categories in the proof are the standard ones; none appears in the statement.

```lean
theorem exists_algebraization :
    ∃ (F : S.X.left.Modules) (_ : F.IsFinitePresentation),
      IsFlatOver S.X.hom.toLRSHom.toShHom F ∧
      (∃ Z : Closeds S.X.left, (Z : Set S.X.left) = SheafOfModules.supp F ∧
        IsProperOver S.X.hom Z) ∧
      ∃ e : ∀ n : ℕ, (Scheme.Modules.pullback (S.closedImmersion n)).obj F ≅ S.F n,
        ∀ n : ℕ,
          (Scheme.Modules.pullbackComp (S.transitionScheme n) (S.closedImmersion (n + 1))).app F ≪≫
            (Scheme.Modules.pullbackCongr (S.transition_fst n)).app F ≪≫ e n =
          (Scheme.Modules.pullback (S.transitionScheme n)).mapIso (e (n + 1)) ≪≫ S.φ n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.28, Tag 0CTB](https://stacks.math.columbia.edu/tag/0CTB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
