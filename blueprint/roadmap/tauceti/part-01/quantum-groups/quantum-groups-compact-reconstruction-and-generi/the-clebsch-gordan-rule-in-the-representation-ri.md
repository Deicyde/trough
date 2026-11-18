---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule
statement: formalized
proof: formalized
---

# The Clebsch–Gordan rule in the representation ring

at a generic parameter,
`[L_m^ε] · [L_n^δ] = ∑_(j = 0)^(min m n) [L_(m + n - 2j)^(εδ)]`.

```lean
TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule {q : ℂ} [Fact (q ≠ 0)]
  (hq : TauCeti.IsGenericQuantumParameter q) (m n : ℕ) (ε δ : ℤˣ) :
  TauCeti.SplitK0.of (TauCeti.FiniteHopfModuleCat.of (TauCeti.UqSl2.LadderModule q m ε)) *
      TauCeti.SplitK0.of (TauCeti.FiniteHopfModuleCat.of (TauCeti.UqSl2.LadderModule q n δ)) =
    ∑ j ∈ Finset.range (min m n + 1),
      TauCeti.SplitK0.of
        (TauCeti.FiniteHopfModuleCat.of (TauCeti.UqSl2.LadderModule q (m + n - 2 * j) (ε * δ)))
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)

## Proof depends on

- [The character homomorphism is injective](the-character-homomorphism-is-injective.md)
- [Complete reducibility](complete-reducibility.md)
- [TauCeti.UqSl2.clebschGordanEquiv](tauceti-uqsl2-clebschgordanequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule)
- [Source of `TauCeti.UqSl2.of_ladderModule_mul_of_ladderModule` in TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean#L277)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
