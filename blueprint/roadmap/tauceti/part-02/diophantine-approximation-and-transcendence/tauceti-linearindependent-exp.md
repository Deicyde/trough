---
declaration: theorem
origin: cited
lean: TauCeti.linearIndependent_exp
statement: formalized
proof: formalized
---

# TauCeti.linearIndependent\_exp

**The Lindemann–Weierstrass theorem**, in Baker's form. The exponentials of pairwise distinct
algebraic numbers are linearly independent over the field `integralClosure ℚ ℂ` of algebraic
numbers.

```lean
TauCeti.linearIndependent_exp.{u_1} {ι : Type u_1} (u : ι → ↥(integralClosure ℚ ℂ))
  (u_inj : Function.Injective u) :
  LinearIndependent ↥(integralClosure ℚ ℂ) fun i => Complex.exp ↑(u i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.linearIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.linearIndependent_exp).

## Sources

- [Tau Ceti documentation: `TauCeti.linearIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.linearIndependent_exp)
- [Source of `TauCeti.linearIndependent_exp` in TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean#L50)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
