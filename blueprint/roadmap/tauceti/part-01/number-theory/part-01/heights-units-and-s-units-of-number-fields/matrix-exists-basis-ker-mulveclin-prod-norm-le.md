---
declaration: theorem
origin: cited
lean: Matrix.exists_basis_ker_mulVecLin_prod_norm_le
statement: formalized
proof: formalized
---

# Matrix.exists_basis_ker_mulVecLin_prod_norm_le

An integer matrix with independent rows has a basis of its entire integral kernel whose
product of sup norms is at most `k! / 2 ^ (k - 1) * √det (A Aᵀ) / minorGcd A`, where `k` is
the number of columns minus the number of rows. The conclusion also includes `k = 0`.

```lean
Matrix.exists_basis_ker_mulVecLin_prod_norm_le.{u_1} {ι : Type u_1} [Fintype ι] {p : ℕ}
  {A : Matrix (Fin p) ι ℤ} (hA : LinearIndependent ℚ (A.map Int.cast).row) :
  ∃ b,
    ∏ l, ‖↑(b l)‖ ≤
      ↑(Fintype.card ι - p).factorial / 2 ^ (Fintype.card ι - p - 1) * √↑(A * A.transpose).det /
        ↑A.minorGcd
```

## Depends on

- [Matrix.minorGcd](matrix-minorgcd.md)

## Proof depends on

- [A basis of the integral points of small sup norm](a-basis-of-the-integral-points-of-small-sup-norm.md)
- [The height of the kernel of an integer matrix](the-height-of-the-kernel-of-an-integer-matrix.md)
- [Pseudo-bases over a Dedekind domain](../../part-02/roths-theorem-and-the-subspace-theorem-over-numb/pseudo-bases-over-a-dedekind-domain.md)
- [Schmidt's covolume identity](../diophantine-approximation-and-transcendence/schmidts-covolume-identity.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_basis_ker_mulVecLin_prod_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Matrix.exists_basis_ker_mulVecLin_prod_norm_le).

## Sources

- [Tau Ceti documentation: `Matrix.exists_basis_ker_mulVecLin_prod_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Matrix.exists_basis_ker_mulVecLin_prod_norm_le)
- [Source of `Matrix.exists_basis_ker_mulVecLin_prod_norm_le` in TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean#L180)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HeightsAndUnits/STATUS.md)
