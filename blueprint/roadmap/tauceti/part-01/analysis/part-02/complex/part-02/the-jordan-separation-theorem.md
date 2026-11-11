---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.not_isPreconnected_compl, TauCeti.IsJordanCurve.not_isPreconnected_compl_onePoint
statement: formalized
proof: formalized
---

# The Jordan separation theorem

The complement of a Jordan curve in the plane is not
preconnected.

```lean
TauCeti.IsJordanCurve.not_isPreconnected_compl {C : Set ℂ} (h : TauCeti.IsJordanCurve C) :
  ¬IsPreconnected Cᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Janiszewski's second theorem](janiszewskis-second-theorem.md)
- [The Jordan–Brouwer separation theorem](../../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.not_isPreconnected_compl`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.not_isPreconnected_compl).

## Other forms

**The Jordan separation theorem on the Riemann sphere.** Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.not_isPreconnected_compl_onePoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/RiemannSphere.html#TauCeti.IsJordanCurve.not_isPreconnected_compl_onePoint).

```lean
TauCeti.IsJordanCurve.not_isPreconnected_compl_onePoint {J : Set (OnePoint ℂ)}
  (hJ : TauCeti.IsJordanCurve J) : ¬IsPreconnected Jᶜ
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.not_isPreconnected_compl`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.not_isPreconnected_compl)
- [Source of `TauCeti.IsJordanCurve.not_isPreconnected_compl` in TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean#L97)
