---
declaration: theorem
origin: cited
lean: MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq
statement: formalized
proof: formalized
---

# The SAGBI criterion

Let `c` be a family of monic polynomials over a field, write
`A w = ∑ i, w i • m.degree (c i)`, and let binomials `Y^(u j) - Y^(v j)` generate the toric ideal
of the leading exponents of `c`. Then `c` is a SAGBI basis of the subalgebra it generates if and
only if, for every `j`, the image of `Y^(u j) - Y^(v j)` under `aeval c` is the image of a
polynomial all of whose exponents `w` satisfy `A w ≺ A (u j)`.

```lean
MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq.{u_1, u_2, u_3, u_4, u_5} {σ : Type u_1}
  {ι : Type u_2} {m : MonomialOrder σ} {k : Type u_3} {J : Type u_4} [Field k]
  {c : ι → MvPolynomial σ k} (hc : ∀ (i : ι), m.Monic (c i)) {u v : J → ι →₀ ℕ}
  (hJ :
    (TauCeti.toricIdeal k fun i => m.degree (c i)) =
      Ideal.span
        (Set.range fun j => (MvPolynomial.monomial (u j)) 1 - (MvPolynomial.monomial (v j)) 1)) :
  m.IsSAGBIBasis (Set.range c) (Algebra.adjoin k (Set.range c)) ↔
    ∀ (j : J),
      ∃ Q,
        (MvPolynomial.aeval c) Q =
            (MvPolynomial.aeval c)
              ((MvPolynomial.monomial (u j)) 1 - (MvPolynomial.monomial (v j)) 1) ∧
          ∀ w ∈ Q.support,
            m.toSyn ((Finsupp.linearCombination ℕ fun i => m.degree (c i)) w) <
              m.toSyn ((Finsupp.linearCombination ℕ fun i => m.degree (c i)) (u j))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SAGBI/Criterion.html#MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq).

## Sources

- [Tau Ceti documentation: `MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SAGBI/Criterion.html#MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq)
- [Source of `MonomialOrder.isSAGBIBasis_range_iff_forall_exists_aeval_eq` in TauCeti/RingTheory/MvPolynomial/SAGBI/Criterion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/SAGBI/Criterion.lean#L236)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
