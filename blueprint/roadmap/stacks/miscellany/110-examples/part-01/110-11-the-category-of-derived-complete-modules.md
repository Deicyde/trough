---
declaration: section
origin: cited
lean: Stacks.Examples.derivedCompleteModules_abelian_exact_colimits_not_grothendieck
statement: formalized
proof: formalized
---

# 110.11 The category of derived complete modules

Section 110.11 of the Stacks Project, [Tag 0ARC](https://stacks.math.columbia.edu/tag/0ARC). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ARD, a lemma

[Tag 0ARD](https://stacks.math.columbia.edu/tag/0ARD) in the Stacks Project.

**`Stacks.Examples.derivedCompleteModules_abelian_exact_colimits_not_grothendieck`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/DerivedCompleteModules.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/DerivedCompleteModules.lean#L325).

> **Stacks 0ARD.** Let `A` be a ring and `I ⊂ A` an ideal. The category `C` of derived complete
> `A`-modules is abelian, and the inclusion `F : C ⥤ ModuleCat A` is exact and preserves all limits.
> If `I` is finitely generated, then `C` has all direct sums and all colimits.
>
> These are not preserved by `F` in general, and filtered colimits in `C` are not exact in general,
> so that `C` is not a Grothendieck abelian category: all of this fails for `A = ℤ_[2]` and
> `I = (2)`, where `F` does not preserve countable direct sums or colimits, sequential colimits in
> `C` are not exact, `C` does not satisfy AB5, and no abelian structure on `C` is Grothendieck.

```lean
theorem derivedCompleteModules_abelian_exact_colimits_not_grothendieck :
    (∀ (A : Type u) [CommRing A] (I : Ideal A),
      letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
        Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
      let P : ObjectProperty (ModuleCat.{u} A) := fun M => IsDerivedCompleteModule I M
      let C := P.FullSubcategory
      let F : C ⥤ ModuleCat.{u} A := P.ι
      Nonempty (Abelian C) ∧ PreservesFiniteLimits F ∧ PreservesFiniteColimits F ∧
        HasLimits C ∧ PreservesLimits F ∧
        (I.FG → HasCoproducts.{u} C ∧ HasColimits C)) ∧
    (letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat (ℤ_[2]))) :=
        Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
      let I : Ideal ℤ_[2] := Ideal.span {2}
      let P : ObjectProperty (ModuleCat (ℤ_[2])) := fun M => IsDerivedCompleteModule I M
      let C := P.FullSubcategory
      let F : C ⥤ ModuleCat (ℤ_[2]) := P.ι
      I.FG ∧ ¬ PreservesColimitsOfShape (Discrete ℕ) F ∧ ¬ PreservesColimits F ∧
        (∃ _ : HasColimitsOfShape ℕ C, ¬ HasExactColimitsOfShape ℕ C) ∧
        (∃ _ : HasFilteredColimits C, ¬ AB5 C) ∧
        ∀ [Abelian C], ¬ IsGrothendieckAbelian C)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.11, Tag 0ARC](https://stacks.math.columbia.edu/tag/0ARC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
