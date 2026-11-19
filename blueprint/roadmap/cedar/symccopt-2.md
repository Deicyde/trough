---
catalog: module
lean: Cedar.SymCC.neverErrorsOpt?, Cedar.SymCC.alwaysMatchesOpt?, Cedar.SymCC.neverMatchesOpt?, Cedar.SymCC.matchesEquivalentOpt?, Cedar.SymCC.matchesImpliesOpt?, Cedar.SymCC.matchesDisjointOpt?, Cedar.SymCC.impliesOpt?, Cedar.SymCC.alwaysAllowsOpt?, Cedar.SymCC.alwaysDeniesOpt?, Cedar.SymCC.equivalentOpt?, Cedar.SymCC.disjointOpt?, Cedar.SymCC.checkNeverErrorsOpt, Cedar.SymCC.checkAlwaysMatchesOpt, Cedar.SymCC.checkNeverMatchesOpt, Cedar.SymCC.checkMatchesEquivalentOpt, Cedar.SymCC.checkMatchesImpliesOpt, Cedar.SymCC.checkMatchesDisjointOpt, Cedar.SymCC.checkImpliesOpt, Cedar.SymCC.checkAlwaysAllowsOpt, Cedar.SymCC.checkAlwaysDeniesOpt, Cedar.SymCC.checkEquivalentOpt, Cedar.SymCC.checkDisjointOpt
statement: formalized
proof: formalized
---

# SymCCOpt

`Cedar.SymCCOpt`, in [Cedar/SymCCOpt.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean).

> This file contains the top-level interface to optimized SymCC.

`Cedar.SymCC.neverErrorsOpt?` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L42))

> Returns `none` iff `p` does not error on any well-formed input in the `εnv` it
> was compiled for.
> Otherwise returns an input `some env` on which `p` errors.

```lean
def neverErrorsOpt? (p : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysMatchesOpt?` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L59))

> Returns `none` iff `p` matches all well-formed inputs in `εnv`. That is,
> if `p` is a `permit` policy, it allows all inputs in `εnv`, or if `p` is a
> `forbid` policy, it denies all inputs in `εnv`.
> Otherwise returns an input `some env` that is not-matched by `p`.
>
> Compare with `alwaysAllowsOpt?`, which takes a policyset (which could consist of a
> single policy, or more) and determines whether it _allows_ all well-formed
> inputs in an `εnv`. This function differs from `alwaysAllowsOpt` on a singleton
> policyset in how it treats `forbid` policies -- while `alwaysAllowsOpt` trivially
> doesn't hold for any policyset containing only `forbid` policies,
> `alwaysMatchesOpt` does hold if the `forbid` policy explicitly denies all inputs in
> the `εnv`.

```lean
def alwaysMatchesOpt? (p : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.neverMatchesOpt?` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L73))

> Returns `none` iff `p` matches no well-formed inputs in `εnv`.
> Otherwise returns an input `some env` that is matched by `p`.
>
> Compare with `alwaysDeniesOpt`, which takes a policyset (which could consist of a
> single policy, or more) and determines whether it _denies_ all well-formed
> inputs in an `εnv`. This function differs from `alwaysDeniesOpt` on a singleton
> policyset in how it treats `forbid` policies -- while `alwaysDeniesOpt` trivially
> holds for any policyset containing only `forbid` policies, `neverMatchesOpt` only
> holds if the `forbid` policy explicitly denies no inputs in the `εnv`.

```lean
def neverMatchesOpt? (p : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.matchesEquivalentOpt?` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L92))

> Returns `none` iff `p₁` and `p₂` match exactly the same set of well-formed
> inputs in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> Otherwise returns an input `some env` on which `p₁` and `p₂`
> have different matching behavior (one matches and the other does not).
>
> Compare with `equivalentOpt?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets is equivalent for well-formed inputs in `εnv`. This function
> differs from `equivalentOpt?` on singleton policysets in how it treats `forbid`
> policies -- while `equivalentOpt?` trivially holds for any pair of `forbid` policies
> (as they both always-deny), `matchesEquivalentOpt?` only holds if the two policies
> match exactly the same set of inputs. Also, a nontrivial `permit` and nontrivial
> `forbid` policy can be `matchesEquivalentOpt?`, but can never be `equivalentOpt?`.

```lean
def matchesEquivalentOpt? (p₁ p₂ : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.matchesImpliesOpt?` (definition, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L112))

> Returns `none` iff `p₁` matching implies that `p₂` matches, for every
> well-formed input in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> That is, for every request where `p₁` matches, `p₂` also matches.
> Otherwise returns an input `some env` that is matched by `p₁` but
> not-matched by `p₂`.
>
> Compare with `impliesOpt?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization decision_ of
> the first implies that of the second. This function differs from `impliesOpt?` on
> singleton policysets in how it treats `forbid` policies -- while for `impliesOpt?`,
> any `forbid` policy trivially implies any `permit` policy (as always-deny always
> implies any policy), for `matchesImpliesOpt?`, a `forbid` policy may or may not
> imply a `permit` policy, and a `permit` policy may or may not imply a `forbid`
> policy.

```lean
def matchesImpliesOpt? (p₁ p₂ : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.matchesDisjointOpt?` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L130))

> Returns `none` iff there is no well-formed input in the `εnv` they were compiled
> for that is matched by both `p₁` and `p₂`.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> Otherwise returns an input `some env` that is matched by both `p₁` and `p₂`.
> This checks that the sets of inputs matched by `p₁` and `p₂` are disjoint.
>
> Compare with `disjointOpt?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets are disjoint. This function differs from `disjointOpt?` on
> singleton policysets in how it treats `forbid` policies -- while for
> `disjointOpt?`, any `forbid` policy is trivially disjoint from any other policy (as
> it allows nothing), `matchesDisjointOpt?` considers whether the `forbid` policy may
> _match_ (rather than _allow_) any input that is matched by the other policy.

```lean
def matchesDisjointOpt? (p₁ p₂ : CompiledPolicy) : SolverM (Option Env)
```

`Cedar.SymCC.impliesOpt?` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L141))

> Returns `none` iff the authorization decision of `ps₁` implies that of `ps₂` for
> every well-formed input in the `εnv` that the policysets were compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> That is, every input allowed by `ps₁` is allowed by `ps₂`; `ps₂` is either more
> permissive than, or equivalent to, `ps₁`.
> Otherwise returns an input `some env` that is allowed by `ps₁` but denied by `ps₂`.

```lean
def impliesOpt? (ps₁ ps₂ : CompiledPolicySet) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysAllowsOpt?` (definition, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L149))

> Returns `none` iff `ps` allows all well-formed inputs in the `εnv` it was
> compiled for.
> Otherwise returns an input `some env` that is denied by `ps`.

```lean
def alwaysAllowsOpt? (ps : CompiledPolicySet) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysDeniesOpt?` (definition, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L157))

> Returns `none` iff `ps` denies all well-formed inputs in the `εnv` it was
> compiled for.
> Otherwise returns an input `some env` that is allowed by `ps`.

```lean
def alwaysDeniesOpt? (ps : CompiledPolicySet) : SolverM (Option Env)
```

`Cedar.SymCC.equivalentOpt?` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L167))

> Returns `none` iff `ps₁` and `ps₂` produce the same authorization decision on
> all well-formed inputs in the `εnv` that the policysets were compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> Otherwise returns an input `some env` on which `ps₁` and `ps₂` produce different
> authorization decisions.

```lean
def equivalentOpt? (ps₁ ps₂ : CompiledPolicySet) : SolverM (Option Env)
```

`Cedar.SymCC.disjointOpt?` (definition, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L177))

> Returns `none` iff there is no well-formed input in `εnv` that the policysets were
> compiled for, that is allowed by both `ps₁` and `ps₂`.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> Otherwise returns an input `some env` that is allowed by both `ps₁` and `ps₂`.
> This checks that the authorization semantics of `ps₁` and `ps₂` are disjoint.

```lean
def disjointOpt? (ps₁ ps₂ : CompiledPolicySet) : SolverM (Option Env)
```

`Cedar.SymCC.checkNeverErrorsOpt` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L186))

> Returns true iff `p` does not error on any well-formed input in the `εnv` it was
> compiled for.

```lean
def checkNeverErrorsOpt (p : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysMatchesOpt` (definition, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L203))

> Returns `none` iff `p` matches all well-formed inputs in `εnv`. That is,
> if `p` is a `permit` policy, it allows all inputs in `εnv`, or if `p` is a
> `forbid` policy, it denies all inputs in `εnv`.
> Otherwise returns an input `some env` that is not-matched by `p`.
>
> Compare with `checkAlwaysAllowsOpt`, which takes a policyset (which could
> consist of a single policy, or more) and determines whether it _allows_ all
> well-formed inputs in an `εnv`. This function differs from
> `checkAlwaysAllowsOpt` on a singleton policyset in how it treats `forbid`
> policies -- while `checkAlwaysAllowsOpt` trivially doesn't hold for any
> policyset containing only `forbid` policies, `checkAlwaysMatchesOpt` does hold
> if the `forbid` policy explicitly denies all inputs in the `εnv`.

```lean
def checkAlwaysMatchesOpt (p : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkNeverMatchesOpt` (definition, [line 218](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L218))

> Returns `none` iff `p` matches no well-formed inputs in `εnv`.
> Otherwise returns an input `some env` that is matched by `p`.
>
> Compare with `checkAlwaysDeniesOpt`, which takes a policyset (which could
> consist of a single policy, or more) and determines whether it _denies_ all
> well-formed inputs in an `εnv`. This function differs from
> `checkAlwaysDeniesOpt` on a singleton policyset in how it treats `forbid`
> policies -- while `checkAlwaysDeniesOpt` trivially holds for any policyset
> containing only `forbid` policies, `checkNeverMatchesOpt` only holds if the
> `forbid` policy explicitly denies no inputs in the `εnv`.

```lean
def checkNeverMatchesOpt (p : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkMatchesEquivalentOpt` (definition, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L235))

> Returns true iff `p₁` and `p₂` match exactly the same set of well-formed
> inputs in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
>
> Compare with `checkEquivalentOpt`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets is equivalent for well-formed inputs in `εnv`. This function
> differs from `checkEquivalentOpt` on singleton policysets in how it treats `forbid`
> policies -- while `checkEquivalentOpt` trivially holds for any pair of `forbid` policies
> (as they both always-deny), `checkMatchesEquivalentOpt` only holds if the two policies
> match exactly the same set of inputs. Also, a nontrivial `permit` and nontrivial
> `forbid` policy can be `checkMatchesEquivalentOpt`, but can never be `checkEquivalentOpt`.

```lean
def checkMatchesEquivalentOpt (p₁ p₂ : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkMatchesImpliesOpt` (definition, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L253))

> Returns true iff `p₁` matching implies that `p₂` matches, for every
> well-formed input in the `εnv` they were compiled for.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> That is, for every request where `p₁` matches, `p₂` also matches.
>
> Compare with `checkImpliesOpt`, which takes two policysets (which could consist of
> a single policy, or more) and determines whether the _authorization decision_ of
> the first implies that of the second. This function differs from `checkImpliesOpt`
> on singleton policysets in how it treats `forbid` policies -- while for
> `checkImpliesOpt`, any `forbid` policy trivially implies any `permit` policy (as
> always-deny always implies any policy), for `checkMatchesImpliesOpt`, a `forbid`
> policy may or may not imply a `permit` policy, and a `permit` policy may or may
> not imply a `forbid` policy.

```lean
def checkMatchesImpliesOpt (p₁ p₂ : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkMatchesDisjointOpt` (definition, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L271))

> Returns true iff there is no well-formed input in the `εnv` they were compiled
> for that is matched by both `p₁` and `p₂`.
> (Caller guarantees that `p₁` and `p₂` were compiled for the same `εnv`.)
> This checks that the sets of inputs matched by `p₁` and `p₂` are disjoint.
>
> Compare with `checkDisjointOpt`, which takes two policysets (which could consist of
> a single policy, or more) and determines whether the _authorization behavior_ of
> those policysets are disjoint. This function differs from `checkDisjointOpt` on
> singleton policysets in how it treats `forbid` policies -- while for
> `checkDisjointOpt`, any `forbid` policy is trivially disjoint from any other policy
> (as it allows nothing), `checkMatchesDisjointOpt` considers whether the `forbid`
> policy may _match_ (rather than _allow_) any input that is matched by the other
> policy.

```lean
def checkMatchesDisjointOpt (p₁ p₂ : CompiledPolicy) : SolverM Bool
```

`Cedar.SymCC.checkImpliesOpt` (definition, [line 281](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L281))

> Returns true iff the authorization decision of `ps₁` implies that of `ps₂` for
> every well-formed input in `εnv` that the policysets were compiled for.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> That is, every input allowed by `ps₁` is allowed by `ps₂`; `ps₂` is either more
> permissive than, or equivalent to, `ps₁`.

```lean
def checkImpliesOpt (ps₁ ps₂ : CompiledPolicySet) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysAllowsOpt` (definition, [line 288](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L288))

> Returns true iff `ps` allows all well-formed inputs in the `εnv` it was compiled
> for.

```lean
def checkAlwaysAllowsOpt (ps : CompiledPolicySet) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysDeniesOpt` (definition, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L295))

> Returns true iff `ps` denies all well-formed inputs in the `εnv` it was compiled
> for.

```lean
def checkAlwaysDeniesOpt (ps : CompiledPolicySet) : SolverM Bool
```

`Cedar.SymCC.checkEquivalentOpt` (definition, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L302))

> Returns true iff `ps₁` and `ps₂` produce the same authorization decision on all
> well-formed inputs in the `εnv` that the policysets were compiled for.

```lean
def checkEquivalentOpt (ps₁ ps₂ : CompiledPolicySet) : SolverM Bool
```

`Cedar.SymCC.checkDisjointOpt` (definition, [line 313](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean#L313))

> Returns true iff there is no well-formed input in `εnv` that is allowed by both
> `ps₁` and `ps₂`.
> (Caller guarantees that `ps₁` and `ps₂` were compiled for the same `εnv`.)
> This checks that the authorization semantics of `ps₁` and `ps₂` are disjoint. If
> this query is satisfiable, then there is at least one well-formed input that is
> allowed by both `ps₁` and `ps₂`.

```lean
def checkDisjointOpt (ps₁ ps₂ : CompiledPolicySet) : SolverM Bool
```

## Depends on

- [SymCCOpt/SatUnsat](symccopt/satunsat.md)
- [SymCCOpt/Verifier](symccopt/verifier.md)

## Sources

- [Cedar/SymCCOpt.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt.lean)
- [Declaration ledger](../../sources/cedar/Cedar.SymCCOpt.json)
