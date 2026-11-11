---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece
statement: formalized
proof: formalized
---

# The Littlewood–Paley decomposition of a symbol

At every point the pieces sum to the
symbol, with only finitely many nonzero terms.

```lean
TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece.{u_1, u_2} {n : ℕ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W]
  {m : ℝ} (φ : ContDiffBump 0) (a : TauCeti.Symbol n V W m)
  (p : TauCeti.CoordinateSpace n × TauCeti.CoordinateSpace n) :
  HasSum (fun j => (TauCeti.Symbol.littlewoodPaleyPiece φ a j).coefficient p) (a.coefficient p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Dyadic.html#TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Dyadic.html#TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece)
- [Source of `TauCeti.Symbol.hasSum_coefficient_littlewoodPaleyPiece` in TauCeti/Analysis/Pseudodifferential/Symbol/Dyadic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Symbol/Dyadic.lean#L106)
