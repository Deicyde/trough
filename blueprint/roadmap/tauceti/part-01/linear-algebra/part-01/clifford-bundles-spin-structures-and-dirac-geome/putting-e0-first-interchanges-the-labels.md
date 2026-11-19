---
declaration: theorem
origin: cited
lean: TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons
statement: formalized
proof: formalized
---

# Putting `e₀` first interchanges the labels

With the basis and polarization as in
`TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume`, but `V ⊕ ℝ` oriented
by `(e₀, e₁, f₁, …, u)`, the opposite orientation: if `i λ = μ`, then `⋀ W` is isomorphic to the
half-spinor space `S^μ` of every spinor module `S` of `V ⊕ ℝ` through `ψ`, uniquely up to a
scalar. Now the module labelled `ω_ℂ = 1` is the restriction of `S⁺` and the module labelled
`ω_ℂ = -1` is the restriction of `S⁻`.

```lean
TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons.{u_1, u_2}
  {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V]
  {Q : QuadraticForm ℝ V} {Q₁ : QuadraticForm ℝ (WithLp 2 (V × ℝ))}
  (P : TauCeti.SpinPolarizationData (QuadraticForm.baseChange ℂ Q)) {ℓ : ℕ}
  [Fact (Module.finrank ℝ V = 2 * ℓ + 1)]
  [Fact (Module.finrank ℝ (WithLp 2 (V × ℝ)) = 2 * ℓ + 1 + 1)]
  {o : Orientation ℝ V (Fin (2 * ℓ + 1))}
  {o' : Orientation ℝ (WithLp 2 (V × ℝ)) (Fin (2 * ℓ + 1 + 1))} (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2)
  (hQ₁ : ∀ (x : WithLp 2 (V × ℝ)), Q₁ x = (CliffordAlgebra.EquivEven.Q' Q) x.ofLp)
  (b : OrthonormalBasis (Fin (2 * ℓ + 1)) ℝ V) (hb : b.toBasis.orientation = o)
  (hbW : ∀ (k : Fin ℓ), 1 ⊗ₜ[ℝ] b ⟨2 * ↑k, ⋯⟩ - Complex.I ⊗ₜ[ℝ] b ⟨2 * ↑k + 1, ⋯⟩ ∈ P.W)
  (hbW' : ∀ (k : Fin ℓ), 1 ⊗ₜ[ℝ] b ⟨2 * ↑k, ⋯⟩ + Complex.I ⊗ₜ[ℝ] b ⟨2 * ↑k + 1, ⋯⟩ ∈ P.W')
  (hline : 1 ⊗ₜ[ℝ] b (Fin.last (2 * ℓ)) ∈ P.line) {S : Type u_2} [AddCommGroup S]
  [_root_.Module ℂ S] [_root_.Module (CliffordAlgebra (QuadraticForm.baseChange ℂ Q₁)) S]
  [IsScalarTower ℂ (CliffordAlgebra (QuadraticForm.baseChange ℂ Q₁)) S] [FiniteDimensional ℂ S]
  (hS : Function.Bijective ⇑(Algebra.lsmul ℂ ℂ S))
  (ho' :
    ((b.prod (OrthonormalBasis.singleton (Fin 1) ℝ)).reindex
            (((Equiv.sumComm (Fin (2 * ℓ + 1)) (Fin 1)).trans finSumFinEquiv).trans
              (finCongr ⋯))).toBasis.orientation =
      o')
  {μ : ℂ} (hμ : Complex.I * P.lineCoordinate ⟨1 ⊗ₜ[ℝ] b (Fin.last (2 * ℓ)), hline⟩ = μ) :
  ∃ T,
    (∀ (x : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) (s : ExteriorAlgebra ℂ ↥P.W),
        T (((TauCeti.spinAction (QuadraticForm.baseChange ℂ Q) P) x) s) =
          ((CliffordAlgebra.EquivEven.eigenspaceComplexVolumeAction hQ₁ o' μ) x) (T s)) ∧
      ∀
        (U :
          ExteriorAlgebra ℂ ↥P.W →ₗ[ℂ]
            ↥(((Algebra.lsmul ℂ ℂ S) (CliffordAlgebra.complexVolume Q₁ o')).eigenspace μ)),
        (∀ (x : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) (s : ExteriorAlgebra ℂ ↥P.W),
            U (((TauCeti.spinAction (QuadraticForm.baseChange ℂ Q) P) x) s) =
              ((CliffordAlgebra.EquivEven.eigenspaceComplexVolumeAction hQ₁ o' μ) x) (U s)) →
          ∃ c, U = c • ↑T
```

## Depends on

- [CliffordAlgebra.complexVolume](cliffordalgebra-complexvolume.md)

## Proof depends on

- [The chirality decomposition](the-chirality-decomposition.md)
- [The odd structure theorem in operator form](../../../representation-theory/spin/the-odd-structure-theorem-in-operator-form.md)
- [Schur's lemma for a full endomorphism representation](schurs-lemma-for-a-full-endomorphism-representat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/HalfSpinRestriction.html#TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/HalfSpinRestriction.html#TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons)
- [Source of `TauCeti.SpinPolarizationData.exists_linearEquiv_eigenspaceComplexVolume_of_cons` in TauCeti/RepresentationTheory/Spin/Polarization/HalfSpinRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Spin/Polarization/HalfSpinRestriction.lean#L166)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
