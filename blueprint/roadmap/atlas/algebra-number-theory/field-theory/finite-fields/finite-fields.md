---
declaration: section
origin: cited
lean: exists_sq_ne_zero_one_neg_one, Polynomial.aeval_pow_card_eq_pow_card
statement: formalized
proof: formalized
---

# Finite fields: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/index.html).

Finite fields and polynomials over them: irreducible and primitive polynomials, permutation polynomials, and the arithmetic of squares.

## A square avoiding $0$, $1$ and $-1$ in a finite field

If $F$ is a finite field with
more than five elements, then there is an element $r \in F$ with $r^2 \neq 0$, $r^2 \neq 1$
and $r^2 \neq -1$.

Formalized by `exists_sq_ne_zero_one_neg_one`, a theorem declared in [MathlibExt/FieldTheory/Finite/FiniteFieldSquare.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/FiniteFieldSquare.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/index.html#exists-sq-ne-zero-one-neg-one).

## Polynomial evaluation commutes with the Frobenius power

Evaluating `p` at `x ^ q` equals the `q`-th power of evaluating `p` at
`x`, where `q` is the cardinality of the finite field `F`.

Formalized by `Polynomial.aeval_pow_card_eq_pow_card`, a theorem declared in [MathlibExt/Algebra/Polynomial/AevalFrobenius.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/AevalFrobenius.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/index.html#aeval-pow-card-eq-pow-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite fields](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/finite-fields)
