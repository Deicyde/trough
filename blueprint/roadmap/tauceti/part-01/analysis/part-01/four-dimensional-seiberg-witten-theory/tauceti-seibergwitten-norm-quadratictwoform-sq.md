---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.norm_quadraticTwoForm_sq
statement: formalized
proof: formalized
---

# TauCeti.SeibergWitten.norm_quadraticTwoForm_sq

`‖q(ψ)‖² = ‖ψ‖⁴ / 8`.

```lean
TauCeti.SeibergWitten.norm_quadraticTwoForm_sq.{u_1, u_2} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [Fact (Module.finrank ℝ V = 4)] {Q : QuadraticForm ℝ V}
  (o : Orientation ℝ V (Fin 4)) {W : Type u_2} [NormedAddCommGroup W] [InnerProductSpace ℂ W]
  [FiniteDimensional ℂ W] {ρ : CliffordAlgebra Q →ₐ[ℝ] Module.End ℂ W}
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (hkl : 2 + 2 = Module.finrank ℝ V)
  (hρ : ∀ (v : V), LinearMap.adjoint (ρ ((CliffordAlgebra.ι Q) v)) = -ρ ((CliffordAlgebra.ι Q) v))
  (h₂ : Module.finrank ℂ ↥(CliffordAlgebra.positiveHalfSpinors o ρ) = 2)
  (ψ : ↥(CliffordAlgebra.positiveHalfSpinors o ρ)) :
  ‖TauCeti.SeibergWitten.quadraticTwoForm o ρ hkl ψ‖ ^ 2 = ‖ψ‖ ^ 4 / 8
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_quadraticTwoForm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/QuadraticTwoForm.html#TauCeti.SeibergWitten.norm_quadraticTwoForm_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.norm_quadraticTwoForm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/QuadraticTwoForm.html#TauCeti.SeibergWitten.norm_quadraticTwoForm_sq)
- [Source of `TauCeti.SeibergWitten.norm_quadraticTwoForm_sq` in TauCeti/Analysis/PDE/SeibergWitten/QuadraticTwoForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/QuadraticTwoForm.lean#L185)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
