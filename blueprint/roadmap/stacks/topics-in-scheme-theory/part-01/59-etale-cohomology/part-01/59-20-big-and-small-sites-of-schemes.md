---
declaration: section
origin: cited
lean: AlgebraicGeometry.coveringMorphismProperty, AlgebraicGeometry.Scheme.precoverage, AlgebraicGeometry.Scheme.ofArrows_mem_precoverage_iff, AlgebraicGeometry.BigFppfOver, AlgebraicGeometry.BigFppfOver.IsCovering, AlgebraicGeometry.BigFppfOver.topology, AlgebraicGeometry.BigSyntomicOver, AlgebraicGeometry.BigSyntomicOver.IsCovering
statement: formalized
proof: formalized
---

# 59.20 Big and small sites of schemes

Section 59.20 of the Stacks Project, [Tag 03X7](https://stacks.math.columbia.edu/tag/03X7). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 23 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03X8, a definition

[Tag 03X8](https://stacks.math.columbia.edu/tag/03X8) in the Stacks Project.

**`AlgebraicGeometry.coveringMorphismProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean#L74). The attribute's comment: “morphism property for each topology”.

> The property required of morphisms in a covering family for the selected topology.

```lean
public abbrev coveringMorphismProperty (τ : CoveringTopology) :
    MorphismProperty Scheme.{u}
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.precoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.precoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean#L83) (StacksFrontier): “precoverage of jointly surjective families”. References: SGA 4 IV (8.5.5), “more general”.
- [`AlgebraicGeometry.Scheme.ofArrows_mem_precoverage_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.ofArrows_mem_precoverage_iff#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean#L86) (StacksFrontier): “joint surjectivity and componentwise property”. References: SGA 3 IV (6.1), “more general”; SGA 4 VII (1.2), “more general”.

## Tag 03XB, a definition

[Tag 03XB](https://stacks.math.columbia.edu/tag/03XB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigFppfOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L232), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L41) (StacksFrontier): “big fppf category”.
- [`AlgebraicGeometry.BigFppfOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L247), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L42) (StacksFrontier): “big fppf coverings”.
- [`AlgebraicGeometry.BigFppfOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L251), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L43) (StacksFrontier): “big fppf topology”.
- [`AlgebraicGeometry.BigSyntomicOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L48), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L45) (StacksFrontier): “big syntomic category”.
- [`AlgebraicGeometry.BigSyntomicOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L46) (StacksFrontier): “big syntomic coverings”.
- [`AlgebraicGeometry.BigSyntomicOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L47) (StacksFrontier): “big syntomic topology”.
- [`AlgebraicGeometry.BigSmoothOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L49) (StacksFrontier): “big smooth category”.
- [`AlgebraicGeometry.BigSmoothOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L61), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L50) (StacksFrontier): “big smooth coverings”.
- [`AlgebraicGeometry.BigSmoothOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L51) (StacksFrontier): “big smooth topology”.
- [`AlgebraicGeometry.BigEtaleOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L53) (StacksFrontier): “big étale category”.
- [`AlgebraicGeometry.BigEtaleOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L88), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L54) (StacksFrontier): “big étale coverings”.
- [`AlgebraicGeometry.BigEtaleOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L55) (StacksFrontier): “big étale topology”.
- [`AlgebraicGeometry.BigZariskiOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L57) (StacksFrontier): “big Zariski category”.
- [`AlgebraicGeometry.BigZariskiOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L58) (StacksFrontier): “big Zariski coverings”.
- [`AlgebraicGeometry.BigZariskiOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L59) (StacksFrontier): “big Zariski topology”.
- [`AlgebraicGeometry.SmallEtale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L132), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L61) (StacksFrontier): “small étale category”.
- [`AlgebraicGeometry.SmallEtale.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L153), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L62) (StacksFrontier): “small étale coverings”.
- [`AlgebraicGeometry.SmallEtale.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L171), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L63) (StacksFrontier): “small étale topology”.
- [`AlgebraicGeometry.SmallZariski`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L65) (StacksFrontier): “small Zariski category”.
- [`AlgebraicGeometry.SmallZariski.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L66) (StacksFrontier): “small Zariski coverings”.
- [`AlgebraicGeometry.SmallZariski.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L128), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L67) (StacksFrontier): “small Zariski topology”.

## Tag 03YX, a lemma

[Tag 03YX](https://stacks.math.columbia.edu/tag/03YX) in the Stacks Project.

**`AlgebraicGeometry.bigSmallEtaleSheafCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean#L154). The attribute's comment: “étale case”.

> **Stacks 03YX, étale case.** Big étale cohomology over `S` agrees, naturally in the abelian
> sheaf, with the cohomology of its restriction to the small étale site.

```lean
public noncomputable def bigSmallEtaleSheafCohomologyIso
    (F : Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1})
    [HasSheafify (BigEtaleOver.topology B S hS) Ab.{u + 1}]
    [HasSheafify (SmallEtale.topology B S hS) Ab.{u + 1}]
    [HasExt.{w} (Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1})]
    [HasExt.{w} (Sheaf (SmallEtale.topology B S hS) Ab.{u + 1})]
    (p : ℕ) :
    Sheaf.H.{w, u + 1} F p ≃+
      (((SmallEtale.inclusion B S hS).sheafPushforwardContinuous
          Ab.{u + 1} (SmallEtale.topology B S hS)
          (BigEtaleOver.topology B S hS)).obj F).H p
```

**`AlgebraicGeometry.bigSmallEtaleSheafCohomologyIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean#L207). The attribute's comment: “étale naturality”.

> **Stacks 03YX, étale naturality.** The étale comparison commutes with morphisms of abelian
> sheaves.

```lean
public theorem bigSmallEtaleSheafCohomologyIso_naturality
    [HasSheafify (BigEtaleOver.topology B S hS) Ab.{u + 1}]
    [HasSheafify (SmallEtale.topology B S hS) Ab.{u + 1}]
    [HasExt.{w} (Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1})]
    [HasExt.{w} (Sheaf (SmallEtale.topology B S hS) Ab.{u + 1})]
    {F G : Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1}}
    (f : F ⟶ G) (p : ℕ) (x : Sheaf.H.{w, u + 1} F p) :
    bigSmallEtaleSheafCohomologyIso B S hS G p (Sheaf.H.map f p x) =
      Sheaf.H.map
        (((SmallEtale.inclusion B S hS).sheafPushforwardContinuous
          Ab.{u + 1} (SmallEtale.topology B S hS)
          (BigEtaleOver.topology B S hS)).map f) p
        (bigSmallEtaleSheafCohomologyIso B S hS F p x)
```

**`AlgebraicGeometry.bigSmallZariskiCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/BigSmallSheafCohomology.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/BigSmallSheafCohomology.lean#L190). The attribute's comment: “Zariski case”.

> **Stacks 03YX, Zariski case.** Big Zariski cohomology over `S` agrees, naturally in the
> abelian sheaf, with the cohomology of its restriction to the small Zariski site.

```lean
public noncomputable def bigSmallZariskiCohomologyIso
    (F : Sheaf (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1})
    [HasSheafify (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1}]
    [HasSheafify (SmallZariski.topology B S.obj S.property) Ab.{u + 1}]
    [HasExt.{w} (Sheaf (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1})]
    [HasExt.{w} (Sheaf (SmallZariski.topology B S.obj S.property) Ab.{u + 1})]
    (p : ℕ) :
    Sheaf.H.{w, u + 1} F p ≃+
      (((SmallZariski.inclusion B S.obj S.property).sheafPushforwardContinuous
          Ab.{u + 1} (SmallZariski.topology B S.obj S.property)
          (BigZariskiOver.topology B S.obj S.property)).obj F).H p
```

**`AlgebraicGeometry.bigSmallZariskiCohomologyIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/BigSmallSheafCohomology.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/BigSmallSheafCohomology.lean#L247). The attribute's comment: “Zariski naturality”.

> **Stacks 03YX, Zariski naturality.** The Zariski comparison commutes with morphisms of
> abelian sheaves.

```lean
public theorem bigSmallZariskiCohomologyIso_naturality
    [HasSheafify (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1}]
    [HasSheafify (SmallZariski.topology B S.obj S.property) Ab.{u + 1}]
    [HasExt.{w} (Sheaf (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1})]
    [HasExt.{w} (Sheaf (SmallZariski.topology B S.obj S.property) Ab.{u + 1})]
    {F G : Sheaf (BigZariskiOver.topology B S.obj S.property) Ab.{u + 1}}
    (f : F ⟶ G) (p : ℕ) (x : Sheaf.H.{w, u + 1} F p) :
    bigSmallZariskiCohomologyIso B S G p (Sheaf.H.map f p x) =
      Sheaf.H.map
        (((SmallZariski.inclusion B S.obj S.property).sheafPushforwardContinuous
          Ab.{u + 1} (SmallZariski.topology B S.obj S.property)
          (BigZariskiOver.topology B S.obj S.property)).map f) p
        (bigSmallZariskiCohomologyIso B S F p x)
```

## Tag 03X9, a definition

[Tag 03X9](https://stacks.math.columbia.edu/tag/03X9) in the Stacks Project.

**`AlgebraicGeometry.IsStandardCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoverings.lean#L94).

> A finite family of affine schemes covering an affine target, with morphisms of the standard
> form appropriate to the chosen topology.

```lean
public structure IsStandardCovering (τ : CoveringTopology) {T : Scheme.{u}} [IsAffine T]
    {I : Type v} (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 03XA, a lemma

[Tag 03XA](https://stacks.math.columbia.edu/tag/03XA) in the Stacks Project.

**`AlgebraicGeometry.exists_standardCovering_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardRefinement.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardRefinement.lean#L86).

> **Stacks Project, Tag 03XA.** A covering of an affine scheme in one of the five standard
> topologies can be refined by a standard covering in that topology.

```lean
public theorem exists_standardCovering_refinement (τ : CoveringTopology)
    {T : Scheme.{u}} [IsAffine T] (U : PreZeroHypercover.{v} T)
    (hU : U.presieve₀ ∈ Scheme.precoverage (coveringMorphismProperty τ) T) :
    ∃ (V : PreZeroHypercover.{v} T) (_ : V.Hom U), IsStandardCovering τ V.X V.f
```

## Tag 03YY, a lemma

[Tag 03YY](https://stacks.math.columbia.edu/tag/03YY) in the Stacks Project.

**`AlgebraicGeometry.exists_extension_abelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ChangeOfBigSites.lean#L710). The attribute's comment: “extend\_abelian\_sheaf”.

> **An abelian sheaf on a big site extends to any larger big site of the same topology.** For
> nested big `τ`-sites over a scheme `S`, every abelian sheaf on the smaller localized site is the
> restriction, up to isomorphism, of an abelian sheaf on the larger one.

```lean
public theorem exists_extension_abelianSheaf {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B')
    (S : Scheme.{u}) (hS : S.size < cutoff τ B)
    (F : Sheaf (overTopology τ B S hS) AddCommGrpCat.{u + 1}) :
    ∃ F' : Sheaf (overTopology τ B' S (largerContains h hS)) AddCommGrpCat.{u + 1},
      Nonempty ((abelianRestrictionOver B B' h S hS).obj F' ≅ F)
```

**`AlgebraicGeometry.cohomologyRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/CohomologyAfterRestriction.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/CohomologyAfterRestriction.lean#L73). The attribute's comment: “cohomology\_after\_restriction”.

> **Restricting an abelian sheaf from a larger big site to a smaller one preserves cohomology
> over every object of the smaller site, naturally in the sheaf.** For nested big `τ`-sites
> localized at a scheme `S` of the smaller one, the cohomology over `U` of the restriction of an
> abelian sheaf agrees with its cohomology over the image of `U`.
>
> The inclusion of the localized sites is continuous, cocontinuous and preserves finite limits, and
> a localized big site is essentially small, so this is
> `Stacks.Cohomology.BiggerSite.cohomologyPresheafFunctorIso`.

```lean
public noncomputable def cohomologyRestrictionIso {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') (S : Scheme.{u})
    (hS : S.size < cutoff τ B)
    [HasSheafify (overTopology τ B S hS) Ab.{u}]
    [HasSheafify (overTopology τ B' S (largerContains h hS)) Ab.{u}]
    [HasExt.{w} (Sheaf (overTopology τ B S hS) Ab.{u})]
    [HasExt.{w} (Sheaf (overTopology τ B' S (largerContains h hS)) Ab.{u})]
    (U : Over (base B S hS)) (p : ℕ) :
    (inclusionOver h S hS).sheafPushforwardContinuous Ab.{u} (overTopology τ B S hS)
          (overTopology τ B' S (largerContains h hS)) ⋙
        Sheaf.cohomologyPresheafFunctor (overTopology τ B S hS) p ⋙
          (evaluation (Over (base B S hS))ᵒᵖ Ab.{w}).obj (op U) ≅
      Sheaf.cohomologyPresheafFunctor (overTopology τ B' S (largerContains h hS)) p ⋙
        (evaluation (Over (base B' S (largerContains h hS)))ᵒᵖ Ab.{w}).obj
          (op ((inclusionOver h S hS).obj U))
```

**`AlgebraicGeometry.cohomologyOverRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/CohomologyOverRestriction.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/CohomologyOverRestriction.lean#L85). The attribute's comment: “part (1): for nested big sites `(Sch/S)_τ ⊆ (Sch'/S)_τ` of one of the five topologies, the cohomology over an object `U` of the smaller site of the restriction of an abelian sheaf on the bigger site is isomorphic to its cohomology over `U` on the bigger site, naturally in the sheaf, with sheafification and `Ext`-groups constructed from essential smallness of the sites”.

> **Restricting an abelian sheaf from a larger big site to a smaller one preserves cohomology
> over every object of the smaller site, naturally in the sheaf.** Let `τ` be one of the Zariski,
> étale, smooth, syntomic and fppf topologies, `S` a scheme, and `B ⊆ B'` two big `τ`-sites with
> `S` in `B`. For every object `U` of the localized site `(Sch/S)_τ` of `B`, every degree `p` and
> every abelian sheaf `ℱ'` on the localized site `(Sch'/S)_τ` of `B'`,
> `H^p_τ(U, ℱ'|_{(Sch/S)_τ}) ≅ H^p_τ(U, ℱ')`, naturally in `ℱ'`, with cohomology over an object
> the `Ext`-based `CategoryTheory.Sheaf.cohomologyPresheafFunctor` with values in any universe
> `max u w`. Sheafification and the `Ext`-groups on both localized sites come from their
> essential smallness, `AlgebraicGeometry.hasSheafify_overTopology_addCommGrp` and
> `AlgebraicGeometry.hasExt_sheaf_overTopology`.

```lean
public noncomputable def cohomologyOverRestrictionIso {τ : CoveringTopology}
    (B B' : BigSite.{u} τ) (h : IsContained B B') (S : Scheme.{u})
    (hS : S.size < cutoff τ B) (U : Over (base B S hS)) (p : ℕ) :
    letI := hasExt_sheaf_overTopology.{u, w} τ B S hS
    letI := hasExt_sheaf_overTopology.{u, w} τ B' S (largerContains h hS)
    (inclusionOver h S hS).sheafPushforwardContinuous Ab.{u} (overTopology τ B S hS)
          (overTopology τ B' S (largerContains h hS)) ⋙
        Sheaf.cohomologyPresheafFunctor (overTopology τ B S hS) p ⋙
          (evaluation (Over (base B S hS))ᵒᵖ Ab.{max u w}).obj (op U) ≅
      Sheaf.cohomologyPresheafFunctor (overTopology τ B' S (largerContains h hS)) p ⋙
        (evaluation (Over (base B' S (largerContains h hS)))ᵒᵖ Ab.{max u w}).obj
          (op ((inclusionOver h S hS).obj U))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.20, Tag 03X7](https://stacks.math.columbia.edu/tag/03X7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
