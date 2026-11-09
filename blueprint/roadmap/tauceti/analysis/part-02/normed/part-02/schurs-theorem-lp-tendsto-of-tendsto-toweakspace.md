---
declaration: theorem
origin: cited
lean: lp.tendsto_of_tendsto_toWeakSpace_one
statement: formalized
proof: formalized
---

# Schur's theorem (`lp.tendsto_of_tendsto_toWeakSpace_one`)

along a countably generated filter, in particular for sequences, weak
convergence in ℓ¹ implies norm convergence.

```lean
lp.tendsto_of_tendsto_toWeakSpace_one.{u_1, u_2, u_3} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  {α : Type u_3} {l : Filter α} [l.IsCountablyGenerated] {x : α → ↥(lp (fun x => 𝕜) 1)}
  {y : ↥(lp (fun x => 𝕜) 1)}
  (hx :
    Filter.Tendsto (fun n => (toWeakSpace 𝕜 ↥(lp (fun x => 𝕜) 1)) (x n)) l
      (nhds ((toWeakSpace 𝕜 ↥(lp (fun x => 𝕜) 1)) y))) :
  Filter.Tendsto x l (nhds y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`lp.tendsto_of_tendsto_toWeakSpace_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Schur.html#lp.tendsto_of_tendsto_toWeakSpace_one).

## Sources

- [Tau Ceti documentation: `lp.tendsto_of_tendsto_toWeakSpace_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Schur.html#lp.tendsto_of_tendsto_toWeakSpace_one)
- [Source of `lp.tendsto_of_tendsto_toWeakSpace_one` in TauCeti/Analysis/Normed/Lp/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Lp/Schur.lean#L164)
