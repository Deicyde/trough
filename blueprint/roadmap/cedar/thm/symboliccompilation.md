---
catalog: module
lean: Cedar.Thm.compile_is_sound, Cedar.Thm.compile_is_complete, Cedar.Thm.isAuthorized_is_sound, Cedar.Thm.isAuthorized_is_complete, Cedar.Thm.compile_well_typed, Cedar.Thm.IsOption, Cedar.Thm.OptionTyped, Cedar.Thm.compile_ok_implies_option
statement: formalized
proof: formalized
---

# SymbolicCompilation

`Cedar.Thm.SymbolicCompilation`, in [Cedar/Thm/SymbolicCompilation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean).

> This file defines the top-level correctness properties for the symbolic
> compiler. We show the encoding is sound and complete with respect to the
> concrete semantics of Cedar. That is, the symbolic semantics both
> overapproximates (soundness) and underapproximates (completeness) the concrete
> semantics.
> -

`Cedar.Thm.compile_is_sound` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L71))

> Let `x` be a Cedar expression, `env` a concrete evaluation environment (request
> and entities), `εnv` a symbolic environment, and `t` the outcome of
> compiling `x` to a Term with respect to `εnv`.
>
> Let `x` and `env` be a well-formed input to the concrete evaluator, i.e.,
> `env.WellFormedFor x`.  This means that the entity store `env.entities` has
> no dangling entity references, and all entity references that occur in `x` and
> `env.request` are included in `env.entities`.
>
> Let `x` and `εnv` be a well-formed input to the symbolic compiler, i.e.,
> `εnv.WellFormedFor x`.  This means that the symbolic entity store `εnv.entities`
> has no dangling (undefined) entity types or references; all term types contained
> in `εnv.entities` represent valid Cedar types; and all entity references that
> occur in `x` and `εnv.request` are valid according to
> `εnv.entities.isValidEntityUID`.
>
> Let `εnv` represent a set of concrete environments that includes `env`, i.e.,
> `env ∈ᵢ εnv`.  We relate concrete structures to their symbolic counterparts via
> interpretations, which map from term variables and uninterpreted functions to
> literals.  For example, `env ∈ᵢ εnv` if there exists a well-formed interpretation
> `I` such that `env ∼ εnv.interpret I` are equivalent according to the sameness
> relation `∼`.  Note that we can't use equality here, because interpreting a
> symbolic structure with respect to an `Interpretation` produces a literal
> symbolic structure (without any unknowns), which is then compared to the
> corresponding concrete structure using a suitable sameness relation.
>
> Given the above, the soundness theorem says that the output of the concrete
> evaluator on `x` and `env` is contained in the set of concrete outcomes
> represented by the output of the symbolic compiler on `x` and `εnv`. We state
> soundness in terms of `Outcome`s rather than `Result`s because the symbolic
> compiler does not distinguish between different kinds of errors---only between
> normal and erroring executions.

```lean
theorem compile_is_sound {x : Expr} {env : Env} {εnv : SymEnv} {t : Term.Outcome εnv} :
  εnv.WellFormedFor x →
  env.WellFormedFor x →
  env ∈ᵢ εnv →
  compile x εnv = .ok t →
  ∃ (o : Outcome Value),
    o ∈ₒ t ∧
    evaluate x env.request env.entities ∼ o
```

`Cedar.Thm.compile_is_complete` (theorem, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L99))

> Let `x` be a Cedar expression and `εnv` a symbolic environment, where
> `x` and `εnv` are a well-formed input to the symbolic compiler, i.e.,
> `εnv.WellFormedFor x`.
>
> Let `t` the outcome of compiling `x` to a Term with respect to `εnv`, and `o` a
> concrete outcome represented by `t`.
>
> Then, the completeness theorem says that there exists a concrete environment
> `env` represented by `εnv` such that `x` and `env` are well-formed inputs to the
> concrete evaluator and evaluating `x` against `env` produces the outcome `o`.

```lean
theorem compile_is_complete {x : Expr} {εnv : SymEnv} {t : Term.Outcome εnv} {o : Outcome Value} :
  εnv.WellFormedFor x →
  compile x εnv = .ok t →
  o ∈ₒ t →
  ∃ (env : Env),
    env.WellFormedFor x ∧
    env ∈ᵢ εnv ∧
    evaluate x env.request env.entities ∼ o
```

`Cedar.Thm.isAuthorized_is_sound` (theorem, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L155))

> Let `ps` be Cedar policies, `env` a concrete evaluation environment (request and
> entities), `εnv` a symbolic environment, and `t` the term resulting
> from symbolically authorizing `ps` with respect to `εnv`, i.e.,
> `SymCC.isAuthorized ps εnv = .ok t`.
>
> Let `ps` and `env` be a well-formed input to the concrete authorizer, i.e.,
> `env.WellFormedForPolicies ps`.  This means that the entity store `env.entities`
> has no dangling entity references, and all entity references that occur in `ps`
> and `env.request` are included in `env.entities`.
>
> Let `ps` and `εnv` be a well-formed input to the symbolic authorizer, i.e.,
> `εnv.WellFormedForPolices ps`.  This means that the symbolic entity store
> `εnv.entities` has no dangling (undefined) entity types or references; all term
> types contained in `εnv.entities` represent valid Cedar types; and all entity
> references that occur in `ps` and `εnv.request` are valid according to
> `εnv.entities.isValidEntityUID`.
>
> Let `εnv` represent a set of concrete environments that includes `env`, i.e.,
> `env ∈ᵢ εnv`.  We relate concrete structures to their symbolic counterparts via
> interpretations, which map from term variables and uninterpreted functions to
> literals.  For example, `env ∈ᵢ εnv` if there exists a well-formed interpretation
> `I` such that `env ∼ εnv.interpret I` are equivalent according to the sameness
> relation `∼`.  Note that we can't use equality here, because interpreting a
> symbolic structure with respect to an `Interpretation` produces a literal
> symbolic structure (without any unknowns), which is then compared to the
> corresponding concrete structure using a suitable sameness relation.
>
> Given the above, the soundness theorem says that the decision of the concrete
> authorizer on `ps` and `env` is contained in the set of concrete decisions
> represented by the output of the symbolic authorizer on `ps` and `εnv`. We state
> soundness in terms of `Decision`s rather than `Response`s because the symbolic
> authorizer computes only decision (and not the extra diagnostics contained in a
> concrete `Response`).

```lean
theorem isAuthorized_is_sound  {ps : Policies} {env : Env} {εnv : SymEnv} {t : Term.Outcome εnv} :
  εnv.WellFormedForPolicies ps →
  env.WellFormedForPolicies ps →
  env ∈ᵢ εnv →
  SymCC.isAuthorized ps εnv = .ok t →
  ∃ (decision : Spec.Decision),
    decision ∈ₒ t ∧
    Spec.isAuthorized env.request env.entities ps ∼ decision
```

`Cedar.Thm.isAuthorized_is_complete` (theorem, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L183))

> Let `ps` be Cedar policies and `εnv` a symbolic environment, where
> `ps` and `εnv` are a well-formed input to the symbolic authorizer, i.e.,
> `εnv.WellFormedForPolicies ps`.
>
> Let `t` the outcome of symbolically authorizing `ps` with respect to `εnv`, and `d` a
> concrete authorization decision represented by `t`.
>
> Then, the completeness theorem says that there exists a concrete environment
> `env` represented by `εnv` such that `ps` and `env` are well-formed inputs to the
> concrete authorizer and authorizing `os` against `env` produces the decision `d`.

```lean
theorem isAuthorized_is_complete {ps : Policies} {εnv : SymEnv} {t : Term.Outcome εnv} {decision : Spec.Decision} :
  εnv.WellFormedForPolicies ps →
  SymCC.isAuthorized ps εnv = .ok t →
  decision ∈ₒ t →
  ∃ (env : Env),
    env.WellFormedForPolicies ps ∧
    env ∈ᵢ εnv ∧
    Spec.isAuthorized env.request env.entities ps ∼ decision
```

`Cedar.Thm.compile_well_typed` (theorem, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L208))

> For any well-typed expression `tx` in a well-formed environment `Γ`
> (which can be produced by Cedar's type checker), the symbolic compiler
> should never fail and produce a term `t` that is well-formed and has
> the type `TermType.ofType tx.typeOf`.

```lean
theorem compile_well_typed {tx : TypedExpr} {Γ : TypeEnv} :
  Γ.WellFormed →
  TypedExpr.WellTyped Γ tx →
  ∃ t : Term,
    compile tx.toExpr (SymEnv.ofEnv Γ) = .ok t ∧
    t.WellFormed (SymEnv.ofEnv Γ).entities ∧
    t.typeOf = .option (TermType.ofType tx.typeOf)
```

`Cedar.Thm.IsOption` (definition, [line 223](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L223))

```lean
def IsOption (tty : TermType)
```

`Cedar.Thm.OptionTyped` (definition, [line 224](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L224))

```lean
def OptionTyped (t : Term)
```

`Cedar.Thm.compile_ok_implies_option` (theorem, [line 398](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean#L398))

> Weaker result than `compile_well_typed`, but requiring weaker hypotheses:
>
> If `compile` on any expression (not necessarily well-typed) produces `.ok t`,
> then `t` must have option type

```lean
theorem compile_ok_implies_option {x : Expr} {εnv : SymEnv} {t : Term} :
  compile x εnv = .ok t →
  ∃ tty, t.typeOf = .option tty
```

## Depends on

- [Spec/Authorizer](../spec/authorizer.md)
- [Well-formedness and interpretations](symcc/data/basic.md)
- [Typechecker/WF](validation-2/typechecker-2/wf.md)
- [Expr/Definition](welltyped/expr-2/definition.md)

## Proof depends on

- [Thm/SymCC/Authorizer](symcc/authorizer.md)
- [Concretizer](symcc/concretizer.md)

## Sources

- [Cedar/Thm/SymbolicCompilation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymbolicCompilation.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.SymbolicCompilation.json)
