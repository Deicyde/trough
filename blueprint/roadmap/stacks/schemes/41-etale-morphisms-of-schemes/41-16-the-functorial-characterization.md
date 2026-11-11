---
declaration: section
origin: cited
lean: AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_formallyEtale
statement: formalized
proof: formalized
---

# 41.16 The functorial characterization

Section 41.16 of the Stacks Project, [Tag 025J](https://stacks.math.columbia.edu/tag/025J). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025K, a theorem

[Tag 025K](https://stacks.math.columbia.edu/tag/025K) in the Stacks Project.

**`AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/EtaleIffFormallyEtale.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/EtaleIffFormallyEtale.lean#L46). The attribute's comment: “étale iff the unique-lifting property, for a morphism locally of finite”. References: EGA IV (17.3.2), “(ii) etale”; EGA IV (17.6.1), “a) <=> d)”; EGA IV (17.3.1); SGA 3 XI (1.6), “étale case”; SGA 4 VII (1.1), “functorial criterion”; SGA 3 XI (1.1); SGA 4½ Arcata (2.1.1), “more general”.

> A morphism of schemes is étale exactly when it is locally of finite presentation and formally
> étale.

```lean
theorem etale_iff_locallyOfFinitePresentation_and_formallyEtale
    {X S : Scheme.{u}} (f : X ⟶ S) :
    Etale f ↔ (LocallyOfFinitePresentation f ∧ FormallyEtale f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.16, Tag 025J](https://stacks.math.columbia.edu/tag/025J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
