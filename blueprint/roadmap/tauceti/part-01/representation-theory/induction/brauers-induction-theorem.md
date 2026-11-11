---
declaration: theorem
origin: cited
lean: TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary, TauCeti.ClassFunction.character_mem_indCharacterSpanInt_isElementary
statement: formalized
proof: formalized
---

# Brauer's induction theorem

Over an algebraically closed field of characteristic zero,
every virtual character of a finite group is an integral combination of virtual characters
induced from elementary subgroups.

```lean
TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary.{u, v} {k : Type u}
  {G : Type v} [Field k] [Group G] [Finite G] [CharZero k] [IsAlgClosed k] :
  (TauCeti.ClassFunction.indVirtualCharacters k G fun E => TauCeti.IsElementary ↥E) =
    TauCeti.virtualCharacters k G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [An induction theorem, one prime at a time and with coefficients in a subring](an-induction-theorem-one-prime-at-a-time-and-wit.md)
- [Brauer's local lemma](brauers-local-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Brauer/Induction.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary).

## Other forms

**Brauer's induction theorem, character form.** Formalized in Tau Ceti as [`TauCeti.ClassFunction.character_mem_indCharacterSpanInt_isElementary`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Brauer/Induction.html#TauCeti.ClassFunction.character_mem_indCharacterSpanInt_isElementary).

```lean
TauCeti.ClassFunction.character_mem_indCharacterSpanInt_isElementary.{u, v} {k : Type u}
  {G : Type v} [Field k] [Group G] [Finite G] [CharZero k] [IsAlgClosed k] (V : FDRep k G) :
  V.character ∈ TauCeti.ClassFunction.indCharacterSpanInt k G fun E => TauCeti.IsElementary ↥E
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Brauer/Induction.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary)
- [Source of `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_isElementary` in TauCeti/RepresentationTheory/Induction/Brauer/Induction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Brauer/Induction.lean#L79)
