---
catalog: module
lean: Cedar.Thm.wf_interpretation_implies_wfl_var, Cedar.Thm.wf_interpretation_implies_wf_var, Cedar.Thm.wf_interpretation_implies_typeOf_var, Cedar.Thm.wf_interpretation_implies_wf_udf, Cedar.Thm.wf_interpretation_implies_wfp_option_get, Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_addrV4, Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_prefixV4, Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_addrV6, Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_prefixV6
statement: formalized
proof: formalized
---

# Basic properties of well-formed interpretations

`Cedar.Thm.SymCC.Interpretation`, in [Cedar/Thm/SymCC/Interpretation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean).

> This file proves basic lemmas about well-formedness predicate on
> interpretations.
> -

`Cedar.Thm.wf_interpretation_implies_wfl_var` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L34))

```lean
public theorem wf_interpretation_implies_wfl_var {εs : SymEntities} {I : Interpretation} {v : TermVar} :
  I.WellFormed εs → v.WellFormed εs → (I.vars v).WellFormedLiteral εs
```

`Cedar.Thm.wf_interpretation_implies_wf_var` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L40))

```lean
public theorem wf_interpretation_implies_wf_var {εs : SymEntities} {I : Interpretation} {v : TermVar} :
  I.WellFormed εs → v.WellFormed εs → (I.vars v).WellFormed εs
```

`Cedar.Thm.wf_interpretation_implies_typeOf_var` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L46))

```lean
public theorem wf_interpretation_implies_typeOf_var {εs : SymEntities} {I : Interpretation} {v : TermVar} :
  I.WellFormed εs → v.WellFormed εs → (I.vars v).typeOf = v.ty
```

`Cedar.Thm.wf_interpretation_implies_wf_udf` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L52))

```lean
public theorem wf_interpretation_implies_wf_udf {εs : SymEntities} {I : Interpretation} {f : UUF} :
  I.WellFormed εs → f.WellFormed εs →
  ((I.funs f).WellFormed εs ∧ (I.funs f).arg = f.arg ∧ (I.funs f).out = f.out)
```

`Cedar.Thm.wf_interpretation_implies_wfp_option_get` (theorem, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L60))

```lean
public theorem wf_interpretation_implies_wfp_option_get {εs : SymEntities} {I : Interpretation} {t : Term} {ty : TermType} :
  I.WellFormed εs → ty.WellFormed εs → t = .app Op.option.get [.none ty] ty →
  (I.partials t).WellFormedLiteral εs ∧ (I.partials t).typeOf = ty
```

`Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_addrV4` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L71))

```lean
public theorem wf_interpretation_implies_wfp_ext_ipaddr_addrV4 {εs : SymEntities} {I : Interpretation} {t : Term}
  (v6 : Ext.IPAddr.IPv6Addr) (p6 : Ext.IPAddr.IPv6Prefix) :
  I.WellFormed εs →
  t = .app (.ext ExtOp.ipaddr.addrV4) [.prim (.ext (.ipaddr (.V6 ⟨v6, p6⟩)))] (.bitvec 32) →
  (I.partials t).WellFormedLiteral εs ∧ (I.partials t).typeOf = (.bitvec 32)
```

`Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_prefixV4` (theorem, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L87))

```lean
public theorem wf_interpretation_implies_wfp_ext_ipaddr_prefixV4 {εs : SymEntities} {I : Interpretation} {t : Term}
  (v6 : Ext.IPAddr.IPv6Addr) (p6 : Ext.IPAddr.IPv6Prefix) :
  I.WellFormed εs →
  t = .app (.ext ExtOp.ipaddr.prefixV4) [.prim (.ext (.ipaddr (.V6 ⟨v6, p6⟩)))] (.option (.bitvec 5)) →
  (I.partials t).WellFormedLiteral εs ∧ (I.partials t).typeOf = (.option (.bitvec 5))
```

`Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_addrV6` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L103))

```lean
public theorem wf_interpretation_implies_wfp_ext_ipaddr_addrV6 {εs : SymEntities} {I : Interpretation} {t : Term}
  (v4 : Ext.IPAddr.IPv4Addr) (p4 : Ext.IPAddr.IPv4Prefix) :
  I.WellFormed εs →
  t = .app (.ext ExtOp.ipaddr.addrV6) [.prim (.ext (.ipaddr (.V4 ⟨v4, p4⟩)))] (.bitvec 128) →
  (I.partials t).WellFormedLiteral εs ∧ (I.partials t).typeOf = (.bitvec 128)
```

`Cedar.Thm.wf_interpretation_implies_wfp_ext_ipaddr_prefixV6` (theorem, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean#L119))

```lean
public theorem wf_interpretation_implies_wfp_ext_ipaddr_prefixV6 {εs : SymEntities} {I : Interpretation} {t : Term}
  (v4 : Ext.IPAddr.IPv4Addr) (p4 : Ext.IPAddr.IPv4Prefix) :
  I.WellFormed εs →
  t = .app (.ext ExtOp.ipaddr.prefixV6) [.prim (.ext (.ipaddr (.V4 ⟨v4, p4⟩)))] (.option (.bitvec 7)) →
  (I.partials t).WellFormedLiteral εs ∧ (I.partials t).typeOf = (.option (.bitvec 7))
```

## Depends on

- [Well-formedness and interpretations](data/basic.md)

## Proof depends on

- [Properties of Terms](term/typeof.md)

## Sources

- [Cedar/Thm/SymCC/Interpretation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Interpretation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Interpretation.json)
