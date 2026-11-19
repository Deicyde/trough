---
catalog: module
lean: CPoly.lawfulBEqOfDecidableEq
statement: formalized
proof: formalized
---

# `LawfulBEq` from `DecidableEq`

`CompPoly.Data.Classes.LawfulBEq`, in [CompPoly/Data/Classes/LawfulBEq.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/LawfulBEq.lean), by Andrew Zitek-Estrada.

> A canonical `LawfulBEq` derived from `DecidableEq`, suitable for `letI` use at
> call sites that need to satisfy `BEq`/`LawfulBEq` constraints (for example on
> `CMvPolynomial` API surfaces) from a `DecidableEq`-only context.
>
> This is intentionally *not* registered as an instance: doing so would conflict
> with other `BEq` paths chosen by typeclass synthesis.

`CPoly.lawfulBEqOfDecidableEq` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/LawfulBEq.lean#L30))

> A canonical `LawfulBEq` instance derived from `DecidableEq`. Intended for
> `letI` use at call sites that need to satisfy `BEq`/`LawfulBEq` constraints
> from a `DecidableEq`-only context.

```lean
def lawfulBEqOfDecidableEq {α : Type*} [DecidableEq α] :
    @LawfulBEq α (instBEqOfDecidableEq)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Classes/LawfulBEq.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/LawfulBEq.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Classes.LawfulBEq.json)
