---
declaration: theorem
origin: cited
lean: TauCeti.transcendental_exp_of_isAlgebraic, TauCeti.transcendental_of_mem_algebraicLogs
statement: formalized
proof: formalized
---

# The Hermite–Lindemann theorem

The exponential of a nonzero algebraic number is
transcendental.

```lean
TauCeti.transcendental_exp_of_isAlgebraic {α : ℂ} (hα : IsAlgebraic ℚ α) (hα0 : α ≠ 0) :
  Transcendental ℚ (Complex.exp α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Lindemann–Weierstrass theorem, in Baker's form](../../part-01/diophantine-approximation-and-transcendence/the-lindemann-weierstrass-theorem-in-bakers-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transcendental_exp_of_isAlgebraic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Corollaries.html#TauCeti.transcendental_exp_of_isAlgebraic).

## Other forms

**Hermite–Lindemann for logarithms.** Formalized in Tau Ceti as [`TauCeti.transcendental_of_mem_algebraicLogs`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Corollaries.html#TauCeti.transcendental_of_mem_algebraicLogs).

```lean
TauCeti.transcendental_of_mem_algebraicLogs {l : ℂ} (hl : l ∈ TauCeti.algebraicLogs) (hl0 : l ≠ 0) :
  Transcendental ℚ l
```

## Sources

- [Tau Ceti documentation: `TauCeti.transcendental_exp_of_isAlgebraic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/Corollaries.html#TauCeti.transcendental_exp_of_isAlgebraic)
- [Source of `TauCeti.transcendental_exp_of_isAlgebraic` in TauCeti/NumberTheory/Transcendental/Lindemann/Corollaries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/Lindemann/Corollaries.lean#L48)
