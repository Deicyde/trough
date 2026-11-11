---
declaration: theorem
origin: cited
lean: CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar
statement: formalized
proof: formalized
---

# Spinor modules carry compatible positive Hermitian metrics

For a Euclidean space with
`Q v = -‖v‖²` and an algebra isomorphism `ρ` from the complexified Clifford algebra onto the
endomorphisms of `S`, there is a positive definite Hermitian form `H` on `S` with
`H (ρ a x) y = H x (ρ (conjStar Q a) y)` for every `a`.

The form is unique up to a positive real scalar
(`CliffordAlgebra.existsUnique_pos_mul_of_surjective`). No parity hypothesis is needed: `ρ` forces
`V` to have even dimension (`CliffordAlgebra.even_finrank_of_algEquiv_end`). Dimension zero, where
`S` is a line, is included.

```lean
CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar.{u_1, u_2} {V : Type u_1} {S : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {Q : QuadraticForm ℝ V}
  [AddCommGroup S] [_root_.Module ℂ S] (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2)
  (ρ : CliffordAlgebra (QuadraticForm.baseChange ℂ Q) ≃ₐ[ℂ] Module.End ℂ S) :
  ∃ H,
    H.IsPosSemidef ∧
      (∀ (x : S), x ≠ 0 → (H x) x ≠ 0) ∧
        ∀ (a : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) (x y : S),
          (H ((ρ a) x)) y = (H x) ((ρ ((CliffordAlgebra.conjStar Q) a)) y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Spinor.html#CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Spinor.html#CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar)
- [Source of `CliffordAlgebra.exists_sesqForm_map_eq_map_conjStar` in TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Spinor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Hermitian/Spinor.lean#L69)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
