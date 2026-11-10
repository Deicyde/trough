---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.cotangent_composition, Stacks.Groupoids.GroupoidScheme.cotangent_inverse
statement: formalized
proof: formalized
---

# 40.5 Local structure

Section 40.5 of the Stacks Project, [Tag 0CK3](https://stacks.math.columbia.edu/tag/0CK3). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CK4, a lemma

[Tag 0CK4](https://stacks.math.columbia.edu/tag/0CK4) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.cotangent_composition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/LocalStructure/Cotangent.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/LocalStructure/Cotangent.lean#L536). The attribute's comment: “composition on I/I²”.

> At an identity of a groupoid scheme, the map `I/I² → J/J²` induced by composition is the
> diagonal followed by the two maps induced by the projections.

```lean
theorem cotangent_composition :
    G.compositionCotangent x =
      ((G.firstCotangent x).coprod (G.secondCotangent x)).comp
        (LinearMap.id.prod LinearMap.id)
```

**`Stacks.Groupoids.GroupoidScheme.cotangent_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/LocalStructure/Cotangent.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/LocalStructure/Cotangent.lean#L556). The attribute's comment: “inversion on I/I²”.

> At an identity of a groupoid scheme, inversion acts by `-1` on `I/I²`.

```lean
theorem cotangent_inverse : G.inverseCotangent x = -LinearMap.id
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.5, Tag 0CK3](https://stacks.math.columbia.edu/tag/0CK3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
