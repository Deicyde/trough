---
declaration: theorem
origin: cited
lean: TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto
statement: formalized
proof: formalized
---

# The converse Schwarz--Christoffel theorem from the prevertex residues

Let `f` be
holomorphic with nonvanishing derivative on the upper half-plane and suppose its pre-Schwarzian
derivative continues to a function `φ` holomorphic off the distinct real prevertices `a i`, with
singularities at worst simple poles of residues `e i`, and decaying at infinity.  Then `f` is the
affine image `A * F + B` of the normalized Schwarz--Christoffel primitive `F` for the data `a` and
`e`, with `A` and `B` read off at the normalization point.

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto.{u_1} {ι : Type u_1} [Fintype ι]
  (a e : ι → ℝ) (ha : Function.Injective a) (z₀ : UpperHalfPlane) {f φ : ℂ → ℂ}
  (hfn : ∀ z ∈ UpperHalfPlane.upperHalfPlaneSet, deriv f z ≠ 0)
  (hφ : DifferentiableOn ℂ φ (Set.range fun i => ↑(a i))ᶜ)
  (hφf : Set.EqOn φ (logDeriv (deriv f)) UpperHalfPlane.upperHalfPlaneSet)
  (hpole :
    ∀ (i : ι),
      Filter.Tendsto (fun z => (z - ↑(a i)) * φ z) (nhdsWithin ↑(a i) {↑(a i)}ᶜ) (nhds ↑(e i)))
  (hinfty : Filter.Tendsto φ (Bornology.cobounded ℂ) (nhds 0)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The canonical Laurent decomposition](../../part-03/contour/the-canonical-laurent-decomposition.md)
- [Rigidity of the pre-Schwarzian derivative](rigidity-of-the-pre-schwarzian-derivative.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Prevertex.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Prevertex.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto)
- [Source of `TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_tendsto` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Prevertex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Prevertex.lean#L383)
