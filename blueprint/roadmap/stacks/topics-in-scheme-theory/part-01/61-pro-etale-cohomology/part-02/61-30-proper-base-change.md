---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.isIso_proetaleCompletedBaseChangeMap_of_isProper
statement: formalized
proof: formalized
---

# 61.30 Proper base change

Section 61.30 of the Stacks Project, [Tag 09C8](https://stacks.math.columbia.edu/tag/09C8). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09C9, a theorem

[Tag 09C9](https://stacks.math.columbia.edu/tag/09C9) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isIso_proetaleCompletedBaseChangeMap_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/CompletedProperBaseChangeTheorem.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/CompletedProperBaseChangeTheorem.lean#L100).

> **Stacks 09C9 (proper base change for derived complete complexes).** Let `f : X ⟶ Y` be a
> proper morphism of schemes and `g : Y' ⟶ Y` a morphism, with base change square
> `sq : IsPullback g' f' f g`. Let `Λ` be a Noetherian ring and `I ⊆ Λ` an ideal such that `Λ/I` is
> torsion. Let `K` be an object of `D(X_proétale, Λ)` such that
> 1. `K` is derived complete,
> 2. `K ⊗^L_Λ Λ/Iⁿ` is bounded below with cohomology sheaves coming from `X_étale`, and
> 3. `Λ/Iⁿ` is a perfect `Λ`-module,
> for every `n ≥ 1`. Then the base change map `Lg^*_comp Rf_* K ⟶ Rf'_* L(g')^*_comp K` is an
> isomorphism.

```lean
theorem isIso_proetaleCompletedBaseChangeMap_of_isProper [IsNoetherianRing Λ] (I : Ideal Λ)
    (hI : AddMonoid.IsTorsion (Λ ⧸ I))
    {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) (g' : X' ⟶ X) (f' : X' ⟶ Y')
    (sq : IsPullback g' f' f g)
    (K : ProetaleDerivedCategory Λ X) (hK : IsDerivedComplete I K)
    (hbdd : ∀ n : ℕ, 1 ≤ n → ∃ a : ℤ, ((proetaleDerivedReduction Λ I X n).obj K).IsGE a)
    (het : ∀ n : ℕ, 1 ≤ n → ∀ q : ℤ, (Scheme.etaleInverseImage.{u, 0, u + 1} X Λ).essImage
      ((DerivedCategory.homologyFunctor _ q).obj ((proetaleDerivedReduction Λ I X n).obj K)))
    (hperf : ∀ n : ℕ, 1 ≤ n → StacksDraft.Perfect.IsPerfectModule (R := Λ) (Λ ⧸ I ^ n)) :
    IsIso (proetaleCompletedBaseChangeMap Λ I f g f' g' sq.w.symm K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.30, Tag 09C8](https://stacks.math.columbia.edu/tag/09C8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
