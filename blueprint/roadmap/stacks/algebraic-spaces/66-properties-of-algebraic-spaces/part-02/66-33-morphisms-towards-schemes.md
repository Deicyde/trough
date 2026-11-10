---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.morphismToAffineEquiv
statement: formalized
proof: formalized
---

# 66.33 Morphisms towards schemes

Section 66.33 of the Stacks Project, [Tag 05Z0](https://stacks.math.columbia.edu/tag/05Z0). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05Z1, a lemma

[Tag 05Z1](https://stacks.math.columbia.edu/tag/05Z1) in the Stacks Project.

**`AlgebraicGeometry.Space.morphismToAffineEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MorphismToAffineScheme.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MorphismToAffineScheme.lean#L522). References: EGA II (1.2.7), “absolute case S=Spec ℤ”; EGA I (2.2.4).

> **Stacks 05Z1.** Pullback of regular functions is a bijection between morphisms of
> algebraic spaces `X ⟶ T` into an affine object of the site and ring homomorphisms
> `Γ(T, 𝒪_T) →+* Γ(X, 𝒪_X)`.
>
> The bijection is specified, not merely asserted: its forward map restricts on every étale
> scheme chart of `X` to pullback of regular functions along the induced morphism of schemes.

```lean
def morphismToAffineEquiv (X : AlgebraicSpaces B S hS) (T : BigFppfOver B S hS)
    (hterminal : IsTerminal S) [IsAffine ((BigFppfOver.toScheme B S hS).obj T)] :
    { e : (X ⟶ schemeSpace T) ≃
        (Γ((BigFppfOver.toScheme B S hS).obj T, ⊤) →+* globalFunctions B S hS X.1) //
      ∀ (f : X ⟶ schemeSpace T) (U : SmallEtale B S hS X.1)
        (s : Γ((BigFppfOver.toScheme B S hS).obj T, ⊤)),
        ((e f) s).1 (op U) = Scheme.Γ.map (op ((BigFppfOver.toScheme B S hS).map
          (yoneda.preimage (U.1.hom ≫ f.hom)))) s }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.33, Tag 05Z0](https://stacks.math.columbia.edu/tag/05Z0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
