---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar, AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_of_isRepresentable, AlgebraicGeometry.FormalSpace.isAdicMorphism_tfae, RingHom.isTaut_of_isAdic, RingHom.isAdic_iff_isTaut, RingHom.isAdic_of_isTaut, AlgebraicGeometry.FormalSpace.IsAdicMorphism, AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces
statement: formalized
proof: formalized
---

# 87.23 Adic morphisms

Section 87.23 of the Stacks Project, [Tag 0AQ2](https://stacks.math.columbia.edu/tag/0AQ2). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AQ2, the section

[Tag 0AQ2](https://stacks.math.columbia.edu/tag/0AQ2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean#L197). The attribute's comment: “the footnote of the section: on WAdm^{adic*} the adic and the taut reading of the chart condition agree”.

> **Section 0AQ2, the footnote.** On `WAdm^{adic*}` the chart condition of the section may be
> read with "adic" or with "taut": the two readings agree, by Stacks 0GBS.

```lean
theorem isAdicOnEveryAffineEtaleDiagram_iff_isTautAdicStar {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) :
    IsAdicOnEveryAffineEtaleDiagram B S hS f ↔
      IsTautOnEveryAffineEtaleDiagramAdicStar B S hS f
```

**`AlgebraicGeometry.FormalSpace.isAdicOnEveryAffineEtaleDiagram_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean#L221). The attribute's comment: “the implication from representability by algebraic spaces to the chart condition, through Stacks 0ANK with the five hypotheses that lemma carries in this library; the converse is not proved, since it would need the chart condition at the wider countably indexed weakly admissible class that Stacks 0ANK is stated at”.

> **Section 0AQ2, condition (1) implies condition (2).** A morphism of locally countably
> indexed formal algebraic spaces over `S` which is representable by algebraic spaces has every
> one of its chart maps in `WAdm^{adic*}` adic; this is the matching the section makes, and it is
> the content of Definition 0AQ3's reference to the discussion.
>
> Stacks 0ANK turns representability into the taut reading of the chart condition at the
> countably indexed weakly admissible class, which contains `WAdm^{adic*}`; the footnote then
> turns taut into adic. The five hypotheses `h0AJ3`, `h0AKX`, `h0AN5`, `h0AQ0` and `h0AN4` are
> those of Stacks 0ANK in this library and are passed straight through.

```lean
theorem isAdicOnEveryAffineEtaleDiagram_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (h0AJ3 : ∀ (V : FppfSheaf B S hS) (v : V ⟶ Y), IsAffineFormalAlgebraicSpace B S hS V →
      IsRepresentableEtale B S hS v → IsFormalAlgebraicSpace B S hS (pullback v f))
    (h0AKX : ∀ (Z : FppfSheaf B S hS), IsLocallyCountablyIndexed B S hS Z →
      ∀ (U : FppfSheaf B S hS) (a : U ⟶ Z), IsAffineFormalAlgebraicSpace B S hS U →
      IsRepresentableEtale B S hS a → IsCountablyIndexed B S hS U)
    (h0AN5 : ∀ {U V : FppfSheaf B S hS} (t : U ⟶ V),
      IsAffineFormalAlgebraicSpace B S hS U → IsAffineFormalAlgebraicSpace B S hS V →
      IsCountablyIndexed B S hS U → IsCountablyIndexed B S hS V →
      (Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS t.hom ↔
        HasPropertyOnAffineChartMap B S hS TopologicalRing.IsCountablyWeaklyAdmissible
          TautChartProperty t))
    (h0AQ0 : ∀ {A A' A'' : FppfSheaf B S hS} (s : A ⟶ A') (r : A' ⟶ A''),
      IsFormalAlgebraicSpace B S hS A → IsFormalAlgebraicSpace B S hS A' →
      IsFormalAlgebraicSpace B S hS A'' →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (s ≫ r).hom →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS s.hom)
    (h0AN4 : ∀ (I : Type (u + 1)) (U W : I → FppfSheaf B S hS) (a : ∀ i, U i ⟶ X)
      (b : ∀ i, W i ⟶ Y) (t : ∀ i, U i ⟶ W i), IsAffineEtaleCover B S hS U a →
      (∀ i, IsAffineFormalAlgebraicSpace B S hS (W i)) →
      (∀ i, Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (b i).hom) →
      (∀ i, Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (t i).hom) →
      (∀ i, a i ≫ f = t i ≫ b i) →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    IsAdicOnEveryAffineEtaleDiagram B S hS f
```

**`AlgebraicGeometry.FormalSpace.isAdicMorphism_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphismConverse.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphismConverse.lean#L250). The attribute's comment: “the equivalence of conditions (1) and (2) of the section for a morphism of locally adic* formal algebraic spaces, together with the footnote reading (2) with taut maps”.

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

**`RingHom.isTaut_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L436). The attribute's comment: “part (1)”.

> A continuous adic homomorphism of linearly topologized rings is taut.

```lean
public theorem isTaut_of_isAdic
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hφ : Continuous φ) (hAdic : RingHom.IsAdic φ) :
    RingHom.IsTaut φ
```

**`RingHom.isAdic_iff_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L467). The attribute's comment: “on WAdm^{adic*}”.

> Adicness and tautness are equivalent for a continuous homomorphism from a linearly
> topologized ring with a finitely generated ideal of definition to a complete separated linearly
> topologized ring. In particular, this applies to morphisms in `WAdm^{adic*}`.

```lean
public theorem isAdic_iff_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hφ : Continuous φ)
    (hA : ∃ I : Ideal A, I.FG ∧ _root_.IsAdic I)
    [@CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)] [T2Space B] :
    RingHom.IsAdic φ ↔ RingHom.IsTaut φ
```

Declarations registered for the tag:

- [`RingHom.isAdic_of_isTaut`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L322), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L461) (StacksFrontier): “part (2)”.
- [`RingHom.isAdic_of_isTaut`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L322), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMapRefined.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMapRefined.lean#L137) (StacksFrontier): “part (2)”.

## Tag 0AQ3, a definition

[Tag 0AQ3](https://stacks.math.columbia.edu/tag/0AQ3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsAdicMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMorphism.lean#L131).

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

**`AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean#L85). The attribute's comment: “the defining condition of an adic morphism”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
