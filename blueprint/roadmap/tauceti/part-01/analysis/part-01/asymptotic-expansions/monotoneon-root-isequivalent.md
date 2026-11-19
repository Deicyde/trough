---
declaration: theorem
origin: cited
lean: MonotoneOn.root_isEquivalent
statement: formalized
proof: formalized
---

# MonotoneOn.root_isEquivalent

DLMF 2.2.2: if `f` is monotone on `[a, ∞)` with `f(x) ∼ x` as `x → +∞`, then any function `g`
such that `g y` is eventually a root of `f(x) = y` in `[a, ∞)` satisfies `g(y) ∼ y` as
`y → +∞`.

```lean
MonotoneOn.root_isEquivalent {f : ℝ → ℝ} {a : ℝ} (hmono : MonotoneOn f (Set.Ici a))
  (hfx : Asymptotics.IsEquivalent Filter.atTop f id) {g : ℝ → ℝ}
  (hg : ∀ᶠ (y : ℝ) in Filter.atTop, a ≤ g y ∧ f (g y) = y) :
  Asymptotics.IsEquivalent Filter.atTop g id
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonotoneOn.root_isEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/TranscendentalEquation.html#MonotoneOn.root_isEquivalent).

## Sources

- [Tau Ceti documentation: `MonotoneOn.root_isEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/TranscendentalEquation.html#MonotoneOn.root_isEquivalent)
- [Source of `MonotoneOn.root_isEquivalent` in TauCeti/Analysis/Asymptotics/TranscendentalEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Asymptotics/TranscendentalEquation.lean#L49)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
