---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul
statement: formalized
proof: formalized
---

# HeckeRing.GL2.Newform.heckeUCuspNat\_eq\_qExpansion\_coeff\_smul

**A newform is an eigenvector of `U_p` at every prime `p` dividing the level, with eigenvalue
`a_p(f)`** (Atkin–Lehner; Li; Diamond–Shurman, Theorem 5.8.2; Miyake, Theorem 4.6.13). Together
with the good eigensystem this makes a newform a full Hecke eigenform (`Newform.toEigenform`).
The statement is on the bad-prime operator `heckeUCuspNat`, matching the `U_p`-spelled API of
`HeckeSlash/BadPrime`; `Newform.heckeTCuspNat_eq_qExpansion_coeff_smul` is the statement at
every prime.

```lean
HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul {N : ℕ} [NeZero N] {k : ℤ}
  (f : HeckeRing.GL2.Newform N k) {p : ℕ} (hp : Nat.Prime p) (hpN : p ∣ N) :
  (HeckeRing.GL2.heckeUCuspNat k p hp hpN) f.toCuspForm =
    (PowerSeries.coeff p) (UpperHalfPlane.qExpansion 1 ⇑f.toCuspForm) • f.toCuspForm
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.html#HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.html#HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul)
- [Source of `HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul` in TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.lean#L80)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
