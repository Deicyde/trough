---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.conormalToDifferentials, Stacks.Groupoids.GroupoidScheme.epi_conormalToDifferentials, Stacks.Groupoids.GroupoidScheme.isIso_conormalToDifferentials, Stacks.Groupoids.GroupoidScheme.targetConormalToDifferentials, Stacks.Groupoids.GroupoidScheme.epi_targetConormalToDifferentials, Stacks.Groupoids.GroupoidScheme.isIso_targetConormalToDifferentials
statement: formalized
proof: formalized
---

# 40.4 Sheaf of differentials

Section 40.4 of the Stacks Project, [Tag 04R8](https://stacks.math.columbia.edu/tag/04R8). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04R9, a lemma

[Tag 04R9](https://stacks.math.columbia.edu/tag/04R9) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.conormalToDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L321). The attribute's comment: “the canonical map”.

> **[Stacks Project, Tag 04R9]: the canonical map `t^* 𝒞_{U/R} ⟶ Ω_{R/U}`**, from the pullback
> along the target morphism of the conormal sheaf of the identity section to the sheaf of
> relative differentials of the source morphism.
>
> It is the canonical map of conormal sheaves of [Stacks Project, Tag 01R4] attached to the
> cartesian square `Stacks.Groupoids.GroupoidScheme.isPullback_diagonal_divide`, whose source is
> `t^* 𝒞_{U/R}` and whose target is the conormal sheaf of the diagonal of `s`, followed by the
> inverse of the isomorphism of [Stacks Project, Tag 08S2] identifying that conormal sheaf with
> `Ω_{R/U}`. See the module docstring on which of `s` and `t` carries the differentials.

```lean
def conormalToDifferentials :
    (RingedSpaceModuleAdjunction.modulePullback G.target.left.toLRSHom.toShHom).obj
        (Stacks.Conormal.conormalSheaf G.identity.left) ⟶
      Scheme.Hom.relativeDifferentials G.source.left
```

**`Stacks.Groupoids.GroupoidScheme.epi_conormalToDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L338). The attribute's comment: “the canonical surjection”.

> **[Stacks Project, Tag 04R9]: the canonical map `t^* 𝒞_{U/R} ⟶ Ω_{R/U}` is surjective.**
> The sheaf of differentials of `R` over `U` is a quotient of the pullback along the target
> morphism of the conormal sheaf of the identity section.
>
> The map of conormal sheaves of the cartesian square is surjective by
> [Stacks Project, Tag 0473], and the comparison of [Stacks Project, Tag 08S2] is an isomorphism.

```lean
theorem epi_conormalToDifferentials : Epi G.conormalToDifferentials
```

**`Stacks.Groupoids.GroupoidScheme.isIso_conormalToDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L457). The attribute's comment: “an isomorphism when the source morphism is flat”.

> **[Stacks Project, Tag 04R9]: the canonical map `t^* 𝒞_{U/R} ⟶ Ω_{R/U}` is an isomorphism
> when the source morphism is flat.** With `R` over `U` via `s`, the sheaf of differentials of `R`
> over `U` is then *equal* to the pullback along the target morphism of the conormal sheaf of the
> identity section, not merely a quotient of it.
>
> Flatness of `s` makes division flat, by
> `Stacks.Groupoids.GroupoidScheme.flat_divide`: division is a base change of the target morphism,
> which is flat with the source morphism because the inverse is an isomorphism. The map of conormal
> sheaves of the cartesian square is then an isomorphism by the flat half of
> [Stacks Project, Tag 0473], and so is the comparison of [Stacks Project, Tag 08S2].

```lean
theorem isIso_conormalToDifferentials [Flat G.source.left] :
    IsIso G.conormalToDifferentials
```

**`Stacks.Groupoids.GroupoidScheme.targetConormalToDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L633). The attribute's comment: “the canonical map for the differentials of the target”.

> **[Stacks Project, Tag 04R9]: the canonical map `s^* 𝒞_{U/R} ⟶ Ω_{R/U}`**, with `R` over `U`
> via `t`. This is the reading of the tag in which the differentials are those of the target
> morphism; it is the previous map pulled back along the inverse, and is built here the same way,
> from the cartesian square
> `Stacks.Groupoids.GroupoidScheme.isPullback_diagonal_divideTarget` and the isomorphism of
> [Stacks Project, Tag 08S2].

```lean
def targetConormalToDifferentials :
    (RingedSpaceModuleAdjunction.modulePullback G.source.left.toLRSHom.toShHom).obj
        (Stacks.Conormal.conormalSheaf G.identity.left) ⟶
      Scheme.Hom.relativeDifferentials G.target.left
```

**`Stacks.Groupoids.GroupoidScheme.epi_targetConormalToDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L647). The attribute's comment: “the canonical surjection for the differentials of the target”.

> **[Stacks Project, Tag 04R9]: the canonical map `s^* 𝒞_{U/R} ⟶ Ω_{R/U}` is surjective**, with
> `R` over `U` via `t`. The sheaf of differentials of `R` seen as a scheme over `U` via the target
> morphism is a quotient of the pullback along the source morphism of the conormal sheaf of the
> identity section.

```lean
theorem epi_targetConormalToDifferentials : Epi G.targetConormalToDifferentials
```

**`Stacks.Groupoids.GroupoidScheme.isIso_targetConormalToDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/SheafOfDifferentials.lean#L751). The attribute's comment: “an isomorphism for the differentials of the target when the source map is flat”.

> **[Stacks Project, Tag 04R9]: the canonical map `s^* 𝒞_{U/R} ⟶ Ω_{R/U}` is an isomorphism
> when the source morphism is flat**, with `R` over `U` via `t`. This is the second reading of the
> tag, in which the differentials are those of the target morphism.
>
> Here flatness of `s` is used directly: division on this side is a base change of the source
> morphism, by `Stacks.Groupoids.GroupoidScheme.isPullback_divideTarget_fst`.

```lean
theorem isIso_targetConormalToDifferentials [Flat G.source.left] :
    IsIso G.targetConormalToDifferentials
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.4, Tag 04R8](https://stacks.math.columbia.edu/tag/04R8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
