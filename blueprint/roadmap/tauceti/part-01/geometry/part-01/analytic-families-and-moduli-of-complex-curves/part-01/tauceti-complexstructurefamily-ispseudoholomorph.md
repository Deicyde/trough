---
declaration: theorem
origin: cited
lean: TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff
statement: formalized
proof: formalized
---

# TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff

Global characterization: `x ↦ (x, σ x)` is `(i, J)`-pseudoholomorphic if and only if `σ` is
differentiable everywhere and `sectionTerm i α j σ b a = 0` for all `b, a`.

```lean
TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff.{u_1, u_2} {B : Type u_1}
  {V : Type u_2} [NormedAddCommGroup B] [NormedSpace ℝ B] [NormedAddCommGroup V] [NormedSpace ℝ V]
  (J : TauCeti.SmoothAlmostComplexStructure (modelWithCornersSelf ℝ (B × V)) (B × V))
  (i : B →L[ℝ] B) (hi : ∀ (a : B), i (i a) = -a) (α : B × V → B →L[ℝ] V) (j : B × V → V →L[ℝ] V)
  {σ : B → V}
  (hJ :
    ∀ (b : B),
      J.toEndomorphism (b, σ b) = TauCeti.ComplexStructureFamily.blockEndomorphism i α j (b, σ b)) :
  (TauCeti.IsPseudoholomorphic (TauCeti.SmoothAlmostComplexStructure.const i hi) J fun x =>
      (x, σ x)) ↔
    Differentiable ℝ σ ∧ ∀ (b a : B), TauCeti.ComplexStructureFamily.sectionTerm i α j σ b a = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Section.html#TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Family/Section.html#TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff)
- [Source of `TauCeti.ComplexStructureFamily.isPseudoholomorphic_graph_iff` in TauCeti/Geometry/Manifold/Complex/Family/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/Family/Section.lean#L200)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
