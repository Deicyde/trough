---
declaration: section
origin: cited
lean: Stacks.Examples.ConstructibleFunctionSheaf.exists_nonzero_limitPreserving_sheaf_vanishing_on_fields
statement: formalized
proof: formalized
---

# 110.59 Sheaves and constructible functions

Section 110.59 of the Stacks Project, [Tag 05LG](https://stacks.math.columbia.edu/tag/05LG). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05LH, a lemma

[Tag 05LH](https://stacks.math.columbia.edu/tag/05LH) in the Stacks Project.

**`Stacks.Examples.ConstructibleFunctionSheaf.exists_nonzero_limitPreserving_sheaf_vanishing_on_fields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Schemes/ConstructibleFunctionSheaf.lean, line 1423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Schemes/ConstructibleFunctionSheaf.lean#L1423).

> A nonzero limit-preserving étale sheaf of abelian groups which vanishes on fields
> and whose restriction maps along thickenings are isomorphisms.

```lean
public theorem exists_nonzero_limitPreserving_sheaf_vanishing_on_fields
    (B : BigEtaleSite.{u}) [UnivLE.{max v w, u}] :
    ∃ G : Sheaf B.topology AddCommGrpCat.{u},
      (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k))),
        IsZero (G.obj.obj (Opposite.op (B.obj (Spec (.of k)) hk)))) ∧
      AlgebraicGeometry.LimitPreserving.{u, u, v, w, u + 1, u}
        B.inclusion (G.obj ⋙ forget AddCommGrpCat.{u}) ∧
      (∀ (X X' : Scheme.{u}) (hX : B.Contains X) (hX' : B.Contains X')
        (i : X ⟶ X'), Stacks.Thickenings.IsThickening i →
          IsIso (G.obj.map (ObjectProperty.homMk i :
            B.obj X hX ⟶ B.obj X' hX').op)) ∧
      (∃ X : B.Scheme, ¬ IsZero (G.obj.obj (Opposite.op X)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.59, Tag 05LG](https://stacks.math.columbia.edu/tag/05LG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
