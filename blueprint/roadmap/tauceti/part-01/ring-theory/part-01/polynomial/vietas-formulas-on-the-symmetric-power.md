---
declaration: theorem
origin: cited
lean: Sym.coeff_toMonic, MvPolynomial.aeval_esymm_eq_coeff_prod_X_sub_C, Polynomial.IsRootEnumeration.aeval_esymm_eq_coeff
statement: formalized
proof: formalized
---

# Vieta's formulas on the symmetric power

the `k`-th coefficient of the monic polynomial of
an unordered `n`-tuple is the `(n - k)`-th elementary symmetric function of the tuple, up to the
sign `(-1) ^ (n - k)`.

```lean
Sym.coeff_toMonic.{u_1} {R : Type u_1} [CommRing R] {n : ℕ} [Nontrivial R] (s : Sym R n) {k : ℕ}
  (hk : k ≤ n) : (↑s.toMonic).coeff k = (-1) ^ (n - k) * (↑s).esymm (n - k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Sym.coeff_toMonic`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/SymmetricPower.html#Sym.coeff_toMonic).

## Other forms

**Vieta's formulas for an indexed family of roots.** Formalized in Tau Ceti as [`MvPolynomial.aeval_esymm_eq_coeff_prod_X_sub_C`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#MvPolynomial.aeval_esymm_eq_coeff_prod_X_sub_C).

```lean
MvPolynomial.aeval_esymm_eq_coeff_prod_X_sub_C.{u_1, u_2, u_3} {σ : Type u_1} {R : Type u_2}
  {S : Type u_3} [Fintype σ] [CommSemiring R] [CommRing S] [Algebra R S] (x : σ → S) {k : ℕ}
  (hk : k ≤ Fintype.card σ) :
  (MvPolynomial.aeval x) (MvPolynomial.esymm σ R k) =
    (-1) ^ k * (∏ i, (Polynomial.X - Polynomial.C (x i))).coeff (Fintype.card σ - k)
```

**Vieta's formulas, read through a root enumeration.** Formalized in Tau Ceti as [`Polynomial.IsRootEnumeration.aeval_esymm_eq_coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/RootEnumeration.html#Polynomial.IsRootEnumeration.aeval_esymm_eq_coeff).

```lean
Polynomial.IsRootEnumeration.aeval_esymm_eq_coeff.{u_1, u_2, u_4} {R : Type u_1} {L : Type u_2}
  {ι : Type u_4} [CommRing R] [CommRing L] [IsDomain L] [Algebra R L] [Fintype ι] {f : Polynomial R}
  {x : ι → L} (hx : f.IsRootEnumeration x) (hf : f.Monic) (hdeg : f.natDegree ≤ Fintype.card ι)
  {k : ℕ} (hk : k ≤ Fintype.card ι) :
  (MvPolynomial.aeval x) (MvPolynomial.esymm ι R k) =
    (-1) ^ k * (algebraMap R L) (f.coeff (Fintype.card ι - k))
```

## Sources

- [Tau Ceti documentation: `Sym.coeff_toMonic`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/SymmetricPower.html#Sym.coeff_toMonic)
- [Source of `Sym.coeff_toMonic` in TauCeti/RingTheory/Polynomial/SymmetricPower.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/SymmetricPower.lean#L164)
