---
declaration: section
origin: cited
lean: exists_simple_submod, exists_simple_submod_algebra, Module.finite_of_simple_tower, Module.End.instDivisionRing, IsSimpleRing.exists_algEquiv_matrix_divisionRing_of_finite, IsSimpleRing.exists_algEquiv_matrix_divisionRing
statement: formalized
proof: formalized
---

# 11.3 Wedderburn's theorem

Section 11.3 of the Stacks Project, [Tag 0744](https://stacks.math.columbia.edu/tag/0744). 2 tags here are carried by 4 declarations of the repository (3 in StacksCore and 1 in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0746, a lemma

[Tag 0746](https://stacks.math.columbia.edu/tag/0746) in the Stacks Project.

**`exists_simple_submod`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Artinian/Module.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Artinian/Module.lean#L27). The attribute's comment: “(2)”.

```lean
lemma exists_simple_submod (A M : Type*) [Ring A] [Nontrivial M] [AddCommGroup M]
    [Module A M] [IsArtinianRing A] : ∃ (p : Submodule A M), IsSimpleModule A p
```

**`exists_simple_submod_algebra`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Artinian/Module.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Artinian/Module.lean#L39). The attribute's comment: “(1)”.

```lean
lemma exists_simple_submod_algebra (A : Type u) [Ring A] [Nontrivial A] [IsArtinianRing A] :
    ∃ (M : Type u) (_ : AddCommGroup M) (_ : Module A M), IsSimpleModule A M
```

**`Module.finite_of_simple_tower`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Artinian/Module.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Artinian/Module.lean#L45). The attribute's comment: “(3)”.

```lean
lemma Module.finite_of_simple_tower (k A M : Type*) [CommSemiring k] [Ring A] [Algebra k A]
    [Module.Finite k A] [AddCommGroup M] [Module A M] [Module k M] [IsScalarTower k A M]
    [IsSimpleModule A M] : Module.Finite k M
```

Declarations registered for the tag:

- [`Module.End.instDivisionRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.End.instDivisionRing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/SimpleModule/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/SimpleModule/Basic.lean#L11) (StacksCore): “(5) part 1”.

## Tag 0747, a theorem

[Tag 0747](https://stacks.math.columbia.edu/tag/0747) in the Stacks Project.

**`IsSimpleRing.exists_algEquiv_matrix_divisionRing_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SimpleModule/WedderburnArtinFinite.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SimpleModule/WedderburnArtinFinite.lean#L30).

> **Wedderburn's theorem**: a simple finite-dimensional algebra `A` over a field `k` is
> isomorphic to a matrix algebra `Mat(n × n, D)`, `n ≥ 1`, over a division algebra `D` which is
> finite-dimensional over `k`.

```lean
theorem exists_algEquiv_matrix_divisionRing_of_finite [IsSimpleRing A] :
    ∃ (n : ℕ) (_ : NeZero n) (D : Type v) (_ : DivisionRing D) (_ : Algebra k D)
      (_ : Module.Finite k D), Nonempty (A ≃ₐ[k] Matrix (Fin n) (Fin n) D)
```

Declarations registered for the tag:

- [`IsSimpleRing.exists_algEquiv_matrix_divisionRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsSimpleRing.exists_algEquiv_matrix_divisionRing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean#L14) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.3, Tag 0744](https://stacks.math.columbia.edu/tag/0744)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
