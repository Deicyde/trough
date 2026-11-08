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

- [FormalGroup.height](formalgroup-height.md)
- [TauCeti.FormalGroupIso](tauceti-formalgroupiso.md)

## Proof depends on

- [The `p`-series has order a power of `p` in characteristic `p`](the-p-series-has-order-a-power-of-p-in-character.md)
- [FormalGroup.TopNilpotentPoint](formalgroup-topnilpotentpoint.md)
- [Nakayama's lemma over `ℤ`](../other-results/part-01/nakayamas-lemma-over-z.md)
- [TauCeti.FormalCoordinate](../formal-laurent-fields-puiseux-expansions-and-con/tauceti-formalcoordinate.md)
- [TauCeti.FormalGroupHom](tauceti-formalgrouphom.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.height_eq_height_iff_nonempty_formalGroupIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Classification.html#FormalGroup.height_eq_height_iff_nonempty_formalGroupIso).

## Sources

- [Tau Ceti documentation: `FormalGroup.height_eq_height_iff_nonempty_formalGroupIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Classification.html#FormalGroup.height_eq_height_iff_nonempty_formalGroupIso)
- [Source of `FormalGroup.height_eq_height_iff_nonempty_formalGroupIso` in TauCeti/RingTheory/FormalGroup/Height/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Height/Classification.lean#L425)
