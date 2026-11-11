---
declaration: theorem
origin: cited
lean: TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min
statement: formalized
proof: formalized
---

# The Eichler–Selberg trace formula at level one

For even `k = w + 2 ≥ 4` and `n ≥ 1`, the
trace of `Tₙ` on the cusp forms of weight `k` on `SL(2, ℤ)` is

`tr(Tₙ | S_k) = -½ ∑_{t² ≤ 4n} H(4n - t²) P_k(t, n) - ½ ∑_{dd' = n} min(d, d')^(k-1)`,

with Hurwitz class numbers normalized by `H(0) = -1/12` and `P_k(t, n) = (dickson 2 n w).eval t`.
The sum over `t` runs over the integers with `t² ≤ 4n`, written as a filter of `[-4n, 4n]`.

```lean
TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min {k : ℤ} {w : ℕ} (hk : k = ↑w + 2)
  (hw : Even w) (hw₀ : w ≠ 0) (n : ℕ) [NeZero n] :
  (LinearMap.trace ℂ (CuspForm (Matrix.SpecialLinearGroup.mapGL ℝ).range k))
      (TauCeti.heckeTCuspLevelOne k n) =
    (-∑ t ∈ Finset.Icc (-4 * ↑n) (4 * ↑n) with t ^ 2 ≤ 4 * ↑n,
            ↑(TauCeti.hurwitzClassNumber (4 * ↑n - t ^ 2).toNat) *
              Polynomial.eval (↑t) (Polynomial.dickson 2 (↑n) w)) /
        2 -
      (∑ p ∈ n.divisorsAntidiagonal, ↑(min p.1 p.2) ^ (w + 1)) / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton in size two](../../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)
- [Popa–Zagier's ambient trace identity (Popa–Zagier, §2, Propositions 2 and 3)](popa-zagiers-ambient-trace-identity-popa-zagier.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/EichlerSelberg.html#TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min).

## Sources

- [Tau Ceti documentation: `TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/EichlerSelberg.html#TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min)
- [Source of `TauCeti.trace_heckeTCuspLevelOne_eq_neg_hurwitzClassNumber_sub_min` in TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/EichlerSelberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/EichlerSelberg.lean#L57)
