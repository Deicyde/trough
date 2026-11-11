---
declaration: theorem
origin: cited
lean: ZeroAtInftyContinuousMap.hasDunfordPettisProperty
statement: formalized
proof: formalized
---

# The Dunford–Pettis property of `c₀`

On a discrete index type, `C₀(ι, 𝕜)` has the
Dunford–Pettis property.

```lean
ZeroAtInftyContinuousMap.hasDunfordPettisProperty.{u_1, u_2} (𝕜 : Type u_1) (ι : Type u_2)
  [RCLike 𝕜] [TopologicalSpace ι] [DiscreteTopology ι] :
  TauCeti.HasDunfordPettisProperty 𝕜 (ZeroAtInftyContinuousMap ι 𝕜)
```

## Depends on

- [TauCeti.HasDunfordPettisProperty](tauceti-hasdunfordpettisproperty.md)

## Proof depends on

- [Gantmacher's criterion](../../../part-03/normed/part-01/gantmachers-criterion.md)
- [Gantmacher's theorem](../../../part-03/normed/part-01/gantmachers-theorem.md)
- [Schur's theorem (`lp.tendsto_of_tendsto_toWeakSpace_one`)](../../../part-03/normed/part-02/schurs-theorem-lp-tendsto-of-tendsto-toweakspace.md)
- [Šmulian's theorem](../part-02/smulians-theorem.md)

## Lean

Formalized in Tau Ceti as [`ZeroAtInftyContinuousMap.hasDunfordPettisProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/DunfordPettis/Dual.html#ZeroAtInftyContinuousMap.hasDunfordPettisProperty).

## Sources

- [Tau Ceti documentation: `ZeroAtInftyContinuousMap.hasDunfordPettisProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/DunfordPettis/Dual.html#ZeroAtInftyContinuousMap.hasDunfordPettisProperty)
- [Source of `ZeroAtInftyContinuousMap.hasDunfordPettisProperty` in TauCeti/Analysis/Normed/Operator/DunfordPettis/Dual.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/DunfordPettis/Dual.lean#L95)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
