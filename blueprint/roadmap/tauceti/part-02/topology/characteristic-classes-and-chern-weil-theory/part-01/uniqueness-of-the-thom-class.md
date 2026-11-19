---
declaration: theorem
origin: cited
lean: TauCeti.VectorBundleOrientation.eq_thomClass_iff
statement: formalized
proof: formalized
---

# Uniqueness of the Thom class

A class of `Hⁿ⁺¹(E, E₀; ℤ)` is the Thom class of the oriented
bundle exactly when it restricts on every fibre to the generator selected by the fibre
orientation, read in a linear trivialization at that point.

```lean
TauCeti.VectorBundleOrientation.eq_thomClass_iff.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {n : ℕ} (o : TauCeti.VectorBundleOrientation F E (Fin (n + 1)))
  (hF : Module.finrank ℝ F = n + 1)
  (u :
    ↑((TauCeti.thomPair F E).singularCohomology ↧(ULift.{w, 0} ℤ) ℤ (↧(ULift.{w, 0} ℤ)) (n + 1))) :
  u = o.thomClass hF ↔
    ∀ (e : Bundle.Trivialization F Bundle.TotalSpace.proj)
      [inst : Bundle.Trivialization.IsLinear ℝ e] (b : B) (hb : b ∈ e.baseSet),
      (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TauCeti.fiberThomPairMap F E b) (n + 1)))
          u =
        (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap
              (Bundle.Trivialization.continuousLinearEquivAt ℝ e b hb).complZeroPairIso.hom
              (n + 1)))
          (((Bundle.Trivialization.mapOrientation (Fin (n + 1)) e hb) (o b)).localCohomologyClass
            hF)
```

## Depends on

- [The integral Thom class of an oriented vector bundle](the-integral-thom-class-of-an-oriented-vector-bu.md)

## Proof depends on

- [Compatible local classes over a trivializing open cover glue uniquely to the Thom pair](compatible-local-classes-over-a-trivializing-ope.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../part-01/algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../../part-01/algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`](../../../../part-01/algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-below.md)
- [The relative universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.eq_thomClass_iff`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/ThomClass.html#TauCeti.VectorBundleOrientation.eq_thomClass_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.eq_thomClass_iff`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/ThomClass.html#TauCeti.VectorBundleOrientation.eq_thomClass_iff)
- [Source of `TauCeti.VectorBundleOrientation.eq_thomClass_iff` in TauCeti/Topology/VectorBundle/Orientation/ThomClass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Orientation/ThomClass.lean#L580)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
