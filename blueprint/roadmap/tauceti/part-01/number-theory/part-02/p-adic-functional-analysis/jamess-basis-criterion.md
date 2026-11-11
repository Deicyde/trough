---
declaration: theorem
origin: cited
lean: SchauderBasis.surjective_inclusionInDoubleDual_iff
statement: formalized
proof: formalized
---

# James's basis criterion

A Banach space with a Schauder basis is reflexive
if and only if that basis is shrinking and boundedly complete.

```lean
SchauderBasis.surjective_inclusionInDoubleDual_iff.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] (b : SchauderBasis 𝕜 E) [CompleteSpace E] :
  Function.Surjective ⇑(NormedSpace.inclusionInDoubleDual 𝕜 E) ↔
    b.IsShrinking ∧ b.IsBoundedlyComplete
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SchauderBasis.surjective_inclusionInDoubleDual_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Reflexive.html#SchauderBasis.surjective_inclusionInDoubleDual_iff).

## Sources

- [Tau Ceti documentation: `SchauderBasis.surjective_inclusionInDoubleDual_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Reflexive.html#SchauderBasis.surjective_inclusionInDoubleDual_iff)
- [Source of `SchauderBasis.surjective_inclusionInDoubleDual_iff` in TauCeti/Analysis/Normed/Module/Bases/Reflexive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Bases/Reflexive.lean#L171)
