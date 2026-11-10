---
declaration: section
origin: cited
lean: Stacks.Cohomology.KFlatDerivedPullback.derivedPullback_commShift, Stacks.Cohomology.KFlatDerivedPullback.derivedPullback_isTriangulated, Stacks.Cohomology.KFlatDerivedPullback.isIso_derivedPullbackComparison_app_of_kFlat, Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback, Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullbackComparison, Stacks.DerivedPullback.Composition.isIso_derivedPullbackCompComparisonCanonical, Stacks.Cohomology.DerivedPullbackTensor.derivedPullbackTensorIso, Stacks.Cohomology.MixedDerivedTensorOnARingedSpace.spaceDerivedLinearMixedTensorIso
statement: formalized
proof: formalized
---

# 20.27 Derived pullback

Section 20.27 of the Stacks Project, [Tag 06YI](https://stacks.math.columbia.edu/tag/06YI). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06YJ, a lemma

[Tag 06YJ](https://stacks.math.columbia.edu/tag/06YJ) in the Stacks Project.

**`Stacks.Cohomology.KFlatDerivedPullback.derivedPullback_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Triangulated.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Triangulated.lean#L146). The attribute's comment: “compatibility with shifts”.

> **The derived pullback commutes with the shift.**  `Lf^*` is the total left derived functor
> of degreewise pullback along `Qh`; degreewise pullback and `Qh` both commute with the shift, and
> the quasi-isomorphisms of `K(𝒪_Y)` are stable under it, so the derived functor does too.

```lean
instance derivedPullback_commShift :
  (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).CommShift ℤ
```

**`Stacks.Cohomology.KFlatDerivedPullback.derivedPullback_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Triangulated.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Triangulated.lean#L192). The attribute's comment: “exactness”.

> **The derived pullback is exact**: `Lf^* : D(𝒪_Y) ⥤ D(𝒪_X)` carries distinguished triangles
> to distinguished triangles.
>
> Every morphism of `D(𝒪_Y)` is, up to isomorphism of arrows, the image of a morphism between
> K-flat complexes: the K-flat objects resolve every object, so their inclusion is a localized
> equivalence and the induced functor is essentially surjective on arrows.  Completing such a
> morphism to a distinguished triangle of `K(𝒪_Y)` leaves all three vertices K-flat, the third by
> `isKFlat_obj₃_of_distTriang`, and the comparison of `Lf^*` is invertible at each of them.  That
> is exactly the input of `CategoryTheory.Functor.isTriangulated_of_rightExtension`.

```lean
instance derivedPullback_isTriangulated :
    (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).IsTriangulated
```

**`Stacks.Cohomology.KFlatDerivedPullback.isIso_derivedPullbackComparison_app_of_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean#L98). The attribute's comment: “computation on K-flat complexes”.

> **A K-flat complex computes the derived pullback**: on it the canonical comparison
> `Lf^* K ⟶ f^* K` is invertible.  This is the clause of Tag 06YJ that says the construction
> agrees with degreewise pullback where degreewise pullback is already derived, and it holds for
> an arbitrary morphism of ringed spaces: the K-flat complexes are a resolving datum for `f^*`,
> and the comparison of a left derived functor is invertible on its resolving class.
>
> The two models of the derived categories are binders rather than the file's pinned
> `HasDerivedCategory.standard`: every ingredient of the proof is model-free.

```lean
theorem isIso_derivedPullbackComparison_app_of_kFlat
    [HasDerivedCategory.{w₁} (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory.{w₂} (SheafOfModules.{u} (structureSheafRing Y))]
    (K : CochainComplex (SheafOfModules.{u} (structureSheafRing Y)) ℤ) (hK : KFlatComplex Y K) :
    IsIso ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullbackComparison f).app
      ((HomotopyCategory.quotient (SheafOfModules.{u} (structureSheafRing Y))
        (ComplexShape.up ℤ)).obj K))
```

Declarations registered for the tag:

- [`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/PullbackPushforwardAdjunction.lean#L291), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean#L123) (StacksFrontier): “the derived pullback functor”.
- [`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullbackComparison`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/PullbackPushforwardAdjunction.lean#L298), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/Unconditional.lean#L126) (StacksFrontier): “canonical comparison”.

## Tag 0D5S, a lemma

[Tag 0D5S](https://stacks.math.columbia.edu/tag/0D5S) in the Stacks Project.

**`Stacks.DerivedPullback.Composition.isIso_derivedPullbackCompComparisonCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/CompositionUnconditional.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/CompositionUnconditional.lean#L152).

> **Stacks 0D5S.**  The canonical comparison from the composite of the derived pullbacks along
> `g` and `f` to the derived pullback along `f ≫ g` is an isomorphism, for arbitrary composable
> morphisms of ringed spaces.
>
> Every hypothesis of `isIso_derivedPullbackCompComparison` is met at the K-flat classes on `Z`
> and on `Y`.

```lean
theorem isIso_derivedPullbackCompComparisonCanonical :
    IsIso (derivedPullbackCompComparisonCanonical f g)
```

## Tag 079U, a lemma

[Tag 079U](https://stacks.math.columbia.edu/tag/079U) in the Stacks Project.

**`Stacks.Cohomology.DerivedPullbackTensor.derivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/PullbackTensorComparison.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/PullbackTensorComparison.lean#L532).

> **Stacks 079U: derived pullback is monoidal.**  For a morphism of ringed spaces
> `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` there is a canonical isomorphism
>
> `Lf^*(K ⊗^L_{𝒪_Y} L) ≅ Lf^*K ⊗^L_{𝒪_X} Lf^*L`,
>
> bifunctorial in `K, L ∈ D(𝒪_Y)`.
>
> It is constructed the way the source constructs it.  On K-flat representatives both sides are
> computed by ordinary total tensor complexes — the K-flat comparison of Stacks 06YU and the
> fact that a K-flat complex computes `Lf^*` — and there the comparison is the degreewise
> isomorphism `f^*(K^p ⊗_{𝒪_Y} L^q) ≅ f^*K^p ⊗_{𝒪_X} f^*L^q` of Stacks 01CD assembled on total
> complexes.  Since `D(𝒪_Y)` is the localization of the K-flat objects of the homotopy category
> at the quasi-isomorphisms (Stacks 06YS), the product of two copies of that localization
> descends the comparison from K-flat representatives to all of `D(𝒪_Y) × D(𝒪_Y)`, which is
> what makes the statement bifunctorial.

```lean
def derivedPullbackTensorIso : pullbackOfTensor f ≅ tensorOfPullbacks f
```

## Tag 08DE, a lemma

[Tag 08DE](https://stacks.math.columbia.edu/tag/08DE) in the Stacks Project.

**`Stacks.Cohomology.MixedDerivedTensorOnARingedSpace.spaceDerivedLinearMixedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/MixedDerivedTensorOnARingedSpace.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/MixedDerivedTensorOnARingedSpace.lean#L374). The attribute's comment: “the canonical bifunctorial isomorphism in D(O_X): the tensor product over the smaller sheaf of rings f⁻¹O_Y is an O_X-module through its first factor”.

> **Stacks 08DE, `O_X`-linearly.**  The canonical bifunctorial isomorphism
>
> `F ⊗^L_{O_X} Lf^*G ≅ F ⊗^L_{f⁻¹O_Y} f⁻¹G`
>
> in `D(O_X)`, for a morphism `f : (X, O_X) ⟶ (Y, O_Y)` of ringed spaces, `F` in `D(O_X)` and `G`
> in `D(O_Y)`.  Both sides are objects of `D(O_X)`: the tensor product over the smaller sheaf of
> rings `f⁻¹O_Y` inherits the `O_X`-action from `F`, and the mixed tensor product realising it is
> `Stacks.MixedTensor.sheafMixedTensorRight`, whose sections are `F(U) ⊗_{f⁻¹O_Y(U)} f⁻¹G(U)`.
>
> `derivedMixedTensorIso` above is the comparison read after restriction of scalars to
> `D(f⁻¹O_Y)`.

```lean
def spaceDerivedLinearMixedTensorIso :
    spaceLinearDerivedTensorPullback f ≅ spaceLinearDerivedMixedTensor f
```

**`Stacks.Cohomology.MixedDerivedTensorOnARingedSpace.derivedLinearMixedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/MixedDerivedTensorOnARingedSpace.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/MixedDerivedTensorOnARingedSpace.lean#L402). The attribute's comment: “the canonical bifunctorial isomorphism, in D(O_X)”.

> **Stacks 08DE, through the one-sided K-flat descent of the mixed tensor product.**  The
> canonical bifunctorial isomorphism
>
> `F ⊗^L_{O_X} Lf^*G ≅ F ⊗^L_{f⁻¹O_Y} f⁻¹G`
>
> in `D(O_X)`, for a morphism `f : (X, O_X) ⟶ (Y, O_Y)` of ringed spaces, `F` in `D(O_X)` and
> `G` in `D(O_Y)`.  The right-hand side is the derived tensor product over `f⁻¹O_Y` of `F` and
> `f⁻¹G`, an object of `D(O_X)` through `F`.  It is stated between the two uncurried bifunctors on
> `D(O_X) × D(O_Y)`, so that bifunctoriality is part of its type, and the left-hand one is written
> with the ringed-space derived pullback of Tag 06YJ.

```lean
def derivedLinearMixedTensorIso :
    spaceLinearDerivedTensorPullback f ≅ spaceDerivedMixedTensorInverseImage f
```

## Tag 0FP0, a lemma

[Tag 0FP0](https://stacks.math.columbia.edu/tag/0FP0) in the Stacks Project.

**`Stacks.Cohomology.DerivedPullbackTensor.derivedPullbackTensorIso_toTensor_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/TensorPullCompatibility.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPullback/TensorPullCompatibility.lean#L192).

> **Stacks 0FP0.**  Let `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` be a morphism of ringed spaces and let
> `K, M` be complexes of `𝒪_Y`-modules.  The diagram
>
> ```
> Lf^*(K ⊗^L_{𝒪_Y} M)  ⟶  Lf^*Tot(K ⊗_{𝒪_Y} M)
>         |                           |
>         v                           v
> Lf^*K ⊗^L_{𝒪_X} Lf^*M        f^*Tot(K ⊗_{𝒪_Y} M)
>         |                           |
>         v                           v
>  f^*K ⊗^L_{𝒪_X} f^*M    ⟶   Tot(f^*K ⊗_{𝒪_X} f^*M)
> ```
>
> commutes: the left hand column — Stacks 079U, then the comparison `Lf^*(QN) ⟶ Q(f^*N)` in each
> tensor factor — followed by the canonical map to the ordinary total tensor complex on `X`
> equals the top row — the derived pullback of the canonical map to the ordinary total tensor
> complex on `Y` — followed by the right hand column, the comparison `Lf^*(QN) ⟶ Q(f^*N)` at
> `Tot(K ⊗_{𝒪_Y} M)` and then the comparison of total complexes of Stacks 01CD.
>
> This is
> `derivedPullbackTensorIso_hom_app_comp_rightComparison_of_complexes` with the right comparison
> written out: postcomposing with the comparison of total complexes cancels the inverse that the
> right comparison ends with, leaving the six arrows of the source's diagram.

```lean
theorem derivedPullbackTensorIso_toTensor_comm
    (K L : CochainComplex (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y) ℤ) :
    (derivedPullbackTensorIso f).hom.app
          (DerivedCategory.Q.obj K, DerivedCategory.Q.obj L) ≫
        (Functor.uncurry.obj
              (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf)).map
            ((derivedPullbackNatTrans f).app K ×ₘ (derivedPullbackNatTrans f).app L) ≫
          (derivedToTensorNatTrans X).app
            ((pullbackComplex f).obj K, (pullbackComplex f).obj L) =
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).map
          ((derivedToTensorNatTrans Y).app (K, L)) ≫
        (derivedPullbackNatTrans f).app
            ((totalComplexPair (Stacks.SheafOfModules.Tensor.sheafTensor Y.sheaf)).obj (K, L)) ≫
          DerivedCategory.Q.map ((pullbackTensorComplexNatIso f).hom.app (K, L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.27, Tag 06YI](https://stacks.math.columbia.edu/tag/06YI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
