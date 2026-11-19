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
- [Source of `TauCeti.karp_theorem` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/BackAndForth/Karp.lean#L373)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
