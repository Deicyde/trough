---
declaration: theorem
origin: cited
lean: IsIntegralCurve.index_trajectoryOperator_hessianOperator
statement: formalized
proof: formalized
---

# The index of the linearized operator is the difference of the Morse indices

Let `f` be a
`C²` function on a finite-dimensional real inner product space and `γ` a negative gradient
trajectory from a nondegenerate critical point `p` at `-∞` to a nondegenerate critical point `q` at
`+∞`. Then the Fredholm index of the linearized operator `ξ ↦ ξ' + Hess f(γ) ξ` from
`W^{1,2}(ℝ, E)` to `L²(ℝ, E)` is `morseIndex f p - morseIndex f q`.

```lean
IsIntegralCurve.index_trajectoryOperator_hessianOperator.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → ℝ} {γ : ℝ → E} {p q : E}
  (hγ : IsIntegralCurve γ fun x x_1 => -gradient f x_1) (hf : ContDiff ℝ 2 f)
  (hp : TauCeti.IsNondegenerateCriticalPoint f p) (hq : TauCeti.IsNondegenerateCriticalPoint f q)
  (hbot : Filter.Tendsto γ Filter.atBot (nhds p)) (htop : Filter.Tendsto γ Filter.atTop (nhds q))
  {AL : ↥(MeasureTheory.Lp (E →L[ℝ] E) ⊤ (MeasureTheory.volume.restrict ↑⊤))}
  (hAL : ↑↑AL =ᵐ[MeasureTheory.volume.restrict ↑⊤] fun s => TauCeti.hessianOperator f (γ s)) :
  (TauCeti.WeakDerivStep.trajectoryOperator AL).index =
    ↑(TauCeti.morseIndex f p) - ↑(TauCeti.morseIndex f q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../../part-03/sobolev/part-01/the-endpoint-local-morrey-estimate.md)
- [The fundamental theorem of calculus for weak derivatives on the line](../../part-03/sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der-2.md)
- [The local Morrey inequality](../../part-03/sobolev/part-01/the-local-morrey-inequality.md)
- [Rellich–Kondrachov on bounded Lipschitz domains](../../part-03/sobolev/part-02/rellich-kondrachov-on-bounded-lipschitz-domains.md)
- [The trajectory operator with hyperbolic limits is Fredholm](the-trajectory-operator-with-hyperbolic-limits-i.md)

## Lean

Formalized in Tau Ceti as [`IsIntegralCurve.index_trajectoryOperator_hessianOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Fredholm.html#IsIntegralCurve.index_trajectoryOperator_hessianOperator).

## Sources

- [Tau Ceti documentation: `IsIntegralCurve.index_trajectoryOperator_hessianOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Fredholm.html#IsIntegralCurve.index_trajectoryOperator_hessianOperator)
- [Source of `IsIntegralCurve.index_trajectoryOperator_hessianOperator` in TauCeti/Analysis/Calculus/Morse/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Fredholm.lean#L278)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
