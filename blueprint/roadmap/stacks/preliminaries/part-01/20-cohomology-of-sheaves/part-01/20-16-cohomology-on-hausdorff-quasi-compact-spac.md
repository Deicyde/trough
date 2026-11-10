---
declaration: section
origin: cited
lean: Stacks.Cohomology.CechRefinement.isIso_colimitToCohomology_one, Stacks.Cohomology.CechRefinement.isIso_colimitToCohomology, Stacks.Topology.isIso_cohomologyOfClosedMap, Stacks.Topology.isIso_sectionsOfClosedMap
statement: formalized
proof: formalized
---

# 20.16 Cohomology on Hausdorff quasi-compact spaces

Section 20.16 of the Stacks Project, [Tag 09V0](https://stacks.math.columbia.edu/tag/09V0). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09V1, a lemma

[Tag 09V1](https://stacks.math.columbia.edu/tag/09V1) in the Stacks Project.

**`Stacks.Cohomology.CechRefinement.isIso_colimitToCohomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/DegreeOneIsomorphism.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/DegreeOneIsomorphism.lean#L750).

> The canonical comparison from the first Čech cohomology of a topological space — the
> colimit, over all open coverings, of the first Čech cohomology of the covering — to the first
> sheaf cohomology of an abelian sheaf is an isomorphism.

```lean
theorem isIso_colimitToCohomology_one
    (G : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{max u v}) :
    IsIso (colimitToCohomology G 1)
```

## Tag 09V2, a lemma

[Tag 09V2](https://stacks.math.columbia.edu/tag/09V2) in the Stacks Project.

**`Stacks.Cohomology.CechRefinement.isIso_colimitToCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/HausdorffQuasiCompactIsomorphism.lean, line 857](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/HausdorffQuasiCompactIsomorphism.lean#L857). The attribute's comment: “the comparison of Stacks 09UZ is an isomorphism in every degree”.

> **Stacks Project, Tag 09V2.** Let `X` be a Hausdorff quasi-compact topological space and
> `F` an abelian sheaf on `X`.  The canonical comparison of Stacks 09UZ from the Čech cohomology
> of `X` — the colimit, over all open coverings of `X`, of the Čech cohomology of the covering —
> to the sheaf cohomology of `F` is an isomorphism in every degree.

```lean
theorem isIso_colimitToCohomology
    (G : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{max u v}) (n : ℤ) :
    IsIso (colimitToCohomology G n)
```

## Tag 09V3, a lemma

[Tag 09V3](https://stacks.math.columbia.edu/tag/09V3) in the Stacks Project.

**`Stacks.Topology.isIso_cohomologyOfClosedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/ClosedMapIso.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/ClosedMapIso.lean#L247). References: SGA 4 Vbis (4.1.3).

> For a quasi-compact subset `Z` of a topological space `X` any two
> distinct points of which have disjoint open neighbourhoods in `X`, the canonical map from the
> colimit of the cohomology of an abelian sheaf `F` over the open neighbourhoods of `Z` to the
> cohomology of the restriction of `F` to `Z` is an isomorphism in every degree.

```lean
theorem isIso_cohomologyOfClosedMap
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (p : ℕ) :
    IsIso (cohomologyOfClosedMap Z F p)
```

**`Stacks.Topology.isIso_sectionsOfClosedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/SubsetSections.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/SubsetSections.lean#L352). The attribute's comment: “degree-zero comparison for sheaves of sets”. References: SGA 4 Vbis (4.1.3), “i = 0”.

> For a quasi-compact subset whose distinct points have disjoint open neighbourhoods in the
> ambient space, the canonical restriction map from the sections on the open neighbourhoods of
> `Z` to the global sections of the restriction of `F` to `Z` is an isomorphism.

```lean
theorem isIso_sectionsOfClosedMap (Z : Set X) (hZ : IsCompact Z)
    (hSep : ∀ x ∈ Z, ∀ y ∈ Z, x ≠ y →
      ∃ U V : Set X, IsOpen U ∧ IsOpen V ∧ x ∈ U ∧ y ∈ V ∧ Disjoint U V)
    (F : X.Sheaf (Type u)) :
    IsIso (sectionsOfClosedMap F Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.16, Tag 09V0](https://stacks.math.columbia.edu/tag/09V0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
