---
declaration: section
origin: cited
lean: Stacks.Examples.exists_flat_algebra_not_filteredColimit
statement: formalized
proof: formalized
---

# 110.78 Flat maps are not directed limits of finitely presented flat maps

Section 110.78 of the Stacks Project, [Tag 0ATE](https://stacks.math.columbia.edu/tag/0ATE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ATF, a lemma

[Tag 0ATF](https://stacks.math.columbia.edu/tag/0ATF) in the Stacks Project.

**`Stacks.Examples.exists_flat_algebra_not_filteredColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/FlatAlgebraNotFilteredColimitAlternatives.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/FlatAlgebraNotFilteredColimitAlternatives.lean#L43).

> There is a commutative ring with a flat algebra which is the colimit of no filtered diagram of
> finitely presented flat algebras; the ring may be chosen to be a finite type algebra over `𝔽_p`
> for a prime `p`, or a one-dimensional Noetherian local ring whose residue field has
> characteristic zero.

```lean
theorem exists_flat_algebra_not_filteredColimit :
    (∃ (A : CommRingCat.{max u v}) (B : CommAlgCat.{max u v} A), Module.Flat A B ∧
      ∀ (J : Type v) [SmallCategory J] [IsFiltered J] (F : J ⥤ CommAlgCat.{max u v} A),
        (∀ j, Algebra.FinitePresentation A (F.obj j) ∧ Module.Flat A (F.obj j)) →
          ∀ c : Cocone F, c.pt = B → IsEmpty (IsColimit c)) ∧
    (∃ p : ℕ, p.Prime ∧ ∃ (A : CommRingCat.{max u v}) (_ : Algebra (ZMod p) A),
      Algebra.FiniteType (ZMod p) A ∧ ∃ B : CommAlgCat.{max u v} A, Module.Flat A B ∧
        ∀ (J : Type v) [SmallCategory J] [IsFiltered J] (F : J ⥤ CommAlgCat.{max u v} A),
          (∀ j, Algebra.FinitePresentation A (F.obj j) ∧ Module.Flat A (F.obj j)) →
            ∀ c : Cocone F, c.pt = B → IsEmpty (IsColimit c)) ∧
    (∃ A : CommRingCat.{max u v}, ∃ hloc : IsLocalRing A,
      letI : IsLocalRing A := hloc
      IsNoetherianRing A ∧ ringKrullDim A = 1 ∧
        CharZero (IsLocalRing.ResidueField A) ∧
          ∃ B : CommAlgCat.{max u v} A, Module.Flat A B ∧
            ∀ (J : Type v) [SmallCategory J] [IsFiltered J]
              (F : J ⥤ CommAlgCat.{max u v} A),
              (∀ j, Algebra.FinitePresentation A (F.obj j) ∧
                Module.Flat A (F.obj j)) →
                ∀ c : Cocone F, c.pt = B → IsEmpty (IsColimit c))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.78, Tag 0ATE](https://stacks.math.columbia.edu/tag/0ATE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
