---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyNoetherian_and_hasPropertySk_isLocal_syntomic, AlgebraicGeometry.isCohenMacaulay_isLocal_syntomic
statement: formalized
proof: formalized
---

# 35.17 Properties of schemes local in the syntomic topology

Section 35.17 of the Stacks Project, [Tag 0369](https://stacks.math.columbia.edu/tag/0369). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 036A, a lemma

[Tag 036A](https://stacks.math.columbia.edu/tag/036A) in the Stacks Project.

**`AlgebraicGeometry.isLocallyNoetherian_and_hasPropertySk_isLocal_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/SerreCondition.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/SerreCondition.lean#L155).

> **Stacks Project, Tag 036A.** Being locally Noetherian and satisfying `(Sₖ)` is local
> for syntomic coverings.

```lean
instance isLocallyNoetherian_and_hasPropertySk_isLocal_syntomic (k : ℕ) :
    ObjectProperty.IsLocal
      (fun X : Scheme.{u} => ∃ h : IsLocallyNoetherian X, @HasPropertySk X h k)
      (Scheme.precoverage @Syntomic)
```

## Tag 036B, a lemma

[Tag 036B](https://stacks.math.columbia.edu/tag/036B) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_isLocal_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/CohenMacaulay.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/CohenMacaulay.lean#L54).

> **Stacks Project, Tag 036B.** Being Cohen–Macaulay is local for syntomic coverings.

```lean
instance isCohenMacaulay_isLocal_syntomic :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsCohenMacaulay X)
      (Scheme.precoverage @Syntomic)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.17, Tag 0369](https://stacks.math.columbia.edu/tag/0369)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
