---
declaration: section
origin: cited
lean: AlgebraicGeometry.genus, AlgebraicGeometry.CurveDuality.genus_eq_finrank_structureSheafCohomology_and_eq_finrank_relativeDualizingModule, AlgebraicGeometry.genus_eq_finrank_structureSheafCohomology, AlgebraicGeometry.topologicalKrullDim_baseChange, AlgebraicGeometry.isIso_globalSections_baseChange, AlgebraicGeometry.genus_baseChange, AlgebraicGeometry.IsProper.isStableUnderBaseChange, AlgebraicGeometry.invertibleCurveDegree_dualizingSheafOverField
statement: formalized
proof: formalized
---

# 53.8 The genus of a curve

Section 53.8 of the Stacks Project, [Tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BY7, a definition

[Tag 0BY7](https://stacks.math.columbia.edu/tag/0BY7) in the Stacks Project.

**`AlgebraicGeometry.genus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Basic.lean#L59).

> The genus of a scheme `X` over a field `k`, namely `dim_k H¹(X, 𝒪_X)`.

```lean
noncomputable def genus {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : ℕ
```

## Tag 0BY8, an equation

[Tag 0BY8](https://stacks.math.columbia.edu/tag/0BY8) in the Stacks Project.

**`AlgebraicGeometry.CurveDuality.genus_eq_finrank_structureSheafCohomology_and_eq_finrank_relativeDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SerreDuality/Duality.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/SerreDuality/Duality.lean#L293). The attribute's comment: “equation 53.8.1.1: the genus is the dimension over the ground field of the first cohomology of the structure sheaf, and the dimension over the ground field of the global sections of the relative dualizing module”.

> **Equation 53.8.1.1 of [Stacks, Tag 0BY8].** Let `k` be a field and let `f : X ⟶ Spec(k)` be
> proper with `X` of topological Krull dimension one. Then
>
> `g = dim_k H^1(X, 𝒪_X) = dim_k H^0(X, ω_X)`,
>
> where `g` is the genus of [Stacks, Tag 0BY7] and `ω_X = H^{-1}(f^×𝒪_{Spec(k)})` is the relative
> dualizing module of [Stacks, Tag 0AWI] — the object that [Stacks, Tag 0BS2] produces as
> `H^{-1}` of the relative dualizing complex `a(𝒪_{Spec(k)})`.
>
> The first equality is the definition of the genus,
> `AlgebraicGeometry.genus_eq_finrank_structureSheafCohomology`; the second is
> `finrank_structureSheafCohomology_eq_finrank_cohomologyOverField_relativeDualizingModule`.
>
> Definition 53.8.1 of the source also assumes `H^0(X, 𝒪_X) = k`, which fixes the ground field and
> makes `X` Cohen--Macaulay and equidimensional; neither equality needs it, so it is not assumed
> here and the statement holds in the generality of the definition and beyond.

```lean
theorem genus_eq_finrank_structureSheafCohomology_and_eq_finrank_relativeDualizingModule
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X = 1) :
    letI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    letI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    genus f = Module.finrank k (structureSheafCohomology f 1) ∧
      Module.finrank k (structureSheafCohomology f 1) =
        Module.finrank k (cohomologyOverField k f
          (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) 0)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.genus_eq_finrank_structureSheafCohomology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Basic.lean#L64), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean#L52) (StacksFrontier): “genus as first cohomology”.

## Tag 0BY9, a lemma

[Tag 0BY9](https://stacks.math.columbia.edu/tag/0BY9) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean#L88). The attribute's comment: “dimension”.

> Extending the ground field of a proper scheme preserves its Krull dimension.

```lean
theorem topologicalKrullDim_baseChange (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    {X' X : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ Spec (.of k')) (f : X ⟶ Spec (.of k))
    (h : IsPullback g' f' f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))
    [LocallyOfFiniteType f] :
    topologicalKrullDim X' = topologicalKrullDim X
```

**`AlgebraicGeometry.isIso_globalSections_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean#L116). The attribute's comment: “global sections”.

> If all global regular functions on a proper scheme over `k` are constant, then after extending
> the ground field to `k'` all global regular functions are again constant.

```lean
theorem isIso_globalSections_baseChange (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    {X' X : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ Spec (.of k')) (f : X ⟶ Spec (.of k))
    (h : IsPullback g' f' f (Spec.map (CommRingCat.ofHom (algebraMap k k')))) [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] :
    IsIso ((Scheme.ΓSpecIso (.of k')).inv ≫ f'.appTop)
```

**`AlgebraicGeometry.genus_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean#L141). The attribute's comment: “genus”.

> The genus of a proper scheme over a field is unchanged by extension of the ground field.

```lean
theorem genus_baseChange (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    {X' X : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ Spec (.of k')) (f : X ⟶ Spec (.of k))
    (h : IsPullback g' f' f (Spec.map (CommRingCat.ofHom (algebraMap k k')))) [IsProper f] :
    genus f' = genus f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsProper.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BaseChange.lean#L50) (StacksFrontier): “properness”. References: EGA II (5.4.2), “more general”; EGA III (4.3.4), “more general”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “partial”; SGA 6 X (7.5), “partial”.

## Tag 0C19, a lemma

[Tag 0C19](https://stacks.math.columbia.edu/tag/0C19) in the Stacks Project.

**`AlgebraicGeometry.invertibleCurveDegree_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/DualizingDegree.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/DualizingDegree.lean#L275).

> Let `X` be a proper scheme over a field `k` of dimension one with `H⁰(X, 𝒪_X) = k`. If `X` is
> Gorenstein, then `deg(ω_X) = 2g - 2`, where `g` is the genus of `X` and `ω_X` is the dualizing
> sheaf of [Stacks, Tag 0BS2].

```lean
theorem invertibleCurveDegree_dualizingSheafOverField (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    [IsGorenstein X] (hdim : topologicalKrullDim X = 1) :
    letI := connectedSpace_of_isIso_globalSections k f
    letI := isInvertible_dualizingSheafOverField_of_connectedSpace k f hdim
    invertibleCurveDegree k f hdim.le (Stacks.Duality.dualizingSheafOverField f) =
      2 * (genus f : ℤ) - 2
```

## Tag 0C1A, a lemma

[Tag 0C1A](https://stacks.math.columbia.edu/tag/0C1A) in the Stacks Project.

**`AlgebraicGeometry.invertibleCurveDegree_relativeDifferentials_eq_two_mul_genus_sub_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DifferentialsDegreeGenus.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DifferentialsDegreeGenus.lean#L69). The attribute's comment: “`deg(Ω_{X/k}) = 2g - 2`”.

> **Stacks Project, Tag 0C1A, second equality.** Let `X` be a smooth proper curve over a field
> `k` with `H⁰(X, 𝒪_X) = k`, of genus `g`. Then `deg(Ω_{X/k}) = 2g - 2`: `Ω_{X/k} ≅ ω_X` by
> Tag 0BS2 (6), and `deg(ω_X) = 2g - 2` (Tag 0C19 for the Gorenstein curve `X`).

```lean
theorem invertibleCurveDegree_relativeDifferentials_eq_two_mul_genus_sub_two :
    invertibleCurveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f)))
        (Scheme.Hom.relativeDifferentials f) = 2 * genus f - 2
```

**`AlgebraicGeometry.finrank_cohomologyOverField_zero_relativeDifferentials_eq_genus_and_curveDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/SmoothCurveDifferentials.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/SmoothCurveDifferentials.lean#L104).

> **[Stacks, Tag 0C1A]**: for a smooth proper curve `X` over a field `k` with
> `H⁰(X, 𝒪_X) = k` and genus `g`, `dim_k H⁰(X, Ω_{X/k}) = g` and `deg(Ω_{X/k}) = 2g - 2`.

```lean
theorem finrank_cohomologyOverField_zero_relativeDifferentials_eq_genus_and_curveDegree
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pX.appTop)] :
    Module.finrank k (cohomologyOverField k pX (Scheme.Hom.relativeDifferentials pX) 0) =
        genus pX ∧
      letI := smoothOfRelativeDimension_one_of_isCurve k pX
      letI := Scheme.Hom.isFiniteLocallyFreeOfRank_one_relativeDifferentials pX
      curveDegree k pX (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := pX)))
          (Scheme.Hom.relativeDifferentials pX) 1 = 2 * (genus pX : ℤ) - 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.8, Tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
