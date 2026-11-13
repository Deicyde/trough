---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isImmersion_isFinitePresentation_factorsThrough_iff_hasDescentAt
statement: formalized
proof: formalized
---

# 76.53 Theorem of the cube

Section 76.53 of the Stacks Project, [Tag 0D22](https://stacks.math.columbia.edu/tag/0D22). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D23, a lemma

[Tag 0D23](https://stacks.math.columbia.edu/tag/0D23) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isImmersion_isFinitePresentation_factorsThrough_iff_hasDescentAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescentLocus/Theorem.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DescentLocus/Theorem.lean#L294).

> Let `f : X ⟶ Y` be a flat, proper morphism of finite presentation of algebraic spaces over
> `S`, and `E` a finite locally free `𝒪_X`-module. Assume that for every `g : Y' ⟶ Y`, with base
> change `f' : X' = X ×_Y Y' ⟶ Y'`, the map `𝒪_{Y'} ⟶ f'_*𝒪_{X'}` is an isomorphism. Then there
> is an immersion `j : Z ⟶ Y` of finite presentation such that a morphism `g : Y' ⟶ Y` factors
> through `j` exactly when there is a finite locally free `𝒪_{Y'}`-module `N` with
> `(f')^*N ≅ (g')^*E` (`AlgebraicGeometry.Space.HasDescentAt`; the source's `(g')^*L` is a typo for
> `(g')^*E`).

```lean
theorem exists_isImmersion_isFinitePresentation_factorsThrough_iff_hasDescentAt
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hfl : IsFlat B S hS f.hom)
    (hP : IsProper B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (E : Modules.{u, u} B S hS X.1 X.2) (hE : SheafOfModules.IsFiniteLocallyFree E)
    (hiso : ∀ {Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y),
      IsIso (structureSharp B S hS (pullback.snd f g))) :
    ∃ (Z : AlgebraicSpaces B S hS) (j : Z ⟶ Y),
      IsImmersion B S hS j.hom ∧ IsFinitePresentation B S hS j.hom ∧
      ∀ {Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y),
        (∃ h : Y' ⟶ Z, h ≫ j = g) ↔ HasDescentAt f E g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.53, Tag 0D22](https://stacks.math.columbia.edu/tag/0D22)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
