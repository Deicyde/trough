---
declaration: theorem
origin: cited
lean: TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae
statement: formalized
proof: formalized
---

# The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)

For units `a` and `b` of a field in which `2` is invertible, the following
are equivalent:
1. `ℍ[K,a,b]` is isomorphic to `M₂(K)`;
2. `b` is a norm from `K[√a] = QuadraticAlgebra K a 0`;
3. `b = x² - a y²` for some `x, y ∈ K`;
4. the ternary form `⟨1, -a, -b⟩` is isotropic;
5. the norm form of `ℍ[K,a,b]`, that is `⟨1, -a, -b, ab⟩`, is isotropic.

```lean
TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae.{u_1} {K : Type u_1} [Field K]
  [Invertible 2] (a b : Kˣ) :
  [Nonempty (QuaternionAlgebra K (↑a) 0 ↑b ≃ₐ[K] Matrix (Fin 2) (Fin 2) K),
      ∃ z, QuadraticAlgebra.norm z = ↑b, ∃ x y, ↑b = x ^ 2 - ↑a * y ^ 2,
      ¬(QuadraticMap.weightedSumSquares K ![1, -↑a, -↑b]).Anisotropic,
      ¬QuadraticMap.Anisotropic (QuaternionAlgebra.normForm (↑a) 0 ↑b)].TFAE
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae`](https://taucetiproject.org/docs/TauCeti/Algebra/Quaternion/SplittingCriterion.html#TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae).

## Sources

- [Tau Ceti documentation: `TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae`](https://taucetiproject.org/docs/TauCeti/Algebra/Quaternion/SplittingCriterion.html#TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae)
- [Source of `TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae` in TauCeti/Algebra/Quaternion/SplittingCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Quaternion/SplittingCriterion.lean#L148)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
