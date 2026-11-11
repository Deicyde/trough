---
declaration: theorem
origin: cited
lean: Multiset.mul_esymm_eq_sum, TauCeti.esymm_mem_adjoin_psum
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

**Newton's identities express `eₖ` through the power sums.** Formalized in Tau Ceti as [`TauCeti.esymm_mem_adjoin_psum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.html#TauCeti.esymm_mem_adjoin_psum).

```lean
TauCeti.esymm_mem_adjoin_psum.{u_1, u_2} (σ : Type u_1) [Fintype σ] (R : Type u_2) [CommRing R]
  [Algebra ℚ R] (k : ℕ) :
  MvPolynomial.esymm σ R k ∈ Algebra.adjoin R (MvPolynomial.psum σ R '' Set.Icc 1 k)
```

## Sources

- [Tau Ceti documentation: `Multiset.mul_esymm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.html#Multiset.mul_esymm_eq_sum)
- [Source of `Multiset.mul_esymm_eq_sum` in TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean#L74)
