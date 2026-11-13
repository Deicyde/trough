---
declaration: section
origin: cited
lean: AlgebraicGeometry.GeometricallyIrreducible, AlgebraicGeometry.geometricallyIrreducible_iff_baseChange_fieldExtension, AlgebraicGeometry.geometricallyIrreducible_of_irreducibleSpace_of_isSepClosed, AlgebraicGeometry.bijOn_image_irreducibleComponents_pullback_snd, AlgebraicGeometry.geometricallyIrreducible_tfae_local, AlgebraicGeometry.geometricallyIrreducible_open, AlgebraicGeometry.geometricallyIrreducible_fiber_iff_isGeometricallyIrreducible_residueField, AlgebraicGeometry.geometricallyIrreducible_fiber_genericPoint_iff_residueField_of_isAffine
statement: formalized
proof: formalized
---

# 33.8 Geometrically irreducible schemes

Section 33.8 of the Stacks Project, [Tag 0364](https://stacks.math.columbia.edu/tag/0364). 17 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0365, a definition

[Tag 0365](https://stacks.math.columbia.edu/tag/0365) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.GeometricallyIrreducible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.GeometricallyIrreducible#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch33.lean#L52) (StacksFrontier): “geometrically irreducible, for a morphism; the tag is the case of `X ⟶ Spec k`”. References: EGA IV (4.5.2), “more general”; EGA IV (4.5.5); EGA IV (4.5.9).

## Tag 054P, a lemma

[Tag 054P](https://stacks.math.columbia.edu/tag/054P) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_iff_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleBaseChange.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleBaseChange.lean#L42).

> **Stacks Project, Tag 054P.** A scheme over a field is geometrically irreducible if and only
> if its base change along any field extension is geometrically irreducible.

```lean
public theorem geometricallyIrreducible_iff_baseChange_fieldExtension
    (k k' : Type u) [Field k] [Field k'] [Algebra k k'] {X : Scheme.{u}}
    (f : X ⟶ Spec (of k)) :
    GeometricallyIrreducible f ↔
      GeometricallyIrreducible
        (pullback.snd f (Spec.map (ofHom (algebraMap k k'))))
```

## Tag 020J, a lemma

[Tag 020J](https://stacks.math.columbia.edu/tag/020J) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_of_irreducibleSpace_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparablyClosed.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparablyClosed.lean#L53). References: EGA IV (4.4.4), “more general”; EGA IV (4.5.9), “(b) ⇒ (a), special case”.

> **Stacks Project, Tag 020J.** An irreducible scheme over a separably closed field is
> geometrically irreducible.

```lean
public theorem geometricallyIrreducible_of_irreducibleSpace_of_isSepClosed
    (k : Type u) [Field k] [IsSepClosed k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [IrreducibleSpace X] : GeometricallyIrreducible f
```

## Tag 038F, a lemma

[Tag 038F](https://stacks.math.columbia.edu/tag/038F) in the Stacks Project.

**`AlgebraicGeometry.bijOn_image_irreducibleComponents_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleProductProjection.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleProductProjection.lean#L88). References: EGA IV (4.5.8), “more general”.

> **Stacks 038F.** Let `k` be a field and let `X`, `Y` be schemes over `k`, presented by
> their structure maps `f : X ⟶ Spec k` and `g : Y ⟶ Spec k`. If `X` is geometrically
> irreducible over `k`, then `X ×_k Y ⟶ Y` induces a bijection between irreducible components:
> taking images along it is a bijection from the irreducible components of `X ×_k Y` onto the
> irreducible components of `Y`.

```lean
public theorem bijOn_image_irreducibleComponents_pullback_snd
    (k : Type u) [Field k] {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [GeometricallyIrreducible f] :
    Set.BijOn (fun Z ↦ (pullback.snd f g).base '' Z)
      (irreducibleComponents (pullback (C := Scheme.{u}) f g))
      (irreducibleComponents Y)
```

## Tag 038G, a lemma

[Tag 038G](https://stacks.math.columbia.edu/tag/038G) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_tfae_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleLocal.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleLocal.lean#L118). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 038G.** For a scheme over a field, geometric irreducibility is
> equivalent to each of the three stated local criteria.

```lean
public theorem geometricallyIrreducible_tfae_local
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    let geometricallyIrreducibleSections := fun U : X.Opens ↦
      let : Algebra k Γ(X, U) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appLE ⊤ U (by simp)).hom.toAlgebra
      Algebra.IsGeometricallyIrreducible k Γ(X, U)
    List.TFAE
      [ GeometricallyIrreducible f,
        Nonempty X ∧ ∀ U : X.affineOpens,
          Nonempty (U : Set X) → geometricallyIrreducibleSections U.1,
        IrreducibleSpace X ∧
          ∃ (I : Type u) (U : I → X.affineOpens),
            (⨆ i, (U i).1) = ⊤ ∧ ∀ i, geometricallyIrreducibleSections (U i).1,
        ∃ (I : Type u) (_ : Nonempty I) (U : I → X.Opens),
          (⨆ i, U i) = ⊤ ∧
            (∀ i, GeometricallyIrreducible ((U i).ι ≫ f)) ∧
            ∀ i j, U i ⊓ U j ≠ ⊥ ]
```

**`AlgebraicGeometry.geometricallyIrreducible_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleLocal.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleLocal.lean#L186). The attribute's comment: “nonempty open subschemes”.

> **Stacks Project, Tag 038G.** Every nonempty open subscheme of a geometrically irreducible
> scheme over a field is geometrically irreducible.

```lean
public theorem geometricallyIrreducible_open
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [GeometricallyIrreducible f] (U : X.Opens) (hU : Nonempty U) :
    GeometricallyIrreducible (U.ι ≫ f)
```

## Tag 054Q, a lemma

[Tag 054Q](https://stacks.math.columbia.edu/tag/054Q) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_fiber_iff_isGeometricallyIrreducible_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericFibreResidueFieldCriterion.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericFibreResidueFieldCriterion.lean#L82). The attribute's comment: “the generic fibre, read on the residue field of the source”. References: EGA IV (4.5.12), “more general”.

> **The generic fibre is geometrically irreducible exactly when the residue field at the
> generic point is.** Let `R` be a domain and let `f : X ⟶ Spec R` carry the generic point of an
> irreducible `X` to the generic point `η` of `Spec R`. Then the generic fibre of `f` is
> geometrically irreducible over `κ(η)` if and only if the residue field of `X` at its generic
> point is geometrically irreducible over `κ(η)`.
>
> This is [Stacks, Tag 054Q] applied to the generic fibre, which is irreducible by
> `AlgebraicGeometry.Scheme.Hom.irreducibleSpace_fiber_of_genericPoint`, followed by the
> identification `AlgebraicGeometry.genericFiberResidueFieldMap` of its residue field at its
> generic point with that of `X`. `X` is not assumed reduced.

```lean
theorem geometricallyIrreducible_fiber_iff_isGeometricallyIrreducible_residueField :
    letI := residueFieldAlgebraOfEq f hgen
    GeometricallyIrreducible (f.fiberToSpecResidueField (genericPoint (Spec R))) ↔
      Algebra.IsGeometricallyIrreducible
        ↥((Spec R).residueField (genericPoint (Spec R))) ↥(X.residueField (genericPoint X))
```

**`AlgebraicGeometry.geometricallyIrreducible_fiber_genericPoint_iff_residueField_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericFibreResidueFieldCriterion.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericFibreResidueFieldCriterion.lean#L147). The attribute's comment: “the generic fibre over an affine base, read on the residue field of the source”. References: EGA IV (4.5.12), “more general”.

> **The generic fibre over an integral affine base is geometrically irreducible exactly when
> the residue field at the generic point is.** The criterion
> `AlgebraicGeometry.geometricallyIrreducible_fiber_iff_isGeometricallyIrreducible_residueField`
> for a base presented as an integral affine scheme rather than literally as the spectrum of a
> domain; the residue field of the base is then written at the generic point of
> `Spec Γ(Y, ⊤)`, which is where a fraction-field presentation of it is available.

```lean
theorem geometricallyIrreducible_fiber_genericPoint_iff_residueField_of_isAffine
    (hgen : f (genericPoint X) = genericPoint Y) :
    letI := residueFieldAlgebraOfEq (f ≫ Y.isoSpec.hom) (comp_isoSpec_genericPoint_eq f hgen)
    GeometricallyIrreducible (f.fiberToSpecResidueField (genericPoint Y)) ↔
      Algebra.IsGeometricallyIrreducible
        ↥((Spec Γ(Y, ⊤)).residueField (genericPoint (Spec Γ(Y, ⊤))))
        ↥(X.residueField (genericPoint X))
```

**`AlgebraicGeometry.geometricallyIrreducible_tfae_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/FunctionField.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/FunctionField.lean#L277). References: EGA IV (4.5.12); EGA IV (4.5.9), “(a) ⇔ (c)”.

> **Stacks Project, Tag 054Q.** For an irreducible scheme `X` over a field `k`, the following
> are equivalent: `X` is geometrically irreducible over `k`; the residue field at a generic point
> is geometrically irreducible over `k`; and the separable closure of `k` in that residue field is
> trivial.

```lean
public theorem geometricallyIrreducible_tfae_functionField
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IrreducibleSpace X] (ξ : X) (hξ : IsGenericPoint ξ Set.univ) :
    letI : Algebra k (X.residueField ξ) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation ξ).hom.toAlgebra
    List.TFAE [
      GeometricallyIrreducible f,
      Algebra.IsGeometricallyIrreducible k (X.residueField ξ),
      separableClosure k (X.residueField ξ) = ⊥]
```

**`Algebra.isGeometricallyIrreducible_tfae_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/GenericPointIrreducible.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyIntegral/GenericPointIrreducible.lean#L188). The attribute's comment: “The affine case. The source states this for an irreducible scheme `X` over `k` and the residue field at its generic point; here `X = Spec A`, and that the spectrum is irreducible is expressed by the hypothesis that the nilradical of `A` is the prime `I`. The scheme-level statement is NOT proved here: deducing it needs in addition the reduction of geometric irreducibility to affine opens (Stacks 038G, formalized as `AlgebraicGeometry.geometricallyIrreducible_tfae_local`) and the identification of the residue field at the generic point with the generic residue field of an affine open's ring of sections.”.

> Let `A` be an algebra over a field `k` whose spectrum is
> irreducible, i.e. whose nilradical `I` is prime; `I` is then the generic point of `Spec A` and
> `κ(I)` is the function field. The following are equivalent.
>
> 1. `A` is geometrically irreducible over `k`;
> 2. `κ(I)` is geometrically irreducible over `k`;
> 3. the separable closure of `k` in `κ(I)` is `k` itself.

```lean
theorem isGeometricallyIrreducible_tfae_residueField (k A : Type u) [Field k] [CommRing A]
    [Algebra k A] (I : Ideal A) [I.IsPrime] (hI : I = nilradical A) :
    List.TFAE [IsGeometricallyIrreducible k A, IsGeometricallyIrreducible k I.ResidueField,
      separableClosure k I.ResidueField = ⊥]
```

## Tag 0H8G, a lemma

[Tag 0H8G](https://stacks.math.columbia.edu/tag/0H8G) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_iff_irreducibleSpace_self_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSelfProduct.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSelfProduct.lean#L311). References: EGA IV (4.5.8), “(i), special case”.

> **Stacks Project, Tag 0H8G.** A scheme over a field is geometrically irreducible
> if and only if its self-product over the field is irreducible.

```lean
public theorem geometricallyIrreducible_iff_irreducibleSpace_self_pullback
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    GeometricallyIrreducible f ↔ IrreducibleSpace ↥(pullback f f)
```

## Tag 038H, a lemma

[Tag 038H](https://stacks.math.columbia.edu/tag/038H) in the Stacks Project.

**`AlgebraicGeometry.bijOn_irreducibleComponents_baseChange_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparablyClosed.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparablyClosed.lean#L71). References: EGA IV (4.5.19), “partial, special case”; EGA IV (4.5.21), “more general”; EGA IV (4.5.6), “(i), special case”; SGA 3 VIA (2.6.0), “k sep. alg. closed”.

> **Stacks Project, Tag 038H.** If `k` is separably algebraically closed, `k' / k` is a field
> extension, and `X` is a scheme over `k`, then the projection `X_{k'} ⟶ X` induces a bijection
> on irreducible components.

```lean
public theorem bijOn_irreducibleComponents_baseChange_of_isSepClosed
    (k k' : Type u) [Field k] [IsSepClosed k] [Field k'] [Algebra k k']
    (X : Scheme.{u}) (f : X ⟶ Spec (of k)) :
    Set.BijOn
      (fun Z ↦
        (pullback.fst (C := Scheme.{u}) f (Spec.map (ofHom (algebraMap k k')))).base '' Z)
      (irreducibleComponents
        (pullback (C := Scheme.{u}) f (Spec.map (ofHom (algebraMap k k')))))
      (irreducibleComponents X)
```

## Tag 038I, a lemma

[Tag 038I](https://stacks.math.columbia.edu/tag/038I) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_tfae_of_isSepClosure`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparableClosure.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleSeparableClosure.lean#L63). References: EGA IV (4.5.9).

> **Stacks Project, Tag 038I.** Geometric irreducibility of a scheme over a field can be tested
> after every finite separable extension, or after base change to any separable algebraic
> closure.

```lean
public lemma geometricallyIrreducible_tfae_of_isSepClosure
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (ksep : Type u) [Field ksep] [Algebra k ksep] [IsSepClosure k ksep] :
    List.TFAE
      [GeometricallyIrreducible f,
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
          [Algebra.IsSeparable k k'],
          IrreducibleSpace ↥(pullback f (Spec.map (ofHom (algebraMap k k')))),
    IrreducibleSpace ↥(pullback f (Spec.map (ofHom (algebraMap k ksep))))]
```

## Tag 04KW, a lemma

[Tag 04KW](https://stacks.math.columbia.edu/tag/04KW) in the Stacks Project.

**`AlgebraicGeometry.preimage_irreducibleComponent_eq_sUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean#L67).

> **Stacks Project, Tag 04KW.** After extension of the base field, the inverse image
> of an irreducible component is a union of irreducible components.

```lean
public theorem preimage_irreducibleComponent_eq_sUnion
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (T : Set X) (hT : T ∈ irreducibleComponents X) :
    let p : Scheme.{u} :=
      pullback (C := Scheme) f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let π : p ⟶ X :=
      pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    π.base ⁻¹' T =
      ⋃₀ {Z : Set p | Z ∈ irreducibleComponents p ∧ Z ⊆ π.base ⁻¹' T}
```

## Tag 04KX, a lemma

[Tag 04KX](https://stacks.math.columbia.edu/tag/04KX) in the Stacks Project.

**`AlgebraicGeometry.mapsTo_irreducibleComponents_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean#L237). References: SGA 3 VIA (2.6.0).

> **Stacks Project, Tag 04KX.** Let `K/k` be an extension of fields and let `X` be a scheme
> over `k`. The image of every irreducible component of `X ×_{Spec k} Spec K` under the projection
> to `X` is an irreducible component of `X`.

```lean
public theorem mapsTo_irreducibleComponents_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    Set.MapsTo
      (fun Z ↦ (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base '' Z)
      (irreducibleComponents
        (pullback (C := Scheme) f (Spec.map (CommRingCat.ofHom (algebraMap k K)))))
      (irreducibleComponents X)
```

**`AlgebraicGeometry.surjOn_irreducibleComponents_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/IrreducibleComponentsBaseChange.lean#L290).

> **Stacks Project, Tag 04KX.** Let `K/k` be an extension of fields and let `X` be a scheme
> over `k`. Every irreducible component of `X` is the image of an irreducible component of
> `X ×_{ Spec k} Spec K` under the projection to `X`.

```lean
public theorem surjOn_irreducibleComponents_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    Set.SurjOn
      (fun Z ↦ (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base '' Z)
      (irreducibleComponents
        (pullback (C := Scheme) f (Spec.map (CommRingCat.ofHom (algebraMap k K)))))
      (irreducibleComponents X)
```

## Tag 0G69, a lemma

[Tag 0G69](https://stacks.math.columbia.edu/tag/0G69) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_of_irreducibleSpace_of_dense_rationalPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleRationalPoints.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleRationalPoints.lean#L151).

> **Stacks Project, Tag 0G69.** An irreducible scheme over a field with a dense set of
> rational points is geometrically irreducible.

```lean
theorem geometricallyIrreducible_of_irreducibleSpace_of_dense_rationalPoints
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IrreducibleSpace X]
    (h : Dense {x : X | ∃ (s : Spec (.of k) ⟶ X),
      s ≫ f = 𝟙 (Spec (.of k)) ∧ x ∈ Set.range s.base}) :
    GeometricallyIrreducible f
```

## Tag 038J, a lemma

[Tag 038J](https://stacks.math.columbia.edu/tag/038J) in the Stacks Project.

**`AlgebraicGeometry.fixed_geometricComponent_iff_exists_geometricallyIrreducible_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GaloisFixedComponentDescent.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GaloisFixedComponentDescent.lean#L117). The attribute's comment: “fixed\_component\_descent”.

> A geometric irreducible component is fixed by the Galois action exactly when it descends
> to a geometrically irreducible component of the original scheme.

```lean
theorem fixed_geometricComponent_iff_exists_geometricallyIrreducible_component
    (k ksep : Type u) [Field k] [Field ksep] [Algebra k ksep]
    [IsSepClosure k ksep]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (Tbar : (galoisActionOnGeometricIrreducibleComponents k ksep (Over.mk f)).V) :
    (∀ σ : MulOpposite (ksep ≃ₐ[k] ksep),
      ConcreteCategory.hom
        ((galoisActionOnGeometricIrreducibleComponents k ksep (Over.mk f)).ρ σ).asHom Tbar =
        Tbar) ↔
      ∃ T : irreducibleComponents X,
        GeometricallyIrreducible
          ((Scheme.IdealSheafData.vanishingIdeal
              ⟨(T : Set X), isClosed_of_mem_irreducibleComponents T.1 T.2⟩).subschemeι ≫ f) ∧
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k ksep)))).base ⁻¹'
          (T : Set X) = Tbar.1
```

**`AlgebraicGeometry.galoisActionOnGeometricIrreducibleComponents`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisAction.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisAction.lean#L162). The attribute's comment: “galois\_action\_on\_geometric\_irreducible\_components”.

> The canonical action of the opposite Galois group on the irreducible components of a scheme
> after base change. A component is sent to its image under the corresponding automorphism of the
> base-changed scheme.

```lean
public noncomputable def galoisActionOnGeometricIrreducibleComponents
    (X : Over (Spec (.of R))) :
    Action (Type u) (MulOpposite (S ≃ₐ[R] S))
```

**`AlgebraicGeometry.galoisActionOnGeometricIrreducibleComponents_fixed_iff_and_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisActionCompatibility.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisActionCompatibility.lean#L97). References: EGA IV (4.5.21), “more general”.

> **Stacks Project, Tag 038J.** Let `k` be a field with separable algebraic closure `ksep` and
> let `X` be a scheme over `k`. The canonical action of `Gal(ksep/k)ᵐᵒᵖ` on the irreducible
> components of `X_{ksep}` has the following properties.
>
> 1. A component `Tbar` is fixed by the action if and only if there is an irreducible component
>    `T` of `X`, geometrically irreducible over `k`, with `T_{ksep} = Tbar`.
> 2. For every field extension `k'/k` with separable algebraic closure `ksep'`, and every embedding
>    `ksep → ksep'` over `k`, taking images along `X_{ksep'} ⟶ X_{ksep}` is a bijection on
>    irreducible components (Tag 038H), and it intertwines the action of `Gal(ksep'/k')` with
>    the action of `Gal(ksep/k)` through restriction of automorphisms.
>
> Geometric irreducibility of `T` is that of its reduced induced closed subscheme over `k`, and
> `T_{ksep}` is the inverse image of `T` in `X_{ksep}`.

```lean
public theorem galoisActionOnGeometricIrreducibleComponents_fixed_iff_and_compatible
    (k ksep : Type u) [Field k] [Field ksep] [Algebra k ksep] [IsSepClosure k ksep]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    (∀ Tbar : (galoisActionOnGeometricIrreducibleComponents k ksep (Over.mk f)).V,
      (∀ σ : MulOpposite (ksep ≃ₐ[k] ksep),
        ConcreteCategory.hom
          ((galoisActionOnGeometricIrreducibleComponents k ksep (Over.mk f)).ρ σ).asHom Tbar =
            Tbar) ↔
        ∃ T : irreducibleComponents X,
          GeometricallyIrreducible
            ((Scheme.IdealSheafData.vanishingIdeal
                ⟨(T : Set X), isClosed_of_mem_irreducibleComponents T.1 T.2⟩).subschemeι ≫ f) ∧
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k ksep)))).base ⁻¹'
            (T : Set X) = Tbar.1) ∧
    ∀ (k' ksep' : Type u) [Field k'] [Field ksep']
      [Algebra k k'] [Algebra k' ksep'] [Algebra k ksep'] [Algebra ksep ksep']
      [IsScalarTower k k' ksep'] [IsScalarTower k ksep ksep'] [IsSepClosure k' ksep'],
      Set.BijOn (fun Z ↦ (baseChangeComparison k ksep ksep' X f).base '' Z)
          (irreducibleComponents
            (pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k ksep')))))
          (irreducibleComponents
            (pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k ksep))))) ∧
        ∀ (σ : MulOpposite (ksep' ≃ₐ[k'] ksep'))
          (Z : (galoisActionOnGeometricIrreducibleComponents k ksep' (Over.mk f)).V),
          irreducibleComponentsBaseChangeComparisonEquiv k ksep ksep' (hsep :=
              IsSepClosure.sep_closed k) X f
            (ConcreteCategory.hom
              ((galoisActionOnGeometricIrreducibleComponents k ksep' (Over.mk f)).ρ
                (MulOpposite.op (AlgEquiv.restrictScalars k σ.unop))).asHom Z) =
          ConcreteCategory.hom
            ((galoisActionOnGeometricIrreducibleComponents k ksep (Over.mk f)).ρ
              (MulOpposite.op
                ((AlgEquiv.restrictNormalHom ksep) (AlgEquiv.restrictScalars k σ.unop)))).asHom
            (irreducibleComponentsBaseChangeComparisonEquiv k ksep ksep' (hsep :=
              IsSepClosure.sep_closed k) X f Z)
```

## Tag 04KY, a lemma

[Tag 04KY](https://stacks.math.columbia.edu/tag/04KY) in the Stacks Project.

**`AlgebraicGeometry.fiber_irreducibleComponentsBaseChangeMap_eq_orbit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/GaloisOrbit.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/GaloisOrbit.lean#L465).

> **Stacks Project, Tag 04KY.** For a scheme over a field `k` and a normal extension `K/k`,
> for instance a separable closure of `k`, the fibre through each geometric irreducible component
> of the canonical map to the irreducible components downstairs is its orbit under the group
> `K ≃ₐ[k] K`.

```lean
public theorem fiber_irreducibleComponentsBaseChangeMap_eq_orbit
    (k K : Type u) [Field k] [Field K] [Algebra k K] [Normal k K]
    (X : Over (Spec (.of k)))
    (Z : (galoisActionOnGeometricIrreducibleComponents k K X).V) :
    (irreducibleComponentsBaseChangeMap k K X) ⁻¹'
        {irreducibleComponentsBaseChangeMap k K X Z} =
      Set.range (fun σ : MulOpposite (K ≃ₐ[k] K) ↦
        ConcreteCategory.hom
          ((galoisActionOnGeometricIrreducibleComponents k K X).ρ σ).asHom Z)
```

## Tag 04KZ, a lemma

[Tag 04KZ](https://stacks.math.columbia.edu/tag/04KZ) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_subextension_defining_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/FiniteExtension.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/FiniteExtension.lean#L408). The attribute's comment: “component\_defined\_over\_finite\_extension”.

> **Stacks Project, Tag 04KZ.** Every irreducible component after extension to a separable
> closure is defined over a finite intermediate extension.

```lean
public theorem exists_finite_subextension_defining_component
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsSepClosure k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (Z : irreducibleComponents
      (pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    ∃ (E : IntermediateField k K) (_ : FiniteDimensional k E)
      (T : irreducibleComponents
        (pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k E)))))
      (p : pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k K))) ⟶
        pullback (C := Scheme.{u}) f (Spec.map (CommRingCat.ofHom (algebraMap k E)))),
      p ≫ pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k E))) =
          pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))) ∧
        p ≫ pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k E))) =
          pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))) ≫
            Spec.map (CommRingCat.ofHom E.val) ∧
        p.base ⁻¹' (T : Set _) = (Z : Set _)
```

**`AlgebraicGeometry.continuous_galoisActionOnGeometricIrreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/OrbitDecomposition.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/OrbitDecomposition.lean#L85). The attribute's comment: “continuous\_action”.

> **Stacks Project, Tag 04KZ.** The Galois action on the geometric irreducible components
> of a locally finite-type scheme is continuous when the component set is discrete.

```lean
public theorem continuous_galoisActionOnGeometricIrreducibleComponents
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsSepClosure k K]
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom] :
    letI : TopologicalSpace (galoisActionOnGeometricIrreducibleComponents k K X).V := ⊥
    Continuous (fun p : MulOpposite (K ≃ₐ[k] K) ×
        (galoisActionOnGeometricIrreducibleComponents k K X).V =>
      ConcreteCategory.hom
        ((galoisActionOnGeometricIrreducibleComponents k K X).ρ p.1).asHom p.2)
```

**`AlgebraicGeometry.exists_finite_single_orbit_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/OrbitDecomposition.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/OrbitDecomposition.lean#L205). The attribute's comment: “finite\_single\_orbit\_decomposition”.

> **Stacks Project, Tag 04KZ.** Over a separable closure, the inverse image of an irreducible
> component is a finite union of irreducible components forming a single Galois orbit.

```lean
public theorem exists_finite_single_orbit_decomposition
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsSepClosure k K]
    (X : Over (Spec (.of k))) [LocallyOfFiniteType X.hom]
    (T : irreducibleComponents X.left) :
    ∃ s : Finset (galoisActionOnGeometricIrreducibleComponents k K X).V,
      s.Nonempty ∧
        ((pullback.fst X.hom (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base ⁻¹'
              (T : Set X.left) =
            ⋃ Z ∈ s, Z.1) ∧
          ∀ Z ∈ s, ∀ Z' ∈ s,
            ∃ σ : MulOpposite (K ≃ₐ[k] K),
              ConcreteCategory.hom
                  ((galoisActionOnGeometricIrreducibleComponents k K X).ρ σ).asHom Z = Z'
```

## Tag 054R, a lemma

[Tag 054R](https://stacks.math.columbia.edu/tag/054R) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_separable_extension_geometricallyIrreducible_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/ComponentsOverFiniteSeparableExtension.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/ComponentsOverFiniteSeparableExtension.lean#L272).

> **Stacks Project, Tag 054R.** After a finite separable extension of the ground field, every
> irreducible component of a scheme locally of finite type over a field is geometrically
> irreducible, provided that the original scheme has only finitely many irreducible components.

```lean
public theorem exists_finite_separable_extension_geometricallyIrreducible_components
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (hX : (irreducibleComponents X).Finite) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k')
      (_ : FiniteDimensional k k') (_ : Algebra.IsSeparable k k'),
      let X' := pullback (C := Scheme.{u}) f (Spec.map (ofHom (algebraMap k k')))
      ∀ Z : irreducibleComponents X',
        GeometricallyIrreducible
          ((Scheme.IdealSheafData.vanishingIdeal (X := X')
              ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩).subschemeι ≫
            pullback.snd f (Spec.map (ofHom (algebraMap k k'))))
```

## Tag 054S, a lemma

[Tag 054S](https://stacks.math.columbia.edu/tag/054S) in the Stacks Project.

**`TopologicalSpace.finite_connectedComponents_of_finite_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/ConnectedComponents.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/ConnectedComponents.lean#L59). The attribute's comment: “finiteness of connected components”.

> **Stacks Project, Tag 054S.** Finitely many irreducible components imply finitely many
> connected components.

```lean
public theorem finite_connectedComponents_of_finite_irreducibleComponents
    {X : Type*} [TopologicalSpace X] (hX : (irreducibleComponents X).Finite) :
    Finite (ConnectedComponents X)
```

**`AlgebraicGeometry.geometricallyConnected_connectedComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/ConnectedComponents.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricIrreducibleComponents/ConnectedComponents.lean#L92). The attribute's comment: “geometric connectedness of connected components”. References: EGA IV (4.5.13.1), “(ii)”.

> **Stacks Project, Tag 054S.** If each of the finitely many irreducible components of a
> scheme over a field is geometrically irreducible, each connected component has an open
> subscheme structure that is geometrically connected over that field.

```lean
public theorem geometricallyConnected_connectedComponent
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (hX : (irreducibleComponents X).Finite)
    (hgeom : ∀ Z : irreducibleComponents X,
      GeometricallyIrreducible
        ((Scheme.IdealSheafData.vanishingIdeal (X := X)
            ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩).subschemeι ≫ f))
    (c : ConnectedComponents X) :
    ∃ U : X.Opens,
      (U : Set X) = (ConnectedComponents.mk : X → ConnectedComponents X) ⁻¹' {c} ∧
        GeometricallyConnected (U.ι ≫ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.8, Tag 0364](https://stacks.math.columbia.edu/tag/0364)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
