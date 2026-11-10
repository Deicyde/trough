---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isBlowupAlong_isFlat_isFinitePresentation_strictTransformSpaceToBlowUp_of_isFiniteType, AlgebraicGeometry.Space.exists_admissibleBlowup_isFiniteLocallyFree_strictTransform, AlgebraicGeometry.Space.exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_of_isProper_unconditional, AlgebraicGeometry.Space.exists_isBlowupAlong_isOpenImmersion_strictTransformSpaceToBlowUp_unconditional, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_dominating_of_isProper, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_extending_section_of_isProper
statement: formalized
proof: formalized
---

# 76.39 Applications

Section 76.39 of the Stacks Project, [Tag 087D](https://stacks.math.columbia.edu/tag/087D). 6 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 087E, a lemma

[Tag 087E](https://stacks.math.columbia.edu/tag/087E) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_isBlowupAlong_isFlat_isFinitePresentation_strictTransformSpaceToBlowUp_of_isFiniteType`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFiniteTypeMorphismByBlowup.lean#L68), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFiniteTypeMorphismByBlowupTag.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFiniteTypeMorphismByBlowupTag.lean#L36) (StacksFrontier).

## Tag 0B4K, a lemma

[Tag 0B4K](https://stacks.math.columbia.edu/tag/0B4K) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_admissibleBlowup_isFiniteLocallyFree_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFiniteLocallyFreeAdmissibleBlowup.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFiniteLocallyFreeAdmissibleBlowup.lean#L63).

> Let `f : X ⟶ A` be a morphism of algebraic spaces over `S` and let `U ⊆ A` be an open
> subspace.  Assume that
> 1. `A` is quasi-compact and quasi-separated,
> 2. `U` is quasi-compact,
> 3. `f` is proper, and
> 4. `f⁻¹(U) ⟶ U` (the restriction `X ×_A U ⟶ U`) is finite locally free.
>
> Then there is a `U`-admissible blowup `b : A' ⟶ A` -- the blowup of `A` in a closed subspace `Z`
> of finite presentation whose points avoid those of `U` -- such that the strict transform
> `X' ⟶ A'` of `X` with respect to `b` is finite locally free.

```lean
theorem exists_admissibleBlowup_isFiniteLocallyFree_strictTransform
    {A X : AlgebraicSpaces B S hS} (f : X ⟶ A) (U : OpenSubspaces B S hS A.1)
    (hAqc : IsQuasiCompactSpace B S hS A.1)
    (hAqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal A.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hf : IsProper B S hS f.hom) (hflf : IsFiniteLocallyFree B S hS (restrictOverHom f U)) :
    ∃ (A' : AlgebraicSpaces B S hS) (b : A' ⟶ A) (Z : ClosedSubspaces B S hS A.1),
      IsFinitePresentation B S hS Z.1.ι ∧
        Disjoint (subspacePointSet B S hS A.1 U.1) (subspacePointSet B S hS A.1 Z.1) ∧
          IsBlowupAlong B S hS Z b ∧
            IsFiniteLocallyFree B S hS
              (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom))
```

## Tag 0GUW, a lemma

[Tag 0GUW](https://stacks.math.columbia.edu/tag/0GUW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_of_isProper_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperIsomorphismOverOpenBlowupUnconditional.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperIsomorphismOverOpenBlowupUnconditional.lean#L52).

> Let `f : X ⟶ A` be a morphism of algebraic spaces over `S` and let `U ⊆ A` be an open subspace.
> Assume that `A` is quasi-compact and quasi-separated, that `U` is quasi-compact, that `f` is proper
> and that `f⁻¹(U) ⟶ U` (the restriction `X ×_A U ⟶ U`) is an isomorphism. Then there is a
> `U`-admissible blowup `b : A' ⟶ A` -- the blowup of `A` in a closed subspace `Z` of finite
> presentation whose points avoid those of `U` -- such that the strict transform of `X` with
> respect to `b` maps isomorphically to `A'`.

```lean
theorem exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_of_isProper_unconditional
    {A X : AlgebraicSpaces B S hS} (f : X ⟶ A) (U : OpenSubspaces B S hS A.1)
    (hAqc : IsQuasiCompactSpace B S hS A.1)
    (hAqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal A.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hf : IsProper B S hS f.hom) (hiso : IsIso (pullback.snd f.hom U.1.ι)) :
    ∃ (A' : AlgebraicSpaces B S hS) (b : A' ⟶ A) (Z : ClosedSubspaces B S hS A.1),
      IsFinitePresentation B S hS Z.1.ι ∧
        Disjoint (subspacePointSet B S hS A.1 U.1) (subspacePointSet B S hS A.1 Z.1) ∧
          IsBlowupAlong B S hS Z b ∧
            IsIso (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)).hom
```

## Tag 087F, a lemma

[Tag 087F](https://stacks.math.columbia.edu/tag/087F) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isBlowupAlong_isOpenImmersion_strictTransformSpaceToBlowUp_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionAfterAdmissibleBlowupUnconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionAfterAdmissibleBlowupUnconditional.lean#L68). The attribute's comment: “corrected: f separated; as published the statement is false (the affine line with doubled origin over 𝐀¹, with U = 𝐀¹ minus the origin)”.

> **Stacks 087F, corrected.**  Let `f : X ⟶ A` be a morphism of algebraic spaces over `S` and
> let `U ⊆ A` be an open subspace.  Assume that `A` is quasi-compact and quasi-separated, that `U`
> is quasi-compact, that `f` is of finite type **and separated**, and that `f⁻¹(U) ⟶ U` is an
> isomorphism.  Then there is a `U`-admissible blowup `b : A' ⟶ A`, with centre `Z`, such that
> `b⁻¹(U)` is scheme-theoretically dense in `A'` and the strict transform of `X` is an open
> immersion into `A'`.
>
> Without separatedness the statement is false; see the module documentation.

```lean
theorem exists_isBlowupAlong_isOpenImmersion_strictTransformSpaceToBlowUp_unconditional
    (hZ : B.Contains (⊤_ Scheme.{u})) {A X : AlgebraicSpaces B S hS} (f : X ⟶ A)
    (U : OpenSubspaces B S hS A.1)
    (hAqc : IsQuasiCompactSpace B S hS A.1) (hAqs : IsAbsolutelyQuasiSeparated B S hS hZ A.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hft : IsFiniteType B S hS f.hom) (hsep : IsSeparated B S hS f.hom)
    (hiso : IsIso (pullback.snd f.hom U.1.ι)) :
    ∃ (A' : AlgebraicSpaces B S hS) (b : A' ⟶ A) (Z : ClosedSubspaces B S hS A.1),
      IsFinitePresentation B S hS Z.1.ι ∧
        Disjoint (subspacePointSet B S hS A.1 U.1) (subspacePointSet B S hS A.1 Z.1) ∧
          IsBlowupAlong B S hS Z b ∧
            IsSchemeTheoreticallyDense B S hS (U.1.preimage b.hom) ∧
              IsOpenImmersion B S hS
                (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)).hom
```

## Tag 087G, a lemma

[Tag 087G](https://stacks.math.columbia.edu/tag/087G) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_dominating_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/QcqsBase.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/QcqsBase.lean#L92).

> **Stacks 087G.** Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S` and let `U ⊆ Y` be an open subspace. Assume that `Y` is quasi-compact and quasi-separated,
> that `U` is quasi-compact, that `f` is proper and that `f⁻¹(U) ⟶ U` is an isomorphism. Then
> there is a `U`-admissible blowup `b : Y' ⟶ Y` which dominates `X`, that is, there is a
> factorization `Y' ⟶ X ⟶ Y` of the blowup morphism.
>
> Being a `U`-admissible blowup is Stacks 086B, `AlgebraicGeometry.Space.IsAdmissibleBlowup`;
> quasi-separatedness of `Y` is absolute quasi-separatedness; and `f⁻¹(U) ⟶ U` is the projection
> `X ×_Y U ⟶ U`.

```lean
theorem exists_isAdmissibleBlowup_dominating_of_isProper {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.1)
    (U : OpenSubspaces B S hS Y.1) (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hf : IsProper B S hS f.hom) (hfU : IsIso (pullback.snd f.hom U.1.ι)) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y), IsAdmissibleBlowup B S hS U b ∧
      ∃ g : Y' ⟶ X, g ≫ f = b
```

## Tag 0CPI, a lemma

[Tag 0CPI](https://stacks.math.columbia.edu/tag/0CPI) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_extending_section_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/SectionExtension.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/SectionExtension.lean#L112).

> **Stacks 0CPI.** Let `S` be a scheme, let `X`, `Y` be algebraic spaces over `S`, let
> `U ⊆ W ⊆ Y` be open subspaces, and let `f : X ⟶ W` and `s : U ⟶ X` be morphisms with
> `f ∘ s = id_U`. Assume that `f` is proper, that `Y` is quasi-compact and quasi-separated, and that
> `U` and `W` are quasi-compact. Then there are a `U`-admissible blowup `b : Y' ⟶ Y` and a morphism
> `s' : b⁻¹(W) ⟶ X` extending `s` with `f ∘ s' = b|_{b⁻¹(W)}`.
>
> Here `W` is the algebraic space `AlgebraicGeometry.Space.openSubspace B S hS Y W`, so
> `f ∘ s = id_U` reads `s ≫ f = U ↪ W`; quasi-separatedness of `Y` is absolute quasi-separatedness;
> being a `U`-admissible blowup is Stacks 086B, `AlgebraicGeometry.Space.IsAdmissibleBlowup`;
> `b⁻¹(W)` is the inverse image subfunctor `W.1.preimage b.hom`, and `b|_{b⁻¹(W)}` is
> `W.1.fromPreimage b.hom`; and `s'` *extends* `s` in that its restriction to `b⁻¹(U) ⊆ b⁻¹(W)` is
> `s ∘ b|_{b⁻¹(U)}` (the morphism `b⁻¹(U) ⟶ U` being an isomorphism, as `b` is `U`-admissible).

```lean
theorem exists_isAdmissibleBlowup_extending_section_of_isProper {X Y : AlgebraicSpaces B S hS}
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.1)
    (U W : OpenSubspaces B S hS Y.1) (hUW : U.1 ≤ W.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hWqc : IsQuasiCompactSpace B S hS W.1.toFunctor)
    (f : X ⟶ openSubspace B S hS Y W) (hf : IsProper B S hS f.hom)
    (s : U.1.toFunctor ⟶ X.1) (hs : s ≫ f.hom = Subfunctor.homOfLe hUW) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y), IsAdmissibleBlowup B S hS U b ∧
      ∃ s' : (W.1.preimage b.hom).toFunctor ⟶ X.1, s' ≫ f.hom = W.1.fromPreimage b.hom ∧
        Subfunctor.homOfLe (fun T _ hx => hUW T hx :
          U.1.preimage b.hom ≤ W.1.preimage b.hom) ≫ s' = U.1.fromPreimage b.hom ≫ s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.39, Tag 087D](https://stacks.math.columbia.edu/tag/087D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
