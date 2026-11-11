---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends
statement: formalized
proof: formalized
---

# The Schwarz--Christoffel theorem for polygonal domains with several ends

Let `U` be a
simply connected, unbounded open set, with a point `q` outside its closure, whose frontier is a
finite union of closed segments and closed rays.  Suppose that `U` coincides near each frontier
point other than the distinct vertices `v i` with an open half-plane, and near the vertex `v i` with
the open sector of opening `(e i + 1) * π` at `v i`, where `e i ∈ (-1, 1)`.  Suppose finally that
far out `U` is covered by pairwise disjoint ends `E k ⊆ U`, each either the far part of a sector of
opening `(-e' k - 1) * π` with `e' k ∈ (-3, -1)`, a half-strip between two parallel sides with
`e' k = -1`, or the far part of the exterior of a closed half-strip with `e' k = -3`.

Then there are distinct real prevertices `a i` of the vertices and `a' k` of the ends, and
constants `A ≠ 0` and `B`, such that `z ↦ A * F z + B` maps the upper half-plane bijectively onto
`U`, where `F` is the normalized Schwarz--Christoffel primitive for these prevertices and the
turning exponents `e i` and `e' k`.  The Schwarz--Christoffel vertex at `a i` is sent to `v i`, and
near `a' k` the map takes its values in the end `E k`.

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends.{u_1, u_2, u_3,
    u_4}
  {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ] (e : ι → ℝ)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (e' : κ → ℝ) (z₀ : UpperHalfPlane) {U : Set ℂ}
  (hUo : IsOpen U) (hUs : IsSimplyConnected U) (hUb : ¬Bornology.IsBounded U) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ p b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - p) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  {σ : Type u_3} {τ : Type u_4} [Finite σ] [Finite τ] {x y : σ → ℂ} {o d : τ → ℂ}
  (hd : ∀ (k : τ), d k ≠ 0)
  (hfr : frontier U = (⋃ i, segment ℝ (x i) (y i)) ∪ ⋃ k, (fun t => o k + ↑t * d k) '' Set.Ici 0)
  {q : ℂ} (hq : q ∉ closure U) {E : κ → Set ℂ} {c b : κ → ℂ} {ρ : κ → ℝ} {R : ℝ}
  (hb : ∀ (k : κ), b k ≠ 0)
  (hE :
    ∀ (k : κ),
      e' k ∈ Set.Ioo (-3) (-1) ∧
          E k = {w | ρ k < ‖w - c k‖ ∧ |((w - c k) / b k).arg| < (-e' k - 1) * Real.pi / 2} ∨
        e' k = -1 ∧
            E k = {w | ρ k < ((w - c k) / b k).re ∧ ((w - c k) / b k).im ∈ Set.Ioo 0 Real.pi} ∨
          e' k = -3 ∧
            E k =
              {w |
                ρ k < ‖w - c k‖ ∧
                  (((w - c k) / b k).re < 0 ∨ ((w - c k) / b k).im ∉ Set.Icc 0 Real.pi)})
  (hEU : ∀ (k : κ), E k ⊆ U) (hUE : ∀ w ∈ U, R < ‖w‖ → ∃ k, w ∈ E k)
  (hEd : Pairwise (Function.onFun Disjoint E)) :
  ∃ a a',
    Function.Injective (Sum.elim a a') ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn
                (fun z =>
                  A * TauCeti.schwarzChristoffelPrimitive (Sum.elim a a') (Sum.elim e e') z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              (∀ (i : ι),
                  A *
                        TauCeti.schwarzChristoffelVertex (Sum.elim a a') (Sum.elim e e') z₀
                          (Sum.inl i) +
                      B =
                    v i) ∧
                ∀ (k : κ),
                  ∀ᶠ (z : ℂ) in nhdsWithin (↑(a' k)) UpperHalfPlane.upperHalfPlaneSet,
                    A * TauCeti.schwarzChristoffelPrimitive (Sum.elim a a') (Sum.elim e e') z₀ z +
                        B ∈
                      E k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's continuity theorem](../../part-02/complex/part-01/caratheodorys-continuity-theorem.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)
- [The Schwarz--Christoffel formula](the-schwarz-christoffel-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/PolygonalDomain.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/PolygonalDomain.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/PolygonalDomain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/PolygonalDomain.lean#L329)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ConformalMapping/STATUS.md)
