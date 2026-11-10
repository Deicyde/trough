---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le
statement: formalized
proof: formalized
---

# The factorisation theorem

**The factorisation theorem** (Silverman, *The Arithmetic of Elliptic Curves*, III.4.11 in its
separable form): an isogeny `ψ : W₁ → W₃` factors through an isogeny `φ : W₁ → W₂`, by a unique
isogeny `λ : W₂ → W₃`, exactly when the function field `ψ` pulls back sits inside the one `φ`
pulls back.

The criterion is on subfields of `F(W₁)`, not on kernels of point maps, and that is what makes it
correct in general: over `ℚ`, a curve with no rational `2`-torsion has `ker [2](ℚ) = {O}` without
the identity factoring through `[2]`, and relative Frobenius has trivial *geometric* point kernel
without the identity factoring through it. In both cases the subfield containment fails, as it
should.

```lean
TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le.{u_1} {F : Type u_1} [Field F]
  {W₁ W₂ W₃ : WeierstrassCurve.Affine F} (φ : TauCeti.Isogeny W₁ W₂) (ψ : TauCeti.Isogeny W₁ W₃) :
  (∃! χ, χ.comp φ = ψ) ↔ ψ.fieldPullback.fieldRange ≤ φ.fieldPullback.fieldRange
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le)
- [Source of `TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.lean#L80)
