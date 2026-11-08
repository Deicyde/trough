---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul
statement: formalized
proof: formalized
---

# A newform is an eigenvector of `U_p` at every prime `p` dividing the level, with eigenvalue `a_p(f)`

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

## Proof depends on

- [Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`](../../part-02/modular-forms/classical-sturm-bound-for-finite-index-subgroups.md)
- [The Main Lemma, per character (Miyake, Lemma 4.6.8; Diamond–Shurman, Theorem 5.7.1)](the-main-lemma-per-character-miyake-lemma-4-6-8.md)
- [The Petersson adjoint formula in the second argument](../../part-02/modular-forms/the-petersson-adjoint-formula-in-the-second-argu.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../../part-02/hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)
- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](../../part-02/modular-forms/sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.html#HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.html#HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul)
- [Source of `HeckeRing.GL2.Newform.heckeUCuspNat_eq_qExpansion_coeff_smul` in TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Newforms/FullEigenform.lean#L80)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
