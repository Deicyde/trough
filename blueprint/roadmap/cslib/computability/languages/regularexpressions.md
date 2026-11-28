---
catalog: module
lean: RegularExpression.mem_sum_matches', RegularExpression.iSup_matches'
statement: formalized
proof: formalized
---

# Regular Expressions (additional definitions and theorems)

`Cslib.Computability.Languages.RegularExpressions`, in [Cslib/Computability/Languages/RegularExpressions.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Languages/RegularExpressions.lean), by Chi-Yun Hsu.

> This file contains additional definitions and theorems about `RegularExpression`
> as defined and developed in `Mathlib.Computability.RegularExpressions`.

`RegularExpression.mem_sum_matches'` (theorem, [line 29](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Languages/RegularExpressions.lean#L29))

```lean
theorem mem_sum_matches' (rs : List (RegularExpression α)) (x : List α) :
    x ∈ rs.sum.matches' ↔ ∃ r ∈ rs, x ∈ r.matches'
```

`RegularExpression.iSup_matches'` (theorem, [line 36](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Languages/RegularExpressions.lean#L36))

```lean
theorem iSup_matches' {I : Type*} [Finite I] {s : Set I} {l : I → Language α}
    (h : ∀ i ∈ s, ∃ r : RegularExpression α, l i = r.matches') :
    ∃ r : RegularExpression α, (⨆ i ∈ s, l i) = r.matches'
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/RegularExpressions.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Languages/RegularExpressions.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Computability.Languages.RegularExpressions.json)
