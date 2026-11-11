---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_grp_iso_of_representable_openSubfunctor
statement: formalized
proof: formalized
---

# 44.5 A representability criterion

Section 44.5 of the Stacks Project, [Tag 0B9P](https://stacks.math.columbia.edu/tag/0B9P). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B9Q, a lemma

[Tag 0B9Q](https://stacks.math.columbia.edu/tag/0B9Q) in the Stacks Project.

**`AlgebraicGeometry.exists_grp_iso_of_representable_openSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/Representability/GroupSchemeCriterion.lean, line 829](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardScheme/Representability/GroupSchemeCriterion.lean#L829).

> A Zariski sheaf of groups with a representable open subfunctor meeting every
> field-valued point after translation by a rational point is a group scheme.

```lean
theorem exists_grp_iso_of_representable_openSubfunctor (k : Type u) [Field k]
    (G : (Over (Spec (.of k)))ᵒᵖ ⥤ GrpCat.{u})
    (hG : Presheaf.IsSheaf (Scheme.zariskiTopology.over (Spec (.of k)))
      (G ⋙ forget GrpCat))
    (F : Subfunctor (G ⋙ forget GrpCat))
    (hF : F.toFunctor.IsRepresentable)
    (hopen : (IsOpenImmersion.over (X := Spec (.of k))).presheaf F.ι)
    (hfield : ∀ (K : Type u) [Field K] [Algebra k K]
      (g : G.obj (op (fieldExtensionPoint k K))),
      ∃ g' : G.obj (op (Over.mk (𝟙 (Spec (.of k))))),
        (G.map (Over.homMk (fieldExtensionPoint k K).hom).op).hom g' * g ∈
          F.obj (op (fieldExtensionPoint k K))) :
    ∃ X : Grp (Over (Spec (.of k))), Nonempty (yonedaGrp.obj X ≅ G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.5, Tag 0B9P](https://stacks.math.columbia.edu/tag/0B9P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
