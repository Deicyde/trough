---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_common_bigZariskiSite, AlgebraicGeometry.exists_common_bigFppfSite, AlgebraicGeometry.exists_common_bigEtaleSite, AlgebraicGeometry.hasFiniteLimits_siteCategory, AlgebraicGeometry.inclusion_isCocontinuous, AlgebraicGeometry.inclusion_preservesFiniteLimits, AlgebraicGeometry.inclusion_isMorphismOfSites, AlgebraicGeometry.inclusionOver_isCocontinuous
statement: formalized
proof: formalized
---

# 34.12 Change of big sites

Section 34.12 of the Stacks Project, [Tag 022I](https://stacks.math.columbia.edu/tag/022I). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 022J, a lemma

[Tag 022J](https://stacks.math.columbia.edu/tag/022J) in the Stacks Project.

**`AlgebraicGeometry.exists_common_bigZariskiSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean#L235). The attribute's comment: “big Zariski sites”.

> A set-sized family of big Zariski sites admits a common enlargement of both its scheme
> cutoffs and covering-family bounds.

```lean
public theorem exists_common_bigZariskiSite {ι : Type v} [Small.{u} ι]
    (B : ι → BigZariskiSite.{u}) :
    ∃ C : BigZariskiSite.{u},
      ∀ i, (B i).schemeCardinal ≤ C.schemeCardinal ∧
        (B i).coveringCardinal ≤ C.coveringCardinal
```

**`AlgebraicGeometry.exists_common_bigFppfSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean#L271). The attribute's comment: “big fppf sites”.

> A set-sized family of big fppf sites admits a common enlargement of both its scheme
> cutoffs and covering-family bounds.

```lean
public theorem exists_common_bigFppfSite {ι : Type v} [Small.{u} ι]
    (B : ι → AlgebraicGeometry.BigFppfSite.{u}) :
    ∃ C : AlgebraicGeometry.BigFppfSite.{u},
      ∀ i, (B i).cutoff ≤ C.cutoff ∧ (B i).coveringBound ≤ C.coveringBound
```

**`AlgebraicGeometry.exists_common_bigEtaleSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/CommonBigSites.lean#L306). The attribute's comment: “big étale sites”.

> A set-sized family of big étale sites admits a common enlargement of both its scheme
> cutoffs and covering-family bounds.

```lean
public theorem exists_common_bigEtaleSite {ι : Type v} [Small.{u} ι]
    (B : ι → AlgebraicGeometry.BigEtaleSite.{u}) :
    ∃ C : AlgebraicGeometry.BigEtaleSite.{u},
      ∀ i, (B i).cutoff ≤ C.cutoff ∧ (B i).coveringBound ≤ C.coveringBound
```

## Tag 022K, a lemma

[Tag 022K](https://stacks.math.columbia.edu/tag/022K) in the Stacks Project.

**`AlgebraicGeometry.hasFiniteLimits_siteCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L313). The attribute's comment: “existence of finite limits in the big sites”.

> The underlying category of any of the five big sites has a terminal object
> and fibre products.

```lean
public instance hasFiniteLimits_siteCategory {τ : CoveringTopology}
    (B : BigSite.{u} τ) : HasFiniteLimits (siteCategory B)
```

**`AlgebraicGeometry.inclusion_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L321). The attribute's comment: “the inclusion is cocontinuous”.

```lean
public theorem inclusion_isCocontinuous {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') :
    (inclusion (Classical.choose h)).IsCocontinuous (siteTopology τ B) (siteTopology τ B')
```

**`AlgebraicGeometry.inclusion_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L371). The attribute's comment: “the inclusion preserves finite limits”.

```lean
public theorem inclusion_preservesFiniteLimits {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') :
    PreservesFiniteLimits (inclusion (Classical.choose h))
```

**`AlgebraicGeometry.inclusion_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L416). The attribute's comment: “the inclusion is a morphism of sites”.

```lean
public theorem inclusion_isMorphismOfSites {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') :
    _root_.IsMorphismOfSites.{u + 1} (inclusion (Classical.choose h))
      (siteTopology τ B) (siteTopology τ B')
```

**`AlgebraicGeometry.inclusionOver_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L467). The attribute's comment: “the localized inclusion is cocontinuous”.

```lean
public theorem inclusionOver_isCocontinuous {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B')
    (S : Scheme.{u}) (hS : S.size < cutoff τ B) :
    (inclusionOver h S hS).IsCocontinuous
      (overTopology τ B S hS)
      (overTopology τ B' S (largerContains h hS))
```

**`AlgebraicGeometry.inclusionOver_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L485). The attribute's comment: “the localized inclusion is a morphism of sites”.

```lean
public theorem inclusionOver_isMorphismOfSites {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B')
    (S : Scheme.{u}) (hS : S.size < cutoff τ B) :
    _root_.IsMorphismOfSites.{u + 1} (inclusionOver h S hS)
      (overTopology τ B S hS)
      (overTopology τ B' S (largerContains h hS))
```

**`AlgebraicGeometry.inclusionOver_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L502). The attribute's comment: “the localized inclusion preserves finite limits”.

```lean
public theorem inclusionOver_preservesFiniteLimits {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B')
    (S : Scheme.{u}) (hS : S.size < cutoff τ B) :
    PreservesFiniteLimits (inclusionOver h S hS)
```

**`AlgebraicGeometry.toposRetraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L533). The attribute's comment: “the retraction of big topoi”.

```lean
public noncomputable def toposRetraction {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') :
    let J := siteTopology τ B
    let K := siteTopology τ B'
    let F := inclusion (Classical.choose h)
    let : F.IsCocontinuous J K := inclusion_isCocontinuous B B' h
    let : F.IsContinuous J K := (inclusion_isMorphismOfSites B B' h).toIsContinuous
    ToposRetraction (siteCategory B) (siteCategory B') J K F
```

**`AlgebraicGeometry.toposRetractionOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L577). The attribute's comment: “the retraction of localized topoi”.

```lean
public noncomputable def toposRetractionOver {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B')
    (S : Scheme.{u}) (hS : S.size < cutoff τ B) :
    let J := overTopology τ B S hS
    let K := overTopology τ B' S (largerContains h hS)
    let F := inclusionOver h S hS
    let : F.IsCocontinuous J K := inclusionOver_isCocontinuous B B' h S hS
    let : F.IsContinuous J K := (inclusionOver_isMorphismOfSites B B' h S hS).toIsContinuous
    ToposRetraction (Over (base B S hS))
      (Over (base B' S (largerContains h hS))) J K F
```

Declarations registered for the tag:

- [`CategoryTheory.Over.hasFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.hasFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L317) (StacksFrontier): “existence of finite limits in localized big sites”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.12, Tag 022I](https://stacks.math.columbia.edu/tag/022I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
