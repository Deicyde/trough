---
declaration: theorem
origin: cited
lean: Multiset.mul_esymm_eq_sum, TauCeti.SymmetricFunction.mul_of_stableEsymm_eq_sum, TauCeti.mul_esymm_succ_eq_sum, TauCeti.esymm_mem_adjoin_psum, TauCeti.mul_hsymm_eq_sum
statement: formalized
proof: formalized
---

# Newton's identities for a multiset

`k` times the `k`-th elementary symmetric function of
the elements of `s` is an explicit combination of the lower elementary symmetric functions and
the power sums `(s.map (· ^ j)).sum`. This is `MvPolynomial.mul_esymm_eq_sum` evaluated at the
elements of `s`.

```lean
Multiset.mul_esymm_eq_sum.{u_1} {R : Type u_1} [CommRing R] (s : Multiset R) (k : ℕ) :
  ↑k * s.esymm k =
    (-1) ^ (k + 1) *
      ∑ a ∈ Finset.HasAntidiagonal.antidiagonal k with a.1 < k,
        (-1) ^ a.1 * s.esymm a.1 * (Multiset.map (fun x => x ^ a.2) s).sum
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Multiset.mul_esymm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.html#Multiset.mul_esymm_eq_sum).

## Other forms

**Newton's identities in the symmetric functions.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.mul_of_stableEsymm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/PowerSum.html#TauCeti.SymmetricFunction.mul_of_stableEsymm_eq_sum).

```lean
TauCeti.SymmetricFunction.mul_of_stableEsymm_eq_sum.{u_1} (R : Type u_1) [CommRing R] (n : ℕ) :
  (↑n + 1) *
      (DirectSum.of (fun i => ↥(TauCeti.stableSymmetricSubmodule R i)) (n + 1))
        (TauCeti.stableEsymm R (n + 1)) =
    ∑ x ∈ Finset.HasAntidiagonal.antidiagonal n,
      (-1) ^ x.2 *
          (DirectSum.of (fun i => ↥(TauCeti.stableSymmetricSubmodule R i)) x.1)
            (TauCeti.stableEsymm R x.1) *
        (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) (x.2 + 1))
          (TauCeti.stablePsum R ⋯)
```

**Newton's identities in a finite alphabet, indexed by the antidiagonal of `n`.** Formalized in Tau Ceti as [`TauCeti.mul_esymm_succ_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Elementary.html#TauCeti.mul_esymm_succ_eq_sum).

```lean
TauCeti.mul_esymm_succ_eq_sum.{u_1, u_2} (σ : Type u_1) [Fintype σ] (R : Type u_2) [CommRing R]
  (n : ℕ) :
  (↑n + 1) * MvPolynomial.esymm σ R (n + 1) =
    ∑ x ∈ Finset.HasAntidiagonal.antidiagonal n,
      (-1) ^ x.2 * MvPolynomial.esymm σ R x.1 * MvPolynomial.psum σ R (x.2 + 1)
```

**Newton's identities express `eₖ` through the power sums.** Formalized in Tau Ceti as [`TauCeti.esymm_mem_adjoin_psum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.html#TauCeti.esymm_mem_adjoin_psum).

```lean
TauCeti.esymm_mem_adjoin_psum.{u_1, u_2} (σ : Type u_1) [Fintype σ] (R : Type u_2) [CommRing R]
  [Algebra ℚ R] (k : ℕ) :
  MvPolynomial.esymm σ R k ∈ Algebra.adjoin R (MvPolynomial.psum σ R '' Set.Icc 1 k)
```

**Newton's identities for the complete homogeneous symmetric polynomials.** Formalized in Tau Ceti as [`TauCeti.mul_hsymm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Complete/PowerSum.html#TauCeti.mul_hsymm_eq_sum).

```lean
TauCeti.mul_hsymm_eq_sum.{u_1, u_2} (σ : Type u_1) [Fintype σ] [DecidableEq σ] (R : Type u_2)
  [CommSemiring R] (k : ℕ) :
  ↑k * MvPolynomial.hsymm σ R k =
    ∑ a ∈ Finset.HasAntidiagonal.antidiagonal k with a.1 < k,
      MvPolynomial.hsymm σ R a.1 * MvPolynomial.psum σ R a.2
```

## Sources

- [Tau Ceti documentation: `Multiset.mul_esymm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.html#Multiset.mul_esymm_eq_sum)
- [Source of `Multiset.mul_esymm_eq_sum` in TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean#L74)
