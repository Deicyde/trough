---
declaration: theorem
origin: cited
lean: CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul
statement: formalized
proof: formalized
---

# In even dimension `Γ` acts on complex-valued forms by `i ^ (ℓ + k (k - 1))` times the Hodge star

for `n = 2ℓ`, `ω ∈ ℂ ⊗[ℝ] ⋀ᵏ V` and `k + l = n`, `Γ ω = i ^ (ℓ + k (k - 1)) ⋆ω`.

```lean
CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {n : ℕ}
  [Fact (Module.finrank ℝ V = n)] {Q : QuadraticForm ℝ V} (o : Orientation ℝ V (Fin n))
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) {ℓ : ℕ} (hn : n = 2 * ℓ) {k l : ℕ}
  (hkl : k + l = Module.finrank ℝ V) (x : TensorProduct ℝ ℂ ↥(⋀[ℝ]^k V)) :
  ((CliffordAlgebra.baseChangeExteriorAction ℂ Q) (CliffordAlgebra.complexVolume Q o))
      ((LinearMap.baseChange ℂ (⋀[ℝ]^k V).subtype) x) =
    Complex.I ^ (ℓ + k * (k - 1)) •
      (LinearMap.baseChange ℂ (⋀[ℝ]^l V).subtype) ((o.complexHodgeStar hkl) x)
```

## Depends on

- [CliffordAlgebra.complexVolume](cliffordalgebra-complexvolume.md)
- [Orientation.hodgeStar](../../analysis/part-01/four-dimensional-seiberg-witten-theory/orientation-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/HodgeStar.html#CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/HodgeStar.html#CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul)
- [Source of `CliffordAlgebra.baseChangeExteriorAction_complexVolume_of_eq_two_mul` in TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/HodgeStar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/HodgeStar.lean#L147)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
