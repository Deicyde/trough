---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.deltaDimensionIrreducible_closureSingleton_isEffectiveCartierDivisor, AlgebraicGeometry.Space.isPrimeDivisor_tfae, AlgebraicGeometry.Space.isPrimeDivisor_tfae_of_isIntegralSpace'
statement: formalized
proof: formalized
---

# 82.12 Preparation for principal divisors

Section 82.12 of the Stacks Project, [Tag 0EPF](https://stacks.math.columbia.edu/tag/0EPF). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EPZ, a lemma

[Tag 0EPZ](https://stacks.math.columbia.edu/tag/0EPZ) in the Stacks Project.

**`AlgebraicGeometry.Space.deltaDimensionIrreducible_closureSingleton_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierComponentDeltaDimension.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierComponentDeltaDimension.lean#L287). The attribute's comment: “part (2)”.

> **Stacks 0EPZ, part (2).** In Situation 0EDT let `X/B` be good and assume `X` integral with
> `dim_δ(X) = n`.  If `Z` is an irreducible component of an effective Cartier divisor `D ⊆ X`,
> then `dim_δ(Z) = n - 1`.
>
> The component is presented by a generic point `ξ` of an irreducible component `W` of the closed
> subset `|D| ⊆ |X|`, and `dim_δ(Z)` is the `δ`-dimension of Stacks 0EDX of the irreducible closed
> subset `closure {ξ}` of `|X|`, the summand `W` contributes to `dim_δ(D)`.
>
> By part (1) the equality is equivalent to the component having codimension one in `|X|`, which
> is `AlgebraicGeometry.Space.codimension_closureSingleton_eq_one_of_isEffectiveCartierDivisor`;
> the passage between the two is the topological equivalence
> `codimension_closureSingleton_eq_one_iff_dimensionFunction` for the dimension function `δ_{X/B}`
> of Stacks 0EDN, which is where integrality of `X` and `dim_δ(X) = n` are used.

```lean
theorem deltaDimensionIrreducible_closureSingleton_isEffectiveCartierDivisor
    (D : BaseSpaceDimensionSituation.{u})
    {X : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u} (sX : X ⟶ D.space)
    (hX : D.IsGood sX) (hint : IsIntegralSpace D.site D.base D.base_mem X) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (E : ClosedSubspaces D.site D.base D.base_mem X)
    (hE : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨X, hX.1⟩ E)
    {W : Set (subspacePointSet D.site D.base D.base_mem X E.1)}
    (hW : W ∈ irreducibleComponents (subspacePointSet D.site D.base D.base_mem X E.1))
    {ξ : subspacePointSet D.site D.base D.base_mem X E.1} (hξ : IsGenericPoint ξ W) :
    deltaDimensionIrreducible D sX hX
        (IrreducibleCloseds.closureSingleton (ξ : points D.site D.base D.base_mem X)) =
      n - 1
```

**`AlgebraicGeometry.Space.isPrimeDivisor_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrimeDivisorDeltaDimension.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrimeDivisorDeltaDimension.lean#L249). The attribute's comment: “part (1)”.

> **Stacks 0EPZ, part (1).** In Situation 0EDT let `X/B` be good and assume `X` integral with
> `dim_δ(X) = n`. For an integral closed subspace `Z ⊆ X` the following are equivalent: `Z` is a
> prime divisor of `X`; the set of points of `Z` has codimension one in `|X|`; and
> `dim_δ(Z) = n - 1`.
>
> These are the hypotheses of the source and nothing else. The equivalence itself is
> `isPrimeDivisor_tfae_of_isIntegralSpace`, which also takes a dimension function on `|X|` with
> underlying function `δ_{X/B}`; that is not an input of Stacks 0EPZ but the conclusion of Stacks
> 0EDN, `exists_dimensionFunction_inducedDimensionValue`, applied to the standing data of
> Situation 0EDT: the base is a quasi-separated, locally Noetherian, universally catenary
> algebraic space with a dimension function, a quasi-separated algebraic space is decent, and a
> good `X/B` is decent and locally of finite type over the base.

```lean
theorem isPrimeDivisor_tfae (D : BaseSpaceDimensionSituation.{u})
    {X : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u} (sX : X ⟶ D.space)
    (hX : D.IsGood sX) (hint : IsIntegralSpace D.site D.base D.base_mem X) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) :
    List.TFAE
      [∃ W : PrimeDivisor D.site D.base D.base_mem X, W.subspace = Z.subspace,
        codimension (integralClosedSubspaceSupport D.site D.base D.base_mem hX.1 Z) = 1,
        deltaDimension D sX Z = n - 1]
```

**`AlgebraicGeometry.Space.isPrimeDivisor_tfae_of_isIntegralSpace'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrimeDivisorDeltaDimensionOfGood.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrimeDivisorDeltaDimensionOfGood.lean#L67). The attribute's comment: “part (1)”.

> In Situation 0EDT let `X/B` be good and assume `X` integral with
> `dim_δ(X) = n`. For an integral closed subspace `Z ⊆ X` the following are equivalent: `Z` is a
> prime divisor of `X`; the set of points of `Z` has codimension one in `|X|`; and
> `dim_δ(Z) = n - 1`.
>
> This is an alias of `AlgebraicGeometry.Space.isPrimeDivisor_tfae`, which is proved at these
> hypotheses in `StacksFrontier.AlgebraicGeometry.Spaces.Chow.PrimeDivisorDeltaDimension`. The
> bundled dimension function on `|X|` with underlying function `δ_{X/B}` that the engine
> `AlgebraicGeometry.Space.isPrimeDivisor_tfae_of_isIntegralSpace` takes is produced from goodness
> of `X/B` by Stacks 0EDN,
> `AlgebraicGeometry.Space.exists_dimensionFunction_inducedDimensionValue`: the base of
> Situation 0EDT is a quasi-separated, locally Noetherian, universally catenary algebraic space
> with a dimension function, a good `X/B` is decent and locally of finite type over it, and a
> quasi-separated algebraic space is decent.

```lean
alias isPrimeDivisor_tfae_of_isIntegralSpace'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.12, Tag 0EPF](https://stacks.math.columbia.edu/tag/0EPF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
