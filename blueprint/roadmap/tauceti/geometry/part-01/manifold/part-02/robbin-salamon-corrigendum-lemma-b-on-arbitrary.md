---
declaration: theorem
origin: cited
lean: TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero
statement: formalized
proof: formalized
---

# Robbin–Salamon Corrigendum Lemma B (on arbitrary real normed spaces under `C²` regularity)

if `i² = -1`, `j(q)² = -1`, `α(q)(i a) + j(q)(α(q) a) = 0`, `mixedTerm i α j q = 0`, and
`verticalTerm j q = 0` on a neighborhood of `p`, then the fibre vector field
`y ↦ horizontalTerm i α j (p.1, y) a b` has vanishing endomorphism Lie derivative on `j(p.1, ·)`
at `p.2`.

```lean
TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero.{u_1, u_2} {B : Type u_1}
  {V : Type u_2} [NormedAddCommGroup B] [NormedSpace ℝ B] [NormedAddCommGroup V] [NormedSpace ℝ V]
  {i : B →L[ℝ] B} (hi : ∀ (a : B), i (i a) = -a) {α : B × V → B →L[ℝ] V} {j : B × V → V →L[ℝ] V}
  {p : B × V} (hα : ContDiffAt ℝ 2 α p) (hj : ContDiffAt ℝ 2 j p)
  (hj_sq : ∀ᶠ (q : B × V) in nhds p, ∀ (v : V), (j q) ((j q) v) = -v)
  (hαj : ∀ᶠ (q : B × V) in nhds p, ∀ (a : B), (α q) (i a) + (j q) ((α q) a) = 0)
  (hmix :
    ∀ᶠ (q : B × V) in nhds p,
      ∀ (a : B) (v : V), TauCeti.ComplexStructureFamily.mixedTerm i α j q a v = 0)
  (hvert :
    ∀ᶠ (q : B × V) in nhds p, ∀ (v w : V), TauCeti.ComplexStructureFamily.verticalTerm j q v w = 0)
  (a b : B) :
  TauCeti.lieDerivEndomorphism
      (fun y => TauCeti.ComplexStructureFamily.horizontalTerm i α j (p.1, y) a b)
      (fun y => j (p.1, y)) p.2 =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nijenhuis–Lie-derivative identity](../../../../analysis/part-01/calculus/part-01/nijenhuis-lie-derivative-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Integrability.html#TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Integrability.html#TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero)
- [Source of `TauCeti.ComplexStructureFamily.lieDerivEndomorphism_horizontalTerm_eq_zero` in TauCeti/Geometry/Manifold/Complex/Family/Integrability.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/Family/Integrability.lean#L550)
