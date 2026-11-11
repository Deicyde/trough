---
declaration: theorem
origin: cited
lean: TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast, TauCeti.lcm_pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast, TauCeti.pow_mul_eval_hasseDeriv_map_multichoose_X_add_one_comp_C_mul_X_mem_range_intCast
statement: formalized
proof: formalized
---

# Baker's denominator bound

If each of `1, …, k` divides the integer `L`, then for every
integer `x` and all `l, m`,

`L ^ m Δ(x; k, l, m) = L ^ m (1 / m!) (d / dx) ^ m (Δ(x; k) ^ l)`

is an integer.

```lean
TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast {k : ℕ} {L : ℤ}
  (hL : ∀ j ∈ Finset.Icc 1 k, ↑j ∣ L) (l m : ℕ) (x : ℤ) :
  ↑L ^ m *
      Polynomial.eval (↑x) ((Polynomial.hasseDeriv m) (Ring.multichoose (Polynomial.X + 1) k ^ l)) ∈
    Set.range Int.cast
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Baker/Delta.html#TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast).

## Other forms

**Baker's denominator bound, classical form.** Formalized in Tau Ceti as [`TauCeti.lcm_pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Baker/Delta.html#TauCeti.lcm_pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast).

```lean
TauCeti.lcm_pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast (k l m : ℕ)
  (x : ℤ) :
  ↑((Finset.Icc 1 k).lcm id) ^ m *
      Polynomial.eval (↑x) ((Polynomial.hasseDeriv m) (Ring.multichoose (Polynomial.X + 1) k ^ l)) ∈
    Set.range Int.cast
```

**Baker's denominator bound at points of a scaled lattice.** Formalized in Tau Ceti as [`TauCeti.pow_mul_eval_hasseDeriv_map_multichoose_X_add_one_comp_C_mul_X_mem_range_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Baker/Delta.html#TauCeti.pow_mul_eval_hasseDeriv_map_multichoose_X_add_one_comp_C_mul_X_mem_range_intCast).

```lean
TauCeti.pow_mul_eval_hasseDeriv_map_multichoose_X_add_one_comp_C_mul_X_mem_range_intCast.{u_1}
  {K : Type u_1} [Field K] [CharZero K] {k : ℕ} {L : ℤ} (hL : ∀ j ∈ Finset.Icc 1 k, ↑j ∣ L) (q : ℤ)
  {x : K} (hx : ↑q * x ∈ Set.range Int.cast) (m : ℕ) :
  ↑L ^ m *
      Polynomial.eval x
        ((Polynomial.hasseDeriv m)
          (Polynomial.map (algebraMap ℚ K)
            ((Ring.multichoose (Polynomial.X + 1) k).comp (Polynomial.C ↑q * Polynomial.X)))) ∈
    Set.range Int.cast
```

## Sources

- [Tau Ceti documentation: `TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Baker/Delta.html#TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast)
- [Source of `TauCeti.pow_mul_eval_hasseDeriv_multichoose_X_add_one_pow_mem_range_intCast` in TauCeti/NumberTheory/Transcendental/Baker/Delta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/Baker/Delta.lean#L174)
