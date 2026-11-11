---
declaration: section
origin: cited
lean: QuadraticForm.forall_quaternary_normForm_eq_zero_iff_forall_ternary_eq_zero, QuaternionAlgebra.nonempty_algEquiv_matrix_of_normForm_eq_zero
statement: formalized
proof: formalized
---

# Splitting of quaternion algebras

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/splitting-of-quaternion-algebras/index.html).

## Anisotropy of the quaternion norm form reduces to a ternary form

The quaternary norm form `x₀² - a·x₁² - b·x₂² + a·b·x₃²` of the
quaternion algebra `ℍ[K, a, b]` is anisotropic if and only if the ternary
form `z² - a·x² - b·y²` is. This equivalence also holds when either parameter
is zero; both forms are then isotropic.

This is the standard reduction of quaternion-algebra isotropy to a ternary
quadratic form. It is used to test whether a quaternion algebra is a
division algebra, in quadratic-form theory (anisotropy of Pfister forms),
and in local-global arguments for quaternion algebras.

Formalized by `QuadraticForm.forall_quaternary_normForm_eq_zero_iff_forall_ternary_eq_zero`, a theorem declared in [MathlibExt/Algebra/QuadraticForm/NormForm.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/QuadraticForm/NormForm.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/splitting-of-quaternion-algebras/index.html#forall-quaternary-norm-form-eq-zero-iff).

## Quaternion algebras with isotropic norm form split

If the norm form of a quaternion algebra over a field of characteristic
not two is isotropic, then the algebra splits: it is isomorphic to the
`2 × 2` matrix algebra.

Formalized by `QuaternionAlgebra.nonempty_algEquiv_matrix_of_normForm_eq_zero`, a theorem declared in [MathlibExt/Algebra/Quaternion/Split.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Quaternion/Split.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/splitting-of-quaternion-algebras/index.html#nonempty-alg-equiv-matrix-of-norm-form-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Splitting of quaternion algebras](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/splitting-of-quaternion-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/associative-algebras/splitting-of-quaternion-algebras)
