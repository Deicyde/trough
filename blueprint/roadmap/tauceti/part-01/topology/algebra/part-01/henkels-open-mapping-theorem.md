---
declaration: theorem
origin: cited
lean: TauCeti.HasZeroSequenceOfUnits.isOpenMap
statement: formalized
proof: formalized
---

# Henkel's open mapping theorem

A surjective `A`-equivariant additive map from a complete
first-countable nonarchimedean group to a Baire space is open, when `A` has a zero sequence of
units.

Only continuity at zero is asked of `f`, and only continuity in the scalar at zero is asked of
the action, in the form `hc` that the Baire step already uses.

```lean
TauCeti.HasZeroSequenceOfUnits.isOpenMap.{u_1, u_2, u_3, u_4} {A : Type u_1} {M : Type u_2}
  {N : Type u_3} [MonoidWithZero A] [TopologicalSpace A] [TauCeti.HasZeroSequenceOfUnits A]
  [AddCommGroup M] [UniformSpace M] [IsUniformAddGroup M] [CompleteSpace M]
  [(nhds 0).IsCountablyGenerated] [NonarchimedeanAddGroup M] [MulActionWithZero A M] [AddGroup N]
  [TopologicalSpace N] [IsTopologicalAddGroup N] [T0Space N] [BaireSpace N] [MulAction A N]
  [ContinuousConstSMul A N] {F : Type u_4} [FunLike F M N] [MulActionHomClass F A M N]
  [AddMonoidHomClass F M N] (f : F) (hf : Function.Surjective ⇑f) (hfc : ContinuousAt (⇑f) 0)
  (hc : ∀ (x : M), ContinuousAt (fun a => a • x) 0) : IsOpenMap ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasZeroSequenceOfUnits.isOpenMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/OpenMapping/Henkel.html#TauCeti.HasZeroSequenceOfUnits.isOpenMap).

## Sources

- [Tau Ceti documentation: `TauCeti.HasZeroSequenceOfUnits.isOpenMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/OpenMapping/Henkel.html#TauCeti.HasZeroSequenceOfUnits.isOpenMap)
- [Source of `TauCeti.HasZeroSequenceOfUnits.isOpenMap` in TauCeti/Topology/Algebra/OpenMapping/Henkel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/OpenMapping/Henkel.lean#L73)
