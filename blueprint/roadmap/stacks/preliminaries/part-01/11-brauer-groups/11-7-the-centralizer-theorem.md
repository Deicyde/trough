---
declaration: section
origin: cited
lean: Subalgebra.centralizer_isSimple, Subalgebra.finrank_centralizer_mul_finrank, Subalgebra.centralizer_centralizer, Subalgebra.tensorCentralizerEquiv, Subalgebra.maximal_comm_iff_self_centralizer, Subalgebra.isMaximal_comm_iff_finrank
statement: formalized
proof: formalized
---

# 11.7 The centralizer theorem

Section 11.7 of the Stacks Project, [Tag 074S](https://stacks.math.columbia.edu/tag/074S). 4 tags here are carried by 7 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 074T, a theorem

[Tag 074T](https://stacks.math.columbia.edu/tag/074T) in the Stacks Project.

**`Subalgebra.centralizer_isSimple`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L154). The attribute's comment: “first part”.

> The centralizer of a simple subalgebra of a finite-dimensional central simple algebra is
> simple.

```lean
theorem Subalgebra.centralizer_isSimple [FiniteDimensional F A] (B : Subalgebra F A)
    [IsSimpleRing B] :
    IsSimpleRing (Subalgebra.centralizer F (B : Set A))
```

**`Subalgebra.finrank_centralizer_mul_finrank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L170). The attribute's comment: “second part”.

> The dimension of the centralizer of a simple subalgebra `B` of a finite-dimensional
> central simple algebra `A` satisfies `dim C_A(B) * dim B = dim A`.

```lean
theorem Subalgebra.finrank_centralizer_mul_finrank [FiniteDimensional F A]
    (B : Subalgebra F A) [IsSimpleRing B] :
    Module.finrank F (Subalgebra.centralizer F (B : Set A)) * Module.finrank F B =
      Module.finrank F A
```

**`Subalgebra.centralizer_centralizer`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L186). The attribute's comment: “third part”.

> The double centralizer theorem: in a finite-dimensional central simple algebra `A`, the
> centralizer of the centralizer of a simple subalgebra `B` is `B` itself.

```lean
theorem Subalgebra.centralizer_centralizer [FiniteDimensional F A] (B : Subalgebra F A)
    [IsSimpleRing B] :
    Subalgebra.centralizer F (Subalgebra.centralizer F (B : Set A) : Set A) = B
```

## Tag 074U, a lemma

[Tag 074U](https://stacks.math.columbia.edu/tag/074U) in the Stacks Project.

**`Subalgebra.tensorCentralizerEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L201).

> A finite-dimensional central simple algebra decomposes as the tensor product of any
> central simple subalgebra and its centralizer.

```lean
noncomputable def Subalgebra.tensorCentralizerEquiv [FiniteDimensional F A]
    (B : Subalgebra F A) [IsSimpleRing B] [Algebra.IsCentral F B] :
    A ≃ₐ[F] B ⊗[F] Subalgebra.centralizer F (B : Set A)
```

## Tag 074V, a lemma

[Tag 074V](https://stacks.math.columbia.edu/tag/074V) in the Stacks Project.

**`Subalgebra.maximal_comm_iff_self_centralizer`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Algebra/Subalgebra/Lattice.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Algebra/Subalgebra/Lattice.lean#L44). The attribute's comment: “(ii) ↔ (iii)”.

```lean
lemma Subalgebra.maximal_comm_iff_self_centralizer (L : Subalgebra k A) :
    Maximal (fun S : Subalgebra k A ↦ IsMulCommutative S) L ↔
      Subalgebra.centralizer k L = L
```

**`Subalgebra.isMaximal_comm_iff_finrank`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L212). The attribute's comment: “(ii) ↔ (i)”.

```lean
lemma Subalgebra.isMaximal_comm_iff_finrank [Module.Finite F A] (L : Subalgebra F A)
    [IsMulCommutative L] [IsSimpleRing L] :
    Subalgebra.centralizer F (L : Set A) = L ↔
      Module.finrank F A = Module.finrank F L * Module.finrank F L
```

## Tag 074W, a lemma

[Tag 074W](https://stacks.math.columbia.edu/tag/074W) in the Stacks Project.

**`Subalgebra.isMaximal_comm_iff_finrank`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleRing/Centralizer.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Centralizer.lean#L212).

```lean
lemma Subalgebra.isMaximal_comm_iff_finrank [Module.Finite F A] (L : Subalgebra F A)
    [IsMulCommutative L] [IsSimpleRing L] :
    Subalgebra.centralizer F (L : Set A) = L ↔
      Module.finrank F A = Module.finrank F L * Module.finrank F L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.7, Tag 074S](https://stacks.math.columbia.edu/tag/074S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
