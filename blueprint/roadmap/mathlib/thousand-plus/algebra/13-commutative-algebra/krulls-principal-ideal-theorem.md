# Krull's principal ideal theorem

**Krull's principal ideal theorem** (also known as **Krullscher Hauptidealsatz**) :
In a commutative Noetherian ring `R`, any prime ideal that is minimal over a principal ideal
has height at most 1.

```lean
Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes.{u_1} {R : Type u_1} [CommRing R]
  [IsNoetherianRing R] (I : Ideal R) [Submodule.IsPrincipal I] (p : Ideal R)
  (hp : p ∈ I.minimalPrimes) : p.height ≤ 1
```

## Depends on

- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Prime spectrum](../../../overview/geometry/algebraic-geometry/prime-spectrum.md)
- [Principal ideal domain](../../../overview/general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Localization](../../../overview/general-algebra/rings/localization.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/KrullsHeightTheorem.html#Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes)
- [Source of `Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes` in Mathlib/RingTheory/Ideal/KrullsHeightTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Ideal/KrullsHeightTheorem.lean#L105)
- [1000+ theorems list: Q3527241](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2574)
- [1000+ theorems project: Q3527241](https://1000-plus.github.io/all.html?length=-1#Q3527241)
- [Wikipedia: Krull's principal ideal theorem](https://en.wikipedia.org/wiki/Krull's_principal_ideal_theorem)
- [Wikidata: Q3527241](https://www.wikidata.org/wiki/Q3527241)
