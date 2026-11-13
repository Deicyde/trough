---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.HasPattern, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat321, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat231, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat4123, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat3412, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat3124, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_4123, MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_3412
statement: formalized
---

# Permutations counted by odd-indexed Fibonacci numbers

12 results, 6 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html).

## Classical pattern containment in a permutation

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n-1\}$ and let $\pi$ be a map from $\{0, 1, \dots, k-1\}$ to itself. Then
$\sigma$ contains the pattern $\pi$ if there are positions $e_0 < e_1 < \dots < e_{k-1}$ in
$\{0, 1, \dots, n-1\}$ such that for all $i, j < k$, $\sigma(e_i) < \sigma(e_j)$ holds exactly
when $\pi(i) < \pi(j)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.HasPattern`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#has-pattern).

## The pattern $321$

The pattern $321$ written with values $0, 1, 2$: the map from
$\{0, 1, 2\}$ to itself sending $0 \mapsto 2$, $1 \mapsto 1$ and $2 \mapsto 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat321`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#pat321).

## The pattern $231$

The pattern $231$ written with values $0, 1, 2$: the map from
$\{0, 1, 2\}$ to itself sending $0 \mapsto 1$, $1 \mapsto 2$ and $2 \mapsto 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat231`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#pat231).

## The permutation pattern $4123$

The pattern $4123$ with its values shifted down by
one: the map $\{0, 1, 2, 3\} \to \{0, 1, 2, 3\}$ sending $0, 1, 2, 3$ to $3, 0, 1, 2$
respectively.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat4123`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#pat4123).

## The permutation pattern $3412$

The pattern $3412$ with its values shifted down by
one: the map $\{0, 1, 2, 3\} \to \{0, 1, 2, 3\}$ sending $0, 1, 2, 3$ to $2, 3, 0, 1$
respectively.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat3412`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#pat3412).

## The pattern $3124$

The pattern $3124$ written with values $0, 1, 2, 3$: the map from
$\{0, 1, 2, 3\}$ to itself sending $0 \mapsto 2$, $1 \mapsto 0$, $2 \mapsto 1$ and $3 \mapsto 3$.

Formalized by `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.pat3124`, a definition declared in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#pat3124).

## $(321, 4123)$-avoiding permutations are counted by odd-indexed Fibonacci numbers

For
every $n \ge 1$, the number of permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$321$ and $4123$, that is, contain neither of them, is the Fibonacci number $F_{2n-1}$, where
$F_0 = 0$ and $F_1 = 1$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_4123` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-321-4123).

## $(321, 3412)$-avoiding permutations are counted by odd-indexed Fibonacci numbers

For
every $n \ge 1$, the number of permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$321$ and $3412$, that is, contain neither of them, is the Fibonacci number $F_{2n-1}$, where
$F_0 = 0$ and $F_1 = 1$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_3412` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-321-3412).

## $(231, 3124)$-avoiding permutations are counted by odd-indexed Fibonacci numbers

For
every $n \ge 1$, the number of permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$231$ and $3124$, that is, contain neither of them, is the Fibonacci number $F_{2n-1}$, where
$F_0 = 0$ and $F_1 = 1$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_231_3124` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-231-3124).

## Position of the smallest entry in $(321, 4123)$-avoiding permutations

For a natural
number $m$, write $S_m(321, 4123)$ for the set of permutations of $\{0, 1, \dots, m-1\}$ that
avoid both patterns $321$ and $4123$, that is, contain neither of them. Let $n \ge 1$ and let
$j$ be a position with $j + 1 < n$. Then the number of permutations $\sigma \in S_n(321, 4123)$
with $\sigma(j) = 0$ equals $(j + 1) \cdot |S_{n-j-1}(321, 4123)|$.

In the source, positions and values start at $1$: with $k = j + 1$, the number of such
permutations with $\sigma(k) = 1$ is $k \cdot |S_{n-k}(321, 4123)|$ for $1 \le k < n$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_4123_pos_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-321-4123-pos-zero).

## Position of the smallest entry in $(231, 3124)$-avoiding permutations

For a natural
number $m$, write $S_m(231, 3124)$ for the set of permutations of $\{0, 1, \dots, m-1\}$ that
avoid both patterns $231$ and $3124$, that is, contain neither of them. Let $n \ge 1$ and let
$j$ be a position with $j + 1 < n$. Then the number of permutations $\sigma \in S_n(231, 3124)$
with $\sigma(j) = 0$ equals $(j + 1) \cdot |S_{n-j-1}(231, 3124)|$.

In the source, positions and values start at $1$: with $k = j + 1$, the number of such
permutations with $\sigma(k) = 1$ is $k \cdot |S_{n-k}(231, 3124)|$ for $1 \le k < n$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_231_3124_pos_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-231-3124-pos-zero).

## Smallest entry in the first two positions of $(321, 3412)$-avoiding permutations

Let
$n \ge 2$. Among the permutations $\sigma$ of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$321$ and $3412$, that is, contain neither of them, the number with $\sigma(0) = 0$ and the
number with $\sigma(1) = 0$ are both equal to the Fibonacci number $F_{2n-3}$, where $F_0 = 0$
and $F_1 = 1$.

In the source's indexing from $1$, these are the permutations with $\sigma(1) = 1$ and with
$\sigma(2) = 1$.

## Sources

- Juan B. Gil, Felix H. Xu, and William Y. Zhu, "Odd-Indexed Fibonacci Numbers via Pattern-Avoiding Permutations", Proposition 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.OddFibonacciWanted.card_avoid_321_3412_pos_zero_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/OddFibonacciWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html#card-avoid-321-3412-pos-zero-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutations counted by odd-indexed Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/permutations-counted-by-odd-indexed-fibonacci-nu)
