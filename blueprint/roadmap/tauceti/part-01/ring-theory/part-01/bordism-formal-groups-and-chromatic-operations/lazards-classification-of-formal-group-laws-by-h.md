---
declaration: theorem
origin: cited
lean: FormalGroup.height_eq_height_iff_nonempty_formalGroupIso
statement: formalized
proof: formalized
---

# Lazard's classification of formal group laws by height

Over a separably closed field `K`
of characteristic `p`, two commutative formal group laws are isomorphic exactly when they have the
same height. In height `⊤` both are isomorphic to the additive formal group law.

```lean
FormalGroup.height_eq_height_iff_nonempty_formalGroupIso.{u_1} {K : Type u_1} [Field K]
  [IsSepClosed K] {p : ℕ} [Fact (Nat.Prime p)] [CharP K p] (F G : FormalGroup K) [F.IsComm]
  [G.IsComm] : F.height p = G.height p ↔ Nonempty (TauCeti.FormalGroupIso F G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Formal group laws of infinite height are the additive ones](formal-group-laws-of-infinite-height-are-the-add.md)
- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.height_eq_height_iff_nonempty_formalGroupIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Classification.html#FormalGroup.height_eq_height_iff_nonempty_formalGroupIso).

## Sources

- [Tau Ceti documentation: `FormalGroup.height_eq_height_iff_nonempty_formalGroupIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Classification.html#FormalGroup.height_eq_height_iff_nonempty_formalGroupIso)
- [Source of `FormalGroup.height_eq_height_iff_nonempty_formalGroupIso` in TauCeti/RingTheory/FormalGroup/Height/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Height/Classification.lean#L468)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
