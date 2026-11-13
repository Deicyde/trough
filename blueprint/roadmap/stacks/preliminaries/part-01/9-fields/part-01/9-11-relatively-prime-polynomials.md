---
declaration: section
origin: cited
lean: coprime_iff_span_pair_eq_top, isCoprime_iff_aeval_ne_zero_of_isAlgClosed
statement: formalized
proof: formalized
---

# 9.11 Relatively prime polynomials

Section 9.11 of the Stacks Project, [Tag 09GW](https://stacks.math.columbia.edu/tag/09GW). 2 tags here are carried by 1 declaration of the repository (in StacksCore) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09GX, a definition

[Tag 09GX](https://stacks.math.columbia.edu/tag/09GX) in the Stacks Project.

**`coprime_iff_span_pair_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Ideal/Operations.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L22). The attribute's comment: “generalization”.

> **Stacks 09GX** (generalization).
> Two elements `x y` of a commutative semiring are coprime if and only if the ideal they
> generate is the whole ring.

```lean
theorem coprime_iff_span_pair_eq_top {R : Type*} [CommSemiring R] (x y : R) :
    IsCoprime x y ↔ Ideal.span ({x, y} : Set R) = ⊤
```

## Tag 09GY, a lemma

[Tag 09GY](https://stacks.math.columbia.edu/tag/09GY) in the Stacks Project.

Declarations registered for the tag:

- [`isCoprime_iff_aeval_ne_zero_of_isAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCoprime_iff_aeval_ne_zero_of_isAlgClosed#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/IsAlgClosed/Basic.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/IsAlgClosed/Basic.lean#L17) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.11, Tag 09GW](https://stacks.math.columbia.edu/tag/09GW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
