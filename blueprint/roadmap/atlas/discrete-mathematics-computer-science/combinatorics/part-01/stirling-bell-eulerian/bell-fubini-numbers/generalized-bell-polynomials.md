---
declaration: section
origin: cited
lean: MetaMathlibExt.genBellNumber, MetaMathlibExt.genBellPolynomial, MetaMathlibExt.genStirling_succ_succ, MetaMathlibExt.genBellPolynomial_eval_one
statement: formalized
proof: formalized
---

# Generalized Bell polynomials

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html).

## Generalized Bell numbers

For a commutative ring $R$, elements $s, h \in R$ and a natural
number $n$, the generalized Bell number is

$$\mathfrak{B}_{s;h}(n) = \sum_{k=0}^{n} \mathfrak{S}_{s;h}(n, k),$$

where the generalized Stirling numbers $\mathfrak{S}_{s;h}(a, j) \in R$ are defined for all
natural numbers $a$ and $j$ by $\mathfrak{S}_{s;h}(0, 0) = 1$,
$\mathfrak{S}_{s;h}(0, j + 1) = \mathfrak{S}_{s;h}(a + 1, 0) = 0$ and
$\mathfrak{S}_{s;h}(a + 1, j + 1) = \mathfrak{S}_{s;h}(a, j) +
h\,(j + 1 + s \max(a - j - 1, 0))\,\mathfrak{S}_{s;h}(a, j + 1)$; here the natural number
$\max(a - j - 1, 0)$ is viewed as an element of $R$.

Formalized by `MetaMathlibExt.genBellNumber`, a definition declared in [MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html#gen-bell-number).

## Generalized Bell polynomials

For a commutative ring $R$, elements $s, h \in R$, a natural
number $n$ and $x \in R$, the generalized Bell polynomial evaluated at $x$ is

$$\mathfrak{B}_{s;h|n}(x) = \sum_{k=0}^{n} \mathfrak{S}_{s;h}(n, k)\, x^k,$$

where the generalized Stirling numbers $\mathfrak{S}_{s;h}(a, j) \in R$ are defined for all
natural numbers $a$ and $j$ by $\mathfrak{S}_{s;h}(0, 0) = 1$,
$\mathfrak{S}_{s;h}(0, j + 1) = \mathfrak{S}_{s;h}(a + 1, 0) = 0$ and
$\mathfrak{S}_{s;h}(a + 1, j + 1) = \mathfrak{S}_{s;h}(a, j) +
h\,(j + 1 + s \max(a - j - 1, 0))\,\mathfrak{S}_{s;h}(a, j + 1)$; here the natural number
$\max(a - j - 1, 0)$ is viewed as an element of $R$.

Formalized by `MetaMathlibExt.genBellPolynomial`, a definition declared in [MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html#gen-bell-polynomial).

## Recurrence for generalized Stirling numbers

Let $R$ be a commutative ring and
$s, h \in R$. The generalized Stirling numbers $\mathfrak{S}_{s;h}(n, k) \in R$ are defined by
$\mathfrak{S}_{s;h}(0, 0) = 1$, $\mathfrak{S}_{s;h}(0, k + 1) = \mathfrak{S}_{s;h}(n + 1, 0) = 0$
and the recurrence below. For all natural numbers $n$ and $k$,

$$\mathfrak{S}_{s;h}(n + 1, k + 1) = \mathfrak{S}_{s;h}(n, k) +
h\,(k + 1 + s \max(n - k - 1, 0))\,\mathfrak{S}_{s;h}(n, k + 1).$$

Here $\max(n - k - 1, 0)$ is a natural number viewed as an element of $R$.

Formalized by `MetaMathlibExt.genStirling_succ_succ`, a theorem declared in [MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html#gen-stirling-succ-succ).

## Generalized Bell polynomials at one

For a commutative ring $R$, elements $s, h \in R$ and
a natural number $n$, the generalized Bell polynomial $\mathfrak{B}_{s;h|n}$ evaluated at $x = 1$
equals the generalized Bell number $\mathfrak{B}_{s;h}(n)$.

Formalized by `MetaMathlibExt.genBellPolynomial_eval_one`, a theorem declared in [MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/GeneralizedBellPolynomial.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html#gen-bell-polynomial-eval-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Bell polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/generalized-bell-polynomials)
