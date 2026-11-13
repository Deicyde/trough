---
declaration: section
origin: cited
lean: MetaMathlibExt.howard_potentialPolynomial_rTwo_eq_partialBell, MetaMathlibExt.howard_potentialPolynomial_eq_partialBell
statement: formalized
proof: formalized
---

# Potential polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/potential-polynomials/index.html).

## Howard's formula for the series $\sum_{k \ge 0} 2x^k/(k+2)!$

Let $n$ be a natural
number, let

$$h(x) = \sum_{k \ge 0} \frac{2}{(k+2)!}\, x^k \in \mathbb{Q}[[x]],$$

let $h^{-1}$ be its inverse in $\mathbb{Q}[[x]]$, and write $[x^n]\, f$ for the coefficient of
$x^n$ in a power series $f$. Let $G_n \in \mathbb{Q}[X]$ be a polynomial of degree at most $n$
such that $G_n(m) = n!\, [x^n]\, (h^{-1})^m$ for every natural number $m \le n$. Then

$$G_n(X) = \sum_{i=0}^{n} (-1)^i\, 2^i\, \frac{n!\, i!}{(n+2i)!} \cdot
\frac{X(X+1)\cdots(X+i-1)}{i!} \cdot \frac{(X+n)(X+n-1)\cdots(X+i+1)}{(n-i)!} \cdot
B_{n+2i,\,i}(0, 1, 1, \dots),$$

where empty products equal $1$ and $B_{n+2i,\,i}(0, 1, 1, \dots)$ is the partial Bell
polynomial evaluated at the sequence whose first term is $0$ and whose other terms are all $1$.

## Sources

- G. Nemes, Journal of Integer Sequences 13 (2010), https://cs.uwaterloo.ca/journals/JIS/VOL13/Nemes/nemes2.tex, lines 120-133 (generic) and 166-173 (specialization).

Formalized by `MetaMathlibExt.howard_potentialPolynomial_rTwo_eq_partialBell`, a theorem declared in [MathlibExt/Combinatorics/HowardPotentialPolynomial.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/HowardPotentialPolynomial.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/potential-polynomials/index.html#howard-potential-polynomial-r-two-eq-par).

## Howard's formula for potential polynomials

Let $K$ be a field of characteristic zero,
let $r \ge 1$ and $n$ be natural numbers, and let $a_0, a_1, a_2, \dots$ be a sequence in $K$
with $a_r \ne 0$. Let $g$ be the formal power series

$$g(x) = \sum_{k \ge 0} \frac{r!\, a_{r+k}}{a_r\, (r+k)!}\, x^k,$$

let $g^{-1}$ be its inverse in $K[[x]]$, and write $[x^n]\, f$ for the coefficient of $x^n$ in a
power series $f$. Let $P \in K[X]$ be a polynomial of degree at most $n$ such that
$P(m) = n!\, [x^n]\, (g^{-1})^m$ for every natural number $m \le n$. Then

$$P(X) = \sum_{i=0}^{n} (-1)^i \left(\frac{r!}{a_r}\right)^i \frac{n!\, i!}{(n+ri)!} \cdot
\frac{X(X+1)\cdots(X+i-1)}{i!} \cdot \frac{(X+n)(X+n-1)\cdots(X+i+1)}{(n-i)!} \cdot
B_{n+ri,\,i}(\tilde a),$$

where empty products equal $1$, $B_{n+ri,\,i}$ is the partial Bell polynomial, and $\tilde a$
is the sequence with $\tilde a_j = a_j$ for $j \ge r$ and $\tilde a_j = 0$ for $j < r$.

## Sources

- G. Nemes, Journal of Integer Sequences 13 (2010), https://cs.uwaterloo.ca/journals/JIS/VOL13/Nemes/nemes2.tex, lines 120-133 (generic) and 166-173 (specialization).

Formalized by `MetaMathlibExt.howard_potentialPolynomial_eq_partialBell`, a theorem declared in [MathlibExt/Combinatorics/HowardPotentialPolynomial.lean, line 1893](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/HowardPotentialPolynomial.lean#L1893). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/potential-polynomials/index.html#howard-potential-polynomial-eq-partial-b).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Potential polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/potential-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/potential-polynomials)
