---
declaration: def
origin: cited
lean: RootPairing.Base.dualCoxeterNumber
statement: formalized
---

# RootPairing.Base.dualCoxeterNumber

The **dual Coxeter number** `h^∨ = 1 + ht(θ^∨)` of a base: one more than the sum of the
coefficients of the coroot of the highest root `θ` in the simple coroots. Equivalently
`h^∨ = 1 + ⟨ρ, θ^∨⟩` (`RootPairing.Base.coroot'_highestRoot_weylVector`).

```lean
RootPairing.Base.dualCoxeterNumber.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] {P : RootPairing ι R M N} [CharZero R] (b : P.Base) [Finite ι] [Nonempty ι] :
  ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.Base.dualCoxeterNumber`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/DualCoxeterNumber.html#RootPairing.Base.dualCoxeterNumber).

## Sources

- [Tau Ceti documentation: `RootPairing.Base.dualCoxeterNumber`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/DualCoxeterNumber.html#RootPairing.Base.dualCoxeterNumber)
- [Source of `RootPairing.Base.dualCoxeterNumber` in TauCeti/LinearAlgebra/RootSystem/DualCoxeterNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/DualCoxeterNumber.lean#L83)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
