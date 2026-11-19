---
declaration: theorem
origin: cited
lean: TauCeti.VectorBundleOrientation.eulerClass_neg
statement: formalized
proof: formalized
---

# Reversing the orientation negates the Euler class

```lean
TauCeti.VectorBundleOrientation.eulerClass_neg.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {n : ℕ} (o : TauCeti.VectorBundleOrientation F E (Fin (n + 1)))
  (hF : Module.finrank ℝ F = n + 1) : (-o).eulerClass hF = -o.eulerClass hF
```

## Depends on

- [The Euler class of an oriented vector bundle](the-euler-class-of-an-oriented-vector-bundle.md)

## Proof depends on

- [Compatible local classes over a trivializing open cover glue uniquely to the Thom pair](compatible-local-classes-over-a-trivializing-ope.md)
- [The integral Thom class of an oriented vector bundle](the-integral-thom-class-of-an-oriented-vector-bu.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../part-01/algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../../part-01/algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)
- [Uniqueness of the Thom class](uniqueness-of-the-thom-class.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.eulerClass_neg`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.eulerClass_neg`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_neg)
- [Source of `TauCeti.VectorBundleOrientation.eulerClass_neg` in TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean#L81)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
