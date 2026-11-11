---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.completeBoard, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.freeElems, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.MakerCanForce, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.MakerWinsBreakerFirst, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.HamiltonianTarget, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.hamiltonicityCriticalBias, MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.hamiltonicityCriticalBias_holds
statement: formalized
---

# Hamiltonicity Maker–Breaker game

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html).

## Edges of the complete graph $K_n$

For a natural number $n$, the complete board is the
finite set of edges of the complete graph $K_n$ on the vertex set $\{0, 1, \dots, n - 1\}$, that is,
the set of all unordered pairs $\{i, j\}$ of distinct vertices $i \ne j$.

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.completeBoard`, a definition declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#complete-board).

## Free elements of a position

For finite sets $X$ (the board), $M$ (the elements claimed
by Maker) and $R$ (the elements claimed by Breaker), the free elements are the elements of $X$
claimed by neither player, that is, the set $X \setminus (M \cup R)$.

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.freeElems`, a definition declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#free-elems).

## Maker can force a win in the biased Maker-Breaker game

Fix a finite board $X$, a bias
$b \in \mathbb{N}$ and a property of finite sets, Maker's target. At a position $(M, R)$, where
$M$ and $R$ are the sets claimed so far by Maker and by Breaker, an element of $X$ is free if it
lies in neither $M$ nor $R$. The relation "Maker, to move at $(M, R)$, can force a win" is the
least one satisfying two rules: it holds when no element of $X$ is free and $M$ satisfies the
target; and it holds when there is a free element $e$ such that, for every set $R'$ of exactly
$\min(b, r)$ of the $r$ elements that are free after $e$ is claimed, Maker can force a win at
$(M \cup \{e\}, R \cup R')$. Thus Maker claims one free element per turn, Breaker answers with
$b$ of them (all remaining ones if fewer are free), play ends when the board is exhausted, and
Maker wins if his set satisfies the target.

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.MakerCanForce`, an inductive type declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#maker-can-force).

## Maker wins the biased game with Breaker moving first

For a finite board $X$, a bias
$b \in \mathbb{N}$ and a target property of Maker's claimed set, Maker wins the $(1 : b)$
Maker-Breaker game on $X$ in which Breaker moves first when, for every set $F \subseteq X$ of
exactly $\min(b, |X|)$ elements that Breaker may claim in his first move, Maker can force a win
when it is his turn at the position where he has claimed nothing and Breaker has claimed $F$.

Breaker moving first is the convention of both sources (Krivelevich, Section 1: "We assume that
Breaker moves first"; Chvátal-Erdős, Section 1: "with the Breaker going first").

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.MakerWinsBreakerFirst`, a definition declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#maker-wins-breaker-first).

## Maker's Hamiltonicity target

For a natural number $n$, a set $C$ of unordered pairs of
vertices from $\{0, 1, \dots, n - 1\}$ meets the Hamiltonicity target when the simple graph on
these $n$ vertices whose edges are the pairs of distinct vertices in $C$ is Hamiltonian: it has a
cycle passing through every vertex exactly once, with the convention that the one-vertex graph is
Hamiltonian.

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.HamiltonianTarget`, a definition declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#hamiltonian-target).

## The Hamiltonicity critical-bias property

This is the statement that the critical bias of
the Hamiltonicity game is $(1 + o(1))\, n / \ln n$. In the $(1 : b)$ Maker-Breaker game on the
edges of the complete graph $K_n$ with Breaker moving first, Breaker claims $b$ free edges per
turn (all remaining free edges if fewer than $b$ are left), Maker claims one free edge per turn,
and Maker wins if, once every edge is claimed, his edges contain a Hamilton cycle. The property
says that for every real $\varepsilon > 0$ there is $n_0$ such that for every $n \ge n_0$, Maker
has a winning strategy for every natural number $b$ with $0 < b \le (1 - \varepsilon)\, n / \ln n$,
and Maker has no winning strategy for any natural number $b \ge (1 + \varepsilon)\, n / \ln n$.

Formalized by `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.hamiltonicityCriticalBias`, a definition declared in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#hamiltonicity-critical-bias).

## The critical bias of the Hamiltonicity game is $(1 + o(1))\, n / \ln n$

Consider the
$(1 : b)$ Maker-Breaker game on the edges of the complete graph $K_n$ in which Breaker moves
first: Breaker claims $b$ free edges per turn (all remaining free edges if fewer than $b$ are
left), Maker claims one free edge per turn, and Maker wins if, once every edge is claimed, his
edges contain a Hamilton cycle. For every real $\varepsilon > 0$ there is $n_0$ such that for
every $n \ge n_0$, Maker has a winning strategy for every natural number $b$ with
$0 < b \le (1 - \varepsilon)\, n / \ln n$, and Maker has no winning strategy for any natural
number $b \ge (1 + \varepsilon)\, n / \ln n$.

Maker's side is Krivelevich's Theorem 1, which gives Maker a win for every
$b \le (1 - 30 / \ln^{1/4} n)\, n / \ln n$ once $n$ is large. Breaker's side follows from the
Chvátal-Erdős Theorem 3.1, whose Breaker strategy claims every edge at some vertex for every
$b > (1 + \varepsilon / 2)\, n / \ln n$ once $n$ is large.

## Sources

- T. Szabó (joint with H. Gebauer and M. Krivelevich), Thresholds for positional games, in Combinatorics, Oberwolfach Reports 5 (2008), no. 1, pp. 56-59, DOI 10.4171/OWR/2008/01; resolution: M. Krivelevich, The critical bias for the Hamiltonicity game is (1 + o(1)) n / ln n, J. Amer. Math. Soc. 24 (2011), 125-131, DOI 10.1090/S0894-0347-2010-00678-9, arXiv:0909.2744; V. Chvátal and P. Erdős, Biased positional games, Ann. Discrete Math. 2 (1978), 221-229, https://users.renyi.hu/~p_erdos/1978-06.pdf, Krivelevich, Section 1 (Breaker moves first) and Theorem 1 (Maker wins for b ≤ (1 - 30/ln^{1/4} n) n/ln n); Chvátal-Erdős, Section 1 (Breaker moves first) and Theorem 3.1 (Breaker wins T(n, b) for b > (1 + ε) n/log n and n > n₀(ε), by isolating a vertex); report p. 57 (the Hamiltonicity game is harder for Maker than the connectivity game), https://arxiv.org/abs/0909.2744.

Stated but not proved: `MathlibExt.Combinatorics.HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.hamiltonicityCriticalBias_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamiltonicityGameCriticalBiasOWR1782Problem013Wanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html#hamiltonicity-critical-bias-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hamiltonicity Maker–Breaker game](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/hamiltonicity-maker-breaker-game)
