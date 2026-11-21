---
catalog: module
lean: CompPoly.GuruswamiSudan.nonzeroEntryCount
statement: formalized
proof: formalized
---

# Guruswami-Sudan Shared Utilities

`CompPoly.Bivariate.GuruswamiSudan.Util`, in [CompPoly/Bivariate/GuruswamiSudan/Util.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Util.lean), by Valerii Huhnin.

> Small helpers shared by the interpolation and root-finding implementation
> modules.

`CompPoly.GuruswamiSudan.nonzeroEntryCount` (definition, [line 22](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Util.lean#L22))

> Count nonzero entries in a dense coefficient vector.

```lean
def nonzeroEntryCount {F : Type _} [Zero F] [BEq F] (v : Array F) : Nat
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Util.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Util.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Util.json)
