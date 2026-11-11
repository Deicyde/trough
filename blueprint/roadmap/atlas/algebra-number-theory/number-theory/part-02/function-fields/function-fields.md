---
declaration: section
origin: cited
lean: MetaMathlibExt.odd_perfect_polynomial_is_square
statement: formalized
proof: formalized
---

# Arithmetic of function fields: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/index.html).

Number-theoretic analogues over F_q[T] and finite fields: polynomial primes, h-free polynomials, function-field adeles, positive-characteristic zeta values.

## Odd perfect polynomials over $\mathbb{F}_2$ are squares (Canaday)

Let $A$ be a polynomial
over $\mathbb{F}_2$ that is coprime to both $X$ and $X + 1$ (that is, odd: $A$ has no linear
factor) and that equals the sum of its monic divisors (that is, perfect). Then $A$ is a square:
$A = B^2$ for some polynomial $B$ over $\mathbb{F}_2$.

Since every nonzero polynomial over $\mathbb{F}_2$ is monic, the sum over monic divisors is the
full divisor sum.

## Sources

- Luis H. Gallardo and Olivier Rahavandrainy, "A Polynomial Variant of Perfect Numbers," Journal of Integer Sequences 23 (2020), Article 20.8.6, Lemma `oddperfect`, lines 155–158 (odd and perfect defined lines 96–108), https://cs.uwaterloo.ca/journals/JIS/VOL23/Gallardo/gallardo7.tex attributed there to Canaday.

Formalized by `MetaMathlibExt.odd_perfect_polynomial_is_square`, a theorem declared in [MathlibExt/NumberTheory/OddPerfectPolynomial.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OddPerfectPolynomial.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/index.html#odd-perfect-polynomial-is-square).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic of function fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields)
