---
declaration: theorem
origin: cited
lean: TauCeti.spechtSubrepresentation_le_or_le_orthogonal
statement: formalized
proof: formalized
---

# James's submodule theorem

A subrepresentation `U` of the Young permutation module `M^μ`
either contains the Specht module `S^μ` or is orthogonal to it for the tabloid form.

The dichotomy is whether some column antisymmetrizer `b_t` fails to annihilate some vector of `U`.
If it does fail, the value is a nonzero multiple of the polytabloid `e_t` and lies in `U`, so `U`
contains the orbit of `e_t`, which spans `S^μ`.  If every `b_t` annihilates every vector of `U`,
then self-adjointness of `b_t` moves it off each polytabloid `e_t = b_t · {t}` and onto the vector
of `U`, where it vanishes.

```lean
TauCeti.spechtSubrepresentation_le_or_le_orthogonal (μ : YoungDiagram)
  (U : Subrepresentation (TauCeti.permutationModule (TauCeti.shapePartition μ)).ρ) :
  TauCeti.spechtSubrepresentation μ ≤ U ∨
    U ≤ TauCeti.orthogonalSubrepresentation (TauCeti.spechtSubrepresentation μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.spechtSubrepresentation_le_or_le_orthogonal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Specht/SubmoduleTheorem.html#TauCeti.spechtSubrepresentation_le_or_le_orthogonal).

## Sources

- [Tau Ceti documentation: `TauCeti.spechtSubrepresentation_le_or_le_orthogonal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Specht/SubmoduleTheorem.html#TauCeti.spechtSubrepresentation_le_or_le_orthogonal)
- [Source of `TauCeti.spechtSubrepresentation_le_or_le_orthogonal` in TauCeti/RepresentationTheory/Symmetric/Specht/SubmoduleTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Symmetric/Specht/SubmoduleTheorem.lean#L200)
