---
declaration: theorem
origin: cited
lean: TauCeti.Real.jacobiSn_add
statement: formalized
proof: formalized
---

# The addition theorem for `sn` (DLMF 22.8.1)

`sn(u + v) = (sn u · cn v · dn v + sn v · cn u · dn u) / (1 - k² sn²(u) sn²(v))`.

```lean
TauCeti.Real.jacobiSn_add {k : ℝ} (hk : k ^ 2 < 1) (u v : ℝ) :
  TauCeti.Real.jacobiSn k (u + v) =
    (TauCeti.Real.jacobiSn k u * TauCeti.Real.jacobiCn k v * TauCeti.Real.jacobiDn k v +
        TauCeti.Real.jacobiSn k v * TauCeti.Real.jacobiCn k u * TauCeti.Real.jacobiDn k u) /
      (1 - k ^ 2 * TauCeti.Real.jacobiSn k u ^ 2 * TauCeti.Real.jacobiSn k v ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.jacobiSn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiSn_add).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.jacobiSn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiSn_add)
- [Source of `TauCeti.Real.jacobiSn_add` in TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean#L106)
