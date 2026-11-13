---
declaration: section
origin: cited
lean: MetaMathlibExt.excedanceCount, MetaMathlibExt.IsRMinusAssociatedCyclePerm, MetaMathlibExt.IsRAssociatedCyclePerm, MetaMathlibExt.rMinusAssociatedStirlingEulerian, MetaMathlibExt.rAssociatedStirlingEulerian, MetaMathlibExt.circularEulerian, MetaMathlibExt.circularEulerian_small, MetaMathlibExt.sameCycle_all_iff_isCycle_support_eq_univ
statement: formalized
---

# Associated Stirling–Eulerian numbers

79 results, 19 proved and 60 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html).

## Number of excedances

For a permutation $\sigma$ of $\{0, 1, \dots, n-1\}$, an excedance
of $\sigma$ is a point $i$ with $\sigma(i) > i$, and the excedance count $e(\sigma)$ is the number
of excedances of $\sigma$.

## Sources

- JIS VOL28/Rakotoson/rakoto12.tex Lines 130-132; URL https://cs.uwaterloo.ca/journals/JIS/VOL28/Rakotoson/rakoto12.tex.

Formalized by `MetaMathlibExt.excedanceCount`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#excedance-count).

## Permutations with all cycles of length at most $r$

A permutation $\sigma$ of
$\{0, 1, \dots, n-1\}$ is an $r$-minus-associated cycle permutation when every cycle of $\sigma$,
fixed points counted as cycles of length one, has length at most $r$: every fixed point of
$\sigma$ forces $1 \le r$, and every cycle of $\sigma$ of length at least $2$ has length at most
$r$. For $n = 0$ the empty permutation qualifies for every $r$.

## Sources

- source JIS VOL28/Rakotoson/rakoto12.tex Lines 106-108 and Lines 257-259; URL https://cs.uwaterloo.ca/journals/JIS/VOL28/Rakotoson/rakoto12.tex.

Formalized by `MetaMathlibExt.IsRMinusAssociatedCyclePerm`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#is-rminus-associated-cycle-perm).

## Permutations with all cycles longer than $r$

A permutation $\sigma$ of
$\{0, 1, \dots, n-1\}$ is an $r$-associated cycle permutation when every cycle of $\sigma$, fixed
points counted as cycles of length one, has length greater than $r$: every fixed point of $\sigma$
forces $r < 1$, and every cycle of $\sigma$ of length at least $2$ has length greater than $r$.
For $n = 0$ the empty permutation qualifies for every $r$.

## Sources

- source JIS VOL28/Rakotoson/rakoto12.tex Lines 106-108 and Lines 653-657; URL https://cs.uwaterloo.ca/journals/JIS/VOL28/Rakotoson/rakoto12.tex.

Formalized by `MetaMathlibExt.IsRAssociatedCyclePerm`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#is-rassociated-cycle-perm).

## $r$-minus-associated Stirling Eulerian numbers

For natural numbers $r$, $n$ and
$m$, the $r$-minus-associated Stirling Eulerian number is the number of permutations $\sigma$ of
$\{0, \dots, n-1\}$ all of whose cycles, fixed points counted as cycles of length $1$, have
length at most $r$, and that have exactly $m$ excedances, that is, exactly $m$ indices $i$ with
$\sigma(i) > i$.

## Sources

- JIS VOL28/Rakotoson/rakoto12.tex Lines 257-259; URL https://cs.uwaterloo.ca/journals/JIS/VOL28/Rakotoson/rakoto12.tex.

Formalized by `MetaMathlibExt.rMinusAssociatedStirlingEulerian`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-stirling-eulerian).

## $r$-associated Stirling Eulerian numbers

For natural numbers $r$, $n$ and $m$, the
$r$-associated Stirling Eulerian number $A^{r}_{n,m}$ is the number of permutations $\sigma$ of
$\{0, \dots, n-1\}$ all of whose cycles, fixed points counted as cycles of length $1$, have
length greater than $r$, and that have exactly $m$ excedances, that is, exactly $m$ indices $i$
with $\sigma(i) > i$.

## Sources

- Source JIS VOL28/Rakotoson/rakoto12.tex Lines 653-657; URL https://cs.uwaterloo.ca/journals/JIS/VOL28/Rakotoson/rakoto12.tex.

Formalized by `MetaMathlibExt.rAssociatedStirlingEulerian`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-stirling-eulerian).

## Circular Eulerian numbers

For natural numbers $n$ and $m$, the circular Eulerian number
$C_{n,m}$ is the number of permutations $\sigma$ of $\{0, 1, \dots, n-1\}$ such that $n \ge 1$,
all points lie in a single cycle of $\sigma$ (for any two points $i$ and $j$ there is an integer
$k$ with $\sigma^k(i) = j$), and $\sigma$ has exactly $m$ excedances, that is, exactly $m$ points
$i$ with $\sigma(i) > i$. In particular $C_{0,m} = 0$ for every $m$, and the identity permutation
of a single point counts as circular.

For $n \ge 2$ the permutations with a single cycle through all points are exactly the $n$-cycles.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorems 5 and 6 (excedance distribution `C_n(x)` over circular permutations, `C_{1,0} = 1`).

Formalized by `MetaMathlibExt.circularEulerian`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#circular-eulerian).

## Small circular Eulerian numbers

Writing $C_{n,m}$ for the circular Eulerian number, we have
$C_{0,0} = 0$, $C_{1,0} = 1$, $C_{3,1} = 1$ and $C_{3,2} = 1$.

Of the two cyclic permutations of $\{1, 2, 3\}$, $1 \mapsto 3 \mapsto 2 \mapsto 1$ has one
excedance and $1 \mapsto 2 \mapsto 3 \mapsto 1$ has two.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 5.

Formalized by `MetaMathlibExt.circularEulerian_small`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#circular-eulerian-small).

## Circular permutations are the full cycles

Let $n \ge 2$ and let $\sigma$ be a
permutation of $\{0, \dots, n-1\}$. Any two points $i$ and $j$ lie in the same cycle of
$\sigma$ (that is, $j = \sigma^k(i)$ for some integer $k$) if and only if $\sigma$ is a cycle,
meaning that it moves some point and any two points it moves lie in the same cycle, and
$\sigma$ moves every point.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorems 5 and 6 (circular permutations).

Formalized by `MetaMathlibExt.sameCycle_all_iff_isCycle_support_eq_univ`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#same-cycle-all-iff-is-cycle-support-eq-u).

## Permutations with all cycles of length $r$

A permutation $\sigma$ of
$\{0, 1, \dots, n-1\}$ is an $r$-cycle permutation when every cycle of $\sigma$, fixed points
counted as cycles of length one, has exactly $r$ elements: for every point $i$, exactly $r$
points $j$ satisfy $\sigma^k(i) = j$ for some integer $k$. For $n = 0$ the condition holds for
every $r$.

These are the paper's $(r)$-cycle permutations, the set $S_n^r$ of Corollary 25.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorems 20-23 and Corollaries 24-26.

Formalized by `MetaMathlibExt.IsRCyclePerm`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#is-rcycle-perm).

## Cycle-type characterization of $r$-cycle permutations

A permutation $\sigma$ of
$\{0, 1, \dots, n-1\}$ has all its cycles, fixed points counted as cycles of length one, of length
exactly $r$ if and only if every fixed point of $\sigma$ forces $r = 1$ and every cycle of $\sigma$
of length at least $2$ has length exactly $r$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorems 20-23 (cycle lengths of `(r)`-cycle permutations).

Formalized by `MetaMathlibExt.isRCyclePerm_iff`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#is-rcycle-perm-iff).

## $r$-cycle Stirling Eulerian numbers

For natural numbers $r$, $n$ and $m$, the number
$A^{(r)}_{n,m}$ is the number of permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose
cycles, fixed points counted as cycles of length $1$, have length exactly $r$, and that have
exactly $m$ excedances, that is, exactly $m$ indices $i$ with $\sigma(i) > i$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorems 20 and 21.

Formalized by `MetaMathlibExt.rCycleStirlingEulerian`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-stirling-eulerian).

## Small $r$-cycle Stirling Eulerian numbers

Write $A^{(r)}_{n,m}$ for the number of
permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points counted as
cycles of length $1$, have length exactly $r$, and that have exactly $m$ excedances (indices $i$
with $\sigma(i) > i$). Then $A^{(2)}_{0,0} = 1$ (the empty permutation), $A^{(2)}_{2,1} = 1$
(the transposition), $A^{(2)}_{3,1} = 0$, and $A^{(3)}_{3,1} = A^{(3)}_{3,2} = 1$ (the two
$3$-cycles).

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 20 and Corollary 25.

Formalized by `MetaMathlibExt.rCycleStirlingEulerian_small`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-stirling-eulerian-small).

## Excedance and cycle generating function of a permutation family

Let $R$ be a
commutative $\mathbb{Q}$-algebra, let $x, q \in R$, and for each $n$ let $P_n$ be a set of
permutations of $\{0, 1, \dots, n-1\}$. The excedance and cycle exponential generating function
of the family $(P_n)$ is the formal power series in $u$ over $R$

$$\sum_{n \ge 0} \frac{1}{n!} \Big(\sum_{\sigma \in P_n} x^{e(\sigma)} q^{c(\sigma)}\Big) u^n,$$

where $e(\sigma)$ is the number of excedances of $\sigma$ (points $i$ with $\sigma(i) > i$) and
$c(\sigma)$ its number of cycles, fixed points counted as cycles of length one.

With $q = 1$ this is the paper's $P(x, u)$, and for general $q$ its $q$-analogue $P(q, x, u)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 6 and Corollary 43 (the series `C(x,u)` and `A_k(x,u)`), Corollary 24 (the weight `x^{e(π)} q^{c(π)}`).

Formalized by `MetaMathlibExt.permExcedanceCycleEGF`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-excedance-cycle-egf).

## Coefficients of the excedance and cycle generating function

Let $R$ be a commutative
$\mathbb{Q}$-algebra, let $x, q \in R$, and for each $n$ let $P_n$ be a set of permutations of
$\{0, 1, \dots, n-1\}$. For every $n \ge 0$, the coefficient of $u^n$ in the excedance and cycle
exponential generating function of the family $(P_n)$ is
$\frac{1}{n!} \sum_{\sigma \in P_n} x^{e(\sigma)} q^{c(\sigma)}$, where $e(\sigma)$ is the number
of excedances of $\sigma$ and $c(\sigma)$ its number of cycles, fixed points counted as cycles of
length one.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 6.

Formalized by `MetaMathlibExt.coeff_permExcedanceCycleEGF`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#coeff-perm-excedance-cycle-egf).

## Constant coefficient of the generating function of all permutations

Let $R$ be a
commutative $\mathbb{Q}$-algebra and let $x, q \in R$. In the excedance and cycle exponential
generating function of the family of all permutations, the coefficient of $u^0$ is $1$.

The only permutation of the empty set has no excedance and no cycle.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 6.

Formalized by `MetaMathlibExt.coeff_zero_permExcedanceCycleEGF_true`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AssociatedStirlingEulerian.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#coeff-zero-perm-excedance-cycle-egf-true).

## Circular Eulerian numbers are shifted Eulerian numbers

An excedance of a permutation
$\sigma$ of $n$ objects $1, \dots, n$ is an index $i$ with $\sigma(i) > i$. Let $C_{n,m}$ be the
number of circular permutations of $n$ objects (permutations with a single cycle through all
$n \ge 1$ points) with exactly $m$ excedances, and let $A_{n,m}$ be the number of permutations of
$n$ objects with exactly $m$ excedances (the $0$-associated Stirling Eulerian number, which
counts the permutations all of whose cycle lengths exceed $0$, that is, all permutations). Then
$C_{1,0} = 1$; for all $n \ge 2$ and $1 \le m \le n$ we have $C_{n,m} = A_{n-1,m-1}$; and for
every $n \ge 2$ the polynomial identity $C_n(x) = x\,A_{n-1}(x)$ holds in $\mathbb{Z}[x]$, where
$C_n(x) = \sum_{m=0}^{n} C_{n,m} x^m$ and $A_{n-1}(x) = \sum_{m=0}^{n-1} A_{n-1,m} x^m$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 5 (`jis-2025-25.5.7-thm-5`).

Stated but not proved: `MetaMathlibExt.circularEulerian_eq_eulerian` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#circular-eulerian-eq-eulerian).

## Recurrence for permutations with cycle lengths at most r, by excedances

Let $r \ge 2$.
An excedance of a permutation $\sigma$ is an $i$ with $\sigma(i) > i$. Let $A^{r-}_{n,m}$ be the
number of permutations of $\{1, \dots, n\}$ all of whose cycles have length at most $r$ and which
have exactly $m$ excedances, and let $C_{\ell,i}$ be the number of circular permutations of
$\ell$ objects (permutations with a single cycle through all points) with exactly $i$
excedances. Then for all natural numbers $m \le n$,

$$A^{r-}_{n+1,m} = \sum_{j=1}^{r-1} \binom{n}{j} \sum_{i=0}^{m} C_{j+1,i}\, A^{r-}_{n-j,m-i} +
A^{r-}_{n,m}.$$

A term with $j > n$ vanishes because $\binom{n}{j} = 0$; there $n - j$ is read as $0$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 10 (`jis-2025-25.5.7-thm-10`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedStirlingEulerian_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-stirling-eulerian-suc).

## Recurrence for the $r$-associated Stirling Eulerian numbers

For natural numbers $r$, $n$,
$m$ let $A^r_{n,m}$ be the number of permutations $\sigma$ of $\{0, \dots, n-1\}$ with exactly
$m$ excedances (points $i$ with $\sigma(i) > i$) all of whose cycles (fixed points counted as
cycles of length one) have length greater than $r$, and for natural numbers $a$, $b$ let
$C_{a,b}$ be the circular Eulerian number, the number of permutations of $\{0, \dots, a-1\}$,
$a \ge 1$, that consist of a single cycle through all points and have exactly $b$ excedances
($C_{0,b} = 0$). If $m \le n$ and $n \ge r + 1$, then

$$A^r_{n,m} = m A^r_{n-1,m} + (n-m) A^r_{n-1,m-1} +
\binom{n-1}{r} \sum_{s=0}^{m} C_{r+1,s} A^r_{n-r-1,m-s},$$

where the term $(n-m) A^r_{n-1,m-1}$ is read as $0$ when $m = 0$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 30 (`jis-2025-25.5.7-thm-30`).

Stated but not proved: `MetaMathlibExt.rAssociatedStirlingEulerian_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-stirling-eulerian-recurrenc).

## Convolution recurrence for the $r$-associated Stirling Eulerian numbers

For natural
numbers $r$, $n$, $m$ let $A^r_{n,m}$ be the number of permutations $\sigma$ of
$\{0, \dots, n-1\}$ with exactly $m$ excedances (points $i$ with $\sigma(i) > i$) all of whose
cycles (fixed points counted as cycles of length one) have length greater than $r$, and for
natural numbers $a$, $b$ let $C_{a,b}$ be the circular Eulerian number, the number of
permutations of $\{0, \dots, a-1\}$, $a \ge 1$, that consist of a single cycle through all
points and have exactly $b$ excedances ($C_{0,b} = 0$). If $r \ge 1$, $m \le n$ and
$n \ge r + 1$, then

$$A^r_{n+1,m} = \sum_{j=r}^{n} \binom{n}{j} \sum_{i=1}^{m} C_{j+1,i} A^r_{n-j,m-i}.$$

The hypothesis $r \ge 1$ is needed: for $r = 0$, $n = 1$, $m = 0$ the left side is
$A^0_{2,0} = 1$ (the identity) while the right side is $0$, every inner sum over $1 \le i \le 0$
being empty.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 31 (`jis-2025-25.5.7-thm-31`).

Stated but not proved: `MetaMathlibExt.rAssociatedStirlingEulerian_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-stirling-eulerian-succ).

## Derangements weighted by excedances and cycle weight $-2$

Let $n \ge 1$. For a
permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices $i$ with
$\sigma(i) > i$) and $c(\sigma)$ its number of cycles. Summing over the derangements $\sigma$ of
$n$ objects (permutations without fixed points), the polynomial
$(x - 1)^2 \sum_{\sigma} x^{e(\sigma)} (-2)^{c(\sigma)}$ equals
$-2x\,\big(-2^{n-1} x - 2^{n-1} x^{n-1} + (x+1)^n\big)$ in $\mathbb{Z}[x]$; that is,
$\sum_{\sigma} x^{e(\sigma)} (-2)^{c(\sigma)} = -2x(-2^{n-1}x - 2^{n-1}x^{n-1} + (x+1)^n)/(x-1)^2$
with the denominator cleared.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 55 (`jis-2025-25.5.7-cor-55`).

Stated but not proved: `MetaMathlibExt.derangement_excedance_cycle_sum_neg_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#derangement-excedance-cycle-sum-neg-two).

## Logarithm of the Eulerian generating function

Let $R$ be a commutative $\mathbb{Q}$-algebra
and $x \in R$, and work with formal power series in $u$ over $R$. For a permutation $\sigma$ write
$e(\sigma)$ for its number of excedances (points $i$ with $\sigma(i) > i$), and let $S_n$ be the
set of permutations of $\{0, \dots, n-1\}$. Let
$A(x,u) = \sum_{n \ge 0} \sum_{\sigma \in S_n} x^{e(\sigma)} u^n/n!$ be the exponential generating
function of excedances over all permutations, and let $C(x,u)$ be the same sum restricted to
circular permutations, that is, to the permutations of $n \ge 1$ points that consist of a single
cycle. Then $\exp C(x,u) = A(x,u)$, that is, $C(x,u) = \ln A(x,u)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 6 (`jis-2025-25.5.7-thm-6`).

Stated but not proved: `MetaMathlibExt.exp_circularPermEGF_eq_permEGF` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#exp-circular-perm-egf-eq-perm-egf).

## Excedance generating function of circular permutations of at most $r$ objects

Let
$R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 1$. For a permutation $\sigma$
let $e(\sigma)$ be its number of excedances (indices $i$ with $\sigma(i) > i$), and for
$j \ge 0$ let $A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over all permutations $\sigma$ of
$j$ objects. Then in $R[[u]]$
$\sum_{n=1}^{r} \sum_{\sigma} x^{e(\sigma)} u^n/n! =
u + x \sum_{j=1}^{r-1} A_j(x)\,u^{j+1}/(j+1)!$, where the inner sum on the left runs over the
circular permutations $\sigma$ of $n$ objects (those with a single cycle through all $n$
points).

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 7 (`jis-2025-25.5.7-thm-7`).

Stated but not proved: `MetaMathlibExt.circularRMinusPermEGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#circular-rminus-perm-egf-eq).

## Excedance generating function of circular permutations of $r$ objects

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 2$. For a permutation $\sigma$ let
$e(\sigma)$ be its number of excedances (indices $i$ with $\sigma(i) > i$), and for $j \ge 0$ let
$A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over all permutations $\sigma$ of $j$ objects. Then
the power series $\sum_{\sigma} x^{e(\sigma)} u^r/r!$ in $R[[u]]$, summed over the circular
permutations $\sigma$ of $r$ objects (those with a single cycle through all $r$ points), equals
$x\,A_{r-1}(x)\,u^r/r!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 8 (`jis-2025-25.5.7-thm-8`).

Stated but not proved: `MetaMathlibExt.circularRCyclePermEGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#circular-rcycle-perm-egf-eq).

## Excedance generating function of circular permutations of more than $r$ objects

Let $R$
be a commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 2$, and work with formal power series
in $u$ over $R$. For a permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices
$i$ with $\sigma(i) > i$). For $j \ge 0$ let $A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over
all permutations $\sigma$ of $j$ objects, and let $A(x,u) = \sum_{n \ge 0} A_n(x)\, u^n/n!$. Let
$C^{r+}(x,u) = \sum_{n \ge r+1} \sum_{\sigma} x^{e(\sigma)} u^n/n!$, where the inner sum runs over
the circular permutations $\sigma$ of $n$ objects (those with a single cycle through all $n$
points). Then

$$\exp C^{r+}(x,u) =
A(x,u) \exp\Bigl(-u - x \sum_{i=1}^{r-1} A_i(x)\, \frac{u^{i+1}}{(i+1)!}\Bigr).$$

This is the identity
$C^{r+}(x,u) = \ln\bigl(A(x,u) \exp(-u - x \sum_{i=1}^{r-1} A_i(x)\, u^{i+1}/(i+1)!)\bigr)$
written in exponential form.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 9 (`jis-2025-25.5.7-thm-9`).

Stated but not proved: `MetaMathlibExt.exp_circularRPlusPermEGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#exp-circular-rplus-perm-egf-eq).

## Exponential generating function of permutations with cycle lengths at most $r$

Let $R$
be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r \ge 2$ be a natural number. For a
permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for its number of excedances
(indices $i$ with $\sigma(i) > i$), and let $A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points included, have
at most $r$ elements. Then

$$A^{r-}(x,u) = \exp\left(u + x \sum_{j=1}^{r-1} \frac{A_j(x)\, u^{j+1}}{(j+1)!}\right),$$

where $\exp$ of a series with zero constant term is its substitution into the exponential series.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 11 (`jis-2025-25.5.7-thm-11`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-eq-exp).

## Logarithm of the generating function of permutations with short cycles

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 2$ an integer, and work with formal power
series in $u$ over $R$. For a permutation $\sigma$ write $e(\sigma)$ for its number of excedances
(points $i$ with $\sigma(i) > i$). Let
$C^{r-}(x,u) = \sum_{n=1}^{r} \sum_{\sigma} x^{e(\sigma)} u^n/n!$, the inner sum over the
permutations of $n$ points that consist of a single cycle, and let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n!$, the inner sum over the
permutations of $n$ points all of whose cycles, fixed points included, have length at most $r$.
Then $\exp C^{r-}(x,u) = A^{r-}(x,u)$, that is, $C^{r-}(x,u) = \ln A^{r-}(x,u)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 12 (`jis-2025-25.5.7-cor-12`).

Stated but not proved: `MetaMathlibExt.exp_circularRMinusPermEGF_eq_rMinusAssociatedPermEGF` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#exp-circular-rminus-perm-egf-eq-r-minus).

## Primitive of the Eulerian generating function

Let $R$ be a commutative
$\mathbb{Q}$-algebra and $x \in R$, and work with formal power series in $u$ over $R$. For a
permutation $\sigma$ write $e(\sigma)$ for its number of excedances (points $i$ with
$\sigma(i) > i$), let $S_n$ be the set of permutations of $\{0, \dots, n-1\}$, and let
$A(x,u) = \sum_{n \ge 0} \sum_{\sigma \in S_n} x^{e(\sigma)} u^n/n!$. If $P(u)$ is a formal power
series in $u$ over $R$ with zero constant term whose derivative is $A(x,u)$, then
$\exp\bigl(x P(u) - (x-1)u\bigr) = A(x,u)$.

This is the paper's $P(x,u) = (\ln A(x,u) + u(x-1))/x$ with the division by $x$ cleared and the
logarithm exponentiated.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 13 (`jis-2025-25.5.7-cor-13`).

Stated but not proved: `MetaMathlibExt.exp_eulerianEGF_primitive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#exp-eulerian-egf-primitive).

## Generating function of permutations with cycle lengths at most $r$ and $k$ cycles

Let
$R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r, k$ be natural numbers with
$r \ge 2$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for its number of
excedances (indices $i$ with $\sigma(i) > i$) and $c(\sigma)$ for its number of cycles, fixed
points included, and let $A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points included, have
at most $r$ elements, and let $A^{r-}_k(x,u)$ be the same series with the inner sum restricted to
those $\sigma$ with $c(\sigma) = k$. Then

$$A^{r-}_k(x,u) = \frac{1}{k!}\Big(u + x \sum_{j=1}^{r-1} \frac{A_j(x)\, u^{j+1}}{(j+1)!}\Big)^k,$$

and $A^{r-}_k(x,u) = L^k/k!$ for every $L \in R[[u]]$ with zero constant term and
$\exp(L) = A^{r-}(x,u)$, where $\exp$ of a series with zero constant term is its substitution
into the exponential series.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 14 (`jis-2025-25.5.7-thm-14`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_cycleCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-cycle-count).

## Cycle-counting generating function for cycle lengths at most r

Let $R$ be a commutative
$\mathbb{Q}$-algebra, let $x, q \in R$ and let $r \ge 2$. For a permutation $\sigma$ write
$e(\sigma)$ for its number of excedances (the $i$ with $\sigma(i) > i$) and $c(\sigma)$ for its
number of cycles, fixed points included, and for $j \ge 1$ let
$A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over the permutations $\sigma$ of
$\{1, \dots, j\}$. Then, as formal power series in $u$ over $R$,

$$\sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} =
\exp\Bigl(q\Bigl(u + x \sum_{j=1}^{r-1} A_j(x) \frac{u^{j+1}}{(j+1)!}\Bigr)\Bigr),$$

where the inner sum on the left runs over the permutations $\sigma$ of $\{1, \dots, n\}$ all of
whose cycles have length at most $r$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 15 (`jis-2025-25.5.7-thm-15`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_q_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-q-eq-exp).

## Cycle lengths at most r: the q-analogue is a q-th power

Let $R$ be a commutative
$\mathbb{Q}$-algebra, let $x, q \in R$ and let $r \ge 2$. For a permutation $\sigma$ write
$e(\sigma)$ for its number of excedances (the $i$ with $\sigma(i) > i$) and $c(\sigma)$ for its
number of cycles, fixed points included, and for $t \in R$ let

$$F_t(u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} t^{c(\sigma)},$$

where the inner sum runs over the permutations $\sigma$ of $\{1, \dots, n\}$ all of whose cycles
have length at most $r$. If $L$ is a formal power series in $u$ over $R$ with constant term $0$
and $\exp(L) = F_1(u)$, then $F_q(u) = \exp(qL)$. This is the identity $F_q = F_1^{\,q}$ with the
power read as $\exp(q \ln F_1)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 16 (`jis-2025-25.5.7-cor-16`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_q_eq_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-q-eq-pow).

## Recurrence for $r$-cycle Stirling Eulerian numbers

An excedance of a permutation
$\sigma$ of $\{0, \dots, N-1\}$ is an index $i$ with $\sigma(i) > i$. Let $A^{(r)}_{N,M}$ be the
number of permutations of $\{0, \dots, N-1\}$ with exactly $M$ excedances all of whose cycles,
fixed points included, have exactly $r$ elements, and let $C_{r,k}$ be the number of permutations
of $\{0, \dots, r-1\}$ with exactly $k$ excedances that consist of a single cycle through all $r$
points. Then for all natural numbers $r$, $n$, $m$ with $r \ge 2$ and $m \le n$,

$$A^{(r)}_{n+1,m} = \binom{n}{r-1} \sum_{k=1}^{m} C_{r,k}\, A^{(r)}_{n-(r-1),\,m-k},$$

where $n - (r-1)$ is truncated subtraction, equal to $0$ when $n < r - 1$ (harmless, since then
$\binom{n}{r-1} = 0$).

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 20 (`jis-2025-25.5.7-thm-20`).

Stated but not proved: `MetaMathlibExt.rCycleStirlingEulerian_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-stirling-eulerian-succ).

## Excedance generating function of permutations with all cycles of length $r$

Let $R$ be
a commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 2$. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ let $\operatorname{exc}(\sigma)$ be the number of points $i$ with
$\sigma(i) > i$, and let $A_{r-1}(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed
over all permutations of $\{0, \dots, r-2\}$. Let
$A^{(r)}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$, the inner
sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles (fixed points
counted as cycles of length one) have length exactly $r$. Then, as formal power series in $u$
over $R$,

$$A^{(r)}(x,u) = \exp\left(\frac{x A_{r-1}(x)\, u^r}{r!}\right).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 21 (`jis-2025-25.5.7-thm-21`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-eq-exp).

## Excedance generating function of permutations with $k$ cycles, all of length $r$

Let
$R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r$, $k$ be natural numbers with
$r \ge 2$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let $\operatorname{exc}(\sigma)$ be
the number of points $i$ with $\sigma(i) > i$, and let
$A_{r-1}(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed over all permutations of
$\{0, \dots, r-2\}$. Let
$A^{(r)}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$, the inner
sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles (fixed points
counted as cycles of length one) have length exactly $r$, and let $A^{(r)}_k(x,u)$ be the same
series with the inner sum restricted to the permutations with exactly $k$ cycles. Then

$$A^{(r)}_k(x,u) = \frac{1}{k!} \left(\frac{x A_{r-1}(x)\, u^r}{r!}\right)^k,$$

and for every formal power series $L$ in $u$ over $R$ with $L(0) = 0$ and
$\exp L = A^{(r)}(x,u)$ also $A^{(r)}_k(x,u) = L^k/k!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 22 (`jis-2025-25.5.7-thm-22`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_cycleCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-cycle-count-eq).

## Cycle-weighted exponential formula for $r$-cycle permutations

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$, and let $r \ge 2$ be a natural number. For a permutation
$\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for its number of excedances (indices $i$ with
$\sigma(i) > i$) and $c(\sigma)$ for its number of cycles, fixed points included, and let
$A_{r-1}(x) = \sum_{\sigma \in S_{r-1}} x^{e(\sigma)}$. Call $\sigma$ an $r$-cycle permutation
when every cycle of $\sigma$, fixed points included, has exactly $r$ elements, and let
$A^{(r)}(q,x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n! \in R[[u]]$,
the inner sum over the $r$-cycle permutations $\sigma$ of $\{0, \dots, n-1\}$. Then

$$A^{(r)}(q,x,u) = \exp\left(\frac{q\, x\, A_{r-1}(x)\, u^r}{r!}\right),$$

where $\exp$ of a series with zero constant term is its substitution into the exponential series.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 23 (`jis-2025-25.5.7-thm-23`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_q_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-q-eq-exp).

## Excedance and cycle polynomial of permutations with k cycles, all of length r

Let $R$ be
a commutative ring, let $x, q \in R$, let $r \ge 2$ and let $n, k \ge 0$. For a permutation
$\pi$ write $e(\pi)$ for its number of excedances (the $i$ with $\pi(i) > i$) and $c(\pi)$ for
its number of cycles, fixed points included, and let $A_{r-1}(x) = \sum_{\sigma} x^{e(\sigma)}$,
summed over the permutations $\sigma$ of $\{1, \dots, r - 1\}$. Summing over the permutations
$\pi$ of $\{1, \dots, n\}$ that have exactly $k$ cycles, all of length exactly $r$,

$$\sum_{\pi} x^{e(\pi)} q^{c(\pi)} = \frac{(rk)!}{(r!)^k\, k!}\, x^k q^k A_{r-1}(x)^k$$

if $n = kr$, and the sum is $0$ otherwise.

The quotient $(rk)!/((r!)^k k!)$ is an exact natural-number division.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 24 (`jis-2025-25.5.7-cor-24`).

Stated but not proved: `MetaMathlibExt.sum_rCyclePerm_cycleCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#sum-r-cycle-perm-cycle-count-eq).

## Number of permutations with all cycles of length $r$

Let $r \ge 2$ and $n \ge 0$. The
number of permutations of $n$ objects all of whose cycles, fixed points counted as cycles of
length one, have length exactly $r$ equals $n!/(r^{n/r}\,(n/r)!)$ if $r$ divides $n$, and $0$
otherwise.

When $r$ divides $n$ the quotient is an integer, so the natural-number division is exact.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 25 (`jis-2025-25.5.7-cor-25`).

Stated but not proved: `MetaMathlibExt.card_rCyclePerm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#card-r-cycle-perm).

## Exponential generating function for permutations with all cycles of length $r$

Let
$r \ge 2$ and, for each $n$, let $S_n^r$ be the set of permutations of $\{0, \dots, n-1\}$ all
of whose cycles (fixed points counted as cycles of length one) have length exactly $r$. Then, as
formal power series over $\mathbb{Q}$,

$$\sum_{n \ge 0} |S_n^r| \frac{u^n}{n!} = \exp\left(\frac{u^r}{r}\right).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 26 (`jis-2025-25.5.7-cor-26`).

Stated but not proved: `MetaMathlibExt.rCyclePermCountEGF_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-count-egf-eq-exp).

## Excedance generating function of permutations with all cycles longer than $r$

Let $R$
be a commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 1$. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ let $\operatorname{exc}(\sigma)$ be the number of points $i$ with
$\sigma(i) > i$, let $A_n(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed over all
permutations of $\{0, \dots, n-1\}$, and let $A(x,u) = \sum_{n \ge 0} A_n(x) u^n/n!$. Let
$A^r(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$, the inner sum
over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles (fixed points counted
as cycles of length one) have length greater than $r$. Then, as formal power series in $u$
over $R$,

$$A^r(x,u) = A(x,u) \exp\left(-u - x \sum_{j=1}^{r-1} \frac{A_j(x)\, u^{j+1}}{(j+1)!}\right).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 32 (`jis-2025-25.5.7-thm-32`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-eq).

## Logarithm of the generating function of permutations with long cycles

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x \in R$ and $r \ge 0$ an integer, and work with formal power
series in $u$ over $R$. For a permutation $\sigma$ write $e(\sigma)$ for its number of excedances
(points $i$ with $\sigma(i) > i$). Let
$C^{r+}(x,u) = \sum_{n \ge r+1} \sum_{\sigma} x^{e(\sigma)} u^n/n!$, the inner sum over the
permutations of $n$ points that consist of a single cycle, and let
$A^{r}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n!$, the inner sum over the
permutations of $n$ points all of whose cycles, fixed points included, have length greater than
$r$. Then $\exp C^{r+}(x,u) = A^{r}(x,u)$, that is, $C^{r+}(x,u) = \ln A^{r}(x,u)$.

At $r = 0$ every permutation has all cycle lengths greater than $0$, so $A^{0}(x,u)$ runs over
all permutations, $C^{0+}(x,u)$ over all circular permutations, and this is Theorem 6.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 33 (`jis-2025-25.5.7-cor-33`).

Stated but not proved: `MetaMathlibExt.exp_circularRPlusPermEGF_eq_rAssociatedPermEGF` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#exp-circular-rplus-perm-egf-eq-r-associa).

## Permutations with $k$ cycles, all of length greater than $r$, by excedances

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x \in R$ and $r, k \in \mathbb{N}$. For a permutation
$\sigma$ of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with $\sigma(i) > i$ and
$c(\sigma)$ the number of cycles of $\sigma$, fixed points included. Let
$A^r(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles (fixed points
included, as cycles of length $1$) have length greater than $r$, and let $A^r_k(x,u)$ be the same
series with the inner sum further restricted to the $\sigma$ with $c(\sigma) = k$. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A^r(x,u)$, where
$\exp(F) = \sum_{m \ge 0} F^m/m!$, then $A^r_k(x,u) = L^k/k!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 34 (`jis-2025-25.5.7-thm-34`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_cycleCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-cycle-count-eq).

## The $q$-analogue for cycles longer than $r$ is a $q$-th power

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$ and $r$ a natural number. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ let $\operatorname{exc}(\sigma)$ be the number of points $i$ with
$\sigma(i) > i$ and $\operatorname{cyc}(\sigma)$ its number of cycles (fixed points counted as
cycles of length one). Let

$$A^r(q,x,u) = \sum_{n \ge 0} \frac{u^n}{n!}
\sum_{\sigma} x^{\operatorname{exc}(\sigma)} q^{\operatorname{cyc}(\sigma)},$$

the inner sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles have
length greater than $r$, and let $A^r(x,u) = A^r(1,x,u)$. If $L$ is a formal power series in
$u$ over $R$ with $L(0) = 0$ and $\exp L = A^r(x,u)$, then $A^r(q,x,u) = \exp(qL)$.

This is the paper's $A^r(q,x,u) = (A^r(x,u))^q$, with the power read through the logarithm $L$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 35 (`jis-2025-25.5.7-thm-35`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_q_eq_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-q-eq-pow).

## Excedance generating function of involutions

Let $R$ be a commutative
$\mathbb{Q}$-algebra and $x, q \in R$. For a permutation $\sigma$ write $e(\sigma)$ for the number
of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for its number of cycles, fixed points included.
Summing over the involutions $\sigma$ of $\{0, \dots, n-1\}$ (permutations all of whose cycles
have length at most $2$), the following identity of formal power series in $u$ over $R$ holds:

$$\sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} \frac{u^n}{n!} = \exp(q(u + x u^2/2)).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 39 (`jis-2025-25.5.7-cor-39`).

Stated but not proved: `MetaMathlibExt.involutionEGF_q_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#involution-egf-q-eq-exp).

## Excedance generating function of fixed-point-free involutions

Let $R$ be a commutative
$\mathbb{Q}$-algebra and $x, q \in R$. For a permutation $\sigma$ write $e(\sigma)$ for the number
of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for its number of cycles, fixed points included.
Summing over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles have length
exactly $2$, the following identity of formal power series in $u$ over $R$ holds:

$$\sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} \frac{u^n}{n!} = \exp(q x u^2/2).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 41 (`jis-2025-25.5.7-cor-41`).

Stated but not proved: `MetaMathlibExt.fixedPointFreeInvolutionEGF_q_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-point-free-involution-egf-q-eq-exp).

## Excedance generating function of permutations with $k$ cycles

Let $R$ be a commutative
$\mathbb{Q}$-algebra and $x \in R$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let
$e(\sigma)$ be the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ the number of cycles of
$\sigma$, fixed points included. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and for $k \ge 0$ let $A_k(x,u)$ be the
same series with the inner sum restricted to the $\sigma$ with $c(\sigma) = k$. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A(x,u)$, where
$\exp(F) = \sum_{m \ge 0} F^m/m!$, then $A_k(x,u) = L^k/k!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 43 (`jis-2025-25.5.7-cor-43`).

Stated but not proved: `MetaMathlibExt.permEGF_cycleCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-egf-cycle-count-eq).

## Brenti's excedance and cycle generating function

Let $R$ be a commutative
$\mathbb{Q}$-algebra and $x, q \in R$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let
$e(\sigma)$ be the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ the number of cycles of
$\sigma$, fixed points included. Let
$A(q,x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} \in R[[u]]$,
the inner sum over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and $A(x,u) = A(1,x,u)$. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A(x,u)$, where
$\exp(F) = \sum_{m \ge 0} F^m/m!$, then $A(q,x,u) = \exp(qL)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 44 (`jis-2025-25.5.7-cor-44`).

Stated but not proved: `MetaMathlibExt.permEGF_q_eq_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-egf-q-eq-pow).

## First points in distinct cycles

For natural numbers $s$ and $n$, a permutation $\sigma$
of $\{0, 1, \dots, n-1\}$ has its first $s$ points in distinct cycles when any two points
$i, j < s$ that lie in the same cycle of $\sigma$ are equal. When $n < s$, only the points below
$n$ are constrained.

This is the side condition of the paper's $(r^-,k,s)$-, $(r^+,\star,s)$-, $((r),k,s)$-cycle and
$s$-fixed-points permutations.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Section 1 (definitions of `(r^-,k,s)`-cycle and `s`-fixed-points permutations).

Formalized by `MetaMathlibExt.FirstPointsInDistinctCycles`, a definition declared in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-in-distinct-cycles).

## The first-points condition for $s = 0$

For every $n \ge 0$ and every permutation
$\sigma$ of $\{0, \dots, n-1\}$, the first $0$ points of $\sigma$ lie in pairwise distinct
cycles: there are no such points, so the condition is vacuous.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Section 1.

Formalized by `MetaMathlibExt.firstPointsInDistinctCycles_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-in-distinct-cycles-zero).

## The identity permutation separates its first points

For all integers $s, n \ge 0$, the
first $s$ points of the identity permutation of $\{0, \dots, n-1\}$ lie in pairwise distinct
cycles: every point forms a cycle of its own.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Section 1.

Formalized by `MetaMathlibExt.firstPointsInDistinctCycles_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-in-distinct-cycles-one).

## First points of the transposition $(0\,1)$

Let $\tau = (0\,1)$ be the transposition of
$\{0, 1, 2\}$. The points $0, \dots, s-1$ lie in pairwise distinct cycles of $\tau$ for $s = 1$
(trivially, as there is only one such point) but not for $s = 2$, since $0$ and $1$ lie in the
same cycle of $\tau$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Section 1.

Formalized by `MetaMathlibExt.firstPointsInDistinctCycles_swap`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-in-distinct-cycles-swap).

## Derivative formula for permutations with cycle lengths at most $r$ and separated first points

**Derivative formula for permutations with cycle lengths at most $r$ and separated first
points.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r, s$ be natural
numbers with $r \ge 1$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for
its number of excedances (indices $i$ with $\sigma(i) > i$), and let
$A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Say that the first $s$ points of $\sigma$ are
separated when the points $i < \min(s, n)$ lie in pairwise distinct cycles. Let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points included, have
at most $r$ elements, and let $F(u)$ be the same series with the inner sum restricted to those
$\sigma$ whose first $s$ points are separated. Then the $s$-th derivative of $F$ with respect to
$u$ is

$$F^{(s)}(u) = \left(1 + x \sum_{i=1}^{r-1} \frac{A_i(x)\, u^i}{i!}\right)^s A^{r-}(x,u).$$

The paper states $r \ge 2$; the case $r = 1$ also holds (both sides are $\exp(u)$), while for
$r = 0$ and $s = 1$ the identity fails (the left side is $0$, the right side $1$).

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 17 (`jis-2025-25.5.7-thm-17`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_firstPoints_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-first-points).

## Derivative formula for permutations with cycle lengths at most $r$, $k$ cycles and separated first points

**Derivative formula for permutations with cycle lengths at most $r$, $k$ cycles and
separated first points.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let
$r, s, k$ be natural numbers with $r \ge 1$ and $s \le k$. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ write $e(\sigma)$ for its number of excedances (indices $i$ with
$\sigma(i) > i$) and $c(\sigma)$ for its number of cycles, fixed points included, and let
$A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Say that the first $s$ points of $\sigma$ are
separated when the points $i < \min(s, n)$ lie in pairwise distinct cycles. Let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points included, have
at most $r$ elements, and let $F(u)$ be the same series with the inner sum restricted to those
$\sigma$ with $c(\sigma) = k$ whose first $s$ points are separated. If $L \in R[[u]]$ has zero
constant term and $\exp(L) = A^{r-}(x,u)$, where $\exp$ of a series with zero constant term is
its substitution into the exponential series, then the $s$-th derivative of $F$ with respect to
$u$ is

$$F^{(s)}(u) = \Big(1 + x \sum_{i=1}^{r-1} \frac{A_i(x)\, u^i}{i!}\Big)^s \frac{L^{k-s}}{(k-s)!}.$$

The hypothesis $r \ge 1$ is needed: for $r = 0$ and $s = k = 1$ the left side is $0$ and the
right side is $1$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 18 (`jis-2025-25.5.7-thm-18`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_firstPoints_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-first-points-2).

## Cycle-weighted derivative formula for permutations with cycle lengths at most $r$ and separated first points

**Cycle-weighted derivative formula for permutations with cycle lengths at most $r$ and
separated first points.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x, q \in R$, and let
$r, s$ be natural numbers with $r \ge 1$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$
write $e(\sigma)$ for its number of excedances (indices $i$ with $\sigma(i) > i$) and $c(\sigma)$
for its number of cycles, fixed points included, and let
$A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Say that the first $s$ points of $\sigma$ are
separated when the points $i < \min(s, n)$ lie in pairwise distinct cycles. Let
$A^{r-}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles, fixed points included, have
at most $r$ elements, and let
$F(u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n!$, the inner sum over the
permutations $\sigma$ of $\{0, \dots, n-1\}$ with all cycles of at most $r$ elements whose first
$s$ points are separated. If $L \in R[[u]]$ has zero constant term and $\exp(L) = A^{r-}(x,u)$,
where $\exp$ of a series with zero constant term is its substitution into the exponential
series, then the $s$-th derivative of $F$ with respect to $u$ is

$$F^{(s)}(u) = q^s \left(1 + x \sum_{i=1}^{r-1} \frac{A_i(x)\, u^i}{i!}\right)^s \exp(qL).$$

The hypothesis $r \ge 1$ is needed: for $r = 0$ and $s = 1$ the left side is $0$ and the right
side is $q$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 19 (`jis-2025-25.5.7-thm-19`).

Stated but not proved: `MetaMathlibExt.rMinusAssociatedPermEGF_firstPoints_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-minus-associated-perm-egf-first-points-3).

## Derivative formula for $r$-cycle permutations with separated first points

Let $R$ be
a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r, s$ be natural numbers with $r \ge 2$.
For a permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for its number of excedances
(indices $i$ with $\sigma(i) > i$), and let $A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Call
$\sigma$ an $r$-cycle permutation when every cycle of $\sigma$, fixed points included, has exactly
$r$ elements, and say that its first $s$ points are separated when the points $i < \min(s, n)$
lie in pairwise distinct cycles. Let
$A^{(r)}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the $r$-cycle permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F(u)$ be the same series
with the inner sum restricted to those $\sigma$ whose first $s$ points are separated. Then the
$s$-th derivative of $F$ with respect to $u$ is

$$F^{(s)}(u) = x^s \left(\frac{A_{r-1}(x)\, u^{r-1}}{(r-1)!}\right)^s A^{(r)}(x,u).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 27 (`jis-2025-25.5.7-thm-27`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_firstPoints_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-first-points-iterate-de).

## Derivative formula for $r$-cycle permutations with $k$ cycles and separated first points

Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r, s, k$ be natural numbers
with $r \ge 2$ and $s \le k$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$
for its number of excedances (indices $i$ with $\sigma(i) > i$) and $c(\sigma)$ for its number of
cycles, fixed points included, and let $A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Call
$\sigma$ an $r$-cycle permutation when every cycle of $\sigma$, fixed points included, has exactly
$r$ elements, and say that its first $s$ points are separated when the points $i < \min(s, n)$
lie in pairwise distinct cycles. Let
$A^{(r)}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the $r$-cycle permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F(u)$ be the same series
with the inner sum restricted to those $\sigma$ with $c(\sigma) = k$ whose first $s$ points are
separated. If $L \in R[[u]]$ has zero constant term and $\exp(L) = A^{(r)}(x,u)$, where $\exp$ of
a series with zero constant term is its substitution into the exponential series, then the
$s$-th derivative of $F$ with respect to $u$ is

$$F^{(s)}(u) = x^s \left(\frac{A_{r-1}(x)\, u^{r-1}}{(r-1)!}\right)^s \frac{L^{k-s}}{(k-s)!}.$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 28 (`jis-2025-25.5.7-thm-28`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_firstPoints_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-first-points-cycle-coun).

## Cycle-weighted derivative formula for $r$-cycle permutations with separated first points

Let $R$ be a commutative $\mathbb{Q}$-algebra, $x, q \in R$, and let $r, s$ be natural numbers
with $r \ge 2$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ write $e(\sigma)$ for its
number of excedances (indices $i$ with $\sigma(i) > i$) and $c(\sigma)$ for its number of cycles,
fixed points included, and let $A_j(x) = \sum_{\sigma \in S_j} x^{e(\sigma)}$. Call $\sigma$ an
$r$-cycle permutation when every cycle of $\sigma$, fixed points included, has exactly $r$
elements, and say that its first $s$ points are separated when the points $i < \min(s, n)$ lie
in pairwise distinct cycles. Let
$A^{(r)}(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n! \in R[[u]]$, the inner sum over
the $r$-cycle permutations $\sigma$ of $\{0, \dots, n-1\}$, and let
$F(u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n!$, the inner sum over the
$r$-cycle permutations $\sigma$ of $\{0, \dots, n-1\}$ whose first $s$ points are separated. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A^{(r)}(x,u)$, where $\exp$ of a series
with zero constant term is its substitution into the exponential series, then the $s$-th
derivative of $F$ with respect to $u$ is

$$F^{(s)}(u) = q^s x^s \left(\frac{A_{r-1}(x)\, u^{r-1}}{(r-1)!}\right)^s \exp(qL).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 29 (`jis-2025-25.5.7-thm-29`).

Stated but not proved: `MetaMathlibExt.rCyclePermEGF_firstPoints_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-cycle-perm-egf-first-points-q-iterate).

## Iterated derivative for cycles longer than $r$ with $s$ points in distinct cycles

Let
$R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r$, $s$ be natural numbers with
$r \ge 1$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let $\operatorname{exc}(\sigma)$ be
the number of points $i$ with $\sigma(i) > i$, let
$A_n(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed over all permutations of
$\{0, \dots, n-1\}$, and let $A(x,u) = \sum_{n \ge 0} A_n(x) u^n/n!$. Let $A^r(x,u)$ be the
series $\sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$ with the inner sum
over the permutations of $\{0, \dots, n-1\}$ all of whose cycles (fixed points counted as
cycles of length one) have length greater than $r$, and let $[A^r(x,u)]_s$ be the same series
with the inner sum further restricted to the permutations whose points among
$0, \dots, s-1$ lie in pairwise distinct cycles. Then the $s$-th formal derivative in $u$
satisfies

$$\frac{\partial^s}{\partial u^s} [A^r(x,u)]_s =
x^s \left(A(x,u) - \sum_{n=0}^{r-1} \frac{A_n(x)\, u^n}{n!}\right)^s A^r(x,u).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 36 (`jis-2025-25.5.7-thm-36`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_firstPoints_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-first-points-itera).

## Iterated derivative for $k$ cycles longer than $r$ with $s$ points in distinct cycles

Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, and let $r$, $s$, $k$ be natural
numbers with $r \ge 1$ and $s \le k$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let
$\operatorname{exc}(\sigma)$ be the number of points $i$ with $\sigma(i) > i$, let
$A_n(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed over all permutations of
$\{0, \dots, n-1\}$, and let $A(x,u) = \sum_{n \ge 0} A_n(x) u^n/n!$. Let $A^r(x,u)$ be the
series $\sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$ with the inner sum
over the permutations of $\{0, \dots, n-1\}$ all of whose cycles (fixed points counted as
cycles of length one) have length greater than $r$, and let $[A^r_k(x,u)]_s$ be the same
series with the inner sum further restricted to the permutations that have exactly $k$ cycles
and whose points among $0, \dots, s-1$ lie in pairwise distinct cycles. If $L$ is a formal
power series in $u$ over $R$ with $L(0) = 0$ and $\exp L = A^r(x,u)$, then the $s$-th formal
derivative in $u$ satisfies

$$\frac{\partial^s}{\partial u^s} [A^r_k(x,u)]_s =
x^s \left(A(x,u) - \sum_{n=0}^{r-1} \frac{A_n(x)\, u^n}{n!}\right)^s \frac{L^{k-s}}{(k-s)!}.$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 37 (`jis-2025-25.5.7-thm-37`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_firstPoints_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-first-points-cycle).

## Iterated derivative of the $q$-analogue for cycles longer than $r$, $s$ points apart

Let $R$ be a commutative $\mathbb{Q}$-algebra, $x, q \in R$, and let $r$, $s$ be natural
numbers with $r \ge 1$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let
$\operatorname{exc}(\sigma)$ be the number of points $i$ with $\sigma(i) > i$ and
$\operatorname{cyc}(\sigma)$ its number of cycles (fixed points counted as cycles of length
one), let $A_n(x) = \sum_{\sigma} x^{\operatorname{exc}(\sigma)}$, summed over all permutations
of $\{0, \dots, n-1\}$, and let $A(x,u) = \sum_{n \ge 0} A_n(x) u^n/n!$. Let $A^r(x,u)$ be the
series $\sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} u^n/n!$ with the inner sum
over the permutations of $\{0, \dots, n-1\}$ all of whose cycles have length greater than $r$,
and let $[A^r(q,x,u)]_s$ be the series
$\sum_{n \ge 0} \sum_{\sigma} x^{\operatorname{exc}(\sigma)} q^{\operatorname{cyc}(\sigma)} u^n/n!$
with the inner sum over the permutations of $\{0, \dots, n-1\}$ all of whose cycles have length
greater than $r$ and whose points among $0, \dots, s-1$ lie in pairwise distinct cycles. If $L$
is a formal power series in $u$ over $R$ with $L(0) = 0$ and $\exp L = A^r(x,u)$, then the
$s$-th formal derivative in $u$ satisfies

$$\frac{\partial^s}{\partial u^s} [A^r(q,x,u)]_s =
q^s x^s \left(A(x,u) - \sum_{n=0}^{r-1} \frac{A_n(x)\, u^n}{n!}\right)^s \exp(qL).$$

The factor $\exp(qL)$ is the paper's $(A^r(x,u))^q$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 38 (`jis-2025-25.5.7-thm-38`).

Stated but not proved: `MetaMathlibExt.rAssociatedPermEGF_firstPoints_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#r-associated-perm-egf-first-points-q-ite).

## Excedances and cycles of involutions

Let $R$ be a commutative $\mathbb{Q}$-algebra,
$x, q \in R$ and $n \ge 0$. For a permutation $\sigma$ write $e(\sigma)$ for the number of $i$ with
$\sigma(i) > i$ and $c(\sigma)$ for its number of cycles, fixed points included. For each $m$ let
$W(m) = \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)}$, summed over the involutions $\sigma$ of
$\{0, \dots, m-1\}$ (permutations all of whose cycles have length at most $2$). Then

$$W(2n) = \sum_{k=0}^{n} \frac{(2n)!}{2^{n-k} (2k)! (n-k)!} q^{n+k} x^{n-k}$$

and

$$W(2n+1) = \sum_{k=0}^{n} \frac{(2n+1)!}{2^{n-k} (2k+1)! (n-k)!} q^{n+k+1} x^{n-k}.$$

The paper prints the summation index as $j$ while the summands use $k$; the sums are read over
$k$, as forced by Corollary 39: an involution of $2n$ (resp. $2n+1$) points with $n - k$
two-cycles has $2k$ (resp. $2k+1$) fixed points.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 40 (`jis-2025-25.5.7-cor-40`).

Stated but not proved: `MetaMathlibExt.involution_excedance_cycle_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#involution-excedance-cycle-sum).

## Excedances and cycles of fixed-point-free involutions

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$ and $n \ge 0$. For a permutation $\sigma$ write $e(\sigma)$ for
the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for its number of cycles, fixed points
included. Summing over the permutations $\sigma$ of $\{0, \dots, 2n-1\}$ all of whose cycles have
length exactly $2$,

$$\sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} = \frac{(2n)!}{2^n\, n!}\, q^n x^n.$$

The paper prints the right-hand side as a sum over $j = 0, \dots, n$ of a summand free of $j$,
which is $n + 1$ times too large (for $n = 1$ the only such involution, $(0\,1)$, has weight
$q x$); the single term is the reading forced by Corollary 41, $\exp(q x u^2/2)$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 42 (`jis-2025-25.5.7-cor-42`).

Stated but not proved: `MetaMathlibExt.fixedPointFreeInvolution_excedance_cycle_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-point-free-involution-excedance-cy).

## Derivative formula for permutations whose first $s$ points lie in distinct cycles

Let
$R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$ and $s \in \mathbb{N}$. For a permutation
$\sigma$ of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with $\sigma(i) > i$. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $A_{[s]}(x,u)$ be the same series
with the inner sum restricted to the $\sigma$ in which no two distinct points less than $s$ lie
in the same cycle. Then the $s$-th derivative in $u$ is

$$\frac{d^s}{du^s} A_{[s]}(x,u) = \bigl(A(x,u) \exp((x-1)u)\bigr)^s A(x,u),$$

where $\exp(F) = \sum_{m \ge 0} F^m/m!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 45 (`jis-2025-25.5.7-cor-45`).

Stated but not proved: `MetaMathlibExt.permEGF_firstPoints_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-egf-first-points-iterate-derivative).

## Derivative formula for permutations with $k$ cycles whose first $s$ points lie in distinct cycles

**Derivative formula for permutations with $k$ cycles whose first $s$ points lie in distinct
cycles.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$ and $s \le k$ natural numbers.
For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with
$\sigma(i) > i$ and $c(\sigma)$ the number of cycles of $\sigma$, fixed points included. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $A_{[s],k}(x,u)$ be the same
series with the inner sum restricted to the $\sigma$ with $c(\sigma) = k$ in which no two
distinct points less than $s$ lie in the same cycle. If $L \in R[[u]]$ has zero constant term
and $\exp(L) = A(x,u)$, where $\exp(F) = \sum_{m \ge 0} F^m/m!$, then the $s$-th derivative in
$u$ is

$$\frac{d^s}{du^s} A_{[s],k}(x,u) =
\bigl(A(x,u) \exp((x-1)u)\bigr)^s \frac{L^{k-s}}{(k-s)!}.$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 46 (`jis-2025-25.5.7-cor-46`).

Stated but not proved: `MetaMathlibExt.permEGF_firstPoints_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-egf-first-points-cycle-count-iterat).

## $q$-analogue of the derivative formula for permutations whose first $s$ points lie in distinct cycles

**$q$-analogue of the derivative formula for permutations whose first $s$ points lie in
distinct cycles.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x, q \in R$ and
$s \in \mathbb{N}$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the
number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ the number of cycles of $\sigma$, fixed points
included. Let $A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$,
the inner sum over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let
$A_{[s]}(q,x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)}$, the
inner sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ in which no two distinct points
less than $s$ lie in the same cycle. If $L \in R[[u]]$ has zero constant term and
$\exp(L) = A(x,u)$, where $\exp(F) = \sum_{m \ge 0} F^m/m!$, then the $s$-th derivative in $u$ is

$$\frac{d^s}{du^s} A_{[s]}(q,x,u) = q^s \bigl(A(x,u) \exp((x-1)u)\bigr)^s \exp(qL).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 47 (`jis-2025-25.5.7-cor-47`).

Stated but not proved: `MetaMathlibExt.permEGF_firstPoints_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 835](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#perm-egf-first-points-q-iterate-derivati).

## Signed excedance sum with weight $-s$ over permutations with separated first points

Let
$R$ be a commutative ring, $x \in R$ and $n, s \ge 0$ integers. For a permutation $\sigma$ write
$e(\sigma)$ for its number of excedances (points $i$ with $\sigma(i) > i$) and $c(\sigma)$ for
its number of cycles, fixed points included. Summing over the permutations $\sigma$ of
$\{0, \dots, n+s-1\}$ in which the points $0, \dots, s-1$ lie in pairwise distinct cycles,
$\sum_{\sigma} x^{e(\sigma)} (-s)^{c(\sigma)} = (-1)^s s^{n+s} (x-1)^n$, with $0^0 = 1$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 48 (`jis-2025-25.5.7-cor-48`).

Stated but not proved: `MetaMathlibExt.firstPoints_excedance_cycle_sum_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 852](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L852). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-excedance-cycle-sum-neg).

## Signed excedance sum with weight $-(s+1)$ over permutations with separated first points

Let $R$ be a commutative ring, $x \in R$ and $n \ge 1$, $s \ge 0$ integers. For a permutation
$\sigma$ write $e(\sigma)$ for its number of excedances (points $i$ with $\sigma(i) > i$) and
$c(\sigma)$ for its number of cycles, fixed points included. Summing over the permutations
$\sigma$ of $\{0, \dots, n+s-1\}$ in which the points $0, \dots, s-1$ lie in pairwise distinct
cycles,
$\sum_{\sigma} x^{e(\sigma)} (-(s+1))^{c(\sigma)} = (-1)^s (s+1)^s (x s^n - (s+1)^n) (x-1)^{n-1}$.

The hypothesis $n \ge 1$ makes $(x-1)^{n-1}$ a polynomial.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 49 (`jis-2025-25.5.7-cor-49`).

Stated but not proved: `MetaMathlibExt.firstPoints_excedance_cycle_sum_neg_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 866](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L866). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#first-points-excedance-cycle-sum-neg-suc).

## Derangements whose first $s$ points lie in distinct cycles

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$ and $s \ge 0$. For a permutation $\sigma$ let $e(\sigma)$ be
its number of excedances (indices $i$ with $\sigma(i) > i$) and $c(\sigma)$ its number of
cycles, fixed points included. Let $A(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} u^n/n!$,
summed over all permutations $\sigma$ of $n$ objects, and let $L \in R[[u]]$ have constant term
$0$ and satisfy $\exp L = A(x,u)$. Let
$D_s(q,x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n!$, the inner sum
over the derangements $\sigma$ of $n$ objects (permutations without fixed points) in which the
first $s$ points (all points, if $n < s$) lie in pairwise distinct cycles. Then the $s$-th
derivative of $D_s$ with respect to $u$ equals $q^s x^s (A(x,u) - 1)^s \exp\big(q\,(L - u)\big)$,
which is the paper's $q^s x^s (A(x,u) - 1)^s (A(x,u) e^{-u})^q$ with the power read through $L$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 51 (`jis-2025-25.5.7-cor-51`).

Stated but not proved: `MetaMathlibExt.derangementEGF_firstPoints_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#derangement-egf-first-points-q-iterate-d).

## Derangements with the first $s$ points in distinct cycles, cycle weight $-s$

Let
$n, s \ge 0$. For a permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices
$i$ with $\sigma(i) > i$) and $c(\sigma)$ its number of cycles, fixed points included. Summing
over the derangements $\sigma$ of $n + s$ objects (permutations without fixed points) in which
the first $s$ points lie in pairwise distinct cycles, the identity
$(x - 1)^s \sum_{\sigma} x^{e(\sigma)} (-s)^{c(\sigma)} = (-1)^s (s x)^s
\sum_{i} \binom{n}{i_1, \dots, i_s} \prod_{j=1}^{s} (x^{i_j} - 1)$
holds in $\mathbb{Z}[x]$, where $i = (i_1, \dots, i_s)$ runs over the $s$-tuples of positive
integers with $i_1 + \dots + i_s = n$ and $\binom{n}{i_1, \dots, i_s}$ is the multinomial
coefficient. This is the paper's formula
$\sum_{\sigma} x^{e(\sigma)} (-s)^{c(\sigma)} = (-1)^s (s x/(x-1))^s \sum_{i}
\binom{n}{i_1, \dots, i_s} \prod_{j} (x^{i_j} - 1)$ with the denominator cleared.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 52 (`jis-2025-25.5.7-cor-52`).

Stated but not proved: `MetaMathlibExt.derangement_firstPoints_excedance_cycle_sum_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 900](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L900). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#derangement-first-points-excedance-cycle).

## Derangements with the first $s$ points in distinct cycles, cycle weight $-(s+1)$

Let
$n, s \ge 0$. For a permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices
$i$ with $\sigma(i) > i$) and $c(\sigma)$ its number of cycles, fixed points included. Summing
over the derangements $\sigma$ of $n + s$ objects (permutations without fixed points) in which
the first $s$ points lie in pairwise distinct cycles, the identity
$(x - 1)^{s+1} \sum_{\sigma} x^{e(\sigma)} (-s-1)^{c(\sigma)} = (-1)^s (s+1)^s x^s
\sum_{\ell=0}^{n} \binom{n}{\ell} (x - x^\ell) \sum_{i} \binom{n-\ell}{i_1, \dots, i_s}
\prod_{j=1}^{s} (x^{i_j} - 1)$
holds in $\mathbb{Z}[x]$, where for each $\ell$ the tuple $i = (i_1, \dots, i_s)$ runs over the
$s$-tuples of positive integers with $i_1 + \dots + i_s = n - \ell$, and
$\binom{n-\ell}{i_1, \dots, i_s}$ is the multinomial coefficient. This is the corrected form of
the paper's formula, with the denominator $(x-1)^{s+1}$ cleared.

The printed Corollary 54 omits the binomial coefficient $\binom{n}{\ell}$ and is false as
printed: for $s = 1$, $n = 3$ and $x = 2$ the left side is $-4$ and the printed right side is
$-20$. The binomial comes from the paper's own proof, which extracts the coefficient of
$u^n/n!$ from the product of the exponential generating functions
$(\sum_{n \ge 1} (x^n - 1) u^n/n!)^s$ and $\sum_{n \ge 0} (x - x^n)/(x-1)\,u^n/n!$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 54 (`jis-2025-25.5.7-cor-54`).

Stated but not proved: `MetaMathlibExt.derangement_firstPoints_excedance_cycle_sum_neg_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 922](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L922). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#derangement-first-points-excedance-cycle-2).

## Excedance generating function of s-fixed-points permutations

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x \in R$ and $s$ a natural number. Call a permutation $\sigma$ of
$\{0, \dots, n-1\}$ an $s$-fixed-points permutation if every fixed point of $\sigma$ is less than
$s$ and any two points less than $s$ in the same cycle of $\sigma$ are equal. Write $e(\sigma)$
for the number of $i$ with $\sigma(i) > i$, let $A(x,u) = \sum_{n \ge 0} \sum_{\sigma}
x^{e(\sigma)} u^n/n!$ over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F(x,u)$ be
the same series restricted to the $s$-fixed-points permutations. Then, as formal power series in
$u$ over $R$,

$$\frac{d^s}{du^s} F(x,u) = \left(A(x,u) \exp((x-1)u)\right)^s A(x,u) \exp(-u).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 57 (`jis-2025-25.5.7-thm-57`).

Stated but not proved: `MetaMathlibExt.fixedPointsPermEGF_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 939](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L939). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-points-perm-egf-iterate-derivative).

## Excedance generating function of s-fixed-points permutations with k cycles

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x \in R$, and $s \le k$ natural numbers. Call a permutation
$\sigma$ of $\{0, \dots, n-1\}$ an $s$-fixed-points permutation if every fixed point of $\sigma$
is less than $s$ and any two points less than $s$ in the same cycle of $\sigma$ are equal. Write
$e(\sigma)$ for the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for the number of cycles
of $\sigma$, fixed points included. Let $A(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)}
u^n/n!$ over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F_k(x,u)$ be the same
series restricted to the $s$-fixed-points permutations with $c(\sigma) = k$. Then for every
formal power series $L$ in $u$ over $R$ with zero constant term and $\exp(L) = A(x,u)$,

$$\frac{d^s}{du^s} F_k(x,u) = \left(A(x,u) \exp((x-1)u)\right)^s \frac{(L - u)^{k-s}}{(k-s)!}.$$

Here $L - u$ is the paper's $\ln(A(x,u) \exp(-u))$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 58 (`jis-2025-25.5.7-thm-58`).

Stated but not proved: `MetaMathlibExt.fixedPointsPermEGF_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 957](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L957). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-points-perm-egf-cycle-count-iterat).

## Cycle-counting excedance generating function of s-fixed-points permutations

Let $R$ be a
commutative $\mathbb{Q}$-algebra, $x, q \in R$ and $s$ a natural number. Call a permutation
$\sigma$ of $\{0, \dots, n-1\}$ an $s$-fixed-points permutation if every fixed point of $\sigma$
is less than $s$ and any two points less than $s$ in the same cycle of $\sigma$ are equal. Write
$e(\sigma)$ for the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for the number of cycles
of $\sigma$, fixed points included. Let $A(x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)}
u^n/n!$ over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let
$F(q,x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n!$ over the
$s$-fixed-points permutations $\sigma$ of $\{0, \dots, n-1\}$. Then for every formal power series
$L$ in $u$ over $R$ with zero constant term and $\exp(L) = A(x,u)$,

$$\frac{d^s}{du^s} F(q,x,u) = q^s \left(A(x,u) \exp((x-1)u)\right)^s \exp(qL) \exp(-qu).$$

Here $\exp(qL)$ is the paper's $(A(x,u))^q$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 59 (`jis-2025-25.5.7-thm-59`).

Stated but not proved: `MetaMathlibExt.fixedPointsPermEGF_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-points-perm-egf-q-iterate-derivati).

## Signed excedance–cycle sum over s-fixed-points permutations, cycle weight -s

Let $R$ be a
commutative ring, $x \in R$, and $s \le n$ natural numbers. Call a permutation $\sigma$ of
$\{0, \dots, n-1\}$ an $s$-fixed-points permutation if every fixed point of $\sigma$ is less than
$s$ and any two points less than $s$ in the same cycle of $\sigma$ are equal. Write $e(\sigma)$
for the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ for the number of cycles of $\sigma$,
fixed points included. Then, summing over the $s$-fixed-points permutations of
$\{0, \dots, n-1\}$,

$$\sum_{\sigma} x^{e(\sigma)} (-s)^{c(\sigma)} = (-1)^s s^n x^{n-s}.$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 60 (`jis-2025-25.5.7-cor-60`).

Stated but not proved: `MetaMathlibExt.fixedPointsPerm_excedance_cycle_sum_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 998](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L998). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-points-perm-excedance-cycle-sum-ne).

## Signed excedance–cycle sum over s-fixed-points permutations, cycle weight -s-1

Let
$s \le n$ be natural numbers. Call a permutation $\sigma$ of $\{0, \dots, n-1\}$ an
$s$-fixed-points permutation if every fixed point of $\sigma$ is less than $s$ and any two points
less than $s$ in the same cycle of $\sigma$ are equal. Write $e(\sigma)$ for the number of $i$
with $\sigma(i) > i$ and $c(\sigma)$ for the number of cycles of $\sigma$, fixed points included.
Then, summing over the $s$-fixed-points permutations $\sigma$ of $\{0, \dots, n-1\}$, the sum
$S = \sum_{\sigma} x^{e(\sigma)} (-s-1)^{c(\sigma)}$ in the polynomial ring $\mathbb{Z}[x]$
satisfies

$$(x - 1) S = (-1)^s (s+1)^s \left(x (s x + 1)^{n-s} - (s+1)^{n-s} x^{n-s}\right).$$

This is the paper's formula with the denominator $x - 1$ cleared.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 61 (`jis-2025-25.5.7-cor-61`).

Stated but not proved: `MetaMathlibExt.fixedPointsPerm_excedance_cycle_sum_neg_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1013](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1013). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#fixed-points-perm-excedance-cycle-sum-ne-2).

## Derivative formula for prescribed cycle lengths through the first $s$ points

Let $R$ be
a commutative $\mathbb{Q}$-algebra, $x \in R$, $s \in \mathbb{N}$ and
$r : \mathbb{N} \to \mathbb{N}$ with $r(i) \ge 2$ for all $i < s$. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with $\sigma(i) > i$, and for $m \ge 0$
let $A_m(x) = \sum_{\sigma} x^{e(\sigma)}$ over all permutations $\sigma$ of
$\{0, \dots, m-1\}$. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F(x,u)$ be the same series with
the inner sum restricted to the $\sigma$ in which no two distinct points less than $s$ lie in
the same cycle and each point $i < s$ lies in a cycle of length $r(i)$. Then the $s$-th
derivative in $u$ is

$$\frac{d^s}{du^s} F(x,u) = x^s \Bigl(\prod_{i=0}^{s-1}
\frac{A_{r(i)-1}(x)\, u^{r(i)-1}}{(r(i)-1)!}\Bigr) A(x,u).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 62 (`jis-2025-25.5.7-thm-62`).

Stated but not proved: `MetaMathlibExt.prescribedCyclePermEGF_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1029](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#prescribed-cycle-perm-egf-iterate-deriva).

## Derivative formula for prescribed cycle lengths through the first $s$ points, with $k$ cycles

**Derivative formula for prescribed cycle lengths through the first $s$ points, with $k$
cycles.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x \in R$, $s \le k$ natural numbers
and $r : \mathbb{N} \to \mathbb{N}$ with $r(i) \ge 2$ for all $i < s$. For a permutation $\sigma$
of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$
the number of cycles of $\sigma$, fixed points included, and for $m \ge 0$ let
$A_m(x) = \sum_{\sigma} x^{e(\sigma)}$ over all permutations $\sigma$ of $\{0, \dots, m-1\}$. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let $F_k(x,u)$ be the same series with
the inner sum restricted to the $\sigma$ with $c(\sigma) = k$ in which no two distinct points
less than $s$ lie in the same cycle and each point $i < s$ lies in a cycle of length $r(i)$. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A(x,u)$, where
$\exp(G) = \sum_{m \ge 0} G^m/m!$, then the $s$-th derivative in $u$ is

$$\frac{d^s}{du^s} F_k(x,u) = x^s \Bigl(\prod_{i=0}^{s-1}
\frac{A_{r(i)-1}(x)\, u^{r(i)-1}}{(r(i)-1)!}\Bigr) \frac{L^{k-s}}{(k-s)!}.$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 63 (`jis-2025-25.5.7-thm-63`).

Stated but not proved: `MetaMathlibExt.prescribedCyclePermEGF_cycleCount_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1052](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1052). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#prescribed-cycle-perm-egf-cycle-count-it).

## $q$-analogue of the derivative formula for prescribed cycle lengths through the first $s$ points

**$q$-analogue of the derivative formula for prescribed cycle lengths through the first $s$
points.** Let $R$ be a commutative $\mathbb{Q}$-algebra, $x, q \in R$, $s \in \mathbb{N}$ and
$r : \mathbb{N} \to \mathbb{N}$ with $r(i) \ge 2$ for all $i < s$. For a permutation $\sigma$ of
$\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with $\sigma(i) > i$ and $c(\sigma)$ the
number of cycles of $\sigma$, fixed points included, and for $m \ge 0$ let
$A_m(x) = \sum_{\sigma} x^{e(\sigma)}$ over all permutations $\sigma$ of $\{0, \dots, m-1\}$. Let
$A(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} \in R[[u]]$, the inner sum
over all permutations $\sigma$ of $\{0, \dots, n-1\}$, and let
$F(q,x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)}$, the inner
sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ in which no two distinct points less
than $s$ lie in the same cycle and each point $i < s$ lies in a cycle of length $r(i)$. If
$L \in R[[u]]$ has zero constant term and $\exp(L) = A(x,u)$, where
$\exp(G) = \sum_{m \ge 0} G^m/m!$, then the $s$-th derivative in $u$ is

$$\frac{d^s}{du^s} F(q,x,u) = q^s x^s \Bigl(\prod_{i=0}^{s-1}
\frac{A_{r(i)-1}(x)\, u^{r(i)-1}}{(r(i)-1)!}\Bigr) \exp(qL).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 64 (`jis-2025-25.5.7-thm-64`).

Stated but not proved: `MetaMathlibExt.prescribedCyclePermEGF_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1078](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1078). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#prescribed-cycle-perm-egf-q-iterate-deri).

## Permutations with all cycle lengths in a prescribed set

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$, and let $\mathcal{R}$ be a finite set of integers, each at
least $2$. For a permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices $i$
with $\sigma(i) > i$) and $c(\sigma)$ its number of cycles, fixed points included, and for
$j \ge 0$ let $A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over all permutations $\sigma$ of
$j$ objects. Then in $R[[u]]$
$\sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n! =
\exp\big(q x \sum_{r \in \mathcal{R}} A_{r-1}(x)\,u^r/r!\big)$, where the inner sum on the left
runs over the permutations $\sigma$ of $n$ objects all of whose cycles, fixed points included,
have length in $\mathcal{R}$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 65 (`jis-2025-25.5.7-thm-65`).

Stated but not proved: `MetaMathlibExt.cycleLengthsInEGF_q_eq_exp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#cycle-lengths-in-egf-q-eq-exp).

## $q$-analogue of the derivative formula for prescribed cycle lengths through the first $s$ points, other cycle lengths in a set $\mathcal{R}$

**$q$-analogue of the derivative formula for prescribed cycle lengths through the first $s$
points, other cycle lengths in a set $\mathcal{R}$.** Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$, $s \in \mathbb{N}$, $r : \mathbb{N} \to \mathbb{N}$ with
$r(i) \ge 2$ for all $i < s$, and $\mathcal{R}$ a finite set of natural numbers, each at least
$2$. For a permutation $\sigma$ of $\{0, \dots, n-1\}$ let $e(\sigma)$ be the number of $i$ with
$\sigma(i) > i$ and $c(\sigma)$ the number of cycles of $\sigma$, fixed points included, and for
$m \ge 0$ let $A_m(x) = \sum_{\sigma} x^{e(\sigma)}$ over all permutations $\sigma$ of
$\{0, \dots, m-1\}$. Let $B(x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)}$,
the inner sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ all of whose cycles (fixed
points included) have length in $\mathcal{R}$. Let
$F(q,x,u) = \sum_{n \ge 0} \frac{u^n}{n!} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)}$, the inner
sum over the permutations $\sigma$ of $\{0, \dots, n-1\}$ in which no two distinct points less
than $s$ lie in the same cycle, each point $i < s$ lies in a cycle of length $r(i)$, and every
cycle containing no point less than $s$ has length in $\mathcal{R}$. If $L \in R[[u]]$ has zero
constant term and $\exp(L) = B(x,u)$, where $\exp(G) = \sum_{m \ge 0} G^m/m!$, then the $s$-th
derivative in $u$ is

$$\frac{d^s}{du^s} F(q,x,u) = q^s x^s \Bigl(\prod_{i=0}^{s-1}
\frac{A_{r(i)-1}(x)\, u^{r(i)-1}}{(r(i)-1)!}\Bigr) \exp(qL).$$

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Theorem 66 (`jis-2025-25.5.7-thm-66`).

Stated but not proved: `MetaMathlibExt.prescribedCycleLengthsInEGF_q_iterate_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#prescribed-cycle-lengths-in-egf-q-iterat).

## Permutations avoiding a prescribed set of cycle lengths

Let $R$ be a commutative
$\mathbb{Q}$-algebra, $x, q \in R$, and let $\mathcal{R}$ be a finite set of integers, each at
least $2$. For a permutation $\sigma$ let $e(\sigma)$ be its number of excedances (indices $i$
with $\sigma(i) > i$) and $c(\sigma)$ its number of cycles, fixed points included; for
$j \ge 0$ let $A_j(x) = \sum_{\sigma} x^{e(\sigma)}$, summed over all permutations $\sigma$ of
$j$ objects; and let $A(q,x,u) = \sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n!$,
summed over all permutations $\sigma$ of $n$ objects. Then in $R[[u]]$
$\sum_{n \ge 0} \sum_{\sigma} x^{e(\sigma)} q^{c(\sigma)} u^n/n! =
A(q,x,u) \exp\big(-q x \sum_{r \in \mathcal{R}} A_{r-1}(x)\,u^r/r!\big)$, where the inner sum on
the left runs over the permutations $\sigma$ of $n$ objects none of whose cycles has length in
$\mathcal{R}$.

## Sources

- Imboa-Navalona Manjaka Rakotoson and Fanja Rakotondrajao, *Associated Stirling Eulerian Numbers and Their q-Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.7, Corollary 67 (`jis-2025-25.5.7-cor-67`).

Stated but not proved: `MetaMathlibExt.cycleLengthsNotInEGF_q_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean, line 1149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AssociatedStirlingEulerianWanted.lean#L1149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html#cycle-lengths-not-in-egf-q-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Associated Stirling–Eulerian numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/associated-stirling-eulerian-numbers)
