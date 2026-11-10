---
declaration: section
origin: cited
lean: AlgebraicGeometry.stalkOfBaseChange_isLocalization, AlgebraicGeometry.faithfullyFlat_stalkMap_fieldExtension, AlgebraicGeometry.Scheme.Pullback.isIso_residueFieldMap_to_residueField_specOfPoint, AlgebraicGeometry.specialFibreRingEquiv, AlgebraicGeometry.fiberLocalRing_dimension_add_localRing_dimension_eq, AlgebraicGeometry.fiberLocalRing_dimension_add_trdeg_eq, AlgebraicGeometry.map_maximalIdeal_stalkMap_eq_of_isReduced_tensorProduct
statement: formalized
proof: formalized
---

# 33.5 Change of fields and local rings

Section 33.5 of the Stacks Project, [Tag 0C4X](https://stacks.math.columbia.edu/tag/0C4X). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C4Y, a lemma

[Tag 0C4Y](https://stacks.math.columbia.edu/tag/0C4Y) in the Stacks Project.

**`AlgebraicGeometry.stalkOfBaseChange_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FieldExtensionStalk.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FieldExtensionStalk.lean#L364). The attribute's comment: “localization_description”.

> **Stacks Project, Tag 0C4Y (localization description).** The local ring at a point of a base
> change by a field extension is the localization of `𝒪_{X,x} ⊗_k K` at the prime obtained from
> the map to the residue field of that point.

```lean
public theorem stalkOfBaseChange_isLocalization
    {k K : Type u} [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y = x) :
    let Y := (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})
    let A := stalkBaseChangeRing (K := K) f x
    let B := residueBaseChangeRing (K := K) f x
    ∃ θ : A ⟶ B, ∃ ψ : B ⟶ Y.residueField y, ∃ φ : A ⟶ Y.presheaf.stalk y,
      pushout.inl (fieldToStalk f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ θ =
        X.residue x ≫ pushout.inl (fieldToResidue f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ∧
      pushout.inr (fieldToStalk f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ θ =
        pushout.inr (fieldToResidue f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ∧
      pushout.inl (fieldToResidue f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ ψ =
        (X.residueFieldCongr hy.symm).hom ≫
          (pullback.fst f (Spec.map
            (CommRingCat.ofHom (algebraMap k K)))).residueFieldMap y ∧
      pushout.inr (fieldToResidue f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ ψ =
        fieldToResidue
          (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K)))) y ∧
      pushout.inl (fieldToStalk f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ φ =
        (X.presheaf.stalkCongr (.of_eq hy.symm)).hom ≫
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).stalkMap y ∧
      pushout.inr (fieldToStalk f x)
          (CommRingCat.ofHom (algebraMap k K : k →+* K)) ≫ φ =
        fieldToStalk
          (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K)))) y ∧
      θ ≫ ψ = φ ≫ Y.residue y ∧
      letI : Algebra A (Y.presheaf.stalk y) := φ.hom.toAlgebra
      let p₀ := RingHom.ker ψ.hom
      let p := stalkBaseChangePrime f x θ p₀
      letI : p₀.IsPrime := RingHom.ker_isPrime _
      letI : p.IsPrime := Ideal.comap_isPrime _ _
      IsLocalization.AtPrime (Y.presheaf.stalk y) p
```

**`AlgebraicGeometry.faithfullyFlat_stalkMap_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/FaithfullyFlatStalk.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/FaithfullyFlatStalk.lean#L57). The attribute's comment: “faithfully_flat_local”.

> For an extension of fields `K / k`, the map on local rings from a point of a `k`-scheme
> to a point above it after base change to `K` is faithfully flat.

```lean
public theorem faithfullyFlat_stalkMap_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y = x) :
    ((eqToHom (congrArg X.presheaf.stalk hy.symm)) ≫
      (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap k K)))).stalkMap y).hom.FaithfullyFlat
```

**`AlgebraicGeometry.Scheme.Pullback.isIso_residueFieldMap_to_residueField_specOfPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ResidueField.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ResidueField.lean#L45). The attribute's comment: “residue_field”.

> **Stacks Project, Tag 0C4Y (residue field).** If `y` is a point of the base change of a
> scheme over `k` to a field extension `K/k`, its residue field is canonically isomorphic to the
> residue field at the corresponding prime of `κ(x) ⊗[k] K`.

```lean
public theorem isIso_residueFieldMap_to_residueField_specOfPoint
    {X Y S : Scheme.{u}} {f : X ⟶ S} {g : Y ⟶ S}
    (y : (pullback f g : Scheme)) :
    let T := Scheme.Pullback.Triplet.ofPoint y
    let p := Scheme.Pullback.SpecOfPoint y
    IsIso (((pullback f g : Scheme).residueFieldCongr
        (Scheme.Pullback.SpecTensorTo_SpecOfPoint y).symm).hom ≫
      T.SpecTensorTo.residueFieldMap p ≫
      (Scheme.Spec.residueFieldIso T.tensor p).hom)
```

**`AlgebraicGeometry.specialFibreRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/MaximalIdealFieldChange.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/MaximalIdealFieldChange.lean#L527). The attribute's comment: “special_fibre”.

> **Stacks Project, Tag 0C4Y (special fibre).**  For a point `y` of the base change of
> a scheme over `k` to an extension field `K`, the quotient of `𝒪_{Y,y}` by the extension
> of the maximal ideal of `𝒪_{X,x}` is the localization of `κ(x) ⊗_k K` at the prime
> induced by `y`.

```lean
noncomputable def specialFibreRingEquiv
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})) :
    let p := RingHom.ker (Scheme.Pullback.ofPointTensor y).hom
    letI : p.IsPrime := RingHom.ker_isPrime _
    ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk y ⧸
        Ideal.map
          ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).stalkMap y).hom
          (IsLocalRing.maximalIdeal
            (X.presheaf.stalk
              ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)))) ≃+*
      Localization.AtPrime p
```

## Tag 0C4Z, a lemma

[Tag 0C4Z](https://stacks.math.columbia.edu/tag/0C4Z) in the Stacks Project.

**`AlgebraicGeometry.fiberLocalRing_dimension_add_localRing_dimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/LocalRingDimension.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/LocalRingDimension.lean#L103). The attribute's comment: “local-ring dimension equality”.

> **Stacks Project, Tag 0C4Z.** After extension of the ground field, the dimension of the local
> fibre ring plus the dimension of the original local ring is the dimension of the new local
> ring.

```lean
theorem fiberLocalRing_dimension_add_localRing_dimension_eq
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})) :
    let Y := (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})
    let g : Y ⟶ X := pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let x := g.base y
    ringKrullDim
          ((Y.presheaf.stalk y) ⧸
            Ideal.map (g.stalkMap y).hom
              (IsLocalRing.maximalIdeal (X.presheaf.stalk x))) +
        ringKrullDim (X.presheaf.stalk x) =
      ringKrullDim (Y.presheaf.stalk y)
```

**`AlgebraicGeometry.fiberLocalRing_dimension_add_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/LocalRingDimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/LocalRingDimension.lean#L142). The attribute's comment: “transcendence degree equality”.

> **Stacks Project, Tag 0C4Z.** After extension of the ground field, the dimension of the local
> fibre ring plus the transcendence degree of the new residue field is the transcendence degree of
> the original residue field.

```lean
theorem fiberLocalRing_dimension_add_trdeg_eq
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})) :
    let Y := (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})
    let g : Y ⟶ X := pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let h : Y ⟶ Spec (.of K) := pullback.snd f (Spec.map
      (CommRingCat.ofHom (algebraMap k K)))
    let x := g.base y
    letI : Algebra k (X.residueField x) := (fieldToResidue f x).hom.toAlgebra
    letI : Algebra K (Y.residueField y) := (fieldToResidue h y).hom.toAlgebra
    ringKrullDim
          ((Y.presheaf.stalk y) ⧸
            Ideal.map (g.stalkMap y).hom
              (IsLocalRing.maximalIdeal (X.presheaf.stalk x))) +
        (Cardinal.toENat (Algebra.trdeg K (Y.residueField y)) : WithBot ℕ∞) =
      (Cardinal.toENat (Algebra.trdeg k (X.residueField x)) : WithBot ℕ∞)
```

## Tag 0C50, a lemma

[Tag 0C50](https://stacks.math.columbia.edu/tag/0C50) in the Stacks Project.

**`AlgebraicGeometry.map_maximalIdeal_stalkMap_eq_of_isReduced_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/MaximalIdealFieldChange.lean, line 858](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/MaximalIdealFieldChange.lean#L858).

> **Stacks Project, Tag 0C50.** Let `X` be locally of finite type over a field `k` and let
> `Y = X ×_{Spec k} Spec K` for an extension of fields `K / k`. If a point `y` of `Y` and its image
> `x` in `X` have local rings of the same dimension, and the scalar extension `κ(x) ⊗[k] K` of the
> residue field at `x` is reduced — for instance if `κ(x) / k` or `K / k` is separable — then the
> maximal ideal of `𝒪_{X, x}` generates the maximal ideal of `𝒪_{Y, y}`.

```lean
theorem map_maximalIdeal_stalkMap_eq_of_isReduced_tensorProduct
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hdim :
      ringKrullDim
          (X.presheaf.stalk
            ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)) =
        ringKrullDim
          ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).presheaf.stalk y))
    (hreduced :
      let x := (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y
      letI : (f x).asIdeal.IsPrime := (f x).isPrime
      letI := ((CommRingCat.ofHom (algebraMap k (f x).asIdeal.ResidueField)) ≫
        (Scheme.Spec.residueFieldIso (.of k) (f x)).inv ≫
        f.residueFieldMap x).hom.toAlgebra
      _root_.IsReduced (TensorProduct k (X.residueField x) K)) :
    Ideal.map
        ((pullback.fst f
          (Spec.map (CommRingCat.ofHom (algebraMap k K)))).stalkMap y).hom
        (IsLocalRing.maximalIdeal
          (X.presheaf.stalk
            ((pullback.fst f
              (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y))) =
      IsLocalRing.maximalIdeal
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).presheaf.stalk y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.5, Tag 0C4X](https://stacks.math.columbia.edu/tag/0C4X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
