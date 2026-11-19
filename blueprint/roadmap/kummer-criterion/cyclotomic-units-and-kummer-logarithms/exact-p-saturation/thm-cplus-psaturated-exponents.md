---
declaration: theorem
origin: cited
lean: KummerCriterion.CPlus_pSaturated_of_generator_exponents_modP_zero
statement: formalized
proof: formalized
---

# CPlus-pSaturated-exponents

Assume that whenever an exponent product

$$
(-1)^s\prod_a\varepsilon_a^{\,e_a}
$$

is a $p$th power in $E^+$, every exponent $e_a$ is divisible by $p$. Then $C^+$ is $p$-saturated in $E^+$.

## Depends on

- [pSaturated](def-psaturated.md)
- [exists-CPlusExponentProduct](thm-exists-cplusexponentproduct.md)

## Proof

Let $x \in C^+$ be a $p$th power in $E^+$, and write $x = (-1)^s \prod_a \varepsilon_a^{e_a}$ by [Theorem exists-CPlusExponentProduct](thm-exists-cplusexponentproduct.md). By hypothesis $p \mid e_a$ for every $a$. Since $p$ is odd, $(-1)^s = \bigl((-1)^s\bigr)^p$, so

$$
x = \Bigl((-1)^s\prod_a\varepsilon_a^{\,e_a/p}\Bigr)^{\!p}
$$

exhibits $x$ as the $p$th power of an element of $C^+$.

## Lean

Formalized as [`KummerCriterion.CPlus_pSaturated_of_generator_exponents_modP_zero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CPlus_pSaturated_of_generator_exponents_modP_zero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 163](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L163)
