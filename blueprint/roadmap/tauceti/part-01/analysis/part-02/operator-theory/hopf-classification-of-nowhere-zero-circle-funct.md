---
declaration: theorem
origin: cited
lean: ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier
statement: formalized
proof: formalized
---

# Hopf classification of nowhere-zero circle functions

A nowhere-zero continuous circle
function has winding number `k` if and only if it is homotopic through nowhere-zero continuous
functions to `fourier k`.

```lean
ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier {T : ℝ} [Fact (0 < T)]
  (f : C(AddCircle T, ℂ)) (hf : ∀ (x : AddCircle T), f x ≠ 0) (k : ℤ) :
  f.windingNumber hf = k ↔
    ∃ H,
      (∀ (p : ↑unitInterval × AddCircle T), H p ≠ 0) ∧
        (∀ (x : AddCircle T), H (0, x) = f x) ∧ ∀ (x : AddCircle T), H (1, x) = (fourier k) x
```

## Depends on

- [ContinuousMap.windingNumber](continuousmap-windingnumber.md)

## Lean

Formalized in Tau Ceti as [`ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Winding.html#ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier).

## Sources

- [Tau Ceti documentation: `ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Winding.html#ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier)
- [Source of `ContinuousMap.windingNumber_eq_iff_exists_homotopy_fourier` in TauCeti/Analysis/Fourier/Winding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Winding.lean#L325)
