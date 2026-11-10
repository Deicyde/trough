---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsPseudoTorsor, AlgebraicGeometry.IsTrivialPseudoTorsor, AlgebraicGeometry.isPseudoTorsor_iff_forall_existsUnique_smul, AlgebraicGeometry.isTrivial_iff_exists_globalSection, CategoryTheory.ModObj.isIso_leftSMul_iff, AlgebraicGeometry.IsFpqcTorsor, AlgebraicGeometry.IsZariskiTorsor, AlgebraicGeometry.IsEtaleTorsor
statement: formalized
proof: formalized
---

# 39.11 Principal homogeneous spaces

Section 39.11 of the Stacks Project, [Tag 0497](https://stacks.math.columbia.edu/tag/0497). 4 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0498, a definition

[Tag 0498](https://stacks.math.columbia.edu/tag/0498) in the Stacks Project.

**`AlgebraicGeometry.IsPseudoTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L61). The attribute's comment: “part (1)”. References: SGA 3 VIB (10.15), “formally principal hom.”; SGA 3 IV (6.7), “(iii)”; SGA 3 IV (5.1.0); SGA 3 III (0.1), “(ii)”; SGA 1 V (5.11), “formally princ. homog.”.

> An action is a pseudo-torsor if its shear map `(g, x) ↦ (g • x, x)` is an
> isomorphism.

```lean
abbrev IsPseudoTorsor {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsTrivialPseudoTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L68). The attribute's comment: “part (2)”. References: SGA 3 IV (5.1.1).

> An action is trivial if it is equivariantly isomorphic to the group object with its left
> regular action.

```lean
abbrev IsTrivialPseudoTorsor {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] : Prop
```

## Tag 0499, a lemma

[Tag 0499](https://stacks.math.columbia.edu/tag/0499) in the Stacks Project.

**`AlgebraicGeometry.isPseudoTorsor_iff_forall_existsUnique_smul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L79). The attribute's comment: “part (1), the pointwise characterization”. References: SGA 3 IV (5.1.0), “more general”; SGA 3 IV (6.7), “(i) ⇔ (iii)”.

> An action is a pseudo-torsor exactly when it is pointwise simply transitive: for every test
> object `T`, any two `T`-points of `X` differ by a unique `T`-point of `G`.

```lean
lemma isPseudoTorsor_iff_forall_existsUnique_smul
    {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] :
    IsPseudoTorsor G X ↔ ∀ (T : C) (x y : T ⟶ X), ∃! g : T ⟶ G, g • x = y
```

**`AlgebraicGeometry.isTrivial_iff_exists_globalSection`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L87). The attribute's comment: “trivial_iff_section”. References: SGA 3 IV (5.1.4); SGA 3 IV (5.1.5), “(ii) trivial ⟺ section”.

> A pseudo-torsor is trivial if and only if it admits a global section.

```lean
lemma isTrivial_iff_exists_globalSection
    {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] (hX : IsPseudoTorsor G X) :
    IsTrivialPseudoTorsor G X ↔ Nonempty (𝟙_ C ⟶ X)
```

Declarations registered for the tag:

- [`CategoryTheory.ModObj.isIso_leftSMul_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ModObj.isIso_leftSMul_iff#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L72) (StacksFrontier): “pointwise_characterization”.

## Tag 049A, a definition

[Tag 049A](https://stacks.math.columbia.edu/tag/049A) in the Stacks Project.

**`AlgebraicGeometry.IsFpqcTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L131). The attribute's comment: “part (1)”. References: SGA 3 IV (5.1.5), “schemes, fpqc”; SGA 3 IV (6.5), “fpqc row”; SGA 3 VIB (10.15), “G-torsor, fpqc T”; SGA 1 XI (4.1).

> A pseudo-torsor trivialized by an fpqc covering.

```lean
abbrev IsFpqcTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsZariskiTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L140). The attribute's comment: “parts (2), (4): Zariski and locally trivial”. References: SGA 1 XI (4.7); SGA 3 IV (6.5), “(Zar) row, special case”; SGA 4 IV (5.9), “special case”.

> A pseudo-torsor trivialized by a Zariski covering; equivalently, a locally trivial
> torsor.

```lean
abbrev IsZariskiTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsEtaleTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L148). The attribute's comment: “parts (2), (3): étale and quasi-isotrivial”. References: SGA 3 IV (5.1.5), “schemes, étale”; SGA 3 IV (6.5), “étale row”; SGA 3 VIB (10.15), “G-torsor, étale T”.

> A pseudo-torsor trivialized by an étale covering; equivalently, a quasi-isotrivial
> torsor.

```lean
abbrev IsEtaleTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsSmoothTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L153). The attribute's comment: “part (2): smooth”.

> A pseudo-torsor trivialized by a smooth covering.

```lean
abbrev IsSmoothTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsSyntomicTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L158). The attribute's comment: “part (2): syntomic”.

> A pseudo-torsor trivialized by a syntomic covering.

```lean
abbrev IsSyntomicTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

**`AlgebraicGeometry.IsFppfTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L167). The attribute's comment: “part (2): fppf”. References: SGA 3 IV (5.1.5), “schemes, fppf”; SGA 3 VIB (10.15), “G-torsor, fppf T”.

> A pseudo-torsor trivialized by an fppf covering.

```lean
abbrev IsFppfTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G] [ModObj G X] : Prop
```

## Tag 049B, a lemma

[Tag 049B](https://stacks.math.columbia.edu/tag/049B) in the Stacks Project.

**`AlgebraicGeometry.isZariskiTorsor_iff_isSiteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean#L341). The attribute's comment: “Zariski”.

> **Stacks Project, Tag 049B.** Zariski torsors under group schemes are exactly the torsors
> of their functors of points on the big Zariski site.

```lean
theorem isZariskiTorsor_iff_isSiteTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G]
    [ModObj G X] :
    IsZariskiTorsor S G X ↔ IsSiteTorsor S (Scheme.zariskiTopology.over S) G X
```

**`AlgebraicGeometry.isEtaleTorsor_iff_isSiteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean#L349). The attribute's comment: “étale”.

> **Stacks Project, Tag 049B.** Étale torsors under group schemes are exactly the torsors of
> their functors of points on the big étale site.

```lean
theorem isEtaleTorsor_iff_isSiteTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G]
    [ModObj G X] :
    IsEtaleTorsor S G X ↔ IsSiteTorsor S (Scheme.etaleTopology.over S) G X
```

**`AlgebraicGeometry.isSmoothTorsor_iff_isSiteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean#L357). The attribute's comment: “smooth”.

> **Stacks Project, Tag 049B.** Smooth torsors under group schemes are exactly the torsors of
> their functors of points on the big smooth site.

```lean
theorem isSmoothTorsor_iff_isSiteTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G]
    [ModObj G X] :
    IsSmoothTorsor S G X ↔
      IsSiteTorsor S ((Scheme.precoverage @Smooth).toGrothendieck.over S) G X
```

**`AlgebraicGeometry.isSyntomicTorsor_iff_isSiteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean#L366). The attribute's comment: “syntomic”.

> **Stacks Project, Tag 049B.** Syntomic torsors under group schemes are exactly the torsors
> of their functors of points on the big syntomic site.

```lean
theorem isSyntomicTorsor_iff_isSiteTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G]
    [ModObj G X] :
    IsSyntomicTorsor S G X ↔
      IsSiteTorsor S ((Scheme.precoverage @Syntomic).toGrothendieck.over S) G X
```

**`AlgebraicGeometry.isFppfTorsor_iff_isSiteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Torsor.lean#L375). The attribute's comment: “fppf”.

> **Stacks Project, Tag 049B.** Fppf torsors under group schemes are exactly the torsors of
> their functors of points on the big fppf site.

```lean
theorem isFppfTorsor_iff_isSiteTorsor (S : Scheme.{u}) (G X : Over S) [GrpObj G]
    [ModObj G X] :
    IsFppfTorsor S G X ↔ IsSiteTorsor S (Scheme.fppfTopology.over S) G X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.11, Tag 0497](https://stacks.math.columbia.edu/tag/0497)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
