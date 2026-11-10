---
declaration: section
origin: cited
lean: Stacks.Duality.preservesCoproducts_rightAdjoint_of_isCompactObject_pushforward, Stacks.Duality.preservesCoproducts_twistedInverseImage_of_isCompactObject_pushforward, Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward, Stacks.Duality.preservesColimitsOfShape_twistedInverseImage, Stacks.Duality.preservesCoproducts_twistedInverseImage_of_perfect_proper, Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_perfect, Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect, Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_perfect
statement: formalized
proof: formalized
---

# 48.13 Right adjoint of pushforward for perfect proper morphisms

Section 48.13 of the Stacks Project, [Tag 0AA9](https://stacks.math.columbia.edu/tag/0AA9). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A9R, a lemma

[Tag 0A9R](https://stacks.math.columbia.edu/tag/0A9R) in the Stacks Project.

**`Stacks.Duality.preservesCoproducts_rightAdjoint_of_isCompactObject_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSums.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSums.lean#L167). The attribute's comment: “a commutes with direct sums: for every right adjoint a of the restricted Rf_* and every index type in Type u, a preserves coproducts of that shape. The source's hypotheses on f — perfect, proper, Noetherian source and target — are not binders here; they enter its proof only to make Rf_*E perfect, hence compact, and that is the hypothesis hpushE. Carried: hpushE, compactness of Rf_*E, which is Tag 0B6G (Rf_* of a perfect complex along a perfect proper morphism is perfect) together with Tag 09M1 (compact iff perfect in D_QCoh) — both in this tree, at StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/ProperDirectImage.lean and StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfect.lean; 09M1 is unconditional in the affine case, but 0B6G is still conditional there, on Tag 02O5 and on the Tor-dimension half of Tag 08EV, which is why hpushE is carried; E, hEc, hE, a compact weak generator of D_QCoh(O_X), Tag 09IS, unproved in this repository and carried in this shape by every consumer here; hpush, quasi-coherence of the cohomology of Rf_*, Tag 08D5; and adj, the existence of the right adjoint, Tag 0A9E, which this repository proves only conditionally in Stacks.Duality.isLeftAdjoint_quasiCoherentDerivedPushforward. No PreservesColimitsOfShape instance for a, or for any functor out of D_QCoh(O_Y), is assumed”.

> **[Stacks, Tag 0A9R].** Let `f : X ⟶ Y` be a morphism of schemes along which derived direct
> image preserves quasi-coherence of cohomology, and let `a` be a right adjoint of the restriction
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Suppose `D_QCoh(𝒪_X)` has a compact weak generator `E`
> whose image `Rf_*E` is compact in `D_QCoh(𝒪_Y)`. Then `a` commutes with direct sums.
>
> In the source `E` is the perfect generator of [Stacks, Tag 09IS] and compactness of `Rf_*E` is
> [Stacks, Tag 0B6G] together with [Stacks, Tag 09M1]; those are the only places the source's
> hypotheses on `f` — perfect, proper, Noetherian — are used, and they appear here only through
> `hpushE`. The formal half of the argument is
> `CategoryTheory.Pretriangulated.preservesCoproducts_of_isCompactObject_map`, read with `Rf_*` as
> the left adjoint and `a` as the right one.

```lean
theorem preservesCoproducts_rightAdjoint_of_isCompactObject_pushforward
    {a : quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X}
    (adj : quasiCoherentDerivedPushforward f hpush ⊣ a)
    (E : quasiCoherentDerivedCategory X) (hEc : IsCompactObject.{u} E)
    (hE : (ObjectProperty.singleton E).IsWeakTriangulatedGenerator)
    (hpushE : IsCompactObject.{u} ((quasiCoherentDerivedPushforward f hpush).obj E)) :
    ∀ J : Type u, PreservesColimitsOfShape (Discrete J) a
```

**`Stacks.Duality.preservesCoproducts_twistedInverseImage_of_isCompactObject_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSums.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSums.lean#L191). The attribute's comment: “the same conclusion at the source's own right adjoint, Stacks.Duality.twistedInverseImage, the f^× of Tag 0A9E. Carries everything Stacks.Duality.preservesCoproducts_rightAdjoint_of_isCompactObject_pushforward carries — hpushE, which is Tag 0B6G with Tag 09M1, neither of them available to this file; E, hEc, hE, the compact weak generator of Tag 09IS; hpush, Tag 08D5 — with the existence of the right adjoint now the instance binder Functor.IsLeftAdjoint rather than an adjunction argument, that binder being Tag 0A9E”.

> **[Stacks, Tag 0A9R] at the source's own right adjoint.** When the restricted derived direct
> image is a left adjoint, `Stacks.Duality.twistedInverseImage` is the right adjoint `a` of
> [Stacks, Tag 0A9E] that Lemma 48.13.1 of the source speaks about, and it commutes with direct
> sums under the same hypotheses as
> `Stacks.Duality.preservesCoproducts_rightAdjoint_of_isCompactObject_pushforward`.

```lean
theorem preservesCoproducts_twistedInverseImage_of_isCompactObject_pushforward
    [(quasiCoherentDerivedPushforward f hpush).IsLeftAdjoint]
    (E : quasiCoherentDerivedCategory X) (hEc : IsCompactObject.{u} E)
    (hE : (ObjectProperty.singleton E).IsWeakTriangulatedGenerator)
    (hpushE : IsCompactObject.{u} ((quasiCoherentDerivedPushforward f hpush).obj E)) :
    ∀ J : Type u, PreservesColimitsOfShape (Discrete J) (twistedInverseImage f hpush)
```

**`Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean#L111).

> Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and let `a` be a right
> adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then `a` commutes with direct sums.

```lean
theorem preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward [IsNoetherian X]
    [IsNoetherian Y] [Perfect f] [IsProper f]
    {a : quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X}
    (adj : quasiCoherentDerivedPushforward f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⊣ a) (J : Type u) :
    PreservesColimitsOfShape (Discrete J) a
```

**`Stacks.Duality.preservesColimitsOfShape_twistedInverseImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean#L123).

> For a perfect proper morphism of Noetherian schemes `f : X ⟶ Y`, the twisted inverse image
> `f^× : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)`, the right adjoint `twistedInverseImage f` of `Rf_*`, commutes
> with direct sums.

```lean
instance preservesColimitsOfShape_twistedInverseImage [IsNoetherian X] [IsNoetherian Y]
    [Perfect f] [IsProper f] (J : Type u) :
    PreservesColimitsOfShape (Discrete J)
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
```

**`Stacks.Duality.preservesCoproducts_twistedInverseImage_of_perfect_proper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsUnconditional.lean#L70).

> **[Stacks, Tag 0A9R].** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes.
> The twisted inverse image `a = f^×`, the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` ([Stacks, Tag 0A9E]), commutes with direct sums.

```lean
theorem preservesCoproducts_twistedInverseImage_of_perfect_proper (J : Type u) :
    PreservesColimitsOfShape (Discrete J)
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
```

## Tag 0AAA, a lemma

[Tag 0AAA](https://stacks.math.columbia.edu/tag/0AAA) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L69). The attribute's comment: “(2) variant: for a supplied cartesian square with open immersion `j`; the tag is `isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`”.

> **[Stacks, Tag 0AAA] (2), for a supplied cartesian square.** Let `f : X ⟶ Y` be a perfect
> proper morphism of Noetherian schemes and `j : V ⟶ Y` an open immersion, with base change
> `j' : U ⟶ X` and `f' : U ⟶ V`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of [Stacks, Tag 0A9L] is an
> isomorphism at every `K ∈ D_QCoh(𝒪_Y)`. The invertibility of `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` that
> the map contains is the open-immersion case of [Stacks, Tag 0A9K],
> `Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion`. The tag, for
> every open `V ⊆ Y`, is `Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`.

```lean
theorem isIso_twistedInverseImageRestrictionMap_app_of_perfect (sq : IsPullback j' f' f j)
    (K : quasiCoherentDerivedCategory Y) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : IsProper f' := MorphismProperty.of_isPullback sq inferInstance
    haveI := isNoetherian_of_isOpenImmersion j
    haveI := isNoetherian_of_isProper f'
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j) sq
    IsIso ((twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j')
      sq).app K)
```

**`Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L101). The attribute's comment: “(2)”.

> **[Stacks, Tag 0AAA] (2).** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian
> schemes and `V ⊆ Y` an open, with `U = f⁻¹(V)`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of
> [Stacks, Tag 0A9L], `Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap`, is an
> isomorphism at every `K ∈ D_QCoh(𝒪_Y)`. The schemes `X`, `Y` are quasi-compact and
> quasi-separated and `V` is quasi-compact because they are Noetherian.

```lean
theorem isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect (V : Y.Opens)
    (K : quasiCoherentDerivedCategory Y) :
    haveI := isNoetherian_of_isOpenImmersion V.ι
    IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K)
```

**`Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L149). The attribute's comment: “(1)”.

> **[Stacks, Tag 0AAA] (1).** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian
> schemes, with `a` the right adjoint of `Rf_*` on `D_QCoh`. For every closed `T ⊆ Y`, if
> `Q ∈ D_QCoh(𝒪_Y)` is supported on `T` then `a(Q)` is supported on `f⁻¹(T)`. Here `T` is the
> complement of the open `W`, and "supported on `T`" is "restricts to zero on `W`". The functor `a`
> exists by [Stacks, Tag 0A9E],
> `Stacks.Duality.DerivedPushforward.isLeftAdjoint_quasiCoherentDerivedPushforward_of_qcqs`.

```lean
theorem isZero_derivedRestrict_twistedInverseImage_of_perfect (W : Y.Opens)
    (Q : quasiCoherentDerivedCategory Y) (hQ : IsZero ((derivedRestrict W.ι).obj Q.obj)) :
    haveI := DerivedPushforward.isLeftAdjoint_quasiCoherentDerivedPushforward_of_qcqs f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    IsZero ((derivedRestrict (f ⁻¹ᵁ W).ι).obj
      ((twistedInverseImage f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj Q).obj)
```

## Tag 0A9U, a lemma

[Tag 0A9U](https://stacks.math.columbia.edu/tag/0A9U) in the Stacks Project.

**`Stacks.Duality.isIso_compareWithPullbackTensor_of_isIso_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonGeneral.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonGeneral.lean#L227). The attribute's comment: “the two-variable comparison map for an arbitrary object of D_QCoh(O_Y), by dévissage along a compact generating family. Carried: `hgen`, the perfect case Stacks 0A9T, asked for only at the generators — held by `Stacks.Duality.isIso_compareWithPullbackTensor_of_isPerfect` of StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfect.lean; `E`, `hEc`, `hE`, the compact generation of D_QCoh(O_Y) by a perfect object, Stacks 09IS, unproved in this repository and carried the same way by every other consumer here; the instance binder `PreservesColimitsOfShape (Discrete J) (quasiCoherentDerivedTensorRight Y L ⋙ a)`, which is Stacks 0A9R, the commutation of `a` with direct sums, unproved in this repository; the instance binders `Functor.CommShift`, `Functor.IsTriangulated` and `NatTrans.CommShift` for the two sides and for the comparison map, the triangulated structure PullbackComparison.lean records as unavailable for this repository's derived tensor product; and, inherited from `Stacks.Duality.compareWithPullbackTensor`, the oplax monoidality `α` of derived pullback and the invertibility of the projection formula, Stacks 08EU”.

> **[Stacks, Tag 0A9U].** Let `f : X ⟶ Y` be a morphism of schemes, let `a` be a right adjoint
> of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, and let `L ∈ D_QCoh(𝒪_Y)`. Suppose `D_QCoh(𝒪_Y)` is
> generated by a family `E` of compact objects, suppose both sides of the two-variable comparison
> map of [Stacks, Tag 0A9S] are exact and commute with direct sums as functors of `K`, suppose the
> comparison map commutes with the shift, and suppose it is invertible at each `E i`. Then it is
> invertible at *every* `K ∈ D_QCoh(𝒪_Y)`.
>
> This is the source's Lemma 48.13.3. The hypothesis `hgen` is [Stacks, Tag 0A9T], the perfect
> case, asked for only at the generators; `E`, `hEc` and `hE` are the compact generation of
> [Stacks, Tag 09IS]; the direct-sum preservation of `quasiCoherentDerivedTensorRight Y L ⋙ a` is
> [Stacks, Tag 0A9R], that `a` commutes with direct sums. The dévissage is
> `StacksDraft.CompactDevissage.isIso_app_of_isCompactlyGenerated`.

```lean
theorem isIso_compareWithPullbackTensor_of_isIso_generators {ι : Type u}
    (E : ι → quasiCoherentDerivedCategory Y) (hEc : ∀ i, IsCompactObject.{u} (E i))
    (hE : ∀ Z : quasiCoherentDerivedCategory Y,
      ((ofObj E).shiftClosure ℤ).rightOrthogonal Z → IsZero Z)
    (hgen : ∀ i, IsIso (compareWithPullbackTensor f hpush α adj (E i) L))
    (K : quasiCoherentDerivedCategory Y) :
    IsIso (compareWithPullbackTensor f hpush α adj K L)
```

**`Stacks.Duality.isIso_compareWithPullback_of_isIso_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonGeneral.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonGeneral.lean#L297). The attribute's comment: “the structure-sheaf specialization, the map the source displays. Carried: everything `Stacks.Duality.isIso_compareWithPullbackTensor_of_isIso_generators` carries, at `L = 𝒪_Y` — `hgen`, the perfect case Stacks 0A9T held by `Stacks.Duality.isIso_compareWithPullbackTensor_of_isPerfect` of StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfect.lean; `E`, `hEc`, `hE`, compact generation, Stacks 09IS; the direct-sum preservation of `quasiCoherentDerivedTensorRight Y (derivedStructureSheaf Y) ⋙ a`, which is Stacks 0A9R; the `CommShift`/`IsTriangulated`/`NatTrans.CommShift` binders; `α` and Stacks 08EU — and in addition the right unitor of the derived tensor product as the hypothesis `ρ`, which `Stacks.Duality.compareWithPullback` already carries because this repository's derived tensor product has no unit”.

> **[Stacks, Tag 0A9U], the map the source displays.** Equation 48.8.0.1 of
> [Stacks, Tag 0A9S], the map `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)`, is an isomorphism for every
> `K ∈ D_QCoh(𝒪_Y)`: it is the two-variable comparison map at `L = 𝒪_Y`, which is an isomorphism by
> `Stacks.Duality.isIso_compareWithPullbackTensor_of_isIso_generators`, followed by `a` applied to
> the right unitor `K ⊗ᴸ_{𝒪_Y} 𝒪_Y ≅ K`.

```lean
theorem isIso_compareWithPullback_of_isIso_generators {ι : Type u}
    (E : ι → quasiCoherentDerivedCategory Y) (hEc : ∀ i, IsCompactObject.{u} (E i))
    (hE : ∀ Z : quasiCoherentDerivedCategory Y,
      ((ofObj E).shiftClosure ℤ).rightOrthogonal Z → IsZero Z)
    (hgen : ∀ i, IsIso (compareWithPullbackTensor f hpush α adj (E i)
      (derivedStructureSheaf Y)))
    (K : quasiCoherentDerivedCategory Y) :
    IsIso (compareWithPullback f hpush α adj ρ K)
```

**`Stacks.Duality.isIso_twistedInverseImageCompareWithPullback_of_perfect_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectProper.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectProper.lean#L62).

> **Stacks Project, Tag 0A9U (Lemma 48.13.3).** Let `f : X ⟶ Y` be a perfect proper morphism of
> Noetherian schemes. The map `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)` of [Stacks, Tag 0A9S] is an
> isomorphism for every object `K` of `D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageCompareWithPullback_of_perfect_of_isProper
    (K : quasiCoherentDerivedCategory Y) :
    IsIso (twistedInverseImageCompareWithPullback f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (quasiCoherentDerivedPullbackTensorIso f).hom
      (quasiCoherentDerivedTensorRightUnitor Y) K)
```

**`Stacks.Duality.isIso_compareWithPullback_twistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonUnconditional.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonUnconditional.lean#L204).

> Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and
> let `a = f^×` be the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` ([Stacks, Tag 0A9E]).
> The map `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)` of Equation 48.8.0.1 ([Stacks, Tag 0A9S]) is an
> isomorphism for every object `K` of `D_QCoh(𝒪_Y)`.
>
> The same holds at any right adjoint of `Rf_*`, by
> `Stacks.Duality.isIso_compareWithPullback_of_perfect_of_isProper`.

```lean
theorem isIso_compareWithPullback_twistedInverseImage [IsNoetherian X] [IsNoetherian Y]
    [IsProper f] [AlgebraicGeometry.Perfect f] (K : quasiCoherentDerivedCategory Y) :
    IsIso (compareWithPullback f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (pullbackCotensorator f)
      (twistedInverseImageAdjunction f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
      quasiCoherentRightUnitor K)
```

## Tag 0BZG, a lemma

[Tag 0BZG](https://stacks.math.columbia.edu/tag/0BZG) in the Stacks Project.

**`Stacks.Duality.isIso_torIndependentTwistedInverseImageBaseChange_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/PerfectBaseChange.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/PerfectBaseChange.lean#L157).

> **[Stacks, Tag 0BZG].** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and
> `g : Y' ⟶ Y` a morphism with `Y'` Noetherian, and let `X' = X ×_Y Y'`, with projections
> `g' : X' ⟶ X` and `f' : X' ⟶ Y'`. If `X` and `Y'` are Tor independent over `Y`, then the base
> change map `L(g')^* a(K) ⟶ a'(Lg^*K)` of [Stacks, Tag 0AA6] is an isomorphism for every
> `K ∈ D_QCoh(𝒪_Y)`, where `a` and `a'` are the right adjoints of `Rf_*` and `Rf'_*` on `D_QCoh`
> ([Stacks, Tag 0A9E]).

```lean
theorem isIso_torIndependentTwistedInverseImageBaseChange_app_of_perfect {X' X Y' Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y] [IsNoetherian Y'] {g' : X' ⟶ X} {f' : X' ⟶ Y'}
    {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g) [IsProper f]
    [AlgebraicGeometry.Perfect f] (hTor : TorIndependent f g)
    (K : quasiCoherentDerivedCategory Y) :
    haveI : QuasiCompact f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : QuasiSeparated f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
    haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
    IsIso ((torIndependentTwistedInverseImageBaseChange sq hTor).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.13, Tag 0AA9](https://stacks.math.columbia.edu/tag/0AA9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
