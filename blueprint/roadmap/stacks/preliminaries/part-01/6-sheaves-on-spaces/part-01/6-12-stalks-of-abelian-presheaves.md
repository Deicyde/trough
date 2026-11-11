---
declaration: section
origin: cited
lean: Stacks.AbelianStalk.existsUnique_addCommGroup_stalk, Stacks.AbelianStalk.stalk_eq_colimit_openNhds
statement: formalized
proof: formalized
---

# 6.12 Stalks of abelian presheaves

Section 6.12 of the Stacks Project, [Tag 007E](https://stacks.math.columbia.edu/tag/007E). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 007F, a lemma

[Tag 007F](https://stacks.math.columbia.edu/tag/007F) in the Stacks Project.

**`Stacks.AbelianStalk.existsUnique_addCommGroup_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean#L114).

> **Stacks 007F**, first assertion. There exists a unique structure of an abelian group on the stalk
> `F_x` of a presheaf of abelian groups `F` at a point `x` such that for every open `U` with `x ∈ U`
> the map `F(U) → F_x` is a homomorphism of groups. The witness is the structure carried by
> Mathlib's stalk in `AddCommGrpCat`.

```lean
theorem existsUnique_addCommGroup_stalk :
    ∃! G : AddCommGroup (ToType (F.stalk x)), letI := G
      ∀ (U : Opens X) (hx : x ∈ U) (s t : ToType (F.obj (op U))),
        F.germ U x hx (s + t) = F.germ U x hx s + F.germ U x hx t
```

**`Stacks.AbelianStalk.stalk_eq_colimit_openNhds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean#L129).

> **Stacks 007F**, second assertion: `F_x = colim_{x ∈ U} F(U)` in the category of abelian groups,
> the colimit being taken over the diagram of sections indexed by the open neighbourhoods of `x`.
> This is an equality of objects of `AddCommGrpCat`, as in the source, and it holds by `rfl` because
> Mathlib defines the stalk to be exactly that colimit; the statement therefore pins Mathlib's
> definition of `TopCat.Presheaf.stalk` down.

```lean
theorem stalk_eq_colimit_openNhds :
    F.stalk x = Limits.colimit ((TopologicalSpace.OpenNhds.inclusion x).op ⋙ F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.12, Tag 007E](https://stacks.math.columbia.edu/tag/007E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
