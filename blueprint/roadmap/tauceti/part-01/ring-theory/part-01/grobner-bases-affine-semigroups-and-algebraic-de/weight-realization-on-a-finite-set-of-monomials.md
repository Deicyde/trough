---
declaration: theorem
origin: cited
lean: MonomialOrder.exists_pos_weight_lt_iff_lt
statement: formalized
proof: formalized
---

# Weight realization on a finite set of monomials

On a finite set `F` of monomials, some
weight vector with positive entries induces exactly the strict comparisons of the monomial order
`m`.

```lean
MonomialOrder.exists_pos_weight_lt_iff_lt.{u_1, u_2} {σ : Type u_1} (m : MonomialOrder σ)
  {F : Set (σ →₀ ℕ)} (hF : F.Finite) :
  ∃ w,
    (∀ (i : σ), 0 < w i) ∧
      ∀ a ∈ F, ∀ b ∈ F, m.toSyn a < m.toSyn b ↔ (Finsupp.weight w) a < (Finsupp.weight w) b
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](../../../geometry/part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`MonomialOrder.exists_pos_weight_lt_iff_lt`](https://taucetiproject.org/docs/TauCeti/Data/Finsupp/MonomialOrder/Weight.html#MonomialOrder.exists_pos_weight_lt_iff_lt).

## Sources

- [Tau Ceti documentation: `MonomialOrder.exists_pos_weight_lt_iff_lt`](https://taucetiproject.org/docs/TauCeti/Data/Finsupp/MonomialOrder/Weight.html#MonomialOrder.exists_pos_weight_lt_iff_lt)
- [Source of `MonomialOrder.exists_pos_weight_lt_iff_lt` in TauCeti/Data/Finsupp/MonomialOrder/Weight.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/Finsupp/MonomialOrder/Weight.lean#L131)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
