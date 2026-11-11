---
declaration: section
origin: cited
lean: ArithmeticFunction.alderTotientTwo, ArithmeticFunction.alderTotientTwo_succ_Iic_apply, ArithmeticFunction.alderTotientTwo_le_totient
statement: formalized
proof: formalized
---

# Alder's totient function

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function/index.html).

## Alder's totient with second argument 2

Alder's extension of Euler's totient with
second argument $2$ is the arithmetic function $g : \mathbb{N} \to \mathbb{N}$ sending a
natural number $k$ to the number of natural numbers $r < k$ with $\gcd(k, r) = 1$ and
$\gcd(k, 2r+1) = 1$. In particular $g(0) = 0$, since there is no natural number $r < 0$.

Formalized by `ArithmeticFunction.alderTotientTwo`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function/index.html#alder-totient-two).

## Alder's totient at a successor as a count over an inclusive range

For every natural
number $k$, Alder's totient $g$ with second argument $2$ satisfies that $g(k+1)$ is the number
of natural numbers $r \le k$ with $\gcd(r, k+1) = 1$ and $\gcd(2r+1, k+1) = 1$.

Formalized by `ArithmeticFunction.alderTotientTwo_succ_Iic_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function/index.html#alder-totient-two-succ-iic-apply).

## Alder's totient with second argument $2$ is at most Euler's totient

For every natural
number $k$, Alder's totient $g(k)$ with second argument $2$ is at most Euler's totient
$\varphi(k)$.

Formalized by `ArithmeticFunction.alderTotientTwo_le_totient`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/AlderTotient.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function/index.html#alder-totient-two-le-totient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alder's totient function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/alder-s-totient-function)
