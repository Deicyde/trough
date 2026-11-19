---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc, TauCeti.SmoothForm.IsOfType.exists_delBar_eventually_eq_of_pi
statement: formalized
proof: formalized
---

# The Dolbeault–Grothendieck lemma for `(0,q)`-forms on polydiscs (`TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc`)

A smooth form `η` of type
`(0,q+1)` on `ι → ℂ`, with coefficients in a complex Banach space, whose Dolbeault differential
vanishes on the polydisc `∏ B(c_i, r_i)`, is Dolbeault-exact on every concentric polydisc
`∏ B(c_i, r'_i)` with `r'_i < r_i`: some smooth form `f` of type `(0,q)` satisfies `∂bar f = η`
there.

```lean
TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc.{u_2, u_3} {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {ι : Type u_3} [Fintype ι] [CompleteSpace F] {q : ℕ}
  {η : TauCeti.SmoothForm (modelWithCornersSelf ℝ (ι → ℂ)) (ι → ℂ) F (q + 1)}
  (hη :
    η.IsOfType (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)) 0 (q + 1))
  {c : ι → ℂ} {r r' : ι → ℝ} (hr : ∀ (i : ι), r' i < r i)
  (hclosed :
    ∀ z ∈ Set.univ.pi fun i => Metric.ball (c i) (r i),
      ↑((TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)).delBar η) z = 0) :
  ∃ f,
    f.IsOfType (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)) 0 q ∧
      ∀ z ∈ Set.univ.pi fun i => Metric.ball (c i) (r' i),
        ↑((TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)).delBar f) z =
          ↑η z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Dolbeault–Grothendieck lemma for `(0,q)`-forms on polydiscs (`TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc`)](the-dolbeault-grothendieck-lemma-for-0-q-forms-o.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/LocalExactness.html#TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc).

## Other forms

**The Dolbeault–Grothendieck lemma for `(0,q)`-forms on product domains.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsOfType.exists_delBar_eventually_eq_of_pi`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/LocalExactness.html#TauCeti.SmoothForm.IsOfType.exists_delBar_eventually_eq_of_pi).

```lean
TauCeti.SmoothForm.IsOfType.exists_delBar_eventually_eq_of_pi.{u_2, u_3} {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {ι : Type u_3} [Fintype ι] [CompleteSpace F] {q : ℕ}
  {η : TauCeti.SmoothForm (modelWithCornersSelf ℝ (ι → ℂ)) (ι → ℂ) F (q + 1)}
  (hη :
    η.IsOfType (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)) 0 (q + 1))
  {U K : ι → Set ℂ} (hU : ∀ (i : ι), IsOpen (U i)) (hK : ∀ (i : ι), IsCompact (K i))
  (hKU : ∀ (i : ι), K i ⊆ U i)
  (hclosed :
    ∀ z ∈ Set.univ.pi U,
      ↑((TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)).delBar η) z = 0) :
  ∃ f,
    f.IsOfType (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)) 0 q ∧
      ∀ᶠ (z : ι → ℂ) in nhdsSet (Set.univ.pi K),
        ↑((TauCeti.SmoothAlmostComplexStructure.ofComplexManifold (ι → ℂ) (ι → ℂ)).delBar f) z =
          ↑η z
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/LocalExactness.html#TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc)
- [Source of `TauCeti.SmoothForm.IsOfType.exists_delBar_eq_of_polydisc` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/LocalExactness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/LocalExactness.lean#L123)
