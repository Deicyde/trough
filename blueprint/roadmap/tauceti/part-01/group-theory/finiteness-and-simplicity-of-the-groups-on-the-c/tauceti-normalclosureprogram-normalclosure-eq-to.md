---
declaration: theorem
origin: cited
lean: TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check
statement: formalized
proof: formalized
---

# TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check

A checked program recovering a generating family proves normal generation of the group.

```lean
TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check.{u_1, u_2} {α : Type u_1} {G : Type u_2}
  [Group G] {n : ℕ} [Fintype α] [DecidableEq G] (p : TauCeti.NormalClosureProgram α n) (f : α → G)
  (x : G) (output : α → Fin n) (hgen : Subgroup.closure (Set.range f) = ⊤)
  (h : p.check f x output = true) : Subgroup.normalClosure {x} = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/NormalGeneration.html#TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check).

## Sources

- [Tau Ceti documentation: `TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/NormalGeneration.html#TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check)
- [Source of `TauCeti.NormalClosureProgram.normalClosure_eq_top_of_check` in TauCeti/GroupTheory/Presentation/NormalGeneration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Presentation/NormalGeneration.lean#L224)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
