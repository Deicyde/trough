---
declaration: theorem
origin: cited
lean: KummerCriterion.normalizedCPlusGenerator_sq_eq_CPlusGenerator
statement: formalized
proof: formalized
---

# normalized-square

Each normalised generator squares to the corresponding standard generator:

$$
\xi_a^{\,2} = \varepsilon_a
\qquad (2 \le a \le (p-1)/2).
$$

## Depends on

- [CPlus](def-cplus.md)
- [normalizedCPlus](def-normalizedcplus.md)

## Proof

Using the identity $1-\zeta_p^{-a} = -\zeta_p^{-a}(1-\zeta_p^a)$ in the numerator and denominator of $\varepsilon_a$,

$$
\varepsilon_a
= \frac{(1-\zeta_p^a)\cdot\bigl(-\zeta_p^{-a}\bigr)(1-\zeta_p^a)}
{(1-\zeta_p)\cdot\bigl(-\zeta_p^{-1}\bigr)(1-\zeta_p)}
= \zeta_p^{\,1-a}\,\frac{(1-\zeta_p^a)^2}{(1-\zeta_p)^2}
= \xi_a^{\,2}.
$$

## Lean

Formalized as [`KummerCriterion.normalizedCPlusGenerator_sq_eq_CPlusGenerator`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.normalizedCPlusGenerator_sq_eq_CPlusGenerator).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 67](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L67)
