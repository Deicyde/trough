---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ
statement: formalized
proof: formalized
---

# Local `W^{k+1,p}` regularity for `\bar∂`

For `1 < p < ∞` and every `k`, a locally `Lᵖ`
function whose distributional `\bar∂` derivative lies in `W^{k,p}_loc` on an open set lies in
`W^{k+1,p}_loc` there.

```lean
TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ.{u_1} {p : ENNReal} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F] (hp : 1 < p) (hp_top : p ≠ ⊤)
  {Ω : TopologicalSpace.Opens ℂ} {k : ℕ} {u f : ℂ → F} (hu : TauCeti.MemLpLoc p (↑Ω) u)
  (hf : TauCeti.MemWkpLoc p (↑Ω) k f)
  (h : TauCeti.HasWeakConjWirtingerDerivOn MeasureTheory.volume Ω u f) :
  TauCeti.MemWkpLoc p (↑Ω) (k + 1) u
```

## Depends on

- [TauCeti.MemWkpLoc](tauceti-memwkploc.md)

## Proof depends on

- [The Calderón–Zygmund inequality for the Cauchy–Riemann operator](../analytic-heegaard-floer-homology/the-calderon-zygmund-inequality-for-the-cauchy-r.md)
- [Hölder's inequality for disjoint pieces](../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Milman–Pettis theorem](../../part-03/convex/milman-pettis-theorem.md)
- [Norm double-annihilator theorem](../../part-03/normed/part-02/norm-double-annihilator-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Regularity.html#TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Regularity.html#TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ)
- [Source of `TauCeti.HasWeakConjWirtingerDerivOn.memWkpLoc_succ` in TauCeti/Analysis/Complex/Wirtinger/Regularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Wirtinger/Regularity.lean#L195)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
