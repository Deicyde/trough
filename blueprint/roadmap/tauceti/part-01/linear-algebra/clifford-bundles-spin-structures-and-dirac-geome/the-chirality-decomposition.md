---
declaration: theorem
origin: cited
lean: CliffordAlgebra.isCompl_eigenspace_complexVolume
statement: formalized
proof: formalized
---

# The chirality decomposition

every module over the complexified Clifford algebra is the
direct sum of the `1`- and `-1`-eigenspaces of `Γ`.

```lean
CliffordAlgebra.isCompl_eigenspace_complexVolume.{u_1, u_2} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {n : ℕ} [Fact (Module.finrank ℝ V = n)]
  {Q : QuadraticForm ℝ V} (o : Orientation ℝ V (Fin n)) {E : Type u_2} [AddCommGroup E]
  [_root_.Module ℂ E] [_root_.Module (CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) E]
  [IsScalarTower ℂ (CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) E]
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) :
  IsCompl (((Algebra.lsmul ℂ ℂ E) (CliffordAlgebra.complexVolume Q o)).eigenspace 1)
    (((Algebra.lsmul ℂ ℂ E) (CliffordAlgebra.complexVolume Q o)).eigenspace (-1))
```

## Depends on

- [CliffordAlgebra.complexVolume](cliffordalgebra-complexvolume.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.isCompl_eigenspace_complexVolume`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Eigenspace.html#CliffordAlgebra.isCompl_eigenspace_complexVolume).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.isCompl_eigenspace_complexVolume`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Eigenspace.html#CliffordAlgebra.isCompl_eigenspace_complexVolume)
- [Source of `CliffordAlgebra.isCompl_eigenspace_complexVolume` in TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Eigenspace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Eigenspace.lean#L214)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
