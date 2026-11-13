---
declaration: section
origin: cited
lean: MetaMathlibExt.IsNicolNumber, MetaMathlibExt.IsTNicolNumber, MetaMathlibExt.IsTNicolNumber.isNicolNumber
statement: formalized
proof: formalized
---

# Nicol numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers/index.html).

## Nicol numbers

A Nicol number is a positive integer $n$ that divides
$\varphi(n) + \sigma(n)$, where $\varphi$ is Euler's totient function and $\sigma(n)$ is the sum
of the positive divisors of $n$.

## Sources

- JIS VOL14/Tang, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Tang2/tang72.tex>, lines 77–90.

Formalized by `MetaMathlibExt.IsNicolNumber`, a definition declared in [MathlibExt/NumberTheory/NicolNumber.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NicolNumber.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers/index.html#is-nicol-number).

## $t$-Nicol numbers

For a natural number $t$, a $t$-Nicol number is a positive integer $n$
such that $\varphi(n) + \sigma(n) = t n$, where $\varphi$ is Euler's totient function and
$\sigma(n)$ is the sum of the positive divisors of $n$.

Formalized by `MetaMathlibExt.IsTNicolNumber`, a definition declared in [MathlibExt/NumberTheory/NicolNumber.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NicolNumber.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers/index.html#is-tnicol-number).

## Every $t$-Nicol number is a Nicol number

For all natural numbers $t$ and $n$, if $n$ is a
$t$-Nicol number, then $n$ is a Nicol number.

Formalized by `MetaMathlibExt.IsTNicolNumber.isNicolNumber`, a theorem declared in [MathlibExt/NumberTheory/NicolNumber.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NicolNumber.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers/index.html#is-nicol-number-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nicol numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/nicol-numbers)
