---
declaration: def
origin: cited
lean: TauCeti.VectorBundleOrientation.eulerClass
statement: formalized
---

# The Euler class of an oriented vector bundle

For an orientation `o` of a real vector
bundle `E → B` with model fibre `F` of dimension `n + 1`, this is the class `e(E, o) ∈ Hⁿ⁺¹(B; ℤ)`
obtained from the Thom class `U ∈ Hⁿ⁺¹(E, E₀; ℤ)` by restriction to `Hⁿ⁺¹(E; ℤ)` followed by
pull-back along the zero section.

```lean
TauCeti.VectorBundleOrientation.eulerClass.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {n : ℕ} (o : TauCeti.VectorBundleOrientation F E (Fin (n + 1)))
  (hF : Module.finrank ℝ F = n + 1) :
  ↑(TopCat.singularCohomology ↧(ULift.{w, 0} ℤ) ℤ (↧(ULift.{w, 0} ℤ)) (↧B) (n + 1))
```

## Depends on

- [The integral Thom class of an oriented vector bundle](the-integral-thom-class-of-an-oriented-vector-bu.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.eulerClass`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.eulerClass`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass)
- [Source of `TauCeti.VectorBundleOrientation.eulerClass` in TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean#L64)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
