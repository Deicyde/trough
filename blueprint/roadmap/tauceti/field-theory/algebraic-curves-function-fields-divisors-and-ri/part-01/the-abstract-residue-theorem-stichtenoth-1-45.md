---
declaration: theorem
origin: cited
lean: TauCeti.finsum_repartitionDualComponent_eq_zero
statement: formalized
proof: formalized
---

# The abstract residue theorem (Stichtenoth, (1.45))

the local components of a Weil
differential sum to zero on every function of `F`.

The constant repartition of `x` lies in the diagonal copy of `F` inside `A_F`, on which every Weil
differential vanishes, and its entry at every place is `x`.  Stichtenoth states the case `x = 1`;
no hypothesis on the constant field `k` is needed, and no residue map has been constructed.

```lean
TauCeti.finsum_repartitionDualComponent_eq_zero.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)} (hω : ω ∈ TauCeti.weilDifferentialSpace k F)
  (x : F) : ∑ᶠ (P : TauCeti.Place k F), (TauCeti.repartitionDualComponent ω P) x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finsum_repartitionDualComponent_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/LocalComponent.html#TauCeti.finsum_repartitionDualComponent_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.finsum_repartitionDualComponent_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/LocalComponent.html#TauCeti.finsum_repartitionDualComponent_eq_zero)
- [Source of `TauCeti.finsum_repartitionDualComponent_eq_zero` in TauCeti/FieldTheory/FunctionField/Differential/LocalComponent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/LocalComponent.lean#L213)
