---
declaration: theorem
origin: cited
lean: MonoidAlgebra.leftIntegral_ne_bot
statement: formalized
proof: formalized
---

# MonoidAlgebra.leftIntegral_ne_bot

A finite group algebra over nontrivial coefficients has nonzero integrals,
even when the group order vanishes in the coefficient semiring.

```lean
MonoidAlgebra.leftIntegral_ne_bot.{u_1, u_2} (R : Type u_1) (G : Type u_2) [CommSemiring R]
  [Group G] [Finite G] [Nontrivial R] : TauCeti.leftIntegral R (MonoidAlgebra R G) ≠ ⊥
```

## Depends on

- [TauCeti.leftIntegral](tauceti-leftintegral.md)

## Lean

Formalized in Tau Ceti as [`MonoidAlgebra.leftIntegral_ne_bot`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.html#MonoidAlgebra.leftIntegral_ne_bot).

## Sources

- [Tau Ceti documentation: `MonoidAlgebra.leftIntegral_ne_bot`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.html#MonoidAlgebra.leftIntegral_ne_bot)
- [Source of `MonoidAlgebra.leftIntegral_ne_bot` in TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.lean#L89)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
