---
declaration: theorem
origin: cited
lean: TauCeti.AlmostComplexStructure.fockAction_complexVolume
statement: formalized
proof: formalized
---

# `Γ` is exterior parity on the Fock module

If the orientation of `V` is induced by `J`, in
the sense that some positively oriented orthonormal basis has the form
`(u₁, J u₁, …, u_ℓ, J u_ℓ)`, then the normalized complex volume element `Γ` acts on `⋀ W` by the
grade involution.

```lean
TauCeti.AlmostComplexStructure.fockAction_complexVolume.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] {n : ℕ} [Fact (Module.finrank ℝ V = n)] [FiniteDimensional ℝ V]
  {Q : QuadraticForm ℝ V} {o : Orientation ℝ V (Fin n)} (J : TauCeti.AlmostComplexStructure V)
  (hQJ : ∀ (v : V), Q (J.toLinearMap v) = Q v) (hQnd : QuadraticMap.Nondegenerate)
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (b : OrthonormalBasis (Fin n) ℝ V)
  (hb : b.toBasis.orientation = o)
  (hbJ : ∀ (k : ℕ) (hk : 2 * k + 1 < n), b ⟨2 * k + 1, hk⟩ = J.toLinearMap (b ⟨2 * k, ⋯⟩)) :
  (J.fockAction hQJ hQnd) (CliffordAlgebra.complexVolume Q o) = CliffordAlgebra.involute.toLinearMap
```

## Depends on

- [CliffordAlgebra.complexVolume](cliffordalgebra-complexvolume.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.fockAction_complexVolume`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Chirality.html#TauCeti.AlmostComplexStructure.fockAction_complexVolume).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.fockAction_complexVolume`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Chirality.html#TauCeti.AlmostComplexStructure.fockAction_complexVolume)
- [Source of `TauCeti.AlmostComplexStructure.fockAction_complexVolume` in TauCeti/RepresentationTheory/Spin/Polarization/Chirality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Polarization/Chirality.lean#L141)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
