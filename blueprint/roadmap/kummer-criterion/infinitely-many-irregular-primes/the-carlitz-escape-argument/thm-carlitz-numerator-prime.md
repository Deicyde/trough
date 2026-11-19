---
declaration: theorem
origin: cited
lean: KummerCriterion.exists_numerator_prime_for_carlitz_base
statement: formalized
proof: formalized
---

# carlitz-numerator-prime

For every finite set $S$ of natural numbers there are $M$ and a prime $p$ such that $M$ is even and positive, $(q-1)\mid M$ for every prime $q \in S$, the prime $p$ is odd, $p\mid\operatorname{num}(B_M/M)$, and $p \notin S$.

## Depends on

- [irregular-base](../the-divisor-closed-multiplier/def-irregular-base.md)
- [irregular-base-mem](../the-divisor-closed-multiplier/lem-irregular-base-mem.md)
- [irregular-base-closed](../the-divisor-closed-multiplier/lem-irregular-base-closed.md)
- [bernoulli-large-multiple](../growth-of-divided-bernoulli-numbers/cor-bernoulli-large-multiple.md)
- [num-prime-of-large](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-prime-of-large.md)
- [vonstaudt-not-dvd-divided](../numerators-p-adic-congruences-and-von-staudt-cla/thm-vonstaudt-not-dvd-divided.md)

## Proof

Put $M = C(S)\cdot 2^t$ with $t$ chosen by [Corollary bernoulli-large-multiple](../growth-of-divided-bernoulli-numbers/cor-bernoulli-large-multiple.md) so that $|B_M/M| > 1$. By [Lemma num-prime-of-large](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-prime-of-large.md) some prime $p$ divides $\operatorname{num}(B_M/M)$. By [Theorem vonstaudt-not-dvd-divided](../numerators-p-adic-congruences-and-von-staudt-cla/thm-vonstaudt-not-dvd-divided.md), $(p-1)\nmid M$; in particular $p \ne 2$. If $p$ were in $S$, then $(p-1)\mid C(S)\mid M$ by [Lemma irregular-base-mem](../the-divisor-closed-multiplier/lem-irregular-base-mem.md), a contradiction; so $p \notin S$. The divisibility $(q-1)\mid M$ for $q \in S$ is again [Lemma irregular-base-mem](../the-divisor-closed-multiplier/lem-irregular-base-mem.md).

## Lean

Formalized as [`KummerCriterion.exists_numerator_prime_for_carlitz_base`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_numerator_prime_for_carlitz_base).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 289](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L289)
