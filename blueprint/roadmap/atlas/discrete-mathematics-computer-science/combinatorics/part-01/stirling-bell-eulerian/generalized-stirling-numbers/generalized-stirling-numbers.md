---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedStirlingFirst, MetaMathlibExt.generalizedStirlingSecond, MetaMathlibExt.generalizedStirlingFirst_eq_sum, MetaMathlibExt.generalizedStirlingSecond_eq_sum
statement: formalized
proof: formalized
---

# Generalized Stirling numbers: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html).

Deformations and generalizations of Stirling numbers: r-Stirling, associated Stirling, Hsu–Shiue, Jacobi–Stirling, Legendre–Stirling, meromorphic and degenerate Stirling numbers, α-Stirling and generalized Stirling matrices, and (q,r)-Whitney and Dowling numbers.

## Generalized Stirling numbers of the first kind

For natural numbers $n$, $m$ and a real
number $x$, the generalized Stirling number of the first kind is

$${n \brack m}_x = \sum_{i=0}^{n-m} \binom{i+m}{m} {n \brack i+m} x^i,$$

where ${n \brack k}$ is the unsigned Stirling number of the first kind, the number of permutations
of $n$ elements with exactly $k$ cycles. For $m > n$ the sum consists of the single term $i = 0$,
which is ${n \brack m} = 0$, so ${n \brack m}_x = 0$.

## Sources

- Carlitz and Broder, as recorded in Cereceda, arXiv:2401.13696v4, lines 132-142; Axioms 14 (2025), 746.

Formalized by `MetaMathlibExt.generalizedStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html#generalized-stirling-first).

## Generalized Stirling numbers of the second kind

For natural numbers $n$, $m$ and a real
number $x$, the generalized Stirling number of the second kind is

$${n \brace m}_x = \sum_{i=0}^{n-m} \binom{n}{i} {n-i \brace m} x^i,$$

where ${n \brace k}$ is the Stirling number of the second kind, the number of partitions of an
$n$-element set into $k$ nonempty blocks. For $m > n$ the sum consists of the single term $i = 0$,
which is $\binom{n}{0} {n \brace m} = 0$, so ${n \brace m}_x = 0$.

## Sources

- Carlitz and Broder, as recorded in Cereceda, arXiv:2401.13696v4, lines 132-142; Axioms 14 (2025), 746.

Formalized by `MetaMathlibExt.generalizedStirlingSecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html#generalized-stirling-second).

## Sum formula for generalized Stirling numbers of the first kind

For natural numbers
$m \le n$ and every real number $x$, the generalized Stirling number of the first kind satisfies

$${n \brack m}_x = \sum_{i=0}^{n-m} \binom{i+m}{m} {n \brack i+m} x^i,$$

where ${n \brack k}$ is the unsigned Stirling number of the first kind; the sum includes both
endpoints $i = 0$ and $i = n - m$.

## Sources

- Cereceda, arXiv:2401.13696v4, lines 132-142.

Formalized by `MetaMathlibExt.generalizedStirlingFirst_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html#generalized-stirling-first-eq-sum).

## Sum formula for generalized Stirling numbers of the second kind

For natural numbers
$m \le n$ and every real number $x$, the generalized Stirling number of the second kind satisfies

$${n \brace m}_x = \sum_{i=0}^{n-m} \binom{n}{i} {n-i \brace m} x^i,$$

where ${n \brace k}$ is the Stirling number of the second kind; the sum includes both endpoints
$i = 0$ and $i = n - m$.

## Sources

- Cereceda, arXiv:2401.13696v4, lines 132-142.

Formalized by `MetaMathlibExt.generalizedStirlingSecond_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingNumbers.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html#generalized-stirling-second-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers)
