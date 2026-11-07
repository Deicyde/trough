---
declaration: theorem
origin: cited
lean: TauCeti.algebraicIndependent_exp
statement: formalized
proof: formalized
---

# TauCeti.algebraicIndependent\_exp

**The Lindemann–Weierstrass theorem**, algebraic independence form. If the algebraic numbers
`u i` are linearly independent over `ℕ` (equivalently, over `ℚ`), then their exponentials are
algebraically independent over the field `integralClosure ℚ ℂ` of algebraic numbers.

```lean
TauCeti.algebraicIndependent_exp.{u_1} {ι : Type u_1} (u : ι → ↥(integralClosure ℚ ℂ))
  (hu : LinearIndependent ℕ u) :
  AlgebraicIndependent ↥(integralClosure ℚ ℂ) fun i => Complex.exp ↑(u i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.linearIndependent\_exp](tauceti-linearindependent-exp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.algebraicIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.algebraicIndependent_exp).

## Sources

- [Tau Ceti documentation: `TauCeti.algebraicIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.algebraicIndependent_exp)
- [Source of `TauCeti.algebraicIndependent_exp` in TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean#L82)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
