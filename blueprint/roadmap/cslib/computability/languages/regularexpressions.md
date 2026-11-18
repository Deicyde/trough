---
catalog: module
lean: RegularExpression.mem_sum_matches', RegularExpression.iSup_matches'
statement: formalized
proof: formalized
---

# Regular Expressions (additional definitions and theorems)

`Cslib.Computability.Languages.RegularExpressions`, in [Cslib/Computability/Languages/RegularExpressions.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularExpressions.lean), by Chi-Yun Hsu.

> This file contains additional definitions and theorems about `RegularExpression`
> as defined and developed in `Mathlib.Computability.RegularExpressions`.

`RegularExpression.mem_sum_matches'` (theorem, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularExpressions.lean#L29))

```lean
theorem mem_sum_matches' (rs : List (RegularExpression α)) (x : List α) :
    x ∈ rs.sum.matches' ↔ ∃ r ∈ rs, x ∈ r.matches'
```

`RegularExpression.iSup_matches'` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularExpressions.lean#L36))

```lean
theorem iSup_matches' {I : Type*} [Finite I] {s : Set I} {l : I → Language α}
    (h : ∀ i ∈ s, ∃ r : RegularExpression α, l i = r.matches') :
    ∃ r : RegularExpression α, (⨆ i ∈ s, l i) = r.matches'
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/RegularExpressions.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularExpressions.lean)
