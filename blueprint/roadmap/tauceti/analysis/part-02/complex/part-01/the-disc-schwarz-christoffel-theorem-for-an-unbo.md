---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty
statement: formalized
proof: formalized
---

# The disc Schwarz--Christoffel theorem for an unbounded polygonal Jordan domain

Suppose a connected open set has Jordan frontier on the Riemann sphere, finitely many distinct
corners of angles `(e i + 1) * π`, straight sides away from those corners, and a sector of opening
`β * π` at infinity. Then it is the bijective image of the unit disc under an affine image of a
disc Schwarz--Christoffel primitive. The finite prevertices have exponents `e i` and tend to the
prescribed vertices; the additional prevertex `1` has exponent `-β - 1` and tends to infinity.

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) {β : ℝ}
  (hβ : β ∈ Set.Ioo 0 2) {U : Set ℂ} (hUo : IsOpen U) (hUc : IsConnected U)
  (hUJ : TauCeti.IsJordanCurve (insert OnePoint.infty (OnePoint.some '' frontier U))) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b, b ≠ 0 ∧ ∀ (z : ℂ), ρ < ‖z - c‖ → (z ∈ U ↔ |((z - c) / b).arg| < β * Real.pi / 2)) :
  ∃ a,
    Function.Injective a ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn
                (fun ζ =>
                  A *
                      TauCeti.schwarzChristoffelDiscPrimitive
                        (Option.elim' 1 fun i => TauCeti.boundaryCayley (a i))
                        (Option.elim' (-β - 1) e) ζ +
                    B)
                (Metric.ball 0 1) U ∧
              (∀ (i : ι),
                  Filter.Tendsto
                    (fun ζ =>
                      A *
                          TauCeti.schwarzChristoffelDiscPrimitive
                            (Option.elim' 1 fun j => TauCeti.boundaryCayley (a j))
                            (Option.elim' (-β - 1) e) ζ +
                        B)
                    (nhdsWithin (↑(TauCeti.boundaryCayley (a i))) (Metric.ball 0 1)) (nhds (v i))) ∧
                Filter.Tendsto
                  (fun ζ =>
                    A *
                        TauCeti.schwarzChristoffelDiscPrimitive
                          (Option.elim' 1 fun i => TauCeti.boundaryCayley (a i))
                          (Option.elim' (-β - 1) e) ζ +
                      B)
                  (nhdsWithin 1 (Metric.ball 0 1)) (Bornology.cobounded ℂ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's theorem for the inside of a Jordan curve](caratheodorys-theorem-for-the-inside-of-a-jordan.md)
- [Rigidity of the pre-Schwarzian derivative](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/rigidity-of-the-pre-schwarzian-derivative.md)
- [Rouché's theorem for a disc, classical form](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Schwarz reflection principle (real axis)](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/schwarz-reflection-principle-real-axis.md)
- [The Schwarz--Christoffel theorem for a bounded polygonal Jordan domain](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-schwarz-christoffel-theorem-for-a-bounded-po.md)
- [The Schwarz--Christoffel theorem for an unbounded polygonal Jordan domain](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-schwarz-christoffel-theorem-for-an-unbounded.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Disc/Infinity.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Disc/Infinity.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelDiscPrimitive_add_of_isJordanCurve_insert_infty` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Disc/Infinity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Disc/Infinity.lean#L39)
