---
declaration: theorem
origin: cited
lean: Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem
statement: formalized
proof: formalized
---

# Euler's criterion in a finite residue domain

Let `P` be a prime of `R` with finite
quotient and `n ∣ #(R ⧸ P) - 1`. For `a ∉ P`, the class of `a` is an `n`-th power in `R ⧸ P`
exactly when `a ^ ((#(R ⧸ P) - 1) / n) ≡ 1 (mod P)`.

```lean
Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem.{u_1} {R : Type u_1} [CommRing R] {P : Ideal R}
  [P.IsPrime] [Finite (R ⧸ P)] {n : ℕ} (hdvd : n ∣ Nat.card (R ⧸ P) - 1) {a : R} (ha : a ∉ P) :
  (∃ b, b ^ n = (Ideal.Quotient.mk P) a) ↔ a ^ ((Nat.card (R ⧸ P) - 1) / n) - 1 ∈ P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's criterion in a finite field](../../../../field-theory/other-results/eulers-criterion-in-a-finite-field.md)

## Lean

Formalized in Tau Ceti as [`Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Frobenius/PowerResidue.html#Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem).

## Sources

- [Tau Ceti documentation: `Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Frobenius/PowerResidue.html#Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem)
- [Source of `Ideal.exists_pow_eq_mk_iff_pow_sub_one_mem` in TauCeti/RingTheory/Frobenius/PowerResidue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Frobenius/PowerResidue.lean#L62)
