---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.quantumDim_ladderModule
statement: formalized
proof: formalized
---

# TauCeti.UqSl2.quantumDim_ladderModule

The quantum dimension of the signed ladder module `L_m^ε` is `ε [m + 1]_q`.

```lean
TauCeti.UqSl2.quantumDim_ladderModule {q : ℂ} [Fact (q ≠ 0)] (hq : q - q⁻¹ ≠ 0) (m : ℕ) (ε : ℤˣ) :
  TauCeti.quantumDim (TauCeti.FiniteHopfModuleCat.of (TauCeti.UqSl2.LadderModule q m ε)) =
    (↑↑ε * TauCeti.quantumInteger q (↑m + 1)) •
      CategoryTheory.CategoryStruct.id
        (CategoryTheory.MonoidalCategoryStruct.tensorUnit
          (TauCeti.FiniteHopfModuleCat ℂ (TauCeti.UqSl2 q)))
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)
- [TauCeti.FiniteHopfModuleCat.pivotalCategory](tauceti-finitehopfmodulecat-pivotalcategory.md)
- [TauCeti.FiniteHopfModuleCat.rigidCategory](tauceti-finitehopfmodulecat-rigidcategory.md)
- [TauCeti.UqSl2.sphericalCategory](tauceti-uqsl2-sphericalcategory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.quantumDim_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Pivotal.html#TauCeti.UqSl2.quantumDim_ladderModule).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.quantumDim_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Pivotal.html#TauCeti.UqSl2.quantumDim_ladderModule)
- [Source of `TauCeti.UqSl2.quantumDim_ladderModule` in TauCeti/QuantumGroups/UqSl2/Pivotal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/UqSl2/Pivotal.lean#L161)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
