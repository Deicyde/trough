---
catalog: module
lean: Cedar.SymCC.verifyEvaluateOpt, Cedar.SymCC.verifyEvaluatePairOpt, Cedar.SymCC.verifyIsAuthorizedOpt, Cedar.SymCC.verifyNeverErrorsOpt, Cedar.SymCC.verifyAlwaysMatchesOpt, Cedar.SymCC.verifyNeverMatchesOpt, Cedar.SymCC.verifyMatchesEquivalentOpt, Cedar.SymCC.verifyMatchesImpliesOpt, Cedar.SymCC.verifyMatchesDisjointOpt, Cedar.SymCC.verifyImpliesOpt, Cedar.SymCC.verifyAlwaysAllowsOpt, Cedar.SymCC.verifyAlwaysDeniesOpt, Cedar.SymCC.verifyEquivalentOpt, Cedar.SymCC.verifyDisjointOpt
statement: formalized
proof: formalized
---

# SymCCOpt/Verifier

`Cedar.SymCCOpt.Verifier`, in [Cedar/SymCCOpt/Verifier.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean).

> This file contains versions of the functions in `SymCC/Verifier.lean` that
> operate on compiled policies (from `SymCCOpt/CompiledPolicies.lean`).
> Unlike the unoptimized functions in `SymCC/Verifier.lean`, the functions in this
> file do not need to call the symbolic compiler.

`Cedar.SymCC.verifyEvaluateOpt` (definition, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L44))

> Returns asserts that are unsatisfiable iff the evaluation of `p`, represented
> as a `Term` of type .option .bool, satisfies `φ` on all inputs drawn from the
> `εnv` that `p` was compiled for.
>
> See also `verifyNeverErrorsOpt`.

```lean
def verifyEvaluateOpt (φ : Term → Term) (p : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyEvaluatePairOpt` (definition, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L64))

> Returns asserts that are unsatisfiable iff the evaluation of `p₁` and `p₂`,
> represented as `Term`s of type .option .bool, satisfy `φ` on all inputs drawn
> from the `εnv` that the policies were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
>
> See also `verifyMatchesImpliesOpt`, `verifyMatchesEquivalentOpt`, and
> `verifyMatchesDisjointOpt`.

```lean
def verifyEvaluatePairOpt (φ : Term → Term → Term) (p₁ p₂ : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyIsAuthorizedOpt` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L85))

> Returns asserts that are unsatisfiable iff the authorization decisions produced
> by `ps₁` and `ps₂`, represented as `Term`s of type .bool, satisfy `φ` on all
> inputs drawn from the `εnv` that the policysets were compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
>
> See also `verifyAlwaysAllowsOpt`, `verifyAlwaysDeniesOpt`, `verifyImpliesOpt`,
> `verifyEquivalentOpt`, and `verifyDisjointOpt`.

```lean
def verifyIsAuthorizedOpt (φ : Term → Term → Term) (ps₁ ps₂ : CompiledPolicySet) : Asserts
```

`Cedar.SymCC.verifyNeverErrorsOpt` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L102))

> Returns asserts that are unsatisfiable iff `p` does not error on any input in
> the `εnv` it was compiled for. If the asserts are satisfiable, then there is
> some input in `εnv` on which `p` errors.

```lean
def verifyNeverErrorsOpt (p : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyAlwaysMatchesOpt` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L110))

> Returns asserts that are unsatisfiable iff `p` matches all inputs in the `εnv`
> it was compiled for.  If the asserts are satisfiable, then there is some input
> in `εnv` which `p` doesn't match.

```lean
def verifyAlwaysMatchesOpt (p : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyNeverMatchesOpt` (definition, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L118))

> Returns asserts that are unsatisfiable iff `p` matches no inputs in `εnv`.
> If the asserts are satisfiable, then there is some input in `εnv` which `p`
> does match.

```lean
def verifyNeverMatchesOpt (p : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyMatchesEquivalentOpt` (definition, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L128))

> Returns asserts that are unsatisfiable iff `p₁` and `p₂` match exactly the same
> set of inputs in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> If the asserts are satisfiable, then there is some input in `εnv` on which `p₁`
> and `p₂` have different matching behavior.

```lean
def verifyMatchesEquivalentOpt (p₁ p₂ : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyMatchesImpliesOpt` (definition, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L142))

> Returns asserts that are unsatisfiable iff `p₁` matching implies that `p₂`
> matches, for every input in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> If the asserts are satisfiable, then there is some input in `εnv` that is
> matched by `p₁` but not matched by `p₂`.

```lean
def verifyMatchesImpliesOpt (p₁ p₂ : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyMatchesDisjointOpt` (definition, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L156))

> Returns asserts that are unsatisfiable iff there is no input in the `εnv` they
> were compiled for that is matched by both `p₁` and `p₂`.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> If the asserts are satisfiable, then there is some input in `εnv` that is
> matched by both `p₁` and `p₂`.

```lean
def verifyMatchesDisjointOpt (p₁ p₂ : CompiledPolicy) : Asserts
```

`Cedar.SymCC.verifyImpliesOpt` (definition, [line 172](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L172))

> Returns asserts that are unsatisfiable iff the authorization decision of `ps₁`
> implies that of `ps₂` for every input in the `εnv` that the policysets were
> compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> In other words, every input allowed by `ps₁` is allowed by `ps₂`.

```lean
def verifyImpliesOpt (ps₁ ps₂ : CompiledPolicySet) : Asserts
```

`Cedar.SymCC.verifyAlwaysAllowsOpt` (definition, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L179))

> Returns asserts that are unsatisfiable iff `ps` allows all inputs in the `εnv`
> it was compiled for.

```lean
def verifyAlwaysAllowsOpt (ps : CompiledPolicySet) : Asserts
```

`Cedar.SymCC.verifyAlwaysDeniesOpt` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L186))

> Returns asserts that are unsatisfiable iff `ps` denies all inputs in the `εnv`
> it was compiled for.

```lean
def verifyAlwaysDeniesOpt (ps : CompiledPolicySet) : Asserts
```

`Cedar.SymCC.verifyEquivalentOpt` (definition, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L195))

> Returns asserts that are unsatisfiable iff `ps₁` and `ps₂` produce the same
> authorization decision on all inputs in the `εnv` that the policysets were
> compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)

```lean
def verifyEquivalentOpt (ps₁ ps₂ : CompiledPolicySet) : Asserts
```

`Cedar.SymCC.verifyDisjointOpt` (definition, [line 206](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean#L206))

> Returns asserts that are unsatisfiable iff there is no input in the `εnv` that
> is allowed by both `ps₁` and `ps₂`.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> This checks that the authorization semantics of `ps₁` and `ps₂` are disjoint.
> If this query is satisfiable, then there is at least one input in this `εnv` that
> is allowed by both `ps₁` and `ps₂`.

```lean
def verifyDisjointOpt (ps₁ ps₂ : CompiledPolicySet) : Asserts
```

## Depends on

- [SymCCOpt/Enforcer](enforcer.md)

## Sources

- [Cedar/SymCCOpt/Verifier.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Verifier.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.Verifier.json)
