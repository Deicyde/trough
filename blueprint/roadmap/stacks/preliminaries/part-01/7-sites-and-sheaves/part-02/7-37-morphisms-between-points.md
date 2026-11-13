---
declaration: section
origin: cited
lean: Stacks.Sites.PointStalk.tStalk, Stacks.Sites.PointStalk.tStalkApp_stalkMk, Stacks.Sites.PointStalk.tStalkApp_theta, CategoryTheory.GrothendieckTopology.Point.Hom
statement: formalized
proof: formalized
---

# 7.37 Morphisms between points

Section 7.37 of the Stacks Project, [Tag 00YG](https://stacks.math.columbia.edu/tag/00YG). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00YH, a lemma

[Tag 00YH](https://stacks.math.columbia.edu/tag/00YH) in the Stacks Project.

**`Stacks.Sites.PointStalk.tStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean#L94).

> Tag 00YH, Lemma 7.37.1: the canonical natural transformation of stalk
> functors `t_stalk : (-)_{p'} ⟹ (-)_p` induced by `t : u' → u`.  Its components are
> `tStalkApp`; naturality is `tStalk_naturality` (part 2).

```lean
noncomputable def tStalk (uu uu' : C ⥤ Type u) (t : uu' ⟶ uu) :
    presheafStalk uu' ⟶ presheafStalk uu
```

**`Stacks.Sites.PointStalk.tStalkApp_stalkMk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean#L104). The attribute's comment: “(1)”.

> Part 1 (Well-defined + defining formula). The stalk transformation acts on a
> representative `[(U, x', s)]` by `[(U, x', s)] ↦ [(U, t_U(x'), s)]`; this is `ι_tStalkApp`
> at `op ⟨U, x'⟩` applied to `s`, since `(map t).op.obj (op ⟨U, x'⟩)` is `op ⟨U, t.app U x'⟩`.

```lean
theorem tStalkApp_stalkMk (uu uu' : C ⥤ Type u) (t : uu' ⟶ uu) (F : Cᵒᵖ ⥤ Type u)
    (U : C) (x' : uu'.obj U) (s : F.obj (Opposite.op U)) :
    tStalkApp uu uu' t F (stalkMk uu' F U x' s) = stalkMk uu F U (t.app U x') s
```

**`Stacks.Sites.PointStalk.tStalkApp_theta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctoriality.lean#L117). The attribute's comment: “(3)”.

> Part 3 (Compatibility with `t`, the agreement of Tag 00Y6).  Under the
> canonical identifications `θ^{u'}_U : u'(U) ≅ (h_U)_{p'}` and
> `θ^u_U : u(U) ≅ (h_U)_p`, the map `(t_stalk)_{h_U} : (h_U)_{p'} → (h_U)_p`
> corresponds to `t_U : u'(U) → u(U)`.  Since `θ` is `stalkMk … (𝟙 U)`, this is the case
> `F := yoneda.obj U`, `s := 𝟙 U` of `tStalkApp_stalkMk`.

```lean
theorem tStalkApp_theta (uu uu' : C ⥤ Type u) (t : uu' ⟶ uu) (U : C) (x' : uu'.obj U) :
    tStalkApp uu uu' t (yoneda.obj U) (theta uu' U x') = theta uu U (t.app U x')
```

## Tag 00YI, a definition

[Tag 00YI](https://stacks.math.columbia.edu/tag/00YI) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Point.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.Hom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/EnoughPoints.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Point/EnoughPoints.lean#L21) (StacksCore): “a morphism of points of a site is a transformation of the fibre functors in the opposite direction”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.37, Tag 00YG](https://stacks.math.columbia.edu/tag/00YG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
