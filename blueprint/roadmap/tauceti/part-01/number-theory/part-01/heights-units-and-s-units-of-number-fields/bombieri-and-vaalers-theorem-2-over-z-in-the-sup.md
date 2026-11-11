---
declaration: theorem
origin: cited
lean: Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le
statement: formalized
proof: formalized
---

# Bombieri and Vaaler's Theorem 2 over `ℤ`, in the sup norm

Let `A` be a `p × n` integer
matrix with linearly independent rows, and let `g` be the greatest common divisor of its maximal
minors. Then `A x = 0` has `n - p` linearly independent integral solutions `x l`, each with
coprime coordinates, whose sup norms `‖x l‖ = max_i |x l i|` satisfy
`∏ l, ‖x l‖ ≤ √det (A Aᵀ) / g`.

```lean
Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le.{u_1} {ι : Type u_1} [Fintype ι] {p : ℕ}
  {A : Matrix (Fin p) ι ℤ} (hA : LinearIndependent ℚ (A.map Int.cast).row) :
  ∃ x,
    LinearIndependent ℤ x ∧
      (∀ (l : Fin (Fintype.card ι - p)), A.mulVec (x l) = 0) ∧
        (∀ (l : Fin (Fintype.card ι - p)), Finset.univ.gcd (x l) = 1) ∧
          ∏ l, ‖x l‖ ≤ √↑(A * A.transpose).det / ↑A.minorGcd
```

## Depends on

- [Matrix.minorGcd](matrix-minorgcd.md)

## Proof depends on

- [The Cauchy–Binet formula](../../../linear-algebra/other-results/the-cauchy-binet-formula.md)
- [The height of the kernel of an integer matrix](the-height-of-the-kernel-of-an-integer-matrix.md)
- [Minkowski's second theorem, upper bound, in terms of the successive minima](minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [Vaaler's cube-slicing theorem](../../../measure-theory/measure/vaalers-cube-slicing-theorem.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le).

## Sources

- [Tau Ceti documentation: `Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le)
- [Source of `Matrix.exists_linearIndependent_mulVec_eq_zero_prod_norm_le` in TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean#L156)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HeightsAndUnits/STATUS.md)
