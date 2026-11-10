---
declaration: section
origin: cited
lean: Stacks.Cohomology.PerfectComplexes.IsPerfectComplex, Stacks.Cohomology.PerfectComplexes.IsPerfect, AlgebraicGeometry.RingedSpace.isPerfect_of_strictlyPerfect_local_models, AlgebraicGeometry.RingedSpace.isPerfectComplex_of_isPerfect_representation, AlgebraicGeometry.RingedSpace.isPerfect_iff_hasFiniteLocallyFreeRepresentation, AlgebraicGeometry.RingedSpace.hasFiniteLocallyFreeRepresentation_iff_hasFiniteFreeRepresentation, Stacks.Cohomology.PerfectFromTorAmplitude.isPerfect_of_hasTorAmplitude_of_isPseudoCoherentFrom, Stacks.Cohomology.TorAmplitude.isPseudoCoherent_and_locallyHasFiniteTorDimension_of_isPerfect
statement: formalized
proof: formalized
---

# 20.49 Perfect complexes

Section 20.49 of the Stacks Project, [Tag 08CL](https://stacks.math.columbia.edu/tag/08CL). 11 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08CM, a definition

[Tag 08CM](https://stacks.math.columbia.edu/tag/08CM) in the Stacks Project.

**`Stacks.Cohomology.PerfectComplexes.IsPerfectComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Defs.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Defs.lean#L59). The attribute's comment: “perfect complexes”.

> A complex is perfect if an open cover admits strictly perfect complexes mapping to its
> restrictions by quasi-isomorphisms.

```lean
def IsPerfectComplex {X : RingedSpace.{u, v}}
    (E : CochainComplex (OXMod.{u, v} X) ℤ) : Prop
```

**`Stacks.Cohomology.PerfectComplexes.IsPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Defs.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Defs.lean#L82). The attribute's comment: “perfect derived-category objects”.

> An object of the derived category is perfect if represented by a perfect complex.

```lean
def IsPerfect {X : RingedSpace.{u, v}}
    [HasDerivedCategory.{d} (OXMod.{u, v} X)]
    (K : DerivedCategory (OXMod.{u, v} X)) : Prop
```

## Tag 08CN, a lemma

[Tag 08CN](https://stacks.math.columbia.edu/tag/08CN) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPerfect_of_strictlyPerfect_local_models`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalCriterion.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalCriterion.lean#L59). The attribute's comment: “local_criterion”.

> An object of the derived category of `𝒪_X`-modules which is, on an open covering of `X`,
> isomorphic in the derived category to a strictly perfect complex is perfect.
>
> The hypothesis fixes a complex `F` representing the object, and asks the local strictly perfect
> models to be isomorphic, in the derived categories of the members of the covering, to the
> restrictions of `F`.

```lean
theorem isPerfect_of_strictlyPerfect_local_models (X : RingedSpace.{u, u})
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    [∀ U : Opens X.carrier, HasDerivedCategory.{d'} (OXMod.{u, u} (X.restrict U.isOpenEmbedding))]
    (K : DerivedCategory (OXMod.{u, u} X))
    (h : ∃ F : CochainComplex (OXMod.{u, u} X) ℤ,
      Nonempty (DerivedCategory.Q.obj F ≅ K) ∧
        ∃ (I : Type u) (U : I → Opens X.carrier), (⨆ i, U i) = ⊤ ∧
          ∀ i : I, ∃ P : CochainComplex
            (OXMod.{u, u} (X.restrict (U i).isOpenEmbedding)) ℤ,
            IsStrictlyPerfect P ∧
              Nonempty (DerivedCategory.Q.obj P ≅
                DerivedCategory.Q.obj (restrictComplex F (U i)))) :
    IsPerfect K
```

**`AlgebraicGeometry.RingedSpace.isPerfectComplex_of_isPerfect_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/RepresentativeIndependence.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/RepresentativeIndependence.lean#L55). The attribute's comment: “representative_independence”.

> **Stacks 08CN.** Every complex representing a perfect object of the derived category of
> `𝒪_X`-modules is itself a perfect complex.
>
> Perfectness of `K` provides one perfect representative `E`. The isomorphism `Q(E) ≅ Q(F)` with
> the complex `F` at hand is a roof of quasi-isomorphisms between `E` and `F`, and perfectness of
> complexes is invariant under roofs.

```lean
theorem isPerfectComplex_of_isPerfect_representation
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    {K : DerivedCategory (OXMod.{u, u} X)} (hK : IsPerfect K)
    {F : CochainComplex (OXMod.{u, u} X) ℤ}
    (hF : Nonempty (DerivedCategory.Q.obj F ≅ K)) :
    IsPerfectComplex F
```

## Tag 0BCJ, a lemma

[Tag 0BCJ](https://stacks.math.columbia.edu/tag/0BCJ) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPerfect_iff_hasFiniteLocallyFreeRepresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalRingStalks.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalRingStalks.lean#L58). The attribute's comment: “perfect iff locally finite locally free”.

> **Stacks 0BCJ.** On a ringed space whose structure-sheaf stalks are local rings, a derived
> object is perfect exactly when it has local bounded finite locally free representatives.

```lean
theorem isPerfect_iff_hasFiniteLocallyFreeRepresentation
    [∀ x : X.carrier, IsLocalRing (ToType (X.presheaf.stalk x))]
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (K : DerivedCategory (OXMod.{u, u} X)) :
    IsPerfect K ↔ HasFiniteLocallyFreeRepresentation K
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSpace.hasFiniteLocallyFreeRepresentation_iff_hasFiniteFreeRepresentation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeRepresentation.lean#L342), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalRingStalks.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LocalRingStalks.lean#L81) (StacksFrontier): “finite locally free iff finite free locally”.

## Tag 08CP, a lemma

[Tag 08CP](https://stacks.math.columbia.edu/tag/08CP) in the Stacks Project.

**`Stacks.Cohomology.PerfectFromTorAmplitude.isPerfect_of_hasTorAmplitude_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/BoundedLocalApproximation.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/BoundedLocalApproximation.lean#L191). References: SGA 6 I (5.8), “(ii) ⟹ (i)”.

> **Tag 08CP.** An object of `D(O_X)` on a ringed space with Tor amplitude in `[a, b]`, for
> integers `a ≤ b`, which is `(a - 1)`-pseudo-coherent, is perfect.
>
> The pseudo-coherence supplies a representative `C` and, near every point, a strictly perfect
> approximation of `C|_U` in degrees above `a - 1` with no terms above `b`; its brutal truncation
> `σ^{≥a-1}P` is concentrated in `[a-1, b]` and still approximates above `a - 1`, and the
> Tor-amplitude hypothesis makes the degree-`a` opcycles of that truncation flat, hence locally a
> direct summand of a finite free module. That is what the truncation criterion consumes.

```lean
theorem isPerfect_of_hasTorAmplitude_of_isPseudoCoherentFrom
    (E : DerivedCategory (OXMod.{u, u} X)) (a b : ℤ) (hab : a ≤ b)
    (hamp : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X E a b)
    (hpc : AlgebraicGeometry.RingedSpace.IsPseudoCoherentFrom E (a - 1)) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect E
```

## Tag 08CQ, a lemma

[Tag 08CQ](https://stacks.math.columbia.edu/tag/08CQ) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.isPseudoCoherent_and_locallyHasFiniteTorDimension_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean#L218). The attribute's comment: “(1) implies (2)”. References: SGA 6 I (5.8.1), “necessity”; SGA 6 I (8.5), “special case”.

> **Tag 08CQ, the forward implication.** A perfect object of `D(O_X)` is pseudo-coherent and
> locally has finite Tor dimension.

```lean
theorem isPseudoCoherent_and_locallyHasFiniteTorDimension_of_isPerfect
    (E : DerivedCategory (OXMod.{u} X)) (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect E) :
    AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := X) E ∧
      LocallyHasFiniteTorDimension X E
```

**`Stacks.Cohomology.TorAmplitude.isPerfect_of_isPseudoCoherent_of_locallyHasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean#L253). The attribute's comment: “(2) implies (1)”. References: SGA 6 I (5.8.1), “sufficiency”.

> **Tag 08CQ, the converse implication.** A pseudo-coherent object of `D(O_X)` which locally has
> finite Tor dimension is perfect.
>
> Perfectness is local on the space
> (`Stacks.Cohomology.PerfectComplexTriangles.isPerfect_of_local_isPerfect`), which is what makes
> the per-member Tor-amplitude intervals of `LocallyHasFiniteTorDimension` usable: over a member `U`
> of the cover witnessing finite Tor dimension there is a *single* interval `[a, b]`, and the
> restriction of `E` to `X|_U` is still pseudo-coherent, hence `(a-1)`-pseudo-coherent, so Tag 08CP
> applies there. The interval is widened to `[min a b, max a b]` so that it is nonempty, which Tag
> 08CP requires.

```lean
theorem isPerfect_of_isPseudoCoherent_of_locallyHasFiniteTorDimension
    (E : DerivedCategory (OXMod.{u} X))
    (hpc : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := X) E)
    (htor : LocallyHasFiniteTorDimension X E) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect E
```

## Tag 09UA, a lemma

[Tag 09UA](https://stacks.math.columbia.edu/tag/09UA) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPerfect_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PerfectDerivedPullback.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PerfectDerivedPullback.lean#L167).

> **The derived pullback of a perfect object of `D(𝒪_Y)` is a perfect object of `D(𝒪_X)`**,
> for any models of the two derived categories.
>
> A representative `K` of the given object is resolved by a K-flat complex `P` (Tag 06YS); `P` is
> again a perfect complex, being quasi-isomorphic to `K`, and `Lf^*` of the object is the class of
> the degreewise pullback `f^*P`, which is perfect by
> `AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPerfectComplex_modulePullback`.

```lean
theorem isPerfect_derivedPullback {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    [hX : HasDerivedCategory.{w₁} (SheafOfModules.{u} (structureSheafRing X))]
    [hY : HasDerivedCategory.{w₂} (SheafOfModules.{u} (structureSheafRing Y))]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y) E) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X)
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj E)
```

## Tag 08CR, a lemma

[Tag 08CR](https://stacks.math.columbia.edu/tag/08CR) in the Stacks Project.

**`Stacks.Cohomology.PerfectComplexTriangles.isPerfect_obj₃_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean#L239). The attribute's comment: “third object”.

> **Tag 08CR, third object.** The third object of a distinguished triangle is perfect if the
> first two are. With perfect complexes `E₁`, `E₂` representing the first two vertices, the third
> vertex is `Q` of the mapping cone of a chain map `γ : E₁ ⟶ G` with `E₂ ⟶ G` a quasi-isomorphism
> (`Stacks.Cohomology.PerfectComplexTriangles.exists_mappingCone_iso_obj₃`); `G` is perfect along
> with `E₂`, and the mapping cone of a morphism of perfect complexes is perfect
> (`AlgebraicGeometry.RingedSpace.isPerfectComplex_mappingCone`).

```lean
theorem isPerfect_obj₃_of_distinguished [HasDerivedCategory.{d} (OXMod.{u} X)]
  (T : Triangle (DerivedCategory (OXMod.{u} X))) (hT : T ∈ distinguishedTriangles)
  (h₁ : Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₁) (h₂ :
    Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₂) :
  Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₃
```

**`Stacks.Cohomology.PerfectComplexTriangles.isPerfect_obj₂_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean#L253). The attribute's comment: “second object”.

> **Tag 08CR, second object.**

```lean
theorem isPerfect_obj₂_of_distinguished [HasDerivedCategory.{d} (OXMod.{u} X)]
  (T : Triangle (DerivedCategory (OXMod.{u} X))) (hT : T ∈ distinguishedTriangles)
  (h₁ : Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₁) (h₃ :
    Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₃) :
  Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₂
```

**`Stacks.Cohomology.PerfectComplexTriangles.isPerfect_obj₁_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/Triangles.lean#L263). The attribute's comment: “first object”.

> **Tag 08CR, first object.**

```lean
theorem isPerfect_obj₁_of_distinguished [HasDerivedCategory.{d} (OXMod.{u} X)]
  (T : Triangle (DerivedCategory (OXMod.{u} X))) (hT : T ∈ distinguishedTriangles)
  (h₂ : Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₂) (h₃ :
    Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₃) :
  Stacks.Cohomology.PerfectComplexes.IsPerfect T.obj₁
```

## Tag 09J5, a lemma

[Tag 09J5](https://stacks.math.columbia.edu/tag/09J5) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPerfect_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/DerivedTensorDatumBridge.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/DerivedTensorDatumBridge.lean#L96). The attribute's comment: “at the derived tensor product of the internal Hom development”.

> On a ringed space the derived tensor product `Stacks.SheafOfModules.derivedTensor` takes a
> pair of perfect objects of `D(O_X)` to a perfect object.

```lean
theorem isPerfect_derivedTensor
    (K L : DerivedCategory (StructureSheafModules X.sheaf))
    (hK : IsPerfect (X := X) K)
    (hL : IsPerfect (X := X) L) :
    IsPerfect (X := X)
      (((derivedTensor X.sheaf).obj K).obj L)
```

**`AlgebraicGeometry.RingedSpace.isPerfect_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/TensorProduct.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/TensorProduct.lean#L163). References: SGA 6 I (4.19), “single ringed space”; SGA 6 0 (4.2), “more general”.

> **The derived tensor product of two perfect objects of `D(𝒪_X)` is perfect.**
>
> Represent the objects by perfect complexes `E` and `F`, and replace `F` by a K-flat resolution
> `B`, which is perfect as well.  The derived tensor product is then the class of the total tensor
> complex `Tot(E ⊗_{𝒪_X} B)`, which is perfect by
> `AlgebraicGeometry.RingedSpace.isPerfectComplex_tensorComplex`.
>
> Stated for an arbitrary derived tensor product, since only its `comparisonRight` field is used.

```lean
theorem isPerfect_derivedTensorProduct
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.sheaf)
    (K L : DerivedCategory (OXMod.{u, u} X)) (hK : IsPerfect K) (hL : IsPerfect L) :
    IsPerfect ((T.tensor.obj K).obj L)
```

## Tag 08CS, a lemma

[Tag 08CS](https://stacks.math.columbia.edu/tag/08CS) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.isPerfect_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PseudoCoherentAndFiniteTorDimension.lean#L296).

> **Tag 08CS.** If a binary biproduct in `D(O_X)` is perfect, then so are both of its summands.
>
> By Tag 08CQ the biproduct is pseudo-coherent and locally of finite Tor dimension; both properties
> pass to the summands, pseudo-coherence by Tag 08CE and locally finite Tor dimension by Tag 08CK;
> and Tag 08CQ turns the pair back into perfectness of each summand.

```lean
theorem isPerfect_of_biprod (K L : DerivedCategory (OXMod.{u} X))
    (h : Stacks.Cohomology.PerfectComplexes.IsPerfect (K ⊞ L)) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect K ∧
      Stacks.Cohomology.PerfectComplexes.IsPerfect L
```

## Tag 08DP, a lemma

[Tag 08DP](https://stacks.math.columbia.edu/tag/08DP) in the Stacks Project.

**`Stacks.Cohomology.ClosedSupportPerfect.isPerfect_derivedPushforward_of_closedSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/ClosedSupportPerfect.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/ClosedSupportPerfect.lean#L635).

> **Stacks 08DP.** The derived pushforward of a perfect object on an open subspace is perfect
> if its cohomology is supported on a subset closed in the ambient space.

```lean
theorem isPerfect_derivedPushforward_of_closedSupport
    (X : RingedSpace.{u, u}) (U : Opens X) (T : Set (X.restrict U.isOpenEmbedding).carrier)
    (hT : IsClosed ((X.ofRestrict U.isOpenEmbedding).hom.base '' T))
    (Rj : DerivedCategory (SheafOfModules.{u} (structureSheafRing
      (X.restrict U.isOpenEmbedding))) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (αj : (modulePushforward (X.ofRestrict U.isOpenEmbedding)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rj)
    [hRj : Rj.IsRightDerivedFunctor αj
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing
      (X.restrict U.isOpenEmbedding))))
    (hE : RingedSpace.IsPerfect (X := X.restrict U.isOpenEmbedding) E)
    (hET : CohomologySupportedOn
      (structureSheafRing (X.restrict U.isOpenEmbedding)) T E) :
    RingedSpace.IsPerfect (X := X) (Rj.obj E)
```

## Tag 0GT1, a lemma

[Tag 0GT1](https://stacks.math.columbia.edu/tag/0GT1) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.cohomologyFiniteFreeLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean#L161). The attribute's comment: “the locus”.

> **The finite free cohomology locus of a derived object.** These are the points at which every
> cohomology stalk `H^i(E)_x` is a finite free `𝒪_{X, x}`-module.

```lean
def cohomologyFiniteFreeLocus [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (E : DerivedCategory (OXMod.{u, u} X)) : Set X.carrier
```

**`AlgebraicGeometry.RingedSpace.subset_cohomologyFiniteFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean#L188). The attribute's comment: “maximality of the locus”.

> **Stacks 0GT1, maximality.** Every open set over which all the cohomology sheaves of a derived
> object are finite locally free is contained in the finite free cohomology locus: finite local
> freeness near a point makes the cohomology stalks there finite free.

```lean
theorem subset_cohomologyFiniteFreeLocus [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (E : DerivedCategory (OXMod.{u, u} X)) (V : Opens X.carrier)
    (hV : ∀ i : ℤ, IsFiniteLocallyFreeOver
      ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) i).obj E) V) :
    (V : Set X.carrier) ⊆ cohomologyFiniteFreeLocus E
```

**`AlgebraicGeometry.RingedSpace.isOpen_cohomologyFiniteFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/CohomologyFiniteFreeLocus.lean#L698). The attribute's comment: “openness of the locus”.

> **Stacks 0GT1, openness.** On a ringed space whose structure-sheaf stalks are local rings,
> the finite free cohomology locus of a perfect object of the derived category of `𝒪_X`-modules is
> open: near a point of the locus the object is computed by a strictly perfect complex, whose
> opcycles are then free on a neighbourhood, and over such a neighbourhood all the cohomology
> stalks are again finite free.

```lean
theorem isOpen_cohomologyFiniteFreeLocus
    [hloc : ∀ x : X.carrier, IsLocalRing (ToType (X.presheaf.stalk x))]
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (E : DerivedCategory (OXMod.{u, u} X))
    (hE : IsPerfect E) : IsOpen (cohomologyFiniteFreeLocus E)
```

**`Stacks.Cohomology.PerfectComplexes.cohomologyFiniteFreeLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Locus.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Locus.lean#L130). The attribute's comment: “the locus”.

> The set of points at which every cohomology sheaf of an object of `D(𝒪_X)` has a
> finite free stalk.

```lean
def cohomologyFiniteFreeLocus {X : RingedSpace.{u, v}}
    [HasDerivedCategory.{d} (OXMod.{u, v} X)]
    (E : DerivedCategory (OXMod.{u, v} X)) : Set X
```

**`Stacks.Cohomology.PerfectComplexes.isOpen_cohomologyFiniteFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean#L719). The attribute's comment: “openness”.

> The locus where all cohomology stalks of a perfect object are finite free is open.

```lean
theorem isOpen_cohomologyFiniteFreeLocus
    {X : RingedSpace.{u, v}}
    [∀ x : X, IsLocalRing (structureSheafStalk X x)]
    [HasDerivedCategory.{d} (OXMod.{u, v} X)]
    (E : DerivedCategory (OXMod.{u, v} X)) (hE : IsPerfect E) :
    IsOpen (cohomologyFiniteFreeLocus E)
```

**`Stacks.Cohomology.PerfectComplexes.isFiniteLocallyFree_homology_restrict_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean#L747). The attribute's comment: “finite locally free”.

> On the finite free locus of a perfect object every cohomology sheaf is finite locally
> free.

```lean
theorem isFiniteLocallyFree_homology_restrict_locus
    {X : RingedSpace.{u, v}}
    [∀ x : X, IsLocalRing (structureSheafStalk X x)]
    [HasDerivedCategory.{d} (OXMod.{u, v} X)]
    (E : DerivedCategory (OXMod.{u, v} X)) (hE : IsPerfect E)
    (i : ℤ) :
    IsFiniteLocallyFree
      ((restrictModules X
        ⟨cohomologyFiniteFreeLocus E,
          isOpen_cohomologyFiniteFreeLocus E hE⟩).obj
        ((DerivedCategory.homologyFunctor (OXMod.{u, v} X) i).obj E))
```

**`Stacks.Cohomology.PerfectComplexes.le_cohomologyFiniteFreeLocus_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/FiniteFreeLocus/Openness.lean#L771). The attribute's comment: “maximality”.

> An open set on which all cohomology sheaves of a perfect object are finite locally free is
> contained in its finite free locus; together with the previous result this says the locus is
> the largest such open set.

```lean
theorem le_cohomologyFiniteFreeLocus_of_isFiniteLocallyFree
    {X : RingedSpace.{u, v}}
    [∀ x : X, IsLocalRing (structureSheafStalk X x)]
    [HasDerivedCategory.{d} (OXMod.{u, v} X)]
    (E : DerivedCategory (OXMod.{u, v} X)) (hE : IsPerfect E)
    (V : Opens X)
    (hV : ∀ i : ℤ, IsFiniteLocallyFree
      ((restrictModules X V).obj
        ((DerivedCategory.homologyFunctor (OXMod.{u, v} X) i).obj E))) :
    V ≤ ⟨cohomologyFiniteFreeLocus E,
      isOpen_cohomologyFiniteFreeLocus E hE⟩
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.49, Tag 08CL](https://stacks.math.columbia.edu/tag/08CL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
