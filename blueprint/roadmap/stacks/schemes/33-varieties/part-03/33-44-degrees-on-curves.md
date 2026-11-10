---
declaration: section
origin: cited
lean: AlgebraicGeometry.curveDegree, AlgebraicGeometry.invertibleCurveDegree, AlgebraicGeometry.curveDegree_baseChange_field, AlgebraicGeometry.curveDegree_add_of_shortExact_of_isProper, AlgebraicGeometry.curveDegree_add_of_shortExact_of_cohomologyFiniteDimensional, AlgebraicGeometry.curveDegree_pullback_eq_of_bijOn_genericPointsOne, AlgebraicGeometry.curveDegree_pullback_eq_of_bijOn_genericPointsOne_of_isProper, AlgebraicGeometry.exists_eulerCharacteristic_tensorSheaf_eq_fiberRank_mul_curveDegree_add_of_isCurve
statement: formalized
proof: formalized
---

# 33.44 Degrees on curves

Section 33.44 of the Stacks Project, [Tag 0AYQ](https://stacks.math.columbia.edu/tag/0AYQ). 17 tags here are carried by 43 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AYR, a definition

[Tag 0AYR](https://stacks.math.columbia.edu/tag/0AYR) in the Stacks Project.

**`AlgebraicGeometry.curveDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean#L82). The attribute's comment: “finite locally free case”.

> The degree of a finite locally free sheaf of constant rank on a proper scheme of
> dimension at most one over a field.

```lean
public noncomputable def curveDegree (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (_hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] : ℤ
```

**`AlgebraicGeometry.invertibleCurveDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean#L106). The attribute's comment: “invertible case”.

> The degree of an invertible sheaf on a proper scheme of dimension at most one over a
> field: its Euler characteristic minus the Euler characteristic of the structure sheaf.

```lean
public noncomputable def invertibleCurveDegree (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (_hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] : ℤ
```

## Tag 0B59, a lemma

[Tag 0B59](https://stacks.math.columbia.edu/tag/0B59) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_baseChange_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeFieldExtension.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeFieldExtension.lean#L68).

> **Stacks Project, Tag 0B59.** Let `k'/k` be an extension of fields, let `X` be a proper
> scheme of dimension at most one over `k` and let `ℰ` be a finite locally free `𝒪_X`-module of
> constant rank. Then the degree of `ℰ` over `k` equals the degree of its inverse image on the
> base change `X_{k'}` over `k'`.

```lean
theorem curveDegree_baseChange_field (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    {X' X : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ Spec (.of k')) (f : X ⟶ Spec (.of k))
    (h : IsPullback g' f' f (Spec.map (CommRingCat.ofHom (algebraMap k k')))) [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    @curveDegree k' _ X' f' (MorphismProperty.of_isPullback (P := @IsProper) h inferInstance)
        ((topologicalKrullDim_baseChange k k' g' f' f h).trans_le hdim)
        ((Scheme.Modules.pullback g').obj E) rank
        (isFiniteLocallyFreeOfRank_pullback g' E rank) =
      curveDegree k f hdim E rank
```

## Tag 0AYS, a lemma

[Tag 0AYS](https://stacks.math.columbia.edu/tag/0AYS) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_add_of_shortExact_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeAdditivityUnconditional.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeAdditivityUnconditional.lean#L49). The attribute's comment: “deg(ℰ₂) = deg(ℰ₁) + deg(ℰ₃) for a short exact sequence of locally free modules of finite constant rank on a proper scheme of dimension at most one over a field”.

> Let `k` be a field and let `X` be a scheme proper over `k` of dimension at most one. For a
> short exact sequence `0 ⟶ ℰ₁ ⟶ ℰ₂ ⟶ ℰ₃ ⟶ 0` of locally free `𝒪_X`-modules of finite constant
> ranks `r₁`, `r₂`, `r₃`, `deg(ℰ₂) = deg(ℰ₁) + deg(ℰ₃)`.

```lean
public theorem curveDegree_add_of_shortExact_of_isProper (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (hdim : topologicalKrullDim X ≤ 1)
    (S : ShortComplex X.Modules) (hS : S.ShortExact) (r₁ r₂ r₃ : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₁ r₁]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₂ r₂]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ r₃] :
    curveDegree k f hdim S.X₂ r₂ =
      curveDegree k f hdim S.X₁ r₁ + curveDegree k f hdim S.X₃ r₃
```

**`AlgebraicGeometry.curveDegree_add_of_shortExact_of_cohomologyFiniteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/CoherentFiniteness.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/CoherentFiniteness.lean#L252). The attribute's comment: “deg(ℰ₂) = deg(ℰ₁) + deg(ℰ₃); `hfin` is [Stacks, Tag 02O6] for `X`”.

> **Additivity of the degree along a short exact sequence.** For a short exact sequence
> `0 ⟶ ℰ₁ ⟶ ℰ₂ ⟶ ℰ₃ ⟶ 0` of finite locally free `𝒪_X`-modules of constant ranks `r₁`, `r₂`, `r₃`
> on a scheme `X` proper over a field `k` and of dimension at most one,
> `deg(ℰ₂) = deg(ℰ₁) + deg(ℰ₃)`.
>
> The single hypothesis `hfin` is [Stacks, Tag 02O6] for `X`; everything else the source uses —
> additivity of the Euler characteristic, additivity of the constant rank, and the empty
> scheme — is discharged. `hfin` is now itself a theorem, so the tag is additionally registered on
> the form that takes no finiteness hypothesis at all,
> `AlgebraicGeometry.curveDegree_add_of_shortExact_of_isProper` of
> `StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeAdditivityUnconditional.lean`, which applies
> this theorem to
> `AlgebraicGeometry.forall_finiteDimensional_cohomologyOverField_of_isProper`.

```lean
public theorem curveDegree_add_of_shortExact_of_cohomologyFiniteDimensional (k : Type u)
    [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hfin : CohomologyFiniteDimensionalOverFieldOn k f) (hdim : topologicalKrullDim X ≤ 1)
    (S : ShortComplex X.Modules) (hS : S.ShortExact) (r₁ r₂ r₃ : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₁ r₁]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₂ r₂]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ r₃] :
    curveDegree k f hdim S.X₂ r₂ =
      curveDegree k f hdim S.X₁ r₁ + curveDegree k f hdim S.X₃ r₃
```

## Tag 0AYU, a lemma

[Tag 0AYU](https://stacks.math.columbia.edu/tag/0AYU) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_pullback_eq_of_bijOn_genericPointsOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveDegreeInvariance/Morphism.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveDegreeInvariance/Morphism.lean#L497). References: SGA 6 X (4.4), “special case”.

> **[Stacks, Tag 0AYU], the "more generally" statement.** Let `k` be a field and let
> `g : X' ⟶ X` be a morphism over `k` between schemes proper over `k` and of dimension at most one
> which induces a bijection between the generic points of the one-dimensional irreducible
> components of `X'` and those of `X`, and isomorphisms of local rings at the points of `X'`
> involved. Let `ℰ` be finite locally free of constant rank `n` on `X`. Then
>
> `deg(g^*ℰ) = deg(ℰ)`.
>
> `hbij` and `hstalk` are the tag's own hypotheses — the bijection on the generic points of the
> one-dimensional components and the isomorphisms of local rings at the corresponding points — and
> the source's "more generally" clause implies its first, birational, sentence, which is not
> separately derived here. The finiteness input [Stacks, Tag 02O6] over a field is not assumed: it
> is `AlgebraicGeometry.cohomologyFiniteDimensionalOverField_of_isProper`. The projection formula
> [Stacks, Tag 01E8] at `g`, the source's displayed equation `g_*g^*ℰ ≅ ℰ ⊗_{𝒪_X} g_*𝒪_{X'}`, is
> proved rather than assumed, by `projectionFormula_iso_of_isFiniteLocallyFreeOfRank` above.
>
> The proof is the source's. The bijection on generic points makes `g` finite, so the cohomology of
> `X'` is read on `X` through `g_*`; the isomorphisms of local rings make the kernel and the
> cokernel of `𝒪_X ⟶ g_*𝒪_{X'}` vanish at the generic points of the one-dimensional components,
> hence give them zero-dimensional support, so clause (5) of [Stacks, Tag 0AYT] applies at both;
> and the computation of `CurveDegreeInvariance/Basic.lean` collapses the difference of the two
> degrees to zero.

```lean
theorem curveDegree_pullback_eq_of_bijOn_genericPointsOne (k : Type u) [Field k]
    {X' X : Scheme.{u}} (p' : X' ⟶ Spec (.of k)) (p : X ⟶ Spec (.of k))
    [IsProper p'] [IsProper p]
    (hdimX' : topologicalKrullDim (X' : Type u) ≤ 1)
    (hdimX : topologicalKrullDim (X : Type u) ≤ 1)
    (g : X' ⟶ X) (hgOver : g ≫ p = p')
    (hbij : Set.BijOn g (genericPointsOne X') (genericPointsOne X))
    (E : X.Modules) (n : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    (hstalk : ∀ z ∈ genericPointsOne X', IsIso (g.stalkMap z)) :
    @curveDegree k _ X' p' _ hdimX' ((Scheme.Modules.pullback g).obj E) n
        (isFiniteLocallyFreeOfRank_pullback g E n) =
      curveDegree k p hdimX E n
```

**`AlgebraicGeometry.curveDegree_pullback_eq_of_bijOn_genericPointsOne_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveDegreeInvariance/Unconditional.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveDegreeInvariance/Unconditional.lean#L66). The attribute's comment: “the 'more generally' statement, with no hypothesis beyond the tag's own”. References: SGA 6 X (4.4), “special case”.

> **[Stacks, Tag 0AYU], the "more generally" statement, with no hypothesis beyond the tag's
> own.** Let `k` be a field and let `g : X' ⟶ X` be a morphism over `k` between schemes proper
> over `k` and of dimension at most one which induces a bijection between the generic points of
> the one-dimensional irreducible components of `X'` and those of `X`, and isomorphisms of the
> local rings at the points of `X'` involved. Let `ℰ` be finite locally free of constant rank `n`
> on `X`. Then
>
> `deg(g^*ℰ) = deg(ℰ)`.
>
> `hbij` and `hstalk` are the tag's own hypotheses, and they are all that
> `curveDegree_pullback_eq_of_bijOn_genericPointsOne` takes: [Stacks, Tag 02O6] over a field and
> the projection formula at `g` are proved there rather than carried.

```lean
theorem curveDegree_pullback_eq_of_bijOn_genericPointsOne_of_isProper (k : Type u) [Field k]
    {X' X : Scheme.{u}} (p' : X' ⟶ Spec (.of k)) (p : X ⟶ Spec (.of k))
    [IsProper p'] [IsProper p]
    (hdimX' : topologicalKrullDim (X' : Type u) ≤ 1)
    (hdimX : topologicalKrullDim (X : Type u) ≤ 1)
    (g : X' ⟶ X) (hgOver : g ≫ p = p')
    (hbij : Set.BijOn g (genericPointsOne X') (genericPointsOne X))
    (E : X.Modules) (n : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    (hstalk : ∀ z ∈ genericPointsOne X', IsIso (g.stalkMap z)) :
    @curveDegree k _ X' p' _ hdimX' ((Scheme.Modules.pullback g).obj E) n
        (isFiniteLocallyFreeOfRank_pullback g E n) =
      curveDegree k p hdimX E n
```

## Tag 0AYV, a lemma

[Tag 0AYV](https://stacks.math.columbia.edu/tag/0AYV) in the Stacks Project.

**`AlgebraicGeometry.exists_eulerCharacteristic_tensorSheaf_eq_fiberRank_mul_curveDegree_add_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveTensorEulerUnit/Unconditional.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveTensorEulerUnit/Unconditional.lean#L65).

> **[Stacks, Tag 0AYV], with no hypothesis.** Let `k` be a field, let `X` be a proper curve
> over `k` with generic point `ξ`, let `ℰ` be finite locally free of rank `n` and let `ℱ` be
> coherent. Then
>
> `χ(X, ℰ ⊗ ℱ) = r·deg(ℰ) + n·χ(X, ℱ)`,
>
> where `r = dim_{κ(ξ)} ℱ_ξ` is the rank of `ℱ` at the generic point.

```lean
public theorem exists_eulerCharacteristic_tensorSheaf_eq_fiberRank_mul_curveDegree_add_of_isCurve
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsCurve k f] [IsProper f] (E : X.Modules) (n : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    (F : X.Modules) [SheafOfModules.IsCoherent F] :
    ∃ h : ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (F))).IsCoherent,
      @eulerCharacteristic k _ X f _
          ((((Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (F))) h =
        (Scheme.Modules.fiberRank F (genericPoint X) : ℤ) *
            curveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f))) E n +
          (n : ℤ) * eulerCharacteristic k f F
```

**`AlgebraicGeometry.eulerCharacteristic_tensorSheaf_eq_fiberRank_mul_curveDegree_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveTensorEulerUnit/Unconditional.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveTensorEulerUnit/Unconditional.lean#L92).

> **[Stacks, Tag 0AYV]**, with the coherence `h` of `ℰ ⊗ ℱ` taken as an argument instead of
> produced existentially: for `ℰ` finite locally free of rank `n` and `ℱ` coherent on a proper curve
> `X` over a field `k`, `χ(X, ℰ ⊗ ℱ) = r·deg(ℰ) + n·χ(X, ℱ)`, where `r = dim_{κ(ξ)} ℱ_ξ` is the
> rank of `ℱ` at the generic point `ξ`.

```lean
public theorem eulerCharacteristic_tensorSheaf_eq_fiberRank_mul_curveDegree_add
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsCurve k f] [IsProper f] (E : X.Modules) (n : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    (F : X.Modules) [SheafOfModules.IsCoherent F]
    (h : ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X.toRingedSpace)).presheaf,
        ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (F))).IsCoherent) :
    @eulerCharacteristic k _ X f _
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (F))) h =
      (Scheme.Modules.fiberRank F (genericPoint X) : ℤ) *
          curveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f))) E n +
        (n : ℤ) * eulerCharacteristic k f F
```

## Tag 0AYW, a lemma

[Tag 0AYW](https://stacks.math.columbia.edu/tag/0AYW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ComponentDegreeDevissage.curveDegree_eq_finsum_componentDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentDegreeDevissage/Basic.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentDegreeDevissage/Basic.lean#L407).

> The degree of a finite locally free module of constant rank on a scheme proper over a field
> and of dimension at most one is the multiplicity-weighted sum of its degrees on the reduced
> one-dimensional components:
>
> `deg(ℰ) = ∑ᶠ ξ, m(ξ) · deg(ℰ|_{C(ξ)})`.

```lean
theorem curveDegree_eq_finsum_componentDegree [IsProper f]
    (hX : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X,
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ
```

**`Stacks.AlgebraicGeometry.ComponentDegreeDevissage.exists_curveDegree_eq_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentDegreeDevissage/Basic.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentDegreeDevissage/Basic.lean#L431).

> The component formula for the degree in existential form: each reduced one-dimensional
> component is proper over the base, has dimension at most one and carries a restriction of `ℰ`
> that is again finite locally free of the same rank, and the component formula holds with respect
> to those three proofs.

```lean
theorem exists_curveDegree_eq_finsum [IsProper f]
    (hX : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    ∃ (hproper : ∀ ξ : genericPointsOne X, IsProper (reducedComponentι X ξ ≫ f))
      (hdimC : ∀ ξ : genericPointsOne X, topologicalKrullDim (reducedComponent X ξ) ≤ 1)
      (hrank : ∀ ξ : genericPointsOne X,
        _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
          ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank),
      curveDegree k f hX E rank =
        ∑ᶠ ξ : genericPointsOne X,
          (componentMultiplicity X ξ : ℤ) *
            @curveDegree k _ (reducedComponent X ξ) (reducedComponentι X ξ ≫ f)
              (hproper ξ) (hdimC ξ)
              ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank (hrank ξ)
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.curveDegree_eq_finsum_componentDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean#L198). The attribute's comment: “the component formula, from the two steps of the source argument”.

> **Stacks 0AYW.** The degree of a finite locally free module of constant rank on a proper
> scheme of dimension at most one over a field is the multiplicity-weighted sum of its degrees on
> the reduced one-dimensional components.

```lean
theorem curveDegree_eq_finsum_componentDegree
    (hreduce : curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X, @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
        ((Scheme.Modules.pullback (i ξ)).obj E) rank
        (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank))
    (hirreducible : ∀ ξ : genericPointsOne X,
      @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
          ((Scheme.Modules.pullback (i ξ)).obj E) rank
          (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank) =
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ) :
    curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X,
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.exists_curveDegree_eq_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean#L219). The attribute's comment: “the existential form the source states”.

> **Stacks 0AYW**, in the existential form the source states: each reduced one-dimensional
> component is proper over the base, has dimension at most one and carries a restriction of `ℰ`
> that is again finite locally free of the same rank, and the component formula holds with respect
> to those three proofs.

```lean
theorem exists_curveDegree_eq_finsum
    (hreduce : curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X, @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
        ((Scheme.Modules.pullback (i ξ)).obj E) rank
        (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank))
    (hirreducible : ∀ ξ : genericPointsOne X,
      @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
          ((Scheme.Modules.pullback (i ξ)).obj E) rank
          (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank) =
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ) :
    ∃ (hproperC : ∀ ξ : genericPointsOne X, IsProper (reducedComponentι X ξ ≫ f))
      (hdimC : ∀ ξ : genericPointsOne X, topologicalKrullDim (reducedComponent X ξ) ≤ 1)
      (hrank : ∀ ξ : genericPointsOne X,
        _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
          ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank),
      curveDegree k f hX E rank =
        ∑ᶠ ξ : genericPointsOne X,
          (componentMultiplicity X ξ : ℤ) *
            @curveDegree k _ (reducedComponent X ξ) (reducedComponentι X ξ ≫ f)
              (hproperC ξ) (hdimC ξ)
              ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank (hrank ξ)
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.curveDegree_eq_sum_componentDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean#L246). The attribute's comment: “the component formula as a finite sum”.

> **Stacks 0AYW** with the locally finite sum read as a finite sum over the components. This is
> the shape in which a consumer that already has the components as a `Fintype` uses the formula.

```lean
theorem curveDegree_eq_sum_componentDegree [Fintype (genericPointsOne X)]
    (hreduce : curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X, @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
        ((Scheme.Modules.pullback (i ξ)).obj E) rank
        (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank))
    (hirreducible : ∀ ξ : genericPointsOne X,
      @curveDegree k _ (Y ξ) (i ξ ≫ f) (hproper ξ) (hdimY ξ)
          ((Scheme.Modules.pullback (i ξ)).obj E) rank
          (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (i ξ) E rank) =
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ) :
    curveDegree k f hX E rank =
      ∑ ξ : genericPointsOne X,
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.curveDegree_eq_finsum_componentDegree_of_stalk_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Devissage.lean#L273). The attribute's comment: “the component formula, from the reduction to the irreducible case”.

> **Stacks 0AYW**, with the first paragraph of the source proof discharged from the
> reduction to a finite family of closed subschemes.
>
> The family `Zs` is the source's `Xᵢ`, the scheme-theoretic closures of the complements of the
> other components, enumerated by `0, …, N - 1`; `σ` picks out the member attached to a given
> one-dimensional component, and `hzero` says the remaining members — the zero-dimensional
> components — contribute nothing.

```lean
theorem curveDegree_eq_finsum_componentDegree_of_stalk_bijective
    {Zs : ℕ → Scheme.{u}} (ι : ∀ j, Zs j ⟶ X) [∀ j, IsClosedImmersion (ι j)] (N : ℕ)
    (σ : genericPointsOne X → Fin N) (hσ : Function.Injective σ)
    (Z : Set X) (hZfin : Z.Finite) (hZcl : ∀ x ∈ Z, IsClosed ({x} : Set X))
    (hbij : ∀ x ∉ Z, Function.Bijective (ConcreteCategory.hom
      ((_root_.AlgebraicGeometry.SheafOfModules.stalkAddCommGroupFunctor X.ringCatSheaf x).map
        (Scheme.Modules.pushforwardUnitSeriesMap ι N))))
    (hirreducible : ∀ ξ : genericPointsOne X,
      @curveDegree k _ (Zs (σ ξ)) (ι (σ ξ) ≫ f) _
          (le_trans (IsClosedImmersion.isClosedEmbedding
            (ι (σ ξ))).isInducing.topologicalKrullDim_le hX)
          ((Scheme.Modules.pullback (ι (σ ξ))).obj E) rank
          (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (ι (σ ξ)) E rank) =
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ)
    (hzero : ∀ j : Fin N, (∀ ξ : genericPointsOne X, σ ξ ≠ j) →
      @curveDegree k _ (Zs j) (ι j ≫ f) _
        (le_trans (IsClosedImmersion.isClosedEmbedding
          (ι j)).isInducing.topologicalKrullDim_le hX)
        ((Scheme.Modules.pullback (ι j)).obj E) rank
        (_root_.AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (ι j) E rank) = 0) :
    curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X,
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.curveDegree_eq_finsum_componentDegree_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Unconditional.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Unconditional.lean#L455).

> **[Stacks, Tag 0AYW].** The degree of a finite locally free module of constant rank on a
> proper scheme of dimension at most one over a field is the multiplicity-weighted sum of its
> degrees on the reduced one-dimensional components.
>
> The four steps are: the degree is the quantity `D(𝒫) = χ(𝒫 ⊗ ℰ) − n·χ(𝒫)` of
> [Stacks, Tag 0AYU] at `𝒫 = 𝒪_X`; `D` is additive along the dévissage of [Stacks, Tag 01YF]
> applied to `𝒪_X`; at each layer `D` is the weighted sum of the component degrees, the weights
> being the lengths of the layer at the generic points; and those lengths add up to the
> multiplicities.

```lean
theorem curveDegree_eq_finsum_componentDegree_of_isProper (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (hX : topologicalKrullDim X ≤ 1)
    (E : X.Modules) (rank : ℕ)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    _root_.AlgebraicGeometry.curveDegree k f hX E rank =
      ∑ᶠ ξ : genericPointsOne X,
        (componentMultiplicity X ξ : ℤ) * componentDegree k f hX E rank ξ
```

**`Stacks.AlgebraicGeometry.ComponentDegrees.exists_curveDegree_eq_finsum_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Unconditional.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ComponentMultiplicity/Unconditional.lean#L526). The attribute's comment: “the existential form the source states, with no hypothesis”.

> **[Stacks, Tag 0AYW]**, in the existential form the source states: each reduced
> one-dimensional component is proper over the base, has dimension at most one and carries a
> restriction of `ℰ` that is again finite locally free of the same rank, and the component formula
> holds with respect to those three proofs.

```lean
theorem exists_curveDegree_eq_finsum_of_isProper (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (hX : topologicalKrullDim X ≤ 1)
    (E : X.Modules) (rank : ℕ)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    ∃ (hproperC : ∀ ξ : genericPointsOne X, IsProper (reducedComponentι X ξ ≫ f))
      (hdimC : ∀ ξ : genericPointsOne X, topologicalKrullDim (reducedComponent X ξ) ≤ 1)
      (hrank : ∀ ξ : genericPointsOne X,
        _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
          ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank),
      _root_.AlgebraicGeometry.curveDegree k f hX E rank =
        ∑ᶠ ξ : genericPointsOne X,
          (componentMultiplicity X ξ : ℤ) *
            @curveDegree k _ (reducedComponent X ξ) (reducedComponentι X ξ ≫ f)
              (hproperC ξ) (hdimC ξ)
              ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj E) rank (hrank ξ)
```

## Tag 0AYX, a lemma

[Tag 0AYX](https://stacks.math.columbia.edu/tag/0AYX) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_tensorSheaf_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveDegreeTensor/Cohomological.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveDegreeTensor/Cohomological.lean#L185). The attribute's comment: “on a proper curve; the whole tag, on a proper scheme of dimension at most one, is AlgebraicGeometry.curveDegree\_tensorSheaf\_eq\_add\_of\_topologicalKrullDim\_le\_one”.

> **[Stacks, Tag 0AYX] on a proper curve.** For `ℰ` and `𝒱` finite locally free of constant
> ranks `n` and `m` on a proper curve over a field,
>
> `deg(ℰ ⊗ 𝒱) = m · deg(ℰ) + n · deg(𝒱)`.
>
> **No hypothesis beyond the source's own**, apart from the curve hypothesis discussed in the
> module docstring. The rank of the tensor product is
> `AlgebraicGeometry.SheafOfModules.isFiniteLocallyFreeOfRank_tensorSheaf`, and the two instances
> of [Stacks, Tag 02O6] over a field that [Stacks, Tag 0AYV] needs are supplied by
> `AlgebraicGeometry.forall_finiteDimensional_cohomologyOverField_of_isProper`.
>
> The proof is the arithmetic of [Stacks, Tag 0AYX]: the Euler characteristic of `ℰ ⊗ 𝒱` is
> `m · deg(ℰ) + n · χ(𝒱)` by [Stacks, Tag 0AYV], whose rank input is the fibre rank of `𝒱` at the
> generic point and hence `m`; every degree is then unfolded into Euler characteristics by
> `AlgebraicGeometry.curveDegree_eq_eulerCharacteristic_sub`, where the identity is linear
> arithmetic.

```lean
public theorem curveDegree_tensorSheaf_eq_add
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (E V : X.Modules) (n m : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} V m] :
    @curveDegree k _ X f _ hdim
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (V))) (n * m)
        (SheafOfModules.isFiniteLocallyFreeOfRank_tensorSheaf X E V n m) =
      (m : ℤ) * curveDegree k f hdim E n + (n : ℤ) * curveDegree k f hdim V m
```

**`AlgebraicGeometry.curveDegree_tensorSheaf_eq_add_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveDegreeTensor/Devissage.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveDegreeTensor/Devissage.lean#L599).

> For `ℰ` and `𝒱` finite locally free of constant ranks `n` and `m` on a scheme `X` proper of
> dimension at most one over a field `k`,
>
> `deg(ℰ ⊗ 𝒱) = m · deg(ℰ) + n · deg(𝒱)`.

```lean
theorem curveDegree_tensorSheaf_eq_add_of_topologicalKrullDim_le_one (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (E V : X.Modules) (n m : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} V m] :
    @curveDegree k _ X f _ hdim
        ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X.toRingedSpace)).presheaf,
            ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj (V))) (n * m)
        (SheafOfModules.isFiniteLocallyFreeOfRank_tensorSheaf X E V n m) =
      (m : ℤ) * curveDegree k f hdim E n + (n : ℤ) * curveDegree k f hdim V m
```

## Tag 0DJ5, a lemma

[Tag 0DJ5](https://stacks.math.columbia.edu/tag/0DJ5) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_eq_curveDegree_exteriorPower_eq_invertibleCurveDegree_determinant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeExteriorDeterminant.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeExteriorDeterminant.lean#L147).

> **[Stacks, Tag 0DJ5].** Let `k` be a field, `X` a proper scheme of dimension at most one over
> `k` and `ℰ` a finite locally free `𝒪_X`-module of constant rank `n`. Then
>
> `deg(ℰ) = deg(⋀ⁿ ℰ) = deg(det(ℰ))`.
>
> Both equalities are asserted, under exactly the source's hypotheses. `det(ℰ)` is the determinant
> of [Stacks, Tag 0FJN], `AlgebraicGeometry.Scheme.Modules.determinant`, and its invertibility —
> which `AlgebraicGeometry.invertibleCurveDegree` needs and the source does not assume — is derived
> from the rank of `ℰ` by `AlgebraicGeometry.Scheme.Modules.isInvertible_determinant`.
>
> The first equality is
> `AlgebraicGeometry.curveDegree_eq_curveDegree_exteriorPower_of_isProper`: the source's dévissage
> on a proper curve, passed to `X` through the one-dimensional components ([Stacks, Tag 0AYW]). The
> second is the identification `⋀ⁿ ℰ ≅ det(ℰ)` of [Stacks, Tag 0B37] together with the agreement of
> the invertible degree with the rank-one degree.

```lean
theorem curveDegree_eq_curveDegree_exteriorPower_eq_invertibleCurveDegree_determinant
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (n : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n] :
    curveDegree k f hdim E n =
        @curveDegree k _ X f _ hdim (Scheme.Modules.exteriorPower E (n : ℤ)) 1
          (Scheme.Modules.isFiniteLocallyFreeOfRank_exteriorPower_self E n) ∧
      @curveDegree k _ X f _ hdim (Scheme.Modules.exteriorPower E (n : ℤ)) 1
          (Scheme.Modules.isFiniteLocallyFreeOfRank_exteriorPower_self E n) =
        @invertibleCurveDegree k _ X f _ hdim (Scheme.Modules.determinant E)
          (Scheme.Modules.isInvertible_determinant E n)
```

## Tag 0AYY, a lemma

[Tag 0AYY](https://stacks.math.columbia.edu/tag/0AYY) in the Stacks Project.

**`AlgebraicGeometry.isFinite_and_curveDegree_tensorSheaf_invertibleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DivisorTwistDegree.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DivisorTwistDegree.lean#L270).

> **[Stacks, Tag 0AYY].** Let `k` be a field, let `X` be a proper scheme of dimension at most
> one over `k` and let `D` be an effective Cartier divisor on `X`. Then `D` is finite over
> `Spec(k)`, of degree
>
> `deg(D) = dim_k Γ(D, 𝒪_D)`,
>
> and for a finite locally free `ℰ` of rank `n`,
>
> `deg(ℰ(D)) = n · deg(D) + deg(ℰ)`,  where `ℰ(D) = ℰ ⊗_{𝒪_X} 𝒪_X(D)`.
>
> The three assertions are about one and the same number `dim_k Γ(D, 𝒪_D)`: it is the rank of the
> finite locally free morphism `D ⟶ Spec(k)` — which is what "finite of degree `deg(D)`" asserts —
> and it is the coefficient of `n` in the twist formula.
>
> Finiteness and the degree are `AlgebraicGeometry.isFinite_divisorSubscheme` and
> `AlgebraicGeometry.isFiniteLocallyFreeOfRank_divisorSubscheme`. The twist formula is
> [Stacks, Tag 0AYX], i.e.
> `AlgebraicGeometry.curveDegree_tensorSheaf_eq_add_of_topologicalKrullDim_le_one`,
> at `ℰ` and `𝒪_X(D)`, whose `deg(𝒪_X(D))` term is
> `AlgebraicGeometry.curveDegree_invertibleSheaf_eq_finrank_globalSections`.

```lean
theorem isFinite_and_curveDegree_tensorSheaf_invertibleSheaf (E : X.Modules) (n : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n] :
    letI : Algebra k Γ(D.subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ (D.subschemeι ≫ f).appTop).hom.toAlgebra
    IsFinite (D.subschemeι ≫ f) ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank (D.subschemeι ≫ f)
          (Module.finrank k Γ(D.subscheme, ⊤)) ∧
        @curveDegree k _ X f _ hdim
            ((((Stacks.SheafOfModules.Tensor.sheafTensor
              ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (E)).obj
              ((Stacks.Divisors.invertibleSheaf' D)))) n
            (isFiniteLocallyFreeOfRank_tensorSheaf_invertibleSheaf D E n) =
          (n : ℤ) * (Module.finrank k Γ(D.subscheme, ⊤) : ℤ) + curveDegree k f hdim E n
```

## Tag 0C6P, a lemma

[Tag 0C6P](https://stacks.math.columbia.edu/tag/0C6P) in the Stacks Project.

**`AlgebraicGeometry.isField_and_finite_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean#L103). The attribute's comment: “the global sections are a finite field extension”.

> For a proper scheme over a field which is reduced and connected, the ring of global sections
> is a finite field extension of the base field.

```lean
theorem isField_and_finite_globalSections (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] [IsReduced X] [ConnectedSpace X] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    IsField Γ(X, ⊤) ∧ Module.Finite k Γ(X, ⊤)
```

**`AlgebraicGeometry.finrank_globalSections_dvd_curveDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean#L156). The attribute's comment: “w divides the degree of a finite locally free sheaf”.

> For a proper scheme over a field which is reduced and connected and of dimension at most one,
> the degree of the extension `Γ(X, 𝒪_X)/k` divides the degree of every finite locally free sheaf
> of constant rank on `X`.

```lean
theorem finrank_globalSections_dvd_curveDegree (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] [IsReduced X] [ConnectedSpace X]
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    (Module.finrank k Γ(X, ⊤) : ℤ) ∣ curveDegree k f hdim E rank
```

**`AlgebraicGeometry.finrank_globalSections_dvd_finrank_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean#L173). The attribute's comment: “w divides the degree of a residue field”.

> For a proper scheme over a field which is reduced and connected, the degree of the extension
> `Γ(X, 𝒪_X)/k` divides the degree over `k` of the residue field at every point.

```lean
theorem finrank_globalSections_dvd_finrank_residueField (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] [IsReduced X] [ConnectedSpace X] (x : X) :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    Module.finrank k Γ(X, ⊤) ∣ Module.finrank k (X.residueField x)
```

**`AlgebraicGeometry.finrank_globalSections_dvd_finrank_globalSections_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/DegreeDivisibility.lean#L186). The attribute's comment: “w divides the degree of a zero-dimensional closed subscheme”.

> Let `X` be a proper scheme over a field which is reduced and connected and let `D ⊆ X` be a
> closed subscheme of dimension zero. Then `D` is finite locally free over `k` of rank
> `dim_k Γ(D, 𝒪_D)`, and the degree of the extension `Γ(X, 𝒪_X)/k` divides it.

```lean
theorem finrank_globalSections_dvd_finrank_globalSections_of_dimension_zero (k : Type u)
    [Field k] {X D : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] [IsReduced X]
    [ConnectedSpace X] (i : D ⟶ X) [IsClosedImmersion i] (hdimD : topologicalKrullDim D = 0) :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    letI : Algebra k Γ(D, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ (i ≫ f).appTop).hom.toAlgebra
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank (i ≫ f) (Module.finrank k Γ(D, ⊤)) ∧
      Module.finrank k Γ(X, ⊤) ∣ Module.finrank k Γ(D, ⊤)
```

## Tag 0AYZ, a lemma

[Tag 0AYZ](https://stacks.math.columbia.edu/tag/0AYZ) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_pullback_eq_degreeOver_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/PullbackDegree.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/PullbackDegree.lean#L332).

> Let `k` be a field, let `f : X ⟶ Y` be a nonconstant morphism of proper curves over `k` and
> let `ℰ` be a finite locally free `𝒪_Y`-module of constant rank `n`. Then
>
> `deg(f^*ℰ) = deg(X/Y)·deg(ℰ)`,
>
> where `deg(X/Y) = [R(X) : R(Y)]` is `AlgebraicGeometry.degreeOver` ([Stacks, Tag 02NY]) and `deg`
> is `AlgebraicGeometry.curveDegree` ([Stacks, Tag 0AYR]).

```lean
theorem curveDegree_pullback_eq_degreeOver_mul (k : Type u) [Field k] {X Y : Scheme.{u}}
    (πX : X ⟶ Spec (.of k)) (πY : Y ⟶ Spec (.of k))
    [IsCurve k πX] [IsCurve k πY] [IsProper πX] [IsProper πY]
    (f : X ⟶ Y) (hf : f ≫ πY = πX) (hnc : ¬ ∃ y : Y, ∀ x : X, f.base x = y)
    (E : Y.Modules) (n : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E n] :
    @curveDegree k _ X πX _ (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := πX)))
        ((Scheme.Modules.pullback f).obj E) n (isFiniteLocallyFreeOfRank_pullback f E n) =
      (@degreeOver X Y f _ _ (locallyOfFiniteType_of_isCurve_comp k πX πY f hf)
          (isDominant_of_not_constant k πX πY f hnc) : ℤ) *
        curveDegree k πY (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := πY))) E n
```

**`AlgebraicGeometry.curveDegree_pullback_eq_degreeOver_mul_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/PullbackDegree.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/PullbackDegree.lean#L422). References: SGA 6 X (4.4), “(4.4.3), special case”.

> Let `k` be a field, let `f : X ⟶ Y` be a nonconstant morphism of proper curves over `k` and
> let `ℰ` be a finite locally free `𝒪_Y`-module. Then
>
> `deg(f^*ℰ) = deg(X/Y)·deg(ℰ)`,
>
> where `deg(X/Y) = [R(X) : R(Y)]` is `AlgebraicGeometry.degreeOver` ([Stacks, Tag 02NY]) and `deg`
> is `AlgebraicGeometry.curveDegree` ([Stacks, Tag 0AYR]), both degrees taken at the fibre rank of
> `ℰ` at the generic point of `Y`.

```lean
theorem curveDegree_pullback_eq_degreeOver_mul_of_isFiniteLocallyFree (k : Type u) [Field k]
    {X Y : Scheme.{u}} (πX : X ⟶ Spec (.of k)) (πY : Y ⟶ Spec (.of k))
    [IsCurve k πX] [IsCurve k πY] [IsProper πX] [IsProper πY]
    (f : X ⟶ Y) (hf : f ≫ πY = πX) (hnc : ¬ ∃ y : Y, ∀ x : X, f.base x = y)
    (E : Y.Modules)
    [SheafOfModules.IsFiniteLocallyFree.{u, u, u} (R := Y.ringCatSheaf) E] :
    letI _hrank : SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E
        (Scheme.Modules.fiberRank E (genericPoint (Y : Type u))) :=
      Scheme.Modules.isFiniteLocallyFreeOfRank_of_fiberRank_eq E
        (Scheme.Modules.fiberRank E (genericPoint (Y : Type u)))
        (genericPoint (Y : Type u)) rfl
    @curveDegree k _ X πX _ (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := πX)))
        ((Scheme.Modules.pullback f).obj E)
        (Scheme.Modules.fiberRank E (genericPoint (Y : Type u)))
        (isFiniteLocallyFreeOfRank_pullback f E
          (Scheme.Modules.fiberRank E (genericPoint (Y : Type u)))) =
      (@degreeOver X Y f _ _ (locallyOfFiniteType_of_isCurve_comp k πX πY f hf)
          (isDominant_of_not_constant k πX πY f hnc) : ℤ) *
        curveDegree k πY (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := πY))) E
          (Scheme.Modules.fiberRank E (genericPoint (Y : Type u)))
```

## Tag 0B40, a lemma

[Tag 0B40](https://stacks.math.columbia.edu/tag/0B40) in the Stacks Project.

**`AlgebraicGeometry.invertibleCurveDegree_nonneg_of_eval_top_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L272). The attribute's comment: “part (1)”.

> **The degree of an invertible module with a nonzero global section is nonnegative**, on a
> proper integral scheme of dimension at most one over a field.

```lean
theorem invertibleCurveDegree_nonneg_of_eval_top_ne_zero [IsProper f] [IsIntegral X]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    (hs : s.eval (op ⊤) ≠ 0) :
    0 ≤ @invertibleCurveDegree k _ X f _ hdim L hL
```

**`AlgebraicGeometry.invertibleCurveDegree_pos_of_eval_top_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L377). The attribute's comment: “part (2)”.

> **A nonzero section with a zero forces positive degree.** On a proper integral scheme of
> dimension at most one over a field, a nonzero global section of an invertible module which
> vanishes at some point forces the degree of that module to be positive.

```lean
theorem invertibleCurveDegree_pos_of_eval_top_ne_zero [IsProper f] [IsIntegral X]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    (hs : s.eval (op ⊤) ≠ 0)
    (hzero : ∃ y : X, y ∉ nonvanishingLocus (X := X.toRingedSpace) L s) :
    0 < @invertibleCurveDegree k _ X f _ hdim L hL
```

**`AlgebraicGeometry.isIso_unitHomEquiv_symm_of_invertibleCurveDegree_nonpos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L432). The attribute's comment: “part (4), in the stronger form the source's proof supports and the text does not state: the multiplication map O\_X -> L of the given section is itself an isomorphism, not merely L isomorphic to O\_X abstractly. The weaker reading is the corollary isTrivial\_of\_invertibleCurveDegree\_nonpos beside it”.

> **A nonzero section of a module of nonpositive degree trivializes it.** On a proper integral
> scheme of dimension at most one over a field, let `ℒ` be an invertible module with `deg(ℒ) ≤ 0`
> and a nonzero global section `s`. Then multiplication by `s` is an isomorphism `𝒪_X ⟶ ℒ`.

```lean
theorem isIso_unitHomEquiv_symm_of_invertibleCurveDegree_nonpos [IsProper f] [IsIntegral X]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    (hs : s.eval (op ⊤) ≠ 0) (hdeg : @invertibleCurveDegree k _ X f _ hdim L hL ≤ 0) :
    IsIso (L.unitHomEquiv.symm s)
```

**`AlgebraicGeometry.isTrivial_of_invertibleCurveDegree_nonpos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L447). The attribute's comment: “part (4) as stated -- L is isomorphic to O\_X”.

> **An invertible module of nonpositive degree with a nonzero global section is trivial**, on
> a proper integral scheme of dimension at most one over a field.

```lean
theorem isTrivial_of_invertibleCurveDegree_nonpos [IsProper f] [IsIntegral X]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    (hs : s.eval (op ⊤) ≠ 0) (hdeg : @invertibleCurveDegree k _ X f _ hdim L hL ≤ 0) :
    SheafOfModules.IsTrivial X.presheaf X.ringCatSheaf.property L
```

**`AlgebraicGeometry.isTrivial_of_eval_top_ne_zero_of_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L537). The attribute's comment: “part (3)”.

> **An invertible module whose inverse also has a nonzero section is trivial.** If an
> invertible module `ℒ` on an integral scheme universally closed over a field and its inverse
> `ℒ^{⊗ -1}` both have nonzero global sections, then `ℒ ≅ 𝒪_X`.

```lean
theorem isTrivial_of_eval_top_ne_zero_of_inverse [IsIntegral X] [UniversallyClosed f]
    (L : X.Modules) [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (s : L.sections) (hs : s.eval (op ⊤) ≠ 0)
    (t : (tensorPowerModule L (-1)).sections) (ht : t.eval (op ⊤) ≠ 0) :
    SheafOfModules.IsTrivial X.presheaf X.ringCatSheaf.property L
```

**`AlgebraicGeometry.invertibleCurveDegree_le_of_hom_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L706). The attribute's comment: “part (5), the inequality deg(N) <= deg(L)”.

> **A nonzero morphism of invertible modules does not decrease the degree.** On a proper
> curve over a field, a nonzero morphism `𝒩 ⟶ ℒ` of invertible modules forces
> `deg(𝒩) ≤ deg(ℒ)`.

```lean
theorem invertibleCurveDegree_le_of_hom_ne_zero [IsCurve k f] [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (N L : X.Modules)
    [hN : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property N]
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (φ : N ⟶ L) (hφ : φ ≠ 0) :
    invertibleCurveDegree k f hdim N ≤ invertibleCurveDegree k f hdim L
```

**`AlgebraicGeometry.isIso_of_invertibleCurveDegree_eq_of_hom_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L724). The attribute's comment: “part (5), the equality case: the morphism is an isomorphism”.

> **A nonzero morphism of invertible modules of equal degree is an isomorphism**, on a proper
> curve over a field.

```lean
theorem isIso_of_invertibleCurveDegree_eq_of_hom_ne_zero [IsCurve k f] [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (N L : X.Modules)
    [hN : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property N]
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (φ : N ⟶ L) (hφ : φ ≠ 0)
    (heq : invertibleCurveDegree k f hdim N = invertibleCurveDegree k f hdim L) : IsIso φ
```

**`AlgebraicGeometry.invertibleCurveDegree_eq_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/SectionDegree.lean#L750). The attribute's comment: “part (5), the converse of the equality case: an isomorphism has equal degrees, so the equality holds exactly when the morphism is an isomorphism”.

> **An isomorphism of invertible modules preserves the degree**, on a proper scheme of
> dimension at most one over a field.

```lean
theorem invertibleCurveDegree_eq_of_isIso [IsProper f] (hdim : topologicalKrullDim X ≤ 1)
    (N L : X.Modules)
    [hN : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property N]
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (φ : N ⟶ L) [IsIso φ] :
    invertibleCurveDegree k f hdim N = invertibleCurveDegree k f hdim L
```

## Tag 0E22, a lemma

[Tag 0E22](https://stacks.math.columbia.edu/tag/0E22) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_globalSections_or_isTrivial_of_invertibleCurveDegree_nonpos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/NonpositiveDegreeSection.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/NonpositiveDegreeSection.lean#L238).

> Let `k` be a field and `X` a proper scheme over `k` which is reduced, connected and
> equidimensional of dimension one, and let `ℒ` be an invertible `𝒪_X`-module whose restriction to
> every irreducible component of `X` has degree `≤ 0`. Then either `H⁰(X, ℒ) = 0` or `ℒ ≅ 𝒪_X`.

```lean
theorem subsingleton_globalSections_or_isTrivial_of_invertibleCurveDegree_nonpos [IsReduced X]
    [ConnectedSpace X] (_hequi : TopologicalSpace.Equidimensional (X : Type u))
    (hdim : topologicalKrullDim (X : Type u) = 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hdeg : ∀ (C : Set X) (hC : C ∈ irreducibleComponents (X : Type u)),
      haveI : SheafOfModules.IsInvertible
          (Scheme.IdealSheafData.vanishingIdeal
            ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subscheme.presheaf
          (Scheme.IdealSheafData.vanishingIdeal
            ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subscheme.ringCatSheaf.2
          ((RingedSpaceModuleAdjunction.modulePullback
            (Scheme.IdealSheafData.vanishingIdeal
              ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subschemeι.toLRSHom.toShHom).obj
            L) :=
        RingedSpaceModuleAdjunction.modulePullback_isInvertible_scheme _ L
      invertibleCurveDegree k
          ((Scheme.IdealSheafData.vanishingIdeal
            ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subschemeι ≫ f)
          ((StacksTag09NX.topologicalKrullDim_le_of_isClosedImmersion
            (Scheme.IdealSheafData.vanishingIdeal
              ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subschemeι).trans hdim.le)
          ((RingedSpaceModuleAdjunction.modulePullback
            (Scheme.IdealSheafData.vanishingIdeal
              ⟨C, isClosed_of_mem_irreducibleComponents C hC⟩).subschemeι.toLRSHom.toShHom).obj
            L) ≤ 0) :
    Subsingleton Γ(L, ⊤) ∨ SheafOfModules.IsTrivial X.presheaf X.ringCatSheaf.2 L
```

## Tag 0B5X, a lemma

[Tag 0B5X](https://stacks.math.columbia.edu/tag/0B5X) in the Stacks Project.

**`AlgebraicGeometry.isAmple_iff_invertibleCurveDegree_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CurveAmple.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CurveAmple.lean#L154). The attribute's comment: “both directions, for a proper curve over a field”.

> **[Stacks, Tag 0B5X].** Let `k` be a field, `X` a proper curve over `k` and `𝓛` an invertible
> `𝒪_X`-module. Then `𝓛` is ample if and only if `deg(𝓛) > 0`.
>
> The forward direction is `AlgebraicGeometry.invertibleCurveDegree_pos_of_isAmple_of_isCurve` of
> `./CurveInputs.lean`. The converse composes the source's second paragraph,
> `AlgebraicGeometry.hasAffinePowerOfDegreePos_of_isCurve` of `./CurveSection.lean`, with its third,
> which enters through `AlgebraicGeometry.isAmple_of_exists_tensorPower_section_of_isCurve` above.
>
> `hdim` is an explicit argument because `AlgebraicGeometry.invertibleCurveDegree` takes the
> dimension bound as one; on a curve it is `le_of_eq (IsCurve.topologicalKrullDim_eq_one f)`, and it
> is an unused argument of that definition, so any two proofs of it give the same degree.

```lean
public theorem isAmple_iff_invertibleCurveDegree_pos [IsCurve k f] [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    Scheme.Modules.IsAmple X L ↔ 0 < invertibleCurveDegree k f hdim L
```

**`AlgebraicGeometry.invertibleCurveDegree_pos_of_isAmple_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CurveInputs.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CurveInputs.lean#L241). The attribute's comment: “the implication: `L` ample ⟹ `deg(L) > 0`, with no hypothesis beyond the tag's own; both directions are registered on `isAmple_iff_invertibleCurveDegree_pos`”.

> **The forward direction of [Stacks, Tag 0B5X], at the source's hypotheses.** On a proper
> curve over a field an ample invertible module has positive degree.
>
> This is `AlgebraicGeometry.invertibleCurveDegree_pos_of_isAmple_of_devissage` with each of its
> four inputs supplied by the theorems above.
>
> The converse implication is `AlgebraicGeometry.isAmple_iff_invertibleCurveDegree_pos` of
> `CurveAmple.lean`, which states both directions.

```lean
public theorem invertibleCurveDegree_pos_of_isAmple_of_isCurve [IsCurve k f] [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) :
    0 < invertibleCurveDegree k f hdim L
```

## Tag 0B5Y, a lemma

[Tag 0B5Y](https://stacks.math.columbia.edu/tag/0B5Y) in the Stacks Project.

**`AlgebraicGeometry.isAmple_iff_forall_invertibleCurveDegree_reducedComponent_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/ComponentCriterion.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/ComponentCriterion.lean#L302). The attribute's comment: “both directions, at the tag's own indexing by the one-dimensional irreducible components with their reduced induced closed subscheme structure”.

> **[Stacks, Tag 0B5Y], both directions.** Let `k` be a field, let `X` be a scheme proper of
> dimension at most one over `k` and let `𝓛` be an invertible `𝒪_X`-module. Then `𝓛` is ample if
> and only if the degree of the restriction of `𝓛` to every one-dimensional irreducible component
> of `X`, taken with its reduced induced closed subscheme structure, is positive.
>
> The components of dimension one are the tag's `C₁, …, C_t`: they are indexed by their generic
> points, `Stacks.AlgebraicGeometry.ComponentDegrees.genericPointsOne X`, the reduced induced
> subscheme is `Stacks.AlgebraicGeometry.ComponentDegrees.reducedComponent`, and that it is a
> proper curve over `k` is proved with no hypothesis.
>
> The implication (1) ⟹ (2) is
> `AlgebraicGeometry.invertibleCurveDegree_reducedComponent_pos_of_isAmple` of
> `./ComponentPositivity.lean`, which has no hypothesis beyond the tag's own.
>
> For the implication (2) ⟹ (1) the covering family of the source is formed: all the irreducible
> components, which are finitely many because a scheme proper over a field is Noetherian. Each has
> dimension zero or one. On a zero-dimensional one the restriction of `𝓛` is ample outright, and on
> a one-dimensional one positivity of the degree makes it ample by the converse direction of
> [Stacks, Tag 0B5X]; ampleness then descends to `X` along the finite surjection from the disjoint
> union, by [Stacks, Tag 0B5V] together with
> `AlgebraicGeometry.isAmple_sigma_of_forall_isAmple_pullback_sigmaι`.
>
> **No hypothesis beyond the tag's own.**

```lean
public theorem isAmple_iff_forall_invertibleCurveDegree_reducedComponent_pos
    (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L] :
    Scheme.Modules.IsAmple X L ↔
      ∀ ζ : genericPointsOne X,
        0 < @invertibleCurveDegree k _ (reducedComponent X ζ) (reducedComponentι X ζ ≫ f)
          (isProper_reducedComponentι_comp k f ζ)
          (topologicalKrullDim_reducedComponent_le X hdim ζ)
          ((Scheme.Modules.pullback (reducedComponentι X ζ)).obj L)
          (SheafOfModules.isInvertible_pullback (reducedComponentι X ζ) L)
```

**`AlgebraicGeometry.invertibleCurveDegree_reducedComponent_pos_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/ComponentPositivity.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/ComponentPositivity.lean#L246). The attribute's comment: “the implication (1) ⟹ (2), at the tag's own indexing by the one-dimensional irreducible components with their reduced induced structure, with no hypothesis beyond the tag's own; the full equivalence is registered on `isAmple_iff_forall_invertibleCurveDegree_reducedComponent_pos`”.

> **The implication (1) ⟹ (2) of [Stacks, Tag 0B5Y].** Let `k` be a field, let `X` be proper of
> dimension at most one over `k` and let `𝓛` be an ample invertible `𝒪_X`-module. Then the degree
> of the restriction of `𝓛` to every one-dimensional irreducible component of `X`, taken with its
> reduced induced closed subscheme structure, is positive.
>
> The components of dimension one are indexed by their generic points,
> `Stacks.AlgebraicGeometry.ComponentDegrees.genericPointsOne X`, and the reduced induced subscheme
> is `Stacks.AlgebraicGeometry.ComponentDegrees.reducedComponent`; that it is a proper curve over
> `k` — integral, separated, of finite type and of dimension exactly one — is
> `Stacks.AlgebraicGeometry.ComponentDegrees.isCurve_reducedComponentι_comp` together with
> `Stacks.AlgebraicGeometry.ComponentDegrees.isProper_reducedComponentι_comp`, both proved with no
> hypothesis. So this is the tag's own family `C₁, …, C_t` and its own conclusion.
>
> **No hypothesis beyond the tag's own.** The reverse implication is
> `AlgebraicGeometry.isAmple_iff_forall_invertibleCurveDegree_reducedComponent_pos` of
> `ComponentCriterion.lean`, which states the full equivalence.

```lean
public theorem invertibleCurveDegree_reducedComponent_pos_of_isAmple [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) (ξ : genericPointsOne X) :
    0 < @invertibleCurveDegree k _ (reducedComponent X ξ) (reducedComponentι X ξ ≫ f)
      (isProper_reducedComponentι_comp k f ξ)
      (topologicalKrullDim_reducedComponent_le X hdim ξ)
      ((Scheme.Modules.pullback (reducedComponentι X ξ)).obj L)
      (SheafOfModules.isInvertible_pullback (reducedComponentι X ξ) L)
```

## Tag 0B8Z, a lemma

[Tag 0B8Z](https://stacks.math.columbia.edu/tag/0B8Z) in the Stacks Project.

**`AlgebraicGeometry.exists_invertible_finrank_cohomologyOverField_zero_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomology.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomology.lean#L237). The attribute's comment: “assertion (1)”.

> **[Stacks, Tag 0B8Z], assertion (1).** On a proper curve over an algebraically closed field
> there is an invertible module `ℒ` with `dim_k H⁰(X, ℒ) = 1` and `H¹(X, ℒ) = 0`.
>
> Starting from an invertible module with vanishing `H¹` and a nonzero global section
> (`AlgebraicGeometry.exists_invertible_isZero_cohomologyOverField_one_and_zero_lt_finrank`) and
> twisting down `dim_k H⁰(X, ℒ₀) - 1` times by
> `AlgebraicGeometry.exists_pointTwistDown`, each step lowering `dim_k H⁰` by one and preserving
> the vanishing of `H¹`.

```lean
public theorem exists_invertible_finrank_cohomologyOverField_zero_eq_one [IsAlgClosed k]
    [IsProper f] [IsCurve k f] :
    ∃ L : X.Modules, SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L ∧
      Module.finrank k (cohomologyOverField k f L 0) = 1 ∧
        IsZero (cohomologyOverField k f L 1)
```

**`AlgebraicGeometry.exists_invertible_isZero_cohomologyOverField_zero_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomology.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomology.lean#L256). The attribute's comment: “assertion (2), the vanishing of both `H⁰` and `H¹`”.

> **[Stacks, Tag 0B8Z], assertion (2).** On a proper curve over an algebraically closed field
> there is an invertible module `𝒩` with `H⁰(X, 𝒩) = 0` and `H¹(X, 𝒩) = 0`.
>
> The same descent as for assertion (1), run one step further, down to `dim_k H⁰ = 0`; the
> vanishing of `H⁰` — rather than only its dimension — comes from the finite dimensionality
> carried along the induction.

```lean
public theorem exists_invertible_isZero_cohomologyOverField_zero_one [IsAlgClosed k] [IsProper f]
    [IsCurve k f] :
    ∃ N : X.Modules, SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N ∧
      IsZero (cohomologyOverField k f N 0) ∧ IsZero (cohomologyOverField k f N 1)
```

## Tag 0B90, a lemma

[Tag 0B90](https://stacks.math.columbia.edu/tag/0B90) in the Stacks Project.

**`AlgebraicGeometry.isZero_cohomologyOverField_one_of_two_mul_genus_sub_one_le_invertibleCurveDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LargeDegreeVanishing.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LargeDegreeVanishing.lean#L641). The attribute's comment: “the whole statement: `H¹(X, L) = 0` for every invertible `O_X`-module `L` with `deg(L) ≥ 2g - 1` on a proper curve `X` over an algebraically closed field, with `g` the genus”.

> **[Stacks, Tag 0B90].** Let `k` be an algebraically closed field, let `X` be a proper curve
> over `k` and let `g = dim_k H¹(X, 𝒪_X)`. Then `H¹(X, ℒ) = 0` for every invertible
> `𝒪_X`-module `ℒ` with `deg(ℒ) ≥ 2g - 1`.
>
> Let `𝒩` be the invertible module of [Stacks, Tag 0B8Z] (2), of degree `g - dim_k H⁰(X, 𝒪_X)`.
> Then `ℒ ⊗ 𝒩^{⊗ -1}` has degree `deg(ℒ) - g + dim_k H⁰(X, 𝒪_X)`, so
>
> `dim_k H⁰(ℒ ⊗ 𝒩^{⊗ -1}) - dim_k H¹(ℒ ⊗ 𝒩^{⊗ -1}) = deg(ℒ) - 2g + 2 dim_k H⁰(X, 𝒪_X) ≥ 1`
>
> because `dim_k H⁰(X, 𝒪_X) ≥ 1` on a proper integral scheme; hence `ℒ ⊗ 𝒩^{⊗ -1}` has a nonzero
> global section and `isZero_cohomologyOverField_one_of_tensorInverse_section` applies.

```lean
public theorem isZero_cohomologyOverField_one_of_two_mul_genus_sub_one_le_invertibleCurveDegree
    [IsAlgClosed k] [IsProper f] [IsCurve k f] (L : X.Modules)
    (hL : SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hdeg : 2 * (genus f : ℤ) - 1 ≤ @invertibleCurveDegree k _ X f _
      (IsCurve.topologicalKrullDim_eq_one (k := k) (f := f)).le L hL) :
    IsZero (cohomologyOverField k f L 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.44, Tag 0AYQ](https://stacks.math.columbia.edu/tag/0AYQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
