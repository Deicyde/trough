---
declaration: section
origin: cited
lean: MetaMathlibExt.stormer_theorem
statement: formalized
proof: formalized
---

# Exponential Diophantine equations: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/index.html).

Equations with unknown exponents: Pillai, Catalan, Størmer, Nagell–Ljunggren, Ramanujan–Nagell and Terai-type equations, powers plus one.

## Størmer's theorem

For every natural number $y \ge 2$, there is a finite set $S$ of
pairs of natural numbers such that, for every positive integer $n$ such that all prime factors
of $n$ and all prime factors of $n + 1$ are at most $y$, the pair $(n, n + 1)$ lies in $S$.

## Sources

- https://en.wikipedia.org/wiki/St%C3%B8rmer%27s_theorem.

Formalized by `MetaMathlibExt.stormer_theorem`, a theorem declared in [MathlibExt/NumberTheory/Stormer.lean, line 552](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Stormer.lean#L552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/index.html#stormer-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential Diophantine equations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/exponential-diophantine)
