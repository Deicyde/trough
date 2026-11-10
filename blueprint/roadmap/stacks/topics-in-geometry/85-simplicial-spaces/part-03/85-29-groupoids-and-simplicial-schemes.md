---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.groupoidSimplicialScheme, Stacks.Groupoids.GroupoidScheme.quasicoherentModuleEquivQuasicoherentOnTotalSite, Stacks.Groupoids.GroupoidScheme.groupoidCechNerveTarget
statement: formalized
proof: formalized
---

# 85.29 Groupoids and simplicial schemes

Section 85.29 of the Stacks Project, [Tag 07TM](https://stacks.math.columbia.edu/tag/07TM). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07TN, a lemma

[Tag 07TN](https://stacks.math.columbia.edu/tag/07TN) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.groupoidSimplicialScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidNerve.lean, line 879](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidNerve.lean#L879).

> **Stacks 07TN.** The simplicial scheme associated to a groupoid scheme.

```lean
noncomputable def groupoidSimplicialScheme {S : Scheme.{u}}
    (G : GroupoidScheme S) : GroupoidSimplicialScheme G
```

## Tag 07TP, a lemma

[Tag 07TP](https://stacks.math.columbia.edu/tag/07TP) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.quasicoherentModuleEquivQuasicoherentOnTotalSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidQuasiCoherentComparison.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidQuasiCoherentComparison.lean#L666). The attribute's comment: “The normalization `e^*α = id` of Stacks 03LI, which the source's proof passes over, is proved here: it is automatic for an invertible descent morphism satisfying the cocycle condition.”.

> **Stacks 07TP.**  Let `S` be a scheme, `(U,R,s,t,c)` a groupoid scheme over `S` and `X` the
> simplicial scheme of Stacks 07TN.  The category of quasi-coherent modules on `(U,R,s,t,c)` in
> the sense of Stacks 03LI is equivalent to the category of quasi-coherent modules on `X_{Zar}`.
>
> The equivalence is the composite of three steps.  Quasi-coherent modules on the total Zariski
> site are the pairs `(ℱ, α)` of Stacks 07TH with quasi-coherent degree-zero module, by Stacks 07TH
> and Stacks 0D7M; such pairs are the groupoid descent data of `(U,R,s,t,c)`, because in degrees
> `≤ 2` the nerve is `U`, `R` and `R ×_{s,U,t} R` with faces the source, the target, the two
> projections and the composition law; and groupoid descent data are the quasi-coherent modules of
> Stacks 03LI, which is `descentDataEquivQuasicoherentModule`.

```lean
noncomputable def quasicoherentModuleEquivQuasicoherentOnTotalSite :
    QuasicoherentModule G ≌ QuasicoherentZariskiModule (groupoidSimplicialScheme G).toSchemes
```

## Tag 07TQ, a lemma

[Tag 07TQ](https://stacks.math.columbia.edu/tag/07TQ) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.groupoidCechNerveTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidCechNerve.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/GroupoidCechNerve.lean#L389).

> The canonical cartesian map from the Čech nerve of the source of a groupoid scheme to its
> nerve.

```lean
noncomputable def groupoidCechNerveTarget {S : Scheme.{u}}
    (G : GroupoidScheme S) :
    CartesianTargetMap G (groupoidSimplicialScheme G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.29, Tag 07TM](https://stacks.math.columbia.edu/tag/07TM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
