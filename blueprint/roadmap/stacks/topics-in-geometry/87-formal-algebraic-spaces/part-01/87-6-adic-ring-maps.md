---
declaration: section
origin: cited
lean: RingHom.IsAdic, RingHom.isAdic_comp, RingHom.isAdic_of_comp, RingHom.isTaut_of_isAdic, RingHom.exists_fg_ideal_isAdic_of_isTaut, RingHom.isAdic_of_isTaut
statement: formalized
proof: formalized
---

# 87.6 Adic ring maps

Section 87.6 of the Stacks Project, [Tag 0GX9](https://stacks.math.columbia.edu/tag/0GX9). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GBR, a definition

[Tag 0GBR](https://stacks.math.columbia.edu/tag/0GBR) in the Stacks Project.

**`RingHom.IsAdic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L44).

> A ring homomorphism `φ : A →+* B` is adic if some ideal defining the
> topology of `A` extends along `φ` to an ideal defining the topology of `B`.

```lean
public abbrev IsAdic {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [TopologicalSpace B] (φ : A →+* B) : Prop
```

## Tag 0GXA, a lemma

[Tag 0GXA](https://stacks.math.columbia.edu/tag/0GXA) in the Stacks Project.

**`RingHom.isAdic_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L362).

> The composite of two continuous adic ring homomorphisms is adic.

```lean
public theorem isAdic_comp {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    [TopologicalSpace A] [TopologicalSpace B] [TopologicalSpace C]
    (f : A →+* B) (g : B →+* C) (hf : RingHom.IsAdic f)
    (hg : RingHom.IsAdic g) :
    RingHom.IsAdic (g.comp f)
```

## Tag 0GXB, a lemma

[Tag 0GXB](https://stacks.math.columbia.edu/tag/0GXB) in the Stacks Project.

**`RingHom.isAdic_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L383).

> If a composite of continuous ring homomorphisms is adic and the middle ring is
> pre-adic, then the second homomorphism is adic.

```lean
public theorem isAdic_of_comp {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    [TopologicalSpace A] [TopologicalSpace B] [TopologicalSpace C]
    (f : A →+* B) (g : B →+* C) (hf_continuous : Continuous f)
    (hg_continuous : Continuous g) (hB : TopologicalRing.IsPreAdic B)
    (hgf : RingHom.IsAdic (g.comp f)) :
    RingHom.IsAdic g
```

## Tag 0GXC, a lemma

[Tag 0GXC](https://stacks.math.columbia.edu/tag/0GXC) in the Stacks Project.

**`RingHom.isTaut_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L435). The attribute's comment: “adic implies taut”.

> A continuous adic homomorphism of linearly topologized rings is taut.

```lean
public theorem isTaut_of_isAdic
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hAdic : RingHom.IsAdic φ) :
    RingHom.IsTaut φ
```

## Tag 0APU, a lemma

[Tag 0APU](https://stacks.math.columbia.edu/tag/0APU) in the Stacks Project.

**`RingHom.exists_fg_ideal_isAdic_of_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L306). The attribute's comment: “the target is adic with a finitely generated ideal of definition”.

> The target of a taut continuous homomorphism from a pre-adic ring with a finitely generated
> ideal of definition is itself adic with a finitely generated ideal of definition, provided that
> the target is complete.

```lean
public theorem exists_fg_ideal_isAdic_of_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hTaut : RingHom.IsTaut φ)
    (hA : ∃ I : Ideal A, I.FG ∧ _root_.IsAdic I)
    [@CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)] [T2Space B] :
    ∃ J : Ideal B, J.FG ∧ _root_.IsAdic J
```

**`RingHom.isAdic_of_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdicRingMap.lean#L322). The attribute's comment: “the homomorphism is adic”.

> A taut continuous homomorphism from a pre-adic ring with a finitely generated ideal of
> definition to a complete linearly topologized ring is adic.

```lean
public theorem isAdic_of_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B]
    (φ : A →+* B) (hTaut : RingHom.IsTaut φ)
    (hA : ∃ I : Ideal A, I.FG ∧ _root_.IsAdic I)
    [@CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)] [T2Space B] :
    RingHom.IsAdic φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.6, Tag 0GX9](https://stacks.math.columbia.edu/tag/0GX9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
