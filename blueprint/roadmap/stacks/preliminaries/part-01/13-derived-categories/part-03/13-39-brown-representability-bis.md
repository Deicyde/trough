---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.exists_iso_preadditiveYoneda_of_generating_of_factorsThroughSigma, CategoryTheory.Pretriangulated.exists_isTriangulated_rightAdjoint_of_generating_of_factorsThroughSigma
statement: formalized
proof: formalized
---

# 13.39 Brown representability, bis

Section 13.39 of the Stacks Project, [Tag 0GYF](https://stacks.math.columbia.edu/tag/0GYF). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GYG, a lemma

[Tag 0GYG](https://stacks.math.columbia.edu/tag/0GYG) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_preadditiveYoneda_of_generating_of_factorsThroughSigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/WeakBrownRepresentability.lean, line 803](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/WeakBrownRepresentability.lean#L803).

> **Brown representability**, weak version: let `𝒟` be a triangulated category with direct
> sums and let `E : ι → 𝒟` be a family of objects such that every nonzero object of `𝒟` receives a
> nonzero morphism from some `E i`, and such that every morphism from some `E i` to a countable
> direct sum `∐ X`, `X : ℕ → 𝒟`, factors through a direct sum `∐ fun n ↦ E (j n)` of members of
> the family via a direct sum of morphisms `E (j n) ⟶ X n`. Then a contravariant cohomological
> functor `H : 𝒟ᵒᵖ ⥤ AddCommGrpCat` which transforms direct sums into products is representable.

```lean
public theorem exists_iso_preadditiveYoneda_of_generating_of_factorsThroughSigma
    {D : Type u} [Category.{v} D] [Preadditive D] [HasZeroObject D] [HasShift D ℤ]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D] [IsTriangulated D]
    [HasCoproducts.{max w v} D] {ι : Type w} (E : ι → D)
    (hE : ∀ X : D, ¬ IsZero X → ∃ (i : ι) (f : E i ⟶ X), f ≠ 0)
    (hE' : ∀ (X : ℕ → D) (i : ι) (α : E i ⟶ ∐ X), ∃ (j : ℕ → ι) (β : ∀ n, E (j n) ⟶ X n)
      (γ : E i ⟶ ∐ fun n ↦ E (j n)), α = γ ≫ Limits.Sigma.map β)
    (H : Dᵒᵖ ⥤ AddCommGrpCat.{v}) [H.IsHomological]
    [∀ J : Type (max w v), PreservesLimitsOfShape (Discrete J) H] :
    ∃ X : D, Nonempty (preadditiveYoneda.obj X ≅ H)
```

## Tag 0GYH, a proposition

[Tag 0GYH](https://stacks.math.columbia.edu/tag/0GYH) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_isTriangulated_rightAdjoint_of_generating_of_factorsThroughSigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean#L636). References: SGA 4 XVII (2.2.13.1), “Triangulated case”.

> Let `D` be a triangulated category with direct sums and let `E : ι → D` be a family of
> objects satisfying conditions (1) and (2) of weak Brown representability
> [Stacks, Tag 0GYG]: every nonzero object of `D` receives a nonzero morphism from some `E i`, and
> every morphism from some `E i` to a countable direct sum `∐ X`, `X : ℕ → D`, factors through a
> direct sum `∐ fun n ↦ E (j n)` of members of the family via a direct sum of morphisms
> `E (j n) ⟶ X n`. Let `F : D ⥤ D'` be an exact functor of triangulated categories which transforms
> direct sums into direct sums. Then `F` has a right adjoint `G`, which is again exact: the
> adjunction `F ⊣ G` is a triangulated adjunction for a (unique) `Functor.CommShift ℤ` structure
> on `G`.

```lean
public theorem exists_isTriangulated_rightAdjoint_of_generating_of_factorsThroughSigma
    (F : D ⥤ D') [F.CommShift ℤ] [F.IsTriangulated]
    [∀ α : Type (max w v), PreservesColimitsOfShape (Discrete α) F]
    {ι : Type w} (E : ι → D)
    (hE : ∀ X : D, ¬ IsZero X → ∃ (i : ι) (f : E i ⟶ X), f ≠ 0)
    (hE' : ∀ (X : ℕ → D) (i : ι) (α : E i ⟶ ∐ X), ∃ (j : ℕ → ι) (β : ∀ n, E (j n) ⟶ X n)
      (γ : E i ⟶ ∐ fun n ↦ E (j n)), α = γ ≫ Limits.Sigma.map β) :
    ∃ (G : D' ⥤ D) (adj : F ⊣ G) (_ : G.CommShift ℤ), adj.IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.39, Tag 0GYF](https://stacks.math.columbia.edu/tag/0GYF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
