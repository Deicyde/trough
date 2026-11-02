---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Language.isRegular_iff_finite_range_leftQuotient
mathlib_file: Mathlib/Computability/MyhillNerode.lean
---

# Myhill–Nerode theorem

**Myhill–Nerode theorem**. A language is regular if and only if the set of left quotients is finite.

```lean
Language.isRegular_iff_finite_range_leftQuotient.{u} {α : Type u} {L : Language α} :
  L.IsRegular ↔ (Set.range L.leftQuotient).Finite
```

## Depends on

- [Natural number](../../../../overview/general-algebra/numbers/natural-number.md)
- [Regular language](../../../../overview/logic-and-computation/formal-languages/regular-language.md)

## Sources

- [Mathlib documentation: `Language.isRegular_iff_finite_range_leftQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/MyhillNerode.html#Language.isRegular_iff_finite_range_leftQuotient)
- [Source of `Language.isRegular_iff_finite_range_leftQuotient` in Mathlib/Computability/MyhillNerode.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/MyhillNerode.lean#L102)
- [1000+ theorems list: Q422187](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L442)
- [1000+ theorems project: Q422187](https://1000-plus.github.io/all.html?length=-1#Q422187)
- [Wikipedia: Myhill–Nerode theorem](https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem)
- [Wikidata: Q422187](https://www.wikidata.org/wiki/Q422187)
