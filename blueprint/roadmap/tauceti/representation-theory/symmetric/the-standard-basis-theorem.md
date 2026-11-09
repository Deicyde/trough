---
declaration: def
origin: cited
lean: TauCeti.standardPolytabloidBasis
statement: formalized
---

# The standard basis theorem

The polytabloids of the standard `μ`-tableaux are a basis of
the Specht module `S^μ`: they are linearly independent by
`TauCeti.linearIndependent_polytabloid` and they span by
`TauCeti.spechtSubrepresentation_eq_span_standard`.

```lean
TauCeti.standardPolytabloidBasis (μ : YoungDiagram) :
  Module.Basis (TauCeti.StandardYoungTableau μ) ℚ ↥(TauCeti.spechtSubrepresentation μ).toSubmodule
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.standardPolytabloidBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Specht/StandardBasis.html#TauCeti.standardPolytabloidBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.standardPolytabloidBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Specht/StandardBasis.html#TauCeti.standardPolytabloidBasis)
- [Source of `TauCeti.standardPolytabloidBasis` in TauCeti/RepresentationTheory/Symmetric/Specht/StandardBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Symmetric/Specht/StandardBasis.lean#L336)
