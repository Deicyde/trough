---
declaration: theorem
origin: cited
lean: TauCeti.karp_theorem_at
statement: formalized
proof: formalized
---

# Karp's theorem at a common carrier

Structures in a relational language that are both
coded into `κ` are potentially isomorphic exactly when they satisfy the same infinitary sentences
with carrier `κ`.

```lean
TauCeti.karp_theorem_at.{u, v, w, w', uκ} {L : FirstOrder.Language} {M : Type w} {N : Type w'}
  [L.Structure M] [L.Structure N] [L.IsRelational] {κ : Type uκ} (cM : TauCeti.IndexCoding M κ)
  (cN : TauCeti.IndexCoding N κ) : TauCeti.PotentialIso M N ↔ TauCeti.InfEquivAt κ M N
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Proof depends on

- [Back-and-forth equivalence at level `α` gives agreement up to quantifier rank `α`](back-and-forth-equivalence-at-level-gives-agreem.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.karp_theorem_at`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem_at).

## Sources

- [Tau Ceti documentation: `TauCeti.karp_theorem_at`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem_at)
- [Source of `TauCeti.karp_theorem_at` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/Karp.lean#L302)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
