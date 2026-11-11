---
declaration: theorem
origin: cited
lean: TauCeti.linearIndependent_exp, TauCeti.algebraicIndependent_exp, TauCeti.LindemannWeierstrass.expEval_injective, TauCeti.LindemannWeierstrass.linearIndependent_exp_algebraMap
statement: formalized
proof: formalized
---

# The Lindemann–Weierstrass theorem, in Baker's form

The exponentials of pairwise distinct
algebraic numbers are linearly independent over the field `integralClosure ℚ ℂ` of algebraic
numbers.

```lean
TauCeti.linearIndependent_exp.{u_1} {ι : Type u_1} (u : ι → ↥(integralClosure ℚ ℂ))
  (u_inj : Function.Injective u) :
  LinearIndependent ↥(integralClosure ℚ ℂ) fun i => Complex.exp ↑(u i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weak Lindemann–Weierstrass theorem](../../part-02/transcendental/the-weak-lindemann-weierstrass-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.linearIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.linearIndependent_exp).

## Other forms

**The Lindemann–Weierstrass theorem, algebraic independence form.** Formalized in Tau Ceti as [`TauCeti.algebraicIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.algebraicIndependent_exp).

```lean
TauCeti.algebraicIndependent_exp.{u_1} {ι : Type u_1} (u : ι → ↥(integralClosure ℚ ℂ))
  (hu : LinearIndependent ℕ u) :
  AlgebraicIndependent ↥(integralClosure ℚ ℂ) fun i => Complex.exp ↑(u i)
```

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

- [Tau Ceti documentation: `TauCeti.linearIndependent_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.html#TauCeti.linearIndependent_exp)
- [Source of `TauCeti.linearIndependent_exp` in TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/Lindemann/Theorem.lean#L50)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
