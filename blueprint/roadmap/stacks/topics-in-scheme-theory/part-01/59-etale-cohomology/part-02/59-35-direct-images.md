---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtalePresheafPushforward, AlgebraicGeometry.smallEtaleBaseChange_isCovering, AlgebraicGeometry.isSheafFor_baseChange_iff, CategoryTheory.Functor.op_comp_isSheaf_of_isSheaf, Stacks.EtaleCohomology.smallEtaleDirectImage, Stacks.EtaleCohomology.etaleAbelianHigherDirectImage
statement: formalized
proof: formalized
---

# 59.35 Direct images

Section 59.35 of the Stacks Project, [Tag 03PV](https://stacks.math.columbia.edu/tag/03PV). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03PW, a definition

[Tag 03PW](https://stacks.math.columbia.edu/tag/03PW) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePresheafPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystem.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystem.lean#L199).

> The direct image `f_*𝓕` of a presheaf of sets `𝓕` on the small étale site of `X` along
> `f : X ⟶ Y`: the presheaf on the small étale site of `Y` sending `V/Y` to `𝓕(V ×_Y X / X)`.

```lean
public def smallEtalePresheafPushforward {X Y : Scheme.{u}} (f : X ⟶ Y) :
    ((X.Etale)ᵒᵖ ⥤ Type w) ⥤ ((Y.Etale)ᵒᵖ ⥤ Type w)
```

## Tag 03PX, a remark

[Tag 03PX](https://stacks.math.columbia.edu/tag/03PX) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleBaseChange_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L205). The attribute's comment: “pullback of coverings”.

> Pulling an étale covering family of `S` back along `f : T ⟶ S` yields an étale covering
> family of `T`.

```lean
public theorem smallEtaleBaseChange_isCovering {S T : B.Scheme} (f : T ⟶ S)
    (E : Covering (SmallEtale B S.obj S.property))
    (hE : SmallEtale.IsCovering B S.obj S.property E) :
    SmallEtale.IsCovering B T.obj T.property
      ⟨(smallEtaleBaseChange B f).obj E.1, E.2.map (smallEtaleBaseChange B f)⟩
```

**`AlgebraicGeometry.isSheafFor_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L218). The attribute's comment: “sheaf condition”.

> The sheaf condition for a presheaf on the small étale category of `T`, tested against the
> base change of a covering family of `S`, agrees with the sheaf condition for its direct image
> tested against the original family.

```lean
public theorem isSheafFor_baseChange_iff {S T : B.Scheme} (f : T ⟶ S)
    (P : (SmallEtale B T.obj T.property)ᵒᵖ ⥤ Type v)
    (E : Covering (SmallEtale B S.obj S.property)) :
    Presieve.IsSheafFor ((smallEtaleBaseChange B f).op ⋙ P) E.2.presieve₀ ↔
      Presieve.IsSheafFor P (E.2.map (smallEtaleBaseChange B f)).presieve₀
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.op_comp_isSheaf_of_isSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.op_comp_isSheaf_of_isSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L227) (StacksFrontier): “direct image of a sheaf”.

## Tag 03PY, a definition

[Tag 03PY](https://stacks.math.columbia.edu/tag/03PY) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleDirectImage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDirectImages.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDirectImages.lean#L70). References: SGA 4½ Arcata (2.3), “f\_* definition”; SGA 4 VII (1.4).

> **The direct image, or pushforward, `f_*` along `f : X ⟶ Y`** on sheaves of sets of the
> small étale sites: the sheaf `f_* F` on `Y_étale` sends an étale `Y`-scheme `V` to `F(V ×_Y X)`,
> that is, `f_*` is precomposition with base change along `f`.

```lean
abbrev smallEtaleDirectImage :
    Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)) ⥤
      Sheaf (smallEtaleTopology Y) (Type (max (u + 1) v))
```

## Tag 04I2, a definition

[Tag 04I2](https://stacks.math.columbia.edu/tag/04I2) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleAbelianHigherDirectImage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDirectImages.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDirectImages.lean#L90). References: SGA 4½ Arcata (2.3), “R^p f\_* definition”; SGA 4½ Arcata (2.3.3), “higher direct images”.

> **The higher direct images `R^p f_*` along `f : X ⟶ Y`**: the right derived functors of the
> direct image `f_* : Ab(X_étale) ⥤ Ab(Y_étale)` on abelian sheaves of the small étale sites. The
> family with `p ≥ 1` is what the source calls the higher direct images.

```lean
abbrev etaleAbelianHigherDirectImage (p : ℕ) :
    Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.35, Tag 03PV](https://stacks.math.columbia.edu/tag/03PV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
