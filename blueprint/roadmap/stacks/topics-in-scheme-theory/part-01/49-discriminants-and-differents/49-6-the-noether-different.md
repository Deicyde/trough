---
declaration: section
origin: cited
lean: Stacks.Discriminant.bijOn_diagonalAnnihilator_prod, Stacks.Discriminant.noetherDifferent_prod, Stacks.Discriminant.map_diagonalAnnihilator_eq, Stacks.Discriminant.map_noetherDifferent_eq, Stacks.Discriminant.diagonalAnnihilatorBaseChange_injective, Stacks.Discriminant.range_diagonalAnnihilatorBaseChange, Stacks.Discriminant.noetherDifferent_eq_map, Stacks.Discriminant.noetherPairingWithFormula
statement: formalized
proof: formalized
---

# 49.6 The Noether different

Section 49.6 of the Stacks Project, [Tag 0BVK](https://stacks.math.columbia.edu/tag/0BVK). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BVL, a lemma

[Tag 0BVL](https://stacks.math.columbia.edu/tag/0BVL) in the Stacks Project.

**`Stacks.Discriminant.bijOn_diagonalAnnihilator_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Basic.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Basic.lean#L188). The attribute's comment: “part (1)”.

> The canonical pair of tensor-square projections identifies the annihilator of the
> kernel of multiplication for a product algebra with the product of the corresponding
> annihilators.

```lean
theorem bijOn_diagonalAnnihilator_prod
    (A : Type u) (B₁ : Type v) (B₂ : Type w)
    [CommRing A] [CommRing B₁] [CommRing B₂] [Algebra A B₁] [Algebra A B₂] :
    Set.BijOn
      (fun x : (B₁ × B₂) ⊗[A] (B₁ × B₂) ↦
        (Algebra.TensorProduct.map (AlgHom.fst A B₁ B₂) (AlgHom.fst A B₁ B₂) x,
          Algebra.TensorProduct.map (AlgHom.snd A B₁ B₂) (AlgHom.snd A B₁ B₂) x))
      (diagonalAnnihilator A (B₁ × B₂) :
        Set ((B₁ × B₂) ⊗[A] (B₁ × B₂)))
      ((diagonalAnnihilator A B₁ : Set (B₁ ⊗[A] B₁)) ×ˢ
        (diagonalAnnihilator A B₂ : Set (B₂ ⊗[A] B₂)))
```

**`Stacks.Discriminant.noetherDifferent_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Basic.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Basic.lean#L226). The attribute's comment: “part (2)”.

> The Noether different of a product algebra is the product of the Noether differents
> of its factors.

```lean
theorem noetherDifferent_prod
    (A : Type u) (B₁ : Type v) (B₂ : Type w)
    [CommRing A] [CommRing B₁] [CommRing B₂] [Algebra A B₁] [Algebra A B₂] :
    noetherDifferent A (B₁ × B₂) =
      Ideal.prod (noetherDifferent A B₁)
        (noetherDifferent A B₂)
```

## Tag 0BVM, a lemma

[Tag 0BVM](https://stacks.math.columbia.edu/tag/0BVM) in the Stacks Project.

**`Stacks.Discriminant.map_diagonalAnnihilator_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/FlatBaseChange.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/FlatBaseChange.lean#L230). The attribute's comment: “part (1)”.

> The annihilator of the diagonal ideal commutes with flat base change.

```lean
theorem map_diagonalAnnihilator_eq (A : Type u) (B : Type v) (A' : Type w)
    [CommRing A] [CommRing B] [CommRing A'] [Algebra A B] [Algebra A A']
    [Algebra.FiniteType A B] [Module.Flat A A'] :
    (diagonalAnnihilator A B).map (envelopingBaseChange A B A') =
      diagonalAnnihilator A' (A' ⊗[A] B)
```

**`Stacks.Discriminant.map_noetherDifferent_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/FlatBaseChange.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/FlatBaseChange.lean#L281). The attribute's comment: “part (2)”.

> The Noether different commutes with flat base change.

```lean
theorem map_noetherDifferent_eq (A : Type u) (B : Type v) (A' : Type w)
    [CommRing A] [CommRing B] [CommRing A'] [Algebra A B] [Algebra A A']
    [Algebra.FiniteType A B] [Module.Flat A A'] :
    (noetherDifferent A B).map
        (Algebra.TensorProduct.includeRight : B →ₐ[A] A' ⊗[A] B) =
      noetherDifferent A' (A' ⊗[A] B)
```

## Tag 0BVN, a lemma

[Tag 0BVN](https://stacks.math.columbia.edu/tag/0BVN) in the Stacks Project.

**`Stacks.Discriminant.diagonalAnnihilatorBaseChange_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean#L373). The attribute's comment: “part (1), injectivity”.

> The canonical base-change map on diagonal annihilators is injective under the open
> localization hypotheses. This is the injectivity implicit in the identification in part (1).

```lean
theorem diagonalAnnihilatorBaseChange_injective
    [Algebra.FiniteType A B']
    (h : AlgebraicGeometry.IsOpenImmersion
      (AlgebraicGeometry.Spec.map
        (CommRingCat.ofHom (algebraMap B' B).ulift.{max v w, max v w}))) :
    Function.Injective (diagonalAnnihilatorBaseChange A B' B)
```

**`Stacks.Discriminant.range_diagonalAnnihilatorBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean#L391). The attribute's comment: “part (1), image”.

> Under the open localization hypotheses, the image of `B ⊗[B'] J'` under the canonical
> map is exactly the diagonal annihilator `J` for `B/A`.

```lean
theorem range_diagonalAnnihilatorBaseChange
    [Algebra.FiniteType A B']
    (h : AlgebraicGeometry.IsOpenImmersion
      (AlgebraicGeometry.Spec.map
        (CommRingCat.ofHom (algebraMap B' B).ulift.{max v w, max v w}))) :
    LinearMap.range (diagonalAnnihilatorBaseChange A B' B) =
      (diagonalAnnihilator A B).restrictScalars B
```

**`Stacks.Discriminant.noetherDifferent_eq_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Localization.lean#L446). The attribute's comment: “part (2)”.

> Under the open localization hypotheses, the Noether different of `B/A` is the extension
> to `B` of the Noether different of `B'/A`.

```lean
theorem noetherDifferent_eq_map
    [Algebra.FiniteType A B']
    (h : AlgebraicGeometry.IsOpenImmersion
      (AlgebraicGeometry.Spec.map
        (CommRingCat.ofHom (algebraMap B' B).ulift.{max v w, max v w}))) :
    noetherDifferent A B =
      Ideal.map (algebraMap B' B)
        (noetherDifferent A B')
```

## Tag 0BVP, a remark

[Tag 0BVP](https://stacks.math.columbia.edu/tag/0BVP) in the Stacks Project.

**`Stacks.Discriminant.noetherPairingWithFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Pairing.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/Pairing.lean#L476).

> **Stacks Project, Tag 0BVP.** The canonical `B`-bilinear pairing between the relative
> dualizing module and the annihilator of the kernel of multiplication, together with its defining
> contraction formula on a finite-open model.

```lean
noncomputable def noetherPairingWithFormula {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    {p : dualizingModule F →ₗ[B]
      (↑(diagonalAnnihilator A B) →ₗ[B] B) // IsNoetherPairing F p}
```

**`Stacks.Discriminant.noetherPairing_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingNaturality.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingNaturality.lean#L487). The attribute's comment: “independence of factorization”.

> **Stacks Project, Tag 0BVP (independence of factorization).** The canonical pairing between
> the relative dualizing module and the diagonal annihilator does not depend on the finite-open
> factorization: the comparison of dualizing modules of Tag 0BT1 carries one pairing to the
> other.

```lean
theorem noetherPairing_naturality
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B)
    (ω : dualizingModule F) (j : ↑(diagonalAnnihilator A B)) :
    noetherPairing G (dualizingModuleEquiv F G ω) j = noetherPairing F ω j
```

## Tag 0BVR, a lemma

[Tag 0BVR](https://stacks.math.columbia.edu/tag/0BVR) in the Stacks Project.

**`Stacks.Discriminant.noetherPairing_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingFlatBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingFlatBaseChange.lean#L110). The attribute's comment: “flat_base_change”.

> **Stacks Project, Tag 0BVR (flat base change).** The canonical pairing
> between the relative dualizing module and the diagonal annihilator commutes
> with flat base change.

```lean
theorem noetherPairing_baseChange
    {A : Type u} {B : Type v} (A₁ : Type x)
    [CommRing A] [CommRing B] [CommRing A₁]
    [Algebra A B] [Algebra A A₁]
    [Algebra.FiniteType A B] [Module.Flat A A₁]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (ω : dualizingModule F)
    (j : diagonalAnnihilator A B) :
    letI : Algebra B (A₁ ⊗[A] B) := Algebra.TensorProduct.rightAlgebra
    noetherPairing (FiniteOpenFactorization.baseChange F A₁)
        (dualizingModule.baseChange F A₁ ω)
        (diagonalAnnihilatorFlatBaseChange A B A₁ j) =
      algebraMap B (A₁ ⊗[A] B) (noetherPairing F ω j)
```

**`Stacks.Discriminant.noetherPairing_prod_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingProductProjection.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingProductProjection.lean#L335). The attribute's comment: “product_projection”.

> **Stacks Project, Tag 0BVR (product projection).** The canonical pairing between the relative
> dualizing module and the diagonal annihilator commutes with the projection to the first factor of
> a product.

```lean
theorem noetherPairing_prod_fst
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    (ω : dualizingModule F) (j : ↑(diagonalAnnihilator A (B × C))) :
    noetherPairing FB ((dualizingModuleProdEquiv F FB FC ω).1)
        (diagonalAnnihilatorProdFst A B C j) =
      (noetherPairing F ω j).1
```

**`Stacks.Discriminant.noetherPairing_prod_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingProductProjection.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/NoetherPairingProductProjection.lean#L367). The attribute's comment: “product_projection”.

> **Stacks Project, Tag 0BVR (product projection).** The canonical pairing between the relative
> dualizing module and the diagonal annihilator commutes with the projection to the second factor
> of a product.

```lean
theorem noetherPairing_prod_snd
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    (ω : dualizingModule F) (j : ↑(diagonalAnnihilator A (B × C))) :
    noetherPairing FC ((dualizingModuleProdEquiv F FB FC ω).2)
        (diagonalAnnihilatorProdSnd A B C j) =
      (noetherPairing F ω j).2
```

## Tag 0BVS, a lemma

[Tag 0BVS](https://stacks.math.columbia.edu/tag/0BVS) in the Stacks Project.

**`Stacks.Discriminant.noetherPairing_flip_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/PairingBijective.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/PairingBijective.lean#L358).

> **Stacks Project, Tag 0BVS.** For a flat quasi-finite homomorphism of Noetherian rings the
> canonical pairing induces a bijection from the annihilator of the diagonal ideal to the dual of
> the relative dualizing module.

```lean
theorem noetherPairing_flip_bijective
    [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    Function.Bijective (noetherPairing F).flip
```

## Tag 0BVT, a lemma

[Tag 0BVT](https://stacks.math.columbia.edu/tag/0BVT) in the Stacks Project.

**`Stacks.Discriminant.noetherPairingEquiv_apply_traceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/TraceElement.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/TraceElement.lean#L413). The attribute's comment: “commutative diagram”.

> **Stacks Project, Tag 0BVT.** Under the isomorphism induced by the canonical pairing,
> multiplication of an element of the diagonal annihilator is evaluation at the trace
> element.

```lean
theorem noetherPairingEquiv_apply_traceElement
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) (j : ↑(diagonalAnnihilator A B)) :
    noetherPairingEquiv F j (dualizingModule.traceElement F) =
      Algebra.TensorProduct.lmul' A j.1
```

**`Stacks.Discriminant.noetherDifferent_eq_range_traceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/TraceElement.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/TraceElement.lean#L484). The attribute's comment: “image of evaluation”.

> **Stacks Project, Tag 0BVT.** The Noether different is the image of evaluation at the trace
> element.

```lean
theorem noetherDifferent_eq_range_traceElement
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    (noetherDifferent A B : Set B) =
      Set.range fun φ : dualizingModule F →ₗ[B] B ↦
        φ (dualizingModule.traceElement F)
```

## Tag 0BVU, a lemma

[Tag 0BVU](https://stacks.math.columbia.edu/tag/0BVU) in the Stacks Project.

**`Stacks.Discriminant.zeroLocus_noetherDifferent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/UnramifiedLocus.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/NoetherDifferent/UnramifiedLocus.lean#L96).

> The primes containing the Noether different are exactly the primes at
> which a finite type algebra is not unramified.

```lean
theorem zeroLocus_noetherDifferent
    (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    [Algebra A B] [Algebra.FiniteType A B] :
    PrimeSpectrum.zeroLocus (noetherDifferent A B : Set B) =
      (Algebra.unramifiedLocus A B)ᶜ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.6, Tag 0BVK](https://stacks.math.columbia.edu/tag/0BVK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
