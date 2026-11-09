---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le
statement: formalized
proof: formalized
---

# Cauchy--Schwarz along a complex line

For a compatible pair, the squares of the
components `g(v, w)` and `ω(v, w) = g(J v, w)` of `w` along the orthogonal pair `v`, `J v` add up
to at most `g(v, v) g(w, w)`.

```lean
TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le.{u_1} {V : Type u_1}
  [AddCommGroup V] [_root_.Module ℝ V] {ω : TauCeti.SymplecticForm V}
  {J : TauCeti.AlmostComplexStructure V} (h : ω.Compatible J) (v w : V) :
  ((ω.associatedBilinForm J) v) w ^ 2 + (fun v w => (ω.toBilinForm v) w) v w ^ 2 ≤
    ((ω.associatedBilinForm J) v) v * ((ω.associatedBilinForm J) w) w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Wirtinger.html#TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Wirtinger.html#TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le)
- [Source of `TauCeti.SymplecticForm.Compatible.sq_associatedBilinForm_add_sq_le` in TauCeti/Geometry/Symplectic/Wirtinger.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Wirtinger.lean#L131)
