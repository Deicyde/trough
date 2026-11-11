---
declaration: theorem
origin: cited
lean: Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add
statement: formalized
proof: formalized
---

# The orbifold area formula for a cocompact Fuchsian group

The covolume of `Γ` is
`2π (-χ(X(Γ)) + ∑ₑ (1 - 1 / mₑ))`, where `X(Γ)` is the compactified quotient, of finite CW type,
and `e` runs over the elliptic orbits of `Γ`, with stabilizer orders `mₑ`. With `χ = 2 - 2g`
this is `2π (2g - 2 + ∑ₑ (1 - 1 / mₑ))`.

```lean
Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  [CompactSpace (MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane)] :
  MeasureTheory.covolume (↥Γ) UpperHalfPlane MeasureTheory.volume =
    ENNReal.ofReal
      (2 * Real.pi *
        (-↑(TauCeti.eulerChar Γ.CompactifiedQuotient) +
          ∑ᶠ (e : MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane) (_ : e ∈ Γ.ellipticOrbits),
            (1 - (↑(TauCeti.cardStabilizerOnOrbit e))⁻¹)))
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [Euler--Poincaré for cellular chains](../../../algebraic-topology/cellular/euler-poincare-for-cellular-chains.md)
- [The Gauss–Bonnet formula](../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [The quotient of a cocompact Fuchsian group has finite CW type](the-quotient-of-a-cocompact-fuchsian-group-has-f.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add).

## Sources

- [Tau Ceti documentation: `Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add)
- [Source of `Subgroup.covolume_eq_two_pi_mul_neg_eulerChar_add` in TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean#L112)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
