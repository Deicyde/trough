---
declaration: theorem
origin: cited
lean: Matrix.continuous_mulVec_extension_iff
statement: formalized
proof: formalized
---

# Matrix.continuous\_mulVec\_extension\_iff

A matrix over the group ring has a unique continuous extension of its action to completed
coordinate modules. Its entries are included coefficientwise in the Novikov ring. No topology
on the group ring is needed to state this uniqueness property.

```lean
Matrix.continuous_mulVec_extension_iff.{u_1, u_2, u_3, u_4} {R : Type u_1} {H : Type u_2}
  {m : Type u_3} {n : Type u_4} [AddMonoid H] [Ring R] [Fintype n]
  (A : Matrix m n (AddMonoidAlgebra R H)) (N : H →+ ℝ)
  (f : (n → TauCeti.NovikovSeries R H N) → m → TauCeti.NovikovSeries R H N) :
  (Continuous f ∧
      ∀ (v : n → AddMonoidAlgebra R H),
        (f fun j => TauCeti.NovikovSeries.ofAddMonoidAlgebra (v j)) = fun i =>
          TauCeti.NovikovSeries.ofAddMonoidAlgebra (A.mulVec v i)) ↔
    f = fun v => (A.map ⇑TauCeti.NovikovSeries.ofAddMonoidAlgebra).mulVec v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.continuous_mulVec_extension_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Matrix.html#Matrix.continuous_mulVec_extension_iff).

## Sources

- [Tau Ceti documentation: `Matrix.continuous_mulVec_extension_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Matrix.html#Matrix.continuous_mulVec_extension_iff)
- [Source of `Matrix.continuous_mulVec_extension_iff` in TauCeti/RingTheory/NovikovSeries/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/Matrix.lean#L122)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
