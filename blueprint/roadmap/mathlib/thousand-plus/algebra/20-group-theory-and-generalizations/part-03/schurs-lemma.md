---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.finrank_endomorphism_simple_eq_one
mathlib_file: Mathlib/CategoryTheory/Preadditive/Schur.lean
---

# Schur's lemma (1000+ theorems)

**Schur's lemma** for endomorphisms in `𝕜`-linear categories.

```lean
CategoryTheory.finrank_endomorphism_simple_eq_one.{v_1, u_1, u_2} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Preadditive C] (𝕜 : Type u_2) [Field 𝕜]
  [IsAlgClosed 𝕜] [CategoryTheory.Linear 𝕜 C] [CategoryTheory.Limits.HasKernels C] (X : C)
  [CategoryTheory.Simple X] [FiniteDimensional 𝕜 (X ⟶ X)] : Module.finrank 𝕜 (X ⟶ X) = 1
```

## Depends on

- [Algebraically closed field](../../../../overview/general-algebra/field-theory/algebraically-closed-field.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Limits](../../../../overview/general-algebra/category-theory/limits.md)
- [Linear independence](../../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Small category](../../../../overview/general-algebra/category-theory/small-category.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Local ring](../../../../overview/general-algebra/rings/local-ring.md)

## Sources

- [Mathlib documentation: `CategoryTheory.finrank_endomorphism_simple_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Preadditive/Schur.html#CategoryTheory.finrank_endomorphism_simple_eq_one)
- [Source of `CategoryTheory.finrank_endomorphism_simple_eq_one` in Mathlib/CategoryTheory/Preadditive/Schur.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Preadditive/Schur.lean#L127)
- [1000+ theorems list: Q1816952](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1909)
- [1000+ theorems project: Q1816952](https://1000-plus.github.io/all.html?length=-1#Q1816952)
- [Wikipedia: Schur's lemma](https://en.wikipedia.org/wiki/Schur's_lemma)
- [Wikidata: Q1816952](https://www.wikidata.org/wiki/Q1816952)
