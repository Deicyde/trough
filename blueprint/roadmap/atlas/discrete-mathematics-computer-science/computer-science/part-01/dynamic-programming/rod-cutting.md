---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.RodCutting.compositionRevenue, Cslib.Algorithms.Lean.RodCutting.compositionRevenue_zero, Cslib.Algorithms.Lean.RodCutting.compositionRevenue_single, Cslib.Algorithms.Lean.RodCutting.compositionRevenue_append, Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod, Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_correct, Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_zero, Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_time_sum
statement: formalized
proof: formalized
---

# Rod cutting

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html).

## Revenue of a rod composition

Let $p = (p_0, \dots, p_{n-1})$ be a price vector with
entries in an additive commutative monoid, where $p_{\ell - 1}$ is the price of a piece of length
$\ell$. For $k \le n$ and a composition $(b_1, \dots, b_m)$ of $k$ into positive parts, its revenue
is $p_{b_1 - 1} + \dots + p_{b_m - 1}$, the total price of its pieces.

Formalized by `Cslib.Algorithms.Lean.RodCutting.compositionRevenue`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#composition-revenue).

## The empty rod earns nothing

Let $p = (p_1, \dots, p_n)$ be prices in an additive
commutative monoid. Every composition of $0$, namely the empty one, has revenue $0$ with respect
to $p$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.compositionRevenue_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#composition-revenue-zero).

## Revenue of an uncut rod

Let $p = (p_1, \dots, p_n)$ be prices in an additive commutative
monoid, $p_i$ being the price of a piece of length $i$. For $0 < k \le n$, the revenue of the
one-part composition $(k)$ of $k$ is $p_k$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.compositionRevenue_single`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#composition-revenue-single).

## Revenue is additive under concatenation

Let $p = (p_1, \dots, p_n)$ be prices in an
additive commutative monoid, and define the revenue of a composition $(b_1, \dots, b_m)$ of some
$k \le n$ to be $p_{b_1} + \dots + p_{b_m}$. If $c$ is a composition of $k$ and $d$ is a
composition of $l$ with $k + l \le n$, then the revenue of their concatenation, a composition of
$k + l$, is the revenue of $c$ plus the revenue of $d$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.compositionRevenue_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#composition-revenue-append).

## Bottom-up rod cutting

Given prices $p = (p_1, \dots, p_n)$ in an additive commutative
monoid $\alpha$ with a linear order, $p_i$ being the price of a piece of length $i$, bottom-up rod
cutting fills a table $r_0, \dots, r_n$ in increasing order by $r_0 = 0$ and
$r_j = \max_{1 \le i \le j} (p_i + r_{j-i})$ for $1 \le j \le n$, and returns $r_n$. Its cost is
the number of candidates $p_i + r_{j-i}$ it evaluates, one for each pair $1 \le i \le j \le n$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod).

## Correctness of bottom-up rod cutting

Let $\alpha$ be an additive commutative monoid with a
linear order in which addition is monotone, and let $p = (p_1, \dots, p_n)$ be prices in $\alpha$,
$p_i$ being the price of a piece of length $i$. The value returned by bottom-up rod cutting on $p$
is the greatest revenue of a composition of $n$: it equals $p_{b_1} + \dots + p_{b_m}$ for some
composition $(b_1, \dots, b_m)$ of $n$ into positive parts, and it is at least this sum for every
such composition.

Prices may be negative; every piece of the rod must be sold, so there is no option to discard
material.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-correct).

## Bottom-up rod cutting on the empty rod

For the empty price vector ($n = 0$) over an
additive commutative monoid with a linear order, bottom-up rod cutting returns $0$ at cost $0$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-zero).

## Cost of bottom-up rod cutting as a sum over rows

For prices $p = (p_1, \dots, p_n)$ in an
additive commutative monoid with a linear order, the cost of bottom-up rod cutting on $p$ (the
number of first-piece candidates it evaluates) equals $\sum_{j=0}^{n} j$.

Row $j$ of the table contributes the $j$ candidates of its scan.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_time_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-time-sum).

## Twice the cost of bottom-up rod cutting

For prices $p = (p_1, \dots, p_n)$ in an additive
commutative monoid with a linear order, the cost $T$ of bottom-up rod cutting on $p$ (the number of
first-piece candidates it evaluates) satisfies $2T = n(n + 1)$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_time_twice`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-time-twice).

## Exact cost of bottom-up rod cutting

For prices $p = (p_1, \dots, p_n)$ in an additive
commutative monoid with a linear order, the cost of bottom-up rod cutting on $p$ (the number of
first-piece candidates it evaluates) is the triangular number $n(n + 1)/2$, whatever the prices.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-time).

## Bottom-up rod cutting takes quadratic time

For prices $p = (p_1, \dots, p_n)$ in an
additive commutative monoid with a linear order, the cost $T$ of bottom-up rod cutting on $p$, the
number of first-piece candidates it evaluates, satisfies $n^2 \le 2T$ and $T \le n^2$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.bottomUpCutRod_time_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#bottom-up-cut-rod-time-bounds).

## Extended bottom-up rod cutting

Let $\alpha$ be an additive commutative monoid with a
linear order, and let $p_1, \dots, p_n \in \alpha$ be the prices of pieces of length
$1, \dots, n$ (the price vector's entry $i - 1$ is $p_i$). The algorithm fills a revenue table
$r_0, \dots, r_n$ and a first-cut table $s_1, \dots, s_n$ for the lengths $j = 0, 1, \dots, n$ in
increasing order: $r_0 = 0$, and for $j \ge 1$ it scans the candidates $p_i + r_{j-i}$ for
$i = 1, \dots, j$ in increasing order of $i$, starting from the candidate for $i = 1$ and moving
to a later candidate only when it is strictly larger than the current one. Then $r_j$ is the
largest candidate and $s_j$ is the least $i$ whose candidate equals $r_j$. The result is the pair
of tables, where $r_j$ is the revenue vector's entry $j$ and $s_j$ is the cut vector's entry
$j - 1$, and the cost is one tick per evaluated candidate, so $j$ ticks for length $j$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod).

## Saved revenues are optimal

Let $p$ be a price vector of length $n$ with entries in a
linearly ordered additive commutative monoid (addition is monotone), and let
$r = (r_0, \dots, r_n)$ be the revenue table computed by the extended bottom-up rod-cutting
algorithm. For every $j \le n$, $r_j$ is the greatest revenue of a composition of $j$: some
composition of $j$ has revenue $r_j$, and every composition of $j$ has revenue at most $r_j$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod-correct).

## The extended algorithm computes the same revenue

For every price vector of length $n$
with entries in an additive commutative monoid carrying a linear order, the last entry $r_n$ of
the revenue table computed by the extended bottom-up rod-cutting algorithm equals the value
returned by the bottom-up rod-cutting algorithm.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod_revenue_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod-revenue-eq).

## Running time of extended bottom-up rod cutting

Let $\alpha$ be an additive commutative
monoid with a linear order. For every vector of $n$ prices in $\alpha$, the extended bottom-up
rod-cutting algorithm has cost exactly $n(n+1)/2$, whatever the prices are.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod-time).

## Extended bottom-up rod cutting on the empty rod

Let $\alpha$ be an additive commutative
monoid with a linear order. On the empty price vector (rod length $0$), the extended bottom-up
rod-cutting algorithm returns the revenue table whose single entry is $0$ together with the empty
first-cut table, at cost $0$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod-zero).

## The saved first cut attains the saved revenue

Let $p = (p_0, \dots, p_{n-1})$ be a
price vector with entries in an additive commutative monoid carrying a linear order, where
$p_{\ell - 1}$ is the price of a piece of length $\ell$. Let $r = (r_0, \dots, r_n)$ be the
revenue table and $s = (s_1, \dots, s_n)$ the saved first cuts computed by the extended bottom-up
rod-cutting algorithm, with $s_j$ stored as entry $j - 1$ of the cut vector. For every $j$ with
$0 < j \le n$, the cut $\ell = s_j$ satisfies $1 \le \ell \le j$ and
$p_{\ell - 1} + r_{j - \ell} = r_j$, and every $\ell'$ with $1 \le \ell' < \ell$ satisfies
$p_{\ell' - 1} + r_{j - \ell'} < r_j$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.extendedBottomUpCutRod_firstCut`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#extended-bottom-up-cut-rod-first-cut).

## Rod cutting with reconstruction

Given a price vector $p$ of length $n$ with entries in an
additive commutative monoid carrying a linear order, where entry $\ell - 1$ is the price of a
piece of length $\ell$, first run the extended bottom-up rod-cutting algorithm to obtain the saved
first cuts $s_1, \dots, s_n$ (with $s_j$ stored as entry $j - 1$ of its cut vector). Then,
starting from the remaining length $L = n$, repeatedly emit a piece of length $s_L$ and replace
$L$ by $L - s_L$ until $L = 0$. The result is the composition of $n$ formed by the emitted pieces
in order. Its cost is the cost of the extended algorithm plus one event per emitted piece;
allocation and arithmetic are free.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution).

## Cost of rod-cutting reconstruction

Let $p$ be a price vector of length $n$ with entries
in an additive commutative monoid carrying a linear order. The rod-cutting reconstruction charges
exactly $n(n+1)/2 + m$ events, where $m$ is the number of pieces of the composition of $n$ it
returns: one event per evaluated first-cut candidate and one per emitted piece.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution-time).

## Reconstructed pieces are the saved first cuts

Let $p$ be a price vector of length $n$
with entries in an additive commutative monoid carrying a linear order. Let $s$ be the vector of
saved first cuts computed by the extended bottom-up rod-cutting algorithm, of length $n$, whose
entry $j - 1$ is the cut saved for length $j$, and let $(b_0, \dots, b_{m-1})$ be the composition
of $n$ returned by the rod-cutting reconstruction. For every $i < m$, the index
$n - (b_0 + \dots + b_{i-1}) - 1$ lies within $s$ and the entry of $s$ at this index is $b_i$:
the $i$-th piece is the first cut saved for the remaining length $n - (b_0 + \dots + b_{i-1})$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution_blocks`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution-blocks).

## Reconstruction earns the final saved revenue

Let $p$ be a price vector of length $n$
with entries in an additive commutative monoid carrying a linear order, and let
$r = (r_0, \dots, r_n)$ be the revenue table computed by the extended bottom-up rod-cutting
algorithm. The revenue of the composition of $n$ returned by the rod-cutting reconstruction
equals $r_n$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution_revenue`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution-revenue).

## Rod-cutting reconstruction is optimal

Let $p$ be a price vector of length $n$ with
entries in a linearly ordered additive commutative monoid (addition is monotone). The composition
of $n$ returned by the rod-cutting reconstruction has the greatest revenue among all compositions
of $n$: its revenue is at least the revenue of every composition of $n$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution-correct).

## Rod-cutting reconstruction on the empty rod

For the empty price vector (rod length
$0$) with entries in an additive commutative monoid carrying a linear order, the rod-cutting
reconstruction returns the empty composition of $0$ and charges no events.

Formalized by `Cslib.Algorithms.Lean.RodCutting.cutRodSolution_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCutting.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#cut-rod-solution-zero).

## Recursive CUT-ROD

Let $\alpha$ be an additive commutative monoid with a linear order,
and let $p_1, \dots, p_n \in \alpha$ be prices, $p_i$ being the price of a piece of length $i$.
Recursive CUT-ROD returns $r(n)$, where $r(0) = 0$ and, for $1 \le j \le n$,
$r(j) = \max(p_1 + r(j - 1), p_2 + r(j - 2), \dots, p_j + r(0))$. The first cuts
$i = 1, \dots, j$ are scanned in increasing order and every $r(j - i)$ is recomputed by a fresh
recursive call, without memoization. One cost tick is charged at every invocation, including
the root call and every call on an empty rod.

Formalized by `Cslib.Algorithms.Lean.RodCutting.recursiveCutRod`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#recursive-cut-rod).

## Correctness of recursive CUT-ROD

Let $\alpha$ be an additive commutative monoid with a
linear order for which addition is monotone, and let $p_1, \dots, p_n \in \alpha$ be prices,
$p_i$ being the price of a piece of length $i$. The value returned by recursive CUT-ROD on these
prices is the greatest revenue of a composition of $n$: it equals the revenue
$p_{i_1} + \dots + p_{i_k}$ of some composition $n = i_1 + \dots + i_k$ into positive parts,
and it is at least the revenue of every such composition.

Every piece is sold: negative prices do not create an option to discard part of the rod.

Formalized by `Cslib.Algorithms.Lean.RodCutting.recursiveCutRod_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#recursive-cut-rod-correct).

## Running time of recursive CUT-ROD

Let $\alpha$ be an additive commutative monoid with a
linear order, and let $p_1, \dots, p_n \in \alpha$ be prices. Recursive CUT-ROD on these prices,
which charges one tick per invocation, makes exactly $2^n$ invocations, counting the root call
and every call on an empty rod, whatever the prices are.

Formalized by `Cslib.Algorithms.Lean.RodCutting.recursiveCutRod_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RecursiveRodCutting.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#recursive-cut-rod-time).

## Memoized rod-cutting auxiliary (CLRS MEMOIZED-CUT-ROD-AUX)

Let $\alpha$ be an additive
commutative monoid with a linear order, let $p = (p_1, \dots, p_n) \in \alpha^n$ be prices, where
$p_i$ is the price of a piece of length $i$, and let $c = (c_0, \dots, c_n)$ be a cache whose
entries are each either unknown or a value in $\alpha$. For $j \le n$ the procedure returns a value
and an updated cache, and counts events, as follows. It first charges one event for probing $c_j$.
If $c_j$ is a known value $v$, it returns $v$ and the unchanged cache $c$. Otherwise, if $j = 0$,
it charges one event for a write and returns $0$ with $c_0$ set to $0$. If $j \ge 1$, then for
$i = 1, \dots, j$ in turn it calls itself on length $j - i$ with the cache returned by the previous
call (starting from $c$), obtaining a value $q_i$, and charges one event for the candidate
$p_i + q_i$. It then charges one event for a write and returns
$q = \max(p_1 + q_1, \dots, p_j + q_j)$ with entry $j$ of the last returned cache set to $q$. The
event count is the total over the whole recursion.

Known entries are returned as they are, whatever their sign, including at length zero.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRodAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-aux).

## The memoized cut-rod procedure (CLRS MEMOIZED-CUT-ROD)

Let $\alpha$ be an additive
commutative monoid with a linear order and let $p = (p_1, \dots, p_n) \in \alpha^n$ be prices, where
$p_i$ is the price of a piece of length $i$. The procedure runs the memoized rod-cutting auxiliary
on length $n$ with the cache $(c_0, \dots, c_n)$ whose entries are all unknown, and returns the
value it computes, discarding the final cache. Its event count is that of the auxiliary call.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRod`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod).

## A cache hit in memoized rod cutting returns at once

Let $\alpha$ be an additive commutative
monoid with a linear order, let $p \in \alpha^n$ be a vector of prices, let $c = (c_0, \dots, c_n)$
be a cache whose entries are each unknown or a value in $\alpha$, and let $j \le n$. If $c_j$ is a
known value $v$, then the memoized rod-cutting auxiliary on length $j$ and cache $c$ returns $v$
and the unchanged cache $c$, and charges exactly one event.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRodAux_hit`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-aux-hit).

## The memoized auxiliary preserves known and higher cache entries

Let $\alpha$ be an additive
commutative monoid with a linear order, let $p \in \alpha^n$ be a vector of prices, let
$c = (c_0, \dots, c_n)$ be a cache whose entries are each unknown or a value in $\alpha$, let
$j \le n$, and let $c'$ be the cache returned by the memoized rod-cutting auxiliary on length $j$
and cache $c$. Then for every $k \le n$, if $c_k$ is a known value $v$, then $c'_k = v$; and for
every $k$ with $j < k \le n$, $c'_k = c_k$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRodAux_preserves`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-aux-preserves).

## Memoized rod cutting on the empty rod

Let $\alpha$ be an additive commutative monoid with
a linear order. For the empty price vector ($n = 0$), the memoized cut-rod procedure returns $0$
and charges exactly $2$ events: one cache probe and one cache write.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRod_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-zero).

## Correctness of the memoized rod-cutting auxiliary

Let $\alpha$ be a linearly ordered
additive commutative monoid (that is, $a \le b$ implies $a + c \le b + c$) and let
$p = (p_1, \dots, p_n) \in \alpha^n$ be prices, where $p_i$ is the price of a piece of length $i$.
Call a cache $c = (c_0, \dots, c_n)$, whose entries are each unknown or a value in $\alpha$, valid
if for every known entry $c_k = v$ the value $v$ is the greatest composition revenue over
compositions of $k$. If $c$ is valid, $j \le n$, and the memoized rod-cutting auxiliary on length
$j$ and cache $c$ returns the value $q$ and the cache $c'$, then $q$ is the greatest composition
revenue over compositions of $j$, the cache $c'$ is valid, and $c'_j = q$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRodAux_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-aux-correct).

## Correctness of memoized rod cutting

Let $\alpha$ be a linearly ordered additive commutative
monoid (that is, $a \le b$ implies $a + c \le b + c$) and let $p = (p_1, \dots, p_n) \in \alpha^n$
be prices, where $p_i$ is the price of a piece of length $i$. The value returned by the memoized
cut-rod procedure on $p$ is the greatest composition revenue over compositions of $n$: it is the
revenue of some composition of $n$, and it is at least the revenue of every composition of $n$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRod_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-correct).

## The memoized auxiliary fills the cache up to the requested length

Let $\alpha$ be a
linearly ordered additive commutative monoid (that is, $a \le b$ implies $a + c \le b + c$), let
$p = (p_1, \dots, p_n) \in \alpha^n$ be prices, where $p_i$ is the price of a piece of length $i$,
and let $j \le n$. If the memoized rod-cutting auxiliary is run on length $j$ with the cache
$(c_0, \dots, c_n)$ whose entries are all unknown, then for every $k \le j$ entry $k$ of the
returned cache is a known value, and that value is the greatest composition revenue over
compositions of $k$.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRodAux_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-aux-complete).

## Event count of memoized rod cutting

Let $\alpha$ be an additive commutative monoid with a
linear order and let $p \in \alpha^n$ be a vector of prices. The memoized cut-rod procedure on $p$
charges exactly $n^2 + 2n + 2$ events, where one event is charged per cache probe, per first-cut
candidate, and per cache write.

Allocation, initialization, arithmetic, comparisons and control are not charged.

Formalized by `Cslib.Algorithms.Lean.RodCutting.memoizedCutRod_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/RodCuttingMemoized.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html#memoized-cut-rod-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rod cutting](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/rod-cutting/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/dynamic-programming/rod-cutting)
