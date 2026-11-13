---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Stockmeyer.stockmeyer_approximate_counting, MetaMathlibExt.Complexity.KeyTheorems.Toda.toda
statement: formalized
---

# Counting complexity: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/index.html).

\#P and PP: #P-completeness (counting SAT, permanent), PP-completeness, Toda's theorem, threshold languages, and approximate counting algorithms and schemes (Stockmeyer, Karp–Luby, Jerrum–Sinclair–Vigoda).

## Stockmeyer: approximate counting of #P functions in BPP^NP

For every function $f$ in
$\#P$ there are a decision problem $O$ in NP, polynomials $p_r$, $p$ and $q$ with
natural-number coefficients, and polynomial-time computable functions $\mathrm{nextQ}$ and
$\mathrm{final}$, each taking a bitstring and a list of query/answer pairs (bitstring, boolean),
with $\mathrm{nextQ}$ returning a bitstring and $\mathrm{final}$ returning a natural number,
such that the following holds. Let $x$ and $w$ be bitstrings with $n = |w| \ge 1$, where $|\cdot|$
denotes length, and put $m = |x| + n$. For a bitstring $r$ of length $p_r(m)$, let $E(r)$ be the
output of the oracle computation that chooses queries with $\mathrm{nextQ}$ and decides with
$\mathrm{final}$, run with oracle $O$, query-length cap $q(m)$ and $p(m)$ adaptive queries on
the bitstring encoding of the pair $(x, (r, w))$ from the empty history. Then
$f(x)/(1 + 1/n) \le E(r) \le f(x) \cdot (1 + 1/n)$, computed in the rationals, for at least two
thirds of the $2^{p_r(m)}$ bitstrings $r$ of length $p_r(m)$.

The bitstring $w$ gives the precision $n$ in unary; the number of random bits, the number of
queries and the query-length cap are all polynomial in $|x| + n$.

## Sources

- L. J. Stockmeyer, "The complexity of approximate counting", Proceedings of the Fifteenth Annual ACM Symposium on Theory of Computing (STOC 1983), 118-126 (journal version in Information and Computation 1985).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Stockmeyer.stockmeyer_approximate_counting` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/StockmeyerWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/StockmeyerWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/index.html#stockmeyer-approximate-counting).

## Toda's theorem: PH is contained in $\mathsf{P}^{\#\mathsf{P}}$

Every decision problem in
the polynomial hierarchy PH lies in $\mathsf{P}^{\#\mathsf{P}}$, the class of decision problems
decidable in polynomial time with a $\#\mathsf{P}$ oracle.

## Sources

- S. Toda, "PP is as hard as the polynomial-time hierarchy", SIAM Journal on Computing 20 (1991), 865-877 (FOCS 1989).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Toda.toda` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/TodaWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/TodaWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/index.html#toda).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting complexity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/counting-complexity)
