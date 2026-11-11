---
declaration: section
origin: cited
lean: CategoryTheory.ObjectProperty.IsLocal, AlgebraicGeometry.isLocal_fpqcPrecoverage_of_affine, AlgebraicGeometry.isLocal_fppfPrecoverage_of_affine, AlgebraicGeometry.isLocal_etalePrecoverage_of_affine, AlgebraicGeometry.isLocal_smoothPrecoverage_of_affine, AlgebraicGeometry.isLocal_syntomicPrecoverage_of_affine
statement: formalized
proof: formalized
---

# 35.15 Local properties of schemes

Section 35.15 of the Stacks Project, [Tag 0347](https://stacks.math.columbia.edu/tag/0347). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0348, a definition

[Tag 0348](https://stacks.math.columbia.edu/tag/0348) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.IsLocal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.IsLocal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean#L47) (StacksFrontier). References: SGA 4 IV (8.2); SGA 4½ Arcata (1.1), “more general”.

## Tag 0349, a lemma

[Tag 0349](https://stacks.math.columbia.edu/tag/0349) in the Stacks Project.

**`AlgebraicGeometry.isLocal_fpqcPrecoverage_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean#L207). The attribute's comment: “fpqc case”.

> **Stacks Project, Tag 0349.** A Zariski-local property of schemes which ascends along
> flat morphisms of affine schemes and descends along the surjective ones is fpqc local.

```lean
theorem isLocal_fpqcPrecoverage_of_affine (P : ObjectProperty Scheme.{u})
    [ObjectProperty.IsLocal P Scheme.zariskiPrecoverage]
    (ascends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Flat f → P S → P X)
    (descends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Flat f → Surjective f → P X → P S) :
    ObjectProperty.IsLocal P Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isLocal_fppfPrecoverage_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean#L261). The attribute's comment: “fppf case”.

> **Stacks Project, Tag 0349.** A Zariski-local property of schemes which ascends along
> flat morphisms of finite presentation of affine schemes and descends along the surjective
> ones is fppf local.

```lean
theorem isLocal_fppfPrecoverage_of_affine (P : ObjectProperty Scheme.{u})
    [ObjectProperty.IsLocal P Scheme.zariskiPrecoverage]
    (ascends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Flat f → FinitePresentation f → P S → P X)
    (descends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Flat f → FinitePresentation f → Surjective f → P X → P S) :
    ObjectProperty.IsLocal P Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.isLocal_etalePrecoverage_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean#L289). The attribute's comment: “étale case”.

> **Stacks Project, Tag 0349.** A Zariski-local property of schemes which ascends along
> étale morphisms of affine schemes and descends along the surjective ones is étale local.

```lean
theorem isLocal_etalePrecoverage_of_affine (P : ObjectProperty Scheme.{u})
    [ObjectProperty.IsLocal P Scheme.zariskiPrecoverage]
    (ascends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Etale f → P S → P X)
    (descends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Etale f → Surjective f → P X → P S) :
    ObjectProperty.IsLocal P Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isLocal_smoothPrecoverage_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean#L304). The attribute's comment: “smooth case”.

> **Stacks Project, Tag 0349.** A Zariski-local property of schemes which ascends along
> smooth morphisms of affine schemes and descends along the surjective ones is smooth
> local.

```lean
theorem isLocal_smoothPrecoverage_of_affine (P : ObjectProperty Scheme.{u})
    [ObjectProperty.IsLocal P Scheme.zariskiPrecoverage]
    (ascends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Smooth f → P S → P X)
    (descends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Smooth f → Surjective f → P X → P S) :
    ObjectProperty.IsLocal P (Scheme.precoverage @Smooth)
```

**`AlgebraicGeometry.isLocal_syntomicPrecoverage_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Criterion.lean#L319). The attribute's comment: “syntomic case”.

> **Stacks Project, Tag 0349.** A Zariski-local property of schemes which ascends along
> syntomic morphisms of affine schemes and descends along the surjective ones is syntomic
> local.

```lean
theorem isLocal_syntomicPrecoverage_of_affine (P : ObjectProperty Scheme.{u})
    [ObjectProperty.IsLocal P Scheme.zariskiPrecoverage]
    (ascends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Syntomic f → P S → P X)
    (descends : ∀ {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S),
      Syntomic f → Surjective f → P X → P S) :
    ObjectProperty.IsLocal P (Scheme.precoverage @Syntomic)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.15, Tag 0347](https://stacks.math.columbia.edu/tag/0347)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
