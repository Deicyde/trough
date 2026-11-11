---
declaration: section
origin: cited
lean: MetaMathlibExt.stirling_triple_ratio_bounds_choose, MetaMathlibExt.mul_stirlingSecond_sub_gt, MetaMathlibExt.symm_triple_ratio_of_logConcave, MetaMathlibExt.symm_triple_ratio_of_logConvex
statement: formalized
---

# Triple products of Stirling numbers

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html).

## Triple products of Stirling numbers bracket the binomial coefficient

Let $n$, $p$ and
$j$ be positive integers with $p \le n$. Write $S(m, i)$ for the Stirling number of the second
kind (the number of partitions of an $m$-element set into $i$ nonempty blocks) and $c(m, i)$ for
the unsigned Stirling number of the first kind (the number of permutations of $m$ elements with
exactly $i$ cycles). Then, as rational numbers,
$\frac{c(p + j, j)\, c(n + j, p + j)}{c(n + j, j)} \le \binom{n}{p} \le
\frac{S(p + j, j)\, S(n + j, p + j)}{S(n + j, j)}$.

## Sources

- René Gy, *On Certain Products of Three Stirling Numbers*, INTEGERS 26 (2026), Article A108, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.stirling_triple_ratio_bounds_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html#stirling-triple-ratio-bounds-choose).

## Gy's inequality for Stirling numbers of the second kind

Let $n$ and $k$ be natural
numbers with $0 < k \le n$, and write $S(m, i)$ for the Stirling number of the second kind, the
number of partitions of an $m$-element set into $i$ nonempty blocks. Then
$(n - 2k)\,S(n + 1, n + 1 - k) < n\,S(n, n - k)$, where the left side is computed in the
integers, so that $n - 2k$ may be negative.

## Sources

- René Gy, *On Certain Products of Three Stirling Numbers*, INTEGERS 26 (2026), Article A108, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.mul_stirlingSecond_sub_gt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html#mul-stirling-second-sub-gt).

## Gy's triple-ratio inequalities for log-concave sequences

Let $n$, $p$ and $j$ be
positive integers, at least two of which equal $1$, and let $x_1, x_2, \dots$ be positive reals
with $x_{k-1} x_{k+1} \le x_k^2$ for all $k \ge 2$. For $m \ge 0$ write $e_i(m)$ and $h_i(m)$ for
the elementary and the complete homogeneous symmetric polynomials of degree $i$ evaluated at
$(x_1, \dots, x_m)$, and put $N = n + p + j$. Then

$$\frac{e_{n+p}(N)}{e_{n+p}(N-1)} \le \frac{e_n(N)}{e_n(N-1)} \cdot \frac{e_p(p+j)}{e_p(p+j-1)}$$

and

$$\frac{h_n(p+j+1)}{h_n(p+j)} \cdot \frac{h_p(j+1)}{h_p(j)} \le \frac{h_{n+p}(j+1)}{h_{n+p}(j)}.$$

## Sources

- René Gy, *On Certain Products of Three Stirling Numbers*, INTEGERS 26 (2026), Article A108, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.symm_triple_ratio_of_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html#symm-triple-ratio-of-log-concave).

## Gy's triple-ratio inequalities for log-convex sequences

Let $n$, $p$ and $j$ be
positive integers, at least two of which equal $1$, and let $x_1, x_2, \dots$ be positive reals
with $x_k^2 \le x_{k-1} x_{k+1}$ for all $k \ge 2$. For $m \ge 0$ write $e_i(m)$ and $h_i(m)$ for
the elementary and the complete homogeneous symmetric polynomials of degree $i$ evaluated at
$(x_1, \dots, x_m)$, and put $N = n + p + j$. Then

$$\frac{e_n(N)}{e_n(N-1)} \cdot \frac{e_p(p+j)}{e_p(p+j-1)} \le \frac{e_{n+p}(N)}{e_{n+p}(N-1)}$$

and

$$\frac{h_{n+p}(j+1)}{h_{n+p}(j)} \le \frac{h_n(p+j+1)}{h_n(p+j)} \cdot \frac{h_p(j+1)}{h_p(j)}.$$

## Sources

- René Gy, *On Certain Products of Three Stirling Numbers*, INTEGERS 26 (2026), Article A108, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.symm_triple_ratio_of_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingTripleProductWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html#symm-triple-ratio-of-log-convex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triple products of Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/triple-products-of-stirling-numbers)
