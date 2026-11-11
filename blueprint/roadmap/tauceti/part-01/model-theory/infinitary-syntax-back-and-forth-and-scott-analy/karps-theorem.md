---
declaration: theorem
origin: cited
lean: TauCeti.karp_theorem, TauCeti.karp_theorem_at, TauCeti.InfEquivAt.potentialIso, TauCeti.PotentialIso.infEquivAt
statement: formalized
proof: formalized
---

# Karp's theorem

Structures in a relational language are potentially isomorphic exactly when
they satisfy the same infinitary sentences. The converse uses the carrier `M ⊕ N`.

```lean
TauCeti.karp_theorem.{u, v, w, w'} {L : FirstOrder.Language} {M : Type w} {N : Type w'}
  [L.Structure M] [L.Structure N] [L.IsRelational] :
  TauCeti.PotentialIso M N ↔ TauCeti.InfEquivW M N
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Proof depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.karp_theorem`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem).

## Other forms

**Karp's theorem at a carrier.** Formalized in Tau Ceti as [`TauCeti.karp_theorem_at`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem_at).

```lean
TauCeti.karp_theorem_at.{u, v, w, w', uκ} {L : FirstOrder.Language} {M : Type w} {N : Type w'}
  [L.Structure M] [L.Structure N] [L.IsRelational] {κ : Type uκ} (cN : TauCeti.IndexCoding N κ) :
  TauCeti.PotentialIso M N ↔ TauCeti.InfEquivAt κ M N
```

**Karp's theorem, converse direction.** Formalized in Tau Ceti as [`TauCeti.InfEquivAt.potentialIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.InfEquivAt.potentialIso).

```lean
TauCeti.InfEquivAt.potentialIso.{u, v, w, w', uκ} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] [L.IsRelational] {κ : Type uκ}
  (cN : TauCeti.IndexCoding N κ) (h : TauCeti.InfEquivAt κ M N) : TauCeti.PotentialIso M N
```

**Karp's theorem, forward direction.** Formalized in Tau Ceti as [`TauCeti.PotentialIso.infEquivAt`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.PotentialIso.infEquivAt).

```lean
TauCeti.PotentialIso.infEquivAt.{u, v, w, w', uκ} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] [L.IsRelational] (h : TauCeti.PotentialIso M N)
  (κ : Type uκ) : TauCeti.InfEquivAt κ M N
```

## Sources

- [Tau Ceti documentation: `TauCeti.karp_theorem`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem)
- [Source of `TauCeti.karp_theorem` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/BackAndForth/Karp.lean#L346)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
