---
declaration: theorem
origin: cited
lean: TauCeti.schwarzian_comp
statement: formalized
proof: formalized
---

# The chain rule for the Schwarzian derivative

If `g` is holomorphic at `x` and `f` is
holomorphic at `g x` with `f' (g x) ≠ 0`, then `S(f ∘ g) = (S(f) ∘ g) * (g') ^ 2 + S(g)` at
`x`.  No hypothesis on `g' x` is needed: if it vanishes, both sides vanish.

```lean
TauCeti.schwarzian_comp {f g : ℂ → ℂ} {x : ℂ} (hf : AnalyticAt ℂ f (g x)) (hg : AnalyticAt ℂ g x)
  (hfn : deriv f (g x) ≠ 0) :
  TauCeti.schwarzian (f ∘ g) x = TauCeti.schwarzian f (g x) * deriv g x ^ 2 + TauCeti.schwarzian g x
```

## Depends on

- [TauCeti.schwarzian](tauceti-schwarzian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.schwarzian_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.schwarzian_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian_comp)
- [Source of `TauCeti.schwarzian_comp` in TauCeti/Analysis/Complex/Conformal/Schwarzian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/Schwarzian.lean#L108)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)
