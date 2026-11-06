---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PythagoreanTriple.classification
mathlib_file: Mathlib/NumberTheory/PythagoreanTriples.lean
---

# Formula for Pythagorean Triples

**Formula for Pythagorean Triples**

```lean
PythagoreanTriple.classification {x y z : ℤ} :
  PythagoreanTriple x y z ↔
    ∃ k m n,
      (x = k * (m ^ 2 - n ^ 2) ∧ y = k * (2 * m * n) ∨
          x = k * (2 * m * n) ∧ y = k * (m ^ 2 - n ^ 2)) ∧
        (z = k * (m ^ 2 + n ^ 2) ∨ z = -k * (m ^ 2 + n ^ 2))
```

## Depends on

- [Integer](../../overview/general-algebra/numbers/integer.md)

## Proof depends on

- [$\Z$ is a Euclidean ring](../../undergraduate/ring-theory/divisibility-in-integral-domains/z-is-a-euclidean-ring.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\Q$ of rational numbers](../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `PythagoreanTriple.classification`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/PythagoreanTriples.html#PythagoreanTriple.classification)
- [Source of `PythagoreanTriple.classification` in Mathlib/NumberTheory/PythagoreanTriples.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/PythagoreanTriples.lean#L604)
- [Freek Wiedijk's 100 theorems, no. 23](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L112)
