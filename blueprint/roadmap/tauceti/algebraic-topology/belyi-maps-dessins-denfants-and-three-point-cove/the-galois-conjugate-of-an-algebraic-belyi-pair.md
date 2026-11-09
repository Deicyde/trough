---
declaration: theorem
origin: cited
lean: TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv
statement: formalized
proof: formalized
---

# The Galois conjugate of an algebraic Belyi pair is an algebraic Belyi pair

if `F` is an
algebraic Belyi pair over `k`, and `τ : F ≃+* F'` carries `k(t)` onto `k'(t)` by the coefficient
map of `σ : k ≃+* k'`, then `F'` is an algebraic Belyi pair over `k'`.

Taking `F' = F` with its structure maps precomposed with `σ⁻¹` and `τ` the identity, this is the
conjugation of a Belyi pair by an automorphism `σ` of the constants.

```lean
TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv.{u_1, u_2, u_3, u_4} {k : Type u_1} {k' : Type u_2}
  {F : Type u_3} {F' : Type u_4} [Field k] [Field k'] [Field F] [Field F'] [Algebra k F]
  [Algebra k' F'] [Algebra (RatFunc k) F] [Algebra (RatFunc k') F'] [IsScalarTower k (RatFunc k) F]
  [IsScalarTower k' (RatFunc k') F'] (σ : k ≃+* k') (τ : F ≃+* F')
  (hτ :
    ∀ (x : RatFunc k),
      τ ((algebraMap (RatFunc k) F) x) =
        (algebraMap (RatFunc k') F') ((TauCeti.RatFunc.mapRingEquiv σ) x))
  [CharZero k] [CharZero k'] [FiniteDimensional (RatFunc k) F] [FiniteDimensional (RatFunc k') F']
  (h : TauCeti.IsAlgebraicBelyiPair k F) : TauCeti.IsAlgebraicBelyiPair k' F'
```

## Depends on

- [TauCeti.IsAlgebraicBelyiPair](tauceti-isalgebraicbelyipair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Conjugation.html#TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Conjugation.html#TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv)
- [Source of `TauCeti.IsAlgebraicBelyiPair.of_mapRingEquiv` in TauCeti/FieldTheory/FunctionField/Belyi/Conjugation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Belyi/Conjugation.lean#L121)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
