---
declaration: section
origin: cited
lean: MetaMathlibExt.subsequence_secondOrderRecurrence
statement: formalized
---

# Recurrences modulo m: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/index.html).

Pisano periods, periods and zero indices of recurrences modulo primes and prime powers, residue distribution.

## Subsequences of a second-order linear recurrence

Let $(P, Q)$ be Lucas sequence
parameters (integers with $Q \ne 0$), let $U_n$ and $V_n$ be the terms of the Lucas sequence
$U(P, Q)$ and of the companion Lucas sequence $V(P, Q)$, and let $(w_n)_{n \ge 0}$ be an integer
sequence with $w_{n+2} = P w_{n+1} - Q w_n$ for every natural number $n$. Then for all natural
numbers $t > 0$ and $r$, the subsequence $w'_n = w_{tn + r}$ satisfies
$w'_{n+2} = V_t w'_{n+1} - Q^t w'_n$ for every natural number $n$, and
$V_t^2 - 4 Q^t = U_t^2 (P^2 - 4Q)$.

The source writes the recurrence as $w_{n+2} = a w_{n+1} + b w_n$,
with subsequence coefficients $a' = V_t$ and $b' = (-1)^{t+1} b^t$ and discriminant
$D(a, b) = a^2 + 4b$; this is the statement above with $P = a$ and $Q = -b$. The source's
identification of the characteristic roots of the new recurrence as $\alpha^t$ and $\beta^t$ is
not part of this statement.

## Sources

- Somer and Křížek, *Generalization of a Theorem of Vélez on Uniform Distribution in Second-Order Linear Recurrences*, INTEGERS 25 (2025), Article A1, Theorem 2.4.

Stated but not proved: `MetaMathlibExt.subsequence_secondOrderRecurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/VelezUniformDistributionWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/VelezUniformDistributionWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/index.html#subsequence-second-order-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recurrences modulo m](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m)
