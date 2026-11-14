---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsGenerator.isDerivation_of_isAutomorphismFamily
statement: formalized
proof: formalized
---

# Generators of automorphism groups are derivations

The module `PhyslibAlpha.ProbabilisticTheory.Dynamics.GeneratorIsDerivation`, [PhyslibAlpha/ProbabilisticTheory/Dynamics/GeneratorIsDerivation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/GeneratorIsDerivation.lean): 1 declaration, 1 with a docstring.

> The generator of a one-parameter family of automorphisms is a derivation.

## i. Overview

> If a one-parameter family `α` with `α 0 = id` preserves a bounded bilinear multiplication at every
> time, its generator is a derivation of that multiplication. Differentiating `α t (a b) = α t a α t
> b` at `0` with the product rule gives `D (a b) = D a b + a D b`. Only boundedness and bilinearity of
> the product are used.

## ii. Key results

> - `IsGenerator.isDerivation_of_isAutomorphismFamily` : the generator of a family of automorphisms is
>   a derivation.

## iv. References

> * None.

## A. The generator is a derivation

**`ProbabilisticTheory.IsGenerator.isDerivation_of_isAutomorphismFamily`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/GeneratorIsDerivation.lean#L52).

> **The generator of a family of automorphisms is a derivation.** If `α 0 = id` and every `α t`
> preserves a bounded bilinear multiplication, the generator of `α` is a derivation of it.

```lean
lemma IsGenerator.isDerivation_of_isAutomorphismFamily
    (bilin : IsBoundedBilinearMap ℝ (fun p : E × E => p.1 * p.2))
    {α : ℝ → E → E} (hα0 : ∀ a, α 0 a = a) (hmul : ∀ t a b, α t (a * b) = α t a * α t b)
    {D : E →ₗ[ℝ] E} (hD : IsGenerator α D) : IsDerivation D
```

## Depends on

- [Derivations](../algebra/derivation.md)
- [Generators of one-parameter groups](generator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Dynamics/GeneratorIsDerivation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/GeneratorIsDerivation.lean)
