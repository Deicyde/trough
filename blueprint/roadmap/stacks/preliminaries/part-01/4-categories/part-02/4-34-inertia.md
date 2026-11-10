---
declaration: section
origin: cited
lean: CategoryTheory.RelativeInertia.diagonalPullbackEquivalence, CategoryTheory.RelativeInertia.isFibered, CategoryTheory.RelativeInertia, CategoryTheory.RelativeInertia.isEquivalenceOver_toFibreProduct, CategoryTheory.RelativeInertia.toFibreProduct_isEquivalence, CategoryTheory.RelativeInertia.squareTwoCommutes
statement: formalized
proof: formalized
---

# 4.34 Inertia

Section 4.34 of the Stacks Project, [Tag 04Z2](https://stacks.math.columbia.edu/tag/04Z2). 3 tags here are carried by 5 declarations of the repository (1 in StacksCore and 4 in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 034H, a lemma

[Tag 034H](https://stacks.math.columbia.edu/tag/034H) in the Stacks Project.

**`CategoryTheory.RelativeInertia.diagonalPullbackEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean#L333). The attribute's comment: “(1)”.

> The comparison functor `Φ : I_{S/S'} ⥤ Δ ⊡ Δ` is an equivalence of categories, with explicit
> quasi-inverse `Ψ`, unit coming from the equality `Ψ ∘ Φ = 𝟭` and counit the isomorphism with
> component `(id, κ)`.

```lean
def diagonalPullbackEquivalence (F : S ⥤ S') :
    RelativeInertia F ≌ CategoricalPullback (diagonal F) (diagonal F)
```

Declarations registered for the tag:

- [`CategoryTheory.RelativeInertia.isFibered`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/RelativeInertia.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaDiagonal.lean#L400) (StacksFrontier): “(2)”.

## Tag 034I, a definition

[Tag 034I](https://stacks.math.columbia.edu/tag/034I) in the Stacks Project.

**`CategoryTheory.RelativeInertia`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Inertia.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Inertia.lean#L72).

> **Stacks 034I.** An object of the relative inertia category `I_{S/S'}` for a
> functor `F : S ⥤ S'`: a pair `(x, α)` with `α : Aut x` such that `F(α) = id_{F(x)}`.
> The relative inertia `I_{S/S'}` (and the absolute inertia `I_S = I_{S/C}`) is the
> fibred category built from this structure.

```lean
structure RelativeInertia (F : S ⥤ S')
```

## Tag 04Z6, a lemma

[Tag 04Z6](https://stacks.math.columbia.edu/tag/04Z6) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isEquivalenceOver_toFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L450).

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

**`CategoryTheory.RelativeInertia.toFibreProduct_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L466).

> Consequence of Stacks 04Z6: the comparison functor `Θ` is an equivalence of the
> underlying categories.

```lean
theorem toFibreProduct_isEquivalence :
    (toFibreProduct p p' F hF).IsEquivalence
```

**`CategoryTheory.RelativeInertia.squareTwoCommutes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaSquare.lean#L476).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
