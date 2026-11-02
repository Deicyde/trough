---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.abc
mathlib_file: Mathlib/NumberTheory/FLT/MasonStothers.lean
---

# Mason–Stothers theorem

**Polynomial ABC theorem.**

```lean
Polynomial.abc.{u_1} {k : Type u_1} [Field k] [DecidableEq k] {a b c : Polynomial k} (ha : a ≠ 0)
  (hb : b ≠ 0) (hc : c ≠ 0) (hab : IsCoprime a b) (hsum : a + b + c = 0) :
  a.natDegree + 1 ≤ (UniqueFactorizationMonoid.radical (a * b * c)).natDegree ∧
      b.natDegree + 1 ≤ (UniqueFactorizationMonoid.radical (a * b * c)).natDegree ∧
        c.natDegree + 1 ≤ (UniqueFactorizationMonoid.radical (a * b * c)).natDegree ∨
    Polynomial.derivative a = 0 ∧ Polynomial.derivative b = 0 ∧ Polynomial.derivative c = 0
```

## Depends on

- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Coprime element](../../../overview/general-algebra/divisibility-in-integral-domains/coprime-element.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../../../overview/general-algebra/divisibility-in-integral-domains/least-common-multiple.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Polynomial.abc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html#Polynomial.abc)
- [Source of `Polynomial.abc` in Mathlib/NumberTheory/FLT/MasonStothers.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/FLT/MasonStothers.lean#L54)
- [1000+ theorems list: Q6783821](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3538)
- [1000+ theorems project: Q6783821](https://1000-plus.github.io/all.html?length=-1#Q6783821)
- [Wikipedia: Mason–Stothers theorem](https://en.wikipedia.org/wiki/Mason%E2%80%93Stothers_theorem)
- [Wikidata: Q6783821](https://www.wikidata.org/wiki/Q6783821)
