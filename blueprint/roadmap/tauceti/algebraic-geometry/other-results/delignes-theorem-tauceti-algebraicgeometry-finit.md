---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank, WeierstrassCurve.IsIntegralModularForm.mem_adjoin
statement: formalized
proof: formalized
---

# Deligne's theorem (`TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`)

Let `G` be a finite locally free commutative group scheme over `S`
whose rank is `n` at every point of `S`. Then every point `x : X ⟶ G` over `S` is killed by
`n`: its `n`-th power in the group of `X`-valued points of `G` is the unit.

```lean
TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank.{u}
  {S : AlgebraicGeometry.Scheme} (G : TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme S) {n : ℕ}
  (hn : ∀ (s : ↥S), AlgebraicGeometry.Scheme.Hom.finrank G.structureMap s = n)
  {X : CategoryTheory.Over S} (x : X ⟶ G.toOver) : x ^ n = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deligne's theorem (`TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk`)](../../algebra/algebraic-group/delignes-theorem-tauceti-alghom-convpow-eq-one-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupScheme/KilledByRank.html#TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank).

## Other forms

**Deligne's theorem.** Formalized in Tau Ceti as [`WeierstrassCurve.IsIntegralModularForm.mem_adjoin`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.html#WeierstrassCurve.IsIntegralModularForm.mem_adjoin).

```lean
WeierstrassCurve.IsIntegralModularForm.mem_adjoin {k : ℕ}
  {f : MvPolynomial WeierstrassCurve.Coeff ℤ} (hf : WeierstrassCurve.IsIntegralModularForm k f) :
  f ∈
    ℤ[WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
      WeierstrassCurve.c₆ WeierstrassCurve.Universal.curve,
      WeierstrassCurve.Δ WeierstrassCurve.Universal.curve]
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupScheme/KilledByRank.html#TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank)
- [Source of `TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank` in TauCeti/AlgebraicGeometry/GroupScheme/KilledByRank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/GroupScheme/KilledByRank.lean#L118)
