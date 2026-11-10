---
declaration: section
origin: cited
lean: Stacks.Discriminant.kaehlerDifferent, Stacks.Discriminant.kaehlerDifferent_comap, Stacks.Discriminant.kaehlerDifferentSubschemeIsoPullback, Stacks.Discriminant.kaehlerDifferentSubschemeIsoPullback_hom_fst, Stacks.Discriminant.range_kaehlerDifferent_subschemeι, Stacks.Discriminant.fittingIdeal_kaehlerDifferential_quotient_mvPolynomial
statement: formalized
proof: formalized
---

# 49.7 The Kähler different

Section 49.7 of the Stacks Project, [Tag 0BVV](https://stacks.math.columbia.edu/tag/0BVV). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BVW, a definition

[Tag 0BVW](https://stacks.math.columbia.edu/tag/0BVW) in the Stacks Project.

**`Stacks.Discriminant.kaehlerDifferent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/Basic.lean#L47).

> **Stacks Project, Tag 0BVW.** The Kähler different of a morphism of schemes which is
> locally of finite type: the zeroth Fitting ideal sheaf of its sheaf of relative
> differentials.

```lean
noncomputable abbrev kaehlerDifferent {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] : Y.IdealSheafData
```

## Tag 0BVX, a lemma

[Tag 0BVX](https://stacks.math.columbia.edu/tag/0BVX) in the Stacks Project.

**`Stacks.Discriminant.kaehlerDifferent_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean#L77). The attribute's comment: “equality of the ideal sheaves cutting out R' and the inverse image of R”.

> **Stacks Project, Tag 0BVX.** For a cartesian square of schemes with right edge `f : Y ⟶ X`
> locally of finite type, left edge `f' : Y' ⟶ X'` and top edge `g' : Y' ⟶ Y`, the Kähler
> different of `f'` is the inverse image along `g'` of the Kähler different of `f`.

```lean
theorem kaehlerDifferent_comap {Y' Y X' X : Scheme.{u}} (g' : Y' ⟶ Y) (f' : Y' ⟶ X')
    (f : Y ⟶ X) (g : X' ⟶ X) (h : IsPullback g' f' f g) [LocallyOfFiniteType f] :
    @kaehlerDifferent Y' X' f'
        (locallyOfFiniteType_isStableUnderBaseChange.of_isPullback h inferInstance) =
      (kaehlerDifferent f).comap g'
```

**`Stacks.Discriminant.kaehlerDifferentSubschemeIsoPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean#L96). The attribute's comment: “the induced isomorphism of closed subschemes”.

> **Stacks Project, Tag 0BVX.** The isomorphism from the closed subscheme `R'` of `Y'` cut out
> by the Kähler different of the base change `f'` to the fibre product `Y' ×_Y R`, where `R ⊆ Y` is
> cut out by the Kähler different of `f`.

```lean
noncomputable def kaehlerDifferentSubschemeIsoPullback {Y' Y X' X : Scheme.{u}} (g' : Y' ⟶ Y)
    (f' : Y' ⟶ X') (f : Y ⟶ X) (g : X' ⟶ X) (h : IsPullback g' f' f g)
    [LocallyOfFiniteType f] :
    (@kaehlerDifferent Y' X' f'
        (locallyOfFiniteType_isStableUnderBaseChange.of_isPullback h inferInstance)).subscheme ≅
      pullback g' (kaehlerDifferent f).subschemeι
```

**`Stacks.Discriminant.kaehlerDifferentSubschemeIsoPullback_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/BaseChange.lean#L109). The attribute's comment: “the induced isomorphism of closed subschemes is over Y'”.

> **Stacks Project, Tag 0BVX.** The isomorphism `R' ≅ Y' ×_Y R` of Tag 0BVX is an isomorphism
> of schemes over `Y'`: composing it with the first projection is the closed immersion of `R'` into
> `Y'`.

```lean
theorem kaehlerDifferentSubschemeIsoPullback_hom_fst {Y' Y X' X : Scheme.{u}} (g' : Y' ⟶ Y)
    (f' : Y' ⟶ X') (f : Y ⟶ X) (g : X' ⟶ X) (h : IsPullback g' f' f g)
    [LocallyOfFiniteType f] :
    (kaehlerDifferentSubschemeIsoPullback g' f' f g h).hom ≫ pullback.fst _ _ =
      Scheme.IdealSheafData.subschemeι (@kaehlerDifferent Y' X' f'
        (locallyOfFiniteType_isStableUnderBaseChange.of_isPullback h inferInstance))
```

## Tag 0BVY, a lemma

[Tag 0BVY](https://stacks.math.columbia.edu/tag/0BVY) in the Stacks Project.

**`Stacks.Discriminant.range_kaehlerDifferent_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/UnramifiedLocus.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/UnramifiedLocus.lean#L88).

> **Stacks Project, Tag 0BVY** and **Stacks Project, Tag 0C3J.** For a morphism of schemes
> `f : Y ⟶ X` locally of finite type, the closed subscheme `R ⊆ Y` cut out by the Kähler different
> of `f` — equivalently, by the zeroth Fitting ideal of `Ω_{Y/X}`, which is what the Kähler
> different is — has as its underlying subset of `Y` exactly the set of points at which `f` is not
> unramified.

```lean
theorem range_kaehlerDifferent_subschemeι {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] :
    Set.range (kaehlerDifferent f).subschemeι = {y : Y | ¬ UnramifiedAt f y}
```

## Tag 0BVZ, a lemma

[Tag 0BVZ](https://stacks.math.columbia.edu/tag/0BVZ) in the Stacks Project.

**`Stacks.Discriminant.fittingIdeal_kaehlerDifferential_quotient_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/Jacobian.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/Jacobian.lean#L165). References: SGA 1 I (7.2), “more general”.

> **Stacks Project, Tag 0BVZ.** The Kähler different of an algebra presented by `n` equations
> in `n` variables is generated by the determinant of its Jacobian matrix.

```lean
theorem fittingIdeal_kaehlerDifferential_quotient_mvPolynomial
    (A : Type u) [CommRing A] (n : ℕ)
    (f : Fin n → MvPolynomial (Fin n) A) :
    let I : Ideal (MvPolynomial (Fin n) A) := Ideal.span (Set.range f)
    let B := MvPolynomial (Fin n) A ⧸ I
    fittingIdeal (M := Ω[B⁄A]) 0 =
      Ideal.span {Ideal.Quotient.mk I
                    (Matrix.of (fun i j : Fin n => MvPolynomial.pderiv j (f i))).det}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.7, Tag 0BVV](https://stacks.math.columbia.edu/tag/0BVV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
