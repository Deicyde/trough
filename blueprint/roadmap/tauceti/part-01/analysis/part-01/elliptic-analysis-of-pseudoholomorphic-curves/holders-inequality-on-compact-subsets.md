---
declaration: theorem
origin: cited
lean: TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply
statement: formalized
proof: formalized
---

# Hölder's inequality on compact subsets

a locally `Lᵖ` field of continuous linear maps
applied to a locally `L^q` field is locally integrable on a locally closed set when
`1/p + 1/q ≤ 1`.

```lean
TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply.{u_1, u_2} {F : Type u_1} {G : Type u_2}
  [NormedAddCommGroup F] [NormedAddCommGroup G] {p q : ENNReal} {U : Set ℂ} [NormedSpace ℝ F]
  [NormedSpace ℝ G] {A : ℂ → F →L[ℝ] G} {w : ℂ → F} (hA : TauCeti.MemLpLoc p U A)
  (hw : TauCeti.MemLpLoc q U w) (hpq : p⁻¹ + q⁻¹ ≤ 1) (hU : IsLocallyClosed U) :
  MeasureTheory.LocallyIntegrableOn (fun z => (A z) (w z)) U MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Basic.html#TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Basic.html#TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply)
- [Source of `TauCeti.MemLpLoc.locallyIntegrableOn_clm_apply` in TauCeti/Analysis/Sobolev/Local/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/Basic.lean#L257)
