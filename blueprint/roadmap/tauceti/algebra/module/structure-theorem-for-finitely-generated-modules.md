---
declaration: theorem
origin: cited
lean: TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow
statement: formalized
proof: formalized
---

# Structure theorem for finitely generated modules over a discrete valuation ring

A
finitely generated module over a discrete valuation ring `R` with uniformizer `ϖ` is isomorphic
to `R ^ n × ∏ i : Fin m, R ⧸ (ϖ ^ e i)` with every exponent `e i` positive.

```lean
TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow.{u, v} (R : Type u) (M : Type v) [CommRing R]
  [IsDomain R] [IsDiscreteValuationRing R] [AddCommGroup M] [_root_.Module R M] [Module.Finite R M]
  {ϖ : R} (hϖ : Irreducible ϖ) :
  ∃ n m e,
    (∀ (i : Fin m), 0 < e i) ∧ Nonempty (M ≃ₗ[R] (Fin n → R) × ((i : Fin m) → R ⧸ R ∙ ϖ ^ e i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/DiscreteValuationRing.html#TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/DiscreteValuationRing.html#TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow)
- [Source of `TauCeti.Module.equiv_pi_prod_pi_quotient_span_pow` in TauCeti/Algebra/Module/DiscreteValuationRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/DiscreteValuationRing.lean#L36)
