---
catalog: module
lean: Cedar.Validation.lubBool, Cedar.Validation.lubQualifiedType, Cedar.Validation.lubRecordType, Cedar.Validation.lub?, Cedar.Validation.subty
statement: formalized
proof: formalized
---

# Subtyping

`Cedar.Validation.Subtyping`, in [Cedar/Validation/Subtyping.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean).

`Cedar.Validation.lubBool` (definition, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean#L27))

```lean
public def lubBool (b₁ b₂ : BoolType) : BoolType
```

`Cedar.Validation.lubQualifiedType` (definition, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean#L31))

```lean
public def lubQualifiedType (q₁ q₂ : QualifiedType) : Option QualifiedType
```

`Cedar.Validation.lubRecordType` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean#L37))

```lean
public def lubRecordType (ty₁ ty₂ : List (Attr × QualifiedType)) : Option (List (Attr × QualifiedType))
```

`Cedar.Validation.lub?` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean#L50))

```lean
public def lub? (ty₁ ty₂ : CedarType) : Option CedarType
```

`Cedar.Validation.subty` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean#L62))

```lean
public def subty (ty₁ ty₂ : CedarType) : Bool
```

## Depends on

- [Validation/Types](types.md)

## Sources

- [Cedar/Validation/Subtyping.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Subtyping.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Subtyping.json)
