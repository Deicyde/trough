---
declaration: theorem
origin: cited
lean: TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator
statement: formalized
proof: formalized
---

# Morse–Smale means every linearized operator is onto

For a `C²` function with globally
Lipschitz gradient, the negative gradient flow is Morse–Smale exactly when, along every negative
gradient trajectory `γ` between nondegenerate critical points, the linearized operator
`ξ ↦ ξ' + Hess f(γ) ξ` from `W^{1,2}(ℝ, E)` to `L²(ℝ, E)` is onto.

```lean
TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → ℝ} {K : NNReal}
  (hfs : ContDiff ℝ 2 f) (hf : LipschitzWith K (gradient f)) :
  TauCeti.IsMorseSmale f hf ↔
    ∀ ⦃p q : E⦄ ⦃γ : ℝ → E⦄,
      TauCeti.IsNondegenerateCriticalPoint f p →
        TauCeti.IsNondegenerateCriticalPoint f q →
          (IsIntegralCurve γ fun x x_1 => -gradient f x_1) →
            Filter.Tendsto γ Filter.atBot (nhds p) →
              Filter.Tendsto γ Filter.atTop (nhds q) →
                ∀ (AL : ↥(MeasureTheory.Lp (E →L[ℝ] E) ⊤ (MeasureTheory.volume.restrict ↑⊤))),
                  (↑↑AL =ᵐ[MeasureTheory.volume.restrict ↑⊤] fun s =>
                      TauCeti.hessianOperator f (γ s)) →
                    Function.Surjective ⇑(TauCeti.WeakDerivStep.trajectoryOperator AL)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../../part-04/sobolev/part-01/the-endpoint-local-morrey-estimate.md)
- [The fundamental theorem of calculus for weak derivatives on the line](../../part-04/sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der-2.md)
- [The local Morrey inequality](../../part-04/sobolev/part-01/the-local-morrey-inequality.md)
- [The Lyapunov inequality near the end](../../part-04/ode/the-lyapunov-inequality-near-the-end.md)
- [Peetre's lemma](../../part-03/normed/part-02/peetres-lemma.md)
- [Rellich–Kondrachov on a disc](../../part-04/sobolev/part-02/rellich-kondrachov-on-a-disc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/MorseSmale/Fredholm.html#TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/MorseSmale/Fredholm.html#TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator)
- [Source of `TauCeti.isMorseSmale_iff_forall_surjective_trajectoryOperator` in TauCeti/Analysis/Calculus/Morse/MorseSmale/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Morse/MorseSmale/Fredholm.lean#L52)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HeegaardFloer/STATUS.md)
