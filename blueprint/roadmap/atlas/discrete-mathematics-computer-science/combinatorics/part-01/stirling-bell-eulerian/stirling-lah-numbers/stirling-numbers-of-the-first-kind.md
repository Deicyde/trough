---
declaration: section
origin: cited
lean: MetaMathlibExt.signedStirlingFirst, MetaMathlibExt.cycleQuotientCount, MetaMathlibExt.cycleQuotientCount_eq, MetaMathlibExt.card_perm_cycleCount_eq_stirlingFirst, Nat.sum_stirlingFirst_mul_X_pow, Nat.sum_stirlingFirst_mul_pow, MetaMathlibExt.stirlingFirst_addition
statement: formalized
proof: formalized
---

# Stirling numbers of the first kind

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html).

## Signed Stirling numbers of the first kind

For natural numbers $n$ and $k$, the signed
Stirling number of the first kind is the integer $(-1)^{n-k} c(n,k)$, where $c(n,k)$ is the
unsigned Stirling number of the first kind (the number of permutations of $n$ elements with
exactly $k$ cycles) and $n - k$ is truncated subtraction, equal to $0$ when $k > n$.

Formalized by `MetaMathlibExt.signedStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SignedStirlingFirst.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SignedStirlingFirst.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#signed-stirling-first).

## Number of cycles of a permutation

For a permutation $\sigma$ of a finite type $\alpha$,
the number of cycles of $\sigma$, counting each fixed point as a cycle of length one, is the
number of equivalence classes of $\alpha$ under the relation that holds between $x$ and $y$ when
$\sigma^i(x) = y$ for some integer $i$.

Formalized by `MetaMathlibExt.cycleQuotientCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Stirling.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Stirling.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#cycle-quotient-count).

## Counting cycles via the cycle type

For a permutation $\sigma$ of a finite type, the
number of cycles of $\sigma$, counting each fixed point as a cycle of length one, equals the
number of cycles of $\sigma$ of length at least $2$ (the length of its cycle type) plus the
number of fixed points of $\sigma$.

Formalized by `MetaMathlibExt.cycleQuotientCount_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Stirling.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Stirling.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#cycle-quotient-count-eq).

## Stirling numbers of the first kind count permutations by cycles

For all natural
numbers $n$ and $k$, the number of permutations $\sigma$ of $\{0, \dots, n-1\}$ such that the
number of cycles of $\sigma$ of length at least $2$ plus the number of fixed points of $\sigma$
equals $k$ is the unsigned Stirling number of the first kind $c(n, k)$. In other words,
$c(n, k)$ counts the permutations of an $n$-element set with exactly $k$ cycles, each fixed
point counted as a cycle of length one.

Formalized by `MetaMathlibExt.card_perm_cycleCount_eq_stirlingFirst`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Stirling.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Stirling.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#card-perm-cycle-count-eq-stirling-first).

## Rising factorial generates Stirling numbers of the first kind

The rising factorial is the generating polynomial of the unsigned Stirling numbers of the
first kind: `ascPochhammer S n = ∑_{k=0}^{n} stirlingFirst n k * X ^ k`
(Graham–Knuth–Patashnik, §6.1).

Formalized by `Nat.sum_stirlingFirst_mul_X_pow`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingAscPochhammer.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingAscPochhammer.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#sum-stirling-first-mul-x-pow).

## Stirling numbers of the first kind and the rising factorial

`∑_{k=0}^{n} stirlingFirst n k * x ^ k = x (x + 1) ⋯ (x + n - 1)`
(Graham–Knuth–Patashnik, §6.1).

Formalized by `Nat.sum_stirlingFirst_mul_pow`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingAscPochhammer.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingAscPochhammer.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#sum-stirling-first-mul-pow).

## Addition formula for Stirling numbers of the first kind

Write $c(n,k)$ for the unsigned
Stirling numbers of the first kind and $u^{\overline{i}} = u(u+1)\cdots(u+i-1)$ for the rising
factorial. For all natural numbers $u$, $v$ and $k$,

$$c(u+v,k) = \sum_{j=0}^{v} \sum_{i=0}^{v} \binom{v}{i}\, u^{\overline{i}}\, c(v-i,j)\, c(u,k-j),$$

where a term with $j > k$ is read as $0$.

## Sources

- Grzegorz Rządkowski, "Two Formulas for Successive Derivatives and Their Applications," Journal of Integer Sequences 12 (2009), Article 09.8.2, Theorem, equation (ex44), lines 257–263, https://cs.uwaterloo.ca/journals/JIS/VOL12/Rzadkowski/rzadkowski3.tex

Formalized by `MetaMathlibExt.stirlingFirst_addition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingFirstAddition.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingFirstAddition.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html#stirling-first-addition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stirling numbers of the first kind](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-first-kind)
