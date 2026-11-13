---
declaration: section
origin: cited
lean: CategoryTheory.RelativeInertia.isEquivalenceOverToDiagonalFibreProductOver, CategoryTheory.RelativeInertia.isEquivalenceOver_toDiagonalFibreProductOver_and_isFibered, CategoryTheory.RelativeInertia.isFibered, CategoryTheory.RelativeInertia, CategoryTheory.RelativeInertia.isEquivalenceOver_toFibreProduct, CategoryTheory.RelativeInertia.toFibreProduct_isEquivalence, CategoryTheory.RelativeInertia.squareTwoCommutes
statement: formalized
proof: formalized
---

# 4.34 Inertia

Section 4.34 of the Stacks Project, [Tag 04Z2](https://stacks.math.columbia.edu/tag/04Z2). 3 tags here are carried by 6 declarations of the repository (1 in StacksCore and 5 in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 034H, a lemma

[Tag 034H](https://stacks.math.columbia.edu/tag/034H) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isEquivalenceOverToDiagonalFibreProductOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonalOver.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonalOver.lean#L278). The attribute's comment: “(1)”.

> **Stacks 034H (1), the equivalence over `C`.** For `F : S ⥤ S'` strictly over `C`, the
> comparison 1-morphism `Φ : I_{S/S'} ⥤ S ×_{Δ, S ×_{S'} S, Δ} S`, `(x, α) ↦ (x, x, (α, id))`, is
> an equivalence in the (2,1)-category of categories over `C`: `Φ` and its quasi-inverse `Ψ`,
> `(U, x, y, (ι, κ)) ↦ (x, κ⁻¹ ∘ ι)`, are functors over `C`, and every component of the unit
> (`id_x`) and of the counit (`(id_x, κ)`) lies over an identity of `C`. The 2-fibre products are
> those of categories over `C` (Stacks 02XQ, `CategoryTheory.TwoFibreProductOver`), with vertical
> comparison isomorphisms.

```lean
noncomputable def isEquivalenceOverToDiagonalFibreProductOver (hF : F ⋙ p' = p) :
    IsEquivalenceOver (RelativeInertia.π F ⋙ p) (diagonalFibreProductOverProj hF)
      (toDiagonalFibreProductOver hF)
```

**`CategoryTheory.RelativeInertia.isEquivalenceOver_toDiagonalFibreProductOver_and_isFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonalOver.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonalOver.lean#L308).

> **Stacks 034H.** Let `p : S ⥤ C` be a fibred category, let `p' : S' ⥤ C` be a category over
> `C` and let `F : S ⥤ S'` be a 1-morphism of fibred categories over `C`. Then
> 1. the comparison 1-morphism `Φ : I_{S/S'} ⥤ S ×_{Δ, S ×_{S'} S, Δ} S` is an equivalence in the
>    (2,1)-category of categories over `C`, the 2-fibre products being those of categories over
>    `C` (`isEquivalenceOverToDiagonalFibreProductOver`), and
> 2. `I_{S/S'}`, with structure functor `(x, α) ↦ p x`, is a fibred category over `C`
>    (`CategoryTheory.RelativeInertia.isFibered`).
>
> The source also assumes `p'` fibred; neither part uses it.

```lean
theorem isEquivalenceOver_toDiagonalFibreProductOver_and_isFibered (hp : p.IsFibered)
    (hF : p.IsFibredOneMorphism p' F) :
    Nonempty (IsEquivalenceOver (RelativeInertia.π F ⋙ p)
      (diagonalFibreProductOverProj hF.comp_eq) (toDiagonalFibreProductOver hF.comp_eq)) ∧
      (RelativeInertia.π F ⋙ p).IsFibered
```

Declarations registered for the tag:

- [`CategoryTheory.RelativeInertia.isFibered`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/RelativeInertia.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean#L412) (StacksFrontier): “(2)”.

## Tag 034I, a definition

[Tag 034I](https://stacks.math.columbia.edu/tag/034I) in the Stacks Project.

**`CategoryTheory.RelativeInertia`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Inertia.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Inertia.lean#L72).

> **Stacks 034I.** An object of the relative inertia category `I_{S/S'}` for a
> functor `F : S ⥤ S'`: a pair `(x, α)` with `α : Aut x` such that `F(α) = id_{F(x)}`.
> The relative inertia `I_{S/S'}` (and the absolute inertia `I_S = I_{S/C}`) is the
> fibred category built from this structure.

```lean
structure RelativeInertia (F : S ⥤ S')
```

## Tag 04Z6, a lemma

[Tag 04Z6](https://stacks.math.columbia.edu/tag/04Z6) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isEquivalenceOver_toFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L450).

> **Stacks 04Z6.** The 2-commutative square
> ```
>   I_{S/S'} --c--> I_S
>      |             |
>   F∘π |            | I_F
>      v             v
>      S' ---e---> I_{S'}
> ```
> is a 2-fibre product in the (2,1)-category of fibred categories over `C`: the canonical
> comparison 1-morphism `Θ` to the explicit 2-fibre product `S' ×_{e, I_{S'}, I_F} I_S` is an
> equivalence of categories **over `C`**.
>
> The witness produced has `Θ` itself as its underlying functor, so the statement is about
> the given comparison functor with its prescribed action on objects and morphisms, and not
> merely about the existence of some equivalence.

```lean
theorem isEquivalenceOver_toFibreProduct :
    Nonempty (IsEquivalenceOver (RelativeInertia.π F ⋙ p)
      (FibreProduct.structureFunctor p p' F hF) (toFibreProduct p p' F hF))
```

**`CategoryTheory.RelativeInertia.toFibreProduct_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L466).

> Consequence of Stacks 04Z6: the comparison functor `Θ` is an equivalence of the
> underlying categories.

```lean
theorem toFibreProduct_isEquivalence :
    (toFibreProduct p p' F hF).IsEquivalence
```

**`CategoryTheory.RelativeInertia.squareTwoCommutes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L476).

> **Stacks 04Z6, the square.** The 2-commutativity of the square is witnessed by a
> natural isomorphism over `C`, `I_F ∘ c ≅ e ∘ (F ∘ π)`. On an object `(x, α)` both
> composites are `(F x, id)`, since `F α = id`, so the canonical 2-isomorphism is the
> identity.

```lean
def squareTwoCommutes :
    (comparison p p' F hF) ⋙ (functoriality p p' F hF)
      ≅ (RelativeInertia.π F ⋙ F) ⋙ (neutralSection p')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.34, Tag 04Z2](https://stacks.math.columbia.edu/tag/04Z2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
