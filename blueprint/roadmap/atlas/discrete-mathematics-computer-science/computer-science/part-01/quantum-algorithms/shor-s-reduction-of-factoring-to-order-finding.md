---
declaration: section
origin: cited
lean: Cslib.Shor.gcd_factor_of_order, Cslib.Shor.exists_factor_of_order
statement: formalized
proof: formalized
---

# Shor's reduction of factoring to order finding

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/shor-s-reduction-of-factoring-to-order-finding/index.html).

## Shor's order-to-factor reduction

Let $N$, $a$ and $r$ be natural numbers with $N > 1$ and
$a \ge 1$. Suppose $a^r \equiv 1 \pmod{N}$, $r$ is even, $a^{r/2} \not\equiv 1 \pmod{N}$ and
$a^{r/2} \not\equiv -1 \pmod{N}$. Then $d = \gcd(a^{r/2} - 1, N)$, the value computed by the
classical post-processing, is a nontrivial factor of $N$: $d$ divides $N$ and $1 < d < N$.

In the algorithm $r$ is the multiplicative order of $a$ modulo $N$, so the hypothesis
$a^{r/2} \not\equiv 1 \pmod{N}$ is the minimality of the order, and the hypothesis
$a^{r/2} \not\equiv -1 \pmod{N}$ is the "good unit" condition. This module assumes that
condition; it does not prove its prevalence among units.

## Sources

- P. W. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer, SIAM J. Comput. 26 (1997), 1484–1509, Section 5; M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Section 5.3.

Formalized by `Cslib.Shor.gcd_factor_of_order`, a theorem declared in [CSLibExt/Algorithms/Quantum/Shor/OrderToFactor.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Shor/OrderToFactor.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/shor-s-reduction-of-factoring-to-order-finding/index.html#gcd-factor-of-order).

## Shor's order-to-factor reduction, existential form

Let $N$, $a$ and $r$ be natural
numbers with $N > 1$ and $a \ge 1$. If $a^r \equiv 1 \pmod{N}$, $r$ is even,
$a^{r/2} \not\equiv 1 \pmod{N}$ and $a^{r/2} \not\equiv -1 \pmod{N}$, then $N$ has a nontrivial
factor: there is a natural number $d$ with $d \mid N$ and $1 < d < N$.

One such factor is $\gcd(a^{r/2} - 1, N)$.

Formalized by `Cslib.Shor.exists_factor_of_order`, a theorem declared in [CSLibExt/Algorithms/Quantum/Shor/OrderToFactor.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Shor/OrderToFactor.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/shor-s-reduction-of-factoring-to-order-finding/index.html#exists-factor-of-order).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shor's reduction of factoring to order finding](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/shor-s-reduction-of-factoring-to-order-finding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/quantum-algorithms/shor-s-reduction-of-factoring-to-order-finding)
