---
catalog: module
lean: Cedar.Thm.compileWithEffect_error_implies, Cedar.Thm.compileWithEffect_none_implies, Cedar.Thm.compileWithEffect_some_implies, Cedar.Thm.satisfiedPolicies_filterMapM_eq, Cedar.Thm.compile_policy_wf, Cedar.Thm.satisfiedPolicies_ok_implies, Cedar.Thm.eqSomeTrue, Cedar.Thm.satisfiedPolicies_wf, Cedar.Thm.satisfiedPolicies_interpret, Cedar.Thm.satisfiedPolicies_eq, Cedar.Thm.satisfiedPolicies_bisimulation, Cedar.Thm.same_decisions_def, Cedar.Thm.same_decisions_iff_allow_true_or_deny_false, Cedar.Thm.same_responses_iff_same_decisions, Cedar.Thm.same_responses_self_decision, Cedar.Thm.same_decision_and_response_implies_same_decision, Cedar.Thm.isAuthorized_ok_implies, Cedar.Thm.isAuthorized_wf, Cedar.Thm.isAuthorized_interpret_eq_when_interpret_eq, Cedar.Thm.isAuthorized_interpret, Cedar.Thm.isAuthorized_same, Cedar.Thm.isAuthorized_bisimulation
statement: formalized
proof: formalized
---

# Thm/SymCC/Authorizer

`Cedar.Thm.SymCC.Authorizer`, in [Cedar/Thm/SymCC/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean).

> This file proves a key lemma used to show the soundness and completeness of
> analyses built on top of Cedar's symbolic authorizer.
> -

`Cedar.Thm.compileWithEffect_error_implies` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L30))

```lean
theorem compileWithEffect_error_implies {effect : Effect} {p : Policy} {εnv : SymEnv} {err : SymCC.Error }:
  compileWithEffect effect p εnv = .error err →
  p.effect = effect ∧ compile p.toExpr εnv = .error err
```

`Cedar.Thm.compileWithEffect_none_implies` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L46))

```lean
theorem compileWithEffect_none_implies {effect : Effect} {p : Policy} {εnv : SymEnv} :
  compileWithEffect effect p εnv = .ok .none →
  p.effect ≠ effect
```

`Cedar.Thm.compileWithEffect_some_implies` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L56))

```lean
theorem compileWithEffect_some_implies {effect : Effect} {p : Policy} {εnv : SymEnv} {t : Term} :
  compileWithEffect effect p εnv = Except.ok (some t) →
  p.effect = effect ∧ compile p.toExpr εnv = .ok t
```

`Cedar.Thm.satisfiedPolicies_filterMapM_eq` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L70))

```lean
theorem satisfiedPolicies_filterMapM_eq {effect : Effect} {ps : Policies} {εnv : SymEnv} :
  List.filterMapM (compileWithEffect effect · εnv) ps =
  (ps.filter (λ p => p.effect == effect)).mapM (λ p => compile p.toExpr εnv)
```

`Cedar.Thm.compile_policy_wf` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L122))

```lean
theorem compile_policy_wf {p : Policy} {εnv : SymEnv} {t : Term} :
  εnv.WellFormedFor p.toExpr →
  compile p.toExpr εnv = .ok t →
  (t.WellFormed εnv.entities ∧ t.typeOf = .option .bool)
```

`Cedar.Thm.satisfiedPolicies_ok_implies` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L131))

```lean
theorem satisfiedPolicies_ok_implies {effect : Effect} {ps : Policies} {εnv : SymEnv} {t : Term} :
  satisfiedPolicies effect ps εnv = .ok t →
  ∃ ts,
    t = anyTrue (eq · (Term.some (Term.bool true))) ts ∧
    List.mapM (λ p => compile p.toExpr εnv) (List.filter (λ p => p.effect == effect) ps) = Except.ok ts
```

`Cedar.Thm.eqSomeTrue` (abbreviation, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L155))

```lean
abbrev eqSomeTrue
```

`Cedar.Thm.satisfiedPolicies_wf` (theorem, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L167))

```lean
theorem satisfiedPolicies_wf {effect : Effect} {ps : Policies} {εnv : SymEnv} {t : Term}
  (hwε : εnv.WellFormedForPolicies ps)
  (hok : Cedar.SymCC.satisfiedPolicies effect ps εnv = .ok t) :
  t.WellFormed εnv.entities ∧ t.typeOf = .bool
```

`Cedar.Thm.satisfiedPolicies_interpret` (theorem, [line 207](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L207))

```lean
theorem satisfiedPolicies_interpret {effect : Effect} {ps : Policies} {εnv : SymEnv} {t : Term} {I : Interpretation}
  (hwε : εnv.WellFormedForPolicies ps)
  (hwI : I.WellFormed εnv.entities)
  (hok : Cedar.SymCC.satisfiedPolicies effect ps εnv = .ok t) :
  Cedar.SymCC.satisfiedPolicies effect ps (εnv.interpret I) = t.interpret I
```

`Cedar.Thm.satisfiedPolicies_eq` (theorem, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L222))

```lean
theorem satisfiedPolicies_eq {effect : Effect} {ps : Policies} {env : Env} {εnv : SymEnv} {t : Term}
  (hwε : εnv.WellFormedForPolicies ps)
  (hwe : env.WellFormedForPolicies ps)
  (heq : env ∼ εnv)
  (hok : Cedar.SymCC.satisfiedPolicies effect ps εnv = .ok t) :
  t = .bool (!(Cedar.Spec.satisfiedPolicies effect ps env.request env.entities).isEmpty)
```

`Cedar.Thm.satisfiedPolicies_bisimulation` (theorem, [line 274](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L274))

```lean
theorem satisfiedPolicies_bisimulation {effect : Effect} {ps : Policies} {env : Env} {εnv : SymEnv} {t : Term} {I : Interpretation}
  (hwε : εnv.WellFormedForPolicies ps)
  (hwe : env.WellFormedForPolicies ps)
  (hwI : I.WellFormed εnv.entities)
  (heq : env ∼ εnv.interpret I)
  (hok : Cedar.SymCC.satisfiedPolicies effect ps εnv = .ok t) :
  t.interpret I = .bool (!(Cedar.Spec.satisfiedPolicies effect ps env.request env.entities).isEmpty)
```

`Cedar.Thm.same_decisions_def` (theorem, [line 314](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L314))

```lean
theorem same_decisions_def {d : Spec.Decision} {t : Term} :
  d ∼ t ↔ SymCC.SameDecisions d t
```

`Cedar.Thm.same_decisions_iff_allow_true_or_deny_false` (theorem, [line 319](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L319))

```lean
theorem same_decisions_iff_allow_true_or_deny_false {d : Spec.Decision} {t : Term} :
  d ∼ t ↔ (d = .allow ∧ t = .bool true ∨ d = .deny ∧ t = .bool false)
```

`Cedar.Thm.same_responses_iff_same_decisions` (theorem, [line 336](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L336))

```lean
theorem same_responses_iff_same_decisions {r : Response} {t : Term} :
  r ∼ t ↔ r.decision ∼ t
```

`Cedar.Thm.same_responses_self_decision` (theorem, [line 341](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L341))

```lean
theorem same_responses_self_decision {resp : Response} :
  resp ∼ resp.decision
```

`Cedar.Thm.same_decision_and_response_implies_same_decision` (theorem, [line 346](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L346))

```lean
theorem same_decision_and_response_implies_same_decision
  {decision : Spec.Decision} {resp : Response} {t : Term} :
  decision ∼ t → resp ∼ t → resp ∼ decision
```

`Cedar.Thm.isAuthorized_ok_implies` (theorem, [line 361](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L361))

```lean
theorem isAuthorized_ok_implies {ps : Policies} {εnv : SymEnv} {t : Term} :
  Cedar.SymCC.isAuthorized ps εnv = .ok t →
  ∃ tp tf,
    satisfiedPolicies .permit ps εnv = .ok tp ∧
    satisfiedPolicies .forbid ps εnv = .ok tf ∧
    t = and tp (not tf)
```

`Cedar.Thm.isAuthorized_wf` (theorem, [line 375](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L375))

```lean
theorem isAuthorized_wf {ps : Policies} {εnv : SymEnv} {t : Term} :
  εnv.WellFormedForPolicies ps →
  Cedar.SymCC.isAuthorized ps εnv = .ok t →
  t.WellFormed εnv.entities ∧ t.typeOf = .bool
```

`Cedar.Thm.isAuthorized_interpret_eq_when_interpret_eq` (theorem, [line 388](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L388))

```lean
theorem isAuthorized_interpret_eq_when_interpret_eq {ps : Policies} {εnv : SymEnv} {I I' : Interpretation} {t : Term}
  (hwε : εnv.WellFormedForPolicies ps)
  (hwI : I.WellFormed εnv.entities)
  (hwI' : I'.WellFormed εnv.entities)
  (heq : ∀ (p : Policy) (t : Term), p ∈ ps → compile p.toExpr εnv = Except.ok t → Term.interpret I t = Term.interpret I' t)
  (hok : SymCC.isAuthorized ps εnv = .ok t) :
  Term.interpret I t = Term.interpret I' t
```

`Cedar.Thm.isAuthorized_interpret` (theorem, [line 406](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L406))

```lean
theorem isAuthorized_interpret {ps : Policies} {εnv : SymEnv} {t : Term} {I : Interpretation} :
  εnv.WellFormedForPolicies ps →
  I.WellFormed εnv.entities →
  Cedar.SymCC.isAuthorized ps εnv = .ok t →
  Cedar.SymCC.isAuthorized ps (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.isAuthorized_same` (theorem, [line 423](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L423))

```lean
theorem isAuthorized_same {ps : Policies} {env : Env} {εnv : SymEnv} {t : Term} :
  εnv.WellFormedForPolicies ps →
  env.WellFormedForPolicies ps →
  env ∼ εnv →
  Cedar.SymCC.isAuthorized ps εnv = .ok t →
  Cedar.Spec.isAuthorized env.request env.entities ps ∼ t
```

`Cedar.Thm.isAuthorized_bisimulation` (theorem, [line 450](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean#L450))

```lean
theorem isAuthorized_bisimulation {ps : Policies} {env : Env} {εnv : SymEnv} {t : Term} {I : Interpretation} :
  εnv.WellFormedForPolicies ps →
  env.WellFormedForPolicies ps →
  I.WellFormed εnv.entities →
  env ∼ εnv.interpret I →
  Cedar.SymCC.isAuthorized ps εnv = .ok t →
  Cedar.Spec.isAuthorized env.request env.entities ps ∼ t.interpret I
```

## Depends on

- [Spec/Authorizer](../../spec/authorizer.md)
- [Well-formedness and interpretations](data/basic.md)

## Proof depends on

- [Authorization](../authorization.md)
- [Thm/SymCC/Compiler](compiler.md)

## Sources

- [Cedar/Thm/SymCC/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Authorizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Authorizer.json)
