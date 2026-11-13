---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar, AlgebraicGeometry.FormalSpace.isAdicMorphism_tfae, RingHom.isTaut_of_isAdic, RingHom.isAdic_iff_isTaut, RingHom.isAdic_of_isTaut, AlgebraicGeometry.FormalSpace.IsAdicMorphism, AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces
statement: formalized
proof: formalized
---

# 87.23 Adic morphisms

Section 87.23 of the Stacks Project, [Tag 0AQ2](https://stacks.math.columbia.edu/tag/0AQ2). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AQ2, the section

[Tag 0AQ2](https://stacks.math.columbia.edu/tag/0AQ2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean#L200). The attribute's comment: “the footnote of the section: on WAdm^\{adic*} the adic and the taut reading of the chart condition agree”.

> **Section 0AQ2, the footnote.** On `WAdm^{adic*}` the chart condition of the section may be
> read with "adic" or with "taut": the two readings agree, by Stacks 0GBS.

```lean
theorem isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) :
    IsAdicOnEveryAffineEtaleDiagram B S hS f ↔
      IsTautOnEveryAffineEtaleDiagramAdicStar B S hS f
```

**`AlgebraicGeometry.FormalSpace.isAdicMorphism_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphismConverse.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphismConverse.lean#L250). The attribute's comment: “the equivalence of conditions (1) and (2) of the section for a morphism of locally adic* formal algebraic spaces, together with the footnote reading (2) with taut maps”.

> **Section 0AQ2.** Let `f : X ⟶ Y` be a morphism of locally adic\* formal algebraic spaces
> over `S`. The following are equivalent:
>
> 1. `f` is representable by algebraic spaces, that is, `f` is an adic morphism in the sense of
>    Definition 0AQ3;
> 2. for every commutative square
>    ```
>    U ⟶ V
>    ↓     ↓
>    X ⟶ Y
>    ```
>    with `U` and `V` affine formal algebraic spaces and `U ⟶ X`, `V ⟶ Y` representable by
>    algebraic spaces and étale, the morphism `U ⟶ V` corresponds to an adic map in
>    `WAdm^{adic*}`;
> 3. the same with "adic" replaced by "taut", which is the footnote of the section.

```lean
theorem isAdicMorphism_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y) :
    List.TFAE
      [ IsAdicMorphism B S hS f,
        IsAdicOnEveryAffineEtaleDiagram B S hS f,
        IsTautOnEveryAffineEtaleDiagramAdicStar B S hS f ]
```

## Tag 0GBS, a lemma

[Tag 0GBS](https://stacks.math.columbia.edu/tag/0GBS) in the Stacks Project.

**`RingHom.isTaut_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L435). The attribute's comment: “part (1)”.

> A continuous adic homomorphism of linearly topologized rings is taut.

```lean
public theorem isTaut_of_isAdic
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hAdic : RingHom.IsAdic φ) :
    RingHom.IsTaut φ
```

**`RingHom.isAdic_iff_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L466). The attribute's comment: “on WAdm^\{adic*}”.

> Adicness and tautness are equivalent for a continuous homomorphism from a linearly
> topologized ring with a finitely generated ideal of definition to a complete separated linearly
> topologized ring. In particular, this applies to morphisms in `WAdm^{adic*}`.

```lean
public theorem isAdic_iff_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B)
    (hA : ∃ I : Ideal A, I.FG ∧ _root_.IsAdic I)
    [@CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)] [T2Space B] :
    RingHom.IsAdic φ ↔ RingHom.IsTaut φ
```

Declarations registered for the tag:

- [`RingHom.isAdic_of_isTaut`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L322), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L460) (StacksFrontier): “part (2)”.

## Tag 0AQ3, a definition

[Tag 0AQ3](https://stacks.math.columbia.edu/tag/0AQ3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsAdicMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean#L134).

> **Stacks 0AQ3.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` with
> `X` and `Y` locally adic\*. Then `f` is an *adic morphism* when `f` is representable by
> algebraic spaces.
>
> The locally adic\* hypotheses on `X` and `Y` are the standing assumptions under which the
> source introduces the terminology; as for Stacks 0AQM they are imposed by the results that use
> the predicate rather than built into it, so that the predicate is the defining condition and
> nothing more.

```lean
abbrev IsAdicMorphism {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean#L85). The attribute's comment: “the defining condition of an adic morphism”.

> **Stacks Project, Tag 02YQ.** A morphism of presheaves is representable by algebraic
> spaces if its pullback to every scheme over the base is an algebraic space.

```lean
abbrev IsRepresentableByAlgebraicSpaces (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.23, Tag 0AQ2](https://stacks.math.columbia.edu/tag/0AQ2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
