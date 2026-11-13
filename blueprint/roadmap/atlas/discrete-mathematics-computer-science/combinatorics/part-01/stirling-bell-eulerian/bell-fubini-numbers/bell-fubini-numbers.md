---
declaration: section
origin: cited
lean: MetaMathlibExt.partialBellPolynomial, MetaMathlibExt.dobinski_formula_hasSum, MetaMathlibExt.rHorseNumber_eq_stirlingFirst_sum_fubini
statement: formalized
proof: formalized
---

# Bell numbers, Fubini numbers and Bell polynomials: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/index.html).

Bell numbers (Dobinski, Spivey, Touchard and Turán-type identities, log-convexity), complete, partial and generalized Bell polynomials, potential polynomials, Fubini (ordered Bell) numbers and their congruences, and horse numbers.

## Partial Bell polynomial

Let $R$ be a commutative semiring, let $n, k \in \mathbb{N}$
and let $x_1, x_2, \dots$ be a sequence in $R$. The partial Bell polynomial $B_{n,k}(x)$ is
the sum, over all tuples $(m_1, \dots, m_{n+1})$ of natural numbers with
$\sum_j j\, m_j = n$ and $\sum_j m_j = k$, of

$$\frac{n!}{\prod_j m_j!\,(j!)^{m_j}} \prod_j x_j^{m_j},$$

where the quotient is a natural number, mapped into $R$.

## Sources

- Mihoubi, *Some Congruences for the Partial Bell Polynomials*, J. Integer Seq. 12 (2009), Article 09.4.1.

Formalized by `MetaMathlibExt.partialBellPolynomial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartialBellPolynomial.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartialBellPolynomial.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/index.html#partial-bell-polynomial).

## Dobinski's formula

Let $B_n$ denote the $n$-th Bell number, the number of partitions of
an $n$-element set. For every natural number $n$, the real series $\sum_{k=0}^{\infty} k^n / k!$
is summable with sum $e \cdot B_n$, so $B_n = \frac{1}{e} \sum_{k=0}^{\infty} \frac{k^n}{k!}$.
At $n = 0$ the term $k = 0$ is $0^0 / 0! = 1$, matching the exponential series.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Mezo/mezo9.tex>, lines 283-293. Only the classical Bell-number identity is stated here; the r-Bell generalizations are excluded.

Formalized by `MetaMathlibExt.dobinski_formula_hasSum`, a theorem declared in [MathlibExt/Combinatorics/DobinskiBell.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DobinskiBell.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/index.html#dobinski-formula-has-sum).

## Schreyer's Fubini formula for r-horse numbers

Let $r \le n$ be natural numbers. For each
$k$, count the surjections $f : \{0, \dots, n - 1\} \to \{0, \dots, k - 1\}$ whose values on the
first $r$ points are strictly increasing, $f(0) < f(1) < \dots < f(r - 1)$, and let $H$ (the
$r$-horse number) be the sum of these counts over $0 \le k \le n$. Then, as rational numbers,

$$
H = \frac{1}{r!} \sum_{j=0}^{r} (-1)^j \, c(r, r - j) \, F_{n-j},
$$

where $c(r, i)$ is the unsigned Stirling number of the first kind (the number of permutations of
$r$ elements with exactly $i$ cycles) and $F_m$ is the $m$-th Fubini number.

The proof follows Schreyer's: the signed falling-factorial expansion is evaluated at integers and
transported to surjection counts by image decomposition and binomial inversion, rather than by
shift operators.

## Sources

- Benjamin Schreyer, "Rigged Horse Numbers and their Modular Periodicity," Journal of Integer Sequences 28 (2025), Article 25.4.1, Theorem, lines 211–215, https://cs.uwaterloo.ca/journals/JIS/VOL28/Schreyer/schreyer7.tex

Formalized by `MetaMathlibExt.rHorseNumber_eq_stirlingFirst_sum_fubini`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RHorseNumberFubini.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/RHorseNumberFubini.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/index.html#r-horse-number-eq-stirling-first-sum-fub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bell numbers, Fubini numbers and Bell polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers)
