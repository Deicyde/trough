---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm
statement: formalized
proof: formalized
---

# An elliptic symbol has a two-sided parametrix symbol

A symbol `a` of order `m` that is
elliptic above some radius has a parametrix symbol `b` of order `-m`: the formal compositions of
`b` with `a` in both orders are the identity, `1 ∼ ∑ₖ sharpTerm b a k` and
`1 ∼ ∑ₖ sharpTerm a b k`. It is unique modulo smoothing symbols
(`TauCeti.Symbol.isAsymptoticSum_sharpTerm_left_iff`), and agrees with the cut-off inverse
`χ(ξ / t) a(x, ξ)⁻¹` (`TauCeti.Symbol.cutoffInverse`) up to a symbol of order `-m - 1`
(`TauCeti.Symbol.exists_coefficient_sub_eq_of_isAsymptoticSum_sharpTerm_left`).

```lean
TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm.{u_1, u_2} {n : ℕ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W]
  {m : ℝ} [CompleteSpace V] {a : TauCeti.Symbol n V W m} {R : ℝ} (ha : a.IsEllipticAbove R) :
  ∃ b,
    ((TauCeti.Symbol.inclusion ⋯)
            (TauCeti.Symbol.const (ContinuousLinearMap.id ℂ V))).IsAsymptoticSum
        (b.sharpTerm a) ∧
      ((TauCeti.Symbol.inclusion ⋯)
            (TauCeti.Symbol.const (ContinuousLinearMap.id ℂ W))).IsAsymptoticSum
        (a.sharpTerm b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Parametrix.html#TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Parametrix.html#TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm)
- [Source of `TauCeti.Symbol.IsEllipticAbove.exists_isAsymptoticSum_sharpTerm` in TauCeti/Analysis/Pseudodifferential/Composition/Parametrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/Composition/Parametrix.lean#L391)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
