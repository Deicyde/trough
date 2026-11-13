---
declaration: section
origin: cited
lean: MetaMathlibExt.stirling_bell_polynomial_connection_pair_general, MetaMathlibExt.stirling_bell_polynomial_connection_pair
statement: formalized
proof: formalized
---

# Laguerre–Stirling–Bell connection pair

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/laguerre-stirling-bell-connection-pair/index.html).

## Laguerre–Stirling–Bell connection pair

Let $\alpha$, $\beta$ and $x$ be real numbers, and
let $n$ and $r$ be natural numbers. Write $\binom{k}{j}$ for the binomial coefficients, $c(n,k)$
for the unsigned Stirling numbers of the first kind, $S(n,k)$ for the Stirling numbers of the
second kind, and $y^{\overline{m}} = y(y+1)\cdots(y+m-1)$ for the rising factorial. For natural
numbers $m$, $s$ and real $y$, let $B_m(y) = \sum_{l=0}^{m} S(m,l)\, y^l$ be the Bell polynomial
and

$$L_{m,s}(y) = \sum_{k=0}^{m} \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j}
(\alpha s + \beta j)^{\overline{m}}\, y^k$$

the generalized Laguerre polynomial. Then

$$L_{n,r}(x) = \sum_{k=0}^{n} \sum_{j=0}^{k} c(n,k) \binom{k}{j} (\alpha r)^{k-j} \beta^j B_j(x)$$

and

$$\sum_{k=0}^{n} (-1)^{n-k} S(n,k)\, L_{k,r}(x) =
\sum_{k=0}^{n} \binom{n}{k} (\alpha r)^{n-k} \beta^k B_k(x).$$

## Sources

- Mark Shattuck, "Combinatorial Properties of a Generalized Class of Laguerre Polynomials," Journal of Integer Sequences 24 (2021), Article 21.2.1, Theorem, equations, lines 330–339, https://cs.uwaterloo.ca/journals/JIS/VOL24/Shattuck/shattuck24.tex

Formalized by `MetaMathlibExt.stirling_bell_polynomial_connection_pair_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingBellPolynomialConnection.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingBellPolynomialConnection.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/laguerre-stirling-bell-connection-pair/index.html#stirling-bell-polynomial-connection-pair).

## Laguerre–Stirling–Bell connection pair, source form

Let $\alpha$, $\beta$ and $x$ be real
numbers with $\beta \neq 0$, and let $n$ and $r$ be natural numbers. Write $\binom{k}{j}$ for the
binomial coefficients, $c(n,k)$ for the unsigned Stirling numbers of the first kind, $S(n,k)$ for
the Stirling numbers of the second kind, and $y^{\overline{m}} = y(y+1)\cdots(y+m-1)$ for the
rising factorial. For natural numbers $m$, $s$ and real $y$, let
$B_m(y) = \sum_{l=0}^{m} S(m,l)\, y^l$ be the Bell polynomial and

$$L_{m,s}(y) = \sum_{k=0}^{m} \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j}
(\alpha s + \beta j)^{\overline{m}}\, y^k$$

the generalized Laguerre polynomial. Then

$$L_{n,r}(x) = \sum_{k=0}^{n} \sum_{j=0}^{k} c(n,k) \binom{k}{j} (\alpha r)^{k-j} \beta^j B_j(x)$$

and

$$\sum_{k=0}^{n} (-1)^{n-k} S(n,k)\, L_{k,r}(x) =
\sum_{k=0}^{n} \binom{n}{k} (\alpha r)^{n-k} \beta^k B_k(x).$$

The hypothesis $\beta \neq 0$ is not used: the same two identities hold for every real $\beta$.

## Sources

- Mark Shattuck, "Combinatorial Properties of a Generalized Class of Laguerre Polynomials," Journal of Integer Sequences 24 (2021), Article 21.2.1, Theorem, equations, lines 330–339, https://cs.uwaterloo.ca/journals/JIS/VOL24/Shattuck/shattuck24.tex

Formalized by `MetaMathlibExt.stirling_bell_polynomial_connection_pair`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingBellPolynomialConnection.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingBellPolynomialConnection.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/laguerre-stirling-bell-connection-pair/index.html#stirling-bell-polynomial-connection-pair-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Laguerre–Stirling–Bell connection pair](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/laguerre-stirling-bell-connection-pair/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/laguerre-stirling-bell-connection-pair)
