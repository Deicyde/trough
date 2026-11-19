---
catalog: module
lean: linearIndependent_fin2'
statement: formalized
proof: formalized
---

# Binary Tower `Fin 2` Linear Independence

`CompPoly.Fields.Binary.Tower.Support.LinearIndependentFin2`, in [CompPoly/Fields/Binary/Tower/Support/LinearIndependentFin2.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/LinearIndependentFin2.lean), by Quang Dao, Chung Thai Nguyen.

> Linear-independence lemmas specialized to functions indexed by `Fin 2`.

`linearIndependent_fin2'` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/LinearIndependentFin2.lean#L30))

```lean
theorem linearIndependent_fin2' {f : Fin 2 → V} :
    LinearIndependent K f ↔ f 0 ≠ 0 ∧ ∀ a : K, a • f 0 ≠ f 1
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Binary/Tower/Support/LinearIndependentFin2.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/LinearIndependentFin2.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Support.LinearIndependentFin2.json)
