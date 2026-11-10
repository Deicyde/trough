---
declaration: section
origin: cited
lean: Rig.IsFiniteTypeOnReductions, Rig.finiteTypeOnReductionsProperty_localizationPreserves, Rig.finiteTypeOnReductionsProperty_finiteProductPreserves, Rig.finiteTypeOnReductionsProperty_faithfullyFlatDescent, Rig.isFiniteTypeOnReductions_local, Rig.isFiniteTypeOnReductions_stableUnderBaseChange, Rig.finiteTypeOnReductions_isStableUnderComposition, Rig.isFiniteTypeOnReductions_of_isTaut_of_isTopologicallyOfFiniteType
statement: formalized
proof: formalized
---

# 88.12 Finite type on reductions

Section 88.12 of the Stacks Project, [Tag 0GC1](https://stacks.math.columbia.edu/tag/0GC1). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GC2, a lemma

[Tag 0GC2](https://stacks.math.columbia.edu/tag/0GC2) in the Stacks Project.

**`Rig.IsFiniteTypeOnReductions`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Reduction.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Reduction.lean#L62). The attribute's comment: “finite\_type\_on\_reductions”.

> A continuous homomorphism of linearly topologized commutative rings is *of finite type on
> reductions* if the induced homomorphism between the quotients by their topological
> nilradicals is of finite type.

```lean
public abbrev IsFiniteTypeOnReductions {A B : Type*} [CommRing A] [TopologicalSpace A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsLinearTopology B B]
    (φ : A →+* B) (hφ : Continuous φ) : Prop
```

**`Rig.finiteTypeOnReductionsProperty_localizationPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ReductionLocality.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/ReductionLocality.lean#L194). The attribute's comment: “localization\_preserves”.

> Finite type on reductions ascends along a completed étale localization diagram of countably
> indexed weakly admissible rings: the first locality axiom of Situation 0CBA.

```lean
public theorem finiteTypeOnReductionsProperty_localizationPreserves :
    TopologicalRing.LocalizationPreserves.{u} TopologicalRing.IsCountablyWeaklyAdmissible
      TopologicalRing.FiniteTypeOnReductionsProperty
```

**`Rig.finiteTypeOnReductionsProperty_finiteProductPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ReductionLocality.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/ReductionLocality.lean#L287). The attribute's comment: “finite\_product”.

> Finite type on reductions is preserved by a finite product of targets: the third locality
> axiom of Situation 0CBA.  Topological nilpotence in a product is a coordinatewise condition, so
> the reduction of the product is a quotient of the product of the reductions.

```lean
public theorem finiteTypeOnReductionsProperty_finiteProductPreserves :
    TopologicalRing.FiniteProductPreserves.{u} TopologicalRing.IsCountablyWeaklyAdmissible
      TopologicalRing.FiniteTypeOnReductionsProperty
```

**`Rig.finiteTypeOnReductionsProperty_faithfullyFlatDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ReductionLocality.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/ReductionLocality.lean#L426). The attribute's comment: “faithfully\_flat\_descent”.

> Finite type on reductions descends along a completed étale localization diagram of countably
> indexed weakly admissible rings whose horizontal map is faithfully flat: the second locality
> axiom of Situation 0CBA.  The reduced diagonal of the diagram is of finite type, being the
> reduction of the canonical map into the completion of an étale algebra followed by the reduction
> of the completed morphism, and finite type descends along the faithfully flat, finitely
> presented reduction of the horizontal map.

```lean
public theorem finiteTypeOnReductionsProperty_faithfullyFlatDescent :
    TopologicalRing.FaithfullyFlatDescent.{u} TopologicalRing.IsCountablyWeaklyAdmissible
      TopologicalRing.FiniteTypeOnReductionsProperty
```

**`Rig.isFiniteTypeOnReductions_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ReductionLocality.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/ReductionLocality.lean#L454).

> Finite type on reductions is a local property of morphisms of countably indexed weakly
> admissible topological rings: it ascends along completed étale localization diagrams, descends
> along those whose horizontal map is faithfully flat, and is preserved by finite products of
> targets.

```lean
public theorem isFiniteTypeOnReductions_local :
    TopologicalRing.PropertyIsLocal.{u} TopologicalRing.FiniteTypeOnReductionsProperty
      TopologicalRing.IsCountablyWeaklyAdmissible
```

## Tag 0GC3, a lemma

[Tag 0GC3](https://stacks.math.columbia.edu/tag/0GC3) in the Stacks Project.

**`Rig.isFiniteTypeOnReductions_stableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/ReductionBaseChange.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/ReductionBaseChange.lean#L319).

> Finite type on reductions is a local property of countably indexed weakly admissible rings
> that is preserved by completed tensor-product base change.

```lean
public theorem isFiniteTypeOnReductions_stableUnderBaseChange :
    TopologicalRing.IsStableUnderBaseChange TopologicalRing.FiniteTypeOnReductionsProperty
```

## Tag 0GC4, a lemma

[Tag 0GC4](https://stacks.math.columbia.edu/tag/0GC4) in the Stacks Project.

**`Rig.finiteTypeOnReductions_isStableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/ReductionComposition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/ReductionComposition.lean#L56).

> Finite type on reductions is a composition-stable local property of morphisms of countably
> indexed weakly admissible topological rings.

```lean
public theorem finiteTypeOnReductions_isStableUnderComposition :
    TopologicalRing.PropertyIsStableUnderComposition
      TopologicalRing.FiniteTypeOnReductionsProperty.{u}
```

## Tag 0GC5, a lemma

[Tag 0GC5](https://stacks.math.columbia.edu/tag/0GC5) in the Stacks Project.

**`Rig.isFiniteTypeOnReductions_of_isTaut_of_isTopologicallyOfFiniteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Reduction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Reduction.lean#L72).

> A continuous taut homomorphism that is topologically of finite type is of finite type on
> reductions, provided its source has a weak ideal of definition.

```lean
public lemma isFiniteTypeOnReductions_of_isTaut_of_isTopologicallyOfFiniteType
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    (φ : A →+* B) (hφ : Continuous φ) (hA : TopologicalRing.IsWeaklyPreAdmissible A)
    (htaut : RingHom.IsTaut φ) (hft : TopologicalRing.IsTopologicallyOfFiniteType φ) :
    IsFiniteTypeOnReductions φ hφ
```

## Tag 0GC6, a lemma

[Tag 0GC6](https://stacks.math.columbia.edu/tag/0GC6) in the Stacks Project.

**`Rig.isTopologicallyOfFiniteType_of_isFiniteTypeOnReductions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Reduction.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Reduction.lean#L280).

> A continuous homomorphism into a Noetherian weakly admissible topological ring that is of
> finite type on reductions is topologically of finite type.

```lean
public theorem isTopologicallyOfFiniteType_of_isFiniteTypeOnReductions
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] [IsNoetherianRing B]
    (φ : A →+* B) (hφ : Continuous φ) (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hred : IsFiniteTypeOnReductions φ hφ) :
    TopologicalRing.IsTopologicallyOfFiniteType φ
```

## Tag 0GG6, a lemma

[Tag 0GG6](https://stacks.math.columbia.edu/tag/0GG6) in the Stacks Project.

**`Rig.isFiniteTypeOnReductions_iff_isTopologicallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Reduction.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Reduction.lean#L363).

> An adic homomorphism into a Noetherian weakly admissible ring is of finite type on
> reductions if and only if it is topologically of finite type.

```lean
public theorem isFiniteTypeOnReductions_iff_isTopologicallyOfFiniteType
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] [IsNoetherianRing B]
    (φ : A →+* B) (hφ : Continuous φ)
    (hA : TopologicalRing.IsWeaklyPreAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hadic : RingHom.IsAdic φ) :
    IsFiniteTypeOnReductions φ hφ ↔
      TopologicalRing.IsTopologicallyOfFiniteType φ
```

## Tag 0GC7, a lemma

[Tag 0GC7](https://stacks.math.columbia.edu/tag/0GC7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnReductions_tfae_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeOnReductionsTfae.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeOnReductionsTfae.lean#L247). The attribute's comment: “the four conditions, for a morphism of locally countably indexed formal algebraic spaces; condition (4) is read for every pair of reductions of the source and the target and every morphism between them over f, reductions existing and being unique up to unique isomorphism by Stacks 0AIN”.

> **Stacks 0GC7.** For a morphism `f : X ⟶ Y` of locally countably indexed formal algebraic
> spaces over `S` the following are equivalent:
>
> 1. every affine representable étale square over `f` has its upper map given by an arrow of
>    `WAdm^{count}` with the property of Stacks 0GC2;
> 2. there is an affine étale covering of `Y` together with affine étale coverings of the fibre
>    products of its members with `X` whose maps to the members of the first covering are given by
>    such arrows;
> 3. there is an affine étale covering of `X` whose members factor through affine formal
>    algebraic spaces representable étale over `Y` by such arrows;
> 4. the morphism of reductions `f_red : X_red ⟶ Y_red` is locally of finite type.
>
> The first three are the three conditions of Stacks 0ANG for the property of Stacks 0GC2, which
> is local on `WAdm^{count}`; (3) ⟹ (4) and (4) ⟹ (1) are the affine computation of Stacks 0GB6
> together with the étale locality of being locally of finite type.

```lean
theorem isLocallyOfFiniteTypeOnReductions_tfae_of_isLocallyCountablyIndexed
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y) :
    List.TFAE
      [HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.FiniteTypeOnReductionsProperty f,
        HasPropertyAfterTargetCover B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.FiniteTypeOnReductionsProperty f,
        HasPropertyAfterSourceCover B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.FiniteTypeOnReductionsProperty f,
        IsLocallyOfFiniteTypeOnReductions B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.12, Tag 0GC1](https://stacks.math.columbia.edu/tag/0GC1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
