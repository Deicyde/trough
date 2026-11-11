---
declaration: theorem
origin: cited
lean: MonoidAlgebra.leftIntegral_eq_rightIntegral
statement: formalized
proof: formalized
---

# MonoidAlgebra.leftIntegral_eq_rightIntegral

The two integral submodules of a group algebra agree, even for a noncommutative group.

```lean
MonoidAlgebra.leftIntegral_eq_rightIntegral.{u_1, u_2} {R : Type u_1} {G : Type u_2}
  [CommSemiring R] [Group G] :
  TauCeti.leftIntegral R (MonoidAlgebra R G) = TauCeti.rightIntegral R (MonoidAlgebra R G)
```

## Depends on

- [TauCeti.leftIntegral](tauceti-leftintegral.md)
- [TauCeti.rightIntegral](tauceti-rightintegral.md)

## Lean

Formalized in Tau Ceti as [`MonoidAlgebra.leftIntegral_eq_rightIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.html#MonoidAlgebra.leftIntegral_eq_rightIntegral).

## Sources

- [Tau Ceti documentation: `MonoidAlgebra.leftIntegral_eq_rightIntegral`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.html#MonoidAlgebra.leftIntegral_eq_rightIntegral)
- [Source of `MonoidAlgebra.leftIntegral_eq_rightIntegral` in TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/HopfAlgebra/Integral/MonoidAlgebra.lean#L62)
- [Tau Ceti roadmap status: Hopfological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HopfologicalAlgebra/STATUS.md)
