---
declaration: section
origin: cited
lean: Module.projectiveDimension_add_depth_eq_depth_self
statement: formalized
proof: formalized
---

# 10.111 Auslander-Buchsbaum

Section 10.111 of the Stacks Project, [Tag 090U](https://stacks.math.columbia.edu/tag/090U). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 090V, a proposition

[Tag 090V](https://stacks.math.columbia.edu/tag/090V) in the Stacks Project.

**`Module.projectiveDimension_add_depth_eq_depth_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ProjectiveDimension/AuslanderBuchsbaum.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/ProjectiveDimension/AuslanderBuchsbaum.lean#L755). The attribute's comment: “Stated with the sum on the left, in `WithBot ℕ∞`, for `Module.projectiveDimension` (Tag 00O4) and `Module.depth` along the maximal ideal (Tag 00LI). See the module docstring.”. References: EGA 0 (17.3.4), “more general”.

> **The Auslander-Buchsbaum formula.** Let `(R, 𝔪)` be a Noetherian local ring and let `M` be
> a nonzero finite `R`-module of finite projective dimension. Then
> `pd_R(M) + depth_𝔪(M) = depth_𝔪(R)`. The equality is read in `WithBot ℕ∞`; the hypotheses make
> all three quantities finite.

```lean
public theorem projectiveDimension_add_depth_eq_depth_self {R : Type u} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M]
    [Module.Finite R M] [Nontrivial M] (hM : projectiveDimension R M ≠ ⊤) :
    projectiveDimension R M + (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) =
      (depth R (IsLocalRing.maximalIdeal R) R : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.111, Tag 090U](https://stacks.math.columbia.edu/tag/090U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
