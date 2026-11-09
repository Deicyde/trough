---
declaration: theorem
origin: cited
lean: TauCeti.EquidecomposableLE.antisymm
statement: formalized
proof: formalized
---

# Schröder–Bernstein theorem for equidecompositions

If each of `A` and `B` is
equidecomposable with a subset of the other, then `A` and `B` are equidecomposable.

```lean
TauCeti.EquidecomposableLE.antisymm.{u_1, u_3} {X : Type u_1} {G : Type u_3} [Group G]
  [MulAction G X] {A B : Set X} (hAB : TauCeti.EquidecomposableLE G A B)
  (hBA : TauCeti.EquidecomposableLE G B A) : TauCeti.Equidecomposable G A B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EquidecomposableLE.antisymm`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equidecomp.html#TauCeti.EquidecomposableLE.antisymm).

## Sources

- [Tau Ceti documentation: `TauCeti.EquidecomposableLE.antisymm`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equidecomp.html#TauCeti.EquidecomposableLE.antisymm)
- [Source of `TauCeti.EquidecomposableLE.antisymm` in TauCeti/Algebra/Group/Action/Equidecomp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Group/Action/Equidecomp.lean#L339)
