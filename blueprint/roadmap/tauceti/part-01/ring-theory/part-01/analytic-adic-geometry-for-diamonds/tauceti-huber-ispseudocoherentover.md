---
declaration: def
origin: cited
lean: TauCeti.Huber.IsPseudoCoherentOver
statement: formalized
---

# TauCeti.Huber.IsPseudoCoherentOver

`M` is *`m`-pseudocoherent* over `R`: it has a resolution `⋯ → F₁ → F₀ → M → 0` by finite free
modules `Fᵢ = Fin (n i) → R`, with augmentation `ε` and differentials `d i : Fᵢ₊₁ → Fᵢ`, which is
exact at `M, F₀, …, F_{m-1}`. Thus `0`-pseudocoherent means finitely generated,
`1`-pseudocoherent means finitely presented, and for `m = ⊤` the whole resolution is exact
(Kedlaya–Liu II, Definition 1.1.1; Stacks, Tag 064T, with the index negated).

```lean
TauCeti.Huber.IsPseudoCoherentOver.{u, v} (R : Type u) (M : Type v) [Ring R] [AddCommGroup M]
  [_root_.Module R M] (m : ℕ∞) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsPseudoCoherentOver`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/PseudoCoherent/Basic.html#TauCeti.Huber.IsPseudoCoherentOver).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsPseudoCoherentOver`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/PseudoCoherent/Basic.html#TauCeti.Huber.IsPseudoCoherentOver)
- [Source of `TauCeti.Huber.IsPseudoCoherentOver` in TauCeti/Algebra/Module/PseudoCoherent/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/PseudoCoherent/Basic.lean#L84)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
