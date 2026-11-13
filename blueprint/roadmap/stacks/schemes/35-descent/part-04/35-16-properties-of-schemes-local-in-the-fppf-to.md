---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyNoetherian_isLocal_fppf, AlgebraicGeometry.jacobsonSpace_isLocal_fppf, AlgebraicGeometry.finiteIrreducibleComponents_isLocal_fppf
statement: formalized
proof: formalized
---

# 35.16 Properties of schemes local in the fppf topology

Section 35.16 of the Stacks Project, [Tag 034B](https://stacks.math.columbia.edu/tag/034B). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 034C, a lemma

[Tag 034C](https://stacks.math.columbia.edu/tag/034C) in the Stacks Project.

**`AlgebraicGeometry.isLocallyNoetherian_isLocal_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Noetherian.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Noetherian.lean#L68).

> **Stacks Project, Tag 034C.** Being locally Noetherian is local for fppf coverings of
> schemes.

```lean
instance isLocallyNoetherian_isLocal_fppf :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsLocallyNoetherian X)
      Scheme.fppfPrecoverage
```

## Tag 0368, a lemma

[Tag 0368](https://stacks.math.columbia.edu/tag/0368) in the Stacks Project.

**`AlgebraicGeometry.jacobsonSpace_isLocal_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Jacobson.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Jacobson.lean#L119).

> **Stacks Project, Tag 0368.** Being Jacobson is local for fppf coverings of schemes.

```lean
instance jacobsonSpace_isLocal_fppf :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => JacobsonSpace X)
      Scheme.fppfPrecoverage
```

## Tag 0BAL, a lemma

[Tag 0BAL](https://stacks.math.columbia.edu/tag/0BAL) in the Stacks Project.

**`AlgebraicGeometry.finiteIrreducibleComponents_isLocal_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/IrreducibleComponents.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/IrreducibleComponents.lean#L163).

> Having finitely many irreducible components on every quasi-compact open is local in the
> fppf topology.

```lean
instance finiteIrreducibleComponents_isLocal_fppf :
    ObjectProperty.IsLocal
      (fun X : Scheme.{u} =>
        ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
      Scheme.fppfPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.16, Tag 034B](https://stacks.math.columbia.edu/tag/034B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
