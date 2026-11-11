---
declaration: section
origin: cited
lean: AlgebraicGeometry.FreeAtGenericPointsSituation.isImmersion_representableBy_fittingRankStratum, AlgebraicGeometry.FreeAtGenericPointsSituation.finitePresentation_hom_of_representableBy, AlgebraicGeometry.FlatDimensionSituation.isFlat_etaleChart_and_iff_of_relativeAssassin_subset, AlgebraicGeometry.FreeAtGenericPointsSituation.flatDimensionFunctor_iso_coproduct_freeAtGenericPointsFunctor, AlgebraicGeometry.isFlatOverInDimensionsGE_iff_forall_exists_freeAtPointOfRank, AlgebraicGeometry.FlatDimensionSituation.exists_mono_finitePresentation_representableBy, AlgebraicGeometry.FlatDimensionSituation.exists_mono_finitePresentation_representableBy_of_isPure, AlgebraicGeometry.exists_mono_finitePresentation_representableBy_of_isPureRelative
statement: formalized
proof: formalized
---

# 38.27 Universal flattening

Section 38.27 of the Stacks Project, [Tag 05PS](https://stacks.math.columbia.edu/tag/05PS). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05UC, a lemma

[Tag 05UC](https://stacks.math.columbia.edu/tag/05UC) in the Stacks Project.

**`AlgebraicGeometry.FreeAtGenericPointsSituation.isImmersion_representableBy_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsImmersion.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsImmersion.lean#L95). The attribute's comment: “representability of H\_p by a locally closed immersion”.

> **Stacks Project, Tag 05UC.** In Situation 05MP, for each `p ≥ 0` the functor `H_p` of
> 05MR is representable by a locally closed immersion `S_p ⟶ S`.

```lean
theorem isImmersion_representableBy_fittingRankStratum :
    ∃ W : Over D.S, IsImmersion W.hom ∧
      Nonempty ((D.freeAtGenericPointsFunctor p).RepresentableBy W)
```

**`AlgebraicGeometry.FreeAtGenericPointsSituation.finitePresentation_hom_of_representableBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsImmersion.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsImmersion.lean#L113). The attribute's comment: “finite presentation of S\_p ⟶ S when the module is of finite presentation”.

> **Stacks Project, Tag 05UC.** In Situation 05MP, if `ℱ` is of finite presentation then
> `S_p ⟶ S` is of finite presentation.
>
> The assertion is proved for an arbitrary morphism representing the generic-rank functor, which
> is legitimate because any two representatives are isomorphic over the base.

```lean
theorem finitePresentation_hom_of_representableBy [D.F.IsFinitePresentation]
    {W : Over D.S} (e : (D.freeAtGenericPointsFunctor p).RepresentableBy W) :
    FinitePresentation W.hom
```

## Tag 05UD, a lemma

[Tag 05UD](https://stacks.math.columbia.edu/tag/05UD) in the Stacks Project.

**`AlgebraicGeometry.FlatDimensionSituation.isFlat_etaleChart_and_iff_of_relativeAssassin_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionEtaleComparison.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionEtaleComparison.lean#L373).

> **Stacks Project, Tag 05UD.** In Situation 05MT, let `h : X' ⟶ X` be étale and let `F'_n` be
> the functor of Stacks 05MU for `(f ∘ h, h^* F)`. Then `F_n` is a subfunctor of `F'_n`, and if
> `h(X')` contains `Ass_{X/S}(F)` then `F_n = F'_n`.
>
> Both functors are subterminal, so the first assertion is the implication between the two
> conditions after every base change `T ⟶ S`, and the second is their equivalence.

```lean
theorem isFlat_etaleChart_and_iff_of_relativeAssassin_subset {X' : Scheme.{u}} (h : X' ⟶ D.X)
    [Etale h] :
    (∀ T : Over D.S, D.IsFlatInDimensionsGEAfterBaseChange T →
      (D.etaleChart h).IsFlatInDimensionsGEAfterBaseChange T) ∧
    (Stacks.Divisors.relativeAssassin D.f D.F ⊆ Set.range h → ∀ T : Over D.S,
      D.IsFlatInDimensionsGEAfterBaseChange T ↔
        (D.etaleChart h).IsFlatInDimensionsGEAfterBaseChange T)
```

## Tag 05UE, a lemma

[Tag 05UE](https://stacks.math.columbia.edu/tag/05UE) in the Stacks Project.

**`AlgebraicGeometry.FreeAtGenericPointsSituation.flatDimensionFunctor_iso_coproduct_freeAtGenericPointsFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/GenericRankCoproduct.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/GenericRankCoproduct.lean#L291).

> Let `f : X ⟶ S` be a smooth morphism of affine schemes with geometrically irreducible fibres
> of dimension `d` and let `F` be a quasi-coherent `𝒪_X`-module of finite presentation. Then
> there is a `c ≥ 0` with
> ```
> F_d = ∐_{p = 0, …, c} H_p
> ```
> where `F_d` is the functor of flatness in dimensions `≥ d` of Stacks 05MT and `H_p` is the
> functor of Stacks 05MP, the coproduct being taken in Zariski sheaves over `S`.
>
> The comparison map out of the pointwise disjoint union is locally bijective, hence becomes an
> isomorphism after sheafification, and sheafification preserves coproducts.
>
> Sheafifying the left-hand side too is not a weakening: `F_d` is an fpqc sheaf by Stacks 05MV,
> a fortiori a Zariski sheaf, so it is isomorphic to its own sheafification. It is written
> sheafified here only so that the statement takes no input from that tag.

```lean
theorem flatDimensionFunctor_iso_coproduct_freeAtGenericPointsFunctor [IsAffine D.X]
    [IsAffine D.S] [D.F.IsFinitePresentation] {d : ℕ} (hd : RelativeDimension D.f d) :
    ∃ c : ℕ, Nonempty
      ((presheafToSheaf (Scheme.zariskiTopology.over D.S) (Type (u + 1))).obj
          ((D.toFlatDimensionSituation d).flatDimensionFunctor ⋙ uliftFunctor.{u + 1}) ≅
        ∐ fun p : Fin (c + 1) ↦
          (presheafToSheaf (Scheme.zariskiTopology.over D.S) (Type (u + 1))).obj
            (D.freeAtGenericPointsFunctor p.val ⋙ uliftFunctor.{u + 1}))
```

**`AlgebraicGeometry.isFlatOverInDimensionsGE_iff_forall_exists_freeAtPointOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/GenericRankDecomposition.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/GenericRankDecomposition.lean#L248). The attribute's comment: “F\_d is the union of the H\_p”.

> **Stacks Project, Tag 05UE.** Let `f : X ⟶ S` be a smooth morphism of affine schemes with
> geometrically irreducible fibres of dimension `d` and let `F` be a quasi-coherent `𝒪_X`-module
> of finite presentation. Then `F` is flat over `S` in dimensions `≥ d` if and only if `F` is
> free of some finite rank on a neighbourhood of the generic point of every fibre.
>
> This is the decomposition `F_d = ∐_p H_p` of the source read on sections: `H_p` of Stacks 05MP
> is freeness of the fixed rank `p` near every fibre's generic point, and the right hand side is
> the union of the `H_p`. Since every hypothesis is stable under base change, the equivalence over
> `S` carries the same equivalence over every scheme `T` over `S`.

```lean
theorem isFlatOverInDimensionsGE_iff_forall_exists_freeAtPointOfRank [IsAffine X] [IsAffine S]
    [Smooth f] (hirr : ∀ s : S, GeometricallyIrreducible (f.fiberToSpecResidueField s)) {d : ℕ}
    (hd : RelativeDimension f d) (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    [F.IsFinitePresentation] :
    IsFlatOverInDimensionsGE f F d ↔
      ∀ (s : S) (ξ : f.fiber s), IsGenericPoint ξ (Set.univ : Set (f.fiber s)) →
        ∃ r : ℕ, FreeAtPointOfRank F (f.fiberι s ξ) r
```

## Tag 05UF, a lemma

[Tag 05UF](https://stacks.math.columbia.edu/tag/05UF) in the Stacks Project.

**`AlgebraicGeometry.FlatDimensionSituation.exists_mono_finitePresentation_representableBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FlatDimensionFunctorRepresentability.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FlatDimensionFunctorRepresentability.lean#L344).

> **Stacks Project, Tag 05UF.** In Situation 05MT, let `s` be a point of `S` and let `d = n` be
> the bound of the situation. Assume that
>
> 1. there exists a complete dévissage of `F/X/S` over `s`,
> 2. `X` is of finite presentation over `S`,
> 3. `F` is an `𝒪_X`-module of finite presentation, and
> 4. `F` is flat over `S` in dimensions `≥ d + 1`.
>
> Then, after replacing `S` by an open neighbourhood `U` of `s`, the functor `F_d` of Stacks 05MU
> is representable by a monomorphism `Z_d ⟶ U` of finite presentation.
>
> Hypothesis (1) is the source's own: the existence of a complete dévissage is assumed by Tag
> 05UF, and is produced étale locally (Tag 05HU) only in the proof of Tag 05UG.

```lean
theorem exists_mono_finitePresentation_representableBy (s : D.S)
    (hdev : Nonempty (CompleteDevissage D.f D.F s)) (hf : FinitePresentation D.f)
    [D.F.IsFinitePresentation] (h : IsFlatOverInDimensionsGE D.f D.F (D.n + 1)) :
    ∃ U : D.S.Opens, s ∈ U ∧ ∃ Z : Over U.toScheme,
      Mono Z.hom ∧ FinitePresentation Z.hom ∧
        Nonempty ((D.openFlatDimensionFunctor U).RepresentableBy Z)
```

## Tag 05UG, a theorem

[Tag 05UG](https://stacks.math.columbia.edu/tag/05UG) in the Stacks Project.

**`AlgebraicGeometry.FlatDimensionSituation.exists_mono_finitePresentation_representableBy_of_isPure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FlatDimensionFunctorPure.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FlatDimensionFunctorPure.lean#L432).

> **Stacks Project, Tag 05UG.** In Situation 05MT, assume moreover that `f` is of finite
> presentation, that `F` is an `𝒪_X`-module of finite presentation, and that `F` is pure relative
> to `S`. Then `F_n` is representable by a monomorphism `Z_n ⟶ S` of finite presentation.
>
> `f` of finite presentation is spelled out as locally of finite presentation, quasi-compact and
> quasi-separated.

```lean
theorem exists_mono_finitePresentation_representableBy_of_isPure [LocallyOfFinitePresentation D.f]
    [QuasiCompact D.f] [QuasiSeparated D.f] [D.F.IsFinitePresentation]
    (hpure : IsPureRelative D.f D.F) :
    ∃ Z : Over D.S, Mono Z.hom ∧ FinitePresentation Z.hom ∧
      Nonempty (D.flatDimensionFunctor.RepresentableBy Z)
```

## Tag 05UH, a lemma

[Tag 05UH](https://stacks.math.columbia.edu/tag/05UH) in the Stacks Project.

**`AlgebraicGeometry.exists_mono_finitePresentation_representableBy_of_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean#L79). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 05UH, part (1).** Let `f : X ⟶ S` be of finite
> presentation and let `F` be an `𝒪_X`-module of finite presentation which is pure relative to
> `S`. Then the universal flattening `Z ⟶ S` of `F` exists and is a monomorphism of finite
> presentation.

```lean
theorem exists_mono_finitePresentation_representableBy_of_isPureRelative
    {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] [F.IsFinitePresentation]
    (hpure : IsPureRelative f F) :
    ∃ Z : Over S, Mono Z.hom ∧ FinitePresentation Z.hom ∧
      Nonempty (Functor.RepresentableBy
        ({ S := S, X := X, f := f, F := F, isQuasicoherent := ‹F.IsQuasicoherent› } :
          FlatnessSituation.{u}).flatFunctor Z)
```

**`AlgebraicGeometry.exists_mono_finitePresentation_representableBy_of_isSchemePureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean#L100). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 05UH, part (2).** Let `f : X ⟶ S` be of finite
> presentation and let `X` be pure relative to `S`. Then the universal flattening `Z ⟶ S` of `X`
> exists and is a monomorphism of finite presentation.

```lean
theorem exists_mono_finitePresentation_representableBy_of_isSchemePureRelative
    {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (hpure : IsSchemePureRelative f) :
    ∃ Z : Over S, Mono Z.hom ∧ FinitePresentation Z.hom ∧
      Nonempty ((structureSheafFlatnessSituation f).flatFunctor.RepresentableBy Z)
```

**`AlgebraicGeometry.exists_mono_finitePresentation_representableBy_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean#L115). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 05UH, part (3).** Let `f : X ⟶ S` be proper
> and of finite presentation and let `F` be an `𝒪_X`-module of finite presentation. Then the
> universal flattening `Z ⟶ S` of `F` exists and is a monomorphism of finite presentation.

```lean
theorem exists_mono_finitePresentation_representableBy_of_isProper
    {X S : Scheme.{u}}
    (f : X ⟶ S) [IsProper f] [LocallyOfFinitePresentation f] (F : X.Modules)
    [F.IsQuasicoherent] [F.IsFinitePresentation] :
    ∃ Z : Over S, Mono Z.hom ∧ FinitePresentation Z.hom ∧
      Nonempty (Functor.RepresentableBy
        ({ S := S, X := X, f := f, F := F, isQuasicoherent := ‹F.IsQuasicoherent› } :
          FlatnessSituation.{u}).flatFunctor Z)
```

**`AlgebraicGeometry.exists_mono_finitePresentation_representableBy_structureSheaf_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalFlatteningOfPure.lean#L131). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 05UH, part (4).** Let `f : X ⟶ S` be proper
> and of finite presentation. Then the universal flattening `Z ⟶ S` of `X` exists, and it is a
> monomorphism of finite presentation.

```lean
theorem exists_mono_finitePresentation_representableBy_structureSheaf_of_isProper
    {X S : Scheme.{u}}
    (f : X ⟶ S) [IsProper f] [LocallyOfFinitePresentation f] :
    ∃ Z : Over S, Mono Z.hom ∧ FinitePresentation Z.hom ∧
      Nonempty ((structureSheafFlatnessSituation f).flatFunctor.RepresentableBy Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.27, Tag 05PS](https://stacks.math.columbia.edu/tag/05PS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
