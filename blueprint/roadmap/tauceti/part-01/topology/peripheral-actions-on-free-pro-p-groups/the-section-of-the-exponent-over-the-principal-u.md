---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_section_principalUnits
statement: formalized
proof: formalized
---

# The section of the exponent over the principal units

Let `F` be a marked free pro-`p`
group of positive rank, and let `k ≥ 1`, with `k ≥ 2` when `p = 2`. Then the exponent character
of the peripheral automorphism group has a continuous homomorphic section over the principal
units `U^(k) = 1 + p ^ k ℤ_p`: a continuous homomorphism `s : U^(k) →ₜ* peripheralAut hF (basis e)`
with `exponent (s v) = v` for every `v`.

```lean
TauCeti.Peripheral.exists_section_principalUnits.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r))
  (hr : 0 < r) {k : ℕ} (hk : 0 < k) (hk₂ : p = 2 → 2 ≤ k) :
  ∃ s, ∀ (v : ↥(TauCeti.unitsPrincipal p k)), (TauCeti.Peripheral.exponent hF e hr) (s v) = ↑v
```

## Depends on

- [TauCeti.Peripheral.exponent](tauceti-peripheral-exponent.md)
- [TauCeti.Peripheral.peripheralAut](tauceti-peripheral-peripheralaut.md)

## Proof depends on

- [The `ℓ`-adic comparison](../profinite-integers-profinite-powers-and-continuo/the-l-adic-comparison.md)
- [The exponent character is continuous](the-exponent-character-is-continuous.md)
- [The peripheral automorphisms form a closed subgroup](the-peripheral-automorphisms-form-a-closed-subgr.md)
- [The peripheral-power theorem](the-peripheral-power-theorem.md)
- [The product decomposition of the profinite integers](../profinite-integers-profinite-powers-and-continuo/the-product-decomposition-of-the-profinite-integ.md)
- [The profinite power](../profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)
- [TauCeti.ContinuousAut.compactSpace](../profinite-integers-profinite-powers-and-continuo/tauceti-continuousaut-compactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_section_principalUnits`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Section.html#TauCeti.Peripheral.exists_section_principalUnits).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_section_principalUnits`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Section.html#TauCeti.Peripheral.exists_section_principalUnits)
- [Source of `TauCeti.Peripheral.exists_section_principalUnits` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Section.lean#L89)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
