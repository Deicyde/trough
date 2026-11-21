---
catalog: module
lean: Batteries.Tactic.PrintPrefixConfig
statement: formalized
proof: formalized
---

# PrintPrefix

`Batteries.Tactic.PrintPrefix`, in [Batteries/Tactic/PrintPrefix.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintPrefix.lean), by Shing Tak Lam, Daniel Selsam, Mario Carneiro.

`Batteries.Tactic.PrintPrefixConfig` (structure, [line 23](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintPrefix.lean#L23))

> Options to control `#print prefix` command and `getMatchingConstants`.

```lean
structure PrintPrefixConfig where
  /-- Include declarations in imported environment. -/
  imported : Bool := true
  /-- Include declarations whose types are propositions. -/
  propositions : Bool := true
  /-- Exclude declarations whose types are not propositions. -/
  propositionsOnly : Bool := false
  /-- Print the type of a declaration. -/
  showTypes : Bool := true
  /--
  Include internal declarations (names starting with `_`, `match_` or `proof_`)
  -/
  internals : Bool := false
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [EnvSearch](../lean/util/envsearch.md)

## Sources

- [Batteries/Tactic/PrintPrefix.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintPrefix.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.PrintPrefix.json)
