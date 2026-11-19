---
declaration: theorem
origin: cited
lean: KummerCriterion.h_eq_hPlus_mul_hMinus
statement: formalized
proof: formalized
---

# h-factorisation

The class number factors as

$$
h(K)=h^+(K)\,h^-(K).
$$

## Depends on

- [class-number-hminus](def-class-number-hminus.md)
- [hplus-divides-h](thm-hplus-divides-h.md)

## Proof

Multiply the defining quotient of [Definition class-number-hminus](def-class-number-hminus.md) by $h^+(K)$; this is legitimate in $\mathbb{N}$ because $h^+(K) \mid h(K)$ ([Theorem hplus-divides-h](thm-hplus-divides-h.md)) and $h^+(K) \ne 0$.

## Lean

Formalized as [`KummerCriterion.h_eq_hPlus_mul_hMinus`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.h_eq_hPlus_mul_hMinus).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 260](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L260)
