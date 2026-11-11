---
declaration: theorem
origin: cited
lean: TauCeti.finitelyRepresentable_doubleDual
statement: formalized
proof: formalized
---

# TauCeti.finitelyRepresentable_doubleDual

The bidual of a normed space is finitely representable in the space.

```lean
TauCeti.finitelyRepresentable_doubleDual.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] :
  TauCeti.FinitelyRepresentable 𝕜 (StrongDual 𝕜 (StrongDual 𝕜 E)) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The principle of local reflexivity](the-principle-of-local-reflexivity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finitelyRepresentable_doubleDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.html#TauCeti.finitelyRepresentable_doubleDual).

## Sources

- [Tau Ceti documentation: `TauCeti.finitelyRepresentable_doubleDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.html#TauCeti.finitelyRepresentable_doubleDual)
- [Source of `TauCeti.finitelyRepresentable_doubleDual` in TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.lean#L332)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
