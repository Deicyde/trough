---
declaration: section
origin: cited
lean: Stacks.BoundedCohomologicalDimension.main_theorem_07k6, CategoryTheory.Functor.hasRightDerivedFunctor_of_isZero_rightDerived, CategoryTheory.Functor.hasLeftDerivedFunctor_of_isZero_leftDerived
statement: formalized
proof: formalized
---

# 13.32 Bounded cohomological dimension

Section 13.32 of the Stacks Project, [Tag 07K5](https://stacks.math.columbia.edu/tag/07K5). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07K6, a lemma

[Tag 07K6](https://stacks.math.columbia.edu/tag/07K6) in the Stacks Project.

**`Stacks.BoundedCohomologicalDimension.main_theorem_07k6`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedCohomologicalDimension/Resolution/DescentAndFreeze.lean, line 828](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedCohomologicalDimension/Resolution/DescentAndFreeze.lean#L828).

> Let `A` be an abelian category and `d : Ob(A) → ℕ∞` a function satisfying the
> bounded cohomological dimension hypotheses. Let `K•` be a cochain complex with
> `n + d(K^n) → -∞` as `n → -∞`. Then there exists a complex `L•` together with a
> quasi-isomorphism `K• → L•` such that `d(L^n) = 0` for all `n ∈ ℤ`.

```lean
alias main_theorem_07k6
```

## Tag 07K7, a lemma

[Tag 07K7](https://stacks.math.columbia.edu/tag/07K7) in the Stacks Project.

**`CategoryTheory.Functor.hasRightDerivedFunctor_of_isZero_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedBoundedCohomologicalDimension.lean, line 1201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedBoundedCohomologicalDimension.lean#L1201). References: SGA 4½ Etat 0 (3.1.9), “(2) right, σ=F-acyclics”; SGA 4½ Etat 0 (4.2.3.2), “right case: Rf on D(A)”.

> **Stacks 07K7.** Let `F : 𝒜 ⥤ ℬ` be a left exact functor of abelian categories, let `P` be
> the class of objects `X` which are right acyclic for `F`, i.e. such that `X[0]` computes the right
> derived functor of `K⁺(𝒜) ⥤ D⁺(ℬ)` in the sense of Stacks 05SX, and let
> `RF⁺ : D⁺(𝒜) ⥤ D⁺(ℬ)` be a right derived functor of `F` on the bounded below derived category.
> Assume that every object of `𝒜` is a subobject of an object of `P`, and that
> `R ^ n F = H ^ n (RF⁺ (- [0])) = 0` for some `n : ℕ`. Then
>
> 1. the right derived functor `RF : D(𝒜) ⥤ D(ℬ)` exists,
> 2. every complex is the source of a quasi-isomorphism into a complex with terms in `P`,
> 3. every complex with terms in `P` computes `RF`, and
> 4. for every `E` in `D(𝒜)`, `H ^ i (RF (τ_{≤ a} E)) ⟶ H ^ i (RF E)` is an isomorphism for
>    `i ≤ a`, `H ^ i (RF E) ⟶ H ^ i (RF (τ_{≥ b - n + 1} E))` is an isomorphism for `i ≥ b`,
>    and `RF` shifts the range of degrees in which `E` lives by at most `n - 1` on the right.
>
> Right acyclicity is the source's notion (Stacks 0157(3) with 05SX); invertibility of the unit of
> `RF⁺` at `X[0]` would be a weaker condition for a non-pointwise Kan extension (see the module
> documentation).

```lean
public theorem hasRightDerivedFunctor_of_isZero_rightDerived
    (F : A ⥤ B) [F.Additive] [PreservesFiniteLimits F]
    (RF' : DerivedCategory.Plus A ⥤ DerivedCategory.Plus B)
    (α' : F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶
      DerivedCategory.Plus.Qh ⋙ RF')
    [RF'.IsRightDerivedFunctor α' (HomotopyCategory.Plus.quasiIso A)]
    (P : ObjectProperty A)
    (hP : ∀ X : A, P X ↔ (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
      (HomotopyCategory.Plus.quasiIso A) ((HomotopyCategory.Plus.singleFunctor A 0).obj X))
    (hmono : ∀ X : A, ∃ (Y : A) (i : X ⟶ Y) (_ : Mono i), P Y)
    (n : ℕ) (hn : ∀ X : A, IsZero ((DerivedCategory.Plus.homologyFunctor B n).obj
      (RF'.obj ((DerivedCategory.Plus.singleFunctor A 0).obj X)))) :
    (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasRightDerivedFunctor
        (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ∧
      (∀ K : CochainComplex A ℤ, ∃ (L : CochainComplex A ℤ) (f : K ⟶ L) (_ : QuasiIso f),
        ∀ i : ℤ, P (L.X i)) ∧
      ∀ (RF : DerivedCategory A ⥤ DerivedCategory B)
        (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
          DerivedCategory.Qh ⋙ RF)
        [RF.IsRightDerivedFunctor α (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))],
        (∀ L : CochainComplex A ℤ, (∀ i : ℤ, P (L.X i)) →
            IsIso (α.app ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj L))) ∧
          ∀ E : DerivedCategory A,
            (∀ a i : ℤ, i ≤ a → IsIso ((DerivedCategory.homologyFunctor B i).map
                (RF.map ((TStructure.t.truncLEι a).app E)))) ∧
              (∀ b i : ℤ, b ≤ i → IsIso ((DerivedCategory.homologyFunctor B i).map
                (RF.map ((TStructure.t.truncGEπ (b - (n : ℤ) + 1)).app E)))) ∧
                (∀ a : ℤ, E.IsGE a → (RF.obj E).IsGE a) ∧
                  ∀ b : ℤ, E.IsLE b → (RF.obj E).IsLE (b + (n : ℤ) - 1)
```

## Tag 07K8, a lemma

[Tag 07K8](https://stacks.math.columbia.edu/tag/07K8) in the Stacks Project.

**`CategoryTheory.Functor.hasLeftDerivedFunctor_of_isZero_leftDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedCohomologicalDimension.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedCohomologicalDimension.lean#L452). References: SGA 4½ Etat 0 (3.1.9), “(2) left, σ=F-acyclics”; SGA 4½ Etat 0 (4.2.3.2), “left case: Lf on D(A)”.

> **Stacks 07K8.** Let `F : 𝒜 ⥤ ℬ` be a right exact functor of abelian categories, let
> `LF' : D⁺(𝒜ᵒᵖ) ⥤ D⁺(ℬᵒᵖ)` be a right derived functor of `F.op` with unit `α'` — this is the
> left derived functor of `F` on the bounded above derived category `D⁻(𝒜)` — and let `P` be the
> class of objects which are left acyclic for `F`, i.e. of those `X` such that `Xᵒᵖ[0]` computes
> the right derived functor of `F.op` in the sense of Stacks 05SX. Assume that every object of
> `𝒜` is a quotient of an object of `P`, and that `L ^ n F = H ^ (-n) (LF (- [0])) = 0` for
> some `n : ℕ`. Then
>
> 1. the left derived functor `LF : D(𝒜) ⥤ D(ℬ)` exists,
> 2. every complex is the target of a quasi-isomorphism from a complex with terms in `P`,
> 3. every complex with terms in `P` computes `LF`, and
> 4. for every `E` in `D(𝒜)`, `H ^ i (LF (τ_{≤ a + n - 1} E)) ⟶ H ^ i (LF E)` is an isomorphism
>    for `i ≤ a`, `H ^ i (LF E) ⟶ H ^ i (LF (τ_{≥ b} E))` is an isomorphism for `i ≥ b`, and `LF`
>    shifts the range of degrees in which `E` lives by at most `n - 1` on the left.

```lean
public theorem hasLeftDerivedFunctor_of_isZero_leftDerived
    (F : A ⥤ B) [F.Additive] [PreservesFiniteColimits F]
    (LF' : DerivedCategory.Plus Aᵒᵖ ⥤ DerivedCategory.Plus Bᵒᵖ)
    (α' : F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶
      DerivedCategory.Plus.Qh ⋙ LF')
    [LF'.IsRightDerivedFunctor α' (HomotopyCategory.Plus.quasiIso Aᵒᵖ)]
    (P : ObjectProperty A)
    (hP : ∀ X : A, P X ↔
      (F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
      (HomotopyCategory.Plus.quasiIso Aᵒᵖ)
      ((HomotopyCategory.Plus.singleFunctor Aᵒᵖ 0).obj (Opposite.op X)))
    (hepi : ∀ X : A, ∃ (Y : A) (p : Y ⟶ X) (_ : Epi p), P Y)
    (n : ℕ) (hn : ∀ X : A, IsZero ((DerivedCategory.Plus.homologyFunctor Bᵒᵖ n).obj
      (LF'.obj ((DerivedCategory.Plus.singleFunctor Aᵒᵖ 0).obj (Opposite.op X))))) :
    (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasLeftDerivedFunctor
        (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ∧
      (∀ K : CochainComplex A ℤ, ∃ (L : CochainComplex A ℤ) (f : L ⟶ K) (_ : QuasiIso f),
        ∀ i : ℤ, P (L.X i)) ∧
      ∀ (LF : DerivedCategory A ⥤ DerivedCategory B)
        (α : DerivedCategory.Qh ⋙ LF ⟶
          F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
        [LF.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))],
        (∀ L : CochainComplex A ℤ, (∀ i : ℤ, P (L.X i)) →
            IsIso (α.app ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj L))) ∧
          ∀ E : DerivedCategory A,
            (∀ a i : ℤ, i ≤ a → IsIso ((DerivedCategory.homologyFunctor B i).map
                (LF.map ((TStructure.t.truncLEι (a + (n : ℤ) - 1)).app E)))) ∧
              (∀ b i : ℤ, b ≤ i → IsIso ((DerivedCategory.homologyFunctor B i).map
                (LF.map ((TStructure.t.truncGEπ b).app E)))) ∧
                (∀ a : ℤ, E.IsGE a → (LF.obj E).IsGE (a - (n : ℤ) + 1)) ∧
                  ∀ b : ℤ, E.IsLE b → (LF.obj E).IsLE b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.32, Tag 07K5](https://stacks.math.columbia.edu/tag/07K5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
