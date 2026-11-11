---
declaration: section
origin: cited
lean: MetaMathlibExt.ramanujanSum, MetaMathlibExt.ramanujanSum_zero, MetaMathlibExt.ramanujanSum_modulus_one, MetaMathlibExt.ramanujanSum_add_mul_modulus
statement: formalized
proof: formalized
---

# Ramanujan sums

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html).

## Ramanujan sum

For a positive integer $n$ and an integer $t$, the Ramanujan sum of modulus
$n$ at $t$ is the complex number

$$c_n(t) = \sum_{a \in (\mathbb{Z}/n\mathbb{Z})^\times} e^{2\pi i a t / n},$$

the sum over the units $a$ modulo $n$ of the standard additive character of $\mathbb{Z}/n\mathbb{Z}$
evaluated at $a t$.

Formalized by `MetaMathlibExt.ramanujanSum`, a definition declared in [MathlibExt/NumberTheory/RamanujanSum.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RamanujanSum.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html#ramanujan-sum).

## Ramanujan sum at zero

For every positive integer $n$, the Ramanujan sum $c_n(0)$ equals
Euler's totient $\varphi(n)$.

Formalized by `MetaMathlibExt.ramanujanSum_zero`, a theorem declared in [MathlibExt/NumberTheory/RamanujanSum.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RamanujanSum.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html#ramanujan-sum-zero).

## Ramanujan sums of modulus one

For every integer $t$, the Ramanujan sum $c_1(t)$ equals
$1$.

Formalized by `MetaMathlibExt.ramanujanSum_modulus_one`, a theorem declared in [MathlibExt/NumberTheory/RamanujanSum.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RamanujanSum.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html#ramanujan-sum-modulus-one).

## Periodicity of Ramanujan sums

For every positive integer $n$ and all integers $t$ and $k$,
the Ramanujan sum $c_n$ of modulus $n$ satisfies $c_n(t + kn) = c_n(t)$.

Formalized by `MetaMathlibExt.ramanujanSum_add_mul_modulus`, a theorem declared in [MathlibExt/NumberTheory/RamanujanSum.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RamanujanSum.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html#ramanujan-sum-add-mul-modulus).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/ramanujan-sums)
