---
catalog: module
lean: Cedar.SymCC.SymEnv.ofTypeEnv, Cedar.SymCC.wellTypedPolicy, Cedar.SymCC.wellTypedPolicies, Cedar.SymCC.neverErrors?, Cedar.SymCC.alwaysMatches?, Cedar.SymCC.neverMatches?, Cedar.SymCC.matchesEquivalent?, Cedar.SymCC.matchesImplies?, Cedar.SymCC.matchesDisjoint?, Cedar.SymCC.implies?, Cedar.SymCC.alwaysAllows?, Cedar.SymCC.alwaysDenies?, Cedar.SymCC.equivalent?, Cedar.SymCC.disjoint?, Cedar.SymCC.checkNeverErrors, Cedar.SymCC.checkAlwaysMatches, Cedar.SymCC.checkNeverMatches, Cedar.SymCC.checkMatchesEquivalent, Cedar.SymCC.checkMatchesImplies, Cedar.SymCC.checkMatchesDisjoint, Cedar.SymCC.checkImplies, Cedar.SymCC.checkAlwaysAllows, Cedar.SymCC.checkAlwaysDenies, Cedar.SymCC.checkEquivalent, Cedar.SymCC.checkDisjoint
statement: formalized
proof: formalized
---

# SymCC

`Cedar.SymCC`, in [Cedar/SymCC.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean).

> This file contains the top-level interface to SymCC.

`Cedar.SymCC.SymEnv.ofTypeEnv` (abbreviation, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L42))

> Given a type environment `Γ`, returns a symbolic environment `εnv` that
> represents all concrete inputs (requests and entities) `env ∈ εnv` that conform
> to `Γ` according to `Cedar.Validation.requestMatchesEnvironment` and
> `Cedar.Validation.entitiesMatchEnvironment`.

```lean
abbrev SymEnv.ofTypeEnv
```

`Cedar.SymCC.wellTypedPolicy` (definition, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L58))

> The Cedar symbolic compiler assumes that it receives well-typed policies.  This
> function enforces this requirement by calling Cedar's typechecker. Specifically,
> given a policy `p` and type environment `Γ`, this function calls the Cedar
> typechecker to obtain a policy `p'` that is semantically equivalent to `p` and
> well-typed with respect to `Γ`.
>
> All functions defined in this file that accept policies as input _must_ be
> called on the _output_ of this function (or `wellTypedPolicies`) to ensure that
> symbolic compilation succeeds. Applying the symbolic compiler directly to a
> policy `p` may result in type errors---that is, the compiler rejecting the
> policy because it does not satisfy the `WellTyped` constraints that are assumed
> by the compiler, and enforced by the typechecker through policy transformation.

```lean
def wellTypedPolicy (p : Policy) (Γ : Cedar.Validation.TypeEnv) : Except Validation.ValidationError Policy
```

`Cedar.SymCC.wellTypedPolicies` (definition, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L83))

> The Cedar symbolic compiler assumes that it receives well-typed policies.  This
> function enforces this requirement by calling Cedar's typechecker. Specifically,
> given policies `ps` and a type environment `Γ`, this function calls the Cedar
> typechecker on each `p ∈ ps` to obtain a policy `p'` that is semantically
> equivalent to `p` and well-typed with respect to `Γ`.
>
> All functions defined in this file that accept policies as input _must_ be
> called on the _output_ of this function (or `wellTypedPolicy`) to ensure that
> symbolic compilation succeeds. Applying the symbolic compiler directly to
> policies `ps` may result in type errors---that is, the compiler rejecting the
> policies because they don't satisfy the `WellTyped` constraints that are assumed
> by the compiler, and enforced by the typechecker through policy transformation.

```lean
def wellTypedPolicies (ps : Policies) (Γ : Cedar.Validation.TypeEnv) : Except Validation.ValidationError Policies
```

`Cedar.SymCC.neverErrors?` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L92))

> Returns `none` iff `p` does not error on any well-formed input in `εnv`.
> Otherwise returns an input `some env` on which `p` errors.

```lean
def neverErrors? (p : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysMatches?` (definition, [line 109](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L109))

> Returns `none` iff `p` matches all well-formed inputs in `εnv`. That is,
> if `p` is a `permit` policy, it allows all inputs in `εnv`, or if `p` is a
> `forbid` policy, it denies all inputs in `εnv`.
> Otherwise returns an input `some env` that is not-matched by `p`.
>
> Compare with `alwaysAllows?`, which takes a policyset (which could consist of a
> single policy, or more) and determines whether it _allows_ all well-formed
> inputs in an `εnv`. This function differs from `alwaysAllows` on a singleton
> policyset in how it treats `forbid` policies -- while `alwaysAllows` trivially
> doesn't hold for any policyset containing only `forbid` policies,
> `alwaysMatches` does hold if the `forbid` policy explicitly denies all inputs in
> the `εnv`.

```lean
def alwaysMatches? (p : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.neverMatches?` (definition, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L123))

> Returns `none` iff `p` matches no well-formed inputs in `εnv`.
> Otherwise returns an input `some env` that is matched by `p`.
>
> Compare with `alwaysDenies?`, which takes a policyset (which could consist of a
> single policy, or more) and determines whether it _denies_ all well-formed
> inputs in an `εnv`. This function differs from `alwaysDenies` on a singleton
> policyset in how it treats `forbid` policies -- while `alwaysDenies` trivially
> holds for any policyset containing only `forbid` policies, `neverMatches` only
> holds if the `forbid` policy explicitly denies no inputs in the `εnv`.

```lean
def neverMatches? (p : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.matchesEquivalent?` (definition, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L140))

> Returns `none` iff `p₁` and `p₂` match exactly the same set of well-formed
> inputs in `εnv`.  Otherwise returns an input `some env` on which `p₁` and `p₂`
> have different matching behavior (one matches and the other does not).
>
> Compare with `equivalent?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets is equivalent for well-formed inputs in `εnv`. This function
> differs from `equivalent?` on singleton policysets in how it treats `forbid`
> policies -- while `equivalent?` trivially holds for any pair of `forbid` policies
> (as they both always-deny), `matchesEquivalent?` only holds if the two policies
> match exactly the same set of inputs. Also, a nontrivial `permit` and nontrivial
> `forbid` policy can be `matchesEquivalent?`, but can never be `equivalent?`.

```lean
def matchesEquivalent? (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.matchesImplies?` (definition, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L158))

> Returns `none` iff `p₁` matching implies that `p₂` matches, for every
> well-formed input in `εnv`. That is, for every request where `p₁` matches, `p₂`
> also matches. Otherwise returns an input `some env` that is matched by `p₁` but
> not-matched by `p₂`.
>
> Compare with `implies?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization decision_ of
> the first implies that of the second. This function differs from `implies?` on
> singleton policysets in how it treats `forbid` policies -- while for `implies?`,
> any `forbid` policy trivially implies any `permit` policy (as always-deny always
> implies any policy), for `matchesImplies?`, a `forbid` policy may or may not
> imply a `permit` policy, and a `permit` policy may or may not imply a `forbid`
> policy.

```lean
def matchesImplies? (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.matchesDisjoint?` (definition, [line 175](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L175))

> Returns `none` iff there is no well-formed input in `εnv` that is matched by
> both `p₁` and `p₂`. Otherwise returns an input `some env` that is matched by
> both `p₁` and `p₂`. This checks that the sets of inputs matched by `p₁` and `p₂`
> are disjoint.
>
> Compare with `disjoint?`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets are disjoint. This function differs from `disjoint?` on
> singleton policysets in how it treats `forbid` policies -- while for
> `disjoint?`, any `forbid` policy is trivially disjoint from any other policy (as
> it allows nothing), `matchesDisjoint?` considers whether the `forbid` policy may
> _match_ (rather than _allow_) any input that is matched by the other policy.

```lean
def matchesDisjoint? (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.implies?` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L184))

> Returns `none` iff the authorization decision of `ps₁` implies that of `ps₂` for
> every well-formed input in `εnv`. That is, every input allowed by `ps₁` is
> allowed by `ps₂`; `ps₂` is either more permissive than, or equivalent to, `ps₁`.
> Otherwise returns an input `some env` that is allowed by `ps₁` but denied by `ps₂`.

```lean
def implies? (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysAllows?` (definition, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L191))

> Returns `none` iff `ps` allows all well-formed inputs in `εnv`. Otherwise
> returns an input `some env` that is denied by `ps`.

```lean
def alwaysAllows? (ps : Policies) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.alwaysDenies?` (definition, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L198))

> Returns `none` iff `ps` denies all well-formed inputs in `εnv`. Otherwise
> returns an input `some env` that is allowed by `ps`.

```lean
def alwaysDenies? (ps : Policies) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.equivalent?` (definition, [line 206](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L206))

> Returns `none` iff `ps₁` and `ps₂` produce the same authorization decision on
> all well-formed inputs in `εnv`. Otherwise returns an input `some env` on which
> `ps₁` and `ps₂` produce different authorization decisions.

```lean
def equivalent? (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.disjoint?` (definition, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L215))

> Returns `none` iff there is no well-formed input in `εnv` that is allowed by
> both `ps₁` and `ps₂`.  Otherwise returns an input `some env` that is allowed by
> both `ps₁` and `ps₂`. This checks that the authorization semantics of `ps₁` and
> `ps₂` are disjoint.

```lean
def disjoint? (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM (Option Env)
```

`Cedar.SymCC.checkNeverErrors` (definition, [line 223](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L223))

> Returns true iff `p` does not error on any well-formed input in `εnv`.

```lean
def checkNeverErrors (p : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysMatches` (definition, [line 239](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L239))

> Returns true iff `p` matches all well-formed inputs in `εnv`. That is,
> if `p` is a `permit` policy, it allows all inputs in `εnv`, or if `p` is a
> `forbid` policy, it denies all inputs in `εnv`.
>
> Compare with `checkAlwaysAllows`, which takes a policyset (which could consist of a
> single policy, or more) and determines whether it _allows_ all well-formed
> inputs in an `εnv`. This function differs from `checkAlwaysAllows` on a
> singleton policyset in how it treats `forbid` policies -- while
> `checkAlwaysAllows` trivially doesn't hold for any policyset containing only
> `forbid` policies, `checkAlwaysMatches` does hold if the `forbid` policy
> explicitly denies all inputs in the `εnv`.

```lean
def checkAlwaysMatches (p : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkNeverMatches` (definition, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L253))

> Returns true iff `p` matches no well-formed inputs in `εnv`.
>
> Compare with `checkAlwaysDenies`, which takes a policyset (which could consist
> of a single policy, or more) and determines whether it _denies_ all well-formed
> inputs in an `εnv`. This function differs from `checkAlwaysDenies` on a
> singleton policyset in how it treats `forbid` policies -- while
> `checkAlwaysDenies` trivially holds for any policyset containing only `forbid`
> policies, `checkNeverMatches` only holds if the `forbid` policy explicitly
> denies no inputs in the `εnv`.

```lean
def checkNeverMatches (p : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkMatchesEquivalent` (definition, [line 269](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L269))

> Returns true iff `p₁` and `p₂` match exactly the same set of well-formed
> inputs in `εnv`.
>
> Compare with `checkEquivalent`, which takes two policysets (which could consist of a
> single policy, or more) and determines whether the _authorization behavior_ of
> those policysets is equivalent for well-formed inputs in `εnv`. This function
> differs from `checkEquivalent` on a singleton policyset in how it treats `forbid`
> policies -- while `checkEquivalent` trivially holds for any pair of `forbid` policies
> (as they both always-deny), `checkMatchesEquivalent` only holds if the two policies
> match exactly the same set of inputs. Also, a nontrivial `permit` and nontrivial
> `forbid` policy can be `checkMatchesEquivalent`, but can never be `checkEquivalent`.

```lean
def checkMatchesEquivalent (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkMatchesImplies` (definition, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L286))

> Returns true iff `p₁` matching implies that `p₂` matches, for every
> well-formed input in `εnv`. That is, for every request where `p₁` matches, `p₂`
> also matches.
>
> Compare with `checkImplies`, which takes two policysets (which could consist of
> a single policy, or more) and determines whether the _authorization decision_ of
> the first implies that of the second. This function differs from `checkImplies`
> on singleton policysets in how it treats `forbid` policies -- while for
> `checkImplies`, any `forbid` policy trivially implies any `permit` policy (as
> always-deny always implies any policy), for `checkMatchesImplies`, a `forbid`
> policy may or may not imply a `permit` policy, and a `permit` policy may or may
> not imply a `forbid` policy.

```lean
def checkMatchesImplies (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkMatchesDisjoint` (definition, [line 303](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L303))

> Returns true iff there is no well-formed input in `εnv` that is matched by
> both `p₁` and `p₂`. This checks that the sets of inputs matched by `p₁` and `p₂`
> are disjoint.
>
> Compare with `checkDisjoint`, which takes two policysets (which could consist of
> a single policy, or more) and determines whether the _authorization behavior_ of
> those policysets are disjoint. This function differs from `checkDisjoint` on
> singleton policysets in how it treats `forbid` policies -- while for
> `checkDisjoint`, any `forbid` policy is trivially disjoint from any other policy
> (as it allows nothing), `checkMatchesDisjoint` considers whether the `forbid`
> policy may _match_ (rather than _allow_) any input that is matched by the other
> policy.

```lean
def checkMatchesDisjoint (p₁ p₂ : Policy) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkImplies` (definition, [line 311](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L311))

> Returns true iff the authorization decision of `ps₁` implies that of `ps₂` for
> every well-formed input in `εnv`. That is, every input allowed by `ps₁` is
> allowed by `ps₂`; `ps₂` is either more permissive than, or equivalent to, `ps₁`.

```lean
def checkImplies (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysAllows` (definition, [line 317](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L317))

> Returns true iff `ps` allows all well-formed inputs in `εnv`.

```lean
def checkAlwaysAllows (ps : Policies) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkAlwaysDenies` (definition, [line 323](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L323))

> Returns true iff `ps` denies all well-formed inputs in `εnv`.

```lean
def checkAlwaysDenies (ps : Policies) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkEquivalent` (definition, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L330))

> Returns true iff `ps₁` and `ps₂` produce the same authorization decision on all
> well-formed inputs in `εnv`.

```lean
def checkEquivalent (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM Bool
```

`Cedar.SymCC.checkDisjoint` (definition, [line 339](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean#L339))

> Returns true iff there is no well-formed input in `εnv` that is allowed by both
> `ps₁` and `ps₂`.  This checks that the authorization semantics of `ps₁` and
> `ps₂` are disjoint. If this query is satisfiable, then there is at least one
> well-formed input that is allowed by both `ps₁` and `ps₂`.

```lean
def checkDisjoint (ps₁ ps₂ : Policies) (εnv : SymEnv) : SolverM Bool
```

## Depends on

- [SymCC/SatUnsat](symcc/part-01/satunsat.md)
- [Cedar/Validation/Validator](validation/validator.md)

## Sources

- [Cedar/SymCC.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC.lean)
- [Declaration ledger](../../sources/cedar/Cedar.SymCC.json)
