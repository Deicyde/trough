---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Pell.matiyasevic
mathlib_file: Mathlib/NumberTheory/PellMatiyasevic.lean
---

# Matiyasevič's theorem

Mathlib states this as `Pell.matiyasevic`.

```lean
Pell.matiyasevic {a k x y : ℕ} :
  (∃ (a1 : 1 < a), Pell.xn a1 k = x ∧ Pell.yn a1 k = y) ↔
    1 < a ∧
      k ≤ y ∧
        (x = 1 ∧ y = 0 ∨
          ∃ u v s t b,
            x * x - (a * a - 1) * y * y = 1 ∧
              u * u - (a * a - 1) * v * v = 1 ∧
                s * s - (b * b - 1) * t * t = 1 ∧
                  1 < b ∧
                    b ≡ 1 [MOD 4 * y] ∧
                      b ≡ a [MOD u] ∧ 0 < v ∧ y * y ∣ v ∧ s ≡ x [MOD u] ∧ t ≡ k [MOD 4 * y])
```

## Depends on

- [Solutions to Pell's equation (Number theory)](solutions-to-pells-equation.md)

## Proof depends on

- [Euclid's' algorithm](../divisibility-in-integral-domains/euclids-algorithm.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Solutions to Pell’s Equation (Freek Wiedijk's 100 theorems)](../../../hundred-theorems/part-02/solutions-to-pells-equation.md)

## Sources

- [Mathlib documentation: `Pell.matiyasevic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/PellMatiyasevic.html#Pell.matiyasevic)
- [Source of `Pell.matiyasevic` in Mathlib/NumberTheory/PellMatiyasevic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/PellMatiyasevic.lean#L761)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L146)
- [1000+ theorems list: Q16251580](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L4085)
- [1000+ theorems project: Q16251580](https://1000-plus.github.io/all.html?length=-1#Q16251580)
- [Wikipedia: Matiyasevich's theorem](https://en.wikipedia.org/wiki/Matiyasevich's_theorem)
- [Wikidata: Q16251580](https://www.wikidata.org/wiki/Q16251580)
