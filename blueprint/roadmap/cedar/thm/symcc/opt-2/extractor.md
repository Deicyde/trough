---
catalog: module
lean: Cedar.Thm.extractOpt?_eqv_extract?
statement: formalized
proof: formalized
---

# Opt/Extractor

`Cedar.Thm.SymCC.Opt.Extractor`, in [Cedar/Thm/SymCC/Opt/Extractor.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Extractor.lean).

> Proofs that the optimized functions in SymCCOpt.Extractor are equivalent to the unoptimized
> ones in SymCC.Extractor.

`Cedar.Thm.extractOpt?_eqv_extract?` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Extractor.lean#L58))

```lean
theorem extractOpt?_eqv_extract? {cpsets : List CompiledPolicies} {I : Interpretation} {εnv : SymEnv} :
  cpsets ≠ [] →
  (∀ cpset ∈ cpsets, cpset.εnv = εnv) →
  -- the `CompiledPolicies` at least have to be constructed with `CompiledPolicy.compile` or `CompiledPolicySet.compile`, even though we don't care about the original uncompiled policies
  (∀ cpset ∈ cpsets, match cpset with
    | .policy cp => ∃ p s reqty, CompiledPolicy.compile p s reqty = .ok cp
    | .pset cpset => ∃ ps s reqty, CompiledPolicySet.compile ps s reqty = .ok cpset
  ) →
  extractOpt? cpsets I = SymEnv.extract? ((cpsets.flatMap CompiledPolicies.allPolicies).map Policy.toExpr) I εnv
```

## Depends on

- [Extracting strongly well-formed counterexamples to verification queries (SymCCOpt/Extractor)](../../../symccopt/extractor.md)

## Proof depends on

- [Opt/CompiledPolicies](compiledpolicies.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Extractor.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Extractor.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Extractor.json)
