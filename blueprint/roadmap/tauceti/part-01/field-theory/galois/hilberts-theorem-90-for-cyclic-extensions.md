---
declaration: theorem
origin: cited
lean: TauCeti.exists_smul_div_eq_iff_norm_eq_one
statement: formalized
proof: formalized
---

# Hilbert's Theorem 90 for cyclic extensions

If `g` generates `Gal(L/K)`, then a unit `x`
of `L` has norm one if and only if `x = g y / y` for a unit `y` of `L`.

```lean
TauCeti.exists_smul_div_eq_iff_norm_eq_one.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [Field L] [Algebra K L] [FiniteDimensional K L] [IsGalois K L] {g : Gal(L/K)}
  (hg : ∀ (σ : Gal(L/K)), σ ∈ Subgroup.zpowers g) {x : Lˣ} :
  (∃ y, g • y / y = x) ↔ (Algebra.norm K) ↑x = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_smul_div_eq_iff_norm_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/Hilbert90.html#TauCeti.exists_smul_div_eq_iff_norm_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_smul_div_eq_iff_norm_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/Hilbert90.html#TauCeti.exists_smul_div_eq_iff_norm_eq_one)
- [Source of `TauCeti.exists_smul_div_eq_iff_norm_eq_one` in TauCeti/FieldTheory/Galois/Hilbert90.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/Galois/Hilbert90.lean#L41)
