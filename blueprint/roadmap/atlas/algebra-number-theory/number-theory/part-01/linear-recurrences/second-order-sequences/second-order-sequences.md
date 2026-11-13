---
declaration: section
origin: cited
lean: MetaMathlibExt.associated_pell_cassini_identity
statement: formalized
proof: formalized
---

# Pell, Jacobsthal and other second-order sequences: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/index.html).

Pell, Pell–Lucas, Jacobsthal, gibonacci, Horadam, Leonardo, Oresme, bi-periodic and (a,b)-Fibonacci sequences.

## Cassini's identity for associated Pell numbers

Let $(Q_n)_{n \ge 0}$ be a sequence of
integers with $Q_0 = Q_1 = 1$ and $Q_{n+2} = 2Q_{n+1} + Q_n$ for every $n \ge 0$. Then for every
natural number $k \ge 1$,

$$Q_{k-1} Q_{k+1} = Q_k^2 + 2(-1)^{k-1}.$$

## Sources

- aBa Mbirika, Janee Schrader, and Jürgen Spilker, "Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers," Journal of Integer Sequences 26 (2023), Article 23.6.4, Lemma [Cassini's identity for Q].

Formalized by `MetaMathlibExt.associated_pell_cassini_identity`, a theorem declared in [MathlibExt/NumberTheory/AssociatedPellCassini.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/AssociatedPellCassini.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/index.html#associated-pell-cassini-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell, Jacobsthal and other second-order sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences)
