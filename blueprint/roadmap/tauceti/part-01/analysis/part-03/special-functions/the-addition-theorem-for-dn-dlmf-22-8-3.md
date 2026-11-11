---
declaration: theorem
origin: cited
lean: TauCeti.Real.jacobiDn_add
statement: formalized
proof: formalized
---

# The addition theorem for `dn` (DLMF 22.8.3)

`dn(u + v) = (dn u · dn v - k² · sn u · cn u · sn v · cn v) / (1 - k² sn²(u) sn²(v))`.

```lean
TauCeti.Real.jacobiDn_add {k : ℝ} (hk : k ^ 2 < 1) (u v : ℝ) :
  TauCeti.Real.jacobiDn k (u + v) =
    (TauCeti.Real.jacobiDn k u * TauCeti.Real.jacobiDn k v -
        k ^ 2 * TauCeti.Real.jacobiSn k u * TauCeti.Real.jacobiCn k u * TauCeti.Real.jacobiSn k v *
          TauCeti.Real.jacobiCn k v) /
      (1 - k ^ 2 * TauCeti.Real.jacobiSn k u ^ 2 * TauCeti.Real.jacobiSn k v ^ 2)
```

## Depends on

- [The Jacobi amplitude `am(u, k)` (DLMF §22.16(i))](../../part-01/elliptic-integrals-the-agm-and-jacobi-elliptic-f/the-jacobi-amplitude-am-u-k-dlmf-22-16-i.md)

## Proof depends on

- [TauCeti.Real.legendreFOrderIso](../../part-01/elliptic-integrals-the-agm-and-jacobi-elliptic-f/tauceti-real-legendreforderiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.jacobiDn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiDn_add).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.jacobiDn_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.html#TauCeti.Real.jacobiDn_add)
- [Source of `TauCeti.Real.jacobiDn_add` in TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Addition.lean#L165)
