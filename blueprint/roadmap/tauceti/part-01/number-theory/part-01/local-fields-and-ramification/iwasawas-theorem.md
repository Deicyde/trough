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

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](the-galois-group-of-the-maximal-unramified-exten.md)
- [The profinite power](../../../topology/profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousMulEquiv_iwasawaGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Presentation.html#TauCeti.nonempty_continuousMulEquiv_iwasawaGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousMulEquiv_iwasawaGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Presentation.html#TauCeti.nonempty_continuousMulEquiv_iwasawaGroup)
- [Source of `TauCeti.nonempty_continuousMulEquiv_iwasawaGroup` in TauCeti/NumberTheory/LocalField/Tame/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Tame/Presentation.lean#L489)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
