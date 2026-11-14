---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulli_div_sModEq_of_modEq_full_geFive
statement: formalized
proof: formalized
---

# kummer-congruence-gefive

Let $p \ge 5$ be a prime and $m, n$ positive even indices with $m \equiv n \pmod{p-1}$ and $(p-1)\nmid n$. Then

$$
\frac{B_m}{m} \;\equiv\; \frac{B_n}{n} \pmod{p}.
$$

## Depends on

- [voronoi-congruence](thm-voronoi-congruence.md)

## Proof

Choose a primitive root $a$ modulo $p$ and apply [Theorem voronoi-congruence](thm-voronoi-congruence.md) to both indices. Since $m \equiv n \pmod{p-1}$, Fermat's little theorem gives $a^m \equiv a^n$ and $j^{m-1}\equiv j^{n-1} \pmod p$ for all $j$, so the two Voronoi sums agree modulo $p$. Subtracting the two instances yields $(a^{n}-1)\bigl(B_m/m - B_n/n\bigr) \equiv 0 \pmod p$, and because $a$ is a primitive root with $(p-1)\nmid n$ the factor $a^{n}-1$ is a $p$-adic unit, giving the congruence.

## Lean

Formalized as [`KummerCriterion.bernoulli_div_sModEq_of_modEq_full_geFive`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulli_div_sModEq_of_modEq_full_geFive).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 217](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L217)
