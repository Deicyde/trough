---
declaration: section
origin: cited
lean: MetaMathlibExt.cyclicLabel, MetaMathlibExt.LadderAdj, MetaMathlibExt.IsConsecutiveCyclicPrimeLabeling, MetaMathlibExt.cyclicLabel_pos, MetaMathlibExt.cyclicLabel_le_size, MetaMathlibExt.cyclicLabel_mem_range, MetaMathlibExt.cyclicLabel_zero_offset_zero
statement: formalized
proof: formalized
---

# Prime labelings of ladder graphs

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html).

## Cyclic labeling of the ladder perimeter

Let $n$ and $s$ be natural numbers. Number the
vertices of the ladder $P_n \times P_2$ along its perimeter by $0, 1, \dots, 2n - 1$, with $v_k$ at
position $k - 1$ and $u_k$ at position $2n - k$ for $1 \le k \le n$. The cyclic label with offset
$s$ of the position $i \in \{0, \dots, 2n - 1\}$ is $((i + s) \bmod 2n) + 1$.

Following Mbirika et al., JIS Vol. 19, the ladder has horizontal adjacency within each row and
vertical adjacency between $v_k$ and $u_k$.

Formalized by `MetaMathlibExt.cyclicLabel`, a definition declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#cyclic-label).

## Adjacency in the ladder graph

Number the vertices of the ladder $P_n \times P_2$ along
its perimeter by $0, 1, \dots, 2n-1$, with $v_k$ at position $k - 1$ and $u_k$ at position
$2n - k$ for $1 \le k \le n$. Two positions $i, j \in \{0, \dots, 2n-1\}$ are adjacent when
$j \equiv i + 1 \pmod{2n}$ or $i \equiv j + 1 \pmod{2n}$ (neighbours along the perimeter
cycle), or when $i + j = 2n - 1$ (the rung joining $v_k$ and $u_k$).

The two end rungs $v_1 u_1$ and $v_n u_n$ are also perimeter edges.

Formalized by `MetaMathlibExt.LadderAdj`, a definition declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#ladder-adj).

## Consecutive cyclic prime labeling of the ladder

Let $n$ and $s$ be natural numbers.
Number the vertices of the ladder $P_n \times P_2$ along its perimeter by $0, 1, \dots, 2n - 1$,
with $v_k$ at position $k - 1$ and $u_k$ at position $2n - k$ for $1 \le k \le n$. The offset $s$
gives a consecutive cyclic prime labeling of the ladder when $n > 0$ and, for all positions
$i, j \in \{0, \dots, 2n - 1\}$ that are adjacent in the ladder graph, the cyclic labels of $i$
and $j$ with offset $s$ are relatively prime.

The cyclic labels place $1, \dots, 2n$ consecutively along the perimeter order: if $1$ is on $v_k$
the order runs $v_k, \dots, v_n, u_n, \dots, u_1, v_1, \dots, v_{k - 1}$ (and analogously from
$u_k$).

Formalized by `MetaMathlibExt.IsConsecutiveCyclicPrimeLabeling`, a definition declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#is-consecutive-cyclic-prime-labeling).

## Cyclic labels are positive

For all natural numbers $n$ and $s$ and every position
$i \in \{0, \dots, 2n-1\}$, the cyclic label of $i$ with offset $s$ is at least $1$.

Formalized by `MetaMathlibExt.cyclicLabel_pos`, a theorem declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#cyclic-label-pos).

## Cyclic labels do not exceed the number of vertices

For all natural numbers $n > 0$ and
$s$ and every position $i \in \{0, \dots, 2n-1\}$, the cyclic label of $i$ with offset $s$ is at
most $2n$.

Formalized by `MetaMathlibExt.cyclicLabel_le_size`, a theorem declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#cyclic-label-le-size).

## Range of the cyclic labels

For all natural numbers $n > 0$ and $s$ and every position
$i \in \{0, \dots, 2n-1\}$, the cyclic label $c$ of $i$ with offset $s$ satisfies
$1 \le c \le 2n$.

Formalized by `MetaMathlibExt.cyclicLabel_mem_range`, a theorem declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#cyclic-label-mem-range).

## The cyclic label of the first position with offset zero

Let $n > 0$ be a natural number
and number the vertices of the ladder $P_n \times P_2$ along its perimeter by $0, 1, \dots, 2n - 1$,
with $v_k$ at position $k - 1$ and $u_k$ at position $2n - k$ for $1 \le k \le n$. Then the cyclic
label with offset $0$ of the position $0$ (the vertex $v_1$) is $1$.

Formalized by `MetaMathlibExt.cyclicLabel_zero_offset_zero`, a theorem declared in [MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ConsecutiveCyclicPrimeLabeling.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html#cyclic-label-zero-offset-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime labelings of ladder graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/prime-labelings-of-ladder-graphs)
