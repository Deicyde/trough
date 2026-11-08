---
declaration: def
origin: cited
lean: LieHom.quotKerEquivOfSurjective
statement: formalized
---

# The first isomorphism theorem for a surjective homomorphism of Lie algebras

the quotient
by its kernel is isomorphic to the target.

```lean
LieHom.quotKerEquivOfSurjective.{u_1, u_2, u_3} {R : Type u_1} {L : Type u_2} {L' : Type u_3}
  [CommRing R] [LieRing L] [LieAlgebra R L] [LieRing L'] [LieAlgebra R L'] (f : L →ₗ⁅R⁆ L')
  (hf : Function.Surjective ⇑f) : (L ⧸ f.ker) ≃ₗ⁅R⁆ L'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieHom.quotKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Quotient.html#LieHom.quotKerEquivOfSurjective).

## Sources

- [Tau Ceti documentation: `LieHom.quotKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Quotient.html#LieHom.quotKerEquivOfSurjective)
- [Source of `LieHom.quotKerEquivOfSurjective` in TauCeti/Algebra/Lie/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Quotient.lean#L197)
