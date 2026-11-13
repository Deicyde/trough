---
declaration: module
origin: cited
lean: PontryaginDual.isPositiveDefiniteSub
statement: formalized
proof: formalized
---

# Pontryagin characters are positive-definite atoms

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.AdditiveCharacter`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AdditiveCharacter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AdditiveCharacter.lean): 1 declaration, 1 with a docstring.

> A continuous character of a topological abelian group becomes a continuous function on the additive
> group after transporting `G` to `Multiplicative G`.

## i. Overview

> A continuous character of a topological abelian group becomes a continuous function on the
> additive group after transporting `G` to `Multiplicative G`. This file proves that every such
> character is a continuous subtraction-positive-definite function. The character-level fact is
> an atomic input for Fourier analysis on locally compact abelian groups; it does not assert a
> measure-representation or Pontryagin-duality theorem.

## ii. Key results

> * `PontryaginDual.isPositiveDefiniteSub`: a continuous Pontryagin character is a
>   continuous positive-definite function in the additive subtraction form.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`PontryaginDual.isPositiveDefiniteSub`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AdditiveCharacter.lean#L54).

> Precomposing a Pontryagin character with `Multiplicative.ofAdd` gives a continuous function in
> subtraction-positive-definite form.

```lean
lemma isPositiveDefiniteSub
    (χ : PontryaginDual (Multiplicative G)) :
    Continuous (fun g : G => (χ (Multiplicative.ofAdd g) : ℂ)) ∧
      IsPositiveDefiniteSub
        (fun g : G => (χ (Multiplicative.ofAdd g) : ℂ))
```

## Depends on

- [Positive-definite functions on an additive commutative group](analysis-positivedefinite-addgroup.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AdditiveCharacter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AdditiveCharacter.lean)
