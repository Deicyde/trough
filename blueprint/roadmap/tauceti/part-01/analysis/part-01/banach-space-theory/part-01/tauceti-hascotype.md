---
declaration: def
origin: cited
lean: TauCeti.HasCotype
statement: formalized
---

# TauCeti.HasCotype

`E` has *Rademacher cotype `q` with constant `C`* if every finite family `y` in `E` satisfies
`‖y‖_q ≤ C R₂(y)`, where `‖y‖_q = ‖WithLp.toLp q y‖` is the `ℓ^q` norm of the family:
`(∑ i, ‖yᵢ‖ ^ q) ^ (1 / q)` for `0 < q < ∞`, the largest `‖yᵢ‖` for `q = ∞`, and the number of
`yᵢ` of nonzero norm for `q = 0`.

```lean
TauCeti.HasCotype.{u_1} (E : Type u_1) [SeminormedAddCommGroup E] (q : ENNReal) (C : NNReal) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasCotype`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.html#TauCeti.HasCotype).

## Sources

- [Tau Ceti documentation: `TauCeti.HasCotype`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.html#TauCeti.HasCotype)
- [Source of `TauCeti.HasCotype` in TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/TypeCotype.lean#L74)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
