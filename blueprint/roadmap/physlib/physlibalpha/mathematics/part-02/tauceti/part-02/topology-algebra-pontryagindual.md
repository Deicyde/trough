---
declaration: module
origin: cited
lean: TauCeti.instPolishSpacePontryaginDual, TauCeti.circleEquivPontryaginDualInt, TauCeti.circleEquivPontryaginDualInt_apply_apply, TauCeti.circleEquivPontryaginDualInt_symm_apply
statement: formalized
proof: formalized
---

# Topology of Pontryagin duals

The module `PhyslibAlpha.Mathematics.TauCeti.Topology.Algebra.PontryaginDual`, [PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean): 4 declarations, 4 with a docstring.

> The Pontryagin dual of a second-countable locally compact monoid is Polish.

## i. Overview

> The Pontryagin dual of a second-countable locally compact monoid is Polish. For locally compact
> abelian groups this ensures that finite Borel measures on the dual are tight and determined by
> their Fourier–Stieltjes transforms.
>
> A continuous character of the discrete group `ℤ` is determined by its value at `1`, which may be
> any point of the unit circle. This file packages that correspondence as an isomorphism of
> topological groups between the unit circle and the Pontryagin dual of `ℤ`. It lets statements
> about the dual of `ℤ`, such as Fourier–Stieltjes transforms of measures on it, be read on the
> concrete unit circle, where a character becomes the monomial `z ↦ zⁿ`.

## ii. Key results

> * `TauCeti.circleEquivPontryaginDualInt`: the point `z` of the unit circle corresponds to the
>   character `n ↦ zⁿ` of `ℤ`.

## iv. References

> * W. Rudin, *Fourier Analysis on Groups*, Interscience (1962), §1.2 (the dual group).

## A. Development

**`TauCeti.instPolishSpacePontryaginDual`**, an instance, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean#L51).

> The Pontryagin dual of a second-countable locally compact monoid is Polish.

```lean
instance instPolishSpacePontryaginDual {A : Type*} [Monoid A] [TopologicalSpace A]
    [LocallyCompactSpace A] [SecondCountableTopology A] : PolishSpace (PontryaginDual A)
```

**`TauCeti.circleEquivPontryaginDualInt`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean#L57).

> The unit circle is the Pontryagin dual of `ℤ`: the point `z` corresponds to the character
> `n ↦ zⁿ`, and a character corresponds to its value at `1`.

```lean
def circleEquivPontryaginDualInt : Circle ≃ₜ* PontryaginDual (Multiplicative ℤ)
```

**`TauCeti.circleEquivPontryaginDualInt_apply_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean#L71).

> The character attached to `z` sends `n` to `zⁿ`.

```lean
lemma circleEquivPontryaginDualInt_apply_apply (z : Circle) (n : Multiplicative ℤ) :
    circleEquivPontryaginDualInt z n = z ^ n.toAdd
```

**`TauCeti.circleEquivPontryaginDualInt_symm_apply`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean#L77).

> The point of the circle attached to a character of `ℤ` is its value at `1`.

```lean
lemma circleEquivPontryaginDualInt_symm_apply (χ : PontryaginDual (Multiplicative ℤ)) :
    circleEquivPontryaginDualInt.symm χ = χ (Multiplicative.ofAdd 1)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Polish spaces of continuous homomorphisms](topology-algebra-continuousmonoidhom-polish.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/PontryaginDual.lean)
