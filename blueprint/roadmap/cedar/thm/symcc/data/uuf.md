---
catalog: module
lean: Cedar.Thm.prefix_ne_at_index, Cedar.Thm.uuf_attrs_ancs_no_confusion, Cedar.Thm.uuf_attrs_tag_keys_no_confusion, Cedar.Thm.uuf_attrs_tag_vals_no_confusion, Cedar.Thm.uuf_tag_vals_tag_keys_no_confusion, Cedar.Thm.uuf_tag_keys_ancs_no_confusion, Cedar.Thm.uuf_tag_vals_ancs_no_confusion
statement: formalized
proof: formalized
---

# UUF

`Cedar.Thm.SymCC.Data.UUF`, in [Cedar/Thm/SymCC/Data/UUF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean).

> Some facts about `UUF.*_id`s.

`Cedar.Thm.prefix_ne_at_index` (theorem, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L27))

```lean
theorem prefix_ne_at_index {p₁ p₂ x y : String} {i : Nat}
  (h₁ : i < p₁.toList.length)
  (h₂ : i < p₂.toList.length)
  (hₙ : p₁.toList[i]? ≠ p₂.toList[i]?) :
  (p₁ ++ x).toList ≠ (p₂ ++ y).toList
```

`Cedar.Thm.uuf_attrs_ancs_no_confusion` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L54))

```lean
theorem uuf_attrs_ancs_no_confusion
  {ety₁ ety₂ ancTy} :
  UUF.attrsId ety₁ ≠ UUF.ancsId ety₂ ancTy
```

`Cedar.Thm.uuf_attrs_tag_keys_no_confusion` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L61))

```lean
theorem uuf_attrs_tag_keys_no_confusion
  {ety₁ ety₂} :
  UUF.attrsId ety₁ ≠ UUF.tagKeysId ety₂
```

`Cedar.Thm.uuf_attrs_tag_vals_no_confusion` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L68))

```lean
theorem uuf_attrs_tag_vals_no_confusion
  {ety₁ ety₂} :
  UUF.attrsId ety₁ ≠ UUF.tagValsId ety₂
```

`Cedar.Thm.uuf_tag_vals_tag_keys_no_confusion` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L75))

```lean
theorem uuf_tag_vals_tag_keys_no_confusion
  {ety₁ ety₂} :
  UUF.tagValsId ety₁ ≠ UUF.tagKeysId ety₂
```

`Cedar.Thm.uuf_tag_keys_ancs_no_confusion` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L82))

```lean
theorem uuf_tag_keys_ancs_no_confusion
  {ety₁ ety₂ ancTy} :
  UUF.tagKeysId ety₁ ≠ UUF.ancsId ety₂ ancTy
```

`Cedar.Thm.uuf_tag_vals_ancs_no_confusion` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean#L89))

```lean
theorem uuf_tag_vals_ancs_no_confusion
  {ety₁ ety₂ ancTy} :
  UUF.tagValsId ety₁ ≠ UUF.ancsId ety₂ ancTy
```

## Depends on

- [Env](../../../symcc/part-01/env.md)

## Sources

- [Cedar/Thm/SymCC/Data/UUF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/UUF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.UUF.json)
