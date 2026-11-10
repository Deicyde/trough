---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsCurve, AlgebraicGeometry.not_isProper_compl_singleton, Stacks.HQuasiProjectiveDimensionOne.isHQuasiProjective_of_topologicalKrullDim_eq_zero, Stacks.HQuasiProjectiveDimensionOne.isHQuasiProjective_of_dimension_le_one, Stacks.HQuasiProjectiveDimensionOne.isProjectiveMorphism_of_isProper_of_topologicalKrullDim_le_one, Stacks.CurveProjectiveCompletion.exists_projective_completion_of_dimension_le_one, Stacks.CurveProjectiveCompletion.exists_projective_completion_discreteValuation_of_isReduced, AlgebraicGeometry.exists_isPurelyInseparable_smooth_normalization
statement: formalized
proof: formalized
---

# 33.43 Curves

Section 33.43 of the Stacks Project, [Tag 0A22](https://stacks.math.columbia.edu/tag/0A22). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A23, a definition

[Tag 0A23](https://stacks.math.columbia.edu/tag/0A23) in the Stacks Project.

**`AlgebraicGeometry.IsCurve`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean#L46). References: EGA II (7.4.2), “special case”.

> **Stacks Project, Tag 0A23.** A curve over a field is a variety of Krull dimension one.

```lean
public class IsCurve (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsVariety k f
```

## Tag 0A24, a lemma

[Tag 0A24](https://stacks.math.columbia.edu/tag/0A24) in the Stacks Project.

**`AlgebraicGeometry.not_isProper_compl_singleton`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Proper.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Proper.lean#L44).

> **Stacks 0A24.** Removing a closed point from an irreducible scheme of positive dimension
> gives an open subscheme which is not proper over any base over which the scheme is separated.

```lean
public lemma not_isProper_compl_singleton
    {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [IrreducibleSpace X] (x : X) (hx : IsClosed ({x} : Set X))
    (hdim : 0 < topologicalKrullDim X) :
    let U : X.Opens := ⟨{x}ᶜ, hx.isOpen_compl⟩
    ¬ IsProper (U.ι ≫ f)
```

## Tag 0A25, a lemma

[Tag 0A25](https://stacks.math.columbia.edu/tag/0A25) in the Stacks Project.

**`Stacks.HQuasiProjectiveDimensionOne.isHQuasiProjective_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean#L159). The attribute's comment: “for a scheme of topological Krull dimension zero, where reducedness is not needed because such a scheme is affine and the structure sheaf of an affine scheme is ample”.

> A separated scheme of finite type over a field `k` of topological Krull dimension zero is
> H-quasi-projective over `k`.

```lean
theorem isHQuasiProjective_of_topologicalKrullDim_eq_zero {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim (X : Type u) = 0) :
    AlgebraicGeometry.IsHQuasiProjective f
```

**`Stacks.HQuasiProjectiveDimensionOne.isHQuasiProjective_of_dimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean#L180).

> A separated scheme of finite type over a field `k` whose topological Krull dimension is at
> most one is H-quasi-projective over `k`.

```lean
theorem isHQuasiProjective_of_dimension_le_one
    {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    AlgebraicGeometry.IsHQuasiProjective f
```

## Tag 0A26, a lemma

[Tag 0A26](https://stacks.math.columbia.edu/tag/0A26) in the Stacks Project.

**`Stacks.HQuasiProjectiveDimensionOne.isProjectiveMorphism_of_isProper_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HQuasiProjectiveDimensionOne/Basic.lean#L203).

> A proper scheme over a field `k` whose topological Krull dimension is at most one is
> H-projective over `k`.

```lean
theorem isProjectiveMorphism_of_isProper_of_topologicalKrullDim_le_one
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    IsProjectiveMorphism f
```

## Tag 0BXV, a lemma

[Tag 0BXV](https://stacks.math.columbia.edu/tag/0BXV) in the Stacks Project.

**`Stacks.CurveProjectiveCompletion.exists_projective_completion_of_dimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCompletion.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCompletion.lean#L286). The attribute's comment: “the whole tag: all three clauses, for every separated scheme of finite type over `k` of dimension at most one”.

> Let `X` be a separated scheme of finite type over a field `k` with `dim(X) ≤ 1`. Then there
> is an open immersion `j : X ⟶ X̄` such that
>
> 1. `X̄` is H-projective over `k`, a closed subscheme of `ℙᵈ_k` for some `d`;
> 2. `j(X)` is dense and scheme-theoretically dense in `X̄`;
> 3. `X̄ \ j(X)` is a finite set of closed points of `X̄`.

```lean
theorem exists_projective_completion_of_dimension_le_one
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (CommRingCat.of k))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (CommRingCat.of k)) (j : X ⟶ Y) (hj : IsOpenImmersion j),
      letI : IsOpenImmersion j := hj
      j ≫ q = f ∧ IsProjectiveMorphism q ∧ IsDominant j ∧
        Scheme.Opens.IsSchemeTheoreticallyDense j.opensRange ∧
        ((Set.range j.base)ᶜ).Finite ∧
        ∀ y : Y, y ∉ Set.range j.base → IsClosed ({y} : Set Y)
```

## Tag 0BXW, a lemma

[Tag 0BXW](https://stacks.math.columbia.edu/tag/0BXW) in the Stacks Project.

**`Stacks.CurveProjectiveCompletion.exists_projective_completion_discreteValuation_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCompletionDiscreteValuation.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCompletionDiscreteValuation.lean#L304).

> **[Stacks, Tag 0BXW].** Let `X` be a reduced separated scheme of finite type over a field `k`
> with `dim(X) ≤ 1`. Then there is an open immersion `j : X ⟶ X'` such that `X'` is H-projective
> over `k`, the image of `j` is dense and scheme-theoretically dense in `X'`, the complement
> `X' ∖ j(X)` is a finite set of closed points, and the local ring of `X'` at each of those points
> is a discrete valuation ring.
>
> The first step of the proof, [Stacks, Tag 0A25], is used in its reduced case
> `Stacks.CurveProjectiveCompletion.isHQuasiProjective_of_isReduced`.

```lean
theorem exists_projective_completion_discreteValuation_of_isReduced
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (CommRingCat.of k))
    [IsSeparated p] [LocallyOfFiniteType p] [QuasiCompact p] [AlgebraicGeometry.IsReduced X]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (CommRingCat.of k)) (j : X ⟶ Y) (hj : IsOpenImmersion j),
      letI : IsOpenImmersion j := hj
      j ≫ q = p ∧ IsProjectiveMorphism q ∧ IsDominant j ∧
        Scheme.Opens.IsSchemeTheoreticallyDense j.opensRange ∧
        ((Set.range j.base)ᶜ).Finite ∧
        ∀ y : Y, y ∉ Set.range j.base →
          IsClosed ({y} : Set Y) ∧
            ∃ _ : IsDomain (Y.presheaf.stalk y),
              IsDiscreteValuationRing (Y.presheaf.stalk y)
```

## Tag 0GK5, a lemma

[Tag 0GK5](https://stacks.math.columbia.edu/tag/0GK5) in the Stacks Project.

**`AlgebraicGeometry.exists_isPurelyInseparable_smooth_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothNormalizationPurelyInseparable.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothNormalizationPurelyInseparable.lean#L132). The attribute's comment: “clauses (1) and (2), with ν smooth over k'; clauses (3), (4), (5) not established”. References: SGA 4 XIV (1.11).

> **[Stacks, Tag 0GK5], clauses (1) and (2), with the normalization smooth over `k'`.** Let `k`
> be a field and let `X` be a scheme of finite type over `k` with `dim X ≤ 1`. There is a finite
> purely inseparable extension `k'/k` such that the normalization of `X_{k'}` is smooth over `k'`.
>
> Clauses (3), (4) and (5) of the source — the compactification `j` with dense image, the finite
> separable extensions `k'_i/k'` and the smooth projective geometrically irreducible pieces over
> them — are not established here; see the module docstring.

```lean
public theorem exists_isPurelyInseparable_smooth_normalization (k : Type u) [Field k]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [LocallyOfFiniteType p] [QuasiCompact p]
    (hdim : topologicalKrullDim X ≤ 1) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : IsPurelyInseparable k k'),
      Smooth (normalizationOverField k' (pullback.fst (spectrumMap k k') p) ≫
        pullback.fst (spectrumMap k k') p)
```

**`AlgebraicGeometry.exists_isPurelyInseparable_dense_openImmersion_smooth_projective_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveCompactificationCurve.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveCompactificationCurve.lean#L117). The attribute's comment: “clauses (3), (4) and (5) -- the whole diagram -- for a REDUCED X. The source's first move is to replace X by its reduction; everything after that move is proved here. The normalization of X_{k'} is exhibited as a DENSE OPEN SUBSCHEME of the disjoint union of the compactifications Ybar_i (clause 3), each of which is SMOOTH, PROJECTIVE and GEOMETRICALLY IRREDUCIBLE of dimension at most one over a finite SEPARABLE extension k'_i/k' (clauses 4 and 5), and the diagram commutes over Spec k'. What is NOT covered: the reduction step, i.e. the case of an X that is not reduced.”. References: EGA IV (17.15.14), “special case”; SGA 4 XIV (1.11), “special case”.

> **[Stacks, Tag 0GK5] for a reduced `X`.** Let `k` be a field and let `X` be a reduced
> separated scheme of finite type over `k` with `dim(X) ≤ 1`. There is a finite purely inseparable
> extension `k'/k`, a finite family of schemes `Ȳᵢ` over `Spec k'`, and a dense open immersion `j`
> from the normalization of `X_{k'}` into their disjoint union over `Spec k'`, such that each `Ȳᵢ`
> is smooth, H-projective and geometrically irreducible of dimension at most one over a finite
> separable extension `k'ᵢ/k'`.

```lean
public theorem exists_isPurelyInseparable_dense_openImmersion_smooth_projective_of_isReduced
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k))
    [IsSeparated p] [LocallyOfFiniteType p] [QuasiCompact p] [AlgebraicGeometry.IsReduced X]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : IsPurelyInseparable k k') (ι : Type u) (_ : Finite ι) (Ybar : ι → Scheme.{u})
      (sbar : (∐ Ybar) ⟶ Spec (.of k'))
      (K : ι → Type u) (_ : ∀ i, Field (K i)) (_ : ∀ i, Algebra k' (K i))
      (_ : ∀ i, Module.Finite k' (K i)) (_ : ∀ i, Algebra.IsSeparable k' (K i))
      (rbar : ∀ i, Ybar i ⟶ Spec (.of (K i)))
      (j : normalizationSchemeOverField k' (pullback.fst (spectrumMap k k') p) ⟶ ∐ Ybar)
      (_ : IsOpenImmersion j),
      Dense (Set.range j.base) ∧
        j ≫ sbar = normalizationOverField k' (pullback.fst (spectrumMap k k') p) ≫
            pullback.fst (spectrumMap k k') p ∧
          (∀ i, rbar i ≫ Spec.map (CommRingCat.ofHom (algebraMap k' (K i)))
              = Sigma.ι Ybar i ≫ sbar) ∧
            ∀ i, Smooth (rbar i) ∧ IsProjectiveMorphism (rbar i) ∧
              GeometricallyIrreducible (rbar i) ∧ topologicalKrullDim (Ybar i : Type u) ≤ 1
```

**`AlgebraicGeometry.exists_isPurelyInseparable_dense_openImmersion_smooth_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveCompactificationCurve.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveCompactificationCurve.lean#L252). References: EGA IV (17.15.14), “special case”; SGA 4 XIV (1.11), “special case”.

> **[Stacks, Tag 0GK5].** Let `k` be a field and let `X` be a separated scheme of finite type
> over `k` with `dim(X) ≤ 1`. There is a finite purely inseparable extension `k'/k` (clause 1) such
> that the normalization of `X_{k'}` (clause 2) is a dense open subscheme (clause 3) of a finite
> disjoint union of schemes `Ȳᵢ`, each smooth, H-projective and geometrically irreducible of
> dimension at most one (clause 5) over a finite separable extension `k'ᵢ/k'` (clause 4), the whole
> diagram commuting over `Spec k'`.

```lean
public theorem exists_isPurelyInseparable_dense_openImmersion_smooth_projective
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k))
    [IsSeparated p] [LocallyOfFiniteType p] [QuasiCompact p]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : IsPurelyInseparable k k') (ι : Type u) (_ : Finite ι) (Ybar : ι → Scheme.{u})
      (sbar : (∐ Ybar) ⟶ Spec (.of k'))
      (K : ι → Type u) (_ : ∀ i, Field (K i)) (_ : ∀ i, Algebra k' (K i))
      (_ : ∀ i, Module.Finite k' (K i)) (_ : ∀ i, Algebra.IsSeparable k' (K i))
      (rbar : ∀ i, Ybar i ⟶ Spec (.of (K i)))
      (j : normalizationSchemeOverField k' (pullback.fst (spectrumMap k k') p) ⟶ ∐ Ybar)
      (_ : IsOpenImmersion j),
      Dense (Set.range j.base) ∧
        j ≫ sbar = normalizationOverField k' (pullback.fst (spectrumMap k k') p) ≫
            pullback.fst (spectrumMap k k') p ∧
          (∀ i, rbar i ≫ Spec.map (CommRingCat.ofHom (algebraMap k' (K i)))
              = Sigma.ι Ybar i ≫ sbar) ∧
            ∀ i, Smooth (rbar i) ∧ IsProjectiveMorphism (rbar i) ∧
              GeometricallyIrreducible (rbar i) ∧ topologicalKrullDim (Ybar i : Type u) ≤ 1
```

**`AlgebraicGeometry.exists_isPurelyInseparable_normalization_coproduct_smooth_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveNormalizationProper.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProjectiveNormalizationProper.lean#L88). The attribute's comment: “clauses (3), (4) and (5) for a PROPER X, where the open immersion j of clause (3) is an isomorphism and the compactifications Ybar_i are the components Y_i of the normalization themselves. Clauses (1) and (2) -- the finite purely inseparable k'/k and the normalization of X_{k'} -- are reproved here as part of the diagram. What the general separated case still needs is the compactification of Stacks 0BXW applied to X before k' is chosen, together with the identification of the normalization of X_{k'} with the open part of the normalization of that compactification.”. References: EGA IV (17.15.14), “Proper case of 17.15.14”; SGA 4 XIV (1.11), “special case”.

> **[Stacks, Tag 0GK5] for a proper `X`.** Let `k` be a field and let `X` be proper over `k`
> with `dim(X) ≤ 1`. There is a finite purely inseparable extension `k'/k` such that the
> normalization of `X_{k'}` is a finite coproduct of schemes `Yᵢ`, each smooth, H-projective and
> geometrically irreducible of dimension at most one over a finite separable extension `k'ᵢ/k'`,
> compatibly with the structure morphisms.

```lean
public theorem exists_isPurelyInseparable_normalization_coproduct_smooth_projective
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsProper p]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : IsPurelyInseparable k k') (ι : Type u) (_ : Finite ι) (Y : ι → Scheme.{u})
      (e : normalizationSchemeOverField k' (pullback.fst (spectrumMap k k') p) ≅ ∐ Y)
      (K : ι → Type u) (_ : ∀ i, Field (K i)) (_ : ∀ i, Algebra k' (K i))
      (_ : ∀ i, Module.Finite k' (K i)) (_ : ∀ i, Algebra.IsSeparable k' (K i))
      (r : ∀ i, Y i ⟶ Spec (.of (K i))),
      (∀ i, r i ≫ Spec.map (CommRingCat.ofHom (algebraMap k' (K i))) =
          Sigma.ι Y i ≫ e.inv ≫
            normalizationOverField k' (pullback.fst (spectrumMap k k') p) ≫
              pullback.fst (spectrumMap k k') p) ∧
        ∀ i, Smooth (r i) ∧ IsProjectiveMorphism (r i) ∧ GeometricallyIrreducible (r i) ∧
          topologicalKrullDim (Y i : Type u) ≤ 1
```

**`AlgebraicGeometry.exists_isSeparable_smooth_isProjectiveMorphism_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProperConnectedComponent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SmoothProperConnectedComponent.lean#L98). The attribute's comment: “clauses (4) and (5), at one component: for a CONNECTED scheme Z smooth and proper over a field k with dim Z <= 1 -- that is, for one of the compactified pieces Ybar_i of the diagram -- the field k'_i = Gamma(Z, O_Z) of clause (4) is a finite SEPARABLE extension of k, and Z is SMOOTH, PROJECTIVE and GEOMETRICALLY IRREDUCIBLE of dimension at most one over it, which is clause (5). The assembly of the diagram -- decomposing the normalization into its components and transporting along the open immersion j of clause (3) -- is not done here; clauses (1) and (2) are carried by AlgebraicGeometry.exists_isPurelyInseparable_smooth_normalization.”.

> **[Stacks, Tag 0GK5], clauses (4) and (5) at one component.** Let `Z` be a connected scheme,
> smooth and proper over a field `k`, of dimension at most one. Then there is a finite separable
> extension `K/k` and a morphism `r : Z ⟶ Spec K` over `k` which is smooth, H-projective and
> geometrically irreducible, with `dim(Z) ≤ 1`.
>
> The field is `K = Γ(Z, 𝒪_Z)` and the morphism is the canonical `Z ⟶ Spec Γ(Z, 𝒪_Z)`, exactly as
> in the source.

```lean
public theorem exists_isSeparable_smooth_isProjectiveMorphism_geometricallyIrreducible
    (k : Type u) [Field k] {Z : Scheme.{u}} (q : Z ⟶ Spec (.of k))
    [IsProper q] [Smooth q] [ConnectedSpace Z]
    (hdim : topologicalKrullDim (Z : Type u) ≤ 1) :
    ∃ (K : Type u) (_ : Field K) (_ : Algebra k K) (_ : Module.Finite k K)
      (_ : Algebra.IsSeparable k K) (r : Z ⟶ Spec (.of K)),
      r ≫ Spec.map (CommRingCat.ofHom (algebraMap k K)) = q ∧
        Smooth r ∧ IsProjectiveMorphism r ∧ GeometricallyIrreducible r ∧
        topologicalKrullDim (Z : Type u) ≤ 1
```

## Tag 0B8Y, a lemma

[Tag 0B8Y](https://stacks.math.columbia.edu/tag/0B8Y) in the Stacks Project.

**`AlgebraicGeometry.isDiscreteValuationRing_stalk_tfae_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveLocalRing/Basic.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveLocalRing/Basic.lean#L144). The attribute's comment: “(1), (2) and (3)”. References: EGA II (7.4.5); EGA II (7.1.6), “curve stalk case”; EGA IV (6.7.5), “partial”; SGA 7 IX (3.2.1), “special case”.

> **Items (1), (2) and (3) of [Stacks, Tag 0B8Y].** At a closed point `x` of a curve over a
> field the local ring `𝒪_{X,x}` is regular if and only if it is normal if and only if it is a
> discrete valuation ring.

```lean
public theorem isDiscreteValuationRing_stalk_tfae_of_isCurve [IsCurve k f] {x : X}
    (hx : IsClosed ({x} : Set X)) :
    List.TFAE [IsRegularLocalRing (X.presheaf.stalk x), IsNormalRing (X.presheaf.stalk x),
      IsDiscreteValuationRing (X.presheaf.stalk x)]
```

**`AlgebraicGeometry.isEffectiveCartierDivisor_closedPoint_tfae_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveLocalRing/EffectiveCartier.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveLocalRing/EffectiveCartier.lean#L130). The attribute's comment: “(1), (2), (3), (4) and (5)”. References: EGA II (7.4.5); EGA II (7.1.6), “curve stalk case”; EGA IV (6.7.5), “partial”.

> At a closed point `x` of a curve over a field the following are equivalent: `𝒪_{X,x}` is
> regular; `𝒪_{X,x}` is normal; `𝒪_{X,x}` is a discrete valuation ring; and the sheaf of ideals of
> the reduced closed subscheme `{x}` is an invertible `𝒪_X`-module, which is to say that `x` is an
> effective Cartier divisor on `X`.

```lean
public theorem isEffectiveCartierDivisor_closedPoint_tfae_of_isCurve [IsCurve k f] {x : X}
    (hx : IsClosed ({x} : Set X)) :
    List.TFAE [IsRegularLocalRing (X.presheaf.stalk x), IsNormalRing (X.presheaf.stalk x),
      IsDiscreteValuationRing (X.presheaf.stalk x),
      Stacks.Divisors.IsEffectiveCartierDivisor
        (Scheme.IdealSheafData.vanishingIdeal (⟨{x}, hx⟩ : Closeds X))]
```

**`AlgebraicGeometry.smoothAt_closedPoint_tfae_of_isCurve_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveLocalRing/Smooth.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveLocalRing/Smooth.lean#L49). The attribute's comment: “(1), (2), (3), (4), (5) and (6), for κ(x) separable over k”. References: EGA IV (17.15.1), “the smoothness item”; SGA 1 II (5.4), “κ(x)/k separable”.

> **Smoothness at a closed point of a curve, for a separable residue field.** Let `k` be a field,
> let `X` be a curve over `k` and let `x` be a closed point of `X` whose residue field is separable
> over `k`. Then the following are equivalent: `𝒪_{X,x}` is regular; `𝒪_{X,x}` is normal; `𝒪_{X,x}`
> is a discrete valuation ring; the sheaf of ideals of the reduced closed subscheme `{x}` is an
> invertible `𝒪_X`-module, which is to say that `x` is an effective Cartier divisor on `X`; and
> `X → Spec k` is smooth at `x`.

```lean
public theorem smoothAt_closedPoint_tfae_of_isCurve_of_isSeparable [IsCurve k f] {x : X}
    (hx : IsClosed ({x} : Set X))
    (hsep : letI : Algebra k (X.residueField x) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      Algebra.IsSeparableExtension k (X.residueField x)) :
    List.TFAE [IsRegularLocalRing (X.presheaf.stalk x), IsNormalRing (X.presheaf.stalk x),
      IsDiscreteValuationRing (X.presheaf.stalk x),
      Stacks.Divisors.IsEffectiveCartierDivisor
        (Scheme.IdealSheafData.vanishingIdeal (⟨{x}, hx⟩ : Closeds X)),
      InfinitesimalLifting.SmoothAt f x]
```

**`AlgebraicGeometry.smoothAt_closedPoint_tfae_of_isCurve_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveLocalRing/Smooth.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveLocalRing/Smooth.lean#L73). The attribute's comment: “(1), (2), (3), (4), (5) and (6), for k perfect”. References: EGA IV (17.15.2), “the smoothness item”; EGA IV (6.7.5), “special case”; SGA 1 II (5.4), “k perfect”.

> **Smoothness at a closed point of a curve, over a perfect field.** Let `k` be a perfect field,
> let `X` be a curve over `k` and let `x` be a closed point of `X`. Then the following are
> equivalent: `𝒪_{X,x}` is regular; `𝒪_{X,x}` is normal; `𝒪_{X,x}` is a discrete valuation ring; the
> sheaf of ideals of the reduced closed subscheme `{x}` is an invertible `𝒪_X`-module, which is to
> say that `x` is an effective Cartier divisor on `X`; and `X → Spec k` is smooth at `x`.

```lean
public theorem smoothAt_closedPoint_tfae_of_isCurve_of_perfectField [PerfectField k] [IsCurve k f]
    {x : X} (hx : IsClosed ({x} : Set X)) :
    List.TFAE [IsRegularLocalRing (X.presheaf.stalk x), IsNormalRing (X.presheaf.stalk x),
      IsDiscreteValuationRing (X.presheaf.stalk x),
      Stacks.Divisors.IsEffectiveCartierDivisor
        (Scheme.IdealSheafData.vanishingIdeal (⟨{x}, hx⟩ : Closeds X)),
      InfinitesimalLifting.SmoothAt f x]
```

## Tag 0H1F, a remark

[Tag 0H1F](https://stacks.math.columbia.edu/tag/0H1F) in the Stacks Project.

**`AlgebraicGeometry.exists_isRegular_isProjectiveMorphism_compactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RegularCompactification.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RegularCompactification.lean#L141). The attribute's comment: “the regular projective compactification”.

> Let `k` be a field and let `X` be a regular curve over `k`. Then there is a nonsingular
> projective curve `X̄` over `k` and an open immersion `j : X ⟶ X̄` over `k` whose complement is a
> finite set of closed points of `X̄`.

```lean
public theorem exists_isRegular_isProjectiveMorphism_compactification
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsCurve k p]
    (hX : IsRegular X) :
    ∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (.of k)) (j : X ⟶ Y) (hj : IsOpenImmersion j),
      letI : IsOpenImmersion j := hj
      j ≫ q = p ∧ IsCurve k q ∧ IsProjectiveMorphism q ∧ IsRegular Y ∧
        ((Set.range j.base)ᶜ).Finite ∧
        ∀ y : Y, y ∉ Set.range j.base → IsClosed ({y} : Set Y)
```

**`AlgebraicGeometry.exists_smooth_isProjectiveMorphism_compactification_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RegularCompactification.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RegularCompactification.lean#L181). The attribute's comment: “the smooth projective compactification over a perfect field”.

> Let `k` be a perfect field and let `X` be a regular curve over `k`. Then `X` is smooth over
> `k`, and there is a nonsingular projective curve `X̄` over `k`, smooth over `k`, with an open
> immersion `j : X ⟶ X̄` over `k` whose complement is a finite set of closed points of `X̄`.

```lean
public theorem exists_smooth_isProjectiveMorphism_compactification_of_perfectField
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k))
    [IsCurve k p] (hX : IsRegular X) :
    Smooth p ∧ ∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (.of k)) (j : X ⟶ Y) (hj : IsOpenImmersion j),
      letI : IsOpenImmersion j := hj
      j ≫ q = p ∧ IsCurve k q ∧ IsProjectiveMorphism q ∧ IsRegular Y ∧ Smooth q ∧
        ((Set.range j.base)ᶜ).Finite ∧
        ∀ y : Y, y ∉ Set.range j.base → IsClosed ({y} : Set Y)
```

## Tag 0A27, a lemma

[Tag 0A27](https://stacks.math.columbia.edu/tag/0A27) in the Stacks Project.

**`AlgebraicGeometry.isAffine_or_isProjectiveMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/AffineOrProjective.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/AffineOrProjective.lean#L209).

> Let `k` be a field and let `X` be a curve over `k`. Then `X` is an affine scheme or `X` is
> H-projective over `k`.

```lean
theorem isAffine_or_isProjectiveMorphism
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] :
    IsAffine X ∨ IsProjectiveMorphism f
```

## Tag 0A28, a lemma

[Tag 0A28](https://stacks.math.columbia.edu/tag/0A28) in the Stacks Project.

**`AlgebraicGeometry.isAffine_of_topologicalKrullDim_le_one_of_forall_component_not_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/AffineOfNoProperComponent.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/AffineOfNoProperComponent.lean#L205).

> **[Stacks, Tag 0A28].** Let `k` be a field and let `X` be a separated scheme of finite type
> over `k` with `dim(X) ≤ 1`. If no irreducible component of `X`, taken with its reduced induced
> closed subscheme structure, is proper over `k` of dimension one, then `X` is an affine scheme.
>
> Each component is integral, and separated and of finite type over `k` of dimension at most one.
> A one-dimensional component is therefore a curve over `k`, so [Stacks, Tag 0A27] makes it affine
> or H-projective over `k`, and the latter would make it proper over `k`, which `hcomponent`
> forbids; a zero-dimensional component is affine by [Stacks, Tag 06LH]. The components are
> finitely many, their coproduct is affine, and the induced morphism to `X` is finite and
> surjective, so [Stacks, Tag 01YQ] makes `X` affine.

```lean
theorem isAffine_of_topologicalKrullDim_le_one_of_forall_component_not_isProper
    (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim X ≤ 1)
    (hcomponent : ∀ Z : irreducibleComponents X,
      topologicalKrullDim (Scheme.IdealSheafData.vanishingIdeal
          (⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩ : Closeds X)).subscheme = 1 →
        ¬ IsProper ((Scheme.IdealSheafData.vanishingIdeal
          (⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩ : Closeds X)).subschemeι ≫ f)) :
    IsAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.43, Tag 0A22](https://stacks.math.columbia.edu/tag/0A22)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
