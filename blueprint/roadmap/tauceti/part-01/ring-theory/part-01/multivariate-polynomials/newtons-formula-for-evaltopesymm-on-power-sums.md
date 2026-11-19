---
declaration: theorem
origin: cited
lean: MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum
statement: formalized
proof: formalized
---

# Newton's formula for `evalTopEsymm` on power sums

for `m > 0`, evaluating the power sum
`pₘ = ∑ᵢ Xᵢ ^ m` at the roots of `Z ^ n - X` (`n = Fintype.card σ`) yields `n * X ^ (m / n)` if
`n ∣ m` and `0` otherwise.

```lean
MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [Fintype σ] [CommRing R] [Nonempty σ] {m : ℕ} (hm : 0 < m) :
  (MvPolynomial.symmetricSubalgebra.evalTopEsymm σ R) ⟨MvPolynomial.psum σ R m, ⋯⟩ =
    if Fintype.card σ ∣ m then ↑(Fintype.card σ) * Polynomial.X ^ (m / Fintype.card σ) else 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Eval.html#MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum).

## Sources

- [Tau Ceti documentation: `MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Eval.html#MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum)
- [Source of `MvPolynomial.symmetricSubalgebra.evalTopEsymm_psum` in TauCeti/RingTheory/MvPolynomial/Symmetric/Eval.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Symmetric/Eval.lean#L207)
