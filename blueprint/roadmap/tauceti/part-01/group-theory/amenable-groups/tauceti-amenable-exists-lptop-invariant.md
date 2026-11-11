---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.exists_lpTop_invariant
statement: formalized
proof: formalized
---

# TauCeti.Amenable.exists_lpTop_invariant

An amenable locally compact group carries a left-invariant mean on `L∞` of any regular left
Haar measure `μ`: a positive linear functional `M` on `L∞(G, μ)` with `M 1 = 1` and
`M (L_g φ) = M φ`.

```lean
TauCeti.Amenable.exists_lpTop_invariant.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [LocallyCompactSpace G] [MeasurableSpace G] [BorelSpace G]
  (μ : MeasureTheory.Measure G) [μ.IsHaarMeasure] [μ.Regular] [TauCeti.Amenable G] :
  ∃ M,
    M 1 = 1 ∧
      ∀ (g : G) (φ : ↥(MeasureTheory.Lp ℝ ⊤ μ)),
        M (((MeasureTheory.Lp.leftTranslation μ ⊤ ℝ) g) φ) = M φ
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [Convolution of `L¹` with `L∞`](convolution-of-l1-with-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.exists_lpTop_invariant`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/LocallyCompact.html#TauCeti.Amenable.exists_lpTop_invariant).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.exists_lpTop_invariant`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/LocallyCompact.html#TauCeti.Amenable.exists_lpTop_invariant)
- [Source of `TauCeti.Amenable.exists_lpTop_invariant` in TauCeti/GroupTheory/Amenable/LocallyCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/LocallyCompact.lean#L262)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
