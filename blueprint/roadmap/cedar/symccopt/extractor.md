---
catalog: module
lean: Cedar.SymCC.extractOpt?
statement: formalized
proof: formalized
---

# Extracting strongly well-formed counterexamples to verification queries (SymCCOpt/Extractor)

`Cedar.SymCCOpt.Extractor`, in [Cedar/SymCCOpt/Extractor.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Extractor.lean).

> This file defines the function `extractOpt?`, which turns interpretations
> into concrete, strongly well-formed counterexamples to verification queries.
>
> See notes on the unoptimized version, `extract?` in `SymCC/Extractor.lean`.
>
> This optimized version is proved equivalent to the unoptimized version in `Thm/SymCC/Opt.lean`.

`Cedar.SymCC.extractOpt?` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Extractor.lean#L42))

> Optimized version of `extract?` in `SymCC/Extractor.lean`.
>
> Caller guarantees that all of the `CompiledPolicy`s and/or `CompiledPolicySet`s were compiled for the same `εnv`.

```lean
public def extractOpt? (cpss : List CompiledPolicies) (I : Interpretation) : Option Env
```

## Depends on

- [SymCCOpt/CompiledPolicies](compiledpolicies.md)

## Sources

- [Cedar/SymCCOpt/Extractor.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Extractor.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.Extractor.json)
