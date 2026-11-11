---
declaration: section
origin: cited
lean: Cslib.polynomiallyBounded_iff_le_mul_pow_self, Cslib.PolynomiallyBounded.const, Cslib.PolynomiallyBounded.id, Cslib.PolynomiallyBounded.add, Cslib.PolynomiallyBounded.mul, Cslib.PolynomiallyBounded.pow, Cslib.PolynomiallyBounded.comp, Cslib.PolynomiallyBounded.mono_bound
statement: formalized
proof: formalized
---

# Polynomially bounded functions

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html).

## Polynomially Bounded

## Polynomial bounds with equal coefficient and exponent

Polynomial growth is equivalent to a global bound whose coefficient equals its exponent.

Formalized by `Cslib.polynomiallyBounded_iff_le_mul_pow_self`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#polynomially-bounded-iff-le-mul-pow-self).

## Constant functions are polynomially bounded

Every constant natural-valued function is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.const`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#const).

## The identity function is polynomially bounded

The identity function on natural numbers is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.id`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#id).

## Sums of polynomially bounded functions are polynomially bounded

A pointwise sum of polynomially bounded functions is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.add`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#add).

## Products of polynomially bounded functions are polynomially bounded

A pointwise product of polynomially bounded functions is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.mul`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#mul).

## Powers of polynomially bounded functions are polynomially bounded

A fixed pointwise power of a polynomially bounded function is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.pow`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#pow).

## Compositions of polynomially bounded functions are polynomially bounded

A composition of polynomially bounded functions is polynomially bounded.

Formalized by `Cslib.PolynomiallyBounded.comp`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#comp).

## The normalized polynomial bound is polynomially bounded and monotone

The normalized bound is itself polynomially bounded and monotone in its input.

Formalized by `Cslib.PolynomiallyBounded.mono_bound`, a theorem declared in [CSLibExt/Foundations/Data/Nat/PolynomialBound.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/Nat/PolynomialBound.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html#mono-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomially bounded functions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/polynomially-bounded-functions)
