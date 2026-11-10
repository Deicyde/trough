---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_iso_normalizationSchemeOverField_coproduct_normal_irreducible, AlgebraicGeometry.isVariety_normalizationOverField, AlgebraicGeometry.isFinite_normalizationOverField, AlgebraicGeometry.isDominant_normalizationOverField, AlgebraicGeometry.Scheme.isBirational_normalization, AlgebraicGeometry.Scheme.exists_normalizationScheme_iso_reduction, AlgebraicGeometry.isProper_and_isProjective_normalizationOverField, AlgebraicGeometry.isFinite_fromNormalization_of_locallyOfFiniteType_over_field
statement: formalized
proof: formalized
---

# 33.27 Normalization

Section 33.27 of the Stacks Project, [Tag 0BXQ](https://stacks.math.columbia.edu/tag/0BXQ). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BXR, a lemma

[Tag 0BXR](https://stacks.math.columbia.edu/tag/0BXR) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_normalizationSchemeOverField_coproduct_normal_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L81). The attribute's comment: “finite\_normal\_components”.

> **Stacks Project, Tag 0BXR.** The normalization of a scheme locally of finite type over a
> field is a coproduct of normal irreducible schemes, each locally of finite type over the field
> via its induced structure morphism.

```lean
public theorem exists_iso_normalizationSchemeOverField_coproduct_normal_irreducible
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [LocallyOfFiniteType p] :
    ∃ (I : Type u) (Z : I → Scheme.{u})
      (_ : ∀ i, IrreducibleSpace (Z i)) (_ : ∀ i, IsNormal (Z i))
      (e : normalizationSchemeOverField k p ≅ ∐ Z),
      ∀ i, LocallyOfFiniteType (Sigma.ι Z i ≫ e.inv ≫ normalizationOverField k p ≫ p)
```

**`AlgebraicGeometry.isVariety_normalizationOverField`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L101). The attribute's comment: “normalization\_of\_variety”.

> **Stacks Project, Tag 0BXR.** The normalization of a variety is a variety over the same
> field.

```lean
public instance isVariety_normalizationOverField (k : Type u) [Field k] {X : Scheme.{u}}
    (p : X ⟶ Spec (.of k)) [IsVariety k p] :
    IsVariety k (normalizationOverField k p ≫ p)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isFinite_normalizationOverField`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L265), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L71) (StacksFrontier): “finite\_normal\_components”.
- [`AlgebraicGeometry.isDominant_normalizationOverField`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L275), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L72) (StacksFrontier): “finite\_normal\_components”.
- [`AlgebraicGeometry.Scheme.isBirational_normalization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBirational/Basic.lean#L158), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L73) (StacksFrontier): “birational\_reduced”.
- [`AlgebraicGeometry.Scheme.exists_normalizationScheme_iso_reduction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalProperty.lean#L716), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L74) (StacksFrontier): “normalization\_of\_reduction”.

## Tag 0GK4, a lemma

[Tag 0GK4](https://stacks.math.columbia.edu/tag/0GK4) in the Stacks Project.

**`AlgebraicGeometry.isProper_and_isProjective_normalizationOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationProperProjective.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationProperProjective.lean#L81).

> **Stacks Project, Tag 0GK4.** Let `k` be a field, let `X` be a proper scheme over `k` and let
> `ν : X^ν ⟶ X` be the normalization morphism. Then `X^ν` is proper over `k`, and if `X` is
> projective over `k` then `X^ν` is projective over `k`.
>
> Projectivity of `X` is an implication inside the conclusion: the properness assertion holds at
> the source's own hypotheses, with nothing assumed about projectivity. Over the affine base
> `Spec k` projectivity and H-projectivity agree ([Stacks, Tag 01WB]), so the implication may be
> read with either notion.

```lean
public theorem isProper_and_isProjective_normalizationOverField (k : Type u) [Field k]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsProper p] :
    IsProper (normalizationOverField k p ≫ p) ∧
      (IsProjective p → IsProjective (normalizationOverField k p ≫ p))
```

## Tag 0BXS, a lemma

[Tag 0BXS](https://stacks.math.columbia.edu/tag/0BXS) in the Stacks Project.

**`AlgebraicGeometry.isFinite_fromNormalization_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationOverField.lean#L145).

> **Stacks Project, Tag 0BXS.** The relative normalization of a scheme locally of finite type
> over a field in a reduced scheme locally of finite type over the same field is finite, as soon as
> the morphism between them is quasi-compact.

```lean
public theorem isFinite_fromNormalization_of_locallyOfFiniteType_over_field
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    (f : Y ⟶ X) (hf : f ≫ pX = pY)
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY]
    [QuasiCompact f] [IsReduced Y] :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian pY
    letI : QuasiSeparated f := QuasiSeparated.of_comp f (terminal.from X)
    IsFinite f.fromNormalization
```

## Tag 0BXT, a lemma

[Tag 0BXT](https://stacks.math.columbia.edu/tag/0BXT) in the Stacks Project.

**`AlgebraicGeometry.exists_isPurelyInseparable_isGeometricallyNormal_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/NormalizationPurelyInseparable.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/NormalizationPurelyInseparable.lean#L557).

> **Stacks Project, Tag 0BXT.** Let `k` be a field and `X` an algebraic `k`-scheme. There is a
> finite purely inseparable extension `k'/k` such that the normalization of `X_{k'}` is
> geometrically normal over `k'`.

```lean
public theorem exists_isPurelyInseparable_isGeometricallyNormal_normalization
    (k : Type u) [Field k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k))
    [LocallyOfFiniteType p] [QuasiCompact p] :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : IsPurelyInseparable k k'),
      IsGeometricallyNormal (normalizationOverField k' (pullback.fst (spectrumMap k k') p) ≫
        pullback.fst (spectrumMap k k') p)
```

## Tag 0C3N, a lemma

[Tag 0C3N](https://stacks.math.columbia.edu/tag/0C3N) in the Stacks Project.

**`AlgebraicGeometry.normalizationBaseChangeComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean#L202). The attribute's comment: “canonical morphism”.

> **Stacks Project, Tag 0C3N.** The canonical morphism from the normalization after extending
> the ground field to the base change of the original normalization.

```lean
noncomputable def normalizationBaseChangeComparison
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    let σ := Spec.map (CommRingCat.ofHom (algebraMap k K))
    let Y := (Over.pullback σ).obj X
    letI : LocallyOfFiniteType Y.hom := by
      dsimp [Y, σ]
      infer_instance
    let hX := finite_irreducibleComponents_of_locallyOfFiniteType k X.hom
    let hY := finite_irreducibleComponents_of_locallyOfFiniteType K Y.hom
    Y.left.normalizationScheme hY ⟶
      ((Over.pullback σ).obj
        (Over.mk (X.left.normalization hX ≫ X.hom))).left
```

**`AlgebraicGeometry.normalizationBaseChangeComparison_comp_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean#L227). The attribute's comment: “projection to the original normalization”.

> **Stacks Project, Tag 0C3N.** The projection of the comparison to the original normalization
> is the canonical map induced by functoriality of relative normalization.  The map on
> generic-point residue spectra is over the projection `X_K ⟶ X`.

```lean
theorem normalizationBaseChangeComparison_comp_fst
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    let σ := Spec.map (CommRingCat.ofHom (algebraMap k K))
    let Y := (Over.pullback σ).obj X
    letI : LocallyOfFiniteType Y.hom := by
      dsimp [Y, σ]
      infer_instance
    let hX := finite_irreducibleComponents_of_locallyOfFiniteType k X.hom
    let hY := finite_irreducibleComponents_of_locallyOfFiniteType K Y.hom
    let fX := Scheme.fromGenericPointResidueFields X.left
    let fY := Scheme.fromGenericPointResidueFields Y.left
    letI : QuasiCompact fX := Scheme.quasiCompactFromGenericPointResidueFields X.left hX
    letI : QuasiSeparated fX := Scheme.quasiSeparatedFromGenericPointResidueFields X.left
    letI : QuasiCompact fY := Scheme.quasiCompactFromGenericPointResidueFields Y.left hY
    letI : QuasiSeparated fY := Scheme.quasiSeparatedFromGenericPointResidueFields Y.left
    ∃ (gY : Scheme.genericPointResidueSpectrum Y.left ⟶
        Scheme.genericPointResidueSpectrum X.left)
      (sq : gY ≫ fX = fY ≫ pullback.fst X.hom σ),
      normalizationBaseChangeComparison X ≫
          pullback.fst (X.left.normalization hX ≫ X.hom) σ =
        Scheme.Hom.normalizationMap fX fY gY (pullback.fst X.hom σ) sq
```

**`AlgebraicGeometry.normalizationBaseChangeComparison_comp_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean#L258). The attribute's comment: “projection to the extended base field”.

> **Stacks Project, Tag 0C3N.** The projection of the comparison to `Spec K` is the structural
> morphism of the normalized base change.  Together with the preceding projection formula, this
> characterizes the map into the fibre product.

```lean
theorem normalizationBaseChangeComparison_comp_snd
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    let σ := Spec.map (CommRingCat.ofHom (algebraMap k K))
    let Y := (Over.pullback σ).obj X
    letI : LocallyOfFiniteType Y.hom := by
      dsimp [Y, σ]
      infer_instance
    let hX := finite_irreducibleComponents_of_locallyOfFiniteType k X.hom
    normalizationBaseChangeComparison X ≫
        pullback.snd (X.left.normalization hX ≫ X.hom) σ =
      Y.left.normalization (finite_irreducibleComponents_of_locallyOfFiniteType K Y.hom) ≫
        Y.hom
```

**`AlgebraicGeometry.normalizationBaseChangeComparison_comp_baseChangeNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Basic.lean#L277). The attribute's comment: “compatibility with normalization morphisms”.

> **Stacks Project, Tag 0C3N.** The canonical comparison commutes with the normalization
> morphisms to the base-changed scheme.

```lean
theorem normalizationBaseChangeComparison_comp_baseChangeNormalization
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    let σ := Spec.map (CommRingCat.ofHom (algebraMap k K))
    let Y := (Over.pullback σ).obj X
    letI : LocallyOfFiniteType Y.hom := by
      dsimp [Y, σ]
      infer_instance
    normalizationBaseChangeComparison X ≫ baseChangeNormalization X =
      Y.left.normalization (finite_irreducibleComponents_of_locallyOfFiniteType K Y.hom)
```

**`AlgebraicGeometry.normalizationBaseChangeComparison_isUniversalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalHomeomorphism.lean, line 930](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalHomeomorphism.lean#L930). The attribute's comment: “universal homeomorphism”.

> **Stacks Project, Tag 0C3N.** The normalization comparison for an arbitrary extension of
> fields is a universal homeomorphism.
>
> The comparison lands in the reduction of its target (its source is reduced), and the resulting
> morphism `d` is integral and birational onto a scheme whose normalization morphism is a universal
> homeomorphism — because that scheme is the reduction of a base change of the *normal* scheme
> `X.normalizationScheme`.

```lean
theorem normalizationBaseChangeComparison_isUniversalHomeomorphism
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    UniversalHomeomorphism (normalizationBaseChangeComparison (k := k) (K := K) X)
```

**`AlgebraicGeometry.normalizationBaseChangeComparison_isIso_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalHomeomorphism.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalHomeomorphism.lean#L992). The attribute's comment: “separable extension”.

> **Stacks Project, Tag 0C3N.** For a separable extension of fields, the normalization
> comparison is an isomorphism.
>
> The target of the comparison is normal, by Tag 0C3M, so the universal property of the
> normalization of `X_K` produces a two-sided inverse.

```lean
theorem normalizationBaseChangeComparison_isIso_of_isSeparableExtension
    [Algebra.IsSeparableExtension k K] (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    IsIso (normalizationBaseChangeComparison (k := k) (K := K) X)
```

## Tag 0C3P, a lemma

[Tag 0C3P](https://stacks.math.columbia.edu/tag/0C3P) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_of_normalization_residueField_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationSeparableResidue.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationSeparableResidue.lean#L577). The attribute's comment: “geometrically reduced at the original point”.

> A reduced one-dimensional point is geometrically reduced if all residue fields above it in
> the normalization are separable over the ground field.

```lean
public theorem isGeometricallyReducedAt_of_normalization_residueField_isSeparable
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X)
    (hred : _root_.IsReduced (X.presheaf.stalk x))
    (hdim : ringKrullDim (X.presheaf.stalk x) = 1)
    (hsep :
      let Xnorm := normalizationSchemeOverField k f
      let ν := normalizationOverField k f
      ∀ x' : Xnorm, ν x' = x →
        letI : Algebra k (Xnorm.residueField x') :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ (ν ≫ f).appTop ≫ Xnorm.Γevaluation x').hom.toAlgebra
        Algebra.IsSeparableExtension k (Xnorm.residueField x')) :
    IsGeometricallyReducedAt f x
```

**`AlgebraicGeometry.isGeometricallyRegularAt_normalization_of_residueField_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationSeparableResidue.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationSeparableResidue.lean#L595). The attribute's comment: “geometrically regular on the normalization”.

> Every point of the normalization above a one-dimensional point is geometrically regular
> when its residue field is separable over the ground field.

```lean
public theorem isGeometricallyRegularAt_normalization_of_residueField_isSeparable
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X)
    (hdim : ringKrullDim (X.presheaf.stalk x) = 1)
    (hsep :
      let Xnorm := normalizationSchemeOverField k f
      let ν := normalizationOverField k f
      ∀ x' : Xnorm, ν x' = x →
        letI : Algebra k (Xnorm.residueField x') :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ (ν ≫ f).appTop ≫ Xnorm.Γevaluation x').hom.toAlgebra
        Algebra.IsSeparableExtension k (Xnorm.residueField x')) :
    let Xnorm := normalizationSchemeOverField k f
    let ν := normalizationOverField k f
    ∀ x' : Xnorm, ν x' = x → IsGeometricallyRegularAt (ν ≫ f) x'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.27, Tag 0BXQ](https://stacks.math.columbia.edu/tag/0BXQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
