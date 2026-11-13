---
declaration: section
origin: cited
lean: Stacks.AbelianStalk.existsUnique_addCommGroup_forget_stalk, Stacks.AbelianStalk.isColimitGermCocone
statement: formalized
proof: formalized
---

# 6.12 Stalks of abelian presheaves

Section 6.12 of the Stacks Project, [Tag 007E](https://stacks.math.columbia.edu/tag/007E). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 007F, a lemma

[Tag 007F](https://stacks.math.columbia.edu/tag/007F) in the Stacks Project.

**`Stacks.AbelianStalk.existsUnique_addCommGroup_forget_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean#L209).

> **Stacks 007F**, first assertion. Let `F` be a presheaf of abelian groups on `X` and `x : X`.
> There exists a unique structure of an abelian group on the stalk `F_x` — the stalk of the
> underlying presheaf of sets, `Presheaf.stalk (F ⋙ forget AddCommGrpCat) x` — such that for every
> open `U` with `x ∈ U` the germ map `F(U) → F_x` is a homomorphism of groups (equivalently,
> additive). The witness is `stalkAddCommGroup`.

```lean
theorem existsUnique_addCommGroup_forget_stalk :
    ∃! G : AddCommGroup (Presheaf.stalk (F ⋙ forget AddCommGrpCat) x), letI := G
      ∀ (U : Opens X) (hx : x ∈ U) (s t : ToType (F.obj (op U))),
        Presheaf.germ (F ⋙ forget AddCommGrpCat) U x hx (s + t) =
          Presheaf.germ (F ⋙ forget AddCommGrpCat) U x hx s +
            Presheaf.germ (F ⋙ forget AddCommGrpCat) U x hx t
```

**`Stacks.AbelianStalk.isColimitGermCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Stalk/Abelian.lean#L247).

> **Stacks 007F**, second assertion: `F_x = colim_{x ∈ U} F(U)` in the category of abelian groups.
> The set-valued stalk `F_x = Presheaf.stalk (F ⋙ forget AddCommGrpCat) x`, with the group
> structure of `existsUnique_addCommGroup_forget_stalk` and the germ maps `F(U) → F_x` as legs
> (`germCocone`, `germCocone_ι_app_apply`), is a colimit cocone in `AddCommGrpCat` of the diagram of
> sections of `F` over the open neighbourhoods of `x`.

```lean
noncomputable def isColimitGermCocone : Limits.IsColimit (germCocone F x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.12, Tag 007E](https://stacks.math.columbia.edu/tag/007E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
