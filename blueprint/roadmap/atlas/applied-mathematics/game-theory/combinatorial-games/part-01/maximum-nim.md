---
declaration: section
origin: cited
lean: MetaMathlibExt.maximumNimMex, MetaMathlibExt.maximumNimMex_eq_iff, MetaMathlibExt.maximumNimGrundy, MetaMathlibExt.maximumNimGrundy_eq, MetaMathlibExt.maximumNimGrundy_div_two_five, MetaMathlibExt.maximumNimGrundy_div_two_four, MetaMathlibExt.maximumNimGrundy_div_two_three, MetaMathlibExt.maximumNimGame
statement: formalized
---

# Maximum Nim

41 results, 19 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html).

## Minimum excludant of a finite set

For a finite set $s$ of natural numbers,
$\operatorname{mex}(s)$ is the least natural number that does not belong to $s$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimMex`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-mex).

## Characterization of the minimum excludant

Let $s$ be a finite set of natural numbers and
$m$ a natural number. Then $\operatorname{mex}(s)$, the least natural number not in $s$, equals $m$
if and only if $m \notin s$ and every natural number $n < m$ lies in $s$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimMex_eq_iff`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-mex-eq-iff).

## Grundy numbers of Maximum Nim

For a rule function $f : \mathbb{N} \to \mathbb{N}$, the
Grundy number $G_f(x)$ of a pile of $x$ stones in Maximum Nim is defined by recursion on $x$ as the
mex (least natural number not in the set) of $\{G_f(x - u) : 1 \le u \le \min(f(x), x)\}$, the
Grundy numbers of the positions reachable from $x$ by removing $u$ stones.

Taking $\min(f(x), x)$ makes the definition total; under the source's hypotheses on $f$, which
include $f(0) = 0$, it does not change the legal moves.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimGrundy`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy).

## Recursive formula for Maximum Nim Grundy numbers

For every rule function
$f : \mathbb{N} \to \mathbb{N}$ and every pile size $x \in \mathbb{N}$, the Grundy number $G_f(x)$
of a pile of $x$ stones in Maximum Nim with rule function $f$ equals the mex (least natural number
not in the set) of $\{G_f(x - u) : 1 \le u \le \min(f(x), x)\}$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimGrundy_eq`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-eq).

## Grundy number of a pile of five in halving Maximum Nim

In Maximum Nim with rule
function $f(x) = \lfloor x/2 \rfloor$, a pile of $5$ stones has Grundy number $1$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (characteristic values).

Formalized by `MetaMathlibExt.maximumNimGrundy_div_two_five`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-div-two-five).

## Grundy number of a pile of four in halving Maximum Nim

In Maximum Nim with rule
function $f(x) = \lfloor x/2 \rfloor$, a pile of $4$ stones has Grundy number $2$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (characteristic values).

Formalized by `MetaMathlibExt.maximumNimGrundy_div_two_four`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-div-two-four).

## Grundy number of a pile of three in halving Maximum Nim

In Maximum Nim with rule
function $f(x) = \lfloor x/2 \rfloor$, a pile of $3$ stones has Grundy number $0$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (characteristic values).

Formalized by `MetaMathlibExt.maximumNimGrundy_div_two_three`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-div-two-three).

## The Maximum Nim game

For a rule function $f : \mathbb{N} \to \mathbb{N}$, the Maximum Nim
game with rule $f$ is the impartial game whose positions are the pile sizes $x \in \mathbb{N}$, in
which the moves from $x$ go to $x - u$ for each $u$ with $1 \le u \le \min(f(x), x)$. The rank of
a position is the pile size itself, and the starting position is the empty pile $0$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimGame`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-game).

## P-positions of Maximum Nim

Let $f : \mathbb{N} \to \mathbb{N}$ be a rule function and let
$x$ be a pile size. The position $x$ of the Maximum Nim game with rule $f$ is a P-position
if and only if, for every $u$ with $1 \le u \le \min(f(x), x)$, the position $x - u$ is not
a P-position.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 2.

Formalized by `MetaMathlibExt.maximumNimGame_isP_iff`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-game-is-p-iff).

## The Maximum Nim map $h_k$

For natural numbers $k$ and $x$, let
$h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$. The paper takes $k \ge 2$; for $k \le 1$ the definition
gives $h_k(x) = x + 1$, because $k - 1$ is truncated to $0$ and $\lfloor x/0 \rfloor$ is taken to
be $0$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Definition 3.1.

Formalized by `MetaMathlibExt.maximumNimH`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h).

## The value $h_3(0) = 1$ of the Maximum Nim map

For the map
$h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ on the natural numbers, we have $h_3(0) = 1$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Definition 3.1.

Formalized by `MetaMathlibExt.maximumNimH_three_zero`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-three-zero).

## The value $h_3(2) = 4$ of the Maximum Nim map

For the map
$h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ on the natural numbers, we have $h_3(2) = 4$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Definition 3.1.

Formalized by `MetaMathlibExt.maximumNimH_three_two`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-three-two).

## Fuel-bounded Josephus simulation

For natural numbers $k$ and $s$ (the starting
position), a fuel $f$ and a list $c$ of natural numbers (the current circle), the simulation
returns the empty list when $f = 0$ or $c$ is empty. Otherwise, with $L$ the length of $c$ and
$i = (s + k - 1) \bmod L$, where the subtraction is truncated at $0$, it returns the entry of
$c$ at zero-based position $i$ followed by the result of the simulation with the same $k$,
starting position $i$ and fuel $f - 1$ on the list obtained from $c$ by deleting the entry at
position $i$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem).

Formalized by `MetaMathlibExt.josephusEliminationOrderAux`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-aux).

## Josephus elimination order

For natural numbers $k$ and $n$, place $1, \dots, n$ in
order on a circle and repeatedly remove one entry. When $L$ entries remain and the current
position is $s$ (zero-based, initially $s = 0$), the entry at zero-based position
$i = (s + k - 1) \bmod L$ is removed, where the subtraction is truncated at $0$, and $i$ becomes
the current position, so the next count starts at the entry after the removed one. The
Josephus elimination order with step $k$ on the circle $1, \dots, n$ is the list of all $n$
entries in the order of their removal.

For $k \ge 1$ this is the classical process that removes every $k$-th remaining entry; the last
entry of the list is the survivor.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem).

Formalized by `MetaMathlibExt.josephusEliminationOrder`, a definition declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order).

## Josephus elimination order for ten people and step three

The Josephus elimination order
with step $3$ on the circle $1, \dots, 10$ is $3, 6, 9, 2, 7, 1, 8, 5, 10, 4$: the entries are
removed in the order $3, 6, 9, 2, 7, 1, 8, 5, 10$, and the survivor $4$ comes last.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem example).

Formalized by `MetaMathlibExt.josephusEliminationOrder_three_ten`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-three-ten).

## Josephus elimination order for three people and step two

The Josephus elimination
order with step $2$ on the circle $1, 2, 3$ is $2, 1, 3$: the entry $2$ is removed first, then
the entry $1$, and the survivor $3$ comes last.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (characteristic values).

Formalized by `MetaMathlibExt.josephusEliminationOrder_two_three`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-two-three).

## Length of the Josephus elimination order

For all natural numbers $k$ and $n$, the
Josephus elimination order with step $k$ on the circle $1, \dots, n$ has exactly $n$ entries.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem).

Formalized by `MetaMathlibExt.josephusEliminationOrder_length`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-length).

## The Josephus elimination order is a permutation of the circle

For all natural numbers
$k$ and $n$, the Josephus elimination order with step $k$ on the circle $1, \dots, n$ is a
permutation of the list $1, 2, \dots, n$; in particular, each of $1, \dots, n$ occurs in it
exactly once.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem).

Formalized by `MetaMathlibExt.josephusEliminationOrder_perm`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-perm).

## The survivor is the last entry of the Josephus elimination order

For natural numbers
$k \ge 1$ and $n \ge 1$, the Josephus elimination order with step $k$ on the circle
$1, \dots, n$ is nonempty and its last entry is $J_k(n)$, the value at $n$ of the Josephus
function for elimination step $k$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Section 3 (Josephus problem).

Formalized by `MetaMathlibExt.josephusEliminationOrder_getLast?`, a theorem declared in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-elimination-order-get-last).

## Grundy value zero characterizes P-positions in Maximum Nim

Let $f : \mathbb{N} \to
\mathbb{N}$ satisfy $f(0) = 0$ and $f(m-1) \le f(m) \le f(m-1) + 1$ for every $m \ge 1$. Then for
every pile size $x \in \mathbb{N}$, the Grundy number of $x$ in Maximum Nim with rule function $f$
is $0$ if and only if $x$ is a P-position (a previous-player win under normal play) of that game.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Theorem 1.

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_eq_zero_iff_isP` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-eq-zero-iff-is-p).

## Grundy number where the rule function increases

Let $f : \mathbb{N} \to \mathbb{N}$
satisfy $f(0) = 0$ and $f(m-1) \le f(m) \le f(m-1) + 1$ for every $m \ge 1$, and let $G$ be the
Grundy number of Maximum Nim with rule function $f$. If $x \ge 1$ and $f(x-1) < f(x)$, then
$G(x) = f(x)$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 1(i).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_eq_rule_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-eq-rule-of-lt).

## Grundy number where the rule function is flat

Let $f : \mathbb{N} \to \mathbb{N}$
satisfy $f(0) = 0$ and $f(m-1) \le f(m) \le f(m-1) + 1$ for every $m \ge 1$, and let $G$ be the
Grundy number of Maximum Nim with rule function $f$. If $x \ge 1$ and $f(x) = f(x-1)$, then
$G(x) = G(x - f(x) - 1)$.

Here $x - f(x) - 1 \ge 0$, since the hypotheses give $f(x) = f(x-1) \le x - 1$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 1(ii).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_eq_sub_rule_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-eq-sub-rule-succ).

## Floor identity for non-multiples in Maximum Nim

Let $k \ge 2$ and $x$ be natural numbers
such that $x$ is not a multiple of $k$. Then
$x - \lfloor x/k \rfloor - 1 = \lfloor (k-1)x/k \rfloor$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 2.

Stated but not proved: `MetaMathlibExt.maximumNim_sub_div_sub_one_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-sub-div-sub-one-eq).

## Maximum Nim Grundy numbers at multiples of the divisor

Let $k \ge 2$ and let $G$ be
the Grundy number of Maximum Nim with rule function $f(y) = \lfloor y/k \rfloor$. Every positive
multiple $x$ of $k$ satisfies $G(x) = x/k$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 3(i).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_div_eq_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-div-eq-of-dvd).

## Maximum Nim Grundy numbers at non-multiples of the divisor

Let $k \ge 2$ and let $G$
be the Grundy number of Maximum Nim with rule function $f(y) = \lfloor y/k \rfloor$. If $x$ is a
natural number not divisible by $k$, then $G(x) = G(\lfloor (k-1)x/k \rfloor)$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 3(ii).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_eq_F_of_not_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-eq-f-of-not-dvd).

## Floor-rule Maximum Nim: positions below k have Grundy number zero

For every natural
number $k \ge 2$ and every natural number $j$ with $1 \le j \le k$, a pile of $k - j$ stones has
Grundy number $0$ in Maximum Nim with rule function $f(y) = \lfloor y/k \rfloor$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 3(iii).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_sub_eq_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-sub-eq-zero).

## A Maximum Nim non-divisibility lemma for $s < t$

Let $k, n, t, h, s, i$ be natural
numbers with $h \ge 1$, $k = nt + h$, $h \le n$ and $s < t$. If $1 \le i \le n$, then $k$ does
not divide $n(k - s) - i$.

The hypotheses force $n \ge 1$, $s < k$ and $i \le n(k - s)$, so both subtractions are ordinary
differences of natural numbers.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 4(i).

Stated but not proved: `MetaMathlibExt.maximumNim_not_dvd_mul_sub_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-not-dvd-mul-sub-of-lt).

## A Maximum Nim non-divisibility lemma for $i \ne h$

Let $k, n, t, h, i$ be natural numbers
with $t \ge 1$, $h \ge 1$, $k = nt + h$ and $h \le n$. If $1 \le i \le n$ and $i \ne h$, then $k$
does not divide $n(k - t) - i$.

The hypotheses force $n \ge 1$, $t \le k$ and $i \le n(k - t)$, so both subtractions are ordinary
differences of natural numbers.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 4(ii).

Stated but not proved: `MetaMathlibExt.maximumNim_not_dvd_mul_sub_of_ne` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-not-dvd-mul-sub-of-ne).

## Floor-rule Maximum Nim: Grundy reduction when $n = kt + u$

Let $k$, $t$, $u$ and $n$ be
natural numbers with $k \ge 2$, $t \ge 1$, $u \le k - 1$ and $n = kt + u$. Write $G(x)$ for the
Grundy number of a pile of $x$ stones in Maximum Nim with rule function
$f(y) = \lfloor y/k \rfloor$. Then for every natural number $i$ with $1 \le i \le n$ that is not
divisible by $k$,

$$G(nk - i) = G\bigl((n - t)k - (u + i - \lfloor i/k \rfloor)\bigr).$$

The hypotheses force $i \le nk$ and $u + i - \lfloor i/k \rfloor \le (n - t)k$, so all
subtractions are ordinary differences of natural numbers. The right side is read with the
parentheses shown; read without them, as in the extracted statement, the equality is false.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 5(i).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_mul_sub_eq_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-mul-sub-eq-decomposit).

## Floor-rule Maximum Nim: one-step Grundy reduction when k = nt + h

Let $n$, $t$, $h$ be
natural numbers with $t \ge 1$ and $1 \le h \le n$, and let $k = nt + h$. Write $G(x)$ for the
Grundy number of a pile of $x$ stones in Maximum Nim with rule function
$f(y) = \lfloor y/k \rfloor$, and let $F(x) = \lfloor (k-1)x/k \rfloor$. Then for every natural
number $i$ with $1 \le i \le n$,

$$G(nk - i) = G(F(nk - i)) = G(n(k - 1) - i).$$

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 5(ii.1).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_mul_sub_eq_F_eq_pred` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-mul-sub-eq-f-eq-pred).

## Floor-rule Maximum Nim: t-step Grundy reduction when k = nt + h

Let $n$, $t$, $h$ be
natural numbers with $t \ge 1$ and $1 \le h \le n$, and let $k = nt + h$. Write $G(x)$ for the
Grundy number of a pile of $x$ stones in Maximum Nim with rule function
$f(y) = \lfloor y/k \rfloor$, let $F(x) = \lfloor (k-1)x/k \rfloor$, and let $F^t$ be the $t$-fold
iterate of $F$. Then for every natural number $i$ with $1 \le i \le n$,

$$G(nk - i) = G(F^t(nk - i)) = G(n(k - t) - i).$$

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 5(ii.2).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_mul_sub_eq_iterate_F` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-mul-sub-eq-iterate-f).

## Floor-rule Maximum Nim: (t+1)-step Grundy reduction when k = nt + h

Let $n$, $t$, $h$ be
natural numbers with $t \ge 1$ and $1 \le h \le n$, and let $k = nt + h$. Write $G(x)$ for the
Grundy number of a pile of $x$ stones in Maximum Nim with rule function
$f(y) = \lfloor y/k \rfloor$, let $F(x) = \lfloor (k-1)x/k \rfloor$, and let $F^{t+1}$ be the
$(t+1)$-fold iterate of $F$. Then for every natural number $i$ with $1 \le i \le h - 1$,

$$G(nk - i) = G(F^{t+1}(nk - i)) = G((n - 1)k - (n - h + i)).$$

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 5(ii.3).

Stated but not proved: `MetaMathlibExt.maximumNimGrundy_mul_sub_eq_succ_iterate_F` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-grundy-mul-sub-eq-succ-itera).

## The Maximum Nim map $h_k$ is strictly increasing

Let $k \ge 2$ be a natural number and
let $h_k$ be the map $x \mapsto x + \lfloor x/(k-1) \rfloor + 1$ on the natural numbers. For all
natural numbers $x$ and $x'$ with $x < x'$, we have $h_k(x) < h_k(x')$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 6(i).

Stated but not proved: `MetaMathlibExt.maximumNimH_strictMono` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-strict-mono).

## The Maximum Nim map $h_k$ exceeds its argument

Let $k \ge 2$ be a natural number and let
$h_k$ be the map $x \mapsto x + \lfloor x/(k-1) \rfloor + 1$ on the natural numbers. Every natural
number $x$ satisfies $x < x + 1 \le h_k(x)$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 6(ii).

Stated but not proved: `MetaMathlibExt.maximumNimH_succ_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-succ-le).

## Iterates of the Maximum Nim map $h_k$ tend to infinity

Let $k \ge 2$ be a natural
number and let $h_k$ be the map $x \mapsto x + \lfloor x/(k-1) \rfloor + 1$ on the natural numbers.
For every natural number $x_0$, the iterates $h_k^p(x_0)$ tend to infinity as $p \to \infty$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 6(iii).

Stated but not proved: `MetaMathlibExt.maximumNimH_iterate_tendsto_atTop` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-iterate-tendsto-at-top).

## Linear bounds on h_k and their iterates

Let $k \ge 2$ be a natural number, let
$h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ on natural numbers, and define the real maps
$h_k^-(x) = x + \frac{x}{k-1}$ and $h_k^+(x) = x + \frac{x}{k-1} + 1$. Writing $g^p$ for the
$p$-fold iterate of a map $g$, for all natural numbers $p$ and $x$: (i)
$(h_k^-)^p(x) = \left(\frac{k}{k-1}\right)^p x$, (ii)
$(h_k^+)^p(x) = \left(\frac{k}{k-1}\right)^p (x + k - 1) - (k - 1)$, and (iii)
$h_k^-(x) \le h_k(x) \le h_k^+(x)$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 7.

Stated but not proved: `MetaMathlibExt.maximumNimH_iterate_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-iterate-bounds).

## Josephus elimination positions as Maximum Nim Grundy numbers

Let $k \ge 2$ and
$1 \le m \le n$. Write $o_n(m)$ for the position, counting from $1$, at which $m$ appears in the
Josephus elimination order of the circle $1, \dots, n$ in which every $k$-th person is removed
and the survivor is listed last, and write $G$ for the Grundy number of Maximum Nim with rule
function $f(y) = \lfloor y/k \rfloor$. Then $n - o_n(m) = G(nk - m)$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Theorem 2.

Stated but not proved: `MetaMathlibExt.josephus_position_complement_eq_maximumNimGrundy` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-position-complement-eq-maximum).

## Josephus survivor via iteration from zero

Let $k \ge 2$ and $n \ge 1$ be natural
numbers, let $h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ for natural numbers $x$, and write
$h_k^p$ for the $p$-th iterate of $h_k$. Then there is a natural number $p \ge 1$ with
$h_k^{p-1}(0) < n(k-1) \le h_k^p(0)$ and $J_k(n) = nk - h_k^p(0)$, where $J_k$ is the Josephus
function for elimination step $k$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Theorem 3.

Stated but not proved: `MetaMathlibExt.josephus_eq_mul_sub_iterate_maximumNimH_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-eq-mul-sub-iterate-maximum-nim).

## Josephus survivor via the shifted iteration

Let $k \ge 2$ and $n \ge 2$ be natural
numbers, let $h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ for natural numbers $x$, and write
$h_k^p$ for the $p$-th iterate of $h_k$. Then there is a natural number $p \ge 1$ with
$h_k^{p-1}(k-1) < n(k-1) \le h_k^p(k-1)$ and $J_k(n) = nk - h_k^p(k-1)$, where $J_k$ is the
Josephus function for elimination step $k$.

The hypothesis $n \ge 2$ is needed: for $n = 1$ every $p \ge 1$ has
$h_k^{p-1}(k-1) \ge k - 1 = n(k-1)$, so no such $p$ exists.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Corollary 1.

Stated but not proved: `MetaMathlibExt.josephus_eq_mul_sub_iterate_maximumNimH_pred` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-eq-mul-sub-iterate-maximum-nim-2).

## Logarithmic bounds on the iterates of h_k

Let $k \ge 2$ and $n \ge 1$ be natural numbers,
let $h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ on natural numbers, write $h_k^p$ for its $p$-fold
iterate, and let

$$v = \frac{\log n}{\log k - \log(k-1)}, \qquad w = \frac{\log(n+1) - \log 2}{\log k - \log(k-1)},$$

where $\log$ is the natural logarithm. Then

$$h_k^{\lfloor w \rfloor}(k-1) \le n(k-1) \le h_k^{\lceil v \rceil}(k-1).$$

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Lemma 8.

Stated but not proved: `MetaMathlibExt.maximumNimH_iterate_floor_le_mul_le_iterate_ceil` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#maximum-nim-h-iterate-floor-le-mul-le-it).

## Logarithmic bounds for the Josephus iteration count

Let $k \ge 2$ and $n \ge 2$ be
natural numbers, let $h_k(x) = x + \lfloor x/(k-1) \rfloor + 1$ for natural numbers $x$, write
$h_k^p$ for the $p$-th iterate of $h_k$, and define the real numbers
$v = \log n / (\log k - \log(k-1))$ and $w = (\log(n+1) - \log 2) / (\log k - \log(k-1))$,
where $\log$ is the natural logarithm. Then there is a natural number $p \ge 1$ with
$\lfloor w \rfloor \le p \le \lceil v \rceil$ and $J_k(n) = nk - h_k^p(k-1)$, where $J_k$ is the
Josephus function for elimination step $k$.

The hypothesis $n \ge 2$ is needed: for $n = 1$ we have $v = 0$, so $\lceil v \rceil = 0$ and no
$p \ge 1$ satisfies $p \le \lceil v \rceil$.

## Sources

- Shoei Takahashi, Hikaru Manabe, Ryohei Miyadera, *Maximum Nim and the Josephus Problem*, INTEGERS 24 (2024), Article G5, Theorem 4.

Stated but not proved: `MetaMathlibExt.josephus_eq_mul_sub_iterate_maximumNimH_between_log_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximumNimJosephusWanted.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MaximumNimJosephusWanted.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html#josephus-eq-mul-sub-iterate-maximum-nim-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum Nim](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/maximum-nim/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/maximum-nim)
