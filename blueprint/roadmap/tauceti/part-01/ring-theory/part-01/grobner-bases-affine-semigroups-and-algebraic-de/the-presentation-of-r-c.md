---
declaration: theorem
origin: cited
lean: MonomialOrder.ker_aeval_eq_span
statement: formalized
proof: formalized
---

# The presentation of `R[c]`

Let `c` be a monic family, write
`A w = ∑ i, w i • m.degree (c i)`, and let binomials `Y^(u j) - Y^(v j)` generate the toric ideal of
the leading exponents of `c`. If each image `aeval c (Y^(u j) - Y^(v j))` is the image of a
polynomial `Q j` all of whose exponents `w` satisfy `A w ≺ A (u j)`, then the lifted relations
`Y^(u j) - Y^(v j) - Q j` generate the kernel of `aeval c`.

```lean
MonomialOrder.ker_aeval_eq_span.{u_1, u_2, u_3, u_4, u_5} {σ : Type u_1} {ι : Type u_2}
  {R : Type u_3} {J : Type u_4} {m : MonomialOrder σ} [CommRing R] {c : ι → MvPolynomial σ R}
  [Nontrivial R] (hc : ∀ (i : ι), m.Monic (c i)) {u v : J → ι →₀ ℕ}
  (hJ :
    (TauCeti.toricIdeal R fun i => m.degree (c i)) =
      Ideal.span
        (Set.range fun j => (MvPolynomial.monomial (u j)) 1 - (MvPolynomial.monomial (v j)) 1))
  {Q : J → MvPolynomial ι R}
  (hQc :
    ∀ (j : J),
      (MvPolynomial.aeval c) (Q j) =
        (MvPolynomial.aeval c) ((MvPolynomial.monomial (u j)) 1 - (MvPolynomial.monomial (v j)) 1))
  (hQ :
    ∀ (j : J),
      ∀ w ∈ (Q j).support,
        m.toSyn ((Finsupp.linearCombination ℕ fun i => m.degree (c i)) w) <
          m.toSyn ((Finsupp.linearCombination ℕ fun i => m.degree (c i)) (u j))) :
  RingHom.ker (MvPolynomial.aeval c) =
    Ideal.span
      (Set.range fun j => (MvPolynomial.monomial (u j)) 1 - (MvPolynomial.monomial (v j)) 1 - Q j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonomialOrder.ker_aeval_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SAGBI/Presentation.html#MonomialOrder.ker_aeval_eq_span).

## Sources

- [Tau Ceti documentation: `MonomialOrder.ker_aeval_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SAGBI/Presentation.html#MonomialOrder.ker_aeval_eq_span)
- [Source of `MonomialOrder.ker_aeval_eq_span` in TauCeti/RingTheory/MvPolynomial/SAGBI/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/SAGBI/Presentation.lean#L115)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
