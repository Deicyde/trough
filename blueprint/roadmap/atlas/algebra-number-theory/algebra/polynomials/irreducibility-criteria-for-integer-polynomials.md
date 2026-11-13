---
declaration: section
origin: cited
lean: MetaMathlibExt.cohn_criterion, MetaMathlibExt.irreducible_of_dumas_padic_criterion
statement: formalized
proof: formalized
---

# Irreducibility criteria for integer polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/irreducibility-criteria-for-integer-polynomials/index.html).

## Cohn's irreducibility criterion

Let $b \ge 2$ be an integer and let $p$ be a prime whose
base-$b$ digits are $a_0, a_1, \dots, a_n$, with units digit $a_0$ and leading digit $a_n \ne 0$.
Then the polynomial $f(x) = a_0 + a_1 x + \dots + a_n x^n$ is irreducible in $\mathbb{Z}[x]$.

## Sources

- https://en.wikipedia.org/wiki/Cohn%27s_irreducibility_criterion

Formalized by `MetaMathlibExt.cohn_criterion`, a theorem declared in [MathlibExt/NumberTheory/Digits/Cohn.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/Cohn.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/irreducibility-criteria-for-integer-polynomials/index.html#cohn-criterion).

## Dumas irreducibility criterion

Let $p$ be a prime, write $v_p$ for the $p$-adic
valuation on $\mathbb{Q}$, and let $f = a_0 + a_1 x + \dots + a_n x^n \in \mathbb{Z}[x]$ have
degree $n \ge 1$, with $a_0 \ne 0$ and $a_n \ne 0$. Suppose that no integer $k > 1$ dividing $n$
divides $v_p(a_0) - v_p(a_n)$, that is, $\gcd(v_p(a_0) - v_p(a_n), n) = 1$, and that for every
$0 \le i \le n$ with $a_i \ne 0$,
$n \, v_p(a_i) \ge (n - i) \, v_p(a_0) + i \, v_p(a_n)$.
Then $f$ is irreducible as a polynomial in $\mathbb{Q}[x]$.

Geometrically, the hypotheses say that the Newton polygon of $f$ with respect to $p$ is the single
segment from $(0, v_p(a_0))$ to $(n, v_p(a_n))$ and has no lattice points other than its
endpoints. Zero coefficients contribute no points to the Newton polygon, so the inequality is
required only for nonzero $a_i$.

## Sources

- Randell Heyman, *On the Number of Polynomials of Bounded Height that Satisfy the Dumas Criterion*, Journal of Integer Sequences 17 (2014), Article 14.2.4, Dumas criterion statement, lines 96–102, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Heyman/heyman2.tex>. Exact algebraic form: Martin Juras, arXiv:1505.07633v1, lines 67–100.

Formalized by `MetaMathlibExt.irreducible_of_dumas_padic_criterion`, a theorem declared in [MathlibExt/NumberTheory/Polynomial/DumasIrreducibilityCriterion.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Polynomial/DumasIrreducibilityCriterion.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/irreducibility-criteria-for-integer-polynomials/index.html#irreducible-of-dumas-padic-criterion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Irreducibility criteria for integer polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/irreducibility-criteria-for-integer-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/irreducibility-criteria-for-integer-polynomials)
