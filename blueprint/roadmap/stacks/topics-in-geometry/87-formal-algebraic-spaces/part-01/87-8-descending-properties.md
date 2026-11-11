---
declaration: section
origin: cited
lean: TopologicalRing.isCountablyGenerated_nhds_zero_of_isTaut_of_faithfullyFlat_quotient, TopologicalRing.isWeaklyPreAdmissible_of_isTaut_of_faithfullyFlat_quotient, TopologicalRing.isPreAdmissible_of_isTaut_of_faithfullyFlat_quotient, TopologicalRing.isWeaklyPreAdic_of_isTaut_of_faithfullyFlat_quotient, TopologicalRing.exists_fg_ideal_of_definition_of_taut
statement: formalized
proof: formalized
---

# 87.8 Descending properties

Section 87.8 of the Stacks Project, [Tag 0GXK](https://stacks.math.columbia.edu/tag/0GXK). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GXL, a lemma

[Tag 0GXL](https://stacks.math.columbia.edu/tag/0GXL) in the Stacks Project.

**`TopologicalRing.isCountablyGenerated_nhds_zero_of_isTaut_of_faithfullyFlat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean#L74).

> A countable fundamental system of open ideals descends along a continuous taut map
> whose induced maps on quotients by open ideals are faithfully flat.

```lean
public theorem isCountablyGenerated_nhds_zero_of_isTaut_of_faithfullyFlat_quotient
    {A : Type u} {B : Type v} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    (hφ_taut : RingHom.IsTaut φ)
    (hφ_quotient : ∀ (I : Ideal A), IsOpen (I : Set A) →
      (Ideal.quotientMap (Ideal.closure (I.map φ)) φ
        (Ideal.map_le_iff_le_comap.mp (fun _ hx ↦ subset_closure hx))).FaithfullyFlat)
    (hB : (nhds (0 : B)).IsCountablyGenerated) :
    (nhds (0 : A)).IsCountablyGenerated
```

## Tag 0GXM, a lemma

[Tag 0GXM](https://stacks.math.columbia.edu/tag/0GXM) in the Stacks Project.

**`TopologicalRing.isWeaklyPreAdmissible_of_isTaut_of_faithfullyFlat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean#L114).

> Weak pre-admissibility descends along a taut map when the induced
> maps on quotients by open ideals and their closed extensions are faithfully flat.

```lean
public theorem isWeaklyPreAdmissible_of_isTaut_of_faithfullyFlat_quotient
    {A : Type u} {B : Type v} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    (φ : A →+* B)
    (hφ_taut : RingHom.IsTaut φ)
    (hφ_quotient : ∀ I : Ideal A, IsOpen (I : Set A) →
      (Ideal.quotientMap (I := I) (Ideal.closure (I.map φ)) φ (by
        exact Ideal.map_le_iff_le_comap.mp
          (show I.map φ ≤ Ideal.closure (I.map φ) from
            fun _ hx ↦ subset_closure hx))).FaithfullyFlat)
    (hB : TopologicalRing.IsWeaklyPreAdmissible B) :
    TopologicalRing.IsWeaklyPreAdmissible A
```

## Tag 0GXN, a lemma

[Tag 0GXN](https://stacks.math.columbia.edu/tag/0GXN) in the Stacks Project.

**`TopologicalRing.isPreAdmissible_of_isTaut_of_faithfullyFlat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean#L150).

> Pre-admissibility descends along a continuous taut homomorphism when all of the induced maps
> on quotients by open ideals and their closed extensions are faithfully flat.

```lean
public theorem isPreAdmissible_of_isTaut_of_faithfullyFlat_quotient
    {A : Type u} {B : Type v} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ) (hφ_taut : RingHom.IsTaut φ)
    (hφ_quotient : ∀ (I : Ideal A), IsOpen (I : Set A) →
      (Ideal.quotientMap (Ideal.closure (I.map φ)) φ
        (Ideal.map_le_iff_le_comap.mp (fun _ hx ↦ subset_closure hx))).FaithfullyFlat)
    (hB : TopologicalRing.IsPreAdmissible B) :
    TopologicalRing.IsPreAdmissible A
```

## Tag 0GXP, a lemma

[Tag 0GXP](https://stacks.math.columbia.edu/tag/0GXP) in the Stacks Project.

**`TopologicalRing.isWeaklyPreAdic_of_isTaut_of_faithfullyFlat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean#L255).

> Weak pre-adicness descends along a continuous taut homomorphism when all maps on the
> corresponding quotients by open ideals are faithfully flat.

```lean
public theorem isWeaklyPreAdic_of_isTaut_of_faithfullyFlat_quotient
    {A : Type u} {B : Type v} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ) (hφ_taut : RingHom.IsTaut φ)
    (hquot : ∀ I : Ideal A, IsOpen (I : Set A) →
      (Ideal.quotientMap (I := I) (Ideal.closure (I.map φ)) φ (by
        exact Ideal.map_le_iff_le_comap.mp
          (show I.map φ ≤ Ideal.closure (I.map φ) from
            fun _ hx ↦ subset_closure hx))).FaithfullyFlat)
    (hB : TopologicalRing.IsWeaklyPreAdic B) : TopologicalRing.IsWeaklyPreAdic A
```

## Tag 0GXQ, a lemma

[Tag 0GXQ](https://stacks.math.columbia.edu/tag/0GXQ) in the Stacks Project.

**`TopologicalRing.exists_fg_ideal_of_definition_of_taut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Descent.lean#L476).

> Adicness with a finitely generated ideal of definition descends along a continuous taut
> homomorphism when all the induced maps modulo open ideals are faithfully flat.

```lean
public theorem exists_fg_ideal_of_definition_of_taut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [@CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A)] [T2Space A]
    [@CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)] [T2Space B]
    (φ : A →+* B) (_hφ : Continuous φ) (_htaut : RingHom.IsTaut φ)
    (_hquot : ∀ I : Ideal A, IsOpen (I : Set A) →
      (Ideal.quotientMap (Ideal.closure (I.map φ)) φ
        (Ideal.le_comap_of_map_le
          (show I.map φ ≤ Ideal.closure (I.map φ) from subset_closure))).FaithfullyFlat)
    (_hB : ∃ J : Ideal B, _root_.IsAdic J ∧ J.FG) :
    ∃ I : Ideal A, _root_.IsAdic I ∧ I.FG
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.8, Tag 0GXK](https://stacks.math.columbia.edu/tag/0GXK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
