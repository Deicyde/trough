---
declaration: theorem
origin: cited
lean: Matrix.sign_det_one_sub_pow
statement: formalized
proof: formalized
---

# The sign of an iterate

If `1 - A ^ k` is invertible for a real square matrix `A`, then
`sgn det (1 - A ^ k) = (-1) ^ i₊ * (-1) ^ ((k + 1) i₋)`, where `i₊` and `i₋` count the real
characteristic roots of `A` in `(1, ∞)` and in `(-∞, -1)`, with algebraic multiplicity.

```lean
Matrix.sign_det_one_sub_pow.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n] (A : Matrix n n ℝ)
  (k : ℕ) (h : (1 - A ^ k).det ≠ 0) :
  SignType.sign (1 - A ^ k).det =
    (-1) ^ (Multiset.filter (fun x => 1 < x) A.charpoly.roots).card *
      (-1) ^ ((k + 1) * (Multiset.filter (fun x => x < -1) A.charpoly.roots).card)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.sign_det_one_sub_pow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/DetSign.html#Matrix.sign_det_one_sub_pow).

## Sources

- [Tau Ceti documentation: `Matrix.sign_det_one_sub_pow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/DetSign.html#Matrix.sign_det_one_sub_pow)
- [Source of `Matrix.sign_det_one_sub_pow` in TauCeti/LinearAlgebra/Matrix/Charpoly/DetSign.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Charpoly/DetSign.lean#L104)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
