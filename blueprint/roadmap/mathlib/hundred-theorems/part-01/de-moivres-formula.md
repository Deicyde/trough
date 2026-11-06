# De Moivre’s Formula

**De Moivre's formula**

```lean
Complex.cos_add_sin_mul_I_pow (n : ℕ) (z : ℂ) :
  (Complex.cos z + Complex.sin z * Complex.I) ^ n =
    Complex.cos (↑n * z) + Complex.sin (↑n * z) * Complex.I
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md)

## Sources

- [Mathlib documentation: `Complex.cos_add_sin_mul_I_pow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Trigonometric.html#Complex.cos_add_sin_mul_I_pow)
- [Source of `Complex.cos_add_sin_mul_I_pow` in Mathlib/Analysis/Complex/Trigonometric.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Trigonometric.lean#L541)
- [Freek Wiedijk's 100 theorems, no. 17](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L87)
- [1000+ theorems list: Q190556](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L147)
- [1000+ theorems project: Q190556](https://1000-plus.github.io/all.html?length=-1#Q190556)
- [Wikipedia: De Moivre's formula](https://en.wikipedia.org/wiki/De_Moivre's_formula)
- [Wikidata: Q190556](https://www.wikidata.org/wiki/Q190556)
