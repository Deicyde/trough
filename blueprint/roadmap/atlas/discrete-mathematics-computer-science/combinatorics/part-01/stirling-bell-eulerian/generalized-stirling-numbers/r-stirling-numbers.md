---
declaration: section
origin: cited
lean: MetaMathlibExt.rStirlingFirst, MetaMathlibExt.rStirlingFirst_self, MetaMathlibExt.rStirlingFirst_zero_of_pos, MetaMathlibExt.rStirlingFirst_succ, MetaMathlibExt.rStirlingFirst_eq_alternating_sum, MetaMathlibExt.rStirlingSecond, MetaMathlibExt.rStirlingSecond_add_add, MetaMathlibExt.rStirlingSecond_eq_zero
statement: formalized
proof: formalized
---

# r-Stirling numbers

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html).

## Unsigned r-Stirling numbers of the first kind

For natural numbers $n$, $m$ and $r$, the
unsigned $r$-Stirling number of the first kind $[n, m]_r$ is the coefficient of $x^m$ in the
polynomial with natural-number coefficients

$$x^r \prod_{r \le k < n} (x + k).$$

For $n \ge r$ this is Broder's characterization
$\sum_m [n, m]_r \, x^m = x^r (x+r)(x+r+1) \cdots (x+n-1)$. For $n < r$ the product is empty, so
the polynomial is $x^r$.

## Sources

- A. Z. Broder, "The r-Stirling numbers", Stanford Computer Science Report STAN-CS-82-949 (December 1982), PDF page 12 / printed page 9, Equation (24); journal version: Discrete Mathematics 49 (1984), 241-259, DOI 10.1016/0012-365X(84)90161-4.

Formalized by `MetaMathlibExt.rStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-first).

## Initial row of the r-Stirling numbers of the first kind

For all natural numbers $m$ and
$r$, the unsigned $r$-Stirling number of the first kind $[r, m]_r$ equals $1$ if $m = r$ and $0$
otherwise: when the first index equals $r$, the product in the definition is empty, so the
polynomial is $x^r$.

Formalized by `MetaMathlibExt.rStirlingFirst_self`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-first-self).

## Vanishing of the r-Stirling numbers of the first kind with second index zero

For all
natural numbers $N$ and $r$ with $r \ge 1$, the unsigned $r$-Stirling number of the first kind
$[N, 0]_r$ is $0$: the defining polynomial is divisible by $x$, so its constant coefficient
vanishes.

Formalized by `MetaMathlibExt.rStirlingFirst_zero_of_pos`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-first-zero-of-pos).

## Recurrence for the r-Stirling numbers of the first kind

For natural numbers $n$, $m$ and
$r$ with $1 \le r \le n$, the unsigned $r$-Stirling numbers of the first kind $[n, m]_r$ satisfy
$[n+1, m]_r = [n, m-1]_r + n \, [n, m]_r$, where for $m = 0$ the term $[n, m-1]_r$ is read as
$[n, 0]_r$.

Formalized by `MetaMathlibExt.rStirlingFirst_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-first-succ).

## Broder's alternating expansion of the r-Stirling numbers of the first kind

Let $n$, $m$
and $r$ be natural numbers with $1 \le r \le n$. Write $[n, m]_r$ for the unsigned $r$-Stirling
number of the first kind, $[a, b]$ for the unsigned Stirling number of the first kind and
$\lbrace a, b \rbrace$ for the Stirling number of the second kind. Then, in the integers,

$$(-1)^r [n, m]_r = \sum_{k=r}^{n+r-m} [n, m+k-r] \, \lbrace k-1, r-1 \rbrace \, (-1)^k.$$

Broder's Equation (43) sums over all $k$; every term outside the range above vanishes, since
$\lbrace k-1, r-1 \rbrace$ vanishes for $k < r$ and $[n, m+k-r]$ vanishes for $k > n + r - m$.

## Sources

- A. Z. Broder, "The r-Stirling numbers", Stanford Computer Science Report STAN-CS-82-949 (December 1982), PDF page 16 / printed page 13, Equation (43); journal version: Discrete Mathematics 49 (1984), 241-259, DOI 10.1016/0012-365X(84)90161-4.

Formalized by `MetaMathlibExt.rStirlingFirst_eq_alternating_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingFirstAlternatingExpansion.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-first-eq-alternating-sum).

## r-Stirling numbers of the second kind

For natural numbers $n$, $m$ and $r$, Broder's
r-Stirling number of the second kind ${n \brace m}_r$ is $0$ unless $r \le m$ and $r \le n$, and
otherwise

$${n \brace m}_r = \sum_{i=0}^{n-r} \binom{n-r}{i} {n-r-i \brace m-r} r^i,$$

where ${a \brace b}$ denotes the Stirling number of the second kind (and $0^0 = 1$).

## Sources

- A. Z. Broder, *The r-Stirling numbers*, Discrete Mathematics 49 (1984), 241-259; Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 4 (exponential generating function of `{m+v \brace k+v}_v`).

Formalized by `MetaMathlibExt.rStirlingSecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second).

## Finite-sum formula for r-Stirling numbers of the second kind

For all natural numbers
$n$, $m$ and $r$, the r-Stirling number of the second kind ${n+r \brace m+r}_r$ satisfies

$${n+r \brace m+r}_r = \sum_{i=0}^{n} \binom{n}{i} {n-i \brace m} r^i,$$

where ${a \brace b}$ denotes the Stirling number of the second kind (and $0^0 = 1$).

## Sources

- A. Z. Broder, *The r-Stirling numbers*, Discrete Mathematics 49 (1984), 241-259.

Formalized by `MetaMathlibExt.rStirlingSecond_add_add`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second-add-add).

## Vanishing of r-Stirling numbers of the second kind

For natural numbers $n$, $m$ and
$r$ with $m < r$ or $n < r$, the r-Stirling number of the second kind ${n \brace m}_r$ is $0$.

## Sources

- A. Z. Broder, *The r-Stirling numbers*, Discrete Mathematics 49 (1984), 241-259.

Formalized by `MetaMathlibExt.rStirlingSecond_eq_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second-eq-zero).

## r-Stirling numbers of the second kind for r = 0

For all natural numbers $n$ and $m$,
the r-Stirling number of the second kind ${n \brace m}_0$ equals the Stirling number of the
second kind ${n \brace m}$.

## Sources

- A. Z. Broder, *The r-Stirling numbers*, Discrete Mathematics 49 (1984), 241-259.

Formalized by `MetaMathlibExt.rStirlingSecond_zero_right`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second-zero-right).

## r-Stirling numbers of the second kind with exactly r blocks

For all natural numbers $n$
and $r$, the r-Stirling number of the second kind ${n+r \brace r}_r$ equals $r^n$ (with
$0^0 = 1$).

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 4 (exponential generating function at `k = 0`).

Formalized by `MetaMathlibExt.rStirlingSecond_add_self`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second-add-self).

## r-Stirling numbers as generalized Stirling numbers

For all natural numbers $n$, $m$
and $r$, the r-Stirling number of the second kind ${n+r \brace m+r}_r$, viewed as a real number,
equals the generalized Stirling number of the second kind of $n$ and $m$ (after Carlitz and
Broder) at the real parameter $x = r$.

## Sources

- A. Z. Broder, *The r-Stirling numbers*, Discrete Mathematics 49 (1984), 241-259.

Formalized by `MetaMathlibExt.rStirlingSecond_add_add_eq_generalizedStirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RStirlingSecond.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html#r-stirling-second-add-add-eq-generalized).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: r-Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/r-stirling-numbers)
