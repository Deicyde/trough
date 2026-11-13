---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowFst, AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowSnd, AlgebraicGeometry.Stack.AlgebraicStacks.isSetoidCategory_dottedArrow_relativeDiagonal, AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowClassesEquiv, AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_valuativeCriterionUniqueness, AlgebraicGeometry.Stack.valuativeCriterionUniqueness_of_isSeparated
statement: formalized
proof: formalized
---

# 101.41 Valuative criterion for the diagonal

Section 101.41 of the Stacks Project, [Tag 0CLS](https://stacks.math.columbia.edu/tag/0CLS). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E8L, a lemma

[Tag 0E8L](https://stacks.math.columbia.edu/tag/0E8L) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowFst`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean#L189). The attribute's comment: “part (1): the dotted arrow coming from the first projection”.

> **Stacks 0E8L, part (1), first arrow.** The triple `(a₁, α₁, id)` is a dotted arrow for the
> square of `f` with top row `x`, bottom row `f ∘ a₁` and right edge `f`.

```lean
def diagonalDottedArrowFst :
    CategoryTheory.DottedArrow D.x D.j f.hom
      ((D.y ≫ (twoFibreProductSquare B S hS f f).fst.hom) ≫ f.hom)
      (diagonalWitness B S hS D)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowSnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean#L203). The attribute's comment: “part (1): the dotted arrow coming from the second projection”.

> **Stacks 0E8L, part (1), second arrow.** The triple `(a₂, α₂, φ)` is a dotted arrow for the
> *same* square of `f`: the compatibility triangle is the statement that `γ` is a 2-morphism into
> the 2-fibre product, by the exchange law and
> `AlgebraicGeometry.Stack.AlgebraicStacks.relativeDiagonal_whiskerLeft_twoFibreProductCell`.

```lean
def diagonalDottedArrowSnd :
    CategoryTheory.DottedArrow D.x D.j f.hom
      ((D.y ≫ (twoFibreProductSquare B S hS f f).fst.hom) ≫ f.hom)
      (diagonalWitness B S hS D)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSetoidCategory_dottedArrow_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean#L256). The attribute's comment: “part (2): the category of diagonal fillers is a setoid”.

> **Stacks 0E8L, part (2), first assertion.** The category of dotted arrows of a valuative
> diagram for the relative diagonal of a 1-morphism of algebraic stacks is a setoid.
>
> The relative diagonal is representable by algebraic spaces (Stacks 04XS), hence its underlying
> functor is faithful (Stacks 04Y5), and the category of dotted arrows along a faithful 1-morphism
> is a thin groupoid.

```lean
theorem isSetoidCategory_dottedArrow_relativeDiagonal :
    IsSetoidCategory
      (CategoryTheory.DottedArrow D.x D.j (relativeDiagonal B S hS f).hom D.y D.γ)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.diagonalDottedArrowClassesEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDiagonal.lean#L502). The attribute's comment: “part (2): isomorphism classes are the morphisms between the two dotted arrows”.

> **Stacks 0E8L, part (2), second assertion.** The isomorphism classes of dotted arrows of a
> valuative diagram for the relative diagonal of `f` correspond bijectively to the morphisms
> `(a₁, α₁, id) ⟶ (a₂, α₂, φ)` of dotted arrows for `f`, by `d ↦ (β ⋆ pr₁) ∘ (β ⋆ pr₂)⁻¹`.

```lean
noncomputable def diagonalDottedArrowClassesEquiv :
    Quotient (isIsomorphicSetoid
        (CategoryTheory.DottedArrow D.x D.j (relativeDiagonal B S hS f).hom D.y D.γ)) ≃
      (diagonalDottedArrowFst B S hS D ⟶ diagonalDottedArrowSnd B S hS D)
```

## Tag 0CLT, a lemma

[Tag 0CLT](https://stacks.math.columbia.edu/tag/0CLT) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_valuativeCriterionUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeUniquenessSeparated.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeUniquenessSeparated.lean#L272).

> **Stacks 0CLT.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. Assume `f` is
> quasi-separated. If `f` satisfies the uniqueness part of the valuative criterion, then `f` is
> separated.
>
> Separatedness of `f` is properness of `Δ_f` in the relative sense of Stacks 04XB. Its three
> conjuncts are: separatedness of `Δ_f`, which is Stacks 0CLR fed with the setoid half of the
> uniqueness criterion; finiteness of type, whose quasi-compactness half is the first conjunct of
> quasi-separatedness and whose local half is part (2) of Stacks 04XS; and universal closedness,
> which comes from the existence part of the valuative criterion for `Δ_f` through Stacks 0CLN and
> Stacks 03KA.

```lean
theorem isSeparated_of_valuativeCriterionUniqueness (f : 𝒳 ⟶ 𝒴)
    (hqs : IsQuasiSeparated B S hS f)
    (hu : ValuativeCriterion.Uniqueness B S hS f) :
    IsSeparated B S hS f
```

## Tag 0CLU, a lemma

[Tag 0CLU](https://stacks.math.columbia.edu/tag/0CLU) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionUniqueness_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedImpliesValuativeUniqueness.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedImpliesValuativeUniqueness.lean#L406).

> **Stacks 0CLU.** A separated 1-morphism of algebraic stacks satisfies the uniqueness part of
> the valuative criterion.
>
> Separatedness is properness of the relative diagonal `Δ_f` in the sense of Stacks 04XB, so `Δ_f`
> is in particular separated there and the category of dotted arrows of every valuative diagram is
> a setoid by **Stacks 0CLC**. For the second half, two dotted arrows `a`, `b` of one valuative
> diagram assemble into a scheme-valued point `(a, b, β_b ∘ β_a⁻¹)` of `𝒳 ×_𝒴 𝒳` whose valuative
> diagram for `Δ_f` is filled by `(α_a, α_b)`; `Δ_f` is proper and representable by algebraic spaces
> (**Stacks 04XS**), so that diagram has a dotted arrow by the valuative criterion of properness for
> algebraic spaces (**Stacks 0A40**), and **Stacks 0E8L** turns that dotted arrow into a morphism
> `a ⟶ b`, which the setoid property makes an isomorphism.

```lean
theorem valuativeCriterionUniqueness_of_isSeparated (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsSeparated B S hS f) :
    ValuativeCriterion.Uniqueness B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.41, Tag 0CLS](https://stacks.math.columbia.edu/tag/0CLS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
