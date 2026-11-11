---
declaration: section
origin: cited
lean: MetaMathlibExt.sun_refined_eulerian_marginals, MetaMathlibExt.refinedEulerianPolynomial_palindromic
statement: formalized
proof: formalized
---

# Refined Eulerian polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/refined-eulerian-polynomials/index.html).

## Marginals of the refined Eulerian polynomial

Let $n \ge 1$. For a permutation $\sigma$
of $\{1, \dots, n\}$, let $\mathrm{odes}(\sigma)$ (resp. $\mathrm{edes}(\sigma)$) be the number
of odd (resp. even) positions $i \in \{1, \dots, n-1\}$ with $\sigma(i) > \sigma(i+1)$, and let
$A_n(p, q) = \sum_{\sigma} p^{\mathrm{odes}(\sigma)} q^{\mathrm{edes}(\sigma)}$, the sum over all
permutations $\sigma$ of $\{1, \dots, n\}$. Then for all real numbers $p$ and $q$,

$$A_n(p, 1) = \frac{n!}{2^{\lfloor n/2 \rfloor}} (1+p)^{\lfloor n/2 \rfloor}$$

and

$$A_n(1, q) = \frac{n!}{2^{\lfloor (n-1)/2 \rfloor}} (1+q)^{\lfloor (n-1)/2 \rfloor}.$$

## Sources

- Hua Sun, "A New Class of Refined Eulerian Polynomials", Journal of Integer Sequences 21 (2018), Article 18.5.5, Proposition lines 248-254, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Sun/sun2.tex>.

Formalized by `MetaMathlibExt.sun_refined_eulerian_marginals`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RefinedEulerianMarginals.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RefinedEulerianMarginals.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/refined-eulerian-polynomials/index.html#sun-refined-eulerian-marginals).

## Palindromicity of the refined Eulerian polynomials

Let $n \ge 1$. For a permutation
$\sigma$ of $\{1, \dots, n\}$, let $\mathrm{odes}(\sigma)$ (resp. $\mathrm{edes}(\sigma)$) be the
number of odd (resp. even) positions $i \in \{1, \dots, n-1\}$ with $\sigma(i) > \sigma(i+1)$,
and let $A_n(p, q) = \sum_{\sigma} p^{\mathrm{odes}(\sigma)} q^{\mathrm{edes}(\sigma)}$, the sum
over all permutations $\sigma$ of $\{1, \dots, n\}$, be the refined Eulerian polynomial with real
coefficients. Let $P_n = (1+q) A_n$ if $n$ is even and $P_n = A_n$ if $n$ is odd. Then $P_n$ is
palindromic of darga $\lfloor n/2 \rfloor$: it is a nonzero polynomial, $P_n(p, q) = P_n(q, p)$
for all real $p$ and $q$, and $P_n(p, q) = (pq)^{\lfloor n/2 \rfloor} P_n(1/p, 1/q)$ for all
nonzero real $p$ and $q$.

## Sources

- Hua Sun, "A New Class of Refined Eulerian Polynomials," Journal of Integer Sequences 21 (2018), Article 18.5.5, Theorem, lines 160–162 (polynomial definition lines 135–136, palindromic-darga definition lines 105–110). <https://cs.uwaterloo.ca/journals/JIS/VOL21/Sun/sun2.tex>

Formalized by `MetaMathlibExt.refinedEulerianPolynomial_palindromic`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RefinedEulerianPolynomial.lean, line 1531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RefinedEulerianPolynomial.lean#L1531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/refined-eulerian-polynomials/index.html#refined-eulerian-polynomial-palindromic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Refined Eulerian polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/refined-eulerian-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/refined-eulerian-polynomials)
