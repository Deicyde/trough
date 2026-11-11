---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook43Wanted.BanachMazurStrategyValid, MathlibExt.Topology.ScottishBook43Wanted.BanachMazurPlayConsistent, MathlibExt.Topology.ScottishBook43Wanted.BanachMazurAHasWinningStrategy, MathlibExt.Topology.ScottishBook43Wanted.BanachMazurBHasWinningStrategy, MathlibExt.Topology.ScottishBook43Wanted.banach_mazur_winning_strategy_characterization
statement: formalized
---

# Banach–Mazur game

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html).

## Valid strategies in the Banach–Mazur game

A strategy in the Banach–Mazur game is a map
$\sigma \colon \mathbb{R} \times \mathbb{R} \to \mathbb{R} \times \mathbb{R}$, a pair $(a, b)$
standing for the open interval $(a, b)$. It is valid if for all reals $a < b$ the pair
$(c, d) = \sigma(a, b)$ satisfies $a \le c < d \le b$, so that it answers each nonempty open
interval with a nonempty open subinterval, possibly the interval itself. Nothing is required of
$\sigma$ on pairs $(a, b)$ with $a \ge b$.

Strategies are taken to depend only on the opponent's last move: the rest of the game depends
only on the current interval.

Formalized by `MathlibExt.Topology.ScottishBook43Wanted.BanachMazurStrategyValid`, a definition declared in [WantedExt/Topology/ScottishBook43Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook43Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html#banach-mazur-strategy-valid).

## Plays of the Banach–Mazur game

Let $(a, b)$ be a pair of reals and let $\sigma_A$ and
$\sigma_B$ be strategies for A and B, maps from pairs of reals to pairs of reals. A sequence
$(p_n)_{n \ge 0}$ of pairs of reals is the play that opens with $(a, b)$ and follows $\sigma_A$
and $\sigma_B$ if $p_0 = (a, b)$, $p_{n+1} = \sigma_B(p_n)$ for every even $n$, and
$p_{n+1} = \sigma_A(p_n)$ for every odd $n$: A opens at index $0$ and moves at the other even
indices, B moves at the odd indices.

Formalized by `MathlibExt.Topology.ScottishBook43Wanted.BanachMazurPlayConsistent`, a definition declared in [WantedExt/Topology/ScottishBook43Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook43Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html#banach-mazur-play-consistent).

## Winning strategy for the first player in the Banach–Mazur game

Let
$E \subseteq \mathbb{R}$. In this game a move is a pair of reals $(c, d)$, standing for the open
interval $(c, d)$, and a valid strategy is a map from pairs to pairs answering each pair $(c, d)$
with $c < d$ by a pair $(c', d')$ with $c \le c' < d' \le d$. Player A has a winning strategy for
$E$ if there are reals $a < b$ and a valid strategy $\sigma_A$ such that, for every valid strategy
$\sigma_B$, the play $(c_n, d_n)_{n \ge 0}$ given by $(c_0, d_0) = (a, b)$,
$(c_{n+1}, d_{n+1}) = \sigma_B(c_n, d_n)$ for even $n$ and
$(c_{n+1}, d_{n+1}) = \sigma_A(c_n, d_n)$ for odd $n$ satisfies
$\left(\bigcap_{n} (c_n, d_n)\right) \cap E \neq \emptyset$.

Formalized by `MathlibExt.Topology.ScottishBook43Wanted.BanachMazurAHasWinningStrategy`, a definition declared in [WantedExt/Topology/ScottishBook43Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook43Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html#banach-mazur-ahas-winning-strategy).

## Winning strategy for the second player in the Banach–Mazur game

Let
$E \subseteq \mathbb{R}$. In this game a move is a pair of reals $(c, d)$, standing for the open
interval $(c, d)$, and a valid strategy is a map from pairs to pairs answering each pair $(c, d)$
with $c < d$ by a pair $(c', d')$ with $c \le c' < d' \le d$. Player B has a winning strategy for
$E$ if there is a valid strategy $\sigma_B$ such that, for all reals $a < b$ and every valid
strategy $\sigma_A$, the play $(c_n, d_n)_{n \ge 0}$ given by $(c_0, d_0) = (a, b)$,
$(c_{n+1}, d_{n+1}) = \sigma_B(c_n, d_n)$ for even $n$ and
$(c_{n+1}, d_{n+1}) = \sigma_A(c_n, d_n)$ for odd $n$ satisfies
$\left(\bigcap_{n} (c_n, d_n)\right) \cap E = \emptyset$.

Formalized by `MathlibExt.Topology.ScottishBook43Wanted.BanachMazurBHasWinningStrategy`, a definition declared in [WantedExt/Topology/ScottishBook43Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook43Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html#banach-mazur-bhas-winning-strategy).

## Banach–Mazur game theorem

For every set $E \subseteq \mathbb{R}$, player A has a winning
strategy in the Banach–Mazur game for $E$ if and only if there are reals $a < b$ such that
$(a, b) \setminus E$ is meagre, and player B has a winning strategy in the Banach–Mazur game for
$E$ if and only if $E$ is meagre.

This answers Mazur's Problem 43 of the Scottish Book. Given $E$, A picks an interval $d_1$,
B picks a subinterval $d_2$ of $d_1$, A picks a subinterval $d_3$ of $d_2$, and so on; A wins if
the intersection of all the chosen intervals meets $E$. Mazur asked whether A has a winning
method only when the complement of $E$ is of first category in some interval, and whether B has
one when $E$ is of first category. Both answers are affirmative, in the characterization form
above (Oxtoby).

## Sources

- S. Mazur, Problem 43 of the Scottish Book; addendum of S. Banach, 4 August 1935: "Mazur's conjecture is true"; J. C. Oxtoby, The Banach-Mazur game and Banach category theorem; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook43Wanted.banach_mazur_winning_strategy_characterization` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook43Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook43Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html#banach-mazur-winning-strategy-characteri).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banach–Mazur game](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/banach-mazur-game/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/descriptive-set-theory/banach-mazur-game)
