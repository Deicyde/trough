---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Pell.eq_pell, Pell.exists_of_not_isSquare
mathlib_file: Mathlib/NumberTheory/PellMatiyasevic.lean
---

# Solutions to Pell’s Equation

Mathlib records this with 2 declarations.

`Pell.eq_pell`: Every solution to **Pell's equation** is recursively obtained from the initial solution
`(1,0)` using the recursion `pell`.

```lean
Pell.eq_pell {a : ℕ} (a1 : 1 < a) {x y : ℕ} (hp : x * x - Pell.d✝ a1 * y * y = 1) :
  ∃ n, x = Pell.xn a1 n ∧ y = Pell.yn a1 n
```

`Pell.exists_of_not_isSquare`: If `d` is a positive integer that is not a square, then there is a nontrivial solution
to the Pell equation `x^2 - d*y^2 = 1`.

```lean
Pell.exists_of_not_isSquare {d : ℤ} (h₀ : 0 < d) (hd : ¬IsSquare d) :
  ∃ x y, x ^ 2 - d * y ^ 2 = 1 ∧ y ≠ 0
```

In `pell.eq_pell`, `d` is defined to be `a*a - 1` for an arbitrary `a > 1`.

## Depends on

- [Integer](../../overview/general-algebra/numbers/integer.md)
- [Solutions to Pell's equation](../../overview/general-algebra/number-theory/solutions-to-pells-equation.md)

## Proof depends on

- [Congruence in $\Z$](../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Dirichlet's approximation theorem](../../thousand-plus/number-theory/part-02/dirichlets-approximation-theorem.md)

## Sources

- [Mathlib documentation: `Pell.eq_pell`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/PellMatiyasevic.html#Pell.eq_pell)
- [Source of `Pell.eq_pell` in Mathlib/NumberTheory/PellMatiyasevic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/PellMatiyasevic.lean#L323)
- [Mathlib documentation: `Pell.exists_of_not_isSquare`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html#Pell.exists_of_not_isSquare)
- [Source of `Pell.exists_of_not_isSquare` in Mathlib/NumberTheory/Pell.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Pell.lean#L322)
- [Freek Wiedijk's 100 theorems, no. 39](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L203)
- [1000+ theorems list: Q853067](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L980)
- [1000+ theorems project: Q853067](https://1000-plus.github.io/?length=-1#Q853067)
- [Wikipedia: Pell's equation](https://en.wikipedia.org/wiki/Pell's_equation)
- [Wikidata: Q853067](https://www.wikidata.org/wiki/Q853067)
