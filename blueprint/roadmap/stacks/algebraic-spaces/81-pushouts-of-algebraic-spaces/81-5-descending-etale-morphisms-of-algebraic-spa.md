---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEffective_homDescentData_of_isEtale_of_isProper_isSurjective, AlgebraicGeometry.Space.isEffective_and_exists_isEtale_iso_of_isProper_isSurjective, AlgebraicGeometry.Space.isEquivalence_spacesEtaleModificationRestriction_of_isProper
statement: formalized
proof: formalized
---

# 81.5 Descending étale morphisms of algebraic spaces

Section 81.5 of the Stacks Project, [Tag 0GFZ](https://stacks.math.columbia.edu/tag/0GFZ). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GG0, a lemma

[Tag 0GG0](https://stacks.math.columbia.edu/tag/0GG0) in the Stacks Project.

**`AlgebraicGeometry.Space.isEffective_homDescentData_of_isEtale_of_isProper_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EtaleEffectiveAlongProper.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EtaleEffectiveAlongProper.lean#L96). The attribute's comment: “both the effectivity and the sharper form naming an étale V ⟶ Y, stated in the library's vocabulary for descent data of spaces; the translation between descent data of spaces and of étale sheaves and the proper case of Stacks 0GFW are carried as hypotheses”.

> **Stacks 0GG0.** Let `f : X ⟶ Y` be a proper surjective morphism of algebraic spaces over
> `S`. A descent datum relative to `f` whose underlying space is étale over `X` is effective;
> more precisely, it is isomorphic to the canonical descent datum of an algebraic space over `Y`
> which is étale over `Y`.
>
> Two statements of the source are carried as hypotheses rather than proved: `hproperCase` is the
> proper case of Stacks 0GFW, which is the case Stacks 0GG0 appeals to, and `hbridge` is the
> translation between descent data of spaces and descent data of spaces-étale sheaves.

```lean
theorem isEffective_homDescentData_of_isEtale_of_isProper_isSurjective
    (hproperCase : DescentEffectiveAlongProperSurjective B S hS)
    (hbridge : EtaleSpaceDescentEffectiveOfSheafDescent B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsurj : IsSurjective B S hS f.hom) (hproper : IsProper B S hS f.hom)
    (D : Descent.HomDescentData.{u, 0} f.hom Y.property X.property)
    (hD : IsEtale B S hS (D.obj PUnit.unit).hom) :
    Descent.HomDescentData.IsEffective.{u, 0} D ∧
      ∃ V : Descent.AlgebraicSpacesOver (B := B) (S := S) (hS := hS) Y.1,
        IsEtale B S hS V.obj.hom ∧
          Nonempty ((Descent.canonicalDescentFunctor.{u, 0} f.hom Y.property
            X.property).obj V ≅ D)
```

**`AlgebraicGeometry.Space.isEffective_and_exists_isEtale_iso_of_isProper_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EtaleEffectiveAlongProperUnconditional.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EtaleEffectiveAlongProperUnconditional.lean#L55). The attribute's comment: “both the effectivity and the sharper form naming an étale V ⟶ Y”.

> **Stacks 0GG0.** Let `f : X ⟶ Y` be a proper surjective morphism of algebraic spaces over
> `S`. Any descent datum `(U/X, φ)` relative to `f` (Stacks 0ADG) with `U` étale over `X` is
> effective (Stacks 0ADQ). More precisely, there exists an algebraic space `V` over `Y`, étale
> over `Y`, whose canonical descent datum is isomorphic to `(U/X, φ)`.

```lean
theorem isEffective_and_exists_isEtale_iso_of_isProper_isSurjective
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsurj : IsSurjective B S hS f.hom) (hproper : IsProper B S hS f.hom)
    (D : Descent.HomDescentData.{u, 0} f.hom Y.property X.property)
    (hD : IsEtale B S hS (D.obj PUnit.unit).hom) :
    Descent.HomDescentData.IsEffective.{u, 0} D ∧
      ∃ V : Descent.AlgebraicSpacesOver (B := B) (S := S) (hS := hS) Y.1,
        IsEtale B S hS V.obj.hom ∧
          Nonempty ((Descent.canonicalDescentFunctor.{u, 0} f.hom Y.property
            X.property).obj V ≅ D)
```

## Tag 0GG1, a lemma

[Tag 0GG1](https://stacks.math.columbia.edu/tag/0GG1) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_spacesEtaleModificationRestriction_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean#L86).

> **[Stacks, Tag 0GG1].** Let `S` be a scheme, let `f : Y ⟶ X` be a proper morphism of
> algebraic spaces over `S`, let `i : Z ⟶ X` be a closed immersion, and let `E = Z ×_X Y` with
> projections `j : E ⟶ Y` and `g : E ⟶ Z`. Suppose `f` is an isomorphism over the open complement
> `u : X ∖ Z ⟶ X` of `Z`: the projection `fU : V ⟶ X ∖ Z` of a fibre product
> `V = (X ∖ Z) ×_X Y` is an isomorphism. Then the functor
> `X_{spaces,étale} ⥤ Y_{spaces,étale} ×_{E_{spaces,étale}} Z_{spaces,étale}`,
> `V ↦ (V ×_X Y, V ×_X Z)`, is an equivalence of categories.

```lean
theorem isEquivalence_spacesEtaleModificationRestriction_of_isProper
    (hf : IsProper B S hS f.hom) (hi : IsClosedImmersion B S hS i.hom)
    (sq : IsPullback j g f i)
    {V : AlgebraicSpaces B S hS} (w' : V ⟶ Y)
    (fU : V ⟶ closedImmersionComplement B S hS i hi) [IsIso fU]
    (sqU : IsPullback w' fU f (closedImmersionComplementHom B S hS i hi)) :
    (spacesEtaleModificationRestriction B S hS f i j g sq.w).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.5, Tag 0GFZ](https://stacks.math.columbia.edu/tag/0GFZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
