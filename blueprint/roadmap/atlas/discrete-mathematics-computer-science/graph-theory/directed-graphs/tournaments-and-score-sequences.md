---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsTournament, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.score, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsReducible, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsCircularTriad, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.egf_factorial_choose, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.landau_score_sequence, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.isReducible_iff, MathlibExt.GraphTheory.TournamentScoreSequenceWanted.card_circularTriads
statement: formalized
---

# Tournaments and score sequences

8 results, 4 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html).

## Tournament

A tournament on the players $1, \dots, n$ is a binary relation $T$, where
$T(i, j)$ means that $i$ beats $j$, such that no player beats itself and for any two distinct
players $i$ and $j$ exactly one of $T(i, j)$ and $T(j, i)$ holds.

Formalized by `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsTournament`, a definition declared in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#is-tournament).

## Score of a player

Let $T$ be a binary relation on the players $1, \dots, n$, where
$T(i, j)$ means that $i$ beats $j$. The score of a player $i$ is the number of players $j$ such
that $T(i, j)$ holds, that is, the number of players that $i$ beats.

In a tournament this is the outdegree of $i$.

Formalized by `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.score`, a definition declared in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#score).

## Reducible tournament

A tournament is reducible if some nonempty proper
set of players loses all games against the complement.

Formalized by `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsReducible`, a definition declared in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#is-reducible).

## Circular triad

Let $T$ be a binary relation on the players $1, \dots, n$, where
$T(i, j)$ means that $i$ beats $j$. A set $S$ of players is a circular triad of $T$ if $S$ has
exactly three elements and every $i \in S$ beats exactly one $j \in S$.

In a tournament this means that the three players form a directed $3$-cycle.

Formalized by `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.IsCircularTriad`, a definition declared in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#is-circular-triad).

## Exponential generating function of a shifted binomial sequence

For natural numbers $a$
and $b$, let $g(n) = n! \binom{n-a+b}{b}$ for $n \ge a$ and $g(n) = 0$ for $n < a$, and let
$A(x) = \sum_{n \ge 0} g(n) x^n / n!$ be its exponential generating function, a formal power
series over $\mathbb{Q}$. Then $(1 - x)^{b+1} A(x) = x^a$; equivalently,
$A(x) = x^a (1 - x)^{-(b+1)}$.

## Sources

- Ian R. Harris and Ryan P. A. McShane, "Counting Tournaments with a Specified Number of Circular Triads", Theorem 1.

Stated but not proved: `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.egf_factorial_choose` is written with `theorem_wanted` in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#egf-factorial-choose).

## Landau's theorem on score sequences

Let $s_1 \le s_2 \le \dots \le s_n$ be a
nondecreasing sequence of natural numbers. There is a tournament on $n$ players in which player
$i$ has score $s_i$ for every $i$ if and only if $\sum_{i=1}^{k} s_i \ge \binom{k}{2}$ for every
$k$ with $1 \le k \le n$ and $\sum_{i=1}^{n} s_i = \binom{n}{2}$.

## Sources

- Ian R. Harris and Ryan P. A. McShane, "Counting Tournaments with a Specified Number of Circular Triads", Theorem 4.

Stated but not proved: `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.landau_score_sequence` is written with `theorem_wanted` in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#landau-score-sequence).

## Moon's reducibility criterion

Let $T$ be a tournament on $n$ players in which the score
$s_i$ of player $i$ satisfies $s_1 \le s_2 \le \dots \le s_n$. Then $T$ is reducible if and only
if $\sum_{i=1}^{k} s_i = \binom{k}{2}$ for some integer $k$ with $1 \le k < n$.

## Sources

- Ian R. Harris and Ryan P. A. McShane, "Counting Tournaments with a Specified Number of Circular Triads", Theorem 5.

Stated but not proved: `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.isReducible_iff` is written with `theorem_wanted` in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#is-reducible-iff).

## Moon's count of circular triads

In a tournament on $n$ players with scores
$s_1, \dots, s_n$, the number of circular triads is
$\binom{n}{3} - \sum_{i=1}^{n} \binom{s_i}{2}$.

## Sources

- Ian R. Harris and Ryan P. A. McShane, "Counting Tournaments with a Specified Number of Circular Triads", Theorem 6.

Stated but not proved: `MathlibExt.GraphTheory.TournamentScoreSequenceWanted.card_circularTriads` is written with `theorem_wanted` in [WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/TournamentScoreSequenceWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html#card-circular-triads).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tournaments and score sequences](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/directed-graphs/tournaments-and-score-sequences)
