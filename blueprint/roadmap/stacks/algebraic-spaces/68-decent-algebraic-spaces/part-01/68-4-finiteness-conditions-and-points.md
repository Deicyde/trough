---
declaration: section
origin: cited
lean: AlgebraicGeometry.locallyQuasiFinite_of_etale, AlgebraicGeometry.flat_and_generalizingMap_of_etale, AlgebraicGeometry.finite_preimage_singleton_of_etale_of_quasiCompact, AlgebraicGeometry.discreteTopology_fiber, AlgebraicGeometry.unramified_of_etale, AlgebraicGeometry.etale_iff_iso_coproduct_spectra_finite_separable, AlgebraicGeometry.Space.exists_etaleCover_finite_fibre_iff_forall_affine_etale, AlgebraicGeometry.Space.finite_chartFibre_of_etaleCover
statement: formalized
proof: formalized
---

# 68.4 Finiteness conditions and points

Section 68.4 of the Stacks Project, [Tag 03JR](https://stacks.math.columbia.edu/tag/03JR). 7 tags here are carried by 44 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03II, a remark

[Tag 03II](https://stacks.math.columbia.edu/tag/03II) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean#L54). The attribute's comment: “etale\_locally\_quasi\_finite”.

> An étale morphism of schemes is locally quasi-finite.

```lean
theorem locallyQuasiFinite_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] :
    LocallyOfFiniteType f ∧ LocallyQuasiFinite f
```

**`AlgebraicGeometry.flat_and_generalizingMap_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean#L63). The attribute's comment: “etale\_flat\_generalizing”. References: EGA IV (2.3.4), “(i), special case”.

> An étale morphism of schemes is flat, and hence generalizations lift along it.

```lean
theorem flat_and_generalizingMap_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] :
    Flat f ∧ GeneralizingMap f.base
```

**`AlgebraicGeometry.finite_preimage_singleton_of_etale_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleQuasiFinite.lean#L71). The attribute's comment: “etale\_quasi\_compact\_finite\_fibres”.

> A quasi-compact étale morphism of schemes has finite fibres.
>
> It is locally quasi-finite, hence quasi-finite as it is quasi-compact.

```lean
theorem finite_preimage_singleton_of_etale_of_quasiCompact {X S : Scheme.{u}} (f : X ⟶ S)
    [Etale f] [QuasiCompact f] (s : S) : (f.base ⁻¹' {s}).Finite
```

**`AlgebraicGeometry.discreteTopology_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/Support/EtaleDiscreteFibres.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/Support/EtaleDiscreteFibres.lean#L40). The attribute's comment: “etale\_discrete\_fibres”.

> Every scheme-theoretic fibre of an étale morphism is a discrete space.

```lean
theorem discreteTopology_fiber {X S : Scheme.{u}} (f : X ⟶ S)
    [Etale f] (s : S) : DiscreteTopology (f.fiber s)
```

**`AlgebraicGeometry.unramified_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/EtaleUnramified.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/EtaleUnramified.lean#L31). The attribute's comment: “etale\_unramified”.

> An étale morphism of schemes is unramified.

```lean
theorem unramified_of_etale {X S : Scheme.{u}} (f : X ⟶ S) [Etale f] : Unramified f
```

**`AlgebraicGeometry.etale_iff_iso_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/OverField.lean#L75). The attribute's comment: “etale\_over\_field”. References: EGA IV (17.6.2), “base = Spec k”; SGA 4½ Arcata (2.1.2), “a)”.

> **Stacks Project, Tag 03PC (over a field).** A morphism to the spectrum of a field is
> étale if and only if its source is, over that spectrum, a coproduct of spectra of finite
> separable field extensions.

```lean
public theorem etale_iff_iso_coproduct_spectra_finite_separable
    (k : Type u) [Field k] {U : Scheme.{u}} (f : U ⟶ Spec (.of k)) :
    Etale f ↔
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra k (K i)) (_ : ∀ i, Module.Finite k (K i))
        (_ : ∀ i, Algebra.IsSeparable k (K i))
        (e : U ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (K i)))) = f
```

## Tag 03JS, a lemma

[Tag 03JS](https://stacks.math.columbia.edu/tag/03JS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etaleCover_finite_fibre_iff_forall_affine_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitenessConditions.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitenessConditions.lean#L449).

> For a point `x` of an algebraic space `X` over `S`, the following are equivalent: some
> jointly locally surjective family of étale charts of `X` has finite fibres above `x`, and every
> étale chart of `X` by an affine scheme has a finite fibre above `x`.

```lean
theorem exists_etaleCover_finite_fibre_iff_forall_affine_etale (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (x : points B S hS X) :
    (∃ (I : Type u) (U : I → BigFppfOver B S hS) (φ : ∀ i, yoneda.obj (U i) ⟶ X),
      Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) (Sigma.desc φ) ∧
      ∀ i, (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) (φ i) ∧
        (pointsMap B S hS (yoneda.obj (U i)) (φ i) ⁻¹' {x}).Finite) ↔
    (∀ U : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
      ∀ φ : yoneda.obj U ⟶ X, (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) φ →
        (pointsMap B S hS (yoneda.obj U) φ ⁻¹' {x}).Finite)
```

**`AlgebraicGeometry.Space.finite_chartFibre_of_etaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsChartFibres.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsChartFibres.lean#L309). The attribute's comment: “part (1) implies part (2)”.

> **Stacks 03JS, part (1) implies part (2).** If some family of étale charts of an algebraic
> space `F` over `S` whose coproduct is surjective has finite chart fibres above a point `x` of
> `|F|`, then every étale chart of `F` with affine source has a finite chart fibre above `x`.
>
> The family is used only through joint surjectivity on points, which is what surjectivity of the
> coproduct gives by `AlgebraicGeometry.Space.exists_pointsMap_eq_of_isSurjective_sigmaDesc`, and
> affineness of the chart is used only through quasi-compactness of its underlying scheme; the
> general statement is `AlgebraicGeometry.Space.finite_chartFibre_of_jointlySurjective`.

```lean
theorem finite_chartFibre_of_etaleCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) {x : points B S hS F}
    {I : Type u} {V : I → BigFppfOver B S hS} (ψ : ∀ i, yoneda.obj (V i) ⟶ F)
    (hψ : ∀ i, IsEtale B S hS (ψ i)) (hsurj : IsSurjective B S hS (Sigma.desc ψ))
    (hfin : ∀ i, (chartFibre B S hS F (ψ i) x).Finite)
    (U : BigFppfOver B S hS) (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (φ : yoneda.obj U ⟶ F) (hφ : IsEtale B S hS φ) :
    (chartFibre B S hS F φ x).Finite
```

**`AlgebraicGeometry.Space.exists_etaleCover_finite_chartFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsChartFibres.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsChartFibres.lean#L329). The attribute's comment: “part (2) implies part (1)”.

> **Stacks 03JS, part (2) implies part (1).** An algebraic space over `S` has an étale
> covering family by affine schemes, so if every étale chart with affine source has a finite chart
> fibre above a point `x` of `|F|`, then the members of one covering family do.
>
> The covering family is the one of Stacks 03FX
> (`AlgebraicGeometry.IsAlgebraicSpace.exists_affine_coproduct_atlas`), exactly as in
> `AlgebraicGeometry.Space.HasFiniteFibresOnEveryAffineEtaleChart.hasFiniteFibresOnSomeEtaleCover`,
> whose surjectivity argument this repeats.

```lean
theorem exists_etaleCover_finite_chartFibre
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : ∀ U : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
      ∀ φ : yoneda.obj U ⟶ F, IsEtale B S hS φ → (chartFibre B S hS F φ x).Finite) :
    ∃ (I : Type u) (V : I → BigFppfOver B S hS) (ψ : ∀ i, yoneda.obj (V i) ⟶ F),
      (∀ i, IsEtale B S hS (ψ i)) ∧ IsSurjective B S hS (Sigma.desc ψ) ∧
      ∀ i, (chartFibre B S hS F (ψ i) x).Finite
```

## Tag 03JU, a lemma

[Tag 03JU](https://stacks.math.columbia.edu/tag/03JU) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleQuasiCompactFieldRepresentative_iff_hasMonomorphicFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonomorphicFieldRepresentative.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MonomorphicFieldRepresentative.lean#L239). The attribute's comment: “conditions (3) and (4)”.

> For a point of an algebraic space over `S`, having a field-valued representative with étale
> quasi-compact self-intersection projections is equivalent to having a monomorphic field-valued
> representative.

```lean
theorem hasEtaleQuasiCompactFieldRepresentative_iff_hasMonomorphicFieldRepresentative
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) :
    HasEtaleQuasiCompactFieldRepresentative B S hS F x ↔
      HasMonomorphicFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.hasFiniteRelationFiberAt_iff_everyEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibers.lean, line 964](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibers.lean#L964). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 03JU, conditions (1) and (2).** For a point of an algebraic space over `S`,
> finiteness of one relation fibre in one étale chart is equivalent to finiteness of every
> relation fibre in every étale chart.

```lean
theorem hasFiniteRelationFiberAt_iff_everyEtaleChart (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) :
    HasFiniteRelationFiberAt B S hS F x ↔
      HasFiniteRelationFiberAtEveryEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.hasFiniteRelationFiberAtEveryEtaleChart_iff_hasEtaleQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibers.lean, line 977](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibers.lean#L977). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 03JU, conditions (2) and (3).** For a point of an algebraic space over `S`,
> finiteness of every relation fibre in every étale chart is equivalent to having a field-valued
> representative with étale quasi-compact self-intersection projections.

```lean
theorem hasFiniteRelationFiberAtEveryEtaleChart_iff_hasEtaleQuasiCompactFieldRepresentative
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    HasFiniteRelationFiberAtEveryEtaleChart B S hS F x ↔
      HasEtaleQuasiCompactFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.HasMonomorphicFieldRepresentative.hasFiniteRelationFiberAtEveryEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreEquivalence.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreEquivalence.lean#L76). The attribute's comment: “part (4) implies part (2)”.

> **Stacks 03JU, condition (4) implies condition (2).** If a point `x` of an algebraic space
> `F` over `S` has a field-valued representative presenting it by a monomorphism out of the
> spectrum of a field, then for every étale chart `φ : h_U ⟶ F` and every pair of points of `|U|`
> above `x` the fibre of `|h_U ×_F h_U| → |U| × |U|` over that pair is finite.

```lean
theorem HasMonomorphicFieldRepresentative.hasFiniteRelationFiberAtEveryEtaleChart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} (h : HasMonomorphicFieldRepresentative B S hS F x) :
    HasFiniteRelationFiberAtEveryEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.HasFiniteRelationFiberAtEveryEtaleChart.hasEtaleQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreFieldRepresentative.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreFieldRepresentative.lean#L194). The attribute's comment: “part (2) implies part (3)”.

> **Stacks 03JU, part (2) implies part (3).** If every pair of points above a point `x` of an
> algebraic space `F` over `S`, in every étale chart of `F`, has finite relation fibre, then `x`
> has a field-valued representative whose two self-intersection projections are étale and
> quasi-compact.
>
> Take a surjective étale chart `φ : h_U ⟶ F` and a point `a` of `|U|` above `x`, let `u` be the
> point of the scheme `U` underlying `a`, and let `ν : P ⟶ U` be the canonical morphism from the
> spectrum `P` of the residue field at `u`. It is a monomorphism, by Stacks 01L6, and the
> composite `f : h_P ⟶ F` presents `x`. Writing the self-fibre-product of `f` as
> `N = P ×_U (U ×_F U) ×_U P`, its first projection factors as the base change of `ν` followed by
> the base change of the chart, that is as a monomorphism followed by an étale morphism to `P`;
> and `N` maps monomorphically to `U ×_F U` with both legs above `a`, so condition (2) makes
> `|N|` finite. The first projection is therefore étale by Tags 02GL and 03DP and quasi-compact
> by finiteness, and the second is the first conjugated by the symmetry of the
> fibre product.

```lean
theorem HasFiniteRelationFiberAtEveryEtaleChart.hasEtaleQuasiCompactFieldRepresentative
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasFiniteRelationFiberAtEveryEtaleChart B S hS F x) :
    HasEtaleQuasiCompactFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.HasEtaleQuasiCompactFieldRepresentative.hasMonomorphicFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreMonomorphism.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreMonomorphism.lean#L422). The attribute's comment: “part (3) implies part (4)”.

> **Stacks 03JU, part (3) implies part (4).** If a point `x` of an algebraic space `F` over `S`
> has a field-valued representative whose two self-intersection projections are étale and
> quasi-compact, then `x` has a field-valued representative presenting it by a monomorphism.
>
> Let `f : h_U ⟶ F` be the morphism presented by the representative of condition (3), so that `U`
> is `Spec k` for a field `k`, and let `R` be the kernel pair of `f`, which exists because the
> diagonal of `F` is representable. The two projections `R ⟶ U` are étale and quasi-compact, hence
> finite locally free with `R` affine, so `(U, R)` is a finite locally free equivalence relation on
> an affine scheme; Stacks 03BM represents its fppf quotient sheaf by the spectrum of the invariant
> ring, which is a field, and which lies in the site because the quotient does not increase size.
> The descent of `f` to that quotient sheaf is a monomorphism because `R` is the kernel pair of `f`
> and `F` is a sheaf, and the resulting field-valued point is dominated by the original one, so it
> represents the same point of `|F|`.

```lean
theorem HasEtaleQuasiCompactFieldRepresentative.hasMonomorphicFieldRepresentative
    (hF : IsAlgebraicSpace B S hS F) {x : points B S hS F}
    (h : HasEtaleQuasiCompactFieldRepresentative B S hS F x) :
    HasMonomorphicFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.HasMonomorphicFieldRepresentative.hasEtaleQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreMonomorphism.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreMonomorphism.lean#L468). The attribute's comment: “part (4) implies part (3)”.

> **Stacks 03JU, part (4) implies part (3).** A field-valued representative presenting a point
> by a monomorphism has invertible self-intersection projections, and an isomorphism is étale and
> quasi-compact after every representable base change.

```lean
theorem HasMonomorphicFieldRepresentative.hasEtaleQuasiCompactFieldRepresentative
    {x : points B S hS F} (h : HasMonomorphicFieldRepresentative B S hS F x) :
    HasEtaleQuasiCompactFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.HasFiniteRelationFiberAt.hasFiniteRelationFiberAtEveryEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreTransfer.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreTransfer.lean#L346). The attribute's comment: “part (1) implies part (2)”.

> **Stacks 03JU, part (1) implies part (2).** If some étale chart of an algebraic space `F`
> over `S` has two points above `x` with finite relation fibre, then every pair of points above
> `x` in every étale chart of `F` has finite relation fibre.
>
> Let `φ : h_U ⟶ F` be the chart of part (1), with points `a`, `b` above `x`, and let
> `ψ : h_W ⟶ F` be any étale chart with points `c`, `d` above `x`. The fibre product
> `T = h_W ×_F h_U` is representable with both projections étale, and Tag 03H4 lifts `(a, c)` and
> `(b, d)` to points of `|T|`. The relation fibre of `h_T ⟶ F` above that pair of lifts is finite
> because the relation fibre of `φ` above `(a, b)` is, and the relation fibre of `ψ` above `(c, d)`
> is finite because that one is.
>
> The hypothesis `_hF` that `F` is an algebraic space is retained from the source statement but is
> not used.

```lean
theorem HasFiniteRelationFiberAt.hasFiniteRelationFiberAtEveryEtaleChart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} (h : HasFiniteRelationFiberAt B S hS F x) :
    HasFiniteRelationFiberAtEveryEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.HasFiniteRelationFiberAtEveryEtaleChart.hasFiniteRelationFiberAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreTransfer.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelationFibreTransfer.lean#L379). The attribute's comment: “part (2) implies part (1)”.

> **Stacks 03JU, part (2) implies part (1).** An algebraic space over `S` has a surjective
> étale chart, which carries a point above `x`, so the universally quantified condition (2) is
> witnessed and condition (1) holds.
>
> This is `AlgebraicGeometry.Space.hasFiniteRelationFiberAt_of_everyEtaleChart` with its
> hypothesis that some étale chart has a point above `x` discharged by an atlas of Tag 03FQ, which
> is surjective on the points of Tag 03BU by Tag 03H5. Together with
> `AlgebraicGeometry.Space.HasFiniteRelationFiberAt.hasFiniteRelationFiberAtEveryEtaleChart` it
> makes conditions (1) and (2) of Stacks 03JU equivalent.

```lean
theorem HasFiniteRelationFiberAtEveryEtaleChart.hasFiniteRelationFiberAt
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} (h : HasFiniteRelationFiberAtEveryEtaleChart B S hS F x) :
    HasFiniteRelationFiberAt B S hS F x
```

## Tag 040U, a lemma

[Tag 040U](https://stacks.math.columbia.edu/tag/040U) in the Stacks Project.

**`AlgebraicGeometry.Space.finiteFibres_of_mono_isFinite_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFibresOneChart.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFibresOneChart.lean#L245). The attribute's comment: “part (2) implies part (1)”.

> Let `F` be an algebraic space over a scheme `S`, let `x` be a point of `|F|` and let
> `φ : h_U ⟶ F` be étale. Suppose some field-valued point of `F` in the class of `x` presents it by
> a monomorphism `Spec(k) ⟶ F` for which `Spec(k) ×_F U` is nonempty and finite over `Spec(k)`.
> Then `x` lies in the image of `|U| → |F|` and the fibres of `|U| → |F|` and of `|R| → |F|` above
> `x`, where `R = h_U ×_F h_U`, are both finite.

```lean
theorem finiteFibres_of_mono_isFinite_fieldFibre (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) {x : points B S hS F} {U : BigFppfOver B S hS}
    {φ : yoneda.obj U ⟶ F} (hφ : IsEtale B S hS φ)
    (h : ∃ p : FieldValuedPoint B S hS F, p.class B S hS F = x ∧
      Mono (fieldMorphism B S hS F p) ∧
      IsFinite B S hS (pullback.fst (fieldMorphism B S hS F p) φ) ∧
      Nonempty (points B S hS (pullback (fieldMorphism B S hS F p) φ))) :
    (∃ a : points B S hS (yoneda.obj U), pointsMap B S hS (yoneda.obj U) φ a = x) ∧
      (chartFibre B S hS F φ x).Finite ∧ (relationFibre B S hS F φ x).Finite
```

**`AlgebraicGeometry.Space.exists_mono_isFinite_fieldFibre_of_finiteFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFibresOneChart.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFibresOneChart.lean#L268). The attribute's comment: “part (1) implies part (2)”.

> A point `x` of `|F|` lying in the image of `|U| → |F|` whose chart and relation fibres above
> it are finite is presented by a monomorphism `Spec(k) ⟶ F` for which `Spec(k) ×_F U` is nonempty
> and finite over `Spec(k)`, finiteness being the presheaf-relative form.

```lean
theorem exists_mono_isFinite_fieldFibre_of_finiteFibres
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} {U : BigFppfOver B S hS} {φ : yoneda.obj U ⟶ F}
    (hφ : IsEtale B S hS φ)
    (h : (∃ a : points B S hS (yoneda.obj U), pointsMap B S hS (yoneda.obj U) φ a = x) ∧
      (chartFibre B S hS F φ x).Finite ∧ (relationFibre B S hS F φ x).Finite) :
    ∃ p : FieldValuedPoint B S hS F, p.class B S hS F = x ∧
      Mono (fieldMorphism B S hS F p) ∧
      (MorphismProperty.inverseImage
        (@_root_.AlgebraicGeometry.IsFinite.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf
        (pullback.fst (fieldMorphism B S hS F p) φ) ∧
      Nonempty (points B S hS (pullback (fieldMorphism B S hS F p) φ))
```

## Tag 03JV, a lemma

[Tag 03JV](https://stacks.math.columbia.edu/tag/03JV) in the Stacks Project.

**`AlgebraicGeometry.Space.hasQuasiCompactMonomorphicFieldRepresentative_of_hasQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldBaseChange.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldBaseChange.lean#L179). The attribute's comment: “condition (5) implies condition (4)”.

> **Stacks 03JV, condition (5) implies condition (4).** If some field-valued point in the
> class of `x` presents it by a quasi-compact morphism, then some field-valued point in that
> class presents it by a morphism which is both a monomorphism and quasi-compact.

```lean
theorem hasQuasiCompactMonomorphicFieldRepresentative_of_hasQuasiCompactFieldRepresentative
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasQuasiCompactFieldRepresentative B S hS F x) :
    HasQuasiCompactMonomorphicFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAt_iff_hasQuasiCompactMonomorphicFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/QuasiCompactMonomorphicPoint.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/QuasiCompactMonomorphicPoint.lean#L209). The attribute's comment: “conditions (1) and (4)”.

> For a point of an algebraic space over `S`, finiteness of the fibres of every affine étale
> chart and of its self-intersection above the point is equivalent to the point being in the class
> of a quasi-compact monomorphism from the spectrum of a field.

```lean
theorem hasFiniteChartAndRelationFibersAt_iff_hasQuasiCompactMonomorphicFieldRepresentative
    (hX : IsAlgebraicSpace B S hS X) (x : points B S hS X) :
    HasFiniteChartAndRelationFibersAt B S hS X x ↔
      HasQuasiCompactMonomorphicFieldRepresentative B S hS X x
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactMonomorphicFieldRepresentative.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactMonomorphicFieldRepresentative.lean#L62). The attribute's comment: “part (4)”.

> **Stacks 03JV, condition (4).** A point of `F` has a *quasi-compact monomorphic
> field-valued representative* when some field-valued point in its class presents it by a
> morphism which is both a monomorphism and quasi-compact.

```lean
def HasQuasiCompactMonomorphicFieldRepresentative (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasFiniteFibresOnEveryAffineEtaleChart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L116). The attribute's comment: “part (1)”.

> **Stacks 03JV, condition (1).** For every affine scheme `U` and every étale morphism
> `φ : h_U ⟶ F`, setting `R = h_U ×_F h_U`, the fibres of `|U| → |F|` and of `|R| → |F|`
> above `x` are both finite.

```lean
def HasFiniteFibresOnEveryAffineEtaleChart (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasFiniteFibresOnSomeEtaleCover`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L125). The attribute's comment: “part (2)”.

> **Stacks 03JV, condition (2).** There is a family of étale morphisms `φ i : h_{U i} ⟶ F`
> whose coproduct is surjective on points and for which, setting `R i = h_{U i} ×_F h_{U i}`,
> the fibres of `|U i| → |F|` and of `|R i| → |F|` above `x` are all finite.

```lean
def HasFiniteFibresOnSomeEtaleCover (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasMonomorphicFieldRepresentativeWithFiniteCharts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L137). The attribute's comment: “part (3)”.

> **Stacks 03JV, condition (3).** Some field-valued representative of `x` presents it by a
> monomorphism `Spec(k) ⟶ F` whose base change along every étale chart of `F` with affine
> source is a finite scheme over `k`.

```lean
def HasMonomorphicFieldRepresentativeWithFiniteCharts (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasQuasiCompactFieldRepresentative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L150). The attribute's comment: “part (5)”.

> **Stacks 03JV, condition (5).** Some field-valued point in the class of `x` presents it
> by a quasi-compact morphism, the monomorphism condition of condition (4) being dropped.

```lean
def HasQuasiCompactFieldRepresentative (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.EveryFieldRepresentativeIsQuasiCompact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L157). The attribute's comment: “part (6)”.

> **Stacks 03JV, condition (6).** *Every* field-valued point in the class of `x` presents
> it by a quasi-compact morphism.

```lean
def EveryFieldRepresentativeIsQuasiCompact (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative.hasQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L166). The attribute's comment: “part (4) implies part (5)”.

> **Stacks 03JV, condition (4) implies condition (5).** Forgetting that the presenting
> morphism is a monomorphism leaves a quasi-compact field-valued representative.

```lean
theorem HasQuasiCompactMonomorphicFieldRepresentative.hasQuasiCompactFieldRepresentative
    {x : points B S hS F}
    (h : HasQuasiCompactMonomorphicFieldRepresentative B S hS F x) :
    HasQuasiCompactFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.EveryFieldRepresentativeIsQuasiCompact.hasQuasiCompactFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsConditions.lean#L177). The attribute's comment: “part (6) implies part (5)”.

> **Stacks 03JV, condition (6) implies condition (5).** A point of `|F|` is by construction
> the class of some field-valued point, so a universally quasi-compact class has a
> quasi-compact representative.

```lean
theorem EveryFieldRepresentativeIsQuasiCompact.hasQuasiCompactFieldRepresentative
    {x : points B S hS F}
    (h : EveryFieldRepresentativeIsQuasiCompact B S hS F x) :
    HasQuasiCompactFieldRepresentative B S hS F x
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative.everyFieldRepresentativeIsQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsEveryRepresentative.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsEveryRepresentative.lean#L39). The attribute's comment: “part (4) implies part (6)”.

> If a point `x` of an algebraic space `F` over `S` is the class of a field-valued point whose
> presenting morphism `Spec(k) ⟶ F` is a quasi-compact monomorphism, then the presenting morphism
> of *every* field-valued point in the class of `x` is quasi-compact.

```lean
theorem HasQuasiCompactMonomorphicFieldRepresentative.everyFieldRepresentativeIsQuasiCompact
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasQuasiCompactMonomorphicFieldRepresentative B S hS F x) :
    EveryFieldRepresentativeIsQuasiCompact B S hS F x
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative.hasMonomorphicFieldRepresentativeWithFiniteCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteCharts.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteCharts.lean#L141). The attribute's comment: “part (4) implies part (3)”.

> **Stacks 03JV, condition (4) implies condition (3).** If a point `x` of a presheaf `F` on
> the big fppf site of `S` is the class of a field-valued point whose presenting morphism
> `Spec(k) ⟶ F` is a quasi-compact monomorphism, then that same monomorphism presents `x` and
> has finite base change to every affine étale chart of `F`.
>
> The representative, the equality of classes and the monomorphism are carried over unchanged;
> the only content is the finiteness of the base change, which is
> `AlgebraicGeometry.Space.isFinite_pullback_fst_fieldMorphism_of_isQuasiCompact` applied to the
> affine — hence quasi-compact — chart.

```lean
theorem hasMonomorphicFieldRepresentativeWithFiniteCharts
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) {x : points B S hS F}
    (h : HasQuasiCompactMonomorphicFieldRepresentative B S hS F x) :
    HasMonomorphicFieldRepresentativeWithFiniteCharts B S hS F x
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative.hasFiniteFibresOnEveryAffineEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean#L169). The attribute's comment: “part (4) implies part (1)”.

> **Stacks 03JV, condition (4) implies condition (1).** If a point `x` of an algebraic space
> `F` over `S` is the class of a field-valued point whose presenting morphism `Spec(k) ⟶ F` is a
> quasi-compact monomorphism, then for every affine scheme `U` and every étale `φ : h_U ⟶ F` the
> fibres of `|U| → |F|` and of `|R| → |F|` above `x`, where `R = h_U ×_F h_U`, are both finite.

```lean
theorem HasQuasiCompactMonomorphicFieldRepresentative.hasFiniteFibresOnEveryAffineEtaleChart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasQuasiCompactMonomorphicFieldRepresentative B S hS F x) :
    HasFiniteFibresOnEveryAffineEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.HasFiniteFibresOnEveryAffineEtaleChart.hasFiniteFibresOnSomeEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean#L237). The attribute's comment: “part (1) implies part (2)”.

> **Stacks 03JV, condition (1) implies condition (2).** An algebraic space over `S` has an
> étale covering family by affine schemes, so the finiteness condition of condition (1), which
> quantifies over *every* affine étale chart, is in particular satisfied by the members of one
> covering family.

```lean
theorem HasFiniteFibresOnEveryAffineEtaleChart.hasFiniteFibresOnSomeEtaleCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasFiniteFibresOnEveryAffineEtaleChart B S hS F x) :
    HasFiniteFibresOnSomeEtaleCover B S hS F x
```

**`AlgebraicGeometry.Space.HasQuasiCompactMonomorphicFieldRepresentative.hasFiniteFibresOnSomeEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFiniteFibres.lean#L272). The attribute's comment: “part (4) implies part (2)”.

> **Stacks 03JV, condition (4) implies condition (2).** The composite of the two implications
> above: condition (4) gives condition (1), which gives condition (2).

```lean
theorem HasQuasiCompactMonomorphicFieldRepresentative.hasFiniteFibresOnSomeEtaleCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasQuasiCompactMonomorphicFieldRepresentative B S hS F x) :
    HasFiniteFibresOnSomeEtaleCover B S hS F x
```

**`AlgebraicGeometry.Space.HasFiniteFibresOnSomeEtaleCover.hasFiniteFibresOnEveryAffineEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromEtaleCover.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromEtaleCover.lean#L97). The attribute's comment: “part (2) implies part (1)”.

> **Stacks 03JV, condition (2) implies condition (1).** If some family of étale charts of an
> algebraic space `F` over `S` with surjective coproduct has finite chart and relation fibres above
> a point `x` of `|F|`, then every étale chart of `F` with affine source has finite chart and
> relation fibres above `x`.
>
> The chart half is Stacks 03JS. For the relation half, condition (2) supplies condition (1) of
> Stacks 03JU at `x`, so Stacks 03JU, part (1) implies part (2), bounds the relation fibre above
> each pair of points of the — now finite — chart fibre, and the fibre of `|R| → |F|` above `x` is
> the union of those.

```lean
theorem HasFiniteFibresOnSomeEtaleCover.hasFiniteFibresOnEveryAffineEtaleChart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} (h : HasFiniteFibresOnSomeEtaleCover B S hS F x) :
    HasFiniteFibresOnEveryAffineEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.hasFiniteFibresOnEveryAffineEtaleChart_iff_onSomeEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromEtaleCover.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromEtaleCover.lean#L152). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 03JV, conditions (1) and (2) are equivalent.** For a point `x` of an algebraic
> space `F` over `S`, finiteness of the chart and relation fibres above `x` on *every* étale
> chart with affine source holds if and only if it holds on the members of *some* étale
> covering family.
>
> This is the first equivalence of Stacks 03JV to be closed. The forward direction is
> `AlgebraicGeometry.Space.HasFiniteFibresOnEveryAffineEtaleChart.hasFiniteFibresOnSomeEtaleCover`,
> which reads the covering family off the affine atlas of Stacks 03FX; the reverse direction is
> `AlgebraicGeometry.Space.HasFiniteFibresOnSomeEtaleCover.hasFiniteFibresOnEveryAffineEtaleChart`
> above, which is the source's own argument through Stacks 03JS and 03JU. Algebraicity of `F` is
> used in both directions and is not removable: the atlas of Stacks 03FX and the transfer of
> Stacks 03JU each require it.

```lean
theorem hasFiniteFibresOnEveryAffineEtaleChart_iff_onSomeEtaleCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} :
    HasFiniteFibresOnEveryAffineEtaleChart B S hS F x ↔
      HasFiniteFibresOnSomeEtaleCover B S hS F x
```

**`AlgebraicGeometry.Space.HasMonomorphicFieldRepresentativeWithFiniteCharts.hasFiniteFibresOnEveryAffineEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromFiniteCharts.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromFiniteCharts.lean#L102). The attribute's comment: “part (3) implies part (1)”.

> **Stacks 03JV, condition (3) implies condition (1).** If a point `x` of an algebraic space
> `F` over `S` is presented by a monomorphism `Spec(k) ⟶ F` whose base change along every étale
> chart with affine source is finite over `Spec(k)`, then for every affine scheme `U` and every
> étale `φ : h_U ⟶ F` the fibres of `|U| → |F|` and of `|R| → |F|` above `x`, where
> `R = h_U ×_F h_U`, are both finite.
>
> This is the source's "apply Lemma 040U to every étale morphism `U → X` with `U` affine", in the
> nonemptiness-free form
> `AlgebraicGeometry.Space.finite_chartFibre_and_relationFibre_of_mono_isFinite`: finiteness of
> the field fibre over `Spec(k)` makes its point set finite and Stacks 03H4 maps that set onto
> the chart fibre, after which the relation fibre is bounded by Stacks 0AC7 above each pair of
> points of the chart fibre, the monomorphism being what 0AC7 needs.

```lean
theorem HasMonomorphicFieldRepresentativeWithFiniteCharts.hasFiniteFibresOnEveryAffineEtaleChart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasMonomorphicFieldRepresentativeWithFiniteCharts B S hS F x) :
    HasFiniteFibresOnEveryAffineEtaleChart B S hS F x
```

**`AlgebraicGeometry.Space.HasMonomorphicFieldRepresentativeWithFiniteCharts.hasFiniteFibresOnSomeEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromFiniteCharts.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromFiniteCharts.lean#L121). The attribute's comment: “part (3) implies part (2)”.

> **Stacks 03JV, condition (3) implies condition (2).** The composite of the implication
> above with
> `AlgebraicGeometry.Space.HasFiniteFibresOnEveryAffineEtaleChart.hasFiniteFibresOnSomeEtaleCover`:
> a monomorphic representative with finite charts gives finiteness of the chart and relation
> fibres on every affine étale chart, hence on the members of the affine étale covering family of
> Stacks 03FX.

```lean
theorem HasMonomorphicFieldRepresentativeWithFiniteCharts.hasFiniteFibresOnSomeEtaleCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasMonomorphicFieldRepresentativeWithFiniteCharts B S hS F x) :
    HasFiniteFibresOnSomeEtaleCover B S hS F x
```

**`AlgebraicGeometry.Space.HasQuasiCompactFieldRepresentative.everyFieldRepresentativeIsQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromQuasiCompactRepresentative.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromQuasiCompactRepresentative.lean#L121). The attribute's comment: “part (5) implies part (6)”.

> **Stacks 03JV, condition (5) implies condition (6).** If some field-valued point in the
> class of a point `x` of an algebraic space `F` over `S` presents it by a quasi-compact
> morphism `Spec(k) ⟶ F`, then *every* field-valued point in the class of `x` does.

```lean
theorem HasQuasiCompactFieldRepresentative.everyFieldRepresentativeIsQuasiCompact
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F}
    (h : HasQuasiCompactFieldRepresentative B S hS F x) :
    EveryFieldRepresentativeIsQuasiCompact B S hS F x
```

**`AlgebraicGeometry.Space.hasQuasiCompactFieldRepresentative_iff_everyFieldRepresentativeIsQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromQuasiCompactRepresentative.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsFromQuasiCompactRepresentative.lean#L148). The attribute's comment: “conditions (5) and (6)”.

> **Stacks 03JV, conditions (5) and (6) are equivalent.** For a point `x` of an algebraic
> space `F` over `S`, *some* field-valued point in the class of `x` has quasi-compact presenting
> morphism if and only if *every* one does.

```lean
theorem hasQuasiCompactFieldRepresentative_iff_everyFieldRepresentativeIsQuasiCompact
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    {x : points B S hS F} :
    HasQuasiCompactFieldRepresentative B S hS F x ↔
      EveryFieldRepresentativeIsQuasiCompact B S hS F x
```

**`AlgebraicGeometry.Space.hasQuasiCompactMonomorphicFieldRepresentative_of_finiteCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsZariskiChart.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointsZariskiChart.lean#L128). The attribute's comment: “part (3) implies part (4)”.

> **Stacks 03JV, condition (3) implies condition (4).** Let `F` be an algebraic space over
> `S` and let `x` be a point of `F`. If some field-valued representative of `x` presents it by
> a monomorphism whose base change along every affine étale chart of `F` is finite, then that
> monomorphism is in addition quasi-compact.
>
> A surjective étale chart `h_V ⟶ F` by a single object of the site exists by Stacks 03FX, and
> `V` is covered by its affine open subschemes, each of which is an object of the site whose
> composite to `F` is an affine étale chart. The hypothesis applies to those charts, and the
> resulting fibre products are affine objects of the site whose projections to the members of
> the covering are morphisms of affine schemes, hence quasi-compact. The Zariski-local criterion
> `AlgebraicGeometry.Space.isQuasiCompact_pullback_snd_of_openCover` turns that into
> quasi-compactness of the base change of the representative along the chart, which is condition
> (4) of Stacks 03KG, and
> `AlgebraicGeometry.Space.isQuasiCompact_of_surjectiveEtale_atlas` is its condition (4) implies
> condition (1).
>
> Together with the converse this closes the adjacent equivalence of conditions (3) and
> (4) of Stacks 03JV.

```lean
theorem hasQuasiCompactMonomorphicFieldRepresentative_of_finiteCharts
    (hF : IsAlgebraicSpace B S hS F) {x : points B S hS F}
    (h : HasMonomorphicFieldRepresentativeWithFiniteCharts B S hS F x) :
    HasQuasiCompactMonomorphicFieldRepresentative B S hS F x
```

## Tag 03JT, a lemma

[Tag 03JT](https://stacks.math.columbia.edu/tag/03JT) in the Stacks Project.

**`AlgebraicGeometry.Space.isReasonableSpace_iff_exists_boundedEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableEtaleCover.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableEtaleCover.lean#L262).

> **Stacks 03JT.** For an algebraic space `X` over `S` the following are equivalent: `(1)`
> there is a jointly surjective family of étale charts of `X` by schemes, each with universally
> bounded fibres, and `(2)` every étale chart of `X` by an affine scheme has universally bounded
> fibres, which is `AlgebraicGeometry.Space.IsReasonableSpace`.

```lean
theorem isReasonableSpace_iff_exists_boundedEtaleCover
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    IsReasonableSpace B S hS X ↔
      ∃ (I : Type u) (U : I → BigFppfOver B S hS) (φ : ∀ i, yoneda.obj (U i) ⟶ X),
        Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) (Sigma.desc φ) ∧
        ∀ i, (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) (φ i) ∧
          HasUniversallyBoundedFibers B S hS (U i) (φ i)
```

## Tag 03IH, a lemma

[Tag 03IH](https://stacks.math.columbia.edu/tag/03IH) in the Stacks Project.

**`AlgebraicGeometry.Space.isVeryReasonableSpace_iff_exists_isZariskiCover_quasiCompact_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableAtlas.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableAtlas.lean#L118).

> **Stacks 03IH.** An algebraic space over `S` is very reasonable — it has a jointly
> surjective family of étale charts by schemes whose two self-intersection projections are
> quasi-compact — if and only if it has a Zariski covering by open subspaces each of which
> carries a quasi-compact surjective étale chart by a scheme.

```lean
theorem isVeryReasonableSpace_iff_exists_isZariskiCover_quasiCompact_chart
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    IsVeryReasonableSpace B S hS X ↔
      ∃ (I : Type u) (Xᵢ : I → Subfunctor X), IsZariskiCover B S hS I Xᵢ ∧
        ∃ (U : I → BigFppfOver B S hS) (φ : ∀ i, yoneda.obj (U i) ⟶ (Xᵢ i).toFunctor),
          ∀ i, IsEtale B S hS (φ i) ∧
            Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) (φ i) ∧
            IsQuasiCompact B S hS (φ i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.4, Tag 03JR](https://stacks.math.columbia.edu/tag/03JR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
