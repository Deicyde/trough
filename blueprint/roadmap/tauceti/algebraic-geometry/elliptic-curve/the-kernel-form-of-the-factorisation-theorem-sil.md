---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le
statement: formalized
proof: formalized
---

# The kernel form of the factorisation theorem (Silverman III.4.11)

When the kernel of
`φ : W₁ → W₂` has `deg φ` points, an isogeny `ψ : W₁ → W₃` factors through `φ`, by a unique
isogeny, exactly when `ker φ ≤ ker ψ`.

Without the hypothesis only the forward implication holds (`TauCeti.Isogeny.ker_le_ker_comp`).
The subfield criterion `TauCeti.Isogeny.existsUnique_comp_eq_iff_fieldRange_le` needs no
hypothesis.

```lean
TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le.{u_1} {F : Type u_1} [Field F]
  {W₁ W₂ W₃ : WeierstrassCurve.Affine F} [DecidableEq F] [WeierstrassCurve.IsElliptic W₁]
  {φ : TauCeti.Isogeny W₁ W₂} (hφ : Nat.card ↥φ.ker = φ.degree) (ψ : TauCeti.Isogeny W₁ W₃) :
  (∃! χ, χ.comp φ = ψ) ↔ φ.ker ≤ ψ.ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The factorisation theorem](the-factorisation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le)
- [Source of `TauCeti.Isogeny.existsUnique_comp_eq_iff_ker_le` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Factorisation.lean#L126)
