---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.sixJ_pentagon
statement: formalized
proof: formalized
---

# The Biedenharn–Elliott pentagon identity

**The Biedenharn–Elliott pentagon identity** for the `α₀ = 1` change-of-decomposition
(`F`-matrix) entries `sixJ` of `clebschGordanInclusion` across all signed ladder modules
`L_a^ε ⊗ L_b^δ ⊗ L_c^ζ ⊗ L_d^θ` at generic `q`.

```lean
TauCeti.UqSl2.sixJ_pentagon {q : ℂ} (hq : TauCeti.IsGenericQuantumParameter q) (ε δ ζ θ : ℤˣ)
  (a b c d e u w x y : ℕ) :
  TauCeti.UqSl2.sixJ hq ε δ (ζ * θ) a b y e u x * TauCeti.UqSl2.sixJ hq (ε * δ) ζ θ u c d e w y =
    ∑ z ∈ Finset.range (b + c + 1),
      TauCeti.UqSl2.sixJ hq δ ζ θ b c d x z y * TauCeti.UqSl2.sixJ hq ε (δ * ζ) θ a z d e w x *
        TauCeti.UqSl2.sixJ hq ε δ ζ a b c w u z
```

## Depends on

- [TauCeti.UqSl2.clebschGordanEquiv](tauceti-uqsl2-clebschgordanequiv.md)

## Proof depends on

- [Schur's lemma, vanishing form](../../../ring-theory/part-01/semisimple/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.sixJ_pentagon`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Pentagon.html#TauCeti.UqSl2.sixJ_pentagon).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.sixJ_pentagon`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Pentagon.html#TauCeti.UqSl2.sixJ_pentagon)
- [Source of `TauCeti.UqSl2.sixJ_pentagon` in TauCeti/QuantumGroups/UqSl2/ClebschGordan/Pentagon.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Pentagon.lean#L419)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
