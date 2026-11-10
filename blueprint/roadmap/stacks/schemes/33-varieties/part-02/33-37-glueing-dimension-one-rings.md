---
declaration: section
origin: cited
lean: Ring.GluingSituation, Ring.GluingSituation.R, Ring.GluingSituation.coe_R, Ring.GluingSituation.subtype_comp_algebraMap_eq, Ring.GluingSituation.equivPullback, Subring.not_surjective_tensorProduct_iff_exists_isDiscreteValuationRing, Ring.SemilocalDVRGluingSituation.exists_maximalIdeal_localization_le_of_units_mem_inf, Ring.SemilocalDVRGluingSituation.not_surjective_tensorProduct_of_units_mem_inf
statement: formalized
proof: formalized
---

# 33.37 Glueing dimension one rings

Section 33.37 of the Stacks Project, [Tag 09MX](https://stacks.math.columbia.edu/tag/09MX). 11 tags here are carried by 31 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09MY, a situation

[Tag 09MY](https://stacks.math.columbia.edu/tag/09MY) in the Stacks Project.

**`Ring.GluingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean#L60). The attribute's comment: “the standing data”.

> **Stacks Project, Tag 09MY.** The standing data for glueing two rings along a common
> fraction field: a field `K` together with two subrings `A` and `B` of `K`, each of which has
> `K` as its fraction field. These fit into a commutative square whose fourth corner is the
> ring `R = A ×_K B = A ∩ B`.

```lean
public structure GluingSituation
```

**`Ring.GluingSituation.R`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean#L84). The attribute's comment: “the fourth corner of the square”.

> The fourth corner `R = A ×_K B` of the commutative square, realized as the intersection
> of `A` and `B` in `K`.

```lean
public def R (S : GluingSituation) : Subring S.K
```

**`Ring.GluingSituation.coe_R`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean#L108). The attribute's comment: “the identification `R = A ∩ B`”.

> The fourth corner of the square is the intersection `A ∩ B` inside the common field.

```lean
public lemma coe_R (S : GluingSituation) : (S.R : Set S.K) = (S.A : Set S.K) ∩ S.B
```

**`Ring.GluingSituation.subtype_comp_algebraMap_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean#L113). The attribute's comment: “commutativity of the square”.

> The square commutes: the two composites `R → A → K` and `R → B → K` agree.

```lean
public lemma subtype_comp_algebraMap_eq (S : GluingSituation) :
    S.A.subtype.comp (algebraMap S.R S.A) = S.B.subtype.comp (algebraMap S.R S.B)
```

**`Ring.GluingSituation.equivPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GluingSituation.lean#L128). The attribute's comment: “the identification `R = A ×_K B`”.

> The fourth corner of the square is the fibre product `A ×_K B`: the intersection of `A`
> and `B` in `K` is canonically isomorphic to the subring of `A × B` of pairs having the same
> image in `K`.

```lean
public def equivPullback (S : GluingSituation) :
    S.R ≃+* RingHom.pullback S.A.subtype S.B.subtype
```

## Tag 09N0, a lemma

[Tag 09N0](https://stacks.math.columbia.edu/tag/09N0) in the Stacks Project.

**`Subring.not_surjective_tensorProduct_iff_exists_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/TensorProductCriterion.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/TensorProductCriterion.lean#L97).

> For two subrings of a field that is the fraction field of the first, with
> the first Noetherian and one-dimensional, the multiplication map from their
> tensor product is not surjective if and only if they are contained in a common
> discrete valuation subring.

```lean
public theorem not_surjective_tensorProduct_iff_exists_isDiscreteValuationRing
    {K : Type u} [Field K] (A B : Subring K)
    [IsFractionRing A K] [IsNoetherianRing A]
    (h_dim : ringKrullDim A = 1) :
    (¬ Function.Surjective
      (Algebra.TensorProduct.lift (B := B) A.subtype.toIntAlgHom
        B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) ↔
      ∃ O : Subring K, IsDiscreteValuationRing O ∧ A ≤ O ∧ B ≤ O
```

## Tag 09N1, a lemma

[Tag 09N1](https://stacks.math.columbia.edu/tag/09N1) in the Stacks Project.

**`Ring.SemilocalDVRGluingSituation.exists_maximalIdeal_localization_le_of_units_mem_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L284). The attribute's comment: “all_units_in_r”.

> If every unit of `A` belongs to `A ∩ B`, then the DVR `B` dominates the
> localization of `A` at some maximal ideal.

```lean
theorem exists_maximalIdeal_localization_le_of_units_mem_inf
    (h_units : ∀ u : S.Aˣ, (((u : S.A) : S.K) ∈ S.R)) :
    ∃ p : MaximalSpectrum S.A,
      LocalSubring.ofPrime S.A p.asIdeal ≤
        ({ toSubring := S.B } : LocalSubring S.K)
```

**`Ring.SemilocalDVRGluingSituation.not_surjective_tensorProduct_of_units_mem_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L312). The attribute's comment: “all_units_in_r”.

> If every unit of `A` belongs to `A ∩ B`, then the canonical
> multiplication map `A ⊗[ℤ] B → K` is not surjective.

```lean
theorem not_surjective_tensorProduct_of_units_mem_inf
    (h_units : ∀ u : S.Aˣ, (((u : S.A) : S.K) ∈ S.R)) :
    ¬ Function.Surjective
      (Algebra.TensorProduct.lift (B := S.B) S.A.subtype.toIntAlgHom
        S.B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))
```

**`Ring.SemilocalDVRGluingSituation.isOpenImmersion_specMap_R_A_of_unit_not_mem_R`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L530). The attribute's comment: “unit_outside_r”.

> If a unit of `A` lies outside `R`, the map from `Spec A` to `Spec R` is an open
> immersion.

```lean
public theorem isOpenImmersion_specMap_R_A_of_unit_not_mem_R
    (h : ¬ ∀ a : S.Aˣ, (((a : S.A) : S.K) ∈ S.R)) :
    IsOpenImmersion
      (Scheme.Spec.map
        (CommRingCat.ofHom ((S.A ⊓ S.B : Subring S.K).inclusion inf_le_left)).op)
```

**`Ring.SemilocalDVRGluingSituation.isOpenImmersion_specMap_R_B_of_unit_not_mem_R`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L544). The attribute's comment: “unit_outside_r”.

> If a unit of `A` lies outside `R`, the map from `Spec B` to `Spec R` is an open
> immersion.

```lean
public theorem isOpenImmersion_specMap_R_B_of_unit_not_mem_R
    (h : ¬ ∀ a : S.Aˣ, (((a : S.A) : S.K) ∈ S.R)) :
    IsOpenImmersion
      (Scheme.Spec.map
        (CommRingCat.ofHom ((S.A ⊓ S.B : Subring S.K).inclusion inf_le_right)).op)
```

**`Ring.SemilocalDVRGluingSituation.range_specMap_R_A_union_R_B_of_unit_not_mem_R`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L559). The attribute's comment: “unit_outside_r”.

> If a unit of `A` lies outside `R`, the images of `Spec A` and `Spec B` cover `Spec R`.

```lean
public theorem range_specMap_R_A_union_R_B_of_unit_not_mem_R
    (h : ¬ ∀ a : S.Aˣ, (((a : S.A) : S.K) ∈ S.R)) :
    Set.range
        (Scheme.Spec.map
          (CommRingCat.ofHom ((S.A ⊓ S.B : Subring S.K).inclusion inf_le_left)).op).base ∪
      Set.range
        (Scheme.Spec.map
          (CommRingCat.ofHom ((S.A ⊓ S.B : Subring S.K).inclusion inf_le_right)).op).base =
      Set.univ
```

**`Ring.SemilocalDVRGluingSituation.tensorProductTo_bijective_of_unit_not_mem_R`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueDVR.lean#L601). The attribute's comment: “unit_outside_r”.

> If a unit of `A` lies outside `R`, multiplication identifies `A ⊗[R] B` with the
> common fraction field.

```lean
public theorem tensorProductTo_bijective_of_unit_not_mem_R
    (h : ¬ ∀ a : S.Aˣ, (((a : S.A) : S.K) ∈ S.R)) :
    Function.Bijective (tensorProductTo S)
```

## Tag 09N2, a lemma

[Tag 09N2](https://stacks.math.columbia.edu/tag/09N2) in the Stacks Project.

**`IsIntegralClosure.finite_maximalSpectrum`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean#L130). The attribute's comment: “the semilocal assertion”. References: EGA 0 (23.2.6), “K' = K case”.

> The integral closure of a semilocal Noetherian domain of dimension at most one in its
> fraction field is semilocal.

```lean
public lemma finite_maximalSpectrum (B : Type u) (K : Type v) (C : Type w)
    [CommRing B] [IsDomain B] [IsNoetherianRing B]
    [Ring.DimensionLEOne B] [Finite (MaximalSpectrum B)] [Field K] [Algebra B K]
    [IsFractionRing B K] [CommRing C] [Algebra B C] [Algebra C K] [IsScalarTower B C K]
    [IsIntegralClosure C B K] :
    Finite (MaximalSpectrum C)
```

**`IsIntegralClosure.exists_pow_mul_mem_range`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean#L155). The attribute's comment: “the conductor assertion”.

> A nonzero element of the Jacobson radical of the integral closure eventually carries every
> element of the integral closure into the original domain.

```lean
public lemma exists_pow_mul_mem_range (B : Type u) (K : Type v) (C : Type w)
    [CommRing B] [IsDomain B] [IsNoetherianRing B]
    [Ring.DimensionLEOne B] [Finite (MaximalSpectrum B)] [Field K] [Algebra B K]
    [IsFractionRing B K] [CommRing C] [Algebra B C] [Algebra C K] [IsScalarTower B C K]
    [IsIntegralClosure C B K]
    (x : C) (hx : x ≠ 0) (hxj : x ∈ Ring.jacobson C) (y : C) :
    ∃ n : ℕ, x ^ n * y ∈ RingHom.range (algebraMap B C)
```

Declarations registered for the tag:

- [`IsIntegralClosure.isDedekindDomain_and_comap_surjective_and_quasiFinite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/DedekindDomain.lean#L339), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/IntegralClosure.lean#L122) (StacksFrontier): “the Dedekind-domain assertion”.

## Tag 09N3, a lemma

[Tag 09N3](https://stacks.math.columbia.edu/tag/09N3) in the Stacks Project.

**`Subring.isOpenImmersion_specMap_inf_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean#L279). The attribute's comment: “the open immersion from A”.

> The left-hand subring gives an open immersion into the spectrum of the intersection.

```lean
public theorem isOpenImmersion_specMap_inf_left
    (hA : ringKrullDim A = 1) (hB : ringKrullDim B = 1)
    (h_surj : Function.Surjective
      (Algebra.TensorProduct.lift (B := B) A.subtype.toIntAlgHom
        B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) :
    IsOpenImmersion
      (Scheme.Spec.map
        (CommRingCat.ofHom ((A ⊓ B : Subring K).inclusion inf_le_left)).op)
```

**`Subring.isOpenImmersion_specMap_inf_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean#L299). The attribute's comment: “the open immersion from B”.

> The right-hand subring gives an open immersion into the spectrum of the intersection.

```lean
public theorem isOpenImmersion_specMap_inf_right
    (hA : ringKrullDim A = 1) (hB : ringKrullDim B = 1)
    (h_surj : Function.Surjective
      (Algebra.TensorProduct.lift (B := B) A.subtype.toIntAlgHom
        B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) :
    IsOpenImmersion
      (Scheme.Spec.map
        (CommRingCat.ofHom ((A ⊓ B : Subring K).inclusion inf_le_right)).op)
```

**`Subring.range_specMap_inf_left_union_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean#L319). The attribute's comment: “the covering assertion”.

> The images of the two spectra cover the spectrum of the intersection.

```lean
public theorem range_specMap_inf_left_union_right
    (hA : ringKrullDim A = 1) (hB : ringKrullDim B = 1)
    (h_surj : Function.Surjective
      (Algebra.TensorProduct.lift (B := B) A.subtype.toIntAlgHom
        B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) :
    Set.range
        (Scheme.Spec.map
          (CommRingCat.ofHom ((A ⊓ B : Subring K).inclusion inf_le_left)).op).base ∪
      Set.range
        (Scheme.Spec.map
          (CommRingCat.ofHom ((A ⊓ B : Subring K).inclusion inf_le_right)).op).base =
      Set.univ
```

**`Subring.intersectionTensorProductTo_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueTwo.lean#L364). The attribute's comment: “the tensor-product assertion”.

> Multiplication identifies the tensor product over the intersection with the common fraction
> field.

```lean
public theorem intersectionTensorProductTo_bijective
    (hA : ringKrullDim A = 1) (hB : ringKrullDim B = 1)
    (h_surj : Function.Surjective
      (Algebra.TensorProduct.lift (B := B) A.subtype.toIntAlgHom
        B.subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) :
    Function.Bijective (intersectionTensorProductTo A B)
```

## Tag 09N4, a lemma

[Tag 09N4](https://stacks.math.columbia.edu/tag/09N4) in the Stacks Project.

**`Subring.isNoetherianRing_gluedSubring`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L748). The attribute's comment: “the Noetherian assertion”.

> The intersection is Noetherian.

```lean
lemma isNoetherianRing_gluedSubring : IsNoetherianRing (gluedSubring B)
```

**`Subring.finite_maximalSpectrum_gluedSubring`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L755). The attribute's comment: “the semilocal assertion”.

> The intersection is semilocal.

```lean
lemma finite_maximalSpectrum_gluedSubring : Finite (MaximalSpectrum (gluedSubring B))
```

**`Subring.ringKrullDim_gluedSubring`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L762). The attribute's comment: “the dimension assertion”.

> The intersection has Krull dimension one.

```lean
lemma ringKrullDim_gluedSubring : ringKrullDim (gluedSubring B) = 1
```

**`Subring.isOpenImmersion_specMap_gluedSubringInclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L770). The attribute's comment: “part (1)”.

> The map on affine spectra induced by inclusion of the intersection into each member is an
> open immersion.

```lean
lemma isOpenImmersion_specMap_gluedSubringInclusion (i : ι) :
    AlgebraicGeometry.IsOpenImmersion
      (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (gluedSubringInclusion B i)))
```

**`Subring.iUnion_range_comap_gluedSubringInclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 780](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L780). The attribute's comment: “part (2)”.

> The images of the spectra of the members cover the spectrum of the intersection.

```lean
lemma iUnion_range_comap_gluedSubringInclusion :
    (⋃ i, Set.range (PrimeSpectrum.comap (gluedSubringInclusion B i))) = Set.univ
```

**`Subring.existsUnique_range_comap_gluedSubringInclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean, line 798](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/GlueFinite.lean#L798). The attribute's comment: “part (3)”.

> Every closed point of the spectrum of the intersection is in the image of exactly one
> member of the family.

```lean
lemma existsUnique_range_comap_gluedSubringInclusion
    (x : MaximalSpectrum (gluedSubring B)) :
    ∃! i, x.toPrimeSpectrum ∈ Set.range
      (PrimeSpectrum.comap (gluedSubringInclusion B i))
```

## Tag 09N5, a lemma

[Tag 09N5](https://stacks.math.columbia.edu/tag/09N5) in the Stacks Project.

**`Ring.exists_ne_zero_inverse_mem_jacobson_of_tensorProduct_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/JacobsonInverse.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/JacobsonInverse.lean#L47).

> For finitely many Noetherian one-dimensional semilocal subrings of a common
> fraction field, surjectivity of the corresponding multiplication maps produces
> a nonzero element whose reciprocal belongs to all their Jacobson radicals.

```lean
public theorem exists_ne_zero_inverse_mem_jacobson_of_tensorProduct_surjective
    {K : Type u} [Field K] {ι : Type v} [Finite ι]
    (A : Subring K) (B : ι → Subring K)
    [IsFractionRing A K] [∀ i, IsFractionRing (B i) K]
    [∀ i, IsNoetherianRing (B i)] [∀ i, Finite (MaximalSpectrum (B i))]
    (h_dim : ∀ i, ringKrullDim (B i) = 1)
    (h_surj : ∀ i, Function.Surjective
      (Algebra.TensorProduct.lift (B := B i) A.subtype.toIntAlgHom
        (B i).subtype.toIntAlgHom (fun _ _ ↦ Commute.all _ _))) :
    ∃ x : A, x ≠ 0 ∧ ∀ i, ∃ y : B i,
      (y : K) = (x : K)⁻¹ ∧ y ∈ Ideal.jacobson (⊥ : Ideal (B i))
```

## Tag 0AB2, a lemma

[Tag 0AB2](https://stacks.math.columbia.edu/tag/0AB2) in the Stacks Project.

**`IsLocalRing.exists_pow_eq_pow_of_eq_at_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/MinimalPrimes.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/MinimalPrimes.lean#L94).

> Two elements of a Noetherian local ring of dimension at most one which
> agree at every minimal prime have equal positive powers if one lies in the
> maximal ideal.

```lean
public theorem exists_pow_eq_pow_of_eq_at_minimalPrimes
    {A : Type*} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hdim : ringKrullDim A ≤ 1) (a₁ a₂ : A)
    (ha₂ : a₂ ∈ IsLocalRing.maximalIdeal A)
    (heq : ∀ p : minimalPrimes A,
      (algebraMap A (@Localization.AtPrime A _ p.1 p.2.isPrime)) a₁ =
        (algebraMap A (@Localization.AtPrime A _ p.1 p.2.isPrime)) a₂) :
    ∃ n : ℕ, 0 < n ∧ a₁ ^ n = a₂ ^ n
```

## Tag 0AB3, a lemma

[Tag 0AB3](https://stacks.math.columbia.edu/tag/0AB3) in the Stacks Project.

**`IsLocalRing.exists_pow_mem_range_of_sub_mem_nilradical_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/MinimalPrimesPower.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/MinimalPrimesPower.lean#L124).

> **Stacks 0AB3.** An element of the product of the minimal-prime localizations that is
> congruent, modulo the extended nilradical, to an element of the maximal ideal has a positive
> power in the image of the original ring.

```lean
public theorem exists_pow_mem_range_of_sub_mem_nilradical_map
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hdim : ringKrullDim A = 1) :
    let L := ∀ p : {q : PrimeSpectrum A // q.asIdeal ∈ minimalPrimes A},
      Localization.AtPrime p.1.asIdeal
    let I : Ideal A := sInf (minimalPrimes A)
      ∀ (f : L) (a : A), a ∈ IsLocalRing.maximalIdeal A →
      f - algebraMap A L a ∈ I.map (algebraMap A L) →
        ∃ n : ℕ, 0 < n ∧ f ^ n ∈ Set.range (algebraMap A L)
```

## Tag 0AB4, a lemma

[Tag 0AB4](https://stacks.math.columbia.edu/tag/0AB4) in the Stacks Project.

**`IsLocalRing.exists_mem_maximalIdeal_radical_span_eq_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/DimensionOneRings.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/DimensionOneRings.lean#L608).

> **Stacks Project, Tag 0AB4.** An integral subring of the product of the minimal-prime
> localizations contains the image of a parameter of a one-dimensional Noetherian local ring.

```lean
public theorem exists_mem_maximalIdeal_radical_span_eq_of_isIntegral
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hdim : ringKrullDim A = 1) :
    let L := ∀ p : {q : PrimeSpectrum A // q.asIdeal ∈ minimalPrimes A},
      Localization.AtPrime p.1.asIdeal
    ∀ (K : Type v) [CommRing K] (f : K →+* L), f.IsIntegral →
      ∃ a : A, a ∈ IsLocalRing.maximalIdeal A ∧
        (∃ x : K, f x = algebraMap A L a) ∧
        (Ideal.span {a}).radical = IsLocalRing.maximalIdeal A
```

## Tag 09N6, a lemma

[Tag 09N6](https://stacks.math.columbia.edu/tag/09N6) in the Stacks Project.

**`Ideal.primeFamilyCompl`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean#L45). The attribute's comment: “the multiplicative system”.

> The elements outside every prime ideal in a finite family.

```lean
public abbrev primeFamilyCompl (s : Finset {p : Ideal A // p.IsPrime}) : Submonoid A
```

**`Ideal.finite_maximalSpectrum_localization_primeFamilyCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean#L120). The attribute's comment: “semilocality”.

> Localization outside finitely many prime ideals is semilocal.

```lean
public theorem finite_maximalSpectrum_localization_primeFamilyCompl
    (s : Finset {p : Ideal A // p.IsPrime})
    {B : Type*} [CommRing B] [Algebra A B] [IsLocalization (primeFamilyCompl s) B] :
    Finite (MaximalSpectrum B)
```

**`Ideal.bijOn_under_maximalSpectrum_localization_primeFamilyCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Semilocalization.lean#L134). The attribute's comment: “the maximal ideals”. References: EGA I (8.1.2), “partial”.

> Contraction identifies the maximal ideals of the localization with the maximal members of
> the finite family of prime ideals.

```lean
public theorem bijOn_under_maximalSpectrum_localization_primeFamilyCompl
    (s : Finset {p : Ideal A // p.IsPrime})
    {B : Type*} [CommRing B] [Algebra A B] [IsLocalization (primeFamilyCompl s) B] :
    Set.BijOn (fun m : MaximalSpectrum B => m.asIdeal.under A) Set.univ
      {p : Ideal A | (∃ q ∈ s, p = q.1) ∧
        ∀ q ∈ s, p ≤ q.1 → p = q.1}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.37, Tag 09MX](https://stacks.math.columbia.edu/tag/09MX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
