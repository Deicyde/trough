---
declaration: section
origin: cited
lean: Module.Flat.quotient_inf
statement: formalized
proof: formalized
---

# 15.16 Flattening stratification

Section 15.16 of the Stacks Project, [Tag 0521](https://stacks.math.columbia.edu/tag/0521). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0522, a lemma

[Tag 0522](https://stacks.math.columbia.edu/tag/0522) in the Stacks Project.

**`Module.Flat.quotient_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/QuotientInf.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/QuotientInf.lean#L238).

> **Stacks 0522**.
> If `M ⧸ I₁ • ⊤` is flat over `R ⧸ I₁` and `M ⧸ I₂ • ⊤` is flat over `R ⧸ I₂`, then
> `M ⧸ (I₁ ⊓ I₂) • ⊤` is flat over `R ⧸ (I₁ ⊓ I₂)`.

```lean
theorem Module.Flat.quotient_inf {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M]
    [Module R M] (I₁ I₂ : Ideal R)
    (h₁ : Module.Flat (R ⧸ I₁) (M ⧸ (I₁ • (⊤ : Submodule R M))))
    (h₂ : Module.Flat (R ⧸ I₂) (M ⧸ (I₂ • (⊤ : Submodule R M)))) :
    Module.Flat (R ⧸ (I₁ ⊓ I₂)) (M ⧸ ((I₁ ⊓ I₂) • (⊤ : Submodule R M)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.16, Tag 0521](https://stacks.math.columbia.edu/tag/0521)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
