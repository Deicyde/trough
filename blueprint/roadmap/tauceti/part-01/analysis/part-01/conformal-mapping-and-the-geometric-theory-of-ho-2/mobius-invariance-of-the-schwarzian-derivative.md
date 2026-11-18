---
declaration: theorem
origin: cited
lean: TauCeti.schwarzian_moebius
statement: formalized
proof: formalized
---

# Möbius invariance of the Schwarzian derivative

If `a * d - b * c ≠ 0`, `f` is
holomorphic at `x` and `c * f x + d ≠ 0`, then postcomposing `f` with the Möbius map
`w ↦ (a * w + b) / (c * w + d)` does not change its Schwarzian derivative at `x`.

```lean
TauCeti.schwarzian_moebius {f : ℂ → ℂ} {x a b c d : ℂ} (hD : a * d - b * c ≠ 0)
  (hf : AnalyticAt ℂ f x) (hx : c * f x + d ≠ 0) :
  TauCeti.schwarzian (fun y => (a * f y + b) / (c * f y + d)) x = TauCeti.schwarzian f x
```

## Depends on

- [TauCeti.schwarzian](tauceti-schwarzian.md)

## Proof depends on

- [The chain rule for the Schwarzian derivative](the-chain-rule-for-the-schwarzian-derivative.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.schwarzian_moebius`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian_moebius).

## Sources

- [Tau Ceti documentation: `TauCeti.schwarzian_moebius`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian_moebius)
- [Source of `TauCeti.schwarzian_moebius` in TauCeti/Analysis/Complex/Conformal/Schwarzian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/Schwarzian.lean#L215)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)
