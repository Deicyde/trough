---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyNoetherian_baseChange_iff
statement: formalized
proof: formalized
---

# 33.11 Change of fields and locally Noetherian schemes

Section 33.11 of the Stacks Project, [Tag 038Q](https://stacks.math.columbia.edu/tag/038Q). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 038R, a lemma

[Tag 038R](https://stacks.math.columbia.edu/tag/038R) in the Stacks Project.

**`AlgebraicGeometry.isLocallyNoetherian_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularNoetherian.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularNoetherian.lean#L80). References: EGA IV (4.7.3), “(i)”; EGA IV (6.7.1), “k'/k finitely generated”.

> Extending the base field by a finitely generated field extension preserves and reflects
> the property that a scheme is locally Noetherian.

```lean
public theorem isLocallyNoetherian_baseChange_iff
    (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    [Algebra.EssFiniteType k k']
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    IsLocallyNoetherian X ↔
      IsLocallyNoetherian
        (pullback f (Spec.map (ofHom (algebraMap k k'))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.11, Tag 038Q](https://stacks.math.columbia.edu/tag/038Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
