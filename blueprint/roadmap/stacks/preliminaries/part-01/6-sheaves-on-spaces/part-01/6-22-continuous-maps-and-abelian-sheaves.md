---
declaration: section
origin: cited
lean: Stacks.Topology.AbelianStalk.stalkPullbackIso_presheaf, Stacks.Topology.AbelianStalk.stalkPullbackIso_sheaf
statement: formalized
proof: formalized
---

# 6.22 Continuous maps and abelian sheaves

Section 6.22 of the Stacks Project, [Tag 008N](https://stacks.math.columbia.edu/tag/008N). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 008O, a lemma

[Tag 008O](https://stacks.math.columbia.edu/tag/008O) in the Stacks Project.

**`Stacks.Topology.AbelianStalk.stalkPullbackIso_presheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/AbelianStalk.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Pullback/AbelianStalk.lean#L86). The attribute's comment: “(1)”.

> **Stacks tag 008O, part (1).**
> For a continuous map `f : X ⟶ Y` and an abelian presheaf `G` on `Y`, the
> canonical comparison map between the stalk of `G` at `f x` and the stalk of
> the presheaf pullback `f_p G` at `x` is an isomorphism of abelian groups.
>
> This is `TopCat.Presheaf.stalkPullbackIso` specialised to the category of
> abelian groups.

```lean
noncomputable def stalkPullbackIso_presheaf
    (G : Y.Presheaf AddCommGrpCat.{v}) (x : X) :
    G.stalk (f x) ≅ ((Presheaf.pullback AddCommGrpCat.{v} f).obj G).stalk x
```

**`Stacks.Topology.AbelianStalk.stalkPullbackIso_sheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/AbelianStalk.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Pullback/AbelianStalk.lean#L118). The attribute's comment: “(2)”.

> **Stacks tag 008O, part (2).**
> For a continuous map `f : X ⟶ Y` and an abelian sheaf `G` on `Y`, the canonical
> comparison map between the stalk of `G` at `f x` and the stalk of the sheaf
> pullback `f⁻¹ G` at `x` is an isomorphism of abelian groups.
>
> The proof factors the comparison through the presheaf pullback: first
> `Presheaf.stalkPullbackIso` gives the presheaf-level iso, then
> `Sheaf.pullbackIso` identifies the sheaf pullback with the sheafification of
> the presheaf pullback, and `sheafifyStalkIso` (above) gives the stalk iso for
> the sheafification step.

```lean
noncomputable def stalkPullbackIso_sheaf
    (G : Y.Sheaf AddCommGrpCat.{v}) (x : X) :
    G.presheaf.stalk (f x) ≅
      ((Sheaf.pullback AddCommGrpCat.{v} f).obj G).presheaf.stalk x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.22, Tag 008N](https://stacks.math.columbia.edu/tag/008N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
