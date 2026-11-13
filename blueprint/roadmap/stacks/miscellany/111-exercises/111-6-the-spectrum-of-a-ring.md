---
declaration: section
origin: cited
lean: TopologicalSpace.ArtinianSpace, TopologicalSpace.NoetherianSpace
statement: formalized
proof: formalized
---

# 111.6 The Spectrum of a ring

Section 111.6 of the Stacks Project, [Tag 027A](https://stacks.math.columbia.edu/tag/027A). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 027F, a definition

[Tag 027F](https://stacks.math.columbia.edu/tag/027F) in the Stacks Project.

**`TopologicalSpace.ArtinianSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/NoetherianSpace.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/NoetherianSpace.lean#L38). The attribute's comment: “Artinian spaces”.

> A topological space is Artinian if its ascending chains of closed subsets stabilize.

```lean
abbrev ArtinianSpace (X : Type*) [TopologicalSpace X] : Prop
```

Declarations registered for the tag:

- [`TopologicalSpace.NoetherianSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.NoetherianSpace#doc) registered with `add_to_stacks` in [StacksFrontier/Exercises/NoetherianSpace.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/NoetherianSpace.lean#L30) (StacksFrontier): “Noetherian spaces”. References: EGA 0 (2.2.1); SGA 4 VI (2.15).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.6, Tag 027A](https://stacks.math.columbia.edu/tag/027A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
