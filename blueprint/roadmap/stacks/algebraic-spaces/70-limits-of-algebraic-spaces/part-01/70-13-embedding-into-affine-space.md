---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver, AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver_of_isRegular, AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.exists_not_isAbsolutelyLocallySeparated_not_isImmersion', AlgebraicGeometry.Space.exists_denseOpen_isImmersion_affineSpaceOver
statement: formalized
proof: formalized
---

# 70.13 Embedding into affine space

Section 70.13 of the Stacks Project, [Tag 088K](https://stacks.math.columbia.edu/tag/088K). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 088L, a lemma

[Tag 088L](https://stacks.math.columbia.edu/tag/088L) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean, line 1020](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean#L1020). The attribute's comment: “with the cutoff-cofinality side condition on the sections of `U` that the directed limit in the proof requires; quasi-separatedness of `X` is not needed”.

> **Stacks 088L.**  Let `f : U ⟶ X` be a morphism of algebraic spaces over `S` with `U` an
> affine scheme, `f` locally of finite type and `X` locally separated.  Then `U` admits an
> immersion into affine `n`-space over `X`, over `X`.
>
> The hypothesis `hcard` bounds the ring of sections of `U` by the cofinality of the site's
> cutoff; it is not part of Stacks 088L, but is the condition under which the directed limit
> used in the proof is an algebraic space in this development, inherited from Stacks 07SF and
> Stacks 0828.  See `exists_isImmersion_affineSpaceOver_of_isRegular` for the form in which it
> disappears, and the implementation notes of this file for why it cannot be removed outright.
>
> Quasi-separatedness of `X`, which Stacks 088L also assumes, is not needed: this development's
> Stacks 0828, part (2) does not assume it of the stages.

```lean
theorem exists_isImmersion_affineSpaceOver (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u})) (U : BigFppfOver B S hS)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : yoneda.obj U ⟶ X)
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hX : IsAlgebraicSpace B S hS X)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hls : IsAbsolutelyLocallySeparated B S hS hZ X)
    (hcard : #Γ((BigFppfOver.toScheme B S hS).obj U, ⊤) < B.cutoff.ord.cof) :
    ∃ (n : ℕ) (j : yoneda.obj U ⟶ affineSpaceOver B S hS X n),
      j ≫ prod.fst = f ∧ IsImmersion B S hS j
```

**`AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean, line 1069](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean#L1069). The attribute's comment: “verbatim, over a big fppf site whose size cutoff is a regular cardinal”.

> **Stacks 088L** over a big fppf site whose size cutoff is a regular cardinal: an affine
> scheme locally of finite type over a locally separated algebraic space admits an immersion
> into affine `n`-space over that space.
>
> Regularity of the cutoff discharges the cardinality side condition of
> `exists_isImmersion_affineSpaceOver` for every `U`: the sections of an affine object of the
> site are bounded by its size, which is below the cutoff, which is its own cofinality.

```lean
theorem exists_isImmersion_affineSpaceOver_of_isRegular (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u})) (hreg : B.cutoff.IsRegular)
    (U : BigFppfOver B S hS) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : yoneda.obj U ⟶ X)
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hX : IsAlgebraicSpace B S hS X)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hls : IsAbsolutelyLocallySeparated B S hS hZ X) :
    ∃ (n : ℕ) (j : yoneda.obj U ⟶ affineSpaceOver B S hS X n),
      j ≫ prod.fst = f ∧ IsImmersion B S hS j
```

**`AlgebraicGeometry.Space.exists_isImmersion_affineSpaceOver_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpace.lean#L1125).

> **Stacks 088L.**  Let `f : U ⟶ X` be a morphism of algebraic spaces over `S` with `U` an
> affine scheme, `f` locally of finite type, and `X` quasi-separated and locally separated.
> Then there is an immersion `U ⟶ 𝔸ⁿ_X` over `X`.
>
> Writing `U = Spec A` with `A` the filtered union of its finite type `ℤ`-subalgebras `Aᵢ`, the
> graph `U ⟶ X ⨯ U` is an immersion because `X` is locally separated (Stacks 03KO), and
> `X ⨯ U` is the directed limit of the stages `X ⨯ Spec Aᵢ`, which have affine transition
> morphisms and are quasi-separated because `X` is.  Stacks 0828, part (2), which places no bound
> on the index set, then makes `U ⟶ X ⨯ Spec Aᵢ` an immersion for some `i`, and `Spec Aᵢ` is a
> closed subscheme of affine space over `ℤ`.

```lean
theorem exists_isImmersion_affineSpaceOver_of_isAbsolutelyQuasiSeparated (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (U : BigFppfOver B S hS)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : yoneda.obj U ⟶ X)
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hX : IsAlgebraicSpace B S hS X)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X)
    (hls : IsAbsolutelyLocallySeparated B S hS B.contains_terminal X) :
    ∃ (n : ℕ) (j : yoneda.obj U ⟶ affineSpaceOver B S hS X n),
      j ≫ prod.fst = f ∧ IsImmersion B S hS j
```

## Tag 088M, a remark

[Tag 088M](https://stacks.math.columbia.edu/tag/088M) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_not_isAbsolutelyLocallySeparated_not_isImmersion'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpaceSharpUnconditional.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EmbeddingIntoAffineSpaceSharpUnconditional.lean#L64). The attribute's comment: “the failure of 088L without local separatedness; the question the remark raises about quasi-separatedness is open and is not a theorem”.

> **Stacks 088M**: the hypothesis of Stacks 088L that `X` be locally separated cannot be
> dropped.
>
> Over a field in which two is invertible there is a finite type morphism `f : Y ⟶ X` of
> algebraic spaces with `Y` an affine scheme and `X` quasi-separated — so every hypothesis
> of Stacks 088L except local separatedness holds — such that `X` is *not* locally separated
> and `Y` admits no immersion over `X` into relative affine `n`-space over `X`, for any `n`.
>
> The witness is the one of Stacks 088W, the chart `𝔸¹_k ⟶ 𝔸¹_k/R` of Stacks 02Z1, and the
> failure of local separatedness is the corresponding half of Stacks 02Z1.
>
> The remark also raises the question whether Stacks 088L holds without quasi-separatedness.
> That is an open question, not a result, and it is not stated here.

```lean
theorem exists_not_isAbsolutelyLocallySeparated_not_isImmersion'
    (k : Type u) [Field k] (hchar : (2 : k) ≠ 0)
    (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k))) (hZ : B.Contains (⊤_ Scheme.{u}))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ∃ (Y : BigFppfOver B (Spec (.of k)) hS)
      (X : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u)
      (f : yoneda.obj Y ⟶ X),
      IsAffine ((BigFppfOver.toScheme B (Spec (.of k)) hS).obj Y) ∧
      IsAlgebraicSpace B (Spec (.of k)) hS X ∧
      IsFiniteType B (Spec (.of k)) hS f ∧
      IsAbsolutelyQuasiSeparated B (Spec (.of k)) hS hZ X ∧
      ¬ IsAbsolutelyLocallySeparated B (Spec (.of k)) hS hZ X ∧
      ∀ (n : ℕ) (j : yoneda.obj Y ⟶ affineSpaceOver B (Spec (.of k)) hS X n),
        j ≫ prod.fst = f → ¬ IsImmersion B (Spec (.of k)) hS j
```

## Tag 088N, a lemma

[Tag 088N](https://stacks.math.columbia.edu/tag/088N) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseOpen_isImmersion_affineSpaceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DenseOpenEmbeddingIntoAffineSpace/ComponentGlueing.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DenseOpenEmbeddingIntoAffineSpace/ComponentGlueing.lean#L348).

> **Stacks 088N.**  Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` with `X`
> Noetherian and `f` of finite presentation.  Then `Y` has a dense open subspace which admits,
> over `X`, an immersion into relative affine `n`-space over `X`.

```lean
public theorem exists_denseOpen_isImmersion_affineSpaceOver
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {Y X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : Y ⟶ X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hXN : AlgebraicGeometry.Space.IsNoetherian B S hS hZ X)
    (hf : AlgebraicGeometry.Space.IsFinitePresentation B S hS f) :
    ∃ (V : Subfunctor Y),
      AlgebraicGeometry.Space.IsOpenSubspace B S hS V ∧
      (letI : TopologicalSpace (AlgebraicGeometry.Space.points B S hS Y) :=
          AlgebraicGeometry.Space.pointTopology B S hS Y;
        DenseRange (AlgebraicGeometry.Space.pointsMap B S hS V.toFunctor V.ι)) ∧
      ∃ (n : ℕ) (i : V.toFunctor ⟶ AlgebraicGeometry.Space.affineSpaceOver B S hS X n),
        AlgebraicGeometry.Space.IsImmersion B S hS i ∧
          i ≫ prod.fst = V.ι ≫ f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.13, Tag 088K](https://stacks.math.columbia.edu/tag/088K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
