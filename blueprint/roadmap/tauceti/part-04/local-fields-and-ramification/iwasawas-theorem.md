---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_continuousMulEquiv_iwasawaGroup
statement: formalized
proof: formalized
---

# Iwasawa's theorem

the tame quotient of the absolute Galois group of `K` is isomorphic, as
a topological group, to the profinite group `⟨σ, τ | σ τ σ⁻¹ = τ ^ q⟩`.

```lean
TauCeti.nonempty_continuousMulEquiv_iwasawaGroup.{u} (K : Type u) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  Nonempty (TauCeti.tameQuotient K ≃ₜ* TauCeti.IwasawaGroup K)
```

## Depends on

- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](the-galois-group-of-the-maximal-unramified-exten.md)
- [The profinite power](../../part-05/profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousMulEquiv_iwasawaGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Presentation.html#TauCeti.nonempty_continuousMulEquiv_iwasawaGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousMulEquiv_iwasawaGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Presentation.html#TauCeti.nonempty_continuousMulEquiv_iwasawaGroup)
- [Source of `TauCeti.nonempty_continuousMulEquiv_iwasawaGroup` in TauCeti/NumberTheory/LocalField/Tame/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Tame/Presentation.lean#L489)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
