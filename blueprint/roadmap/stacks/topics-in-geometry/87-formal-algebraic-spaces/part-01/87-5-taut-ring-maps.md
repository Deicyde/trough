---
declaration: section
origin: cited
lean: RingHom.IsTaut, RingHom.isTaut_iff_hasBasis_isWeakIdealOfDefinition, RingHom.isTaut_completion, RingHom.isTaut_comp, RingHom.isTaut_of_comp, RingHom.isTaut_completedTensorProduct_baseChange, RingHom.isCountablyGenerated_nhds_zero_of_isTaut, RingHom.isWeaklyPreAdmissible_of_isTaut
statement: formalized
proof: formalized
---

# 87.5 Taut ring maps

Section 87.5 of the Stacks Project, [Tag 0GX1](https://stacks.math.columbia.edu/tag/0GX1). 10 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AMX, a definition

[Tag 0AMX](https://stacks.math.columbia.edu/tag/0AMX) in the Stacks Project.

**`RingHom.IsTaut`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L53).

> A ring homomorphism is *taut* if the closure of the extension of each open source ideal is
> open, and the resulting closed extended ideals form a neighbourhood basis of zero in the target.
>
> For the Stacks definition, the source and target are linearly topologized rings and the
> homomorphism is continuous; those ambient hypotheses are imposed by statements using this
> predicate.

```lean
public abbrev IsTaut {A B : Type*} [CommRing A] [TopologicalSpace A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] (φ : A →+* B) : Prop
```

## Tag 0AMY, a lemma

[Tag 0AMY](https://stacks.math.columbia.edu/tag/0AMY) in the Stacks Project.

**`RingHom.isTaut_iff_hasBasis_isWeakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L80).

> A continuous homomorphism of weakly admissible topological rings is taut exactly when the
> closed extensions of the weak ideals of definition are weak ideals of definition and form a
> neighbourhood basis of zero in the target.

```lean
public theorem isTaut_iff_hasBasis_isWeakIdealOfDefinition
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hB : TopologicalRing.IsWeaklyAdmissible B) :
    RingHom.IsTaut φ ↔
      (∀ I : Ideal A, TopologicalRing.IsWeakIdealOfDefinition I →
        TopologicalRing.IsWeakIdealOfDefinition (Ideal.closure (I.map φ))) ∧
      (nhds (0 : B)).HasBasis
        (fun I : Ideal A ↦ TopologicalRing.IsWeakIdealOfDefinition I)
        (fun I : Ideal A ↦ (Ideal.closure (I.map φ) : Set B))
```

## Tag 0GX2, a lemma

[Tag 0GX2](https://stacks.math.columbia.edu/tag/0GX2) in the Stacks Project.

**`RingHom.isTaut_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L352).

> The canonical map from a linearly topologized ring to its completion is taut.

```lean
public theorem isTaut_completion {A : Type*} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] :
    letI : UniformSpace A := IsTopologicalAddGroup.rightUniformSpace A
    letI : IsUniformAddGroup A := isUniformAddGroup_of_addCommGroup
    RingHom.IsTaut (UniformSpace.Completion.coeRingHom :
      A →+* UniformSpace.Completion A)
```

## Tag 0GX3, a lemma

[Tag 0GX3](https://stacks.math.columbia.edu/tag/0GX3) in the Stacks Project.

**`RingHom.isTaut_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L400).

> The composite of continuous taut homomorphisms of linearly topologized rings is taut.

```lean
public lemma isTaut_comp {A B C : Type*}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing C] [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (φ : A →+* B) (ψ : B →+* C) (hφ : Continuous φ) (hψ : Continuous ψ)
    (hφ_taut : RingHom.IsTaut φ) (hψ_taut : RingHom.IsTaut ψ) :
    RingHom.IsTaut (ψ.comp φ)
```

## Tag 0GX4, a lemma

[Tag 0GX4](https://stacks.math.columbia.edu/tag/0GX4) in the Stacks Project.

**`RingHom.isTaut_of_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L434).

> If a composite of two continuous ring homomorphisms is taut, then its second
> map is taut.

```lean
public lemma isTaut_of_comp {A B C : Type*}
    [CommRing A] [TopologicalSpace A]
    [CommRing B] [TopologicalSpace B]
    [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    (φ : A →+* B) (ψ : B →+* C) (hφ : Continuous φ) (hψ : Continuous ψ)
    (hcomp : RingHom.IsTaut (ψ.comp φ)) : RingHom.IsTaut ψ
```

## Tag 0GX5, a lemma

[Tag 0GX5](https://stacks.math.columbia.edu/tag/0GX5) in the Stacks Project.

**`RingHom.isTaut_completedTensorProduct_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautTensor.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautTensor.lean#L115).

> Completed tensor-product base change preserves a taut homomorphism.

```lean
public lemma isTaut_completedTensorProduct_baseChange
    {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (_hB : Continuous (algebraMap A B)) (hC : Continuous (algebraMap A C))
    (hTaut : RingHom.IsTaut (algebraMap A B)) :
    letI : Algebra C (B ⊗[A] C) := Algebra.TensorProduct.rightAlgebra
    RingHom.IsTaut
      (algebraMap C (TopologicalRing.CompletedTensorProduct (R := A) (M := B) (N := C)))
```

## Tag 0GX6, a lemma

[Tag 0GX6](https://stacks.math.columbia.edu/tag/0GX6) in the Stacks Project.

**`RingHom.isCountablyGenerated_nhds_zero_of_isTaut`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L467).

> The target of a taut continuous homomorphism of linearly topologized rings has a countable
> fundamental system of open ideals if the source does.

```lean
public lemma isCountablyGenerated_nhds_zero_of_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    (hφ_taut : RingHom.IsTaut φ) (hA : (nhds (0 : A)).IsCountablyGenerated) :
    (nhds (0 : B)).IsCountablyGenerated
```

## Tag 0GX7, a lemma

[Tag 0GX7](https://stacks.math.columbia.edu/tag/0GX7) in the Stacks Project.

**`RingHom.isWeaklyPreAdmissible_of_isTaut`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L489).

> Weak pre-admissibility ascends along a continuous taut homomorphism of
> linearly topologized rings.

```lean
public lemma isWeaklyPreAdmissible_of_isTaut
    {A B : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    (hφ_taut : RingHom.IsTaut φ) (hA : TopologicalRing.IsWeaklyPreAdmissible A) :
    TopologicalRing.IsWeaklyPreAdmissible B
```

## Tag 0GX8, a lemma

[Tag 0GX8](https://stacks.math.columbia.edu/tag/0GX8) in the Stacks Project.

**`RingHom.isPreAdmissible_of_isTaut`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L525).

> Pre-admissibility ascends along a continuous taut homomorphism of linearly topologized
> rings.

```lean
public lemma isPreAdmissible_of_isTaut {A : Type u} {B : Type v} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] (φ : A →+* B) (hφ : Continuous φ)
    (hφ_taut : RingHom.IsTaut φ) (hA : TopologicalRing.IsPreAdmissible A) :
    TopologicalRing.IsPreAdmissible B
```

## Tag 0APT, a lemma

[Tag 0APT](https://stacks.math.columbia.edu/tag/0APT) in the Stacks Project.

**`RingHom.isOpenMap_of_isTaut_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L284). The attribute's comment: “openness”.

> A continuous taut map with dense image from a complete countably based linearly
> topologized ring to a separated linearly topologized ring is open.

```lean
public lemma isOpenMap_of_isTaut_of_denseRange (φ : A →+* B) (hφ : Continuous φ)
    (hA : @CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A))
    (hcount : (nhds (0 : A)).IsCountablyGenerated) (htaut : RingHom.IsTaut φ)
    (hdense : DenseRange φ) : IsOpenMap φ
```

**`RingHom.surjective_of_isTaut_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L293). The attribute's comment: “surjectivity”.

> A continuous taut map with dense image under the completeness and countability hypotheses
> is surjective.

```lean
public lemma surjective_of_isTaut_of_denseRange (φ : A →+* B) (hφ : Continuous φ)
    (hA : @CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A))
    (hcount : (nhds (0 : A)).IsCountablyGenerated) (htaut : RingHom.IsTaut φ)
    (hdense : DenseRange φ) : Function.Surjective φ
```

**`RingHom.completeSpace_of_isTaut_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L309). The attribute's comment: “completeness of the target”.

> The separated target of a continuous taut dense map from a complete countably based
> linearly topologized ring is complete.

```lean
public lemma completeSpace_of_isTaut_of_denseRange (φ : A →+* B) (hφ : Continuous φ)
    (hA : @CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A))
    (hcount : (nhds (0 : A)).IsCountablyGenerated) (htaut : RingHom.IsTaut φ)
    (hdense : DenseRange φ) :
    @CompleteSpace B (IsTopologicalAddGroup.rightUniformSpace B)
```

**`RingHom.isClosed_ker_of_continuous`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L323). The attribute's comment: “closed kernel”.

> The kernel of a continuous ring homomorphism into a space with closed points is closed.

```lean
public lemma isClosed_ker_of_continuous {R S : Type*} [CommRing R] [TopologicalSpace R]
    [CommRing S] [TopologicalSpace S] [T1Space S] (φ : R →+* S) (hφ : Continuous φ) :
    IsClosed (RingHom.ker φ : Set R)
```

**`RingHom.quotientKerEquiv_of_isTaut_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/Taut.lean#L332). The attribute's comment: “quotient presentation”.

> The canonical map from the quotient by the kernel to the target is a homeomorphic ring
> equivalence.

```lean
public lemma quotientKerEquiv_of_isTaut_of_denseRange (φ : A →+* B) (hφ : Continuous φ)
    (hA : @CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A))
    (hcount : (nhds (0 : A)).IsCountablyGenerated) (htaut : RingHom.IsTaut φ)
    (hdense : DenseRange φ) :
    ∃ e : (A ⧸ RingHom.ker φ) ≃+* B,
      (∀ a : A, e (Ideal.Quotient.mk (RingHom.ker φ) a) = φ a) ∧ IsHomeomorph e
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.5, Tag 0GX1](https://stacks.math.columbia.edu/tag/0GX1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
