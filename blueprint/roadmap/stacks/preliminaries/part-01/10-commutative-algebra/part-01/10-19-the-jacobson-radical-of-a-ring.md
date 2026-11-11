---
declaration: section
origin: cited
lean: Ideal.le_ringJacobson_iff_isUnit_one_add, Ideal.isUnit_of_isUnit_quotient_mk, IsLocalHom.of_comap_surjective
statement: formalized
proof: formalized
---

# 10.19 The Jacobson radical of a ring

Section 10.19 of the Stacks Project, [Tag 0AMD](https://stacks.math.columbia.edu/tag/0AMD). 2 tags here are carried by 2 declarations of the repository (all in StacksCore) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AME, a lemma

[Tag 0AME](https://stacks.math.columbia.edu/tag/0AME) in the Stacks Project.

**`Ideal.le_ringJacobson_iff_isUnit_one_add`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Jacobson/Ideal.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Jacobson/Ideal.lean#L35). The attribute's comment: “(1) ⇔ (2)”.

> **Stacks 0AME**, (1) ⇔ (2): an ideal is contained in the Jacobson radical if and only if
> every element of `1 + I` is a unit.
>
> Forwards is `Ideal.mem_jacobson_bot` at `y = 1`. Backwards uses that `I` is an ideal: to place
> `x ∈ I` in the radical one must invert `1 + x * y` for every `y`, and `x * y` is again in `I`.

```lean
theorem le_ringJacobson_iff_isUnit_one_add (I : Ideal R) :
    I ≤ Ring.jacobson R ↔ ∀ x ∈ I, IsUnit (1 + x)
```

**`Ideal.isUnit_of_isUnit_quotient_mk`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Jacobson/Ideal.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Jacobson/Ideal.lean#L49). The attribute's comment: “in this case a unit mod I is a unit”.

> **Stacks 0AME**, the closing clause: if `I` is contained in the Jacobson radical, then an
> element of `R` whose image in `R ⧸ I` is a unit is itself a unit.
>
> Given a right inverse `y` mod `I`, the difference `x * y - 1` lies in `I` and hence in the
> radical, so `x * y` is a unit by `Ideal.isUnit_of_sub_one_mem_jacobson_bot`; a factor of a unit
> in a commutative ring is a unit.

```lean
theorem isUnit_of_isUnit_quotient_mk (I : Ideal R) (h : I ≤ Ring.jacobson R) (x : R)
    (hx : IsUnit (Ideal.Quotient.mk I x)) : IsUnit x
```

## Tag 0B7C, a lemma

[Tag 0B7C](https://stacks.math.columbia.edu/tag/0B7C) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalHom.of_comap_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalHom.of_comap_surjective#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/RingHom.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/RingHom.lean#L49) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.19, Tag 0AMD](https://stacks.math.columbia.edu/tag/0AMD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
