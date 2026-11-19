---
declaration: theorem
origin: cited
lean: TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero
statement: formalized
proof: formalized
---

# The pre-Schwarzian derivative is conjugation-symmetric when a reflection identity holds off the real axis

If `F` carries conjugation to the affine reflection `w ↦ c + u * conj w` at every
non-real point of an open set `Ω`, then `logDeriv (deriv F)` intertwines conjugation with
conjugation at every point `z` of `Ω` whose conjugate also lies in `Ω`, real points included. The
degenerate factor `u = 0` is allowed: then `deriv F` vanishes at `z` and at `conj z`, and both sides
are `0`.

```lean
TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero {Ω : Set ℂ}
  {F : ℂ → ℂ} {c u : ℂ} (hΩopen : IsOpen Ω)
  (hrefl : ∀ z ∈ Ω, z.im ≠ 0 → F ((starRingEnd ℂ) z) = c + u * (starRingEnd ℂ) (F z)) {z : ℂ}
  (hz : z ∈ Ω) (hz' : (starRingEnd ℂ) z ∈ Ω) :
  logDeriv (deriv F) ((starRingEnd ℂ) z) = (starRingEnd ℂ) (logDeriv (deriv F) z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/LogDeriv.html#TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/LogDeriv.html#TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero)
- [Source of `TauCeti.logDeriv_deriv_conj_eq_conj_logDeriv_deriv_of_isOpen_of_forall_im_ne_zero` in TauCeti/Analysis/Complex/Conformal/Reflection/LogDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/Reflection/LogDeriv.lean#L272)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ConformalMapping/STATUS.md)
