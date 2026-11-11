---
declaration: section
origin: cited
lean: MetaMathlibExt.stirlingSecond_addition, MetaMathlibExt.stirlingSecond_mul_factorial_eq_sum, MetaMathlibExt.hasSum_stirlingSecond_succ_egf
statement: formalized
proof: formalized
---

# Stirling numbers of the second kind

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind/index.html).

## Addition formula for Stirling numbers of the second kind

Write $S(n,k)$ for the Stirling
numbers of the second kind. For all natural numbers $u$, $v$ and $k$ with $u > 0$,

$$S(u+v,k) = \sum_{n=1}^{k} S(u,n) \sum_{m=k-n}^{v} \binom{v}{m} S(m,k-n)\, n^{v-m},$$

where an inner sum with $k - n > v$ is empty.

The source does not state the hypothesis $u > 0$, but the formula needs it: for $u = 0$ and
$v = k = 1$ the left side is $S(1,1) = 1$, while every term on the right has the factor
$S(0,1) = 0$.

## Sources

- Grzegorz Rządkowski, "Two Formulas for Successive Derivatives and Their Applications," Journal of Integer Sequences 12 (2009), Article 09.8.2, Theorem, equation (ex33), lines 198–204, https://cs.uwaterloo.ca/journals/JIS/VOL12/Rzadkowski/rzadkowski3.tex

Formalized by `MetaMathlibExt.stirlingSecond_addition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingSecondAddition.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingSecondAddition.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind/index.html#stirling-second-addition).

## Explicit formula for Stirling numbers of the second kind

Write $S(t,k)$ for the Stirling
numbers of the second kind. For all natural numbers $t$ and $k$,

$$k!\, S(t,k) = \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j}\, j^t,$$

with the convention $0^0 = 1$.

## Sources

- R. L. Graham, D. E. Knuth, and O. Patashnik, *Concrete Mathematics*, 2nd ed., Section 6.1.

Formalized by `MetaMathlibExt.stirlingSecond_mul_factorial_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingSecondExplicit.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingSecondExplicit.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind/index.html#stirling-second-mul-factorial-eq-sum).

## Exponential generating function of a shifted Stirling column

Write $S(n,k)$ for the
Stirling numbers of the second kind. For every natural number $j$ and every real number $x$, the
series

$$\sum_{n=0}^{\infty} S(n+1,j+1)\, \frac{x^n}{n!}$$

converges unconditionally to $e^x (e^x - 1)^j / j!$.

## Sources

- R. L. Graham, D. E. Knuth, and O. Patashnik, *Concrete Mathematics*, 2nd ed., Section 7.6 (the column generating function `(e^x - 1)^(j+1)/(j+1)!`, differentiated).

Formalized by `MetaMathlibExt.hasSum_stirlingSecond_succ_egf`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingSecondExplicit.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingSecondExplicit.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind/index.html#has-sum-stirling-second-succ-egf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stirling numbers of the second kind](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-numbers-of-the-second-kind)
