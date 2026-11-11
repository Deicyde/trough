---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.etalePrecoverage, AlgebraicGeometry.Scheme.etalePrecoverage_le_fpqcPrecoverage, AlgebraicGeometry.BigEtaleOver, AlgebraicGeometry.BigEtaleOver.IsCovering, AlgebraicGeometry.BigEtaleOver.topology, AlgebraicGeometry.SmallEtale, AlgebraicGeometry.SmallEtale.IsCovering, AlgebraicGeometry.SmallEtale.topology
statement: formalized
proof: formalized
---

# 59.27 Étale coverings

Section 59.27 of the Stacks Project, [Tag 03PF](https://stacks.math.columbia.edu/tag/03PF). 4 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 13 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03PG, a definition

[Tag 03PG](https://stacks.math.columbia.edu/tag/03PG) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.etalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L161) (StacksFrontier): “the étale coverings: families of étale morphisms that are jointly surjective”. References: SGA 4 VII (1.2); SGA 4 XVII (0.10), “partial”.

## Tag 03PH, a lemma

[Tag 03PH](https://stacks.math.columbia.edu/tag/03PH) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etalePrecoverage_le_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L60). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L64).

> **Stacks 022C, 03PH.** Every étale covering family is an fpqc covering family.

```lean
public theorem etalePrecoverage_le_fpqcPrecoverage :
    Scheme.etalePrecoverage ≤ Scheme.fpqcPrecoverage
```

## Tag 03PI, a definition

[Tag 03PI](https://stacks.math.columbia.edu/tag/03PI) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigEtaleOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L82) (StacksFrontier): “big étale site (Sch/S)\_étale, category”.
- [`AlgebraicGeometry.BigEtaleOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L88), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L83) (StacksFrontier): “big étale site (Sch/S)\_étale, coverings”.
- [`AlgebraicGeometry.BigEtaleOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L85) (StacksFrontier): “big étale site (Sch/S)\_étale, topology”.
- [`AlgebraicGeometry.SmallEtale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L132), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L88) (StacksFrontier): “small étale site S\_étale, category”.
- [`AlgebraicGeometry.SmallEtale.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L153), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L89) (StacksFrontier): “small étale site S\_étale, coverings”.
- [`AlgebraicGeometry.SmallEtale.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L171), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L90) (StacksFrontier): “small étale site S\_étale, topology”.
- [`AlgebraicGeometry.BigZariskiOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L92) (StacksFrontier): “big Zariski site (Sch/S)\_Zar, category”.
- [`AlgebraicGeometry.BigZariskiOver.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L93) (StacksFrontier): “big Zariski site (Sch/S)\_Zar, coverings”.
- [`AlgebraicGeometry.BigZariskiOver.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L95) (StacksFrontier): “big Zariski site (Sch/S)\_Zar, topology”.
- [`AlgebraicGeometry.SmallZariski`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L98) (StacksFrontier): “small Zariski site S\_Zar, category”.
- [`AlgebraicGeometry.SmallZariski.IsCovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L99) (StacksFrontier): “small Zariski site S\_Zar, coverings”.
- [`AlgebraicGeometry.SmallZariski.topology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L128), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSmallSites/Basic.lean#L101) (StacksFrontier): “small Zariski site S\_Zar, topology”.

## Tag 03PJ, a proposition

[Tag 03PJ](https://stacks.math.columbia.edu/tag/03PJ) in the Stacks Project.

**`AlgebraicGeometry.bigSmallEtaleSheafCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/SheafCohomology.lean#L154). The attribute's comment: “big-site cohomology over S agrees with that of the restriction to S\_etale”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.27, Tag 03PF](https://stacks.math.columbia.edu/tag/03PF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
