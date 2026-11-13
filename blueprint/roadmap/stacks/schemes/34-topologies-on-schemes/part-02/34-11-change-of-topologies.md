---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigFppfSite.isSite_covBounded_isZariskiCovering, AlgebraicGeometry.BigFppfSite.isSite_covBounded_isEtaleCovering, AlgebraicGeometry.BigFppfSite.isSite_covBounded_smoothCovering, AlgebraicGeometry.BigFppfSite.isSite_covBounded_syntomicCovering, AlgebraicGeometry.BigFppfSite.toBigZariskiSite, AlgebraicGeometry.BigFppfSite.toBigEtaleSite, AlgebraicGeometry.BigFppfSite.toBigSmoothSite, AlgebraicGeometry.BigFppfSite.toBigSyntomicSite
statement: formalized
proof: formalized
---

# 34.11 Change of topologies

Section 34.11 of the Stacks Project, [Tag 03FE](https://stacks.math.columbia.edu/tag/03FE). 1 tag here is carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03FF, a remark

[Tag 03FF](https://stacks.math.columbia.edu/tag/03FF) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSite.isSite_covBounded_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L200). The attribute's comment: “Zariski site axioms”.

> The Zariski coverings of a big fppf site's category whose index type meets its covering
> bound satisfy the site axioms.

```lean
theorem isSite_covBounded_isZariskiCovering :
    IsSite (CovBounded (IsZariskiCovering (κ := B.cutoff)) B.coveringBound)
```

**`AlgebraicGeometry.BigFppfSite.isSite_covBounded_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L208). The attribute's comment: “étale site axioms”.

> The étale coverings of a big fppf site's category whose index type meets its covering
> bound satisfy the site axioms.

```lean
theorem isSite_covBounded_isEtaleCovering :
    IsSite (CovBounded (IsEtaleCovering (κ := B.cutoff)) B.coveringBound)
```

**`AlgebraicGeometry.BigFppfSite.isSite_covBounded_smoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L217). The attribute's comment: “smooth site axioms”.

> The smooth coverings of a big fppf site's category whose index type meets its covering
> bound satisfy the site axioms.

```lean
theorem isSite_covBounded_smoothCovering :
    IsSite (CovBounded (SmoothCovering B.cutoff) B.coveringBound)
```

**`AlgebraicGeometry.BigFppfSite.isSite_covBounded_syntomicCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L226). The attribute's comment: “syntomic site axioms”.

> The syntomic coverings of a big fppf site's category whose index type meets its covering
> bound satisfy the site axioms.

```lean
theorem isSite_covBounded_syntomicCovering :
    IsSite (CovBounded (SyntomicCovering B.cutoff) B.coveringBound)
```

**`AlgebraicGeometry.BigFppfSite.toBigZariskiSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L242). The attribute's comment: “the big Zariski site”.

> The big Zariski site carried by a chosen big fppf site: the same size-bounded category of
> schemes, with the chosen fppf covering families which are Zariski coverings.

```lean
def toBigZariskiSite : BigZariskiSite.{u}
```

**`AlgebraicGeometry.BigFppfSite.toBigEtaleSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L268). The attribute's comment: “the big étale site”.

> The big étale site carried by a chosen big fppf site: the same size-bounded category of
> schemes, with the chosen fppf covering families which are étale coverings.

```lean
def toBigEtaleSite : BigEtaleSite.{u}
```

**`AlgebraicGeometry.BigFppfSite.toBigSmoothSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L295). The attribute's comment: “the big smooth site”.

> The big smooth site carried by a chosen big fppf site: the same size-bounded category of
> schemes, with the chosen fppf covering families which are smooth coverings.

```lean
def toBigSmoothSite : BigSmoothSite.{u}
```

**`AlgebraicGeometry.BigFppfSite.toBigSyntomicSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenCoarserSites.lean#L324). The attribute's comment: “the big syntomic site”.

> The big syntomic site carried by a chosen big fppf site: the same size-bounded category of
> schemes, with the chosen fppf covering families which are syntomic coverings.

```lean
def toBigSyntomicSite : BigSyntomicSite.{u}
```

**`AlgebraicGeometry.etaleCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean#L207). The attribute's comment: “étale coverings”.

> The selected étale coverings on the underlying category of a chosen big fppf site: the
> families selected by the fppf site which are étale coverings.

```lean
public abbrev etaleCovering (B : BigFppfSite.{u})
    (E : Covering B.Schemes) : Prop
```

**`AlgebraicGeometry.etaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean#L217). The attribute's comment: “étale topology”.

> The big étale topology on the underlying category of a chosen big fppf site.

```lean
public abbrev etaleTopology (B : BigFppfSite.{u}) : GrothendieckTopology B.Schemes
```

**`AlgebraicGeometry.etaleCovering_isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean#L240). The attribute's comment: “étale site”.

> **Stacks 03FF.** The étale subcollection of a chosen big fppf site satisfies the site
> axioms.

```lean
public theorem etaleCovering_isSite (B : BigFppfSite.{u}) :
    IsSite (etaleCovering B)
```

**`AlgebraicGeometry.etaleCovering_has_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleSite.lean#L249). The attribute's comment: “étale covering representatives”.

> **Stacks 03FF.** Every étale covering of the common category is combinatorially
> equivalent to a selected étale covering.

```lean
public theorem etaleCovering_has_representative (B : BigFppfSite.{u})
    (E : Covering B.Schemes) (hE : IsEtaleCovering E) :
    ∃ E' : Covering B.Schemes,
      etaleCovering B E' ∧ Covering.CombEquiv E E'
```

**`AlgebraicGeometry.BigFppfSite.carriedIsCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L159). The attribute's comment: “the chosen covering families of the big τ-site carried by a big fppf site”.

> **Stacks 03FF.**  The chosen covering families of the big `τ`-site carried by `B`, as a
> predicate on the covering families of `B`'s own category.

```lean
public def carriedIsCovering : CoveringTopology → Covering B.Schemes → Prop
```

**`AlgebraicGeometry.BigFppfSite.carriedIsCovering_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L231). The attribute's comment: “the chosen covering families are nested along the chain of topologies”.

> **Stacks 03FF, the nesting of the four coarser systems.**  A chosen `τ'`-covering family is
> a chosen `τ`-covering family when `τ` is finer than `τ'`: the covering bound is `B`'s own in
> every one of the five cases, so only the morphism property changes, and the five properties are
> nested.

```lean
public theorem carriedIsCovering_mono (h : τ.IsFiner τ') {E : Covering B.Schemes}
    (hE : B.carriedIsCovering τ' E) : B.carriedIsCovering τ E
```

**`AlgebraicGeometry.BigFppfSite.zariskiCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L65). The attribute's comment: “Zariski coverings”.

> The chosen Zariski covering families of `Sch_κ` are the chosen fppf covering families which are
> Zariski coverings.

```lean
abbrev zariskiCovering (E : Covering B.Schemes) : Prop
```

**`AlgebraicGeometry.BigFppfSite.etaleCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L71). The attribute's comment: “étale coverings”. References: SGA 4 VII (1.2), “Cov X: étale coverings”.

> The chosen étale covering families of `Sch_κ` are the chosen fppf covering families which are
> étale coverings.

```lean
abbrev etaleCovering (E : Covering B.Schemes) : Prop
```

**`AlgebraicGeometry.BigFppfSite.smoothCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L77). The attribute's comment: “smooth coverings”.

> The chosen smooth covering families of `Sch_κ` are the chosen fppf covering families which are
> smooth coverings.

```lean
abbrev smoothCovering (E : Covering B.Schemes) : Prop
```

**`AlgebraicGeometry.BigFppfSite.syntomicCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L83). The attribute's comment: “syntomic coverings”.

> The chosen syntomic covering families of `Sch_κ` are the chosen fppf covering families which
> are syntomic coverings.

```lean
abbrev syntomicCovering (E : Covering B.Schemes) : Prop
```

**`AlgebraicGeometry.BigFppfSite.zariskiTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L114). The attribute's comment: “Zariski topology”.

> The big Zariski topology carried by a chosen big fppf site.

```lean
abbrev zariskiTopology : GrothendieckTopology B.Schemes
```

**`AlgebraicGeometry.BigFppfSite.etaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L119). The attribute's comment: “étale topology”. References: SGA 4 VII (1.2), “étale topology on (Sch)”.

> The big étale topology carried by a chosen big fppf site.

```lean
abbrev etaleTopology : GrothendieckTopology B.Schemes
```

**`AlgebraicGeometry.BigFppfSite.smoothTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L124). The attribute's comment: “smooth topology”.

> The big smooth topology carried by a chosen big fppf site.

```lean
abbrev smoothTopology : GrothendieckTopology B.Schemes
```

**`AlgebraicGeometry.BigFppfSite.syntomicTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L129). The attribute's comment: “syntomic topology”.

> The big syntomic topology carried by a chosen big fppf site.

```lean
abbrev syntomicTopology : GrothendieckTopology B.Schemes
```

**`AlgebraicGeometry.BigFppfSite.zariskiCovering_has_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ChosenCoverings.lean#L144). The attribute's comment: “Zariski representatives”.

> Every Zariski covering family of `Sch_κ` is combinatorially equivalent to a chosen Zariski
> covering family.

```lean
theorem zariskiCovering_has_representative (E : Covering B.Schemes)
    (hE : IsZariskiCovering E) :
    ∃ E' : Covering B.Schemes, B.zariskiCovering E' ∧ Covering.CombEquiv E E'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.11, Tag 03FE](https://stacks.math.columbia.edu/tag/03FE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
