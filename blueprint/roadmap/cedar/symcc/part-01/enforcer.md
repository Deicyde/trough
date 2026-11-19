---
catalog: module
lean: Cedar.SymCC.footprint, Cedar.SymCC.footprints, Cedar.SymCC.acyclicity, Cedar.SymCC.transitivity, Cedar.SymCC.enforce
statement: formalized
proof: formalized
---

# Cedar/SymCC/Enforcer

`Cedar.SymCC.Enforcer`, in [Cedar/SymCC/Enforcer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean).

> This file defines the algorithm for emitting well-formedness assumptions about
> Cedar hierarchies. A valid Cedar hierarchy graph is the irreflexive transitive
> closure of a DAG.  (Note that the `in` operator is reflexive, but this is
> enforced separately by the semantics, and it's not needed in the hierarchy.)
>
> The generated assumptions are expressed as Terms that enforce the acyclicty and
> transitivity constraints on the symbolic store, for a given Cedar expression.
>
> The grounding relies on the fact that a Cedar expression can reference only a
> finite number of entities (so the domain of the quantification is finite), and
> we can compute an overapproximation of that set by statically analyzing the
> expression. We call this set the _footprint_ of the expression `x`, and it
> consists of all subexpressions of `x` that could have an Entity type. The
> grounding procedure computes the footprint, and grounds the acyclicity and
> transitivity constraints on the set of entity terms in the footprint.

`Cedar.SymCC.footprint` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean#L61))

> Returns the terms corresponding to subexpressions of `x` of the following form:
>
>   * A variable term with an entity type
>   * An entity reference literal
>   * An attribute access expression with an entity type
>   * A binary (`getTag`) expression with an entity type
>
> These are the only basic expressions in Cedar that may evaluate to an entity.
> All other expressions that evaluate to an entity are build up from the above
> basic expresions.
>
> All returned terms are of type `TermType.option .entity`.

```lean
def footprint (x : Expr) (εnv : SymEnv) : Set Term
```

`Cedar.SymCC.footprints` (definition, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean#L91))

> Returns the set of Terms corresponding to the footprints of xs.

```lean
def footprints (xs : List Expr) (εnv : SymEnv) : Set Term
```

`Cedar.SymCC.acyclicity` (definition, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean#L97))

> Returns the acyclicity constraint for the given term.

```lean
def acyclicity (t : Term) (εs : SymEntities) : Term
```

`Cedar.SymCC.transitivity` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean#L110))

> Returns the transitivity constraint for the given term.

```lean
def transitivity (t₁ t₂ : Term) (εs : SymEntities) : Term
```

`Cedar.SymCC.enforce` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean#L141))

> Returns the ground acyclicity and transitivity assumptions for xs and env.

```lean
def enforce (xs : List Expr) (εnv : SymEnv) : Set Term
```

## Depends on

- [Cedar/SymCC/Compiler](compiler.md)

## Sources

- [Cedar/SymCC/Enforcer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Enforcer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Enforcer.json)
