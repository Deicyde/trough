---
declaration: section
origin: cited
lean: AlgebraicGeometry.GeometricallyConnected, AlgebraicGeometry.geometricallyConnected_iff_baseChange_fieldExtension, AlgebraicGeometry.pullback_snd_connectedComponentsMap_bijective, AlgebraicGeometry.geometricallyConnected_spec_iff, AlgebraicGeometry.baseChange_connectedComponents_bijective, AlgebraicGeometry.geometricallyConnected_iff_connectedSpace, AlgebraicGeometry.geometricallyConnected_iff_connectedSpace_baseChange, AlgebraicGeometry.exists_fg_subalgebra_descending_isCompact_open
statement: formalized
proof: formalized
---

# 33.7 Geometrically connected schemes

Section 33.7 of the Stacks Project, [Tag 0361](https://stacks.math.columbia.edu/tag/0361). 19 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0362, a definition

[Tag 0362](https://stacks.math.columbia.edu/tag/0362) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.GeometricallyConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.GeometricallyConnected#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch33.lean#L49) (StacksFrontier): “geometrically connected, for a morphism; the tag is the case of `X ⟶ Spec k`”. References: EGA III (4.3.4); EGA IV (4.5.2), “partial”; SGA 1 IX (3.4).

## Tag 054N, a lemma

[Tag 054N](https://stacks.math.columbia.edu/tag/054N) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_iff_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedBaseChange.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedBaseChange.lean#L40).

> **Stacks Project, Tag 054N.** A scheme over a field is geometrically connected if and only if
> its base change along a field extension is geometrically connected.

```lean
public theorem geometricallyConnected_iff_baseChange_fieldExtension
    {X : Scheme.{u}} (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    (f : X ⟶ Spec (.of k)) :
    GeometricallyConnected f ↔
      GeometricallyConnected
        (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))
```

## Tag 0385, a lemma

[Tag 0385](https://stacks.math.columbia.edu/tag/0385) in the Stacks Project.

**`AlgebraicGeometry.pullback_snd_connectedComponentsMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedProductProjection.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedProductProjection.lean#L64).

> **Stacks 0385.** Let `k` be a field and let `X`, `Y` be schemes over `k`, presented by
> their structure maps `f : X ⟶ Spec k` and `g : Y ⟶ Spec k`. If `X` is geometrically connected
> over `k`, then the projection `X ×_k Y ⟶ Y` induces a bijection between the connected components
> of `X ×_k Y` and the connected components of `Y`.

```lean
public theorem pullback_snd_connectedComponentsMap_bijective
    (k : Type u) [Field k] {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [GeometricallyConnected f] :
    Function.Bijective (pullback.snd f g).continuous.connectedComponentsMap
```

## Tag 0386, a lemma

[Tag 0386](https://stacks.math.columbia.edu/tag/0386) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_spec_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedAffine.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedAffine.lean#L34).

> An affine scheme is geometrically connected over a field if and only if its coordinate
> algebra is geometrically connected over that field.

```lean
public theorem geometricallyConnected_spec_iff (k A : Type u) [Field k] [CommRing A]
    [Algebra k A] :
    GeometricallyConnected (Spec.map (ofHom (algebraMap k A))) ↔
      Algebra.IsGeometricallyConnected k A
```

## Tag 0363, a lemma

[Tag 0363](https://stacks.math.columbia.edu/tag/0363) in the Stacks Project.

**`AlgebraicGeometry.baseChange_connectedComponents_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparablyClosed.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparablyClosed.lean#L60). The attribute's comment: “bijection on connected components”. References: EGA III (4.3.4), “special case”; EGA IV (4.4.1), “special case”; EGA IV (4.5.15), “special case”; EGA IV (4.5.21), “more general”; EGA IV (4.5.6), “(i), special case”; SGA 3 VIA (4.1), “special case”.

> **Stacks Project, Tag 0363.** Base change along any extension of a separably closed
> field induces a bijection on the connected components of a scheme.

```lean
public theorem baseChange_connectedComponents_bijective
    (k k' : Type u) [Field k] [IsSepClosed k] [Field k'] [Algebra k k']
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    Function.Bijective
      (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap k k')))).continuous.connectedComponentsMap
```

**`AlgebraicGeometry.geometricallyConnected_iff_connectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparablyClosed.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparablyClosed.lean#L77). The attribute's comment: “geometric connectedness”. References: EGA IV (4.4.4), “more general”; EGA IV (8.4.5), “special case”.

> **Stacks Project, Tag 0363.** Over a separably closed field, a scheme is geometrically
> connected if and only if its underlying topological space is connected.

```lean
public theorem geometricallyConnected_iff_connectedSpace
    (k : Type u) [Field k] [IsSepClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    GeometricallyConnected f ↔ ConnectedSpace X
```

## Tag 0387, a lemma

[Tag 0387](https://stacks.math.columbia.edu/tag/0387) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_iff_connectedSpace_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparableClosure.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedSeparableClosure.lean#L58).

> A scheme over a field is geometrically connected if and only if its base change to a
> separable algebraic closure is connected.

```lean
public theorem geometricallyConnected_iff_connectedSpace_baseChange
    (k : Type u) [Field k] (ksep : Type u) [Field ksep] [Algebra k ksep]
    [IsSepClosure k ksep] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    GeometricallyConnected f ↔
      ConnectedSpace
        (CategoryTheory.Limits.pullback f
          (Spec.map (CommRingCat.ofHom (algebraMap k ksep))) : Scheme.{u})
```

## Tag 0388, a lemma

[Tag 0388](https://stacks.math.columbia.edu/tag/0388) in the Stacks Project.

**`AlgebraicGeometry.exists_fg_subalgebra_descending_isCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpenSubalgebra.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpenSubalgebra.lean#L231). References: EGA IV (8.2.11), “X_A over f.g. subalgs”.

> **[Stacks, Tag 0388].** Let `X` be a scheme over a commutative ring `k` and let `A` be a
> `k`-algebra. A quasi-compact open `V` of the base change `X_A` is the inverse image of a
> quasi-compact open `V'` of `X_{A'}` for some finitely generated `k`-subalgebra `A' ⊆ A`.
>
> The morphism `X_A ⟶ X_{A'}` along which `V'` is pulled back is characterised by its two
> projections: it covers the morphism `Spec A ⟶ Spec A'` induced by the inclusion `A' ⊆ A` and it
> commutes with the projection to `X`.

```lean
public theorem exists_fg_subalgebra_descending_isCompact_open
    {k A : Type u} [CommRing k] [CommRing A] [Algebra k A]
    (X : Scheme.{u}) (f : X ⟶ Spec (CommRingCat.of k))
    (V : (pullback (Spec.map (CommRingCat.ofHom (algebraMap k A))) f).Opens)
    (hV : IsCompact V.1) :
    ∃ (A' : Subalgebra k A) (_ : A'.FG)
      (V' : (pullback (Spec.map (CommRingCat.ofHom (algebraMap k A'))) f).Opens),
      IsCompact V'.1 ∧
        ∃ p : pullback (Spec.map (CommRingCat.ofHom (algebraMap k A))) f ⟶
              pullback (Spec.map (CommRingCat.ofHom (algebraMap k A'))) f,
          p ≫ pullback.fst (Spec.map (CommRingCat.ofHom (algebraMap k A'))) f =
              pullback.fst (Spec.map (CommRingCat.ofHom (algebraMap k A))) f ≫
                Spec.map (CommRingCat.ofHom (Subalgebra.val A').toRingHom) ∧
            p ≫ pullback.snd (Spec.map (CommRingCat.ofHom (algebraMap k A'))) f =
              pullback.snd (Spec.map (CommRingCat.ofHom (algebraMap k A))) f ∧
            V = p ⁻¹ᵁ V'
```

## Tag 038A, an equation

[Tag 038A](https://stacks.math.columbia.edu/tag/038A) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.galoisActionOnBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisAction.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisAction.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/IrreducibleGaloisAction.lean#L128) (StacksFrontier): “For a Galois extension `kbar/k` the group `kbar ≃ₐ[k] kbar` is `Gal(kbar/k)`, and `galoisActionOnBaseChange` is the canonical action of its opposite group on `X_kbar`, induced by the automorphisms `Spec σ` of `Spec kbar` through the defining fibre product. The opposite group appears because `Spec σ ≫ Spec τ = Spec (τ ∘ σ)`.”.

## Tag 04KU, a lemma

[Tag 04KU](https://stacks.math.columbia.edu/tag/04KU) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_subextension_descending_isCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpen.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpen.lean#L407). The attribute's comment: “part (1)”.

> A quasi-compact open in the base change of a scheme to an algebraic extension is pulled back
> from a quasi-compact open after a finite intermediate extension.

```lean
public theorem exists_finite_subextension_descending_isCompact_open
    {k K : Type u} [Field k] [Field K] [Algebra k K] [Algebra.IsAlgebraic k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (CommRingCat.of k))
    (V : (pullback f (spectrumMap k K)).Opens) (hV : IsCompact V.1) :
    ∃ (E : IntermediateField k K) (_ : FiniteDimensional k E)
      (V' : (pullback f (spectrumMap k E)).Opens),
      IsCompact V'.1 ∧
        ∃ p : pullback f (spectrumMap k K) ⟶ pullback f (spectrumMap k E),
          p ≫ pullback.fst f (spectrumMap k E) = pullback.fst f (spectrumMap k K) ∧
          p ≫ pullback.snd f (spectrumMap k E) =
            pullback.snd f (spectrumMap k K) ≫ Spec.map (CommRingCat.ofHom E.val) ∧
          V = p ⁻¹ᵁ V'
```

**`AlgebraicGeometry.exists_open_subgroup_fixing_isCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpen.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/QuasiCompactOpen.lean#L483). The attribute's comment: “part (2)”.

> A quasi-compact open in the base change of a scheme to a Galois extension is fixed by an open
> subgroup of the Galois group.

```lean
public theorem exists_open_subgroup_fixing_isCompact_open
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsGalois k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (CommRingCat.of k))
    (V : (pullback f (spectrumMap k K)).Opens) (hV : IsCompact V.1) :
    ∃ H : Subgroup Gal(K/k), IsOpen (H : Set Gal(K/k)) ∧
      ∀ σ : Gal(K/k), σ ∈ H →
        ∃ a : pullback f (spectrumMap k K) ≅ pullback f (spectrumMap k K),
          a.hom ≫ pullback.fst f (spectrumMap k K) = pullback.fst f (spectrumMap k K) ∧
          a.hom ≫ pullback.snd f (spectrumMap k K) =
            pullback.snd f (spectrumMap k K) ≫
              Spec.map (CommRingCat.ofHom σ.toRingEquiv.toRingHom) ∧
      V = a.hom ⁻¹ᵁ V
```

## Tag 038B, a lemma

[Tag 038B](https://stacks.math.columbia.edu/tag/038B) in the Stacks Project.

**`AlgebraicGeometry.exists_closed_subset_with_preimage_eq_of_galois_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/GaloisInvariantClosed.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/GaloisInvariantClosed.lean#L511).

> **Stacks Project, Tag 038B.** A closed subset of a scheme after base change by a
> Galois field extension descends if it is invariant under the Galois group.

```lean
public theorem exists_closed_subset_with_preimage_eq_of_galois_invariant
    (k K : Type u) [Field k] [Field K] [Algebra k K] [IsGalois k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (Tbar : Set (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme))
    (hTbar : IsClosed Tbar)
    (hstable : ∀ σ : K ≃ₐ[k] K,
      (galoisBaseChangeMap k K X f σ) ⁻¹' Tbar = Tbar) :
    ∃ T : Set X, IsClosed T ∧
      (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ⁻¹' T = Tbar
```

## Tag 0389, a lemma

[Tag 0389](https://stacks.math.columbia.edu/tag/0389) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_iff_forall_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedFiniteSeparable.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedFiniteSeparable.lean#L193). References: EGA IV (8.4.5), “more general”; EGA IV (4.5.17), “more general”.

> A scheme over a field is geometrically connected if and only if its base change to every
> finite separable extension is connected.

```lean
public theorem geometricallyConnected_iff_forall_finite_separable
    {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) :
    GeometricallyConnected f ↔
      ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
        [Algebra.IsSeparable k k'],
        ConnectedSpace ↥(pullback f
          (Spec.map (CommRingCat.ofHom (algebraMap k k'))))
```

## Tag 038C, a lemma

[Tag 038C](https://stacks.math.columbia.edu/tag/038C) in the Stacks Project.

**`AlgebraicGeometry.not_connectedSpace_of_galois_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGalois.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGalois.lean#L117).

> Let `kbar/k` be a possibly infinite Galois extension and let `T → X` be a morphism of
> schemes over `k`. If `T_kbar` is connected and `X_kbar` is disconnected, then `X` is
> disconnected.

```lean
public theorem not_connectedSpace_of_galois_baseChange
    (k kbar : Type u) [Field k] [Field kbar] [Algebra k kbar] [IsGalois k kbar]
    {T X : Scheme.{u}} (f : T ⟶ X) (p : X ⟶ Spec (.of k))
    (hT : ConnectedSpace
      ((pullback (f ≫ p) (Spec.map <| ofHom <| algebraMap k kbar)) : Scheme.{u}))
    (hX : ¬ ConnectedSpace
      ((pullback p (Spec.map <| ofHom <| algebraMap k kbar)) : Scheme.{u})) :
    ¬ ConnectedSpace X
```

## Tag 056R, a lemma

[Tag 056R](https://stacks.math.columbia.edu/tag/056R) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_of_comp_of_connectedSpace`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedCriterion.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedCriterion.lean#L41).

> If a connected scheme over a field admits a morphism over that field from a geometrically
> connected scheme, then it is geometrically connected.

```lean
public lemma geometricallyConnected_of_comp_of_connectedSpace
    (k : Type u) [Field k] {T X : Scheme.{u}} (f : T ⟶ X)
    (p : X ⟶ Spec (.of k)) [GeometricallyConnected (f ≫ p)] [ConnectedSpace X] :
    GeometricallyConnected p
```

## Tag 04KV, a lemma

[Tag 04KV](https://stacks.math.columbia.edu/tag/04KV) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_of_connectedSpace_of_algebraicClosure_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedPoint.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedPoint.lean#L47). The attribute's comment: “point with algebraically closed base field”.

> **Stacks Project, Tag 04KV.** A connected scheme over a field is geometrically
> connected if the field is algebraically closed in the residue field of one of
> its points.

```lean
public theorem geometricallyConnected_of_connectedSpace_of_algebraicClosure_eq_bot
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [ConnectedSpace X] (x : X)
    (h : let : (f x).asIdeal.IsPrime := (f x).isPrime
      let := ((CommRingCat.ofHom (algebraMap k (f x).asIdeal.ResidueField)) ≫
        (Scheme.Spec.residueFieldIso (.of k) (f x)).inv ≫
        f.residueFieldMap x).hom.toAlgebra
      IsAlgClosedIn k (X.residueField x)) :
    GeometricallyConnected f
```

**`AlgebraicGeometry.geometricallyConnected_of_connectedSpace_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedPoint.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedPoint.lean#L100). The attribute's comment: “rational-point consequence”. References: SGA 3 VIA (2.1.2), “Y = Spec of field ext”.

> **Stacks Project, Tag 04KV, rational-point consequence.** A connected scheme
> over a field with a rational point is geometrically connected.

```lean
public theorem geometricallyConnected_of_connectedSpace_of_section
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [ConnectedSpace X] (s : Spec (.of k) ⟶ X) (hs : s ≫ f = 𝟙 _) :
    GeometricallyConnected f
```

## Tag 04PY, a lemma

[Tag 04PY](https://stacks.math.columbia.edu/tag/04PY) in the Stacks Project.

Declarations registered for the tag:

- [`Continuous.preimage_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.preimage_connectedComponent#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch33.lean#L46) (StacksFrontier): “for the continuous map X_K → X; stated for any continuous map”.

## Tag 07VM, a lemma

[Tag 07VM](https://stacks.math.columbia.edu/tag/07VM) in the Stacks Project.

**`AlgebraicGeometry.baseChange_image_connectedComponent_eq_connectedComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedComponentsFiniteExtension.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedComponentsFiniteExtension.lean#L98). References: EGA IV (4.4.1), “partial, special case”; SGA 3 VIA (2.4.1), “partial”.

> **Stacks Project, Tag 07VM.** Let `K/k` be a finite extension of fields and let `X` be a
> scheme over `k`. The projection `X_K → X` sends every connected component of `X_K` onto a
> connected component of `X`.

```lean
public theorem baseChange_image_connectedComponent_eq_connectedComponent
    {X : Scheme.{u}} (k K : Type u) [Field k] [Field K] [Algebra k K] [FiniteDimensional k K]
    (f : X ⟶ Spec (.of k))
    (t : ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base ''
        connectedComponent t =
      connectedComponent
        ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base t)
```

## Tag 04PZ, a lemma

[Tag 04PZ](https://stacks.math.columbia.edu/tag/04PZ) in the Stacks Project.

**`AlgebraicGeometry.image_connectedComponent_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedComponentsFieldExtension.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedComponentsFieldExtension.lean#L443). References: EGA IV (4.4.1), “partial”; SGA 3 VIA (2.4.1), “partial”; SGA 3 VIB (1.4.1), “partial”.

> **Stacks Project, Tag 04PZ** (Gabber). Let `K/k` be an extension of fields -- not assumed
> finite, algebraic or separable -- and let `X` be a scheme over `k`. The projection `X_K ⟶ X`
> sends every connected component of `X_K` onto a connected component of `X`: the image of the
> connected component of a point `x` is the connected component of its image.

```lean
theorem image_connectedComponent_baseChange
    {X : Scheme.{u}} (k K : Type u) [Field k] [Field K] [Algebra k K]
    (f : X ⟶ Spec (.of k))
    (x : ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base ''
        connectedComponent x =
      connectedComponent
        ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base x)
```

## Tag 038D, a lemma

[Tag 038D](https://stacks.math.columbia.edu/tag/038D) in the Stacks Project.

**`AlgebraicGeometry.galoisActionOnGeometricConnectedComponents`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean#L95). The attribute's comment: “galois_action_on_geometric_connected_components”.

> The canonical action of the opposite Galois group on the connected components of a scheme
> after base change. A component is sent to its image under the corresponding automorphism of the
> base-changed scheme.

```lean
public noncomputable def galoisActionOnGeometricConnectedComponents
    (X : Over (Spec (.of R))) :
    Action (Type u) (MulOpposite (S ≃ₐ[R] S))
```

**`AlgebraicGeometry.galoisActionOnGeometricConnectedComponents_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean#L175). The attribute's comment: “base_extension_compatibility”.

> Restriction of Galois automorphisms commutes with the canonical map on the connected
> components of the two geometric base changes.

```lean
public theorem galoisActionOnGeometricConnectedComponents_baseChange
    (k' : Type u) [Field k'] [Algebra k k'] [Algebra k' kbar']
    [IsScalarTower k k' kbar'] [Normal k kbar]
    (p : pullback X.hom (spectrumMap k kbar') ⟶ pullback X.hom (spectrumMap k kbar))
    (hp₁ : p ≫ pullback.fst X.hom (spectrumMap k kbar) =
      pullback.fst X.hom (spectrumMap k kbar'))
    (hp₂ : p ≫ pullback.snd X.hom (spectrumMap k kbar) =
      pullback.snd X.hom (spectrumMap k kbar') ≫
        Spec.map (CommRingCat.ofHom (algebraMap kbar kbar')))
    (σ : kbar' ≃ₐ[k'] kbar')
    (C : ConnectedComponents (galoisActionOnBaseChange k kbar' X).V) :
    p.continuous.connectedComponentsMap
        (ConcreteCategory.hom
          ((galoisActionOnGeometricConnectedComponents k kbar' X).ρ
            (MulOpposite.op (σ.restrictScalars k))).asHom C) =
      ConcreteCategory.hom
        ((galoisActionOnGeometricConnectedComponents k kbar X).ρ
          (MulOpposite.op ((σ.restrictScalars k).restrictNormal kbar))).asHom
        (p.continuous.connectedComponentsMap C)
```

**`AlgebraicGeometry.baseChangeComparison_connectedComponents_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisAction.lean#L222). The attribute's comment: “base_extension_compatibility”.

> The canonical base-extension map is bijective on geometric connected components.

```lean
public theorem baseChangeComparison_connectedComponents_bijective
    [IsSepClosed kbar]
    (p : pullback X.hom (spectrumMap k kbar') ⟶ pullback X.hom (spectrumMap k kbar))
    (hp₁ : p ≫ pullback.fst X.hom (spectrumMap k kbar) =
      pullback.fst X.hom (spectrumMap k kbar'))
    (hp₂ : p ≫ pullback.snd X.hom (spectrumMap k kbar) =
      pullback.snd X.hom (spectrumMap k kbar') ≫
        Spec.map (CommRingCat.ofHom (algebraMap kbar kbar'))) :
    Function.Bijective p.continuous.connectedComponentsMap
```

**`AlgebraicGeometry.galoisActionOnGeometricConnectedComponents_fixed_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisFixed.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisFixed.lean#L318). The attribute's comment: “fixed_components”.

> **Stacks Project, Tag 038D.** A connected component of the base change of `X` to a separable
> algebraic closure `kbar` of `k` is fixed by the Galois action if and only if it is the inverse
> image of a connected component of `X` which is geometrically connected over `k`.

```lean
public theorem galoisActionOnGeometricConnectedComponents_fixed_iff
    (k kbar : Type u) [Field k] [Field kbar] [Algebra k kbar] [IsSepClosure k kbar]
    (X : Over (Spec (.of k)))
    (C : ConnectedComponents (galoisActionOnBaseChange k kbar X).V) :
    (∀ σ : MulOpposite (kbar ≃ₐ[k] kbar),
        ConcreteCategory.hom
          ((galoisActionOnGeometricConnectedComponents k kbar X).ρ σ).asHom C = C) ↔
      ∃ T : Set X.left, (∃ x : X.left, T = connectedComponent x) ∧
        IsGeometricallyConnectedSubset X.hom T ∧
        ⇑(pullback.fst X.hom (spectrumMap k kbar)) ⁻¹' T =
          ConnectedComponents.mk ⁻¹' {C}
```

## Tag 038E, a lemma

[Tag 038E](https://stacks.math.columbia.edu/tag/038E) in the Stacks Project.

**`AlgebraicGeometry.finite_geometricConnectedComponents_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean#L100). The attribute's comment: “part (a)”.

> Open connected components of the geometric base change of a quasi-compact scheme are
> finite in number.

```lean
public theorem finite_geometricConnectedComponents_of_isOpen
    [CompactSpace X.left]
    (hopen : ∀ x : (galoisActionOnBaseChange k ksep X).V,
      IsOpen (connectedComponent x)) :
    Finite (ConnectedComponents (galoisActionOnBaseChange k ksep X).V)
```

**`AlgebraicGeometry.continuous_galoisActionOnGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean#L113). The attribute's comment: “part (b)”.

> The absolute Galois action on open geometric connected components of a quasi-compact
> scheme is continuous for the Krull topology.

```lean
public theorem continuous_galoisActionOnGeometricConnectedComponents
    [CompactSpace X.left]
    (hopen : ∀ x : (galoisActionOnBaseChange k ksep X).V,
      IsOpen (connectedComponent x)) :
    let : TopologicalSpace (galoisActionOnGeometricConnectedComponents k ksep X).V :=
      (inferInstance : TopologicalSpace
        (ConnectedComponents (galoisActionOnBaseChange k ksep X).V))
    Continuous (fun p : MulOpposite (ksep ≃ₐ[k] ksep) ×
        ConnectedComponents (galoisActionOnBaseChange k ksep X).V =>
      ConcreteCategory.hom
        ((galoisActionOnGeometricConnectedComponents k ksep X).ρ p.1).asHom p.2)
```

**`AlgebraicGeometry.isOpen_geometricConnectedComponent_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean#L168). The attribute's comment: “finite type implies assumption (2)”.

> The geometric connected components of a scheme of finite type over a field are open.

```lean
public theorem isOpen_geometricConnectedComponent_of_finiteType
    [LocallyOfFiniteType X.hom] [QuasiCompact X.hom]
    (x : (galoisActionOnBaseChange k ksep X).V) :
    IsOpen (connectedComponent x)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ConnectedGaloisContinuity.lean#L50) (StacksFrontier): “finite type implies assumption (1)”. References: SGA 3 VIB (10.1), “Y is quasi-compact”; SGA 4 VI (1.14), “(i), special case”; SGA 4 VIII (5.1), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.7, Tag 0361](https://stacks.math.columbia.edu/tag/0361)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
