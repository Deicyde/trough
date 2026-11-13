---
declaration: section
origin: cited
lean: MetaMathlibExt.jacobiStirlingFirstPoly, MetaMathlibExt.jacobiStirlingFirst, MetaMathlibExt.jacobiStirlingFirst_initial_row, MetaMathlibExt.jacobiStirlingFirst_recurrence, MetaMathlibExt.jacobiStirlingFirst_support, MetaMathlibExt.jacobiStirlingFirst_diagonal, MetaMathlibExt.legendreStirlingFirstPoly, MetaMathlibExt.legendreStirlingFirst
statement: formalized
proof: formalized
---

# Jacobi–Stirling and Legendre–Stirling numbers

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html).

## Generating polynomial of the first-kind Jacobi–Stirling numbers

For a commutative ring
$R$, an element $\zeta \in R$ and a natural number $n$, the $n$-th first-kind Jacobi–Stirling
generating polynomial is $\prod_{i=0}^{n-1} (X - i(i + \zeta))$ in $R[X]$.

Formalized by `MetaMathlibExt.jacobiStirlingFirstPoly`, a definition declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first-poly).

## First-kind Jacobi–Stirling numbers

For a commutative ring $R$, an element $\zeta \in R$
and natural numbers $n$ and $k$, the first-kind Jacobi–Stirling number $J(n,k;\zeta)$ is the
coefficient of $X^k$ in the polynomial $\prod_{i=0}^{n-1} (X - i(i + \zeta))$ over $R$.

Formalized by `MetaMathlibExt.jacobiStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first).

## Initial row of the first-kind Jacobi–Stirling numbers

For every commutative ring $R$,
every $\zeta \in R$ and every natural number $k$, the first-kind Jacobi–Stirling number
$J(0,k;\zeta)$ equals $1$ if $k = 0$ and $0$ otherwise.

Formalized by `MetaMathlibExt.jacobiStirlingFirst_initial_row`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first-initial-row).

## Recurrence for the first-kind Jacobi–Stirling numbers

For every commutative ring $R$,
every $\zeta \in R$ and all natural numbers $n$ and $k$, the first-kind Jacobi–Stirling numbers
satisfy $J(n+1,k+1;\zeta) = J(n,k;\zeta) - n(n + \zeta)\,J(n,k+1;\zeta)$.

Formalized by `MetaMathlibExt.jacobiStirlingFirst_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first-recurrence).

## First-kind Jacobi–Stirling numbers vanish above the diagonal

For every commutative ring
$R$, every $\zeta \in R$ and all natural numbers $n < k$, the first-kind Jacobi–Stirling number
$J(n,k;\zeta)$ equals $0$.

Formalized by `MetaMathlibExt.jacobiStirlingFirst_support`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first-support).

## Diagonal of the first-kind Jacobi–Stirling numbers

For every commutative ring $R$, every
$\zeta \in R$ and every natural number $n$, the first-kind Jacobi–Stirling number
$J(n,n;\zeta)$ equals $1$.

Formalized by `MetaMathlibExt.jacobiStirlingFirst_diagonal`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/JacobiStirlingFirstKind.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#jacobi-stirling-first-diagonal).

## Generating polynomial of the Legendre–Stirling numbers of the first kind

For a natural
number $n$, this is the polynomial $\prod_{i=0}^{n-1} \bigl(X - i(i+1)\bigr)$ with integer
coefficients; for $n = 0$ it is the empty product $1$.

Formalized by `MetaMathlibExt.legendreStirlingFirstPoly`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first-poly).

## Legendre–Stirling numbers of the first kind

For natural numbers $n$ and $k$, the
Legendre–Stirling number of the first kind $J(n, k; 1)$ is the coefficient of $x^k$ in the
integer polynomial $\prod_{i=0}^{n-1} \bigl(x - i(i+1)\bigr)$, which is $1$ when $n = 0$. These
are the Jacobi–Stirling numbers of the first kind $J(n, k; \zeta)$ at $\zeta = 1$.

Formalized by `MetaMathlibExt.legendreStirlingFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first).

## Initial row of the Legendre–Stirling numbers of the first kind

For every natural number
$k$, the Legendre–Stirling number of the first kind $J(0, k; 1)$ equals $1$ if $k = 0$ and $0$
otherwise.

Formalized by `MetaMathlibExt.legendreStirlingFirst_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first-zero).

## Recurrence for the Legendre–Stirling numbers of the first kind

For all natural numbers
$n$ and $k$, the Legendre–Stirling numbers of the first kind satisfy
$J(n + 1, k + 1; 1) = J(n, k; 1) - n(n + 1) \, J(n, k + 1; 1)$.

Formalized by `MetaMathlibExt.legendreStirlingFirst_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first-succ).

## Legendre–Stirling numbers of the first kind vanish above the diagonal

For all natural
numbers $n < k$, the Legendre–Stirling number of the first kind $J(n, k; 1)$ is $0$.

Formalized by `MetaMathlibExt.legendreStirlingFirst_eq_zero_of_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first-eq-zero-of-lt).

## Diagonal Legendre–Stirling numbers of the first kind

For every natural number $n$, the
Legendre–Stirling number of the first kind $J(n, n; 1)$ equals $1$.

Formalized by `MetaMathlibExt.legendreStirlingFirst_diag`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LegendreStirlingFirstKind.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html#legendre-stirling-first-diag).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobi–Stirling and Legendre–Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/jacobi-stirling-and-legendre-stirling-numbers)
