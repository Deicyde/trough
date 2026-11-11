---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem997Wanted.WellDistributed, MathlibExt.NumberTheory.ErdosProblem997Wanted.primeFract, MathlibExt.NumberTheory.ErdosProblem997Wanted.Statement, MathlibExt.NumberTheory.ErdosProblem997Wanted.Statement_holds
statement: formalized
---

# Fractional parts of multiples of primes

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html).

## Well-distributed sequences

A sequence $(x_m)_{m \in \mathbb{N}}$ of real numbers is
well-distributed if for every $\varepsilon > 0$ there is a $K$ such that for all $k \ge K$, all
$n \in \mathbb{N}$ and all real numbers $a, b$ with $0 \le a \le b \le 1$, the number $N$ of
indices $m$ with $n < m \le n + k$ and $x_m \in [a, b)$ satisfies $|N - (b - a)k| < \varepsilon k$.

No condition $x_m \in [0, 1)$ is imposed, so finite changes to a sequence do not affect this
property.

## Sources

- EP-997 (Erdős Problem #997) [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem997Wanted.WellDistributed`, a definition declared in [WantedExt/NumberTheory/ErdosProblem997Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem997Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html#well-distributed).

## Fractional parts of multiples of the primes

For a real number $\alpha$, this is the
sequence taking $n \in \mathbb{N}$ to the fractional part $\{\alpha p_n\} = \alpha p_n -
\lfloor \alpha p_n \rfloor$, where $p_0 = 2, p_1 = 3, p_2 = 5, \dots$ are the primes in
increasing order.

## Sources

- EP-997 (Erdős Problem #997) [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem997Wanted.primeFract`, a definition declared in [WantedExt/NumberTheory/ErdosProblem997Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem997Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html#prime-fract).

## Statement of Erdős Problem 997

For every real number $\alpha$, the sequence
$n \mapsto \{\alpha p_n\}$ of fractional parts of $\alpha$ times the primes
$p_0 = 2, p_1 = 3, p_2 = 5, \dots$ is not well-distributed.

## Sources

- EP-997 (Erdős Problem #997) [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem997Wanted.Statement`, a definition declared in [WantedExt/NumberTheory/ErdosProblem997Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem997Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html#statement).

## Erdős Problem 997 holds

For every real number $\alpha$, the sequence
$n \mapsto \{\alpha p_n\}$ of fractional parts of $\alpha$ times the primes
$p_0 = 2, p_1 = 3, p_2 = 5, \dots$ is not well-distributed.

## Sources

- Boris Alexeev, Mark Putterman, Mehtaab Sawhney, Mark Sellke, and Gregory Valiant, Short proofs in combinatorics and number theory, arXiv:2603.29961 (2026), https://arxiv.org/abs/2603.29961. Resolved true: Alexeev, Putterman, Sawhney, Sellke, and Valiant proved that the prime-indexed fractional-part sequence is never well-distributed.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem997Wanted.Statement_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem997Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem997Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html#statement-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractional parts of multiples of primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/fractional-parts-of-multiples-of-primes)
