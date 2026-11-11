---
declaration: section
origin: cited
lean: MetaMathlibExt.centralTrinomialCoeff_three_term_recurrence, MetaMathlibExt.centralTrinomialCoeff_eq_legendre_specialValue
statement: formalized
proof: formalized
---

# Central trinomial coefficients

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/central-trinomial-coefficients/index.html).

## Three-term recurrence for central trinomial coefficients

For a natural number $m$, let
$T_m$ be the central trinomial coefficient, the coefficient of $x^m$ in $(1 + x + x^2)^m$.
For every natural number $n$ the following holds, where for $n = 0$ the index $n - 1$ is read
as $0$ (the last term then vanishes, since $3n = 0$):

$$(n + 1)\,T_{n+1} = (2n + 1)\,T_n + 3n\,T_{n-1}.$$

## Sources

- P. Blasiak, G. Dattoli, A. Horzela, K. A. Penson, and K. Zhukovsky, "Motzkin Numbers, Central Trinomial Coefficients and Hybrid Polynomials," Journal of Integer Sequences 11 (2008), Article 08.1.1, Corollary containing Equation (24), lines 364–369, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Penson/penson131.tex>.

Formalized by `MetaMathlibExt.centralTrinomialCoeff_three_term_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CentralTrinomialRecurrence.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/CentralTrinomialRecurrence.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/central-trinomial-coefficients/index.html#central-trinomial-coeff-three-term-recur).

## Central trinomial coefficients as Legendre values

For a natural number $n$, let $c_n$ be the
central trinomial coefficient, the coefficient of $X^n$ in $(1 + X + X^2)^n$, and let $P_n$ be the
$n$th Legendre polynomial. Then, in the complex numbers,

$$
c_n = i^n \sqrt{3^n}\, P_n\Bigl(-\frac{i}{\sqrt{3}}\Bigr).
$$

Here $P_n(-i/\sqrt{3})$ is computed through the shifted Legendre polynomial
$\tilde{P}_n(y) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{n+k}{n} y^k$, which satisfies
$\tilde{P}_n(y) = P_n(1 - 2y)$, evaluated at $y = (1 + i/\sqrt{3})/2$.

Proof: Bonnet's recurrence $(n+1) P_{n+1}(x) = (2n+1) x P_n(x) - n P_{n-1}(x)$, evaluated at
$x = -i/\sqrt{3}$ and rescaled by $i^n \sqrt{3^n}$, becomes the central trinomial recurrence
$(n+1) c_{n+1} = (2n+1) c_n + 3n c_{n-1}$ (OEIS A002426); both sides agree at $n = 0, 1$.

## Sources

- P. Blasiak, G. Dattoli, A. Horzela, K. A. Penson, and K. Zhukovsky, "Motzkin Numbers, Central Trinomial Coefficients and Hybrid Polynomials," Journal of Integer Sequences 11 (2008), Article 08.1.1, Proposition with equation `eq20`, lines 337-343, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Penson/penson131.tex>.

Formalized by `MetaMathlibExt.centralTrinomialCoeff_eq_legendre_specialValue`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CentralTrinomialLegendre.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/CentralTrinomialLegendre.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/central-trinomial-coefficients/index.html#central-trinomial-coeff-eq-legendre-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central trinomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/central-trinomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/central-trinomial-coefficients)
