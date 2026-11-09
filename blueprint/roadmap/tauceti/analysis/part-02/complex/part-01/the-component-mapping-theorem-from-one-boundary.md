---
declaration: theorem
origin: cited
lean: TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value
statement: formalized
proof: formalized
---

# The component mapping theorem from one boundary sheet

Under boundary avoidance,
one uniquely parametrized regular boundary value makes the primitive a bijection onto the
complementary component of the finite boundary trace containing its base-point image.
Neither simple connectivity of that component nor global boundary injectivity is assumed.

```lean
TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value.{u_1}
  {ι : Type u_1} [Fintype ι] (a e : ι → ℝ) (z₀ : UpperHalfPlane)
  (hfinite : ∀ (j : ι), -1 ≤ ∑ i with a i = a j, e i)
  (havoid :
    Disjoint (TauCeti.schwarzChristoffelPrimitive a e z₀ '' UpperHalfPlane.upperHalfPlaneSet)
      (TauCeti.schwarzChristoffelFiniteBoundary a e z₀))
  {p q x : ℝ} (ha : ∀ (i : ι), e i ≠ 0 → a i ∉ Set.Ioo p q) (hx : x ∈ Set.Ioo p q)
  (hunique :
    ∀ (t : OnePoint ℝ),
      TauCeti.schwarzChristoffelSphereBoundary a e z₀ t =
          TauCeti.schwarzChristoffelSphereBoundary a e z₀ ↑x →
        t = ↑x) :
  Set.BijOn (TauCeti.schwarzChristoffelPrimitive a e z₀) UpperHalfPlane.upperHalfPlaneSet
    (connectedComponentIn (TauCeti.schwarzChristoffelFiniteBoundary a e z₀)ᶜ
      (TauCeti.schwarzChristoffelPrimitive a e z₀ ↑z₀))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rouché's theorem for a disc, classical form](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/BoundarySheet.html#TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value).

## Sources

- [Tau Ceti documentation: `TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/BoundarySheet.html#TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value)
- [Source of `TauCeti.bijOn_schwarzChristoffelPrimitive_connectedComponentIn_of_unique_boundary_value` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/BoundarySheet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/BoundarySheet.lean#L178)
