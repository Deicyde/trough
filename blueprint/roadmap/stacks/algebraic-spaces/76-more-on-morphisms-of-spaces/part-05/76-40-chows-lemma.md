---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isOpenImmersion_of_isOpenImmersion_unconditional, AlgebraicGeometry.Space.hasChowBlowupDiagram_of_isFiniteType_of_isSeparated, AlgebraicGeometry.Space.exists_denseOpen_hasChowBlowupDiagram, AlgebraicGeometry.Space.exists_isRelativelyAmple_of_isAdmissibleBlowup_of_projectiveSpaceImmersion, AlgebraicGeometry.Space.C1573.exists_isAdmissibleBlowup_isImmersion_projectiveSpace
statement: formalized
proof: formalized
---

# 76.40 Chow's lemma

Section 76.40 of the Stacks Project, [Tag 088P](https://stacks.math.columbia.edu/tag/088P). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 088Q, a lemma

[Tag 088Q](https://stacks.math.columbia.edu/tag/088Q) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isOpenImmersion_of_isOpenImmersion_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CommonAdmissibleBlowupUnconditional.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CommonAdmissibleBlowupUnconditional.lean#L55).

> **Stacks 088Q.** Let `Y` be a quasi-compact and quasi-separated algebraic space over `S` and
> let `j₁ : U ⟶ X₁`, `j₂ : U ⟶ X₂` be open immersions of algebraic spaces over `Y`, with `U`,
> `X₁` and `X₂` separated and of finite type over `Y`. There is a commutative diagram
> `X₁ ⟵ X₁' ⟶ X ⟵ X₂' ⟶ X₂` under `U` and over `Y`, in which `b_k : X_k' ⟶ X_k` is a
> `U`-admissible blowup (`U` being the open subspace `j_k(U)` of `X_k`), `i_k : X_k' ⟶ X` is an
> open immersion, and `X` is separated and of finite type over `Y`. Moreover the morphisms
> `u_k : U ⟶ X_k'` of the diagram are open immersions.

```lean
theorem exists_isAdmissibleBlowup_isOpenImmersion_of_isOpenImmersion_unconditional
    {Y U X₁ X₂ : AlgebraicSpaces B S hS}
    (f₁ : X₁ ⟶ Y) (f₂ : X₂ ⟶ Y) (j₁ : U ⟶ X₁) (j₂ : U ⟶ X₂)
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.1)
    (hj₁ : IsOpenImmersion B S hS j₁.hom) (hj₂ : IsOpenImmersion B S hS j₂.hom)
    (hj : j₁ ≫ f₁ = j₂ ≫ f₂)
    (hUft : IsFiniteType B S hS (j₁ ≫ f₁).hom) (hUsep : IsSeparated B S hS (j₁ ≫ f₁).hom)
    (hX₁ft : IsFiniteType B S hS f₁.hom) (hX₁sep : IsSeparated B S hS f₁.hom)
    (hX₂ft : IsFiniteType B S hS f₂.hom) (hX₂sep : IsSeparated B S hS f₂.hom) :
    ∃ (X₁' X₂' X : AlgebraicSpaces B S hS) (b₁ : X₁' ⟶ X₁) (b₂ : X₂' ⟶ X₂)
      (i₁ : X₁' ⟶ X) (i₂ : X₂' ⟶ X) (g : X ⟶ Y) (u₁ : U ⟶ X₁') (u₂ : U ⟶ X₂'),
      IsAdmissibleBlowup B S hS ⟨Subfunctor.range j₁.hom, @isOpenSubspace_range_of_open B S hS
        _ _ j₁.hom (mono_of_isOpenImmersion B S hS _ hj₁) U.2 hj₁⟩ b₁ ∧
      IsAdmissibleBlowup B S hS ⟨Subfunctor.range j₂.hom, @isOpenSubspace_range_of_open B S hS
        _ _ j₂.hom (mono_of_isOpenImmersion B S hS _ hj₂) U.2 hj₂⟩ b₂ ∧
      IsOpenImmersion B S hS i₁.hom ∧ IsOpenImmersion B S hS i₂.hom ∧
      IsSeparated B S hS g.hom ∧ IsFiniteType B S hS g.hom ∧
      i₁ ≫ g = b₁ ≫ f₁ ∧ i₂ ≫ g = b₂ ≫ f₂ ∧
      u₁ ≫ b₁ = j₁ ∧ u₂ ≫ b₂ = j₂ ∧ u₁ ≫ i₁ = u₂ ≫ i₂ ∧
      IsOpenImmersion B S hS u₁.hom ∧ IsOpenImmersion B S hS u₂.hom
```

## Tag 088R, a lemma

[Tag 088R](https://stacks.math.columbia.edu/tag/088R) in the Stacks Project.

**`AlgebraicGeometry.Space.hasChowBlowupDiagram_of_isFiniteType_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChowBlowupDiagramExistence.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChowBlowupDiagramExistence.lean#L88).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and let `U ⊆ X` be an open
> subspace. Assume that `U` is quasi-compact, that `Y` is quasi-compact and quasi-separated, that
> `i : U ⟶ ℙⁿ_Y` is an immersion over `Y`, and that `f` is of finite type and separated. Then there
> is a commutative diagram
> ```
>         U
>      ↙  ↓  ↘  ↘
>    X ← X' → Z' → Z
>      ↘  ↓  ↙    ↓
>         Y  ←  ℙⁿ_Y
> ```
> in which the arrows with source `U` are open immersions, `X' ⟶ X` is a `U`-admissible blowup,
> `X' ⟶ Z'` is an open immersion and `Z' ⟶ Y` is proper and representable; more precisely
> `Z' ⟶ Z` is a `U`-admissible blowup and `Z ⟶ ℙⁿ_Y` is a closed immersion, through which `i`
> factors (`AlgebraicGeometry.Space.HasChowBlowupDiagram`).

```lean
theorem hasChowBlowupDiagram_of_isFiniteType_of_isSeparated
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (U : Subfunctor X) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (n : ℕ) (i : U.toFunctor ⟶ projectiveSpaceOver B S hS Y n) (hi : IsImmersion B S hS i)
    (hiY : i ≫ prod.fst = U.ι ≫ f)
    (hft : IsFiniteType B S hS f) (hsep : IsSeparated B S hS f) :
    HasChowBlowupDiagram B S hS hX f U hU n i
```

## Tag 088S, a lemma

[Tag 088S](https://stacks.math.columbia.edu/tag/088S) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseOpen_hasChowBlowupDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChowBlowupDiagramNoetherian.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChowBlowupDiagramNoetherian.lean#L62).

> **Stacks 088S.**  Let `f : X ⟶ Y` be a separated morphism of finite type of algebraic spaces
> over `S`, with `Y` Noetherian.  Then there are a dense open subspace `U ⊆ X`, an integer `n` and
> an immersion `i : U ⟶ ℙⁿ_Y` over `Y` for which the diagram of Stacks 088S exists
> (`AlgebraicGeometry.Space.HasChowBlowupDiagram`): a `U`-admissible blowup `X' ⟶ X`, an open
> immersion `X' ⟶ Z'`, a proper representable `Z' ⟶ Y`, a `U`-admissible blowup `Z' ⟶ Z` and a
> closed immersion `Z ⟶ ℙⁿ_Y`, with the arrows out of `U` open immersions and everything
> commuting.

```lean
theorem exists_denseOpen_hasChowBlowupDiagram (hTop : B.Contains (⊤_ Scheme.{u}))
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hsep : IsSeparated B S hS f) (hft : IsFiniteType B S hS f)
    (hYnoeth : IsNoetherian B S hS hTop Y) :
    ∃ (U : Subfunctor X) (hU : IsOpenSubspace B S hS U),
      (letI : TopologicalSpace (points B S hS X) := pointTopology B S hS X;
        DenseRange (pointsMap B S hS U.toFunctor U.ι)) ∧
      ∃ (n : ℕ) (i : U.toFunctor ⟶ projectiveSpaceOver B S hS Y n),
        IsImmersion B S hS i ∧ i ≫ prod.fst = U.ι ≫ f ∧
          HasChowBlowupDiagram B S hS hX f U hU n i
```

## Tag 088T, a remark

[Tag 088T](https://stacks.math.columbia.edu/tag/088T) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isRelativelyAmple_of_isAdmissibleBlowup_of_projectiveSpaceImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupProjectiveRelativeAmple.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupProjectiveRelativeAmple.lean#L69).

> **Stacks 088T.** Let `Y` be a quasi-compact algebraic space, `i : Z ⟶ ℙⁿ_Y` a closed
> immersion, `U ⊆ Z` an open subspace and `b : Z' ⟶ Z` a `U`-admissible blowup, as in Lemmas 088R
> and 088S, and let `g = b ≫ (Z ⟶ ℙⁿ_Y ⟶ Y)`. Then
>
> 1. `g` is a composition of projective morphisms: `b` is proper and representable and carries a
>    `b`-ample invertible module, and `Z ⟶ Y` is proper and representable and carries an ample
>    invertible module relative to it;
> 2. there exists a `g`-ample invertible `𝒪_{Z'}`-module.

```lean
theorem exists_isRelativelyAmple_of_isAdmissibleBlowup_of_projectiveSpaceImmersion
    {Y Z Z' : AlgebraicSpaces B S hS} (hY : IsQuasiCompactSpace B S hS Y.1) {n : ℕ}
    {hP : B.Contains (projectiveSpaceOver n S)} (D : ProjectiveSpaceImmersion B S hS n hP Z Y)
    (U : OpenSubspaces B S hS Z.1) {b : Z' ⟶ Z} (hb : IsAdmissibleBlowup B S hS U b) :
    (IsProper B S hS b.hom ∧ yoneda.relativelyRepresentable b.hom ∧
        ∃ L : Modules.{u, u} B S hS Z'.1 Z'.2,
          Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS Z'.1)
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS Z'.1 Z'.2).O)).property L ∧
          IsRelativelyAmple B S hS b L) ∧
      (IsProper B S hS D.hom.hom ∧ yoneda.relativelyRepresentable D.hom.hom ∧
        ∃ M : Modules.{u, u} B S hS Z.1 Z.2,
          Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS Z.1)
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS Z.1 Z.2).O)).property M ∧
          IsRelativelyAmple B S hS D.hom M) ∧
      ∃ L : Modules.{u, u} B S hS Z'.1 Z'.2,
        Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS Z'.1)
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS Z'.1 Z'.2).O)).property L ∧
        IsRelativelyAmple B S hS (b ≫ D.hom) L
```

## Tag 088U, a lemma

[Tag 088U](https://stacks.math.columbia.edu/tag/088U) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.exists_isAdmissibleBlowup_isImmersion_projectiveSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/ChowLemma/Main.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/Main.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/Main.lean#L38) (StacksFrontier).
- [`AlgebraicGeometry.Space.C1573.exists_isAdmissibleBlowup_isImmersion_projectiveSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/ChowLemma/Main.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ChowLemmaTag.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChowLemmaTag.lean#L25) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.40, Tag 088P](https://stacks.math.columbia.edu/tag/088P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
