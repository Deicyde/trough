---
declaration: section
origin: cited
lean: Cslib.Games.Player, Cslib.Games.Player.opponent, Cslib.Games.Player.eq_or_eq_opponent, Cslib.Games.Player.Wins, Cslib.Games.ParityGame, Cslib.Games.ParityGame.IsPlay, Cslib.Games.ParityGame.WonBy, Cslib.Games.ParityGame.PositionalStrategy
statement: formalized
proof: formalized
---

# Parity games

59 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html).

## Players of a parity game

A parity game has exactly two players, the even player and the
odd player.

The even player is the one who wins the plays whose largest priority occurring infinitely often
is even, and the odd player the one who wins those where it is odd.

Formalized by `Cslib.Games.Player`, an inductive type declared in [CSLibExt/Computability/Games/Parity.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#player).

## Opponent

The opponent of a player of a parity game is the other player: the opponent
of the even player is the odd player, and the opponent of the odd player is the even player.

Formalized by `Cslib.Games.Player.opponent`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#opponent).

## Every player is $p$ or the opponent of $p$

For all players $p$ and $q$ of a parity game,
$q = p$ or $q$ is the opponent of $p$.

Formalized by `Cslib.Games.Player.eq_or_eq_opponent`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#eq-or-eq-opponent).

## Parity winning condition of a player

A player wins an infinite sequence of
natural-number priorities when the sequence satisfies that player's parity condition: the even
player wins it when the largest priority occurring infinitely often exists and is even, and the
odd player wins it when the largest priority occurring infinitely often exists and is odd.

Formalized by `Cslib.Games.Player.Wins`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#wins).

## Parity game

A parity game on a type of positions consists of an owner for each
position, which is one of the two players, a move relation between positions, where the owner of
$v$ may move from $v$ to $w$ when $v$ is related to $w$, and a natural-number priority for each
position, such that every position has at least one move (there are no dead ends).

As in the usual infinite-play model, the absence of dead ends means that both players always
have positional strategies.

Formalized by `Cslib.Games.ParityGame`, a structure declared in [CSLibExt/Computability/Games/Parity.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#parity-game).

## Plays of a parity game

An infinite sequence of positions $\pi_0, \pi_1, \dots$ of a
parity game is a play if for every $i$ there is a move from $\pi_i$ to $\pi_{i+1}$.

Formalized by `Cslib.Games.ParityGame.IsPlay`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#is-play).

## Winner of a play in a parity game

Let $G$ be a parity game, write $\Omega(v)$ for the
priority of a position $v$, and let $p$ be a player. An infinite sequence
$\pi = \pi_0 \pi_1 \pi_2 \dots$ of positions of $G$ is won by $p$ when its priority sequence
$\Omega(\pi_0) \Omega(\pi_1) \Omega(\pi_2) \dots$ satisfies the parity condition of $p$: among
the priorities occurring infinitely often there is a largest one, and it is even if $p$ is the
even player and odd if $p$ is the odd player.

The definition applies to every infinite sequence of positions, whether or not it follows the
moves of $G$.

Formalized by `Cslib.Games.ParityGame.WonBy`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#won-by).

## Positional strategy in a parity game

A positional (memoryless) strategy for player `p`: a choice of successor at each position,
legal at the positions `p` owns. Its values elsewhere are irrelevant.

Formalized by `Cslib.Games.ParityGame.PositionalStrategy`, a structure declared in [CSLibExt/Computability/Games/Parity.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#positional-strategy).

## Positional strategies exist

In a parity game, every player has a positional strategy,
since every position has a move.

Formalized by `Cslib.Games.ParityGame.nonempty_positionalStrategy`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#nonempty-positional-strategy).

## Plays conforming to a strategy

Let $\sigma$ be a positional strategy of player $p$ in a
parity game. An infinite sequence of positions $\pi_0, \pi_1, \dots$ (not necessarily a play)
conforms to $\sigma$ if $\pi_{i+1} = \sigma(\pi_i)$ for every $i$ such that $p$ owns $\pi_i$.

Formalized by `Cslib.Games.ParityGame.Conforms`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#conforms).

## Winning strategy from a position

Let $p$ be a player of a parity game. A positional
strategy $\sigma$ of $p$ wins from a position $v$ when every play starting at $v$ that conforms
to $\sigma$ (at every position owned by $p$, the play moves to the successor chosen by $\sigma$)
is won by $p$.

Formalized by `Cslib.Games.ParityGame.WinsFrom`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#wins-from).

## Winning region of a parity game

The positions from which player `p` has a winning positional strategy.

Formalized by `Cslib.Games.ParityGame.WinningRegion`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#winning-region).

## Bounded priorities give every play a winner

Let $p$ be a player of a parity game in
which every position has priority at most $d$, for some natural number $d$. Then every infinite
sequence of positions, in particular every play, is won by $p$ or by the opponent of $p$.

Formalized by `Cslib.Games.ParityGame.wonBy_or_wonBy_opponent`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#won-by-or-won-by-opponent).

## No play is won by both players

In a parity game, for every player $p$, no infinite
sequence of positions (play or not) is won both by $p$ and by the opponent of $p$.

Formalized by `Cslib.Games.ParityGame.not_wonBy_and_wonBy_opponent`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#not-won-by-and-won-by-opponent).

## Winning is prefix independent

Let $p$ be a player of a parity game, $\pi = (\pi_0,
\pi_1, \dots)$ an infinite sequence of positions and $j$ a natural number. Then the sequence
$(\pi_j, \pi_{j+1}, \dots)$, obtained by dropping the first $j$ positions of $\pi$, is won by $p$
if and only if $\pi$ is won by $p$.

Formalized by `Cslib.Games.ParityGame.wonBy_drop_iff`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#won-by-drop-iff).

## Joint successor of two strategies

Let $\sigma$ be a positional strategy of player $p$
and $\tau$ a positional strategy of the opponent of $p$ in a parity game. The joint successor of
a position $v$ is $\sigma(v)$ if $p$ owns $v$, and $\tau(v)$ otherwise.

Formalized by `Cslib.Games.ParityGame.jointNext`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#joint-next).

## Outcome of two positional strategies

Let $p$ be a player of a parity game, $\sigma$ a
positional strategy of $p$ and $\tau$ a positional strategy of the opponent of $p$. The outcome
of $\sigma$ and $\tau$ from a position $v$ is the infinite sequence of positions
$v_0, v_1, v_2, \dots$ with $v_0 = v$ in which $v_{i+1}$ is the successor chosen by $\sigma$ at
$v_i$ if $p$ owns $v_i$, and the successor chosen by $\tau$ at $v_i$ otherwise. It is the play
from $v$ in which $p$ follows $\sigma$ and the opponent follows $\tau$.

Formalized by `Cslib.Games.ParityGame.outcome`, a definition declared in [CSLibExt/Computability/Games/Parity.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#outcome).

## The winning regions of the two players are disjoint

In a parity game, for every player
$p$, no position lies both in the winning region of $p$ and in the winning region of the
opponent of $p$.

Formalized by `Cslib.Games.ParityGame.disjoint_winningRegion`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#disjoint-winning-region).

## Winning strategies keep winning along allowed moves

In a parity game, let $\sigma$ be a
positional strategy of player $p$ that wins from a position $v$, and let $w$ be a position with a
move from $v$ to $w$ such that $w = \sigma(v)$ if $p$ owns $v$. Then $\sigma$ wins from $w$.

Formalized by `Cslib.Games.ParityGame.WinsFrom.of_move`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#of-move).

## Opponent moves stay in the winning region

In a parity game, let $v$ be a position in the
winning region of player $p$ that is owned by the opponent of $p$. Then every position $w$ with a
move from $v$ to $w$ is in the winning region of $p$.

Formalized by `Cslib.Games.ParityGame.move_mem_winningRegion`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#move-mem-winning-region).

## A winning strategy's move stays in the winning region

In a parity game, let $\sigma$ be a
positional strategy of player $p$ that wins from a position $v$ owned by $p$. Then the successor
$\sigma(v)$ chosen by $\sigma$ is in the winning region of $p$.

Formalized by `Cslib.Games.ParityGame.next_mem_winningRegion`, a theorem declared in [CSLibExt/Computability/Games/Parity.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Parity.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#next-mem-winning-region).

## Controllable predecessor

Let $G$ be a parity game, $p$ a player and $X$ a set of
positions. The controllable predecessor $\mathrm{cpre}_p(X)$ of $X$ for $p$ is the set of
positions $v$ such that either $v$ is owned by $p$ and some move from $v$ leads into $X$, or $v$
is not owned by $p$ and every move from $v$ leads into $X$.

Formalized by `Cslib.Games.ParityGame.cpre`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#cpre).

## Attractor operator

Let $G$ be a parity game, $p$ a player and $T$ a set of positions. The
attractor operator of $T$ for $p$ is the monotone map on sets of positions sending $X$ to
$T \cup \mathrm{cpre}_p(X)$, where $\mathrm{cpre}_p$ is the controllable predecessor for $p$.

Formalized by `Cslib.Games.ParityGame.attractorStep`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-step).

## Attractor

Let $G$ be a parity game, $p$ a player and $T$ a set of positions. The
attractor of $T$ for $p$ is the least fixed point of the attractor operator
$X \mapsto T \cup \mathrm{cpre}_p(X)$ on sets of positions, where $\mathrm{cpre}_p$ is the
controllable predecessor for $p$.

Formalized by `Cslib.Games.ParityGame.attractor`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor).

## Attractor stages

Let $G$ be a parity game, $p$ a player, $T$ a set of positions and $n$ a
natural number. The $n$-th attractor stage $S_n$ of $T$ for $p$ is the set obtained by applying the
attractor operator $X \mapsto T \cup \mathrm{cpre}_p(X)$ $n$ times to $\emptyset$, where
$\mathrm{cpre}_p$ is the controllable predecessor for $p$; thus $S_0 = \emptyset$ and
$S_{n+1} = T \cup \mathrm{cpre}_p(S_n)$.

The $n$-th stage consists of the positions from which $p$ can force a visit to $T$ within fewer
than $n$ moves.

Formalized by `Cslib.Games.ParityGame.attractorStage`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-stage).

## The attractor is a fixed point

Let $G$ be a parity game, $p$ a player and $T$ a set of
positions, and let $A$ be the attractor of $T$ for $p$. Then $T \cup \mathrm{cpre}_p(A) = A$, where
$\mathrm{cpre}_p(A)$ is the controllable predecessor of $A$ for $p$; that is, $A$ is a fixed point
of the attractor operator $X \mapsto T \cup \mathrm{cpre}_p(X)$.

Formalized by `Cslib.Games.ParityGame.union_cpre_attractor`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#union-cpre-attractor).

## The attractor lies in every closed set

Let $G$ be a parity game, $p$ a player and $T$ a
set of positions. If a set $X$ of positions satisfies $T \cup \mathrm{cpre}_p(X) \subseteq X$,
where $\mathrm{cpre}_p$ is the controllable predecessor for $p$, then the attractor of $T$ for $p$
is contained in $X$.

Formalized by `Cslib.Games.ParityGame.attractor_subset_of`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-subset-of).

## The attractor stabilizes after as many stages as there are positions

Let $G$ be a parity
game with finitely many positions, $N$ of them, let $p$ be a player and $T$ a set of positions.
Then the attractor of $T$ for $p$ equals the $N$-th attractor stage of $T$ for $p$, that is, the
result of applying the attractor operator $X \mapsto T \cup \mathrm{cpre}_p(X)$ $N$ times to
$\emptyset$, where $\mathrm{cpre}_p$ is the controllable predecessor for $p$.

Formalized by `Cslib.Games.ParityGame.attractor_eq_attractorStage_card`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-eq-attractor-stage-card).

## Attractor strategy

Let $G$ be a parity game, $p$ a player and $T$ a set of positions. The
attractor strategy of $p$ for $T$ is the positional strategy of $p$ that at a position $v$ moves
to a successor of $v$ lying in the $n$-th attractor stage of $T$ for $p$, for the least $n$ for
which $v$ has such a successor, and to an arbitrary successor of $v$ if no successor of $v$ lies
in any attractor stage.

Formalized by `Cslib.Games.ParityGame.attractorStrategy`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-strategy).

## The attractor strategy moves into the stage from its controllable predecessor

Let $G$ be
a parity game, $p$ a player, $T$ a set of positions, $n$ a natural number and $S_n$ the $n$-th
attractor stage of $T$ for $p$. If a position $v$ owned by $p$ lies in the controllable
predecessor $\mathrm{cpre}_p(S_n)$ of $S_n$ for $p$, then the successor that the attractor
strategy of $p$ for $T$ chooses at $v$ lies in $S_n$.

Formalized by `Cslib.Games.ParityGame.attractorStrategy_next_mem`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-strategy-next-mem).

## The attractor strategy reaches the target from an attractor stage

Let $G$ be a parity
game, $p$ a player, $T$ a set of positions and $n$ a natural number. If $\pi$ is a play of $G$
that conforms to the attractor strategy of $p$ for $T$ and whose initial position $\pi_0$ lies in
the $n$-th attractor stage of $T$ for $p$, then $\pi_i \in T$ for some $i < n$.

Formalized by `Cslib.Games.ParityGame.attractorStrategy_reaches`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-strategy-reaches).

## Forcing a visit to a set

Let $G$ be a parity game, $p$ a player, $\sigma$ a positional
strategy of $p$, $T$ a set of positions and $v$ a position. The strategy $\sigma$ forces a visit
to $T$ from $v$ when every play $\pi$ of $G$ with $\pi_0 = v$ that conforms to $\sigma$ visits
$T$, that is, $\pi_i \in T$ for some $i \in \mathbb{N}$.

Formalized by `Cslib.Games.ParityGame.ForcesReach`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#forces-reach).

## The attractor strategy reaches the target from the attractor

Let $G$ be a parity game
with finitely many positions, $N$ of them, let $p$ be a player and $T$ a set of positions. If
$\pi$ is a play of $G$ that conforms to the attractor strategy of $p$ for $T$ and whose initial
position $\pi_0$ lies in the attractor of $T$ for $p$, then $\pi_i \in T$ for some $i < N$.

Formalized by `Cslib.Games.ParityGame.attractorStrategy_reaches_of_mem_attractor`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-strategy-reaches-of-mem-attrac).

## The attractor strategy forces a visit

Let $G$ be a parity game with finitely many
positions, $p$ a player and $T$ a set of positions. From every position $v$ of the attractor of
$T$ for $p$, the attractor strategy of $p$ for $T$ forces a visit to $T$: every play from $v$
conforming to it visits $T$.

Formalized by `Cslib.Games.ParityGame.forcesReach_attractorStrategy`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#forces-reach-attractor-strategy).

## Trap for a player

Let $G$ be a parity game and $p$ a player. A set $U$ of positions is a
trap for $p$ when, for every position $v \in U$, every move from $v$ leads into $U$ if $v$
belongs to $p$, and some move from $v$ leads into $U$ if $v$ does not belong to $p$. Thus $p$
cannot force the play out of $U$.

Formalized by `Cslib.Games.ParityGame.IsTrap`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#is-trap).

## The complement of an attractor is a trap

Let $G$ be a parity game, $p$ a player and $T$
a set of positions. The complement of the attractor of $T$ for $p$ is a trap for $p$.

Formalized by `Cslib.Games.ParityGame.isTrap_compl_attractor`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#is-trap-compl-attractor).

## Traps disjoint from a set avoid its attractor

Let $G$ be a parity game, $p$ a player and
$T$ a set of positions. If a set $U$ of positions is a trap for $p$ and is disjoint from $T$, then
$U$ is disjoint from the attractor of $T$ for $p$.

Since the complement of the attractor is itself a trap for $p$ disjoint from $T$, it is the
largest such trap.

Formalized by `Cslib.Games.ParityGame.IsTrap.disjoint_attractor`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#disjoint-attractor).

## Trap strategy

Let $G$ be a parity game, $p$ a player and $U$ a set of positions. The trap
strategy for $U$ is the positional strategy of the opponent of $p$ that, at each position $v$,
moves to some position $w \in U$ with a move from $v$ to $w$ if there is one, and to an arbitrary
position reachable from $v$ in one move otherwise.

Formalized by `Cslib.Games.ParityGame.trapStrategy`, a definition declared in [CSLibExt/Computability/Games/Attractor.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#trap-strategy).

## The trap strategy stays in the trap

Let $G$ be a parity game, $p$ a player and $U$ a trap
for $p$. If $\pi$ is a play with $\pi_0 \in U$ that conforms to the trap strategy of the opponent
of $p$ for $U$, then $\pi_i \in U$ for every $i \in \mathbb{N}$.

Formalized by `Cslib.Games.ParityGame.IsTrap.trapStrategy_stays`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#trap-strategy-stays).

## The trap strategy avoids the target

Let $G$ be a parity game, $p$ a player, $T$ a set of
positions and $A$ the attractor of $T$ for $p$. If $\pi$ is a play starting at a position outside
$A$ that conforms to the trap strategy of the opponent of $p$ for the complement of $A$, then
$\pi_i \notin T$ for every $i \in \mathbb{N}$.

Formalized by `Cslib.Games.ParityGame.trapStrategy_avoids`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#trap-strategy-avoids).

## No strategy forces a visit from outside the attractor

Let $G$ be a parity game, $p$ a
player and $T$ a set of positions. If a position $v$ is not in the attractor of $T$ for $p$, then
no positional strategy of $p$ forces a visit to $T$ from $v$.

Formalized by `Cslib.Games.ParityGame.not_forcesReach_of_notMem_attractor`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#not-forces-reach-of-not-mem-attractor).

## Characterization of the attractor

Let $G$ be a parity game with finitely many positions,
$p$ a player and $T$ a set of positions. A position $v$ lies in the attractor of $T$ for $p$ if
and only if some positional strategy of $p$ forces a visit to $T$ from $v$.

Formalized by `Cslib.Games.ParityGame.mem_attractor_iff`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#mem-attractor-iff).

## Winning regions are traps for the opponent

In a parity game $G$, the winning region of a
player $p$, the set of positions from which $p$ has a winning positional strategy, is a trap for
the opponent of $p$.

Formalized by `Cslib.Games.ParityGame.isTrap_winningRegion`, a theorem declared in [CSLibExt/Computability/Games/Attractor.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Attractor.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#is-trap-winning-region).

## Encoded parity game

An encoded finite parity game on the $n$ positions
$0, \dots, n - 1$ consists of an owner for each position, given as a Boolean (false for the even
player, true for the odd player), a move relation, given as a Boolean-valued $n \times n$
matrix, and a priority for each position, given as a natural number.

No seriality is assumed: a position may have no move, since restricted subgames need not be
serial on the whole arena.

Formalized by `Cslib.Games.EncodedParityGame`, a structure declared in [CSLibExt/Computability/Games/Encoded.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#encoded-parity-game).

## The parity game of a serial encoded game

Let $G$ be an encoded parity game on the
positions $\{0, \dots, n-1\}$ in which every position has a move to some position. The associated
parity game has the same positions, moves and priorities, and a position is owned by the odd
player if $G$ assigns it to the odd player and by the even player otherwise; every position has
a move by the hypothesis on $G$.

Formalized by `Cslib.Games.EncodedParityGame.toParityGame`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#to-parity-game).

## Dual parity game

The dual of an encoded parity game $G$ is the encoded parity game with
the same positions and moves in which every position is owned by the other player than in $G$
and has priority one more than in $G$.

Since incrementing priorities flips every parity, the even player wins the dual game exactly
where the odd player wins the original.

Formalized by `Cslib.Games.EncodedParityGame.dualGame`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#dual-game).

## Controllable predecessor inside a set of positions

Let $G$ be an encoded parity game,
$p$ a player (encoded as a Boolean: false for even, true for odd), and $U$, $X$ sets of
positions. The controllable predecessor of $X$ for $p$ inside $U$ is the set of positions
$v \in U$ such that either $v$ is owned by $p$ and some move of $G$ goes from $v$ to a position
of $U \cap X$, or $v$ is not owned by $p$ and every move of $G$ from $v$ to a position of $U$
ends in $X$.

Moves leaving $U$ are ignored; in particular a position of $U$ not owned by $p$ with no move into
$U$ belongs to the set.

Formalized by `Cslib.Games.EncodedParityGame.cpreIn`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#cpre-in).

## Attractor inside a set of positions

Let $G$ be an encoded parity game on $n$ positions,
$p$ a player (encoded as a Boolean: false for even, true for odd), and $T$, $U$ sets of
positions. The attractor of $T$ for $p$ inside $U$ is the set obtained from $\emptyset$ by
applying $n$ times the map $X \mapsto (T \cap U) \cup \mathrm{CPre}_p^U(X)$, where
$\mathrm{CPre}_p^U(X)$ is the controllable predecessor of $X$ for $p$ inside $U$.

Formalized by `Cslib.Games.EncodedParityGame.attractorIn`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#attractor-in).

## Rank of a priority in a parity game

The rank of a priority `p` among the distinct priorities occurring in
the game: the number of distinct priorities `q < p` that occur.

Formalized by `Cslib.Games.EncodedParityGame.priorityRank`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-rank).

## Compressed priority

Let $G$ be an encoded parity game on the positions
$\{0, \dots, n-1\}$. The compressed priority of a natural number $p$ is $2r + (p \bmod 2)$, where
$r$ is the rank of $p$ in $G$: the number of distinct priorities $q < p$ that occur in $G$.

The compressed priority of $p$ is congruent to $p$ modulo $2$. On the priorities that occur in
$G$, compression is injective and strictly increasing.

Formalized by `Cslib.Games.EncodedParityGame.priorityCompressed`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-compressed).

## Priority compression

For an encoded parity game $G$ on $n$ positions, the compressed game
has the same owners and moves as $G$ and gives each position $v$ the priority $2r + (q \bmod 2)$,
where $q$ is the priority of $v$ in $G$ and $r$ is the number of distinct priorities occurring
in $G$ that are smaller than $q$.

Since at most $n$ distinct priorities occur, every compressed priority is strictly below $2n$.

Formalized by `Cslib.Games.EncodedParityGame.priorityCompress`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-compress).

## Priority ranks are below the number of priorities

Let $G$ be an encoded parity game,
and for a natural number $p$ let the rank of $p$ be the number of distinct priorities $q < p$
that occur in $G$. For every position $v$ of $G$, the rank of the priority of $v$ is strictly
less than the number of distinct priorities that occur in $G$.

The priorities below the priority of $v$ form a proper subset of the occurring priorities, since
the priority of $v$ occurs but is not below itself.

## Sources

- M. Jurdziński, "Small progress measures for solving parity games", *Proceedings of STACS 2000*, LNCS 1770, 290-301.

Formalized by `Cslib.Games.EncodedParityGame.priorityRank_lt_card`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-rank-lt-card).

## Strict monotonicity of priority ranks

Let $G$ be an encoded parity game, and for a
natural number $p$ let the rank of $p$ be the number of distinct priorities $q < p$ that occur
in $G$. If $v$ and $w$ are positions of $G$ and the priority of $w$ is strictly less than the
priority of $v$, then the rank of the priority of $w$ is strictly less than the rank of the
priority of $v$.

The priority of $w$ is counted in the rank of the priority of $v$ but not in its own rank.

## Sources

- M. Jurdziński, "Small progress measures for solving parity games", *Proceedings of STACS 2000*, LNCS 1770, 290-301.

Formalized by `Cslib.Games.EncodedParityGame.priorityRank_lt_of_lt`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-rank-lt-of-lt).

## Monotonicity of priority ranks

Let $G$ be an encoded parity game, and for a natural
number $p$ let the rank of $p$ be the number of distinct priorities $q < p$ that occur in $G$. If
$v$ and $w$ are positions of $G$ and the priority of $w$ is at most the priority of $v$, then the
rank of the priority of $w$ is at most the rank of the priority of $v$.

## Sources

- M. Jurdziński, "Small progress measures for solving parity games", *Proceedings of STACS 2000*, LNCS 1770, 290-301.

Formalized by `Cslib.Games.EncodedParityGame.priorityRank_le_of_le`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-rank-le-of-le).

## Bound on compressed priorities

For an encoded parity game $G$ on $n$ positions, every
priority of the priority-compressed game of $G$ is strictly less than $2n$.

This holds because at most $n$ distinct priorities occur in $G$.

Formalized by `Cslib.Games.EncodedParityGame.priorityCompressed_lt`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-compressed-lt).

## Priority compression preserves and reflects the order of priorities

For an encoded
parity game $G$ and positions $v$, $w$, the priority of $v$ is smaller than the priority of $w$
in the priority-compressed game of $G$ if and only if it is smaller in $G$.

Formalized by `Cslib.Games.EncodedParityGame.priorityCompressed_lt_iff`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-compressed-lt-iff).

## Priority compression preserves parity

For an encoded parity game $G$ and every position
$v$, the priority of $v$ in the priority-compressed game of $G$ has the same parity as the
priority of $v$ in $G$.

Formalized by `Cslib.Games.EncodedParityGame.priorityCompressed_mod_two`, a theorem declared in [CSLibExt/Computability/Games/Encoded.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#priority-compressed-mod-two).

## Maximal priority on a set of positions

For an encoded parity game $G$ and a set $U$ of
positions, the maximal priority on $U$ is the largest priority of $G$ at a position of $U$, or
$0$ if $U$ is empty.

Formalized by `Cslib.Games.EncodedParityGame.maxPriorityIn`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#max-priority-in).

## Positions of maximal priority

For an encoded parity game $G$ and a set $U$ of positions,
the positions of maximal priority in $U$ are the positions $v \in U$ whose priority equals the
maximal priority of $G$ on $U$.

Formalized by `Cslib.Games.EncodedParityGame.maxPositionsIn`, a definition declared in [CSLibExt/Computability/Games/Encoded.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Games/Encoded.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html#max-positions-in).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity games](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/parity-games)
