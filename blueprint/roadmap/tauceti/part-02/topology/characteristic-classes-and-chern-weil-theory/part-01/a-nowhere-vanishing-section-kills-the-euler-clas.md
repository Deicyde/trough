---
declaration: theorem
origin: cited
lean: TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero
statement: formalized
proof: formalized
---

# A nowhere-vanishing section kills the Euler class

If an oriented real vector bundle has a
continuous section `s` with `s b ≠ 0` for every `b`, its Euler class vanishes.

```lean
TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero.{w} {B : Type w}
  [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {n : ℕ} (o : TauCeti.VectorBundleOrientation F E (Fin (n + 1)))
  (hF : Module.finrank ℝ F = n + 1) {s : (b : B) → E b} (hs : Continuous fun b => ⟨b, s b⟩)
  (hs₀ : ∀ (b : B), s b ≠ 0) : o.eulerClass hF = 0
```

## Depends on

- [The Euler class of an oriented vector bundle](the-euler-class-of-an-oriented-vector-bundle.md)

## Proof depends on

- [The integral Thom class of an oriented vector bundle](the-integral-thom-class-of-an-oriented-vector-bu.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero)
- [Source of `TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_forall_ne_zero` in TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean#L110)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
