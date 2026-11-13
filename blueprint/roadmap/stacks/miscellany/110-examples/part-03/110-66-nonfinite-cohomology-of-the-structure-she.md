---
declaration: section
origin: cited
lean: Stacks.Examples.exists_projective_not_finite_globalSections
statement: formalized
proof: formalized
---

# 110.66 Nonfinite cohomology of the structure sheaf of a projective scheme

Section 110.66 of the Stacks Project, [Tag 0HAS](https://stacks.math.columbia.edu/tag/0HAS). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HAT, a lemma

[Tag 0HAT](https://stacks.math.columbia.edu/tag/0HAT) in the Stacks Project.

**`Stacks.Examples.exists_projective_not_finite_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/NonfiniteGlobalSections.lean, line 839](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Scheme/NonfiniteGlobalSections.lean#L839).

> **Stacks Project, Tag 0HAT (Non-finite `H⁰`).**
> 1. There exist a ring `R` and a projective scheme `X` over `R` such that `H⁰(X, 𝒪_X)` is not a
>    finite `R`-module. Here `f : X ⟶ Spec R` is projective both in the sense of Tag 01W8
>    (`AlgebraicGeometry.IsProjective`) and in the H-projective sense
>    (`AlgebraicGeometry.IsProjectiveMorphism`, a closed immersion into `𝐏ⁿ_R` over `R`), and
>    `H⁰(X, 𝒪_X) = Γ(X, 𝒪_X)` is an `R`-module through `R ≅ Γ(Spec R, 𝒪) → Γ(X, 𝒪_X)`.
> 2. There exist a ring `R` and a quasi-coherent module `𝓕` of finite type on `𝐏¹_R` such that
>    `H⁰(𝐏¹_R, 𝓕)` is not a finite `R`-module, `H⁰(𝐏¹_R, 𝓕) = Γ(𝐏¹_R, 𝓕)` being an `R`-module
>    through the structure morphism `𝐏¹_R ⟶ Spec R`.
>
> Following the source, `R` is a ring with an ideal `I` that is not finitely generated, `X` is
> `Proj(R[x, y] / x y I)` (`Stacks.Examples.NonfiniteGlobalSections.pinchScheme`) and `𝓕 = i_* 𝒪_X`
> for the closed immersion `i : X ⟶ 𝐏¹_R` (`Stacks.Examples.NonfiniteGlobalSections.pinchSheaf`);
> the ring is `k[x₀, x₁, …]/(x₀², x₁², …)` over `k = ℚ`, whose ideal `(x₀, x₁, …)` is not finitely
> generated (`Stacks.Examples.infiniteSquareZeroVariableIdeal_not_fg`). The ring and both schemes
> live in an arbitrary universe.

```lean
theorem exists_projective_not_finite_globalSections :
    (∃ (R : Type u) (_ : CommRing R) (X : Scheme.{u}) (f : X ⟶ Spec (.of R)),
      IsProjective f ∧ IsProjectiveMorphism f ∧
        ¬ ((Scheme.ΓSpecIso (.of R)).inv ≫ f.appTop).hom.Finite) ∧
    (∃ (R : Type u) (_ : CommRing R) (F : (projectiveSpaceOverRing 1 (.of R)).Modules),
      F.IsQuasicoherent ∧ F.IsFiniteType ∧
        ¬ Module.Finite R ((ModuleCat.restrictScalars ((Scheme.ΓSpecIso (.of R)).inv ≫
          (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R)).appTop).hom).obj
            (F.val.obj (Opposite.op ⊤))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.66, Tag 0HAS](https://stacks.math.columbia.edu/tag/0HAS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
