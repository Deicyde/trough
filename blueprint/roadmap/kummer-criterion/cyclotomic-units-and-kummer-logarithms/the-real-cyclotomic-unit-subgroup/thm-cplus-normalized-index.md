---
declaration: theorem
origin: cited
lean: KummerCriterion.CPlus_index_prime_dvd_iff_normalizedCPlus_index_prime_dvd
statement: formalized
proof: formalized
---

# CPlus-normalized-index

For an odd prime $p$,

$$
p\mid[(\mathcal O_{K^+})^\times:C^+]
\Longleftrightarrow
p\mid[(\mathcal O_{K^+})^\times:C^+_{\mathrm{norm}}].
$$

## Depends on

- [normalized-square](thm-normalized-square.md)

## Proof

By [Theorem normalized-square](thm-normalized-square.md), $C^+ \subseteq C^+_{\mathrm{norm}}$ and every square of a normalised generator lies in $C^+$, so the quotient $C^+_{\mathrm{norm}}/C^+$ is an elementary abelian $2$-group of bounded rank; in particular the two indices differ by a power of $2$. Since $p$ is odd, multiplying or dividing by a power of $2$ does not affect $p$-divisibility.

## Lean

Formalized as [`KummerCriterion.CPlus_index_prime_dvd_iff_normalizedCPlus_index_prime_dvd`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CPlus_index_prime_dvd_iff_normalizedCPlus_index_prime_dvd).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 88](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L88)
