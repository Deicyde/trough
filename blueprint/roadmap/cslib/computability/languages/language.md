---
catalog: module
lean: List.eq_nil_ofIsEmpty, Language.eq_zero_or_one_ofIsEmpty, Language.mem_biInf, Language.mem_biSup, Language.le_one_iff_eq, Language.mem_singleton, Language.mem_sub_one, Language.reverse_sub, Language.sub_one_mul, Language.mul_sub_one, Language.kstar_sub_one, Language.sub_one_kstar, Language.kstar_iff_mul_add, Language.self_eq_add_mul_iff
statement: formalized
proof: formalized
---

# Language (additional definitions and theorems)

`Cslib.Computability.Languages.Language`, in [Cslib/Computability/Languages/Language.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean), by Ching-Tsun Chou.

> This file contains additional definitions and theorems about `Language`
> as defined and developed in `Mathlib.Computability.Language`.

`List.eq_nil_ofIsEmpty` (theorem, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L26))

> `[]` is the only list over an empty type.

```lean
theorem eq_nil_ofIsEmpty [IsEmpty α] (xl : List α) : xl = []
```

`Language.eq_zero_or_one_ofIsEmpty` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L40))

> `0` and `1` are the only possible languages over an empty type.

```lean
theorem eq_zero_or_one_ofIsEmpty [IsEmpty α] (l : Language α) : l = 0 ∨ l = 1
```

`Language.mem_biInf` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L51))

```lean
theorem mem_biInf {I : Type*} (s : Set I) (l : I → Language α) (x : List α) :
    (x ∈ ⨅ i ∈ s, l i) ↔ ∀ i ∈ s, x ∈ l i
```

`Language.mem_biSup` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L58))

> A grind regression found moving to nightly-2026-03-31 (changes from lean#13166)

```lean
theorem mem_biSup {I : Type*} (s : Set I) (l : I → Language α) (x : List α) :
    (x ∈ ⨆ i ∈ s, l i) ↔ ∃ i ∈ s, x ∈ l i
```

`Language.le_one_iff_eq` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L63))

```lean
theorem le_one_iff_eq : l ≤ 1 ↔ l = 0 ∨ l = 1
```

`Language.mem_singleton` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L67))

```lean
theorem mem_singleton (x y : List α) : x ∈ ({y} : Language α) ↔ x = y
```

`Language.mem_sub_one` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L71))

```lean
theorem mem_sub_one (x : List α) : x ∈ (l - 1) ↔ x ∈ l ∧ x ≠ []
```

`Language.reverse_sub` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L75))

```lean
theorem reverse_sub (l m : Language α) : (l - m).reverse = l.reverse - m.reverse
```

`Language.sub_one_mul` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L81))

> A grind regression found moving to nightly-2026-03-31 (changes from lean#13166)

```lean
theorem sub_one_mul : (l - 1) * l = l * l - 1
```

`Language.mul_sub_one` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L97))

```lean
theorem mul_sub_one : l * (l - 1) = l * l - 1
```

`Language.kstar_sub_one` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L107))

> A grind regression found moving to nightly-2026-03-31 (changes from lean#13166)

```lean
theorem kstar_sub_one : l∗ - 1 = (l - 1) * l∗
```

`Language.sub_one_kstar` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L122))

```lean
theorem sub_one_kstar : (l - 1)∗ = l∗
```

`Language.kstar_iff_mul_add` (theorem, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L127))

```lean
theorem kstar_iff_mul_add : m = l∗ ↔ m = (l - 1) * m + 1
```

`Language.self_eq_add_mul_iff` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean#L132))

> The reverse version of Arden's lemma `Language.self_eq_mul_add_iff`.

```lean
theorem self_eq_add_mul_iff {l m n : Language α} (hm : [] ∉ m) :
    l = l * m + n ↔ l = n * m∗
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/Language.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Language.lean)
