---
declaration: section
origin: cited
lean: Stacks.Chow.exists_properClosedSubscheme_or_finiteDimensional_functionField, Stacks.Chow.locallyFinite_closure_image_of_isSpectralMap
statement: formalized
proof: formalized
---

# 42.11 Preparation for proper pushforward

Section 42.11 of the Stacks Project, [Tag 02R0](https://stacks.math.columbia.edu/tag/02R0). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02R1, a lemma

[Tag 02R1](https://stacks.math.columbia.edu/tag/02R1) in the Stacks Project.

**`Stacks.Chow.exists_properClosedSubscheme_or_finiteDimensional_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PreparationProperPushforward/FiniteFunctionFieldExtension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/PreparationProperPushforward/FiniteFunctionFieldExtension.lean#L142).

> **Stacks Project, Tag 02R1.** Let `X` and `Y` be integral schemes locally of finite type
> over a Chow base `(S, δ)` and let `f : X ⟶ Y` be a morphism over `S` with
> `dim_δ X = dim_δ Y`. Then either `f(X)` is contained in a proper closed subscheme of `Y`, or
> `f` is dominant and the extension of function fields `R(X)/R(Y)` is finite.

```lean
theorem exists_properClosedSubscheme_or_finiteDimensional_functionField
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    [IsIntegral X] [IsIntegral Y] (f : X ⟶ Y) (hf : f ≫ sY = sX)
    (hdim : schemeDeltaDimension C sX = schemeDeltaDimension C sY) :
    (∃ (Z : Scheme.{u}) (i : Z ⟶ Y), IsClosedImmersion i ∧
        Set.range f.base ⊆ Set.range i.base ∧ Set.range i.base ≠ Set.univ) ∨
      (∃ hdom : IsDominant f,
        letI : IsDominant f := hdom
        letI : Algebra Y.functionField X.functionField :=
          (dominantFunctionFieldMap f).toAlgebra
        FiniteDimensional Y.functionField X.functionField)
```

## Tag 02R2, a lemma

[Tag 02R2](https://stacks.math.columbia.edu/tag/02R2) in the Stacks Project.

**`Stacks.Chow.locallyFinite_closure_image_of_isSpectralMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/LocallyFiniteImage.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/LocallyFiniteImage.lean#L39).

> **Stacks 02R2.** Under a spectral map to a prespectral space, the closures of the images of
> a locally finite family of subsets form a locally finite family.

```lean
theorem locallyFinite_closure_image_of_isSpectralMap {X : Type u} {Y : Type v}
    [TopologicalSpace X] [TopologicalSpace Y] [PrespectralSpace Y] (f : X → Y)
    (hf : IsSpectralMap f) {I : Type w} (Z : I → Set X) (hZ : LocallyFinite Z) :
    LocallyFinite fun i ↦ closure (f '' Z i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.11, Tag 02R0](https://stacks.math.columbia.edu/tag/02R0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
