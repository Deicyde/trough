---
catalog: module
lean: Cedar.SymCC.UnaryFunction.uuf?, Cedar.SymCC.SymEntityData.uufAncestors, Cedar.SymCC.SymEntities.uufAncestors, Cedar.SymCC.UUF.repairAncestors, Cedar.SymCC.Interpretation.repair, Cedar.SymCC.SymEnv.extract?
statement: formalized
proof: formalized
---

# Extracting strongly well-formed counterexamples to verification queries (SymCC/Extractor)

`Cedar.SymCC.Extractor`, in [Cedar/SymCC/Extractor.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean).

> This file defines the function `extract?`, which turns interpretations
> into concrete, strongly well-formed counterexamples to verification queries.
>
> The function takes as input a list of expressions `xs`, an interpretation `I`,
> and a symbolic environment `εnv`.  Given these inputs, it returns an environment
> `env ∈ εnv` such that `env` is strongly well-formed, and each term in
> `footprint xs εnv` has the same interpretation under both `I` and every `I'`
> for which f `env ∼ εnv.interpret I'`.
>
> If `I` is the result of solving a `verify*` query (see Cedar.SymCC.Verifier),
> then `εnv.extract? xs I` is a valid strongly well-formed counterexample
> to that query. More generally, `εnv.extract? xs I` extracts such a
> counterexample for any verification query that is expressed as a boolean
> combination of (boolean) terms obtained by compiling `xs` with respect to `εnv`.
>
> See `Cedar.Thm.SymCC.Verification` for how this is used to prove that verification
> queries based on Cedar's compiler and hierarchy enforcer are correct.

`Cedar.SymCC.UnaryFunction.uuf?` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L52))

```lean
def UnaryFunction.uuf? : UnaryFunction → Option UUF
```

`Cedar.SymCC.SymEntityData.uufAncestors` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L56))

```lean
def SymEntityData.uufAncestors (δ : SymEntityData) : Set UUF
```

`Cedar.SymCC.SymEntities.uufAncestors` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L59))

```lean
def SymEntities.uufAncestors (εs : SymEntities) : Set UUF
```

`Cedar.SymCC.UUF.repairAncestors` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L62))

```lean
def UUF.repairAncestors (fts : Set EntityUID) (I : Interpretation) (f : UUF) : UDF
```

`Cedar.SymCC.Interpretation.repair` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L76))

```lean
def Interpretation.repair (footprint : Set Term) (εnv : SymEnv) (I : Interpretation) : Interpretation
```

`Cedar.SymCC.SymEnv.extract?` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean#L86))

```lean
def SymEnv.extract? (xs : List Expr) (I : Interpretation) (εnv : SymEnv) : Option Env
```

## Depends on

- [Concretizing symbolic environments](concretizer.md)
- [Cedar/SymCC/Enforcer](enforcer.md)
- [Interpretations](interpretation.md)

## Sources

- [Cedar/SymCC/Extractor.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Extractor.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Extractor.json)
