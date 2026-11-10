---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span
statement: formalized
proof: formalized
---

# Cohen–Hewitt factorization

Let `A` be a Banach algebra with a left approximate identity
`l` bounded by `C`, acting boundedly on the left of a Banach space `E` through `L`. Every `x` in
the essential part `closure (span (A · E))` factors as `x = L a y` with `‖a‖ ≤ C`, where `y` lies in
the closure of `A · x` and within any prescribed distance `ε` of `x`.

```lean
ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {A : Type u_2} {E : Type u_3} [RCLike 𝕜] [NonUnitalNormedRing A] [NormedSpace 𝕜 A]
  [IsScalarTower 𝕜 A A] [SMulCommClass 𝕜 A A] [CompleteSpace A] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [CompleteSpace E] (L : A →L[𝕜] E →L[𝕜] E)
  (hL : ∀ (a b : A) (z : E), (L (a * b)) z = (L a) ((L b) z)) {l : Filter A} [l.NeBot] {C : ℝ}
  (hC : ∀ᶠ (e : A) in l, ‖e‖ ≤ C) (hl : ∀ (a : A), Filter.Tendsto (fun x => x * a) l (nhds a))
  {x : E} (hx : x ∈ (Submodule.span 𝕜 (Set.range fun p => (L p.1) p.2)).topologicalClosure) {ε : ℝ}
  (hε : 0 < ε) :
  ∃ a y, ‖a‖ ≤ C ∧ y ∈ closure (Set.range fun b => (L b) x) ∧ ‖y - x‖ < ε ∧ (L a) y = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContinuousLinearMap.unitizationAction](continuouslinearmap-unitizationaction.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.html#ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.html#ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span)
- [Source of `ContinuousLinearMap.exists_apply_eq_of_mem_topologicalClosure_span` in TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.lean#L305)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
