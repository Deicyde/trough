---
declaration: theorem
origin: cited
lean: TauCeti.Real.jacobiCn_add
statement: formalized
proof: formalized
---

# The addition theorem for `cn` (DLMF 22.8.2)

`cn(u + v) = (cn u · cn v - sn u · dn u · sn v · dn v) / (1 - k² sn²(u) sn²(v))`.

```lean
TauCeti.Real.jacobiCn_add {k : ℝ} (hk : k ^ 2 < 1) (u v : ℝ) :
  TauCeti.Real.jacobiCn k (u + v) =
    (TauCeti.Real.jacobiCn k u * TauCeti.Real.jacobiCn k v -
        TauCeti.Real.jacobiSn k u * TauCeti.Real.jacobiDn k u * TauCeti.Real.jacobiSn k v *
          TauCeti.Real.jacobiDn k v) /
      (1 - k ^ 2 * TauCeti.Real.jacobiSn k u ^ 2 * TauCeti.Real.jacobiSn k v ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.jacobiCn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiCn_add).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.jacobiCn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiCn_add)
- [Source of `TauCeti.Real.jacobiCn_add` in TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean#L137)
