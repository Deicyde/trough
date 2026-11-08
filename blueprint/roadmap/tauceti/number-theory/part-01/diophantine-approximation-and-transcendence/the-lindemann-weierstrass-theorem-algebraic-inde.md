---
declaration: theorem
origin: cited
lean: TauCeti.algebraicIndependent_exp, TauCeti.LindemannWeierstrass.expEval_injective, TauCeti.LindemannWeierstrass.linearIndependent_exp_algebraMap
statement: formalized
proof: formalized
---

# The Lindemann–Weierstrass theorem, algebraic independence form

If the algebraic numbers
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

- [The Lindemann–Weierstrass theorem, in Baker's form](the-lindemann-weierstrass-theorem-in-bakers-form.md)
- [The weak Lindemann–Weierstrass theorem](the-weak-lindemann-weierstrass-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.algebraicIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.algebraicIndependent_exp).

## Other forms

**The Lindemann–Weierstrass theorem over a Galois number field.** Formalized in Tau Ceti as [`TauCeti.LindemannWeierstrass.expEval_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Galois.html#TauCeti.LindemannWeierstrass.expEval_injective).

```lean
TauCeti.LindemannWeierstrass.expEval_injective.{u_1} {K : Type u_1} [Field K] [NumberField K]
  [IsGalois ℚ K] [Algebra K ℂ] : Function.Injective ⇑(TauCeti.LindemannWeierstrass.expEval K)
```

**The Lindemann–Weierstrass theorem over a Galois number field, linear independence form.** Formalized in Tau Ceti as [`TauCeti.LindemannWeierstrass.linearIndependent_exp_algebraMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Galois.html#TauCeti.LindemannWeierstrass.linearIndependent_exp_algebraMap).

```lean
TauCeti.LindemannWeierstrass.linearIndependent_exp_algebraMap.{u_1} {K : Type u_1} [Field K]
  [NumberField K] [IsGalois ℚ K] [Algebra K ℂ] :
  LinearIndependent K fun γ => Complex.exp ((algebraMap K ℂ) γ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.algebraicIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.algebraicIndependent_exp)
- [Source of `TauCeti.algebraicIndependent_exp` in TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean#L82)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
