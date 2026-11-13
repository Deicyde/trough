---
declaration: section
origin: cited
lean: Stacks.Examples.exists_groupScheme_flat_identityComponent_not_flat
statement: formalized
proof: formalized
---

# 110.49 A non-flat group scheme with flat identity component

Section 110.49 of the Stacks Project, [Tag 06RJ](https://stacks.math.columbia.edu/tag/06RJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06RK, a lemma

[Tag 06RK](https://stacks.math.columbia.edu/tag/06RK) in the Stacks Project.

**`Stacks.Examples.exists_groupScheme_flat_identityComponent_not_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/GroupSchemes/NonFlatFlatIdentityComponent.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/GroupSchemes/NonFlatFlatIdentityComponent.lean#L365). References: EGA IV (17.12.8), “non-flat example”.

> **Stacks Project, Tag 06RK.** A group scheme can fail to be flat over its base even when its
> identity component is flat over the base.

```lean
public theorem exists_groupScheme_flat_identityComponent_not_flat :
    ∃ (S : Scheme.{u}) (G : CategoryTheory.Over S) (hG : GrpObj G),
      letI : GrpObj G := hG
      ¬ Flat G.hom ∧
        ∃ U : G.left.Opens,
          Flat (U.ι ≫ G.hom) ∧
            IsClosed (U : Set G.left) ∧
              Set.range (η[G]).left = (U : Set G.left) ∧
                ∀ s : S,
                  _root_.IsConnected {g : {g : G.left // G.hom g = s} |
                    (g.1 : G.left) ∈ (U : Set G.left)}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.49, Tag 06RJ](https://stacks.math.columbia.edu/tag/06RJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
