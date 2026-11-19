---
declaration: theorem
origin: cited
lean: FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_𝔾ₐ
statement: formalized
proof: formalized
---

# Formal group laws of infinite height are the additive ones

Over a field `K` of
characteristic `p`, a commutative formal group law has height `⊤` exactly when it is isomorphic
to the additive formal group law.

```lean
FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_𝔾ₐ.{u_2} {K : Type u_2} [Field K] {p : ℕ}
  [hp : Fact (Nat.Prime p)] [CharP K p] (F : FormalGroup K) [F.IsComm] :
  F.height p = ⊤ ↔ Nonempty (TauCeti.FormalGroupIso F FormalGroup.𝔾ₐ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_𝔾ₐ`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Logarithm/InfiniteHeight.html#FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_%F0%9D%94%BE%E2%82%90).

## Sources

- [Tau Ceti documentation: `FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_𝔾ₐ`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Logarithm/InfiniteHeight.html#FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_%F0%9D%94%BE%E2%82%90)
- [Source of `FormalGroup.height_eq_top_iff_nonempty_formalGroupIso_𝔾ₐ` in TauCeti/RingTheory/FormalGroup/Logarithm/InfiniteHeight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Logarithm/InfiniteHeight.lean#L236)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
