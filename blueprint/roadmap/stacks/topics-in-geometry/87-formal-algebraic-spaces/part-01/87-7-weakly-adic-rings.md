---
declaration: section
origin: cited
lean: TopologicalRing.IsWeaklyPreAdic, TopologicalRing.IsWeaklyAdic, TopologicalRing.weaklyPreAdic_tfae, TopologicalRing.isLinearTopology_completion, TopologicalRing.isWeaklyAdic_completion, TopologicalRing.isAdmissible_of_isWeaklyAdic, TopologicalRing.exists_countable_basis_open_ideals, TopologicalRing.exists_fg_isAdic_of_fg_closure_powers_basis
statement: formalized
proof: formalized
---

# 87.7 Weakly adic rings

Section 87.7 of the Stacks Project, [Tag 0GXD](https://stacks.math.columbia.edu/tag/0GXD). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GXE, a definition

[Tag 0GXE](https://stacks.math.columbia.edu/tag/0GXE) in the Stacks Project.

**`TopologicalRing.IsWeaklyPreAdic`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L46). The attribute's comment: “part (1)”.

> A linearly topologized ring is *weakly pre-adic* if the closures of the powers of some
> ideal are open and form a neighborhood basis at zero.

```lean
public class IsWeaklyPreAdic (A : Type*) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] : Prop
```

**`TopologicalRing.IsWeaklyAdic`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L55). The attribute's comment: “part (2)”.

> A linearly topologized ring is *weakly adic* if it is weakly pre-adic, complete, and
> separated. Completeness uses the canonical uniformity of its additive topological group.

```lean
public class IsWeaklyAdic (A : Type*) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] : Prop extends IsWeaklyPreAdic A, T2Space A
```

## Tag 0GXF, a lemma

[Tag 0GXF](https://stacks.math.columbia.edu/tag/0GXF) in the Stacks Project.

**`TopologicalRing.weaklyPreAdic_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L118). The attribute's comment: “weakly\_pre\_adic\_characterizations”.

> The four equivalent characterizations of a weakly pre-adic linearly topologized ring.

```lean
public lemma weaklyPreAdic_tfae (A : Type u) [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] :
    List.TFAE
      [ TopologicalRing.IsWeaklyPreAdic A,
        HasTautPreAdicSource.{u, max u v} A,
        TopologicalRing.IsPreAdmissible A ∧
          ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧
            (∀ n : ℕ, 1 ≤ n → IsOpen ((I ^ n).topologicalClosure : Set A)),
        TopologicalRing.IsPreAdmissible A ∧
          (∀ I : Ideal A, TopologicalRing.IsIdealOfDefinition I →
            ∀ n : ℕ, 1 ≤ n → IsOpen ((I ^ n).topologicalClosure : Set A)) ]
```

**`TopologicalRing.isLinearTopology_completion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L284). The attribute's comment: “completion\_weakly\_adic”.

> Completion preserves the linear topology of a linearly topologized ring.

```lean
public instance isLinearTopology_completion (A : Type*) [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] :
    letI : UniformSpace A := IsTopologicalAddGroup.rightUniformSpace A
    letI : IsUniformAddGroup A := isUniformAddGroup_of_addCommGroup
    IsLinearTopology (UniformSpace.Completion A) (UniformSpace.Completion A)
```

**`TopologicalRing.isWeaklyAdic_completion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L295). The attribute's comment: “completion\_weakly\_adic”.

> The completion of a weakly pre-adic linearly topologized ring is weakly adic.

```lean
public instance isWeaklyAdic_completion (A : Type*) [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] [TopologicalRing.IsWeaklyPreAdic A] :
    letI : UniformSpace A := IsTopologicalAddGroup.rightUniformSpace A
    letI : IsUniformAddGroup A := isUniformAddGroup_of_addCommGroup
    TopologicalRing.IsWeaklyAdic (UniformSpace.Completion A)
```

**`TopologicalRing.isAdmissible_of_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L354). The attribute's comment: “weakly\_adic\_admissible”.

> A weakly adic linearly topologized ring is admissible.

```lean
public theorem isAdmissible_of_isWeaklyAdic (A : Type*) [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalRing.IsWeaklyAdic A] : TopologicalRing.IsAdmissible A
```

**`TopologicalRing.exists_countable_basis_open_ideals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L371). The attribute's comment: “weakly\_adic\_countable\_basis”.

> A weakly adic linearly topologized ring has a countable fundamental system of open
> ideals.

```lean
public theorem exists_countable_basis_open_ideals (A : Type*) [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalRing.IsWeaklyAdic A] :
    ∃ I : ℕ → Ideal A, (∀ n : ℕ, IsOpen (I n : Set A)) ∧
      (𝓝 (0 : A)).HasBasis (fun _ : ℕ ↦ True) (fun n ↦ (I n : Set A))
```

## Tag 0GXG, a lemma

[Tag 0GXG](https://stacks.math.columbia.edu/tag/0GXG) in the Stacks Project.

**`TopologicalRing.exists_fg_isAdic_of_fg_closure_powers_basis`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L641).

> A complete linearly topologized ring whose topology is the fundamental system given by the
> closures of the powers of a finitely generated ideal is adic with a finitely generated ideal of
> definition.

```lean
public lemma exists_fg_isAdic_of_fg_closure_powers_basis
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [T2Space A]
    [hcomplete : @CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A)]
    (I : Ideal A) (hIfg : I.FG)
    (hopen : ∀ n : ℕ, IsOpen ((I ^ n).topologicalClosure : Set A))
    (hbasis : (𝓝 (0 : A)).HasBasis (fun _ : ℕ ↦ True)
      (fun n ↦ ((I ^ n).topologicalClosure : Set A))) :
    ∃ J : Ideal A, J.FG ∧ _root_.IsAdic J
```

## Tag 0GXH, a lemma

[Tag 0GXH](https://stacks.math.columbia.edu/tag/0GXH) in the Stacks Project.

**`TopologicalRing.exists_fg_isAdic_of_quotient_closure_sq_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L701).

> A weakly adic ring with an ideal of definition `I` for which
> `I / closure(I ^ 2)` is finite has a finitely generated ideal defining its topology.

```lean
public lemma exists_fg_isAdic_of_quotient_closure_sq_finite
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [TopologicalRing.IsWeaklyAdic A]
    (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I)
    [Module.Finite A
      (I ⧸ Submodule.comap I.subtype (I ^ 2).topologicalClosure)] :
    ∃ J : Ideal A, J.FG ∧ _root_.IsAdic J
```

## Tag 0GXI, a lemma

[Tag 0GXI](https://stacks.math.columbia.edu/tag/0GXI) in the Stacks Project.

**`TopologicalRing.isWeaklyPreAdic_of_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L724).

> The target of a continuous taut homomorphism from a weakly pre-adic linearly topologized
> ring is weakly pre-adic.

```lean
public theorem isWeaklyPreAdic_of_isTaut {A B : Type*} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    [TopologicalRing.IsWeaklyPreAdic A] (hφ_taut : RingHom.IsTaut φ) :
    TopologicalRing.IsWeaklyPreAdic B
```

## Tag 0GXJ, a lemma

[Tag 0GXJ](https://stacks.math.columbia.edu/tag/0GXJ) in the Stacks Project.

**`TopologicalRing.completedTensorProduct_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdic.lean#L778).

> The completed tensor product of weakly pre-adic linearly topologized rings
> over a commutative ring is weakly adic.

```lean
public theorem completedTensorProduct_isWeaklyAdic
    {B A C : Type*} [CommRing B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra B A] [Algebra B C]
    (hA : TopologicalRing.IsWeaklyPreAdic A) (hC : TopologicalRing.IsWeaklyPreAdic C) :
    TopologicalRing.IsWeaklyAdic
      (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.7, Tag 0GXD](https://stacks.math.columbia.edu/tag/0GXD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
