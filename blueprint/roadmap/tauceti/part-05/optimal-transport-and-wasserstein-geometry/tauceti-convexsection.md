---
declaration: def
origin: cited
lean: TauCeti.convexSection
statement: formalized
---

# TauCeti.convexSection

The section of `u` on `Ω` at `x`, with slope `ℓ` and strict height `h`.

```lean
TauCeti.convexSection.{u_1} {E : Type u_1} [AddCommGroup E] [_root_.Module ℝ E] (Ω : Set E)
  (u : E → ℝ) (x : E) (ℓ : E →ₗ[ℝ] ℝ) (h : ℝ) : Set E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.convexSection`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Section/Basic.html#TauCeti.convexSection).

## Sources

- [Tau Ceti documentation: `TauCeti.convexSection`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Section/Basic.html#TauCeti.convexSection)
- [Source of `TauCeti.convexSection` in TauCeti/Analysis/Convex/Section/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/Section/Basic.lean#L53)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
