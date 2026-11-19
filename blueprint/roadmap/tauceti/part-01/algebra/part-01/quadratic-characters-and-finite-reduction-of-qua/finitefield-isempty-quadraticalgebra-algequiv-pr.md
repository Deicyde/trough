---
declaration: theorem
origin: cited
lean: FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card
statement: formalized
proof: formalized
---

# FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card

Over a finite field of even cardinality, `F[X]/(X² - r)` is never `F × F`: the oddness
hypothesis of the split case cannot be dropped.

```lean
FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card.{u_1} {F : Type u_1} [Field F]
  [Finite F] (heven : Even (Nat.card F)) (r : F) : IsEmpty (QuadraticAlgebra F r 0 ≃ₐ[F] F × F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [QuadraticAlgebra.algEquivDualNumberOfDoubleRoot](quadraticalgebra-algequivdualnumberofdoubleroot.md)
- [QuadraticAlgebra.isField_iff_not_isSquare](quadraticalgebra-isfield-iff-not-issquare.md)

## Lean

Formalized in Tau Ceti as [`FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card).

## Sources

- [Tau Ceti documentation: `FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card)
- [Source of `FiniteField.isEmpty_quadraticAlgebra_algEquiv_prod_of_even_card` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L145)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
