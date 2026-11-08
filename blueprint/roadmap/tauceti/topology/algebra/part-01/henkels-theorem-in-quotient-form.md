---
declaration: theorem
origin: cited
lean: TauCeti.HasZeroSequenceOfUnits.isQuotientMap
statement: formalized
proof: formalized
---

# Henkel's theorem in quotient form

Under exactly the hypotheses of
`TauCeti.HasZeroSequenceOfUnits.isOpenMap`, the map does not merely carry open sets to open sets:
the topology of `N` is the one coinduced from `M`, so a map out of `N` is continuous exactly when
its composite with `f` is.

The quotient conclusion needs `f` continuous everywhere, but that is not an extra hypothesis: an
additive homomorphism out of a topological group is continuous as soon as it is continuous at `0`
(`continuous_of_continuousAt_zero`), so `hfc` is the same assumption the open-mapping theorem
makes. This is the form behind `TauCeti.Huber.IsTateRing.isModuleTopology`, which pins down the
topology of a finite module over a Tate ring.

```lean
TauCeti.HasZeroSequenceOfUnits.isQuotientMap.{u_1, u_2, u_3, u_4} {A : Type u_1} {M : Type u_2}
  {N : Type u_3} [MonoidWithZero A] [TopologicalSpace A] [TauCeti.HasZeroSequenceOfUnits A]
  [AddCommGroup M] [UniformSpace M] [IsUniformAddGroup M] [CompleteSpace M]
  [(nhds 0).IsCountablyGenerated] [NonarchimedeanAddGroup M] [MulActionWithZero A M] [AddGroup N]
  [TopologicalSpace N] [IsTopologicalAddGroup N] [T0Space N] [BaireSpace N] [MulAction A N]
  [ContinuousConstSMul A N] {F : Type u_4} [FunLike F M N] [MulActionHomClass F A M N]
  [AddMonoidHomClass F M N] (f : F) (hf : Function.Surjective ⇑f) (hfc : ContinuousAt (⇑f) 0)
  (hc : ∀ (x : M), ContinuousAt (fun a => a • x) 0) : Topology.IsQuotientMap ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Henkel's open mapping theorem](henkels-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasZeroSequenceOfUnits.isQuotientMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/OpenMapping/Henkel.html#TauCeti.HasZeroSequenceOfUnits.isQuotientMap).

## Sources

- [Tau Ceti documentation: `TauCeti.HasZeroSequenceOfUnits.isQuotientMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/OpenMapping/Henkel.html#TauCeti.HasZeroSequenceOfUnits.isQuotientMap)
- [Source of `TauCeti.HasZeroSequenceOfUnits.isQuotientMap` in TauCeti/Topology/Algebra/OpenMapping/Henkel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/OpenMapping/Henkel.lean#L86)
