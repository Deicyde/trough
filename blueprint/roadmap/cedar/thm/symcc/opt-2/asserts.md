---
catalog: module
lean: Cedar.Thm.Asserts.Equiv, Cedar.Thm.ResultAssertsEquiv, Cedar.Thm.Asserts.Equiv.symm, Cedar.Thm.Asserts.Equiv.checkUnsatAsserts, Cedar.Thm.Asserts.Equiv.checkSatAsserts, Cedar.Thm.Asserts.Equiv.satAsserts?, Cedar.Thm.Asserts.Equiv.satAssertsOpt?
statement: formalized
proof: formalized
---

# Opt/Asserts

`Cedar.Thm.SymCC.Opt.Asserts`, in [Cedar/Thm/SymCC/Opt/Asserts.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean).

`Cedar.Thm.Asserts.Equiv` (inductive type, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L28))

> A notion of equivalence for `Asserts`, suited to the purposes of Cedar.Thm.SymCC.Opt.

```lean
inductive Asserts.Equiv : Asserts → Asserts → Prop where
  -- `Asserts` are equivalent to themselves
  | rfl (a : Asserts) : Equiv a a
  -- `Asserts` are also equivalent if constant-false appears in both lists, regardless of what else does or does not appear in the `Asserts`
  | constantFalse {a₁ a₂ : Asserts} (h₁ : .prim (.bool false) ∈ a₁) (h₂ : .prim (.bool false) ∈ a₂) : Equiv a₁ a₂
```

`Cedar.Thm.ResultAssertsEquiv` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L37))

```lean
def ResultAssertsEquiv (res₁ res₂ : Except ε Asserts) : Prop
```

`Cedar.Thm.Asserts.Equiv.symm` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L47))

> Symmetry for Asserts.Equiv

```lean
theorem Asserts.Equiv.symm {a₁ a₂ : Asserts} :
  a₁ ~ a₂ → a₂ ~ a₁
```

`Cedar.Thm.Asserts.Equiv.checkUnsatAsserts` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L57))

> Equivalent `Asserts` produce the same output in `checkUnsatAsserts`

```lean
theorem Asserts.Equiv.checkUnsatAsserts {a₁ a₂ : Asserts} {εnv : SymEnv} :
  a₁ ~ a₂ →
  checkUnsatAsserts a₁ εnv = checkUnsatAsserts a₂ εnv
```

`Cedar.Thm.Asserts.Equiv.checkSatAsserts` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L69))

> Equivalent `Asserts` produce the same output in `checkSatAsserts`

```lean
theorem Asserts.Equiv.checkSatAsserts {a₁ a₂ : Asserts} (εnv : SymEnv) :
  a₁ ~ a₂ →
  checkSatAsserts a₁ εnv = checkSatAsserts a₂ εnv
```

`Cedar.Thm.Asserts.Equiv.satAsserts?` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L81))

> Equivalent `Asserts` produce the same output in `satAsserts?`

```lean
theorem Asserts.Equiv.satAsserts? {a₁ a₂ : Asserts} (ps : Policies) (εnv : SymEnv) :
  a₁ ~ a₂ →
  satAsserts? ps a₁ εnv = satAsserts? ps a₂ εnv
```

`Cedar.Thm.Asserts.Equiv.satAssertsOpt?` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean#L91))

> Equivalent `Asserts` produce the same output in `satAssertsOpt?`

```lean
theorem Asserts.Equiv.satAssertsOpt? {a₁ a₂ : Asserts} (cpss : List CompiledPolicies) :
  a₁ ~ a₂ →
  satAssertsOpt? cpss a₁ = satAssertsOpt? cpss a₂
```

## Depends on

- [SymCCOpt/SatUnsat](../../../symccopt/satunsat.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Asserts.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Asserts.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Asserts.json)
