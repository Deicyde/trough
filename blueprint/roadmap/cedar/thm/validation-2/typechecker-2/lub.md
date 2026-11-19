---
catalog: module
lean: Cedar.Thm.IsLubOfRecordTypes, Cedar.Thm.lubRecordType_is_lub_of_record_types, Cedar.Thm.lubRecord_find_implies_find, Cedar.Thm.lubRecord_find_implied_by_find_left, Cedar.Thm.lubRecord_contains_left, Cedar.Thm.lubRecord_find_implies_find_left, Cedar.Thm.lubRecordType_nil_some, Cedar.Thm.lubBool_eq_ite, Cedar.Thm.lubBool_comm, Cedar.Thm.lubQualified_comm, Cedar.Thm.lubRecord_comm, Cedar.Thm.lub?_entity, Cedar.Thm.lub_comm, Cedar.Thm.lub_refl, Cedar.Thm.lubRecordType_refl, Cedar.Thm.lubQualifiedType_refl, Cedar.Thm.lubQualified_is_lub_of_getType, Cedar.Thm.lub_trans, Cedar.Thm.lubRecordType_trans, Cedar.Thm.lubQualifiedType_trans, Cedar.Thm.subty_iff_lub?_eq_some, Cedar.Thm.subty_trans, Cedar.Thm.lub_left_subty, Cedar.Thm.lubRecordType_left_subty, Cedar.Thm.lubQualifiedType_left_subty, Cedar.Thm.sizeOf_qualified_lt_sizeOf_record_type, Cedar.Thm.lubBool_assoc_none_some, Cedar.Thm.lub_assoc_none_some, Cedar.Thm.lubRecordType_assoc_none_some, Cedar.Thm.lubQualifiedType_assoc_none_some, Cedar.Thm.lubBool_assoc_some_some, Cedar.Thm.lub_assoc_some_some, Cedar.Thm.lubRecordType_assoc_some_some, Cedar.Thm.lubQualifiedType_assoc_some_some, Cedar.Thm.lub_assoc, Cedar.Thm.lub_lub_fixed, Cedar.Thm.foldlM_of_lub_is_LUB, Cedar.Thm.foldlM_of_lub_assoc
statement: formalized
proof: formalized
---

# LUB

`Cedar.Thm.Validation.Typechecker.LUB`, in [Cedar/Thm/Validation/Typechecker/LUB.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean).

> This file contains useful definitions and lemmas about the
> least upper bound (LUB) functions on Cedar types.

`Cedar.Thm.IsLubOfRecordTypes` (inductive type, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L38))

```lean
inductive IsLubOfRecordTypes : List (Attr × Qualified CedarType) → List (Attr × Qualified CedarType) → List (Attr × Qualified CedarType) → Prop where
  | nil : IsLubOfRecordTypes [] [] []
  | cons {a : Attr} {qty qty₁ qty₂ : Qualified CedarType} {rty rty₁ rty₂ : List (Attr × Qualified CedarType)}
    (h₁ : lubQualifiedType qty₁ qty₂ = .some qty)
    (h₂ : IsLubOfRecordTypes rty rty₁ rty₂) :
    IsLubOfRecordTypes ((a, qty) :: rty) ((a, qty₁) :: rty₁) ((a, qty₂) :: rty₂)
```

`Cedar.Thm.lubRecordType_is_lub_of_record_types` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L45))

```lean
theorem lubRecordType_is_lub_of_record_types {rty rty₁ rty₂ : List (Attr × Qualified CedarType)} :
  lubRecordType rty₁ rty₂ = .some rty →
  IsLubOfRecordTypes rty rty₁ rty₂
```

`Cedar.Thm.lubRecord_find_implies_find` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L68))

```lean
theorem lubRecord_find_implies_find {a : Attr} {qty : QualifiedType} {rty rty₁ rty₂ : List (Attr × Qualified CedarType)}
  (h₁ : IsLubOfRecordTypes rty rty₁ rty₂)
  (h₂ : Map.find? (Map.mk rty) a = .some qty) :
  (∃ qty₁ qty₂,
    Map.find? (Map.mk rty₁) a = .some qty₁ ∧
    Map.find? (Map.mk rty₂) a = .some qty₂ ∧
    lubQualifiedType qty₁ qty₂ = .some qty)
```

`Cedar.Thm.lubRecord_find_implied_by_find_left` (theorem, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L88))

```lean
theorem lubRecord_find_implied_by_find_left {a : Attr} {qty₁ : QualifiedType} {rty rty₁ rty₂ : List (Attr × Qualified CedarType)}
  (h₁ : IsLubOfRecordTypes rty rty₁ rty₂)
  (h₂ : Map.find? (Map.mk rty₁) a = .some qty₁) :
  (∃ qty qty₂,
    Map.find? (Map.mk rty₂) a = .some qty₂ ∧
    Map.find? (Map.mk rty) a = .some qty ∧
    lubQualifiedType qty₁ qty₂ = .some qty)
```

`Cedar.Thm.lubRecord_contains_left` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L108))

```lean
theorem lubRecord_contains_left {a : Attr} {rty rty₁ rty₂ : List (Attr × Qualified CedarType)}
  (h₁ : IsLubOfRecordTypes rty rty₁ rty₂)
  (h₂ : Map.contains (Map.mk rty₁) a = true) :
  Map.contains (Map.mk rty) a = true
```

`Cedar.Thm.lubRecord_find_implies_find_left` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L118))

```lean
theorem lubRecord_find_implies_find_left {a : Attr} {qty : QualifiedType} {rty rty₁ rty₂ : List (Attr × Qualified CedarType)}
  (h₁ : IsLubOfRecordTypes rty rty₁ rty₂)
  (h₂ : Map.find? (Map.mk rty) a = some qty) :
  ∃ qty₁,
    Map.find? (Map.mk rty₁) a = some qty₁ ∧
    Qualified.isRequired qty₁ = Qualified.isRequired qty
```

`Cedar.Thm.lubRecordType_nil_some` (theorem, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L136))

```lean
theorem lubRecordType_nil_some {rty₁ rty₂ : List (Attr × QualifiedType)} :
  lubRecordType [] rty₁ = some rty₂ →
  (rty₁ = [] ∧ rty₂ = [])
```

`Cedar.Thm.lubBool_eq_ite` (theorem, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L142))

```lean
theorem lubBool_eq_ite {bty₁ bty₂ : BoolType} :
  lubBool bty₁ bty₂ = if bty₁ = bty₂ then bty₁ else .anyBool
```

`Cedar.Thm.lubBool_comm` (theorem, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L146))

```lean
theorem lubBool_comm {bty₁ bty₂ : BoolType} :
  lubBool bty₁ bty₂ = lubBool bty₂ bty₁
```

`Cedar.Thm.lubQualified_comm` (theorem, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L153))

```lean
theorem lubQualified_comm {qty₁ qty₂ : Qualified CedarType} :
  lubQualifiedType qty₁ qty₂ = lubQualifiedType qty₂ qty₁
```

`Cedar.Thm.lubRecord_comm` (theorem, [line 169](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L169))

```lean
theorem lubRecord_comm {rty₁ rty₂ : List (Attr × Qualified CedarType)} :
  lubRecordType rty₁ rty₂ = lubRecordType rty₂ rty₁
```

`Cedar.Thm.lub?_entity` (theorem, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L189))

```lean
theorem lub?_entity {ety₁ ety₂ : EntityType} :
  (CedarType.entity ety₁ ⊔ CedarType.entity ety₂) = if ety₁ = ety₂ then some (CedarType.entity ety₁) else none
```

`Cedar.Thm.lub_comm` (theorem, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L193))

```lean
theorem lub_comm {ty₁ ty₂ : CedarType} :
  (ty₁ ⊔ ty₂) = (ty₂ ⊔ ty₁)
```

`Cedar.Thm.lub_refl` (theorem, [line 224](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L224))

```lean
theorem lub_refl (ty : CedarType) :
  (ty ⊔ ty) = some ty
```

`Cedar.Thm.lubRecordType_refl` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L237))

```lean
theorem lubRecordType_refl (rty : List (Attr × QualifiedType)) :
  lubRecordType rty rty = some rty
```

`Cedar.Thm.lubQualifiedType_refl` (theorem, [line 252](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L252))

```lean
theorem lubQualifiedType_refl (qty : QualifiedType) :
  lubQualifiedType qty qty = some qty
```

`Cedar.Thm.lubQualified_is_lub_of_getType` (theorem, [line 273](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L273))

```lean
theorem lubQualified_is_lub_of_getType {qty qty₁ qty₂: Qualified CedarType}
  (h₁ : lubQualifiedType qty₁ qty₂ = .some qty) :
  (qty₁.getType ⊔ qty₂.getType) = .some qty.getType
```

`Cedar.Thm.lub_trans` (theorem, [line 290](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L290))

```lean
theorem lub_trans {ty₁ ty₂ ty₃ : CedarType} :
  (ty₁ ⊔ ty₂) = some ty₂ →
  (ty₂ ⊔ ty₃) = some ty₃ →
  (ty₁ ⊔ ty₃) = some ty₃
```

`Cedar.Thm.lubRecordType_trans` (theorem, [line 346](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L346))

```lean
theorem lubRecordType_trans {rty₁ rty₂ rty₃ : List (Attr × QualifiedType)} :
  (lubRecordType rty₁ rty₂) = some rty₂ →
  (lubRecordType rty₂ rty₃) = some rty₃ →
  (lubRecordType rty₁ rty₃) = some rty₃
```

`Cedar.Thm.lubQualifiedType_trans` (theorem, [line 381](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L381))

```lean
theorem lubQualifiedType_trans {qty₁ qty₂ qty₃ : QualifiedType} :
  (lubQualifiedType qty₁ qty₂) = some qty₂ →
  (lubQualifiedType qty₂ qty₃) = some qty₃ →
  (lubQualifiedType qty₁ qty₃) = some qty₃
```

`Cedar.Thm.subty_iff_lub?_eq_some` (theorem, [line 403](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L403))

```lean
theorem subty_iff_lub?_eq_some {ty₁ ty₂ : CedarType} :
  ty₁ ⊑ ty₂ ↔ (ty₁ ⊔ ty₂) = some ty₂
```

`Cedar.Thm.subty_trans` (theorem, [line 409](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L409))

```lean
theorem subty_trans {ty₁ ty₂ ty₃ : CedarType} :
  ty₁ ⊑ ty₂ → ty₂ ⊑ ty₃ → ty₁ ⊑ ty₃
```

`Cedar.Thm.lub_left_subty` (theorem, [line 422](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L422))

```lean
theorem lub_left_subty {ty₁ ty₂ ty₃ : CedarType} :
  (ty₁ ⊔ ty₂) = some ty₃ → ty₁ ⊑ ty₃
```

`Cedar.Thm.lubRecordType_left_subty` (theorem, [line 459](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L459))

```lean
theorem lubRecordType_left_subty {rty₁ rty₂ rty₃ : List (Attr × QualifiedType)} :
  lubRecordType rty₁ rty₂ = some rty₃ →
  lubRecordType rty₁ rty₃ = some rty₃
```

`Cedar.Thm.lubQualifiedType_left_subty` (theorem, [line 480](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L480))

```lean
theorem lubQualifiedType_left_subty {qty₁ qty₂ qty₃ : QualifiedType} :
  lubQualifiedType qty₁ qty₂ = some qty₃ →
  lubQualifiedType qty₁ qty₃ = some qty₃
```

`Cedar.Thm.sizeOf_qualified_lt_sizeOf_record_type` (theorem, [line 503](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L503))

```lean
theorem sizeOf_qualified_lt_sizeOf_record_type (x : Attr × Qualified CedarType) (xs : List (Attr × Qualified CedarType)) :
  sizeOf x.snd < sizeOf (x :: xs)
```

`Cedar.Thm.lubBool_assoc_none_some` (theorem, [line 514](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L514))

```lean
theorem lubBool_assoc_none_some {ty₁ ty₂ : CedarType} {bty₁ bty₂ : BoolType}
  (h₁ : (ty₁ ⊔ CedarType.bool bty₁) = none)
  (h₂ : some (CedarType.bool (lubBool bty₁ bty₂)) = some ty₂) :
  (ty₁ ⊔ ty₂) = none
```

`Cedar.Thm.lub_assoc_none_some` (theorem, [line 531](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L531))

```lean
theorem lub_assoc_none_some {ty₁ ty₂ ty₃ ty₄ : CedarType}
  (h₁ : (ty₁ ⊔ ty₂) = none)
  (h₂ : (ty₂ ⊔ ty₃) = some ty₄) :
  (ty₁ ⊔ ty₄) = none
```

`Cedar.Thm.lubRecordType_assoc_none_some` (theorem, [line 566](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L566))

```lean
theorem lubRecordType_assoc_none_some {rty₁ rty₂ rty₃ rty₄ : List (Attr × QualifiedType)}
  (h₁ : (lubRecordType rty₁ rty₂) = none)
  (h₂ : (lubRecordType rty₂ rty₃) = some rty₄) :
  (lubRecordType rty₁ rty₄) = none
```

`Cedar.Thm.lubQualifiedType_assoc_none_some` (theorem, [line 603](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L603))

```lean
theorem lubQualifiedType_assoc_none_some {qty₁ qty₂ qty₃ qty₄ : QualifiedType}
  (h₁ : (lubQualifiedType qty₁ qty₂) = none)
  (h₂ : (lubQualifiedType qty₂ qty₃) = some qty₄) :
  (lubQualifiedType qty₁ qty₄) = none
```

`Cedar.Thm.lubBool_assoc_some_some` (theorem, [line 626](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L626))

```lean
theorem lubBool_assoc_some_some {ty₄ ty₅ : CedarType } { bty₁ bty₂ bty₃ : BoolType }
  (h₁ : CedarType.bool (lubBool bty₁ bty₂) = ty₄)
  (h₂ : CedarType.bool (lubBool bty₂ bty₃) = ty₅) :
(ty₄ ⊔ CedarType.bool bty₃) = (CedarType.bool bty₁ ⊔ ty₅)
```

`Cedar.Thm.lub_assoc_some_some` (theorem, [line 638](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L638))

```lean
theorem lub_assoc_some_some {ty₁ ty₂ ty₃ ty₄ ty₅ : CedarType}
  (h₁ : (ty₁ ⊔ ty₂) = some ty₄)
  (h₂ : (ty₂ ⊔ ty₃) = some ty₅) :
  (ty₄ ⊔ ty₃) = (ty₁ ⊔ ty₅)
```

`Cedar.Thm.lubRecordType_assoc_some_some` (theorem, [line 674](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L674))

```lean
theorem lubRecordType_assoc_some_some {rty₁ rty₂ rty₃ rty₄ rty₅ : List (Attr × QualifiedType)}
  (h₁ : (lubRecordType rty₁ rty₂) = some rty₄)
  (h₂ : (lubRecordType rty₂ rty₃) = some rty₅) :
  (lubRecordType rty₄ rty₃) = (lubRecordType rty₁ rty₅)
```

`Cedar.Thm.lubQualifiedType_assoc_some_some` (theorem, [line 726](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L726))

```lean
theorem lubQualifiedType_assoc_some_some {qty₁ qty₂ qty₃ qty₄ qty₅ : QualifiedType}
  (h₁ : (lubQualifiedType qty₁ qty₂) = some qty₄)
  (h₂ : (lubQualifiedType qty₂ qty₃) = some qty₅) :
  (lubQualifiedType qty₄ qty₃) = (lubQualifiedType qty₁ qty₅)
```

`Cedar.Thm.lub_assoc` (theorem, [line 746](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L746))

```lean
theorem lub_assoc (ty₁ ty₂ ty₃ : CedarType) :
  (do let ty₄ ← (ty₁ ⊔ ty₂) ; (ty₄ ⊔ ty₃)) =
  (do let ty₄ ← (ty₂ ⊔ ty₃) ; (ty₁ ⊔ ty₄))
```

`Cedar.Thm.lub_lub_fixed` (theorem, [line 762](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L762))

```lean
theorem lub_lub_fixed {ty₁ ty₂ ty₃ ty₄ : CedarType}
  (h₁ : (ty₁ ⊔ ty₂) = some ty₃)
  (h₂ : (ty₃ ⊔ ty₄) = some ty₄) :
  (ty₁ ⊔ ty₄) = some ty₄
```

`Cedar.Thm.foldlM_of_lub_is_LUB` (theorem, [line 774](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L774))

```lean
theorem foldlM_of_lub_is_LUB {ty lubTy : CedarType } {tys : List CedarType}
  (h₁ : List.foldlM lub? ty tys = some lubTy) :
  (ty ⊔ lubTy) = some lubTy
```

`Cedar.Thm.foldlM_of_lub_assoc` (theorem, [line 791](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean#L791))

```lean
theorem foldlM_of_lub_assoc (ty₁ ty₂ : CedarType) (tys : List CedarType) :
  List.foldlM lub? ty₁ (ty₂ :: tys) =
  (do let ty₃ ← List.foldlM lub? ty₂ tys ; ty₁ ⊔ ty₃)
```

## Depends on

- [Subtyping](../../../validation/subtyping.md)

## Proof depends on

- [Map properties](../../data/map.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/LUB.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LUB.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.LUB.json)
