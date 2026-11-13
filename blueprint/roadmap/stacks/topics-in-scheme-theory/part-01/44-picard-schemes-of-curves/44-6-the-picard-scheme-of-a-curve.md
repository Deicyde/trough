---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_c_baseChange_of_isCurve_of_section, Stacks.RigidifiedPicard.cohomologyLocus, Stacks.RigidifiedPicard.isOpenSubfunctor_cohomologyLocus, AlgebraicGeometry.genus, Stacks.RigidifiedPicard.exists_representableBy_cohomologyLocus, AlgebraicGeometry.exists_invertible_baseChangeTwist_finrank_eq_one_of_isSepClosed, AlgebraicGeometry.exists_finrank_cohomologyOverField_add_schemePullbackClass_eq_one, AlgebraicGeometry.exists_invertible_baseChangeTwist_finrank_cohomologyOverField_eq_one_of_isSepClosed
statement: formalized
proof: formalized
---

# 44.6 The Picard scheme of a curve

Section 44.6 of the Stacks Project, [Tag 0B9R](https://stacks.math.columbia.edu/tag/0B9R). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B9U, a lemma

[Tag 0B9U](https://stacks.math.columbia.edu/tag/0B9U) in the Stacks Project.

**`AlgebraicGeometry.isIso_c_baseChange_of_isCurve_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSchemeCurve/PointedCurveStructureSheaf.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSchemeCurve/PointedCurveStructureSheaf.lean#L216).

> Let `k` be a field and let `X` be a smooth projective curve over `k` with a `k`-rational
> point, given as a section `σ` of its structure morphism `f`. Then `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` is an
> isomorphism for every `k`-scheme `T`.

```lean
theorem isIso_c_baseChange_of_isCurve_of_section {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsCurve k f] [IsProjectiveVariety k f] [Smooth f]
    (σ : Spec (.of k) ⟶ X) (hσ : σ ≫ f = 𝟙 _)
    {T : Scheme.{u}} (g : T ⟶ Spec (.of k)) :
    IsIso (pullback.snd f g).toLRSHom.toHom.c
```

## Tag 0B9V, a lemma

[Tag 0B9V](https://stacks.math.columbia.edu/tag/0B9V) in the Stacks Project.

**`Stacks.RigidifiedPicard.cohomologyLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/CohomologyLocus.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/CohomologyLocus.lean#L53). The attribute's comment: “F is a subfunctor, for f flat, proper and locally of finite presentation with a section (the source's smooth projective curve over a field with a rational point is a special case)”.

> The rigidified classes `ℒ ∈ Pic_{X/S,σ}(T)` with `Rf_{T,*}ℒ` isomorphic to an invertible
> `𝒪_T`-module placed in degree `0`, as a subfunctor of `Pic_{X/S,σ}`.

```lean
def cohomologyLocus : Subfunctor (functor f σ hσ ⋙ forget GrpCat)
```

**`Stacks.RigidifiedPicard.isOpenSubfunctor_cohomologyLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/CohomologyLocus.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/CohomologyLocus.lean#L74). The attribute's comment: “the inclusion is representable by open immersions, for f flat, proper and locally of finite presentation with a section”.

> The inclusion `F ⊆ Pic_{X/S,σ}` is representable by open immersions, in the elementwise form
> of [Stacks, Tag 01JI]: for every `S`-scheme `T` and every `ℒ ∈ Pic_{X/S,σ}(T)` there is an open
> `U ⊆ T` such that for every `g : T' ⟶ T` over `S`, the restriction of `ℒ` to `T'` lies in `F(T')`
> exactly when `g` maps `T'` into `U`.

```lean
theorem isOpenSubfunctor_cohomologyLocus : IsOpenSubfunctor (cohomologyLocus f σ hσ)
```

## Tag 0B9W, a definition

[Tag 0B9W](https://stacks.math.columbia.edu/tag/0B9W) in the Stacks Project.

**`AlgebraicGeometry.genus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Basic.lean#L59). The attribute's comment: “smooth projective geometrically irreducible curve over a field”.

> The genus of a scheme `X` over a field `k`, namely `dim_k H¹(X, 𝒪_X)`.

```lean
noncomputable def genus {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : ℕ
```

## Tag 0B9X, a lemma

[Tag 0B9X](https://stacks.math.columbia.edu/tag/0B9X) in the Stacks Project.

**`Stacks.RigidifiedPicard.exists_representableBy_cohomologyLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurve.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurve.lean#L282).

> **[Stacks, Tag 0B9X].** Let `k` be a field and `X` a smooth projective curve of genus `g` over
> `k` with a rational point `σ`. The open subfunctor `F ⊆ Pic_{X/k,σ}` of [Stacks, Tag 0B9V] is
> representable by an open subscheme of `Hilb^g_{X/k}`.

```lean
theorem exists_representableBy_cohomologyLocus (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsCurve k f] [Smooth f] (hproj : IsProjectiveMorphism f)
    (σ : Spec (.of k) ⟶ X) (hσ : σ ≫ f = 𝟙 _) :
    haveI : IsProper f := isProper_of_isProjectiveMorphism f hproj
    haveI : GeometricallyIrreducible f := geometricallyIrreducible_of_isCurve_of_section k f σ hσ
    haveI : SmoothOfRelativeDimension 1 f := smoothOfRelativeDimension_one_of_isCurve k f
    ∀ (H : Over (Spec (.of k)))
      (_ : Stacks.Hilbert.RepresentsHilbertFunctorOfRank (Over.mk f) H (genus f)),
      ∃ W : H.left.Opens, Nonempty ((cohomologyLocus f σ hσ).toFunctor.RepresentableBy
        (Over.mk (W.ι ≫ H.hom)))
```

## Tag 0B9Y, a lemma

[Tag 0B9Y](https://stacks.math.columbia.edu/tag/0B9Y) in the Stacks Project.

**`AlgebraicGeometry.exists_invertible_baseChangeTwist_finrank_eq_one_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/BaseChangeTwistLowCohomology.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/BaseChangeTwistLowCohomology.lean#L438). The attribute's comment: “for X\_K given as any pullback square of X ⟶ Spec k along Spec K ⟶ Spec k, with L ⊗ L₀|\_\{X\_K} the twist baseChangeTwist p L L₀ = L ⊗ p^*L₀”.

> **Stacks Project, Tag 0B9Y.** Let `k` be a separably closed field, `X` a smooth projective
> curve over `k`, `K/k` a field extension and `X' = X_K` the base change, given as any pullback
> square with `X ⟶ Spec k ⟵ Spec K`. For every invertible sheaf `L` on `X'` there is an invertible
> sheaf `L₀` on `X` with
>
> `dim_K H⁰(X', L ⊗ p^*L₀) = 1` and `dim_K H¹(X', L ⊗ p^*L₀) = 0`.
>
> The proof is the source's: the start of the descending induction is
> `AlgebraicGeometry.ampleTwistStart`, its step is `AlgebraicGeometry.pointIdealTwistStep`, and the
> induction joining them is `AlgebraicGeometry.exists_hasPrescribedLowCohomology_one`, whose
> cohomology is Tag 0B8Z's step lemma. The genus `g` of the source occurs in neither the assertion
> nor the proof and is not a parameter. This form, for an arbitrary pullback square, is the one
> `Stacks.PicardFunctor.TwistToNormalized` quantifies over.

```lean
theorem exists_invertible_baseChangeTwist_finrank_eq_one_of_isSepClosed
    (k K : Type u) [Field k] [IsSepClosed k] [Field K] [Algebra k K]
    {X X' : Scheme.{u}} (f : X ⟶ Spec (.of k)) (f' : X' ⟶ Spec (.of K)) (p : X' ⟶ X)
    (hp : IsPullback p f' f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
    [IsCurve k f] [Smooth f] (hproj : IsProjective f)
    (L : X'.Modules) [Stacks.Ample.IsInvertibleModule X' L] :
    ∃ L₀ : X.Modules, Stacks.Ample.IsInvertibleModule X L₀ ∧
      Module.finrank K (cohomologyOverField K f' (baseChangeTwist p L L₀) 0) = 1 ∧
      Module.finrank K (cohomologyOverField K f' (baseChangeTwist p L L₀) 1) = 0
```

**`AlgebraicGeometry.exists_finrank_cohomologyOverField_add_schemePullbackClass_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomologyFieldExtension.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomologyFieldExtension.lean#L501). The attribute's comment: “on Picard classes: the class c of the invertible sheaf L on X\_K and the class c₀ of L₀ on X, with c + p^*c₀ the class of L ⊗ L₀|\_\{X\_K}; H¹ = 0 is stated as vanishing, which gives dim\_K H¹ = 0. Properness of X is used in place of projectivity”.

> Let `k` be a separably closed field, `X` a smooth proper curve over `k`, `K/k` a field
> extension and `p : X_K ⟶ X` the projection of the base change. For every Picard class `c` on
> `X_K` (the class of an invertible `𝓛`) there is a Picard class `c₀` on `X` (the class of an
> invertible `𝓛₀`) such that the class `c + p^*c₀` (that of `𝓛 ⊗ 𝓛₀|_{X_K}`) has
>
> `dim_K H⁰(X_K, c + p^*c₀) = 1` and `H¹(X_K, c + p^*c₀) = 0`.

```lean
theorem exists_finrank_cohomologyOverField_add_schemePullbackClass_eq_one
    [IsSepClosed k] [IsProper f] [IsCurve k f] [Smooth f] (c : Stacks.Picard.ofScheme 𝔛) :
    ∃ c₀ : Stacks.Picard.ofScheme X,
      Module.finrank K (cohomologyOverField K 𝔣
        (Stacks.Picard.picardRepresentative (𝔛).toRingedSpace
          (c + Stacks.Picard.schemePullbackClass 𝔭 c₀)).obj 0) = 1 ∧
      IsZero (cohomologyOverField K 𝔣
        (Stacks.Picard.picardRepresentative (𝔛).toRingedSpace
          (c + Stacks.Picard.schemePullbackClass 𝔭 c₀)).obj 1)
```

**`AlgebraicGeometry.exists_invertible_baseChangeTwist_finrank_cohomologyOverField_eq_one_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomologyFieldExtension.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PrescribedLowCohomologyFieldExtension.lean#L522). The attribute's comment: “the source's statement on sheaves, with L ⊗ L₀|\_\{X\_K} the twist baseChangeTwist p L L₀ = L ⊗ p^*L₀; properness of X is used in place of projectivity”.

> Let `k` be a separably closed field, `X` a smooth proper curve over `k`, `K/k` a field
> extension and `p : X_K ⟶ X` the projection of the base change. For every invertible
> `𝒪_{X_K}`-module `𝓛` there is an invertible `𝒪_X`-module `𝓛₀` with
>
> `dim_K H⁰(X_K, 𝓛 ⊗ p^*𝓛₀) = 1` and `dim_K H¹(X_K, 𝓛 ⊗ p^*𝓛₀) = 0`.

```lean
theorem exists_invertible_baseChangeTwist_finrank_cohomologyOverField_eq_one_of_isSepClosed
    [IsSepClosed k] [IsProper f] [IsCurve k f] [Smooth f]
    (L : (𝔛).Modules) [hL : Stacks.Ample.IsInvertibleModule 𝔛 L] :
    ∃ L₀ : X.Modules, Stacks.Ample.IsInvertibleModule X L₀ ∧
      Module.finrank K (cohomologyOverField K 𝔣 (baseChangeTwist 𝔭 L L₀) 0) = 1 ∧
      Module.finrank K (cohomologyOverField K 𝔣 (baseChangeTwist 𝔭 L L₀) 1) = 0
```

## Tag 0B9Z, a proposition

[Tag 0B9Z](https://stacks.math.columbia.edu/tag/0B9Z) in the Stacks Project.

**`Stacks.PicardFunctor.isRepresentable_picardFunctor_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/CurvePicard/PicardCurveRepresentable.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/CurvePicard/PicardCurveRepresentable.lean#L53).

> **Stacks Project, Tag 0B9Z.** Let `k` be a separably closed field and `X` a smooth projective
> curve over `k`. The Picard functor `Pic_{X/k}` is representable.

```lean
theorem isRepresentable_picardFunctor_of_isSepClosed [IsSepClosed k]
    [IsCurve k (B.inclusion.map f)] [Smooth (B.inclusion.map f)]
    [IsProjectiveVariety k (B.inclusion.map f)] :
    (picardFunctor B hX hk f).IsRepresentable
```

**`Stacks.RigidifiedPicard.isRepresentable_picardFunctor_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardFunctorRepresentable.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardFunctorRepresentable.lean#L216).

> **[Stacks, Tag 0B9Z].** Let `k` be a separably closed field and `X` a smooth projective curve
> over `k`. The Picard functor `Pic_{X/k}` is representable.

```lean
theorem isRepresentable_picardFunctor_of_isSepClosed (k : Type u) [Field k] [IsSepClosed k]
    (B : BigFppfSite.{u}) {X : Scheme.{u}} (hX : B.Contains X) (hk : B.Contains (Spec (.of k)))
    (f : B.obj hX ⟶ B.obj hk) [IsCurve k (B.inclusion.map f)] [Smooth (B.inclusion.map f)]
    (hproj : IsProjectiveMorphism (B.inclusion.map f)) :
    (Stacks.PicardFunctor.picardFunctor B hX hk f).IsRepresentable
```

**`Stacks.RigidifiedPicard.exists_grp_iso_functor_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurve.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurve.lean#L301). The attribute's comment: “as the rigidified functor Pic\_\{X/k,σ} at a rational point σ, which the source's proof identifies with Pic\_\{X/k}”.

> **[Stacks, Tag 0B9Z].** The Picard functor of a smooth projective curve `X` over a separably
> closed field `k` is representable: for a rational point `σ`, the rigidified Picard functor
> `Pic_{X/k,σ} ≅ Pic_{X/k}` is represented by a group scheme over `k`.

```lean
theorem exists_grp_iso_functor_of_isSepClosed (k : Type u) [Field k] [IsSepClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [Smooth f]
    (hproj : IsProjectiveMorphism f) :
    haveI : IsProper f := isProper_of_isProjectiveMorphism f hproj
    ∃ (σ : Spec (.of k) ⟶ X) (hσ : σ ≫ f = 𝟙 _) (P : Grp (Over (Spec (.of k)))),
      Nonempty (yonedaGrp.obj P ≅ functor f σ hσ)
```

## Tag 0BA0, a lemma

[Tag 0BA0](https://stacks.math.columbia.edu/tag/0BA0) in the Stacks Project.

**`Stacks.AbelMap.picardScheme_clause_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean#L87). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0BA0, clause (1).**

```lean
theorem picardScheme_clause_one :
    haveI := geometricallyIrreducible_of_isSepClosed B hX hk f
    haveI := isProjectiveVariety_of_isProjective B hX hk f hproj
    haveI := isRepresentable_picardFunctor_of_isSepClosed B hX hk f
    Nonempty (IsColimit (Cofan.mk (picardScheme B hX hk f)
        fun d => (picardDegreeLocus B hX hk f (curveSection B hX hk f)
          (curveSection_comp B hX hk f) d).ι)) ∧
      ∀ d : ℤ, SmoothOfRelativeDimension (genus (B.inclusion.map f))
          (picardDegreeComponentHom B hX hk f (curveSection B hX hk f)
            (curveSection_comp B hX hk f) d) ∧
        IsProper (picardDegreeComponentHom B hX hk f (curveSection B hX hk f)
            (curveSection_comp B hX hk f) d) ∧
        IsVariety k (picardDegreeComponentHom B hX hk f (curveSection B hX hk f)
            (curveSection_comp B hX hk f) d) ∧
        topologicalKrullDim (B.inclusion.obj (picardSchemeDegreeComponent B hX hk f
            (curveSection B hX hk f) (curveSection_comp B hX hk f) d).left) =
          (genus (B.inclusion.map f) : WithBot ℕ∞)
```

**`Stacks.AbelMap.picardScheme_clause_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean#L127). The attribute's comment: “(3)”.

> **Stacks Project, Tag 0BA0, clause (3).**

```lean
theorem picardScheme_clause_three :
    haveI := geometricallyIrreducible_of_isSepClosed B hX hk f
    haveI := isProjectiveVariety_of_isProjective B hX hk f hproj
    haveI := isRepresentable_picardFunctor_of_isSepClosed B hX hk f
    ∃ H : AlgebraicGeometry.OpenSubgroupScheme (picardGrp B hX hk f),
      IsClosedImmersion H.ι.hom.hom.left ∧
        Set.range H.ι.hom.hom.left.base = (picardDegreeLocus B hX hk f (curveSection B hX hk f)
          (curveSection_comp B hX hk f) 0 : Set (picardScheme B hX hk f))
```

**`Stacks.AbelMap.picardScheme_clauses_four_five_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurve.lean#L161). The attribute's comment: “(4), (5) and (6)”.

> **Stacks Project, Tag 0BA0, clauses (4), (5) and (6).** For every `d ≥ 0` the degree-`d`
> Hilbert scheme `Hilb^d_{X/k}` exists in the site ([Stacks, Tag 0B9I]), and for every scheme `H`
> representing it there is a unique morphism `γ_d : H ⟶ Pic^d_{X/k}` classifying the invertible
> module `𝒪(D_univ)` of the universal divisor (clause (4)); it is surjective for `d ≥ g` and smooth
> for `d ≥ 2g - 1` (clause (5)), and birational for `d = g` (clause (6)).

```lean
theorem picardScheme_clauses_four_five_six (d : ℕ) :
    haveI := geometricallyIrreducible_of_isSepClosed B hX hk f
    haveI := isProjectiveVariety_of_isProjective B hX hk f hproj
    haveI := isRepresentable_picardFunctor_of_isSepClosed B hX hk f
    (∃ H : BigFppfOver B (Spec (.of k)) hk,
      Nonempty (Stacks.Hilbert.RepresentsHilbertFunctorOfRank (Over.mk (B.inclusion.map f))
        (Over.mk (B.inclusion.map H.hom)) d)) ∧
    ∀ (H : BigFppfOver B (Spec (.of k)) hk)
      (hH : Stacks.Hilbert.RepresentsHilbertFunctorOfRank (Over.mk (B.inclusion.map f))
        (Over.mk (B.inclusion.map H.hom)) d),
    ∃! γ : H ⟶ picardSchemeDegreeComponent B hX hk f (curveSection B hX hk f)
        (curveSection_comp B hX hk f) d,
      (∀ {T : BigFppfOver B (Spec (.of k)) hk} (t : T ⟶ H),
        picardHomEquiv B hX hk f (t ≫ γ ≫ picardSchemeDegreeComponentι B hX hk f
            (curveSection B hX hk f) (curveSection_comp B hX hk f) d) =
          (toPicardFunctor B hX hk f).app (op T) (hH.family (testMap B hk t)).picardClass) ∧
      (genus (B.inclusion.map f) ≤ d → Surjective (B.inclusion.map γ.left)) ∧
      (2 * (genus (B.inclusion.map f) : ℤ) - 1 ≤ d →
        AlgebraicGeometry.Smooth (B.inclusion.map γ.left)) ∧
      (d = genus (B.inclusion.map f) → IsBirational (B.inclusion.map γ.left))
```

**`Stacks.AbelMap.picardScheme_clause_two_bijOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurvePoints.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/PicardSchemeCurvePoints.lean#L45). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0BA0, clause (2).** For a smooth projective curve `X` over a separably
> closed field `k`, the natural map from the `k`-points of `Pic^d_{X/k}` to `Pic(X)`, sending a
> point `q` to the invertible `𝒪_X`-module whose class in `Pic_{X/k}(Spec k)` is classified by `q`
> followed by the inclusion `Pic^d_{X/k} ⟶ Pic_{X/k}`, is a bijection onto the invertible modules of
> degree `d`.

```lean
theorem picardScheme_clause_two_bijOn (d : ℤ) :
    haveI := geometricallyIrreducible_of_isSepClosed B hX hk f
    haveI := isProjectiveVariety_of_isProjective B hX hk f hproj
    haveI := isRepresentable_picardFunctor_of_isSepClosed B hX hk f
    Set.BijOn
      (fun q : baseOver B hk ⟶ picardSchemeDegreeComponent B hX hk f (curveSection B hX hk f)
          (curveSection_comp B hX hk f) d =>
        picardPointsEquiv B hX hk f (curveSection B hX hk f) (curveSection_comp B hX hk f)
          (isIso_baseChangeProj_c_of_isCurve B hX hk f (curveSection B hX hk f)
            (curveSection_comp B hX hk f))
          (q ≫ picardSchemeDegreeComponentι B hX hk f (curveSection B hX hk f)
            (curveSection_comp B hX hk f) d))
      Set.univ
      {x : Stacks.Picard.ofScheme X |
        @invertibleCurveDegree k _ X (B.inclusion.map f) _
          (IsCurve.topologicalKrullDim_eq_one (k := k) (f := B.inclusion.map f)).le (rep x)
          (Stacks.Picard.picardRepresentative X.toRingedSpace x).property = d}
```

**`Stacks.RigidifiedPicard.exists_picardScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurveRegistered.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/Jacobian/PicardOfCurveRegistered.lean#L45).

> **[Stacks, Tag 0BA0].** Let `k` be a separably closed field and `X` a smooth projective curve
> of genus `g` over `k`. Choosing a rational point `σ`, the Picard functor is represented by a group
> scheme `P` (`Pic_{X/k} ≅ Pic_{X/k,σ}`, [Stacks, Tag 0B9Z]), and:
> 1. `P` is the disjoint union of the open and closed `P^d`, `g`-dimensional smooth proper varieties;
> 2. the `k`-points of `P^d` are the invertible `𝒪_X`-modules of degree `d`: the natural map
>    `pointClassOf`, sending a rational point to the class it classifies, is a bijection from the
>    rational points landing in `P^d` onto the classes of degree `d`;
> 3. `P^0` is an open and closed subgroup scheme;
> 4. for `d ≥ 0` there is the canonical Abel morphism `γ_d : Hilb^d_{X/k} ⟶ P^d`, classifying the
>    rigidified class of `𝒪(D_univ)`;
> 5. `γ_d` is surjective for `d ≥ g` and smooth for `d ≥ 2g - 1`;
> 6. `γ_g` is birational.

```lean
theorem exists_picardScheme (k : Type u) [Field k] [IsSepClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsCurve k f] [Smooth f] (hproj : IsProjectiveMorphism f) :
    haveI : IsProper f := isProper_of_isProjectiveMorphism f hproj
    haveI : GeometricallyIrreducible f := geometricallyIrreducible_of_isCurve_of_isSepClosed k f
    haveI : SmoothOfRelativeDimension 1 f := smoothOfRelativeDimension_one_of_isCurve k f
    ∃ (σ : Spec (.of k) ⟶ X) (hσ : σ ≫ f = 𝟙 _) (P : Grp (Over (Spec (.of k))))
      (e : yonedaGrp.obj P ≅ functor f σ hσ),
      -- (1)
      (∀ d d' : ℤ, d ≠ d' → Disjoint
        (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d : Set P.X.left)
        (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d')) ∧
      (⨆ d, degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d = ⊤) ∧
      (∀ d : ℤ,
        IsClopen (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d :
          Set P.X.left) ∧
        IsProperVariety k
          ((degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d).ι ≫
            P.X.hom) ∧
        SmoothOfRelativeDimension (genus f)
          ((degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d).ι ≫
            P.X.hom) ∧
        topologicalKrullDim
          (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d) =
            (genus f : WithBot ℕ∞)) ∧
      -- (2)
      (∀ d : ℤ, Set.BijOn (pointClassOf f σ hσ P e)
        {r | Set.range r.left ⊆
          (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d :
            Set P.X.left)}
        {c | invertibleCurveDegreeHom k f (IsCurve.topologicalKrullDim_eq_one (k := k) (f := f)).le
          c = d}) ∧
      -- (3)
      (∃ K : OpenSubgroupScheme P, ∃ i : degreeLocusOver f
          (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e 0 ≅ K.carrier.X,
        degreeLocusι f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e 0 =
          i.hom ≫ K.ι.hom.hom) ∧
      ∀ (H : ℕ → Over (Spec (.of k)))
        (hH : ∀ d, Stacks.Hilbert.RepresentsHilbertFunctorOfRank (Over.mk f) (H d) d),
        -- (4)
        (∀ d : ℕ,
          abelMorphismDegree f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e
              (hH d) ≫
            (degreeLocus f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e d).ι =
              (abelMorphismFull f σ hσ (hH d) P e).left ∧
          ∀ {T : Over (Spec (.of k))} (m : T ⟶ H d),
            (e.hom.app (op T)).hom (m ≫ abelMorphismFull f σ hσ (hH d) P e) =
              abelElementFull f σ hσ (hH d) m) ∧
        -- (5), surjectivity
        (∀ d : ℕ, genus f ≤ d → Surjective
          (abelMorphismDegree f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e
            (hH d))) ∧
        -- (5), smoothness
        (∀ d : ℕ, 2 * (genus f : ℤ) - 1 ≤ d → Smooth
          (abelMorphismDegree f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ P e
            (hH d))) ∧
        -- (6)
        IsBirational (abelMorphismDegree f (topologicalKrullDim_fiber_le_one_of_isCurve k f) σ hσ
          P e (hH (genus f)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.6, Tag 0B9R](https://stacks.math.columbia.edu/tag/0B9R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
