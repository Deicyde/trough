---
declaration: theorem
origin: cited
lean: KummerCriterion.dvd_h_iff_dvd_hMinus_of_dvd_hPlus_imp
statement: formalized
proof: formalized
---

# dvd-h-iff-dvd-hminus-from-plus-to-minus

Assume that a separate argument proves the implication

$$
p\mid h^+(K)\Longrightarrow p\mid h^-(K).
$$

Then

$$
p\mid h(K)\Longleftrightarrow p\mid h^-(K).
$$

## Depends on

- [h-factorisation](thm-h-factorisation.md)

## Proof

Write $h(K) = h^+(K)\,h^-(K)$ by [Theorem h-factorisation](thm-h-factorisation.md). If $p \mid h(K)$, then by primality $p\mid h^+(K)$ or $p\mid h^-(K)$, and the first alternative implies the second by hypothesis; either way $p \mid h^-(K)$. Conversely $h^-(K)$ divides $h(K)$, so $p \mid h^-(K)$ implies $p \mid h(K)$.

## Lean

Formalized as [`KummerCriterion.dvd_h_iff_dvd_hMinus_of_dvd_hPlus_imp`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.dvd_h_iff_dvd_hMinus_of_dvd_hPlus_imp).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 274](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L274)
