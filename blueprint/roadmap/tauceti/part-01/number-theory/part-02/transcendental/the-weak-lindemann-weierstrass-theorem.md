---
declaration: theorem
origin: cited
lean: TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq
statement: formalized
proof: formalized
---

# The weak Lindemann–Weierstrass theorem

Let `K` be a number field, Galois over `ℚ` and
embedded in `ℂ`. If a nonzero formal exponential sum `x = ∑ δ_γ [γ] ∈ K[K]` is fixed by the
conjugation `galConj τ` for every `τ ∈ Gal(K/ℚ)`, then `∑ δ_γ exp γ ≠ 0`.

```lean
TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq.{u_1} {K : Type u_1} [Field K]
  [NumberField K] [IsGalois ℚ K] [Algebra K ℂ] {x : AddMonoidAlgebra K K} (hx : x ≠ 0)
  (hfix : ∀ (τ : Gal(K/ℚ)), (TauCeti.LindemannWeierstrass.galConj τ) x = x) :
  (TauCeti.LindemannWeierstrass.expEval K) x ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hermite's estimate](hermites-estimate.md)
- [Hermite's identity](hermites-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Galois.html#TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Galois.html#TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq)
- [Source of `TauCeti.LindemannWeierstrass.expEval_ne_zero_of_forall_galConj_eq` in TauCeti/NumberTheory/Transcendental/Lindemann/Galois.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/Lindemann/Galois.lean#L106)
