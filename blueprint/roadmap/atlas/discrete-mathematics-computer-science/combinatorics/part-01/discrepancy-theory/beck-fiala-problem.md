---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LinearBeckFialaWanted.conjecture, MathlibExt.Combinatorics.LinearBeckFialaWanted.conjecture_holds
statement: formalized
---

# Beck–Fiala problem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/beck-fiala-problem/index.html).

## Linear Beck–Fiala conjecture

This is the statement that there is a real constant
$C > 0$ such that the following holds for all natural numbers $n$, $m$ and $t \ge 1$. Let
$S_1, \dots, S_n$ be subsets of $\{1, \dots, m\}$ such that each $S_i$ has at most $t$ elements,
each element of $\{1, \dots, m\}$ lies in at most $t$ of the sets $S_i$, and $S_i$ and $S_{i'}$
have at most one common element whenever $i \ne i'$. Then there are signs
$\varepsilon_1, \dots, \varepsilon_m \in \{1, -1\}$ such that
$\left|\sum_{j \in S_i} \varepsilon_j\right| \le C\sqrt{t}$ for every $i$.

In matrix terms: a $t$-sparse $0/1$ matrix (in rows and columns) in which every two rows share
at most one nonzero entry has discrepancy $O(\sqrt{t})$, improving the general bound
$O(\sqrt{t \log t})$.

## Sources

- AIM-COMBINATORICS-0044__20000919; AIM Hereditary discrepancy, item 1.7.

Formalized by `MathlibExt.Combinatorics.LinearBeckFialaWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/LinearBeckFialaWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearBeckFialaWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/beck-fiala-problem/index.html#conjecture).

## Linear Beck–Fiala systems have discrepancy $O(\sqrt{t})$

There is a real constant $C > 0$
such that the following holds for all natural numbers $n$, $m$ and $t \ge 1$. Let
$S_1, \dots, S_n$ be subsets of $\{1, \dots, m\}$ such that each $S_i$ has at most $t$ elements,
each element of $\{1, \dots, m\}$ lies in at most $t$ of the sets $S_i$, and $S_i$ and $S_{i'}$
have at most one common element whenever $i \ne i'$. Then there are signs
$\varepsilon_1, \dots, \varepsilon_m \in \{1, -1\}$ such that
$\left|\sum_{j \in S_i} \varepsilon_j\right| \le C\sqrt{t}$ for every $i$.

Guo, Fang and Lu prove that every $0/1$ matrix with at most $t$ nonzero entries in each column
has discrepancy less than $3\sqrt{2\pi t}$ (arXiv:2609.11189, Corollary 1.2 of their Komlós
bound, Theorem 1.1; Karingula and Lovett give an elementary proof of the Komlós bound with
constant 36, arXiv:2609.20979). Linear systems with $t$-sparse rows and columns are a special
case.

## Sources

- Shengtao Guo, Ethan X. Fang and Junwei Lu, Vector balancing via directional total variation, arXiv:2609.11189 (2026), https://arxiv.org/abs/2609.11189.

Stated but not proved: `MathlibExt.Combinatorics.LinearBeckFialaWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/LinearBeckFialaWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearBeckFialaWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/beck-fiala-problem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Beck–Fiala problem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/beck-fiala-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/discrepancy-theory/beck-fiala-problem)
