---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Parallel.PrefixSum.seg, Cslib.Algorithms.Lean.Parallel.PrefixSum.prefixProd, Cslib.Algorithms.Lean.Parallel.PrefixSum.seg_mul_seg, Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone, Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone_eq_seg, Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone_eq_prefix, Cslib.Algorithms.Lean.Parallel.PrefixSum.roundWork, Cslib.Algorithms.Lean.Parallel.PrefixSum.roundWork_eq_card
statement: formalized
proof: formalized
---

# Parallel prefix sums

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html).

## Window product

For a sequence $x : \mathbb{N} \to M$ in a monoid $M$ and
$a, b \in \mathbb{N}$, the window product is the ordered product $x_a x_{a+1} \cdots x_{b-1}$ of
the terms with indices $a \le j < b$; it is the empty product $1$ when $b \le a$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.seg`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#seg).

## Prefix product

For a sequence $x_0, x_1, \dots$ in a monoid $M$ and a natural number $i$,
the prefix product at $i$ is $x_0 x_1 \cdots x_i$, the factors taken in increasing order of
index.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.prefixProd`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#prefix-prod).

## Products of adjacent windows

Let $M$ be a monoid and $x : \mathbb{N} \to M$ a sequence,
and for $a, b \in \mathbb{N}$ let $x_{[a, b)}$ be the ordered product $x_a x_{a+1} \cdots x_{b-1}$
(equal to $1$ if $b \le a$). For all $a \le b \le c$, $x_{[a, b)} \, x_{[b, c)} = x_{[a, c)}$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.seg_mul_seg`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#seg-mul-seg).

## The Kogge–Stone scan

Given a sequence $x_0, x_1, \dots$ in a monoid $M$, the value
$s_k(i)$ at position $i$ after $k$ rounds is defined by $s_0(i) = x_i$ and, for each $k$,
$s_{k+1}(i) = s_k(i - 2^k) \, s_k(i)$ if $2^k \le i$ and $s_{k+1}(i) = s_k(i)$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#kogge-stone).

## What the scan holds after each round

Let $x_0, x_1, \dots$ be a sequence in a monoid
$M$, let $k$ and $i$ be natural numbers, and let $m = \min(i + 1, 2^k)$. After $k$ rounds of the
Kogge–Stone scan, position $i$ holds the product $x_{i+1-m} \cdots x_i$ of the $m$ consecutive
inputs ending at $i$, taken in increasing order of index.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone_eq_seg`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#kogge-stone-eq-seg).

## The scan computes all prefix products

Let $x_0, x_1, \dots$ be a sequence in a monoid $M$
and let $n$ and $K$ be natural numbers with $n \le 2^K$. After $K$ rounds of the Kogge–Stone scan,
every position $i < n$ holds the prefix product $x_0 x_1 \cdots x_i$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone_eq_prefix`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#kogge-stone-eq-prefix).

## Work of a scan round

The work of round $k$ on $n$ positions is $\max(n - 2^k, 0)$, the
number of positions $i < n$ with $i \ge 2^k$, each of which performs one multiplication.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.roundWork`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#round-work).

## The work of a round counts its combining positions

For natural numbers $n$ and $k$, the
work of round $k$ on $n$ positions equals the number of positions $i$ with $2^k \le i < n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.roundWork_eq_card`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#round-work-eq-card).

## Work of the Kogge–Stone scan

The total work of $K$ rounds on $n$ positions is
$\sum_{k=0}^{K-1} \max(n - 2^k, 0)$, the sum over the rounds $k < K$ of the work
$\max(n - 2^k, 0)$ of round $k$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.work`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#work).

## Work bound for the Kogge–Stone scan

For all $n, K \in \mathbb{N}$, the total work of $K$
rounds of the scan on $n$ positions is at most $nK$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.work_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#work-le).

## Span of the Kogge–Stone scan

The span of $K$ rounds of the scan is $K$: each round is
one parallel step.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.span`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#span).

## The scan computes all prefixes in logarithmically many rounds

Let $x_0, x_1, \dots$ be a
sequence in a monoid $M$ and let $n$ be a natural number. After $\lceil \log_2 n \rceil$ rounds of
the Kogge–Stone scan (the least $K$ with $n \le 2^K$), every position $i < n$ holds the prefix
product $x_0 x_1 \cdots x_i$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.koggeStone_clog_eq_prefix`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#kogge-stone-clog-eq-prefix).

## One round of the scan on a list

Given a list $y_0, \dots, y_{n-1}$ in a monoid $M$ and a
natural number $k$, one round produces the list of length $n$ whose entry $i$ is
$y_{i - 2^k} \, y_i$ when $2^k \le i$ and $y_i$ when $i < 2^k$.

The list is traversed in lockstep with its own suffix starting at position $2^k$, so a round
costs $O(n)$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.roundList`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#round-list).

## Tabulated Kogge–Stone scan

For a list $y = (y_0, \dots, y_{n-1})$ in a monoid $M$, the
list after $K$ rounds is defined by recursion on $K$: after $0$ rounds it is $y$, and after
$K + 1$ rounds it is round $K$ applied to the list after $K$ rounds. Here round $k$ sends a list
$(z_0, \dots, z_{n-1})$ to the list of length $n$ whose entry $i$ is $z_i$ for $i < 2^k$ and
$z_{i - 2^k} z_i$ for $2^k \le i < n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.scanList`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#scan-list).

## The tabulated scan agrees with the round recursion

Let $x_0, \dots, x_{n-1}$ be a list of
elements of a monoid $M$, extended to a sequence by $x_j = 1$ for $j \ge n$. For every number of
rounds $K$ and every position $i < n$, entry $i$ of the list produced by $K$ rounds of the
tabulated scan equals the value at position $i$ after $K$ rounds of the Kogge–Stone scan applied
to the sequence $x$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.getD_scanList`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#get-d-scan-list).

## The tabulated scan computes all prefix products

Let $x_0, \dots, x_{n-1}$ be a list of
elements of a monoid $M$ and let $K$ be a natural number with $n \le 2^K$. Then for every $i < n$,
entry $i$ of the list produced by $K$ rounds of the tabulated scan equals the prefix product
$x_0 x_1 \cdots x_i$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.getD_scanList_eq_prefix`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/PrefixSum.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#get-d-scan-list-eq-prefix).

## Adjacent pair products of a sequence

For a sequence $x \colon \mathbb{N} \to M$ in a
monoid $M$, the sequence of adjacent pair products is the sequence whose term at $i$ is
$x(2i) \cdot x(2i+1)$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.pairUp`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#pair-up).

## Blelloch's scan

Let $M$ be a monoid. For a natural number $k$ and a sequence
$x = (x_0, x_1, \dots)$ in $M$, the scan $B_k(x)$ is the sequence in $M$ defined by recursion
on $k$: $B_0(x)$ is constantly $1$, and $B_{k+1}(x)$ is obtained from the scan $y = B_k(p)$ of
the pair products $p_i = x_{2i} x_{2i+1}$ by setting $B_{k+1}(x)_{2i} = y_i$ and
$B_{k+1}(x)_{2i+1} = y_i x_{2i}$ for every $i$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blelloch`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch).

## Blelloch's scan computes the exclusive prefix products

Let $M$ be a monoid, $k$ a
natural number and $x = (x_0, x_1, \dots)$ a sequence in $M$. For every $j < 2^k$, the value at
position $j$ of Blelloch's scan of $x$ on $2^k$ positions is the exclusive prefix product
$x_0 x_1 \cdots x_{j-1}$ (equal to $1$ when $j = 0$).

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blelloch_eq_seg`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-eq-seg).

## Work of Blelloch's scan

The number $W(k)$ of monoid multiplications Blelloch's scan
performs on $2^k$ positions is defined by $W(0) = 0$ and $W(k+1) = 2^k + W(k) + 2^k$: on
$2^{k+1}$ positions, $2^k$ pair products, the recursive scan on the $2^k$ pair products, and
$2^k$ products for the odd positions.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blellochWork`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-work).

## Parallel steps of Blelloch's scan

The span $S(k)$ of Blelloch's scan on $2^k$
positions is defined by $S(0) = 0$ and $S(k+1) = S(k) + 2$: one parallel step for the pair
products, the recursive scan, and one parallel step for the odd positions.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blellochSpan`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-span).

## Blelloch's scan is work-efficient

For every natural number $k$, the number $W(k)$ of
monoid multiplications Blelloch's scan performs on $n = 2^k$ positions satisfies
$W(k) + 2 = 2^{k+1}$, so $W(k) = 2^{k+1} - 2 < 2n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blellochWork_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-work-eq).

## Blelloch's scan has logarithmic span

For every natural number $k$, the span of
Blelloch's scan on $n = 2^k$ positions is $2k = 2 \log_2 n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blellochSpan_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-span-eq).

## Adjacent pair products of a list

For a list $[a_0, a_1, \ldots, a_{n-1}]$ of
elements of a monoid $M$, the list of adjacent pair products is $[a_0 a_1, a_2 a_3, \ldots]$:
it has length $\lfloor n/2 \rfloor$, its $i$-th entry is $a_{2i} a_{2i+1}$, and when $n$ is odd
the last element $a_{n-1}$ is dropped.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.pairList`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#pair-list).

## Interleaving step of Blelloch's list scan

Let $M$ be a monoid. For lists
$z = (z_0, z_1, \dots)$ and $x = (x_0, x_1, \dots)$ in $M$, the expansion of $z$ along $x$ is
the list $(z_0, z_0 x_0, z_1, z_1 x_2, z_2, z_2 x_4, \dots)$: each $z_i$ is followed by
$z_i x_{2i}$, and the list stops at the first $i$ for which $z_i$ or $x_{2i+1}$ does not
exist.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.expand`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#expand).

## Blelloch's scan on lists

Let $M$ be a monoid. For a natural number $k$ and a list
$xs = (x_0, x_1, \dots)$ in $M$, the list scan $L_k(xs)$ is defined by recursion on $k$:
$L_0(xs)$ is the one-element list $(1)$, and $L_{k+1}(xs)$ is obtained from the list scan
$z = L_k(p)$ of the pair products $p = (x_0 x_1, x_2 x_3, \dots)$ of $xs$ (a trailing unpaired
entry is dropped) by interleaving: $L_{k+1}(xs) = (z_0, z_0 x_0, z_1, z_1 x_2, \dots)$, where
each $z_i$ is followed by $z_i x_{2i}$ and the list stops at the first $i$ for which $z_i$ or
$x_{2i+1}$ does not exist.

On a list of length $2^k$ this takes $O(2^k)$ time.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.blellochList`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#blelloch-list).

## The list implementation computes Blelloch's scan

Let $M$ be a monoid, $k$ a natural
number and $xs = (x_0, \dots, x_{2^k - 1})$ a list in $M$ of length $2^k$. For every $j < 2^k$,
the entry at position $j$ of Blelloch's list scan of $xs$ in $k$ rounds equals the value at
position $j$ of Blelloch's scan on $2^k$ positions of the sequence
$x_0, \dots, x_{2^k - 1}, 1, 1, \dots$ obtained by extending $xs$ by $1$.

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.getD_blellochList`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#get-d-blelloch-list).

## The list implementation computes the exclusive prefix products

Let $M$ be a monoid,
$k$ a natural number and $xs = (x_0, \dots, x_{2^k - 1})$ a list in $M$ of length $2^k$. For
every $j < 2^k$, the entry at position $j$ of Blelloch's list scan of $xs$ in $k$ rounds is
the exclusive prefix product $x_0 x_1 \cdots x_{j-1}$ (equal to $1$ when $j = 0$).

Formalized by `Cslib.Algorithms.Lean.Parallel.PrefixSum.getD_blellochList_eq_seg`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Parallel/Blelloch.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html#get-d-blelloch-list-eq-seg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parallel prefix sums](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/parallel-algorithms/parallel-prefix-sums)
