---
declaration: section
origin: cited
lean: skolemNoether, skolemNoether'
statement: formalized
proof: formalized
---

# 11.6 Skolem-Noether

Section 11.6 of the Stacks Project, [Tag 074P](https://stacks.math.columbia.edu/tag/074P). 2 tags here are carried by 2 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 074Q, a theorem

[Tag 074Q](https://stacks.math.columbia.edu/tag/074Q) in the Stacks Project.

**`skolemNoether`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SkolemNoether.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/SkolemNoether.lean#L125). References: SGA 4½ Arcata (3.1.2), “more general”.

> **Skolem–Noether**: two algebra homomorphisms from a simple algebra to a
> finite-dimensional central simple algebra are conjugate by a unit.

```lean
public theorem skolemNoether (K : Type u) (A B : Type v) [Field K] [Ring A] [Algebra K A]
    [Module.Finite K A] [Algebra.IsCentral K A] [IsSimpleRing A]
    [Ring B] [Algebra K B] [IsSimpleRing B] (f g : B →ₐ[K] A) :
    ∃ x : Aˣ, ∀ b : B, g b = x * f b * x⁻¹
```

## Tag 074R, a lemma

[Tag 074R](https://stacks.math.columbia.edu/tag/074R) in the Stacks Project.

**`skolemNoether'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SkolemNoether.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/SkolemNoether.lean#L141). References: SGA 4½ Arcata (3.1.2), “more general”.

```lean
public theorem skolemNoether' (K : Type u) (A : Type v) [Field K] [Ring A] [Algebra K A]
    [Module.Finite K A] [Algebra.IsCentral K A] [IsSimpleRing A] (e : A ≃ₐ[K] A) :
    ∃ x : Aˣ, ∀ a : A, e a = x * a * x⁻¹
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.6, Tag 074P](https://stacks.math.columbia.edu/tag/074P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
