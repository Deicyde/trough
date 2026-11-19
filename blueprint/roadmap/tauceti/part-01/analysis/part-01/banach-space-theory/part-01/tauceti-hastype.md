---
declaration: def
origin: cited
lean: TauCeti.HasType
statement: formalized
---

# TauCeti.HasType

`E` has *Rademacher type `p` with constant `C`* if every finite family `y` in `E` satisfies
`R₂(y) ≤ C ‖y‖ₚ`, where `‖y‖ₚ = ‖WithLp.toLp p y‖` is the `ℓᵖ` norm of the family:
`(∑ i, ‖yᵢ‖ ^ p) ^ (1 / p)` for `0 < p < ∞`, the largest `‖yᵢ‖` for `p = ∞`, and the number of
`yᵢ` of nonzero norm for `p = 0`.

```lean
TauCeti.HasType.{u_1} (E : Type u_1) [SeminormedAddCommGroup E] (p : ENNReal) (C : NNReal) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.html#TauCeti.HasType).

## Sources

- [Tau Ceti documentation: `TauCeti.HasType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.html#TauCeti.HasType)
- [Source of `TauCeti.HasType` in TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.lean#L66)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
