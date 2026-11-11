---
declaration: theorem
origin: cited
lean: TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one
statement: formalized
proof: formalized
---

# The Euler class of an oriented line bundle vanishes

For an oriented real vector bundle of
rank one over a normal paracompact base, `e(E, o) = 0` in `H¹(B; ℤ)`: the bundle has a positive,
hence nowhere-zero, continuous section.

```lean
TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one.{w} {B : Type w}
  [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommGroup (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] [NormalSpace B] [ParacompactSpace B]
  (o : TauCeti.VectorBundleOrientation F E (Fin 1)) (hF : Module.finrank ℝ F = 1) :
  o.eulerClass hF = 0
```

## Depends on

- [The Euler class of an oriented vector bundle](the-euler-class-of-an-oriented-vector-bundle.md)

## Proof depends on

- [A nowhere-vanishing section kills the Euler class](a-nowhere-vanishing-section-kills-the-euler-clas.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/EulerClass.html#TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one)
- [Source of `TauCeti.VectorBundleOrientation.eulerClass_eq_zero_of_finrank_eq_one` in TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/Orientation/EulerClass.lean#L124)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
