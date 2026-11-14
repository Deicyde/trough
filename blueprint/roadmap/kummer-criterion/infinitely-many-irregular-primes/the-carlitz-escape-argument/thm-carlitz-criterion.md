---
declaration: theorem
origin: cited
lean: KummerCriterion.not_isRegularPrime_iff_exists_dvd_bernoulli_div_self_num
statement: formalized
proof: formalized
---

# carlitz-criterion

An odd prime $p$ is irregular if and only if $p \mid \operatorname{num}(B_m/m)$ for some positive even index $m$.

## Depends on

- [irregular-of-bernoulli-witness](../from-bernoulli-numerators-to-irregular-primes/thm-irregular-of-bernoulli-witness.md)
- [bernoulli-witness-of-irregular](../from-bernoulli-numerators-to-irregular-primes/thm-bernoulli-witness-of-irregular.md)
- [kummer-congruence-full](../the-unrestricted-kummer-congruence/thm-kummer-congruence-full.md)
- [vonstaudt-not-dvd-divided](../numerators-p-adic-congruences-and-von-staudt-cla/thm-vonstaudt-not-dvd-divided.md)
- [num-transport](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-transport.md)
- [num-of-divided](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-of-divided.md)
- [positive-residue](lem-positive-residue.md)

## Proof

If $p$ is irregular, [Theorem bernoulli-witness-of-irregular](../from-bernoulli-numerators-to-irregular-primes/thm-bernoulli-witness-of-irregular.md) produces a witness $B_{2k}$ in Kummer's range; since $2k \le p-3 < p$, the index is a unit modulo $p$ and the divisibility passes to the divided numerator.

Conversely, suppose $p\mid\operatorname{num}(B_m/m)$ with $m$ positive and even. By [Theorem vonstaudt-not-dvd-divided](../numerators-p-adic-congruences-and-von-staudt-cla/thm-vonstaudt-not-dvd-divided.md), necessarily $(p-1)\nmid m$. Let $m'$ be the positive residue of [Lemma positive-residue](lem-positive-residue.md). The full Kummer congruence ([Theorem kummer-congruence-full](../the-unrestricted-kummer-congruence/thm-kummer-congruence-full.md)) gives $B_m/m \equiv B_{m'}/m' \pmod p$, so $p\mid\operatorname{num}(B_{m'}/m')$ by [Lemma num-transport](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-transport.md), hence $p \mid \operatorname{num}(B_{m'})$ by [Lemma num-of-divided](../numerators-p-adic-congruences-and-von-staudt-cla/lem-num-of-divided.md). Since $2 \le m' \le p-3$ and $m'$ is even, this is a Bernoulli witness in Kummer's range, and $p$ is irregular by [Theorem irregular-of-bernoulli-witness](../from-bernoulli-numerators-to-irregular-primes/thm-irregular-of-bernoulli-witness.md).

## Lean

Formalized as [`KummerCriterion.not_isRegularPrime_iff_exists_dvd_bernoulli_div_self_num`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_isRegularPrime_iff_exists_dvd_bernoulli_div_self_num).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 265](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L265)
