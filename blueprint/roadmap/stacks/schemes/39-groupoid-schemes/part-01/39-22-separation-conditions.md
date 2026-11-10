---
declaration: section
origin: cited
lean: AlgebraicGeometry.diagonalDiagram_commutes, AlgebraicGeometry.topComparison_isIso, AlgebraicGeometry.bottomComparison_isIso, AlgebraicGeometry.rightSquare_isPullback, AlgebraicGeometry.sourceTarget_quasiSeparated_iff_stabilizer_quasiSeparated, AlgebraicGeometry.stabilizer_quasiSeparated_iff_identity_quasiCompact, AlgebraicGeometry.sourceTarget_isSeparated_iff_stabilizer_isSeparated, AlgebraicGeometry.stabilizer_isSeparated_iff_identity_isClosedImmersion
statement: formalized
proof: formalized
---

# 39.22 Separation conditions

Section 39.22 of the Stacks Project, [Tag 02YG](https://stacks.math.columbia.edu/tag/02YG). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02YH, a lemma

[Tag 02YH](https://stacks.math.columbia.edu/tag/02YH) in the Stacks Project.

**`AlgebraicGeometry.diagonalDiagram_commutes`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean#L446). The attribute's comment: “commutativity of the diagram”.

> The left-hand part of the displayed diagonal diagram commutes.

```lean
lemma diagonalDiagram_commutes {S : Scheme.{u}} (G : GroupoidScheme S) :
    arrowDiagonal G ≫ bottomComparison G = topComparison G ≫ rightVertical G
```

**`AlgebraicGeometry.topComparison_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean#L480). The attribute's comment: “the upper horizontal arrow”.

> The upper comparison morphism in the diagonal diagram is an isomorphism.

```lean
lemma topComparison_isIso {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsIso (topComparison G)
```

**`AlgebraicGeometry.bottomComparison_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean#L614). The attribute's comment: “the lower horizontal arrow”.

> The lower comparison morphism in the diagonal diagram is an isomorphism, with inverse
> `(f, h) ↦ (f, f ∘ h)`.

```lean
lemma bottomComparison_isIso {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsIso (bottomComparison G)
```

**`AlgebraicGeometry.rightSquare_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/DiagonalDiagram.lean#L621). The attribute's comment: “the right square”.

> The right-hand square in the diagonal diagram is a pullback square.

```lean
lemma rightSquare_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback (pullback.snd G.source (𝟙 G.objects)) (rightVertical G)
      (identityStabilizer G) (pullback.snd G.source
        (pullback.snd (sourceTarget G) (diagonal G)))
```

## Tag 02YI, a lemma

[Tag 02YI](https://stacks.math.columbia.edu/tag/02YI) in the Stacks Project.

**`AlgebraicGeometry.sourceTarget_quasiSeparated_iff_stabilizer_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean#L132). The attribute's comment: “quasi_separated_equivalences”.

> The source-target morphism is quasi-separated exactly when the stabilizer is
> quasi-separated over the object scheme.

```lean
theorem sourceTarget_quasiSeparated_iff_stabilizer_quasiSeparated
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    QuasiSeparated (sourceTarget G).left ↔ QuasiSeparated (stabilizer G).hom
```

**`AlgebraicGeometry.stabilizer_quasiSeparated_iff_identity_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean#L142). The attribute's comment: “quasi_separated_equivalences”.

> The stabilizer is quasi-separated exactly when its identity section is quasi-compact.

```lean
theorem stabilizer_quasiSeparated_iff_identity_quasiCompact
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    QuasiSeparated (stabilizer G).hom ↔ QuasiCompact (identityStabilizer G).left
```

**`AlgebraicGeometry.sourceTarget_isSeparated_iff_stabilizer_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean#L203). The attribute's comment: “separated_equivalences”.

> The source-target morphism is separated exactly when the stabilizer is separated over
> the object scheme.

```lean
theorem sourceTarget_isSeparated_iff_stabilizer_isSeparated
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsSeparated (sourceTarget G).left ↔ IsSeparated (stabilizer G).hom
```

**`AlgebraicGeometry.stabilizer_isSeparated_iff_identity_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Separation.lean#L212). The attribute's comment: “separated_equivalences”. References: SGA 3 II (4.11.4), “more general”.

> The stabilizer is separated exactly when its identity section is a closed immersion.

```lean
theorem stabilizer_isSeparated_iff_identity_isClosedImmersion
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsSeparated (stabilizer G).hom ↔ IsClosedImmersion (identityStabilizer G).left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.22, Tag 02YG](https://stacks.math.columbia.edu/tag/02YG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
