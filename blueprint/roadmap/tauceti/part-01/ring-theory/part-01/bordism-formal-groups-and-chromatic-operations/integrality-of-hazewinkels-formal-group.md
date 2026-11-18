---
declaration: theorem
origin: cited
lean: TauCeti.coeff_hazewinkelFormalGroup_mem
statement: formalized
proof: formalized
---

# Integrality of Hazewinkel's formal group

If `σ` lifts Frobenius
modulo `p A`, and sends the integral generators `vᵢ` to their `p`-th powers, the formal
group with Hazewinkel's rational logarithm has all its coefficients in `A`.

```lean
TauCeti.coeff_hazewinkelFormalGroup_mem.{u_1} {K : Type u_1} [CommRing K] [Algebra ℚ K] {p : ℕ}
  (v : ℕ+ → K) [hp : Fact (Nat.Prime p)] (σ : K →+* K) (A : Subring K)
  (hσp : ∀ a ∈ A, ∃ b ∈ A, σ a - a ^ p = ↑p * b) (hσv : ∀ (j : ℕ+), σ (v j) = v j ^ p)
  (hv : ∀ (j : ℕ+), v j ∈ A) (d : Fin 2 →₀ ℕ) :
  (MvPowerSeries.coeff d) (TauCeti.hazewinkelFormalGroup p v).toPowerSeries ∈ A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hazewinkel's functional equation lemma](hazewinkels-functional-equation-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.coeff_hazewinkelFormalGroup_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/FunctionalEquation.html#TauCeti.coeff_hazewinkelFormalGroup_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.coeff_hazewinkelFormalGroup_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/FunctionalEquation.html#TauCeti.coeff_hazewinkelFormalGroup_mem)
- [Source of `TauCeti.coeff_hazewinkelFormalGroup_mem` in TauCeti/RingTheory/FormalGroup/Hazewinkel/FunctionalEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Hazewinkel/FunctionalEquation.lean#L139)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
