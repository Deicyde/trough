---
declaration: theorem
origin: cited
lean: TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn
statement: formalized
proof: formalized
---

# Rigidity of the pre-Schwarzian derivative

Two holomorphic functions with nonvanishing
derivatives on a domain have equal pre-Schwarzian derivatives exactly when one is obtained from
the other by postcomposition with `w ↦ a * w + b` for a nonzero constant `a`.

```lean
TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn {Ω : Set ℂ} (hΩopen : IsOpen Ω)
  (hΩconn : IsPreconnected Ω) {f g : ℂ → ℂ} (hfn : ∀ z ∈ Ω, deriv f z ≠ 0)
  (hgn : ∀ z ∈ Ω, deriv g z ≠ 0) :
  (∃ a, a ≠ 0 ∧ ∃ b, Set.EqOn f (fun z => a * g z + b) Ω) ↔
    Set.EqOn (logDeriv (deriv f)) (logDeriv (deriv g)) Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PreSchwarzian.html#TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PreSchwarzian.html#TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn)
- [Source of `TauCeti.exists_eqOn_const_mul_add_iff_logDeriv_deriv_eqOn` in TauCeti/Analysis/Complex/Conformal/PreSchwarzian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/PreSchwarzian.lean#L177)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ConformalMapping/STATUS.md)
