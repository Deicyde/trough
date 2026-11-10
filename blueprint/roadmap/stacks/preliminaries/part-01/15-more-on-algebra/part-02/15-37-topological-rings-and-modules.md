---
declaration: section
origin: cited
lean: TopologicalRing.IsIdealOfDefinition, TopologicalRing.IsPreAdmissible, TopologicalRing.IsAdmissible, TopologicalRing.IsPreAdic, TopologicalRing.IsAdic, TopologicalRing.preAdic_and_adic_iff_admissible_and_open_powers, IsTopologicalRing, TopModuleCat
statement: formalized
proof: formalized
---

# 15.37 Topological rings and modules

Section 15.37 of the Stacks Project, [Tag 07E7](https://stacks.math.columbia.edu/tag/07E7). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07E8, a definition

[Tag 07E8](https://stacks.math.columbia.edu/tag/07E8) in the Stacks Project.

**`TopologicalRing.IsIdealOfDefinition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L91). The attribute's comment: “(4)”.

> An ideal of definition is open and its powers are cofinal among the neighborhoods of zero.

```lean
public def IsIdealOfDefinition {R : Type u} [CommRing R] [TopologicalSpace R]
    (I : Ideal R) : Prop
```

**`TopologicalRing.IsPreAdmissible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L98). The attribute's comment: “(5)”.

> A topological ring is pre-admissible if it has an ideal of definition.

```lean
public def IsPreAdmissible (R : Type u) [CommRing R] [TopologicalSpace R] : Prop
```

**`TopologicalRing.IsAdmissible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L107). The attribute's comment: “(6)”. References: EGA 0 (7.1.2), “admissible”.

> A topological ring is admissible if it is pre-admissible and complete.

```lean
public def IsAdmissible (R : Type u) [CommRing R] [TopologicalSpace R]
    [IsTopologicalRing R] : Prop
```

**`TopologicalRing.IsPreAdic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L114). The attribute's comment: “(7)”.

> A topological ring is pre-adic if an ideal of definition defines its topology through its
> powers.

```lean
public def IsPreAdic (R : Type u) [CommRing R] [TopologicalSpace R] : Prop
```

**`TopologicalRing.IsAdic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L119). The attribute's comment: “(8)”. References: EGA 0 (7.1.9), “preadic (J^n a basis)”.

> A topological ring is adic if it is pre-adic and complete.

```lean
public def IsAdic (R : Type u) [CommRing R] [TopologicalSpace R]
    [IsTopologicalRing R] : Prop
```

**`TopologicalRing.preAdic_and_adic_iff_admissible_and_open_powers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L137). The attribute's comment: “equivalent characterization”.

> A (pre-)adic topological ring is equivalently a (pre-)admissible topological ring possessing
> an ideal of definition all of whose positive powers are open.

```lean
public theorem preAdic_and_adic_iff_admissible_and_open_powers
    {R : Type u} [CommRing R] [TopologicalSpace R]
    [IsTopologicalRing R] [IsLinearTopology R R] :
    (IsPreAdic R ↔ IsPreAdmissible R ∧
      ∃ I : Ideal R, IsIdealOfDefinition I ∧
        ∀ n : ℕ, 1 ≤ n → IsOpen ((I ^ n : Ideal R) : Set R)) ∧
    (IsAdic R ↔ IsAdmissible R ∧
      ∃ I : Ideal R, IsIdealOfDefinition I ∧
        ∀ n : ℕ, 1 ≤ n → IsOpen ((I ^ n : Ideal R) : Set R))
```

Declarations registered for the tag:

- [`IsTopologicalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsTopologicalRing#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L73) (StacksFrontier): “(1), topological rings”.
- [`TopModuleCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L74) (StacksFrontier): “(1), topological modules”.
- [`ContinuousLinearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ContinuousLinearMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L75) (StacksFrontier): “(2), homomorphisms of topological modules”. References: EGA 0 (18.5.3), “partial”; EGA 0 (19.1.1); SGA 3 VIIB (0.2); SGA 3 VIIB (0.2.2); SGA 3 VIIB (0.3.6); SGA 3 VIIB (0.5.B); SGA 3 VIIB (1.3.5.A); SGA 6 II (AppII.3.0.2).
- [`StacksTopologicalRingHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Ring.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L84) (StacksFrontier): “(2), homomorphisms of topological rings”.
- [`IsLinearTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLinearTopology#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L85) (StacksFrontier): “(3), linear topologies”. References: EGA 0 (20.3.1); EGA 0 (7.1.1).
- [`IsTopologicalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsTopologicalRing#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean#L86) (StacksFrontier): “(1), topological rings”.
- [`TopModuleCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean#L87) (StacksFrontier): “(1), topological modules”.
- [`ContinuousLinearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ContinuousLinearMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean#L88) (StacksFrontier): “(2), homomorphisms of topological modules”. References: EGA 0 (18.5.3), “partial”; EGA 0 (19.1.1); SGA 3 VIIB (0.2); SGA 3 VIIB (0.2.2); SGA 3 VIIB (0.3.6); SGA 3 VIIB (0.5.B); SGA 3 VIIB (1.3.5.A); SGA 6 II (AppII.3.0.2).
- [`StacksTopologicalRingHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Ring.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean#L89) (StacksFrontier): “(2), homomorphisms of topological rings”.
- [`IsLinearTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLinearTopology#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRingsRefined.lean#L90) (StacksFrontier): “(3), linear topologies”. References: EGA 0 (20.3.1); EGA 0 (7.1.1).

## Tag 07E9, a lemma

[Tag 07E9](https://stacks.math.columbia.edu/tag/07E9) in the Stacks Project.

**`RingHom.continuous_adic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Continuous.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Continuous.lean#L29).

> A ring homomorphism `φ : R → S` between commutative rings is continuous with respect to the
> `I`-adic topology on `R` and the `J`-adic topology on `S` if and only if there exists `n ≥ 1` with
> `φ(I ^ n) ⊆ J`.

```lean
theorem RingHom.continuous_adic_iff {R S : Type*} [CommRing R] [CommRing S]
    (φ : R →+* S) (I : Ideal R) (J : Ideal S) :
    @Continuous R S I.adicTopology J.adicTopology φ ↔
      ∃ n : ℕ, 1 ≤ n ∧ ∀ x ∈ I ^ n, φ x ∈ J
```

## Tag 0CQU, a lemma

[Tag 0CQU](https://stacks.math.columbia.edu/tag/0CQU) in the Stacks Project.

**`dense_iInter_of_isOpen_of_complete_linearTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/BaireLinearTopology.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/BaireLinearTopology.lean#L77).

> The Baire category theorem for complete linearly topologized abelian groups with a
> countable fundamental system of neighbourhoods of zero.

```lean
public theorem dense_iInter_of_isOpen_of_complete_linearTopology
    {M : Type*} [AddCommGroup M] [TopologicalSpace M] [IsTopologicalAddGroup M]
    [T2Space M] [IsLinearTopology ℤ M]
    (hcomplete : @CompleteSpace M (IsTopologicalAddGroup.rightUniformSpace M))
    (hcount : (nhds (0 : M)).IsCountablyGenerated)
    {U : ℕ → Set M} (hUopen : ∀ n, IsOpen (U n)) (hUdense : ∀ n, Dense (U n)) :
    Dense (⋂ n, U n)
```

## Tag 0CQV, a lemma

[Tag 0CQV](https://stacks.math.columbia.edu/tag/0CQV) in the Stacks Project.

**`exists_isOpen_of_iUnion_eq_univ_of_complete_linearTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/BaireLinearTopology.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/BaireLinearTopology.lean#L112).

> A countable closed-subgroup cover of a complete linearly topologized abelian group contains
> an open subgroup.

```lean
public theorem exists_isOpen_of_iUnion_eq_univ_of_complete_linearTopology
    {M : Type*} [AddCommGroup M] [TopologicalSpace M] [IsTopologicalAddGroup M]
    [T2Space M] [IsLinearTopology ℤ M]
    (hcomplete : @CompleteSpace M (IsTopologicalAddGroup.rightUniformSpace M))
    (hcount : (nhds (0 : M)).IsCountablyGenerated)
    (N : ℕ → AddSubgroup M) (hNclosed : ∀ n, IsClosed (N n : Set M))
    (hNcover : (⋃ n, (N n : Set M)) = Set.univ) :
    ∃ n, IsOpen (N n : Set M)
```

## Tag 0CQW, a lemma

[Tag 0CQW](https://stacks.math.columbia.edu/tag/0CQW) in the Stacks Project.

**`open_mapping_lemma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/OpenMapping.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/OpenMapping.lean#L288).

> Let `u : N → M` be a continuous homomorphism of topological abelian groups. Assume that `M`
> is separated, and that `N` is complete (which, by `IsGroupComplete`, includes separatedness of
> `N`), linearly topologized, and has a countable fundamental system of neighbourhoods of `0`. Then
> exactly one of the following two statements holds:
>
> 1. `u` is open; or
> 2. there exists an open subgroup `N' ⊆ N` such that the image `u(N')` is nowhere dense in `M`.

```lean
theorem open_mapping_lemma
    {N : Type*} [AddCommGroup N] [TopologicalSpace N] [IsTopologicalAddGroup N]
    {M : Type*} [AddCommGroup M] [TopologicalSpace M] [IsTopologicalAddGroup M]
    [T2Space M]
    (u : N →+ M) (hu : Continuous u)
    (hNcomplete : IsGroupComplete N)
    (hNlin : IsLinearlyTopologized N)
    (hNcount : HasCountableFundamentalSystem N) :
    Xor (IsOpenMap u)
      (∃ N' : AddSubgroup N, IsOpen (N' : Set N) ∧ IsNowhereDense (u '' (N' : Set N)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.37, Tag 07E7](https://stacks.math.columbia.edu/tag/07E7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
