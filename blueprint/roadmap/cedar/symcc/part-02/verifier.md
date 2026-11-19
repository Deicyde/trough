---
catalog: module
lean: Cedar.SymCC.Asserts, Cedar.SymCC.verifyEvaluate, Cedar.SymCC.verifyEvaluatePair, Cedar.SymCC.verifyIsAuthorized, Cedar.SymCC.verifyNeverErrors, Cedar.SymCC.verifyAlwaysMatches, Cedar.SymCC.verifyNeverMatches, Cedar.SymCC.verifyMatchesEquivalent, Cedar.SymCC.verifyMatchesImplies, Cedar.SymCC.verifyMatchesDisjoint, Cedar.SymCC.verifyImplies, Cedar.SymCC.verifyAlwaysAllows, Cedar.SymCC.verifyAlwaysDenies, Cedar.SymCC.verifyEquivalent, Cedar.SymCC.verifyDisjoint
statement: formalized
proof: formalized
---

# SymCC/Verifier

`Cedar.SymCC.Verifier`, in [Cedar/SymCC/Verifier.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean).

> This file contains `verify*` functions that use the Cedar symbolic compiler,
> authorizer, and hierarchy enforcer to generate a list of `Asserts`. These are
> boolean terms whose conjunction is unsatisfiable if and only if the verified
> property holds.

`Cedar.SymCC.Asserts` (abbreviation, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L36))

```lean
abbrev Asserts
```

`Cedar.SymCC.verifyEvaluate` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L43))

> Returns asserts that are unsatisfiable iff the evaluation of `p`, represented as
> a Term of type .option .bool, satisfies `φ` on all inputs drawn from `εnv`.  See also
> `verifyNeverErrors`, `verifyAlwaysMatches`, and `verifyNeverMatches`.

```lean
def verifyEvaluate (φ : Term → Term) (p : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyEvaluatePair` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L54))

> Returns asserts that are unsatisfiable iff the evaluation of `p₁` and `p₂`,
> represented as Terms of type .option .bool, satisfy `φ` on all inputs drawn from
> `εnv`. See also `verifyMatchesImplies`, `verifyMatchesEquivalent`, and
> `verifyMatchesDisjoint`.

```lean
def verifyEvaluatePair (φ : Term → Term → Term) (p₁ p₂ : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyIsAuthorized` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L67))

> Returns asserts that are unsatisfiable iff the authorization decisions produced
> by `ps₁` and `ps₂`, represented as Terms of type .bool, satisfy `φ` on all
> inputs drawn from `εnv`. See also `verifyAlwaysAllows`, `verifyAlwaysDenies`,
> `verifyImplies`, `verifyEquivalent`, and `verifyDisjoint`.

```lean
def verifyIsAuthorized (φ : Term → Term → Term) (ps₁ ps₂ : Policies) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyNeverErrors` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L78))

> Returns asserts that are unsatisfiable iff `p` does not error on any input in
> `εnv`. If the asserts are satisfiable, then there is some input in `εnv` on
> which `p` errors.

```lean
def verifyNeverErrors (p : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyAlwaysMatches` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L86))

> Returns asserts that are unsatisfiable iff `p` matches all inputs in `εnv`.
> If the asserts are satisfiable, then there is some input in `εnv` which `p`
> doesn't match.

```lean
def verifyAlwaysMatches (p : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyNeverMatches` (definition, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L95))

> Returns asserts that are unsatisfiable iff `p` matches no inputs in `εnv`.
> If the asserts are satisfiable, then there is some input in `εnv` which `p`
> does match.

```lean
def verifyNeverMatches (p : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyMatchesEquivalent` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L103))

> Returns asserts that are unsatisfiable iff `p₁` and `p₂` match exactly the same
> set of inputs in `εnv`.

```lean
def verifyMatchesEquivalent (p₁ p₂ : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyMatchesImplies` (definition, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L115))

> Returns asserts that are unsatisfiable iff `p₁` matching implies that `p₂`
> matches, for every input in `εnv`. In other words, for every request where `p₁`
> matches, `p₂` also matches.

```lean
def verifyMatchesImplies (p₁ p₂ : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyMatchesDisjoint` (definition, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L128))

> Returns asserts that are unsatisfiable iff there is no input in `εnv` that is
> matched by both `p₁` and `p₂`. In other words, the sets of inputs matched by
> `p₁` and `p₂` are disjoint. If this query is satisfiable, then there is at
> least one input that is matched by both `p₁` and `p₂`.

```lean
def verifyMatchesDisjoint (p₁ p₂ : Policy) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyImplies` (definition, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L142))

> Returns asserts that are unsatisfiable iff the authorization decision of `ps₁`
> implies that of `ps₂` for every input in `εnv`. In other words, every input
> allowed by `ps₁` is allowed by `ps₂`.

```lean
def verifyImplies (ps₁ ps₂ : Policies) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyAlwaysAllows` (definition, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L148))

> Returns asserts that are unsatisfiable iff `ps` allows all inputs in `εnv`.

```lean
def verifyAlwaysAllows (ps : Policies) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyAlwaysDenies` (definition, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L174))

> Returns asserts that are unsatisfiable iff `ps` denies all inputs in `εnv`.

```lean
def verifyAlwaysDenies (ps : Policies) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyEquivalent` (definition, [line 181](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L181))

> Returns asserts that are unsatisfiable iff `ps₁` and `ps₂` produce the same
> authorization decision on all inputs in `εnv`.

```lean
def verifyEquivalent (ps₁ ps₂ : Policies) (εnv : SymEnv) : Result Asserts
```

`Cedar.SymCC.verifyDisjoint` (definition, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean#L190))

> Returns asserts that are unsatisfiable iff there is no input in `εnv` that is
> allowed by both `ps₁` and `ps₂`.  This checks that the authorization semantics
> of `ps₁` and `ps₂` are disjoint. If this query is satisfiable, then there is at
> least one input that is allowed by both `ps₁` and `ps₂`.

```lean
def verifyDisjoint (ps₁ ps₂ : Policies) (εnv : SymEnv) : Result Asserts
```

## Depends on

- [Cedar/SymCC/Authorizer](../part-01/authorizer.md)
- [Cedar/SymCC/Enforcer](../part-01/enforcer.md)

## Sources

- [Cedar/SymCC/Verifier.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Verifier.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Verifier.json)
