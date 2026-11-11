---
declaration: def
origin: cited
lean: TauCeti.VectorBundleOrientation.thomClass
statement: formalized
---

# The integral Thom class of an oriented vector bundle

For an orientation `o` of a real
vector bundle `E` over an arbitrary base, with model fibre `F` of dimension `n + 1`, this is the
class `U ∈ Hⁿ⁺¹(E, E₀; ℤ)` whose restriction to the fibre pair `(E_b, E_b ∖ {0})` over every
point `b` is the generator of `Hⁿ⁺¹(E_b, E_b ∖ {0}; ℤ)` selected by the orientation `o b`: the
pull-back, along any linear trivialization at `b`, of the generator of `Hⁿ⁺¹(F, F ∖ {0}; ℤ)`
selected by `o b` read in that trivialization
(`TauCeti.VectorBundleOrientation.singularCohomologyMap_fiberThomPairMap_thomClass`). This
property determines it (`TauCeti.VectorBundleOrientation.eq_thomClass_iff`).

```lean
TauCeti.VectorBundleOrientation.thomClass.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {n : ℕ} (o : TauCeti.VectorBundleOrientation F E (Fin (n + 1)))
  (hF : Module.finrank ℝ F = n + 1) :
  ↑((TauCeti.thomPair F E).singularCohomology ↧(ULift.{w, 0} ℤ) ℤ (↧(ULift.{w, 0} ℤ)) (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Compatible local classes over a trivializing open cover glue uniquely to the Thom pair](compatible-local-classes-over-a-trivializing-ope.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem over a field](../../../algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientation.thomClass`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/ThomClass.html#TauCeti.VectorBundleOrientation.thomClass).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientation.thomClass`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/ThomClass.html#TauCeti.VectorBundleOrientation.thomClass)
- [Source of `TauCeti.VectorBundleOrientation.thomClass` in TauCeti/Topology/VectorBundle/Orientation/ThomClass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/Orientation/ThomClass.lean#L453)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
