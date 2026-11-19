---
declaration: theorem
origin: cited
lean: TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty
statement: formalized
proof: formalized
---

# Every perfectoid Tate ring has a pseudouniformiser with compatible `p`-power roots (Scholze, *Étale cohomology of diamonds*, Lemma 3.10)

```lean
TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty.{u_1} {p : ℕ} [Fact (Nat.Prime p)] {R : Type u_1}
  [CommRing R] [UniformSpace R] [IsUniformAddGroup R] [IsTopologicalRing R] [CompleteSpace R]
  [T2Space R] [TauCeti.Huber.IsTateRing R] [TauCeti.Perfectoid.IsPerfectoidTateRing p R] :
  Nonempty (TauCeti.Perfectoid.PseudoUniformizerRoots p R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/PseudoUniformizerRoots/Existence.html#TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/PseudoUniformizerRoots/Existence.html#TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty)
- [Source of `TauCeti.Perfectoid.PseudoUniformizerRoots.nonempty` in TauCeti/RingTheory/Perfectoid/PseudoUniformizerRoots/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/PseudoUniformizerRoots/Existence.lean#L143)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
