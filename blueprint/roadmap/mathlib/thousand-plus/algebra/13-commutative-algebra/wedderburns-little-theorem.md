# Wedderburn's little theorem

A finite division ring is a field. See `Finite.isDomain_to_isField` and
`Fintype.divisionRingOfIsDomain` for more general statements, but these create data, and therefore
may cause diamonds if used improperly.

```lean
littleWedderburn.{u_1} (D : Type u_1) [DivisionRing D] [Finite D] : Field D
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)

## Sources

- [Mathlib documentation: `littleWedderburn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/LittleWedderburn.html#littleWedderburn)
- [Source of `littleWedderburn` in Mathlib/RingTheory/LittleWedderburn.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/LittleWedderburn.lean#L166)
- [1000+ theorems list: Q943246](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1127)
- [1000+ theorems project: Q943246](https://1000-plus.github.io/all.html?length=-1#Q943246)
- [Wikipedia: Wedderburn's little theorem](https://en.wikipedia.org/wiki/Wedderburn's_little_theorem)
- [Wikidata: Q943246](https://www.wikidata.org/wiki/Q943246)
