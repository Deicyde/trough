---
declaration: theorem
origin: cited
lean: TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy
statement: formalized
proof: formalized
---

# Trivial monodromy of the canonical marking

Let `γ₀` and `γ₁` be loops in the fibres over
`y₀` and `y₁`, and let `H : I × I → (Y × E)/Λ` be a free homotopy between them in the total
space: `H (·, 0) = γ₀`, `H (·, 1) = γ₁`, and each `H (·, s)` is a loop. Then `γ₀` and `γ₁` have
the same marking. The intermediate loops `H (·, s)` need not lie in single fibres; when they do,
this says that carrying a loop along a path in the base does not change its marking.

```lean
TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy.{u_1} {Y E : Type} [TopologicalSpace Y]
  [LocallyCompactSpace Y] [T2Space Y] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] {Λ : Type u_1} [AddCommGroup Λ] (P : Y → Λ →ₗ[ℤ] E)
  [∀ (y : Y), DiscreteTopology ↥(P y).range] [∀ (y : Y), IsZLattice ℝ (P y).range]
  (hcont : ∀ (l : Λ), Continuous fun y => (P y) l) (hinj : ∀ (y : Y), Function.Injective ⇑(P y))
  {y₀ y₁ : Y} {z₀ : ↑{z | TauCeti.torusFamilyProjection P z = y₀}}
  {z₁ : ↑{z | TauCeti.torusFamilyProjection P z = y₁}} (γ₀ : Path z₀ z₀) (γ₁ : Path z₁ z₁)
  (H : C(↑unitInterval × ↑unitInterval, AddAction.orbitRel.Quotient Λ (Y × E)))
  (hH : ∀ (s : ↑unitInterval), H (0, s) = H (1, s)) (h₀ : ∀ (t : ↑unitInterval), ↑(γ₀ t) = H (t, 0))
  (h₁ : ∀ (t : ↑unitInterval), ↑(γ₁ t) = H (t, 1)) :
  (TauCeti.torusFamilyMarking P hcont hinj y₀)
      ((TauCeti.HurewiczOne.H₁AddEquivHomology ↧↑{z | TauCeti.torusFamilyProjection P z = y₀})
        (TauCeti.HurewiczOne.loopClass γ₀)) =
    (TauCeti.torusFamilyMarking P hcont hinj y₁)
      ((TauCeti.HurewiczOne.H₁AddEquivHomology ↧↑{z | TauCeti.torusFamilyProjection P z = y₁})
        (TauCeti.HurewiczOne.loopClass γ₁))
```

## Depends on

- [TauCeti.torusFamilyMarking](tauceti-torusfamilymarking.md)

## Proof depends on

- [The Hurewicz theorem](../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Family/Basic.html#TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Family/Basic.html#TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy)
- [Source of `TauCeti.torusFamilyMarking_loopClass_eq_of_homotopy` in TauCeti/AlgebraicTopology/Singular/Torus/Family/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Torus/Family/Basic.lean#L356)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexTori/STATUS.md)
