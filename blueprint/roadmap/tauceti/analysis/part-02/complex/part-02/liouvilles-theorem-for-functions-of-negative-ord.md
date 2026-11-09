---
declaration: theorem
origin: cited
lean: TauCeti.OrderLE.isConst
statement: formalized
proof: formalized
---

# Liouville's theorem for functions of negative order

An entire function of order at most
`A < 0` is constant.

```lean
TauCeti.OrderLE.isConst {f : ℂ → ℂ} {A : ℝ} (h : TauCeti.OrderLE f A) (hf : Differentiable ℂ f)
  (hA : A < 0) : Function.IsConst f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrderLE.isConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder.html#TauCeti.OrderLE.isConst).

## Sources

- [Tau Ceti documentation: `TauCeti.OrderLE.isConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder.html#TauCeti.OrderLE.isConst)
- [Source of `TauCeti.OrderLE.isConst` in TauCeti/Analysis/Complex/GrowthOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/GrowthOrder.lean#L160)
