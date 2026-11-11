---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale
statement: formalized
proof: formalized
---

# Bubbles are holomorphic for the frozen structure

Let `u i` solve the Floer equation
`(du - X_K)^{0,1} = 0` for a domain-dependent structure `J(z, x)` at the points `c i + ε i • w`,
where the centres `c i` tend to `z₀` and the scales `ε i` tend to `0`. If the rescaled maps
`w' ↦ u i (c i + ε i • w')` converge at `w` to `x₀` and their derivatives at `w` converge to `L`,
and if `J` and the Hamiltonian vector fields of `K` are continuous at `(z₀, x₀)`, then `L` is
complex linear for the structure `J(z₀, x₀)` frozen at the bubbling point `z₀`.

```lean
TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {Ks Kt : ℝ × ℝ → V → ℝ}
  {ι : Type u_2} {l : Filter ι} {u : ι → ℝ × ℝ → V} {c : ι → ℝ × ℝ} {ε : ι → ℝ} {z₀ : ℝ × ℝ}
  (ω : TauCeti.SymplecticForm V) [l.NeBot] {J : ℝ × ℝ → V → TauCeti.AlmostComplexStructure V}
  {w : ℝ × ℝ} {x₀ : V} {L : ℝ × ℝ →L[ℝ] V} (hc : Filter.Tendsto c l (nhds z₀))
  (hε : Filter.Tendsto ε l (nhds 0))
  (hx : Filter.Tendsto (fun i => u i (c i + ε i • w)) l (nhds x₀))
  (hL : Filter.Tendsto (fun i => fderiv ℝ (fun w' => u i (c i + ε i • w')) w) l (nhds L))
  (hJ : ContinuousAt (fun p => LinearMap.toContinuousLinearMap (J p.1 p.2).toLinearMap) (z₀, x₀))
  (hXs : ContinuousAt (Function.uncurry fun z => ω.hamiltonianVectorField (Ks z)) (z₀, x₀))
  (hXt : ContinuousAt (Function.uncurry fun z => ω.hamiltonianVectorField (Kt z)) (z₀, x₀))
  (hsol :
    ∀ᶠ (i : ι) in l,
      TauCeti.IsComplexLinearMap (TauCeti.AlmostComplexStructure.product ℝ)
        (J (c i + ε i • w) (u i (c i + ε i • w)))
        ↑(ω.perturbedFDeriv Ks Kt (u i) (c i + ε i • w))) :
  TauCeti.IsComplexLinearMap (TauCeti.AlmostComplexStructure.product ℝ) (J z₀ x₀) ↑L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Rescaling/Basic.html#TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Rescaling/Basic.html#TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale)
- [Source of `TauCeti.SymplecticForm.isComplexLinearMap_of_tendsto_rescale` in TauCeti/Geometry/Symplectic/Floer/Rescaling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/Rescaling/Basic.lean#L216)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
