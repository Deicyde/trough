---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ComplexesSituation.complexesIsom_finitePresentation_and_affine_overQuasiCompactNegativeExtLocus, AlgebraicGeometry.Space.ComplexesSituation.isQuasiSeparated_and_isLocallyOfFinitePresentation_complexesAlgebraicStack
statement: formalized
proof: formalized
---

# 108.12 Properties of moduli of complexes on a proper morphism

Section 108.12 of the Stacks Project, [Tag 0DPV](https://stacks.math.columbia.edu/tag/0DPV). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DPW, a lemma

[Tag 0DPW](https://stacks.math.columbia.edu/tag/0DPW) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.complexesIsom_finitePresentation_and_affine_overQuasiCompactNegativeExtLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesDiagonalProved.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesDiagonalProved.lean#L401). The attribute's comment: “Corrected statement (Stacks erratum): the source asserts that the diagonal of Complexes\_\{X/B} over B is affine and of finite presentation; the 'affine' part is false (counterexample: X = P^1 over A^2\_k with complexes E = [O(-2) -s-> O], s = a(x^2 - y^2) + bxy, and E' = E ⊗ O(2), for which Isom(E, E') is empty over the origin and has a section over A^2 minus the origin, so is not affine over A^2). Formalized: the diagonal over B is representable by algebraic spaces and of finite presentation, and for (T, E), (T, E') the functor Isom(E, E') factors through the open W(E, E') ∩ W(E', E) of 0DLC, whose inclusion into T is quasi-compact, and is affine and of finite presentation over it; so the diagonal is quasi-affine and of finite presentation.”.

> **Stacks 0DPW, corrected: the diagonal of `Complexes_{X/B}` over `B` is quasi-affine and of
> finite presentation.**  Let `f : X ⟶ B` be proper, flat and of finite presentation
> (Situation 0DLE), and let `x = (T, E)`, `y = (T, E')` be objects of `Complexes_{X/B}` over the
> same scheme `T` and the same morphism `T ⟶ B`, so that `E`, `E'` are `B`-perfect objects of
> `D(𝒪_{X_T})` with vanishing negative self-Exts on the fibres; the base change of the diagonal of
> `Complexes_{X/B}` over `B` along the `T`-point `(x, y)` of `Complexes_{X/B} ×_B Complexes_{X/B}`
> is `Isom(x, y)`.  Then:
>
> 1. the presheaf `Isom(x, y)` on `(Sch/T)` is the relative derived Isom functor
>    `T' ↦ Isom(E_{T'}, E'_{T'})` of `X_T ⟶ T`;
> 2. it is an algebraic space of finite presentation over `T`: the diagonal of `Complexes_{X/B}`
>    over `B` is representable by algebraic spaces and of finite presentation;
> 3. the opens `W(E, E')` and `W(E', E)` of `T` of Stacks 0DLC, part (1), exist;
> 4. for these opens (`W(E, E')`: the field points `y` of `T` with `Ext^i(E_y, E'_y) = 0` for
>    `i < 0`, and symmetrically), the inclusion of `W(E, E') ∩ W(E', E)` into `T` is
>    quasi-compact, and `Isom(x, y)` factors through this open and is affine and of finite
>    presentation over it.
>
> **This is the corrected form of Stacks 0DPW**, not the statement as written.  The source asserts
> that the diagonal is affine and of finite presentation; the "affine" part is false (its proof
> applies Stacks 0DLC, part (3), as if `W(E, E')` were all of `T`): for `X = P¹` over `A²_k`,
> `E = [O(-2) --s--> O]` with `s = a(x² - y²) + bxy` and `E' = E ⊗ O(2)`, `Isom(E, E')` is empty
> over the origin and has a section over `A² ∖ 0`, so it is not affine over `A²`.

```lean
theorem complexesIsom_finitePresentation_and_affine_overQuasiCompactNegativeExtLocus :
    Nonempty ((complexesFunctor D).isomPresheaf ⟨A, rfl⟩ ⟨sameTest A E' h₁ h₂, rfl⟩ ≅
      (overSchemeTest A.T.left).op ⋙ relativeDerivedIsomFunctor (D.projection A.T) A.E E') ∧
    IsFinitePresentationAlgebraicSpaceOver ((schemeSpaceFunctor B S hS).obj A.T.left)
      (relativeDerivedIsomFunctor (D.projection A.T) A.E E') ∧
    (∃ W₁ : OpenSubspaces B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).1,
      IsNegativeExtLocus (D.projection A.T) A.E E' W₁) ∧
    (∃ W₂ : OpenSubspaces B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).1,
      IsNegativeExtLocus (D.projection A.T) E' A.E W₂) ∧
    ∀ (W₁ W₂ : OpenSubspaces B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).1),
      IsNegativeExtLocus (D.projection A.T) A.E E' W₁ →
      IsNegativeExtLocus (D.projection A.T) E' A.E W₂ →
      IsQuasiCompact B S hS (openSubspaceImmersion B S hS ⟨W₁.1 ⊓ W₂.1,
          isOpenSubspace_inf B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).2 W₁.1 W₂.1
            W₁.2 W₂.2⟩).hom ∧
      (∀ T' : SchemesOver ((schemeSpaceFunctor B S hS).obj A.T.left),
        Nonempty ((relativeDerivedIsomFunctor (D.projection A.T) A.E E').obj (op T')) →
          ∃ t : (schemeSpaceFunctor B S hS).obj T'.left ⟶ openSubspaceAsSpace B S hS ⟨W₁.1 ⊓ W₂.1,
          isOpenSubspace_inf B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).2 W₁.1 W₂.1
            W₁.2 W₂.2⟩,
            t ≫ openSubspaceImmersion B S hS ⟨W₁.1 ⊓ W₂.1,
          isOpenSubspace_inf B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).2 W₁.1 W₂.1
            W₁.2 W₂.2⟩ = T'.hom) ∧
      IsAffineFinitePresentationAlgebraicSpaceOver (openSubspaceAsSpace B S hS ⟨W₁.1 ⊓ W₂.1,
          isOpenSubspace_inf B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).2 W₁.1 W₂.1
            W₁.2 W₂.2⟩)
        ((CostructuredArrow.map (S := schemeSpaceFunctor B S hS)
          (openSubspaceImmersion B S hS ⟨W₁.1 ⊓ W₂.1,
          isOpenSubspace_inf B S hS ((schemeSpaceFunctor B S hS).obj A.T.left).2 W₁.1 W₂.1
            W₁.2 W₂.2⟩)).op ⋙
          relativeDerivedIsomFunctor (D.projection A.T) A.E E')
```

## Tag 0DPX, a lemma

[Tag 0DPX](https://stacks.math.columbia.edu/tag/0DPX) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.isQuasiSeparated_and_isLocallyOfFinitePresentation_complexesAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesQuasiSeparatedLocallyFinitePresentation.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesQuasiSeparatedLocallyFinitePresentation.lean#L72).

> In Situation 0DLE (`f : X ⟶ B` proper, flat and of finite presentation), the morphism
> `Complexes_{X/B} → B` is quasi-separated and locally of finite presentation. Here `Complexes_{X/B}`
> is the algebraic stack given by `isAlgebraicStack_complexes_proved`, taken through its small model,
> and `B` is the algebraic stack of its category of elements.

```lean
theorem isQuasiSeparated_and_isLocallyOfFinitePresentation_complexesAlgebraicStack
    (D : ComplexesSituation B S hS) :
    Stack.AlgebraicStacks.IsQuasiSeparated B S hS
        (complexesStructureMorphism D (isAlgebraicStack_complexes_proved.{u, w} hS D)) ∧
      Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
        (complexesStructureMorphism D (isAlgebraicStack_complexes_proved.{u, w} hS D))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.12, Tag 0DPV](https://stacks.math.columbia.edu/tag/0DPV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
