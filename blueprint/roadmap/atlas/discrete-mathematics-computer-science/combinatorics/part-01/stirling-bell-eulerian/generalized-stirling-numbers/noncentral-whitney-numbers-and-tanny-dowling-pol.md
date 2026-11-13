---
declaration: section
origin: cited
lean: MetaMathlibExt.noncentralWhitneySecond, MetaMathlibExt.noncentralTannyDowlingPolynomial
statement: formalized
proof: formalized
---

# Noncentral Whitney numbers and Tanny–Dowling polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/noncentral-whitney-numbers-and-tanny-dowling-pol/index.html).

## Noncentral Whitney numbers of the second kind

For elements $m$ and $a$ of a commutative
ring $R$, the noncentral Whitney numbers of the second kind $W_{m,a}(n, k) \in R$, for natural
numbers $n$ and $k$, are defined by $W_{m,a}(0, 0) = 1$, $W_{m,a}(0, k) = 0$ for $k \ge 1$,
$W_{m,a}(n + 1, 0) = (-a)^{n+1}$, and

$$W_{m,a}(n + 1, k + 1) = W_{m,a}(n, k) + ((k + 1) m - a) \, W_{m,a}(n, k + 1).$$

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL24/Mangontarum/mang13.tex>, recurrence underlying the Tanny-Dowling polynomial in equation (6).

Formalized by `MetaMathlibExt.noncentralWhitneySecond`, a definition declared in [MathlibExt/NumberTheory/NoncentralTannyDowlingPolynomial.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NoncentralTannyDowlingPolynomial.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/noncentral-whitney-numbers-and-tanny-dowling-pol/index.html#noncentral-whitney-second).

## Noncentral Tanny–Dowling polynomials

For elements $m$ and $a$ of a commutative ring $R$
and a natural number $n$, the noncentral Tanny–Dowling polynomial $D_{m,a,n}(x) \in R[x]$ is

$$D_{m,a,n}(x) = \sum_{k=0}^{n} k! \, W_{m,a}(n, k) \, x^k,$$

where $W_{m,a}(n, k)$ are the noncentral Whitney numbers of the second kind.

## Sources

- equation (6), source <https://cs.uwaterloo.ca/journals/JIS/VOL24/Mangontarum/mang13.tex>.

Formalized by `MetaMathlibExt.noncentralTannyDowlingPolynomial`, a definition declared in [MathlibExt/NumberTheory/NoncentralTannyDowlingPolynomial.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NoncentralTannyDowlingPolynomial.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/noncentral-whitney-numbers-and-tanny-dowling-pol/index.html#noncentral-tanny-dowling-polynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Noncentral Whitney numbers and Tanny–Dowling polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/noncentral-whitney-numbers-and-tanny-dowling-pol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/noncentral-whitney-numbers-and-tanny-dowling-pol)
