---
declaration: theorem
origin: cited
lean: TauCeti.eventually_ricciWidthProfile_neg
statement: formalized
proof: formalized
---

# TauCeti.eventually_ricciWidthProfile_neg

Every finite initial width gives an eventually negative comparison profile.

```lean
TauCeti.eventually_ricciWidthProfile_neg (w : ℝ) :
  ∀ᶠ (t : ℝ) in Filter.atTop, TauCeti.ricciWidthProfile w t < 0
```

## Depends on

- [TauCeti.ricciWidthProfile](tauceti-ricciwidthprofile.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eventually_ricciWidthProfile_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.eventually_ricciWidthProfile_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.eventually_ricciWidthProfile_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/WidthComparison.html#TauCeti.eventually_ricciWidthProfile_neg)
- [Source of `TauCeti.eventually_ricciWidthProfile_neg` in TauCeti/Geometry/RicciFlow/WidthComparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RicciFlow/WidthComparison.lean#L160)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Poincare3D/STATUS.md)
