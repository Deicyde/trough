---
declaration: theorem
origin: cited
lean: CoxeterSystem.geometricRepresentation_injective
statement: formalized
proof: formalized
---

# Tits' theorem

the standard geometric representation of a Coxeter system is faithful.

```lean
CoxeterSystem.geometricRepresentation_injective.{u_1, u_2} {I : Type u_1} {W : Type u_2} [Group W]
  {M : CoxeterMatrix I} (cs : CoxeterSystem M W) : Function.Injective ⇑cs.geometricRepresentation
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CoxeterSystem.geometricRepresentation_injective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Geometric/Sign.html#CoxeterSystem.geometricRepresentation_injective).

## Sources

- [Tau Ceti documentation: `CoxeterSystem.geometricRepresentation_injective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Geometric/Sign.html#CoxeterSystem.geometricRepresentation_injective)
- [Source of `CoxeterSystem.geometricRepresentation_injective` in TauCeti/GroupTheory/Coxeter/Geometric/Sign.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Coxeter/Geometric/Sign.lean#L152)
