---
declaration: theorem
origin: cited
lean: TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff
statement: formalized
proof: formalized
---

# An induction theorem is a single membership

The virtual characters induced from a family
of subgroups exhaust `R(G)` exactly when the constant function `1`, the character of the trivial
representation, is one of them.

Brauer's induction theorem is this statement for the elementary subgroups, and its whole content is
therefore the membership `1 ∈ V_G`.

```lean
TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff.{u, v} {k : Type u} {G : Type v}
  [Field k] [Group G] [Finite G] {P : Subgroup G → Prop} :
  TauCeti.ClassFunction.indVirtualCharacters k G P = TauCeti.virtualCharacters k G ↔
    1 ∈ TauCeti.ClassFunction.indVirtualCharacters k G P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff)
- [Source of `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff` in TauCeti/RepresentationTheory/Induction/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Ideal.lean#L378)
