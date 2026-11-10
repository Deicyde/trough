---
declaration: section
origin: cited
lean: DifferentialGradedAlgebra, DifferentialGradedAlgebra.Hom, DifferentialGraded.IsGradedCommutative, DifferentialGraded.IsStrictlyGradedCommutative, DifferentialGradedAlgebra.tensorProductGrading, DifferentialGradedAlgebra.tensorProductDifferential, DifferentialGradedAlgebra.gradedTensorProduct, DifferentialGradedAlgebra.tensorProduct
statement: formalized
proof: formalized
---

# 22.3 Differential graded algebras

Section 22.3 of the Stacks Project, [Tag 061U](https://stacks.math.columbia.edu/tag/061U). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 061V, a definition

[Tag 061V](https://stacks.math.columbia.edu/tag/061V) in the Stacks Project.

Declarations registered for the tag:

- [`DifferentialGradedAlgebra`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/Abelian/Basic.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean#L89) (StacksFrontier): “differential graded algebras”.

## Tag 061X, a definition

[Tag 061X](https://stacks.math.columbia.edu/tag/061X) in the Stacks Project.

Declarations registered for the tag:

- [`DifferentialGradedAlgebra.Hom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean#L44), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean#L90) (StacksFrontier): “homomorphisms of differential graded algebras”.

## Tag 061W, a definition

[Tag 061W](https://stacks.math.columbia.edu/tag/061W) in the Stacks Project.

**`DifferentialGraded.IsGradedCommutative`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/GradedCommutative.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/GradedCommutative.lean#L49). The attribute's comment: “commutativity”.

> A grading on a ring is *graded-commutative* when two homogeneous elements
> commute unless both degrees are odd, in which case they anticommute.

```lean
public class IsGradedCommutative {ι : Type w} [Semiring ι]
    [DecidablePred (Odd : ι → Prop)] {A : Type u} [Ring A]
    {S : Type v} [Membership A S] (𝒜 : ι → S) : Prop
```

**`DifferentialGraded.IsStrictlyGradedCommutative`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/GradedCommutative.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/GradedCommutative.lean#L59). The attribute's comment: “strict commutativity”. References: SGA 6 VII (2.1).

> A grading is *strictly graded-commutative* when it is graded-commutative and
> every homogeneous element of odd degree has square zero.

```lean
public class IsStrictlyGradedCommutative {ι : Type w} [Semiring ι]
    [DecidablePred (Odd : ι → Prop)] {A : Type u} [Ring A]
    {S : Type v} [Membership A S] (𝒜 : ι → S) extends IsGradedCommutative 𝒜
```

## Tag 065W, a definition

[Tag 065W](https://stacks.math.columbia.edu/tag/065W) in the Stacks Project.

**`DifferentialGradedAlgebra.tensorProductGrading`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L73). The attribute's comment: “the total grading”.

> The degree-`n` part is spanned by pure tensors whose factors have degrees
> adding to `n`.

```lean
public noncomputable def tensorProductGrading (n : ℤ) :
    Submodule R (A.grading ᵍ⊗[R] B.grading)
```

**`DifferentialGradedAlgebra.tensorProductDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L86). The attribute's comment: “the signed differential”. References: SGA 4 XVII (1.1.10), “(i)”.

> The signed tensor differential `d_A ⊗ 1 + (-1)^deg ⊗ d_B`.

```lean
public noncomputable def tensorProductDifferential :
    (A.grading ᵍ⊗[R] B.grading) →ₗ[R] (A.grading ᵍ⊗[R] B.grading)
```

**`DifferentialGradedAlgebra.gradedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L567). The attribute's comment: “the differential graded algebra construction”.

> The tensor product differential graded algebra with the specified carrier,
> total grading, Koszul multiplication, and signed differential.

```lean
public noncomputable def gradedTensorProduct : TensorProductData A B
```

**`DifferentialGradedAlgebra.tensorProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 575](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L575). The attribute's comment: “the coefficient differential graded algebra”. References: SGA 4 XVII (1.1.10), “(i)”.

> The tensor product as a coefficient algebra for differential graded modules.

```lean
public noncomputable abbrev tensorProduct : DifferentialGradedAlgebra R
```

**`DifferentialGradedAlgebra.tmul_mem_grading`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L580). The attribute's comment: “the degree of a pure tensor”.

> A pure tensor of elements in degrees `p` and `q` has degree `p + q`.

```lean
public lemma tmul_mem_grading (p q : ℤ) (a : A.A) (b : B.A)
    (ha : a ∈ A.grading p) (hb : b ∈ B.grading q) :
    (a ᵍ⊗ₜ[R] b : A.grading ᵍ⊗[R] B.grading) ∈
      (tensorProduct A B).grading (p + q)
```

**`DifferentialGradedAlgebra.tensorProductDifferential_tmul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L589). The attribute's comment: “the homogeneous differential formula”.

> On a pure tensor whose first factor has degree `p`, the tensor-product
> differential is `d a ⊗ₜ b + (-1)^p • (a ⊗ₜ d b)`.

```lean
public lemma tensorProductDifferential_tmul (p : ℤ) (a : A.grading p) (b : B.A) :
    (tensorProduct A B).d (((a : A.A) ᵍ⊗ₜ[R] b : A.grading ᵍ⊗[R] B.grading)) =
      (A.d a ᵍ⊗ₜ[R] b : A.grading ᵍ⊗[R] B.grading) +
        (p.negOnePow : ℤ) • ((a : A.A) ᵍ⊗ₜ[R] B.d b)
```

Declarations registered for the tag:

- [`GradedTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=GradedTensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L63) (StacksFrontier): “the Koszul-signed underlying algebra”. References: SGA 7 XII (1.9).
- [`GradedTensorProduct.of`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=GradedTensorProduct.of#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L65) (StacksFrontier): “the underlying module identification”.
- [`GradedTensorProduct.tmul_coe_mul_coe_tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=GradedTensorProduct.tmul_coe_mul_coe_tmul#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProduct.lean#L66) (StacksFrontier): “the homogeneous multiplication formula”. References: SGA 7 XII (1.9), “more general”.

## Tag 065X, a lemma

[Tag 065X](https://stacks.math.columbia.edu/tag/065X) in the Stacks Project.

**`DifferentialGradedAlgebra.totSummandMap_tmul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProductTotalComplex.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProductTotalComplex.lean#L93). The attribute's comment: “the identification on a homogeneous pure tensor”.

> On a pure tensor of homogeneous elements the summand map is `a ⊗ b ↦ a ⊗ b`.

```lean
lemma totSummandMap_tmul (p q n : ℤ) (h : p + q = n)
    (a : A.grading p) (b : B.grading q) :
    ((totSummandMap A B p q n h (a ⊗ₜ[R] b) : tensorProductGrading A B n) :
      A.grading ᵍ⊗[R] B.grading) = (a : A.A) ᵍ⊗ₜ[R] (b : B.A)
```

**`DifferentialGradedAlgebra.tensorToCochainComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/TensorProductTotalComplex.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/TensorProductTotalComplex.lean#L228).

> **Stacks Tag 065X.** For differential graded algebras `(A, d)` and `(B, d)` over a
> commutative ring `R`, the cochain complex of `R`-modules underlying `A ⊗_R B` is the total
> complex of the double complex `A^• ⊗_R B^•`.

```lean
noncomputable def tensorToCochainComplexIso :
    toCochainComplex (tensorProduct A B) ≅
      HomologicalComplex.tensorObj (toCochainComplex A) (toCochainComplex B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.3, Tag 061U](https://stacks.math.columbia.edu/tag/061U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
