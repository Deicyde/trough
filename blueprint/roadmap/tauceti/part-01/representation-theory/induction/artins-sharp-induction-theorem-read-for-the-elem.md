---
declaration: theorem
origin: cited
lean: TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary
statement: formalized
proof: formalized
---

# Artin's sharp induction theorem, read for the elementary subgroups

Every cyclic subgroup
is elementary, so the sharp cyclic theorem gives the explicit multiplier `|G|` here too.

When `Nat.card G` vanishes in `k`, the multiple is zero; the intended nonvacuous content is the
characteristic-zero specialization.

This is *weaker* than Brauer's induction theorem, which asserts the same with multiplier `1`. By
`TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff`, Brauer's theorem is
equivalent to `1` being induced from the elementary subgroups, which is not proved here.

```lean
TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary.{u, v} {k : Type u}
  {G : Type v} [Field k] [Group G] [Finite G] {f : G → k} (hf : f ∈ TauCeti.virtualCharacters k G) :
  Nat.card G • f ∈ TauCeti.ClassFunction.indVirtualCharacters k G fun E => TauCeti.IsElementary ↥E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's induction theorem with its induced-character-span target](artins-induction-theorem-with-its-induced-charac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Artin/Basic.html#TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Artin/Basic.html#TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary)
- [Source of `TauCeti.ClassFunction.natCard_nsmul_mem_indVirtualCharacters_isElementary` in TauCeti/RepresentationTheory/Induction/Artin/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Artin/Basic.lean#L205)
