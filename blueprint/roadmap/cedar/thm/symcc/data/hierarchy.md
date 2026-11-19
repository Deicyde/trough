---
catalog: module
lean: Cedar.Spec.Entities.Acyclic, Cedar.Spec.Entities.Transitive, Cedar.Spec.Entities.Hierarchical, Cedar.Spec.Entities.StronglyWellFormed, Cedar.Spec.Env.StronglyWellFormed, Cedar.Spec.Env.StronglyWellFormedFor, Cedar.Spec.Env.StronglyWellFormedForAll, Cedar.Spec.Env.StronglyWellFormedForPolicy, Cedar.Spec.Env.StronglyWellFormedForPolicies, Cedar.SymCC.SymEntityData.isEnum, Cedar.SymCC.SymEntityData.ConcreteAncestors, Cedar.SymCC.SymEntityData.SymbolicAncestors, Cedar.SymCC.SymEntityData.PartitionedAncestors, Cedar.SymCC.SymEntityData.PartitionedAncestors.isUDF_iff_isEnum, Cedar.SymCC.SymEntities.Partitioned, Cedar.SymCC.SymEntities.Acyclic, Cedar.SymCC.SymEntityData.knownAncestors, Cedar.SymCC.SymEntities.Transitive, Cedar.SymCC.SymEntities.Hierarchical, Cedar.SymCC.SymEntities.StronglyWellFormed, Cedar.SymCC.Term.isBasic, Cedar.SymCC.SymRequest.IsBasic, Cedar.SymCC.SymRequest.StronglyWellFormed, Cedar.SymCC.SymEnv.StronglyWellFormed, Cedar.SymCC.SymEnv.StronglyWellFormedFor, Cedar.SymCC.SymEnv.StronglyWellFormedForAll, Cedar.SymCC.SymEnv.StronglyWellFormedForPolicy, Cedar.SymCC.SymEnv.StronglyWellFormedForPolicies
statement: formalized
proof: formalized
---

# Strongly well-formed ancestor relations

`Cedar.Thm.SymCC.Data.Hierarchy`, in [Cedar/Thm/SymCC/Data/Hierarchy.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean).

> The Cedar specification requires the entity hierarchy to be a DAG. This means
> that a legal `ancestor` relation on entities is the transitive closure of a DAG:
> it is (1) acyclic and (b) transitive.
>
> This file formalizes the hierarchy requirements on the `ancestor` relation as
> extra constraints on well-formed `Entities`.  A set of `Entities` is _strongly
> well-formed_ if it satisfies the `WellFormed` predicate, as well as the
> `Acyclic` and `Transitive` predicate on its `ancestor` relation.
>
> We apply the same notion of strong well-formedness to symbolic environments.
> Specifically, if an Entity type is enumerated (such as Cedar's action), then the
> concrete the ancestor relation over that type must be concrete, acyclic, and
> transitive. Moreover, an enumerated type can only have other enumerated types as
> ancestors, and a non-enumerated type can only have other non-enumerated types as
> ancestors.  These constraints are enforced for actions, and we will continue to
> enforce them for other enums in the future.
>
> If needed, we could allow enumerated types to have arbirary entities as parents,
> but at the cost of generating more assumptions and complicating the proofs.
> Specifically, to lift this restriction, we need to the following:
>   * Change the definition of `footprints` to include all members of every
>     enumerated type, which will cause transitivity and acyclicity constraints to
>     be generated for these members along with the entities referenced in the
>     analyzed policies.
>   * Change the definition of `SameEntities es εs` so that `es` includes all
>     enumerated values from `εs`.  This is necessary to show soundness of
>     assumption generation (see `mem_footprint_reduce_exists_swf`; similar lemma
>     must hold for enumerated entities that would be included in the footprint).
>     This will require adjusting the proof that the result of `concretize?`
>     matches the input symbolic environment according to the new stricter
>     definition of `SameEntities`.  (It does, but this needs to be proven.)
>   * Drop the hierarchy assumptions defined in this file.  They become
>     unnecessary since they are checked / enforced by the assumption generator.
>   * Adjust the proofs of assumption generation soundness and completeness. These
>     proofs should become more uniform in that they can treat UDFs and UUFs
>     symmetrically.
>
> We use strong well-formedness to prove the correctness of Cedar's assumption
> generation (`Cedar.SymCC.Enforcer.enforce`).  Specifically, the assumptions
> are weak enough to be satisfied by all well-formed `ancestor` relations.  And
> they are strong enough to be satisfied only by (finite) well-formed `ancestor`
> relations.
>
> Finally, strongly well-formed environments also restrict the shape of the
> symbolic request. Specifically, the terms to which the request variables must be
> either variables or literals. They cannot be arbitrary terms because we need to
> be able to show that every "get attribute" term in the encoding corresponds to a
> "get attribute" expression in an input policy. This means that request terms
> cannot include spurious "get attribute" subterms.  Note that we can relax this
> strong well-formedness constraint on the `context` term to allow combination of
> variables and literals, similar to the partial evaluator.  This would complicate
> proofs so we won't do it until we find a use case for this functionality.
>
> See `Cedar/Thm/Verification.lean` for an example of how these definitions are
> used to prove soundness and completeness of the
> `Cedar.SymCC.Verifier.verifyEquivalent` query, which checks that two Cedar
> policies are equivalent on all strongly well-formed environments `env`
> represented by a given symbolic environment `εnv`.

`Cedar.Spec.Entities.Acyclic` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L92))

```lean
public def Entities.Acyclic (es : Entities) : Prop
```

`Cedar.Spec.Entities.Transitive` (definition, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L95))

```lean
public def Entities.Transitive (es : Entities) : Prop
```

`Cedar.Spec.Entities.Hierarchical` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L102))

```lean
public def Entities.Hierarchical (es : Entities) : Prop
```

`Cedar.Spec.Entities.StronglyWellFormed` (definition, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L105))

```lean
public def Entities.StronglyWellFormed (es : Entities) : Prop
```

`Cedar.Spec.Env.StronglyWellFormed` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L108))

```lean
public def Env.StronglyWellFormed (env : Env) : Prop
```

`Cedar.Spec.Env.StronglyWellFormedFor` (definition, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L112))

```lean
public def Env.StronglyWellFormedFor (env : Env) (x : Expr) : Prop
```

`Cedar.Spec.Env.StronglyWellFormedForAll` (definition, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L116))

```lean
public def Env.StronglyWellFormedForAll (env : Env) (xs : List Expr) : Prop
```

`Cedar.Spec.Env.StronglyWellFormedForPolicy` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L120))

```lean
public def Env.StronglyWellFormedForPolicy (env : Env) (p : Policy) : Prop
```

`Cedar.Spec.Env.StronglyWellFormedForPolicies` (definition, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L123))

```lean
public def Env.StronglyWellFormedForPolicies (env : Env) (ps : Policies) : Prop
```

`Cedar.SymCC.SymEntityData.isEnum` (definition, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L132))

```lean
public def SymEntityData.isEnum (δ : SymEntityData) : Bool
```

`Cedar.SymCC.SymEntityData.ConcreteAncestors` (definition, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L135))

```lean
public def SymEntityData.ConcreteAncestors (δ : SymEntityData) : Prop
```

`Cedar.SymCC.SymEntityData.SymbolicAncestors` (definition, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L138))

```lean
public def SymEntityData.SymbolicAncestors (δ : SymEntityData) : Prop
```

`Cedar.SymCC.SymEntityData.PartitionedAncestors` (definition, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L143))

```lean
public def SymEntityData.PartitionedAncestors (δ : SymEntityData) : Prop
```

`Cedar.SymCC.SymEntityData.PartitionedAncestors.isUDF_iff_isEnum` (theorem, [line 147](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L147))

```lean
public theorem SymEntityData.PartitionedAncestors.isUDF_iff_isEnum
  {δ : SymEntityData} {ancTy : EntityType} {f : UnaryFunction}
  (hpa : δ.PartitionedAncestors)
  (hf : δ.ancestors.find? ancTy = .some f) :
  f.isUDF = δ.isEnum
```

`Cedar.SymCC.SymEntities.Partitioned` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L167))

```lean
public def SymEntities.Partitioned (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEntities.Acyclic` (definition, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L177))

```lean
public def SymEntities.Acyclic (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEntityData.knownAncestors` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L184))

```lean
public def SymEntityData.knownAncestors (uid : EntityUID) (δ : SymEntityData) : Set EntityUID
```

`Cedar.SymCC.SymEntities.Transitive` (definition, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L191))

```lean
public def SymEntities.Transitive (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEntities.Hierarchical` (definition, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L198))

```lean
public def SymEntities.Hierarchical (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEntities.StronglyWellFormed` (definition, [line 201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L201))

```lean
public def SymEntities.StronglyWellFormed (εs : SymEntities) : Prop
```

`Cedar.SymCC.Term.isBasic` (definition, [line 204](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L204))

```lean
public def Term.isBasic : Term → Bool
```

`Cedar.SymCC.SymRequest.IsBasic` (definition, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L208))

```lean
public def SymRequest.IsBasic (ρ : SymRequest) : Prop
```

`Cedar.SymCC.SymRequest.StronglyWellFormed` (definition, [line 214](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L214))

```lean
public def SymRequest.StronglyWellFormed (ρ : SymRequest) (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEnv.StronglyWellFormed` (definition, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L217))

```lean
public def SymEnv.StronglyWellFormed (εnv : SymEnv) : Prop
```

`Cedar.SymCC.SymEnv.StronglyWellFormedFor` (definition, [line 221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L221))

```lean
public def SymEnv.StronglyWellFormedFor (εnv : SymEnv) (x : Expr) : Prop
```

`Cedar.SymCC.SymEnv.StronglyWellFormedForAll` (definition, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L225))

```lean
public def SymEnv.StronglyWellFormedForAll (εnv : SymEnv) (xs : List Expr) : Prop
```

`Cedar.SymCC.SymEnv.StronglyWellFormedForPolicy` (definition, [line 229](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L229))

```lean
public def SymEnv.StronglyWellFormedForPolicy (εnv : SymEnv) (p : Policy) : Prop
```

`Cedar.SymCC.SymEnv.StronglyWellFormedForPolicies` (definition, [line 232](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean#L232))

```lean
public def SymEnv.StronglyWellFormedForPolicies (εnv : SymEnv) (ps : Policies) : Prop
```

## Depends on

- [Well-formedness and interpretations](basic.md)

## Sources

- [Cedar/Thm/SymCC/Data/Hierarchy.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Hierarchy.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.Hierarchy.json)
