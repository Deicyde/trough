---
catalog: module
lean: Cedar.Spec.Prim.WellFormed, Cedar.Spec.Value.WellFormed, Cedar.Spec.Request.WellFormed, Cedar.Spec.EntityData.WellFormed, Cedar.Spec.Entities.WellFormed, Cedar.Spec.Prim.ValidRef, Cedar.Spec.Expr.ValidRefs, Cedar.Spec.Env.WellFormed, Cedar.Spec.Entities.ValidRefsFor, Cedar.Spec.Env.WellFormedFor, Cedar.Spec.Env.WellFormedForPolicies, Cedar.Spec.Value.WellStructured, Cedar.Spec.Entities.ClosedFor, Cedar.Spec.Outcome, Cedar.Spec.SameOutcomes, Cedar.Spec.SameDecisions, Cedar.Spec.Same, Cedar.SymCC.TermType.cedarType?, Cedar.SymCC.TermType.isCedarRecordType, Cedar.SymCC.isCedarRecordType_implies_term_record_type, Cedar.SymCC.isCedarRecordType_implies_cedarType?_some, Cedar.SymCC.TermType.isCedarType, Cedar.SymCC.TermType.WellFormed, Cedar.SymCC.TermPrim.WellFormed, Cedar.SymCC.TermVar.WellFormed, Cedar.SymCC.ExtOp.WellTyped, Cedar.SymCC.UUF.WellFormed, Cedar.SymCC.Op.WellTyped, Cedar.SymCC.Term.WellFormed, Cedar.SymCC.Term.WellFormedLiteral, Cedar.SymCC.UDF.WellFormed, Cedar.SymCC.UnaryFunction.WellFormed, Cedar.SymCC.SymRequest.WellFormed, Cedar.SymCC.SymTags.WellFormed, Cedar.SymCC.SymEntityData.WellFormed, Cedar.SymCC.SymEntities.WellFormed, Cedar.SymCC.SymEnv.WellFormed, Cedar.SymCC.SymEntities.ValidRefsFor, Cedar.SymCC.SymEnv.WellFormedFor, Cedar.SymCC.SymEnv.WellFormedLiteralFor, Cedar.SymCC.SymEnv.WellFormedForPolicies, Cedar.SymCC.Asserts.WellFormed, Cedar.SymCC.SameValues, Cedar.SymCC.SameOutcomes, Cedar.SymCC.SameResults, Cedar.SymCC.SameDecisions, Cedar.SymCC.SameResponses, Cedar.SymCC.SameRequests, Cedar.SymCC.SameTags, Cedar.SymCC.SameEntityData, Cedar.SymCC.SameEntities, Cedar.SymCC.SameEnvs, Cedar.SymCC.Term.WellFormedPartialApp, Cedar.SymCC.Interpretation.WellFormed, Cedar.SymCC.Asserts.satisfiedBy, Cedar.SymCC.Asserts.Satisfiable, Cedar.SymCC.Asserts.Unsatisfiable, Cedar.SymCC.Term.Outcome, Cedar.SymCC.instCoeTermOutcome, Cedar.SymCC.memOfTermOutcome, Cedar.SymCC.memOfSymEnv, Cedar.SymCC.Env.EnumCompleteFor
statement: formalized
proof: formalized
---

# Well-formedness and interpretations

`Cedar.Thm.SymCC.Data.Basic`, in [Cedar/Thm/SymCC/Data/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean).

> This file defines well-formedness constraints and relations on concrete and
> symbolic structures. We prove correctness properties of the symbolic compiler
> with respect to these defintions.
>
> Well-formedness of a concrete structure is defined with respect to a set of
> concrete entities `es : Entities`.  A `Value`, `Request`, or `EntityData`
> structure is well-formed with respect to `es` if it references only entity UIDs
> that are in the _domain_ of `es`; i.e., if the structure references a `uid`,
> then `uid ∈ es`. The set `es` is well-formed if it consists of well-formed
> `EntityData` structures, which amounts to saying that there are no dangling
> references in the entities set `es`. Finally, an environment `Env` consisting of
> a request `req` and entities `es` is _well-formed for_ an expression `x` if `es`
> is well-formed, `req` is well-formed with respect to `es`, and `es` supports
> `x`. We say that `es` _supports_ `x` if all entity UIDs referenced by `x` are in
> the domain of `es`. If `env` is well-formed for `x`, then evaluating `x` against
> `env` cannot result in an `entityDoesNotExist` error.
>
> Well-formed symbolic structures are defined analagously to well-formed concrete
> structures. In particular, well-formedness of a symbolic structure is defined
> with respect to a set of symbolic entity declarations `εs : SymEntities`. A
> `Term`, `SymRequest`, or `SymEntityData` structure is well-formed with respect
> to `εs` if it references only entity types and UIDs that are in the _domain_ of
> `εs`, and if all referenced term types represent valid Cedar types. An entity
> type `ety` is in the domain of `εs` if `ety ∈ εs`, and entity UID `uid` is in
> the domain of `εs` if `εs.isValidEntityUID uid`.  The set `εs` is well-formed if
> it consists of well-formed `SymEntityData` structures. A symbolic environment
> `SymEnv` consisting of a symbolic request `ρeq` and entities `εs` is
> _well-formed for_ an expression `x` if `εs` is well-formed, `ρeq` is well-formed
> with respect to `εs`, and `εs` _supports_ `x`.  We say that `εs` supports `x` if
> `εs.isValidEntityUID uid` for every entity `uid` referenced by `x`.
>
> A well-formed symbolic structure represents a _set_ of well-formed symbolic
> _literal_ structures, which, in turn, represent corresponding well-formed Cedar
> structures. A _literal_ symbolic structure contains no term variables or
> uninterpreted functions. Symbolic structures are related to literals through
> _interpretations_. An `Interpretation` binds term variables to literal terms and
> uninterpreted functions (`UUF`) to interpreted ones (`UDF`). When a well-formed
> symbolic structure is interpreted with respect to a well-formed Interpretation,
> the result is a well-formed literal symbolic structure. Interpreting a literal
> against any Interpretation returns the same literal.
>
> A literal term or symbolic request represent a single corresponding Cedar
> structure (i.e., a `Value`, `Outcome Value`, or `Request`). A well-formed
> literal symbolic environment `εnv : SymEnv` represents a set of well-formed
> concrete environments that lead to equivalent evaluation outcomes. In
> particular, if `εnv` is a literal symbolic environment that is well-formed for
> an expression `x`, then `x` produces the same outcome when evaluated against any
> concrete environment `env ∈ εnv` that is well-formed for `x`. We write `env ∈ εnv`
> to denote that exists a well-formed interpretation `I` such that
> `εnv.interpret I` is a literal that represents `env`.

`Cedar.Spec.Prim.WellFormed` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L94))

```lean
public def Prim.WellFormed (es : Entities) : Prim → Prop
```

`Cedar.Spec.Value.WellFormed` (inductive type, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L98))

```lean
public inductive Value.WellFormed (es : Entities) : Value → Prop
  | prim_wf {p : Prim}
    (h₁ : p.WellFormed es) :
    WellFormed es (.prim p)
  | set_wf {s : Set Value}
    (h₁ : ∀ v, v ∈ s → v.WellFormed es)
    (h₂ : s.WellFormed) :
    WellFormed es (.set s)
  | record_wf {r : Map Attr Value}
    (h₁ : ∀ a v, r.find? a = some v → v.WellFormed es)
    (h₂ : r.WellFormed) :
    WellFormed es (.record r)
  | ext_wf {xv : Ext} :
    WellFormed es (.ext xv)
```

`Cedar.Spec.Request.WellFormed` (definition, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L114))

```lean
public def Request.WellFormed (es : Entities) (req : Request) : Prop
```

`Cedar.Spec.EntityData.WellFormed` (definition, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L121))

```lean
public def EntityData.WellFormed (es : Entities) (d : EntityData) : Prop
```

`Cedar.Spec.Entities.WellFormed` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L129))

```lean
public def Entities.WellFormed (es : Entities) : Prop
```

`Cedar.Spec.Prim.ValidRef` (definition, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L134))

```lean
public def Prim.ValidRef (validRef : EntityUID → Prop) : Prim → Prop
```

`Cedar.Spec.Expr.ValidRefs` (inductive type, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L138))

```lean
public inductive Expr.ValidRefs (validRef : EntityUID → Prop) : Expr → Prop
  | lit_valid {p : Prim}
    (h₁ : p.ValidRef validRef) :
    ValidRefs validRef (.lit p)
  | var_valid {v : Var} :
    ValidRefs validRef (.var v)
  | ite_valid {x₁ x₂ x₃ : Expr}
    (h₁ : ValidRefs validRef x₁)
    (h₂ : ValidRefs validRef x₂)
    (h₃ : ValidRefs validRef x₃) :
    ValidRefs validRef (.ite x₁ x₂ x₃)
  | and_valid {x₁ x₂ : Expr}
    (h₁ : ValidRefs validRef x₁)
    (h₂ : ValidRefs validRef x₂) :
    ValidRefs validRef (.and x₁ x₂)
  | or_valid {x₁ x₂ : Expr}
    (h₁ : ValidRefs validRef x₁)
    (h₂ : ValidRefs validRef x₂) :
    ValidRefs validRef (.or x₁ x₂)
  | binaryApp_valid {op₂ : BinaryOp} {x₁ x₂ : Expr}
    (h₁ : ValidRefs validRef x₁)
    (h₂ : ValidRefs validRef x₂) :
    ValidRefs validRef (.binaryApp op₂ x₁ x₂)
  | unaryApp_valid {op₁ : UnaryOp} {x₁ : Expr}
    (h₁ : ValidRefs validRef x₁) :
    ValidRefs validRef (.unaryApp op₁ x₁)
  | hasAttr_valid {x₁ : Expr} {a : Attr}
    (h₁ : ValidRefs validRef x₁) :
    ValidRefs validRef (.hasAttr x₁ a)
  | extHasAttr_valid {x₁ : Expr} {a : Attr} {as : List Attr}
    (h₁ : ValidRefs validRef x₁) :
    ValidRefs validRef (.extHasAttr x₁ a as)
  | getAttr_valid {x₁ : Expr} {a : Attr}
    (h₁ : ValidRefs validRef x₁) :
    ValidRefs validRef (.getAttr x₁ a)
  | set_valid {xs : List Expr}
    (h₁ : ∀ x ∈ xs, ValidRefs validRef x) :
    ValidRefs validRef (.set xs)
  | record_valid {axs : List (Attr × Expr)}
    (h₁ : ∀ ax ∈ axs, ValidRefs validRef ax.snd) :
    ValidRefs validRef (.record axs)
  | call_valid {xfn : ExtFun} {xs : List Expr}
    (h₁ : ∀ x ∈ xs, ValidRefs validRef x) :
    ValidRefs validRef (.call xfn xs)
```

`Cedar.Spec.Env.WellFormed` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L184))

```lean
public def Env.WellFormed (env : Env) : Prop
```

`Cedar.Spec.Entities.ValidRefsFor` (abbreviation, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L188))

```lean
public abbrev Entities.ValidRefsFor (es : Entities) (x : Expr) : Prop
```

`Cedar.Spec.Env.WellFormedFor` (definition, [line 192](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L192))

```lean
public def Env.WellFormedFor (env : Env) (x : Expr) : Prop
```

`Cedar.Spec.Env.WellFormedForPolicies` (definition, [line 196](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L196))

```lean
public def Env.WellFormedForPolicies (env : Env) (ps : Policies) : Prop
```

`Cedar.Spec.Value.WellStructured` (inductive type, [line 201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L201))

```lean
public inductive Value.WellStructured : Value → Prop
  | prim_ws {p : Prim} :
    WellStructured (.prim p)
  | set_ws {s : Set Value}
    (h₁ : ∀ v, v ∈ s → v.WellStructured)
    (h₂ : s.WellFormed) :
    WellStructured (.set s)
  | record_ws {r : Map Attr Value}
    (h₁ : ∀ a v, r.find? a = some v → v.WellStructured)
    (h₂ : r.WellFormed) :
    WellStructured (.record r)
  | ext_ws {xv : Ext} :
    WellStructured (.ext xv)
```

`Cedar.Spec.Entities.ClosedFor` (definition, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L215))

```lean
public def Entities.ClosedFor (es : Entities) (uids : Set EntityUID) : Prop
```

`Cedar.Spec.Outcome` (abbreviation, [line 220](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L220))

```lean
public abbrev Outcome (α)
```

`Cedar.Spec.SameOutcomes` (definition, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L222))

```lean
public def SameOutcomes (res : Result Value) (out : Outcome Value) : Prop
```

`Cedar.Spec.SameDecisions` (definition, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L228))

```lean
public def SameDecisions (resp : Response) (dec : Decision) : Prop
```

`Cedar.Spec.Same` (class, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L235))

> The notation typeclass for the heterogeneous sameness (equivalence) relation.
> This enables the notation `a ∼ b : Prop` where `a : α`, `b : β`.

```lean
public class Same (α : Type u) (β : Type v) where
  /-- `a ∼ b` relates `a` and `b`. The meaning of this notation is type-dependent. -/
  same : α → β → Prop
```

`Cedar.SymCC.TermType.cedarType?` (definition, [line 256](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L256))

```lean
public def TermType.cedarType? : TermType → Option CedarType
  | .bool             => .some (.bool .anyBool)
  | .bitvec 64        => .some .int
  | .string           => .some .string
  | .entity ety       => .some (.entity ety)
  | .set ty           => do .some (.set (← ty.cedarType?))
  | .record rty       => do
    let crty ← rty.mapMOnValues₂ λ ⟨tyᵢ, _⟩ => qualifiedType? tyᵢ
    .some (.record crty)
  | .ext xty          => .some (.ext xty)
  | _                 => .none
```

`Cedar.SymCC.TermType.isCedarRecordType` (definition, [line 274](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L274))

> Not @[expose]'d -- callers use the public lemmas immediately below which
> specify things you can conclude when `isCedarRecordType` is true

```lean
public def TermType.isCedarRecordType (ty : TermType) : Bool
```

`Cedar.SymCC.isCedarRecordType_implies_term_record_type` (theorem, [line 279](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L279))

```lean
public theorem isCedarRecordType_implies_term_record_type {ty : TermType} :
  ty.isCedarRecordType → ∃ rty, ty = .record rty
```

`Cedar.SymCC.isCedarRecordType_implies_cedarType?_some` (theorem, [line 303](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L303))

```lean
public theorem isCedarRecordType_implies_cedarType?_some {ty : TermType} :
  ty.isCedarRecordType → ∃ cty, ty.cedarType? = some cty
```

`Cedar.SymCC.TermType.isCedarType` (definition, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L308))

```lean
public def TermType.isCedarType (ty : TermType) : Bool
```

`Cedar.SymCC.TermType.WellFormed` (inductive type, [line 311](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L311))

```lean
public inductive TermType.WellFormed (εs : SymEntities) : TermType → Prop
  | bool_wf :
    WellFormed εs .bool
  | bitvec_wf {n : Nat} :
    WellFormed εs (.bitvec n)
  | string_wf :
    WellFormed εs .string
  | option_wf {ty : TermType}
    (h₁ : WellFormed εs ty) :
    WellFormed εs (.option ty)
  | entity_wf {ety : EntityType}
    (h₁ : εs.isValidEntityType ety) :
    WellFormed εs (.entity ety)
  | set_wf {ty : TermType}
    (h₁ : WellFormed εs ty) :
    WellFormed εs (.set ty)
  | record_wf {rty : Map Attr TermType}
    (h₁ : ∀ a ty, rty.find? a = some ty → WellFormed εs ty)
    (h₂ : rty.WellFormed):
    WellFormed εs (.record rty)
  | ext_wf {xty : ExtType} :
    WellFormed εs (.ext xty)
```

`Cedar.SymCC.TermPrim.WellFormed` (inductive type, [line 334](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L334))

```lean
public inductive TermPrim.WellFormed (εs : SymEntities) : TermPrim → Prop
  | bool_wf {b : Bool} :
    WellFormed εs (.bool b)
  | bitvec_wf {n : Nat} {bv : BitVec n} :
    WellFormed εs (.bitvec bv)
  | string_wf {s : String} :
    WellFormed εs (.string s)
  | entity_wf {uid : EntityUID}
    (h₁ : εs.isValidEntityUID uid) :
    WellFormed εs (.entity uid)
  | ext_wf {x : Ext} :
    WellFormed εs (.ext x)
```

`Cedar.SymCC.TermVar.WellFormed` (definition, [line 348](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L348))

```lean
public def TermVar.WellFormed (εs : SymEntities) (v : TermVar) : Prop
```

`Cedar.SymCC.ExtOp.WellTyped` (inductive type, [line 351](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L351))

```lean
public inductive ExtOp.WellTyped : ExtOp → List Term → TermType → Prop
  | decimal.val_wt {t : Term}
    (h₁ : t.typeOf = (.ext .decimal)) :
    WellTyped ExtOp.decimal.val [t] (.bitvec 64)
  | ipaddr.isV4_wt {t : Term}
    (h₁ : t.typeOf = (.ext .ipAddr)) :
    WellTyped ipaddr.isV4 [t] .bool
  | ipaddr.addrV4_wt {t : Term}
    (h₁ : t.typeOf = (.ext .ipAddr)) :
    WellTyped ipaddr.addrV4 [t] (.bitvec 32)
  | ipaddr.prefixV4_wt {t : Term}
    (h₁ : t.typeOf = (.ext .ipAddr)) :
    WellTyped ipaddr.prefixV4 [t] (.option (.bitvec 5))
  | ipaddr.addrV6_wt {t : Term}
    (h₁ : t.typeOf = (.ext .ipAddr)) :
    WellTyped ipaddr.addrV6 [t] (.bitvec 128)
  | ipaddr.prefixV6_wt {t : Term}
    (h₁ : t.typeOf = (.ext .ipAddr)) :
    WellTyped ipaddr.prefixV6 [t] (.option (.bitvec 7))
  | datetime.val_wt {t : Term}
    (h₁ : t.typeOf = (.ext .datetime)) :
    WellTyped datetime.val [t] (.bitvec 64)
  | datetime.ofBitVec_wt {t : Term}
    (h₁ : t.typeOf = (.bitvec 64)) :
    WellTyped datetime.ofBitVec [t] (.ext .datetime)
  | duration.val_wt {t : Term}
    (h₁ : t.typeOf = (.ext .duration)) :
    WellTyped duration.val [t] (.bitvec 64)
  | duration.ofBitVec_wt {t : Term}
    (h₁ : t.typeOf = (.bitvec 64)) :
    WellTyped duration.ofBitVec [t] (.ext .duration)
```

`Cedar.SymCC.UUF.WellFormed` (definition, [line 384](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L384))

```lean
public def UUF.WellFormed (εs : SymEntities) (f : UUF) : Prop
```

`Cedar.SymCC.Op.WellTyped` (inductive type, [line 388](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L388))

```lean
public inductive Op.WellTyped (εs : SymEntities) : Op → List Term → TermType → Prop
  | not_wt {t : Term}
    (h₁ : t.typeOf = .bool) :
    WellTyped εs .not [t] .bool
  | and_wt {t₁ t₂ : Term}
    (h₁ : t₁.typeOf = .bool)
    (h₂ : t₂.typeOf = .bool) :
    WellTyped εs .and [t₁, t₂] .bool
  | or_wt {t₁ t₂ : Term}
    (h₁ : t₁.typeOf = .bool)
    (h₂ : t₂.typeOf = .bool) :
    WellTyped εs .or [t₁, t₂] .bool
  | eq_wt {t₁ t₂ : Term}
    (h₁ : t₁.typeOf = t₂.typeOf) :
    WellTyped εs .eq [t₁, t₂] .bool
  | ite_wt {t₁ t₂ t₃ : Term}
    (h₁ : t₁.typeOf = .bool)
    (h₂ : t₂.typeOf = t₃.typeOf) :
    WellTyped εs .ite [t₁, t₂, t₃] t₂.typeOf
  | uuf_wt {f : UUF} {t : Term}
    (h₁ : t.typeOf = f.arg)
    (h₂ : f.WellFormed εs) :
    WellTyped εs (.uuf f) [t] f.out
  | bvneg_wt {t : Term} {n : Nat}
    (h₁ : t.typeOf = .bitvec n) :
    WellTyped εs .bvneg [t] (.bitvec n)
  | bvnego_wt {t : Term} {n : Nat}
    (h₁ : t.typeOf = .bitvec n) :
    WellTyped εs .bvnego [t] .bool
  | bvadd_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvadd [t₁, t₂] (.bitvec n)
  | bvsub_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsub [t₁, t₂] (.bitvec n)
  | bvmul_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvmul [t₁, t₂] (.bitvec n)
  | bvsdiv_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsdiv [t₁, t₂] (.bitvec n)
  | bvudiv_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvudiv [t₁, t₂] (.bitvec n)
  | bvsrem_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsrem [t₁, t₂] (.bitvec n)
  | bvsmod_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsmod [t₁, t₂] (.bitvec n)
  | bvurem_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvurem [t₁, t₂] (.bitvec n)
  | bvshl_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvshl [t₁, t₂] (.bitvec n)
  | bvlshr_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvlshr [t₁, t₂] (.bitvec n)
  | bvsaddo_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsaddo [t₁, t₂] .bool
  | bvssubo_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvssubo [t₁, t₂] .bool
  | bvsmulo_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsmulo [t₁, t₂] .bool
  | bvslt_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvslt [t₁, t₂] .bool
  | bvsle_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvsle [t₁, t₂] .bool
  | bvult_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvult [t₁, t₂] .bool
  | bvule_wt {t₁ t₂ : Term} {n : Nat}
    (h₁ : t₁.typeOf = .bitvec n)
    (h₂ : t₂.typeOf = .bitvec n) :
    WellTyped εs .bvule [t₁, t₂] .bool
  | zero_extend_wt {t : Term} {n m : Nat}
    (h₁ : t.typeOf = .bitvec m) :
    WellTyped εs (.zero_extend n) [t] (.bitvec (n + m))
  | set.member_wt {t₁ t₂ : Term}
    (h₁ : t₂.typeOf = .set (t₁.typeOf)) :
    WellTyped εs Op.set.member [t₁, t₂] .bool
  | set.subset_wt {t₁ t₂ : Term} {ty : TermType}
    (h₁ : t₁.typeOf = .set ty)
    (h₂ : t₂.typeOf = .set ty) :
    WellTyped εs Op.set.subset [t₁, t₂] .bool
  | set.inter_wt {t₁ t₂ : Term} {ty : TermType}
    (h₁ : t₁.typeOf = .set ty)
    (h₂ : t₂.typeOf = .set ty) :
    WellTyped εs Op.set.inter [t₁, t₂] (.set ty)
  | option.get_wt {t : Term} {ty : TermType}
    (h₁ : t.typeOf = .option ty) :
    WellTyped εs Op.option.get [t] ty
  | record.get_wt {t : Term} {a : Attr} {ty : TermType} {rty : Map Attr TermType}
    (h₁ : t.typeOf = .record rty)
    (h₂ : rty.find? a = .some ty) :
    WellTyped εs (Op.record.get a) [t] ty
  | string.like_wt {t : Term} {p : Pattern}
    (h₁ : t.typeOf = .string) :
    WellTyped εs (Op.string.like p) [t] .bool
  | ext_wt {xop : ExtOp} {ts : List Term} {ty : TermType}
    (h₁ : xop.WellTyped ts ty) :
    WellTyped εs (.ext xop) ts ty
```

`Cedar.SymCC.Term.WellFormed` (inductive type, [line 513](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L513))

```lean
public inductive Term.WellFormed (εs : SymEntities) : Term → Prop
  | prim_wf {p : TermPrim}
    (h₁ : p.WellFormed εs) :
    WellFormed εs (.prim p)
  | var_wf {v : TermVar}
    (h₁ : v.WellFormed εs) :
    WellFormed εs (.var v)
  | none_wf {ty : TermType}
    (h₁ : ty.WellFormed εs):
    WellFormed εs (.none ty)
  | some_wf {t : Term}
    (h₁ : t.WellFormed εs):
    WellFormed εs (.some t)
  | app_wf {op : Op} {ts : List Term} {ty : TermType}
    (h₁ : ∀ t, t ∈ ts → t.WellFormed εs)
    (h₂ : op.WellTyped εs ts ty) :
    WellFormed εs (.app op ts ty)
  | set_wf {s : Set Term} {ty : TermType}
    (h₁ : ∀ t, t ∈ s → t.WellFormed εs)
    (h₂ : ∀ t, t ∈ s → t.typeOf = ty)
    (h₃ : ty.WellFormed εs)
    (h₄ : s.WellFormed) :
    WellFormed εs (.set s ty)
  | record_wf {r : Map Attr Term}
    (h₁ : ∀ a t, (a, t) ∈ r.toList → t.WellFormed εs)
    (h₂ : r.WellFormed):
    WellFormed εs (.record r)
```

`Cedar.SymCC.Term.WellFormedLiteral` (definition, [line 542](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L542))

```lean
public def Term.WellFormedLiteral (εs : SymEntities) (t : Term) : Prop
```

`Cedar.SymCC.UDF.WellFormed` (definition, [line 546](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L546))

```lean
public def UDF.WellFormed (εs : SymEntities) (f : UDF) : Prop
```

`Cedar.SymCC.UnaryFunction.WellFormed` (definition, [line 557](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L557))

```lean
public def UnaryFunction.WellFormed (εs : SymEntities) : UnaryFunction → Prop
```

`Cedar.SymCC.SymRequest.WellFormed` (definition, [line 562](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L562))

```lean
public def SymRequest.WellFormed (εs : SymEntities) (req : SymRequest) : Prop
```

`Cedar.SymCC.SymTags.WellFormed` (definition, [line 573](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L573))

```lean
public def SymTags.WellFormed (εs : SymEntities) (ety : EntityType) (τs : SymTags) : Prop
```

`Cedar.SymCC.SymEntityData.WellFormed` (definition, [line 582](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L582))

```lean
public def SymEntityData.WellFormed (εs : SymEntities) (ety : EntityType) (d : SymEntityData) : Prop
```

`Cedar.SymCC.SymEntities.WellFormed` (definition, [line 595](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L595))

```lean
public def SymEntities.WellFormed (εs : SymEntities) : Prop
```

`Cedar.SymCC.SymEnv.WellFormed` (definition, [line 600](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L600))

```lean
public def SymEnv.WellFormed (εnv : SymEnv) : Prop
```

`Cedar.SymCC.SymEntities.ValidRefsFor` (abbreviation, [line 604](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L604))

```lean
public abbrev SymEntities.ValidRefsFor (εs : SymEntities) (x : Expr) : Prop
```

`Cedar.SymCC.SymEnv.WellFormedFor` (definition, [line 608](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L608))

```lean
public def SymEnv.WellFormedFor (εnv : SymEnv) (x : Expr) : Prop
```

`Cedar.SymCC.SymEnv.WellFormedLiteralFor` (definition, [line 612](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L612))

```lean
public def SymEnv.WellFormedLiteralFor (εnv : SymEnv) (x : Expr) : Prop
```

`Cedar.SymCC.SymEnv.WellFormedForPolicies` (definition, [line 616](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L616))

```lean
public def SymEnv.WellFormedForPolicies (εnv : SymEnv) (ps : Policies) : Prop
```

`Cedar.SymCC.Asserts.WellFormed` (definition, [line 620](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L620))

```lean
public def Asserts.WellFormed (εs : SymEntities) (asserts : Asserts) : Prop
```

`Cedar.SymCC.SameValues` (definition, [line 626](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L626))

```lean
public def SameValues (v : Value) (t : Term) : Prop
```

`Cedar.SymCC.SameOutcomes` (definition, [line 630](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L630))

```lean
public def SameOutcomes : Outcome Value → Term → Prop
```

`Cedar.SymCC.SameResults` (definition, [line 636](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L636))

```lean
public def SameResults : Spec.Result Value → Term → Prop
```

`Cedar.SymCC.SameDecisions` (definition, [line 642](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L642))

```lean
public def SameDecisions : Spec.Decision → Term → Prop
```

`Cedar.SymCC.SameResponses` (definition, [line 648](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L648))

```lean
public def SameResponses (resp : Response) (t : Term) : Prop
```

`Cedar.SymCC.SameRequests` (definition, [line 652](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L652))

```lean
public def SameRequests (req : Request) (ρeq : SymRequest) : Prop
```

`Cedar.SymCC.SameTags` (definition, [line 659](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L659))

```lean
public def SameTags (uid : EntityUID) (d : EntityData) (δ : SymEntityData) : Prop
```

`Cedar.SymCC.SameEntityData` (definition, [line 669](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L669))

```lean
public def SameEntityData (uid : EntityUID) (d : EntityData) (δ : SymEntityData) : Prop
```

`Cedar.SymCC.SameEntities` (definition, [line 686](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L686))

```lean
public def SameEntities (es : Entities) (εs : SymEntities) : Prop
```

`Cedar.SymCC.SameEnvs` (definition, [line 694](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L694))

```lean
public def SameEnvs (env : Env) (εnv : SymEnv) : Prop
```

`Cedar.SymCC.Term.WellFormedPartialApp` (inductive type, [line 726](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L726))

```lean
public inductive Term.WellFormedPartialApp (εs : SymEntities) : Term → Prop
  | none_wfp {ty : TermType}
    (h₁ : ty.WellFormed εs) :
    Term.WellFormedPartialApp εs (Term.app Op.option.get [.none ty] ty)
  | ext_ipddr_addr4_wfp {ip : IPAddr}
    (h₁ : ¬ ip.isV4) :
    Term.WellFormedPartialApp εs (Term.app (.ext ExtOp.ipaddr.addrV4) [.prim (.ext (.ipaddr ip))] (.bitvec 32))
  | ext_ipddr_prefix4_wfp {ip : IPAddr}
    (h₁ : ¬ ip.isV4) :
    Term.WellFormedPartialApp εs (Term.app (.ext ExtOp.ipaddr.prefixV4) [.prim (.ext (.ipaddr ip))] (.option (.bitvec 5)))
  | ext_ipddr_addr6_wfp {ip : IPAddr}
    (h₁ : ¬ ip.isV6) :
    Term.WellFormedPartialApp εs (Term.app (.ext ExtOp.ipaddr.addrV6) [.prim (.ext (.ipaddr ip))] (.bitvec 128))
  | ext_ipddr_prefix6_wfp {ip : IPAddr}
    (h₁ : ¬ ip.isV6) :
    Term.WellFormedPartialApp εs (Term.app (.ext ExtOp.ipaddr.prefixV6) [.prim (.ext (.ipaddr ip))] (.option (.bitvec 7)))
```

`Cedar.SymCC.Interpretation.WellFormed` (definition, [line 744](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L744))

```lean
public def Interpretation.WellFormed (I : Interpretation) (εs : SymEntities) : Prop
```

`Cedar.SymCC.Asserts.satisfiedBy` (definition, [line 760](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L760))

```lean
public def Asserts.satisfiedBy (I : Interpretation) (asserts : Asserts) : Bool
```

`Cedar.SymCC.Asserts.Satisfiable` (definition, [line 763](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L763))

```lean
public def Asserts.Satisfiable (env : SymEnv) (asserts : Asserts) : Prop
```

`Cedar.SymCC.Asserts.Unsatisfiable` (definition, [line 766](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L766))

```lean
public def Asserts.Unsatisfiable (env : SymEnv) (asserts : Asserts) : Prop
```

`Cedar.SymCC.Term.Outcome` (structure, [line 775](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L775))

```lean
public structure Term.Outcome (εnv : SymEnv) where
  term : Term
deriving Repr, DecidableEq
```

`Cedar.SymCC.instCoeTermOutcome` (instance, [line 779](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L779))

```lean
public instance instCoeTermOutcome {εnv} : CoeOut (Term.Outcome εnv) Term
```

`Cedar.SymCC.memOfTermOutcome` (definition, [line 782](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L782))

```lean
public def memOfTermOutcome {α} {εnv} [Same α Term] (o : α) (o' : Term.Outcome εnv) : Prop
```

`Cedar.SymCC.memOfSymEnv` (definition, [line 787](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L787))

```lean
public def memOfSymEnv (env : Env) (εnv : SymEnv) : Prop
```

`Cedar.SymCC.Env.EnumCompleteFor` (definition, [line 799](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean#L799))

> This is a condition that `env` contains all enum entities
> (including actions) specified in `εnv`. It's required for
> completeness (of `SymEnv.ofEnv`) and satisfied by the
> concretizer, but it's not required for the soundness, so
> we keep it as a separate definition here.

```lean
public def Env.EnumCompleteFor (env : Env) (εnv : SymEnv) : Prop
```

## Depends on

- [Response](../../../spec/response.md)
- [Concretizing symbolic environments](../../../symcc/part-01/concretizer.md)
- [Interpretations](../../../symcc/part-01/interpretation.md)
- [SymCC/Verifier](../../../symcc/part-02/verifier.md)
- [Map properties](../../data/map.md)

## Sources

- [Cedar/Thm/SymCC/Data/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.Basic.json)
