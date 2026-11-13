---
declaration: section
origin: cited
lean: isAlgClosed_iff_forall_algebraMap_surjective, IsAlgClosed.algebraMap_bijective_of_isIntegral, IsAlgClosed.tfae, exists_isAlgClosure
statement: formalized
proof: formalized
---

# 9.10 Algebraic closure

Section 9.10 of the Stacks Project, [Tag 09GP](https://stacks.math.columbia.edu/tag/09GP). 3 tags here are carried by 4 declarations of the repository (3 in StacksCore and 1 in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09GQ, a definition

[Tag 09GQ](https://stacks.math.columbia.edu/tag/09GQ) in the Stacks Project.

**`isAlgClosed_iff_forall_algebraMap_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L25). The attribute's comment: “Equivalence between Stacks' definition and mathlib's”.

> **Stacks 09GQ** (equivalence between Stacks' definition and mathlib's), **Stacks 09GR**
> (condition (4) ⇔ (1)).
> A field `K` is algebraically closed iff for every algebraic field extension `L/K` the
> structure map `K → L` is surjective, i.e. `K` has no proper algebraic extension.

```lean
theorem isAlgClosed_iff_forall_algebraMap_surjective (K : Type u) [Field K] :
    IsAlgClosed K ↔ ∀ (L : Type u) [Field L] [Algebra K L] [Algebra.IsAlgebraic K L],
      (⇑(algebraMap K L)).Surjective
```

Declarations registered for the tag:

- [`IsAlgClosed.algebraMap_bijective_of_isIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsAlgClosed.algebraMap_bijective_of_isIntegral#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L14) (StacksCore): “Universe polymorphic version”.

## Tag 09GR, a lemma

[Tag 09GR](https://stacks.math.columbia.edu/tag/09GR) in the Stacks Project.

**`isAlgClosed_iff_forall_algebraMap_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L25). The attribute's comment: “(4) ⇔ (1)”.

> **Stacks 09GQ** (equivalence between Stacks' definition and mathlib's), **Stacks 09GR**
> (condition (4) ⇔ (1)).
> A field `K` is algebraically closed iff for every algebraic field extension `L/K` the
> structure map `K → L` is surjective, i.e. `K` has no proper algebraic extension.

```lean
theorem isAlgClosed_iff_forall_algebraMap_surjective (K : Type u) [Field K] :
    IsAlgClosed K ↔ ∀ (L : Type u) [Field L] [Algebra K L] [Algebra.IsAlgebraic K L],
      (⇑(algebraMap K L)).Surjective
```

**`IsAlgClosed.tfae`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L43).

> **Stacks 09GR**.
> For a field `K`, the following are equivalent:
> (1) every algebraic field extension `L/K` has surjective structure map `K → L`;
> (2) every irreducible polynomial in `K[X]` has degree `1`;
> (3) every nonconstant polynomial in `K[X]` has a root in `K`;
> (4) `K` is algebraically closed.

```lean
theorem IsAlgClosed.tfae (K : Type u) [Field K] :
    [∀ (L : Type u) [Field L] [Algebra K L] [Algebra.IsAlgebraic K L],
      (⇑(algebraMap K L)).Surjective,
    ∀ p : K[X], Irreducible p → p.degree = 1,
    ∀ p : K[X], p.degree ≠ 0 → ∃ (x : K), p.IsRoot x,
    IsAlgClosed K].TFAE
```

Declarations registered for the tag:

- [`IsAlgClosed.algebraMap_bijective_of_isIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsAlgClosed.algebraMap_bijective_of_isIntegral#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L15) (StacksCore): “(4) ⇒ (1), Universe polymorphic version”.

## Tag 09GT, a theorem

[Tag 09GT](https://stacks.math.columbia.edu/tag/09GT) in the Stacks Project.

**`exists_isAlgClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/IsAlgClosed/AlgebraicClosure.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/IsAlgClosed/AlgebraicClosure.lean#L23).

> **Stacks 09GT**.
> Every field `k` has an algebraic closure: there is a field `K` with a `k`-algebra structure
> (an extension of `k`) such that `K` is algebraic over `k` and algebraically closed.

```lean
theorem exists_isAlgClosure (k : Type u) [Field k] :
    ∃ (K : Type u) (_ : Field K) (_ : Algebra k K), IsAlgClosure k K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.10, Tag 09GP](https://stacks.math.columbia.edu/tag/09GP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
