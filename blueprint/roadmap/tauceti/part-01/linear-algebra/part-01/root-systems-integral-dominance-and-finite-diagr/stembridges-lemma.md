---
declaration: theorem
origin: cited
lean: RootPairing.stembridge_step
statement: formalized
proof: formalized
---

# Stembridge's lemma

Let `lam` and `mu` be distinct dominant weights with `mu - lam` in
the positive root cone `Q⁺`. Then there is a positive root `β` such that `lam + β` is dominant
and `mu - (lam + β)` is still in `Q⁺`.

Since `β` is a nonzero member of `Q⁺` (`TauCeti.root_mem_posRootCone_of_mem_posRoots`), the step
strictly increases `lam` in the integral root order. Neither endpoint needs integral
simple-coroot values, and the roots need not span `M`. If `lam` lies in an additive subgroup
containing the roots, so does `lam + β`.

This is the inductive step of Rapoport, *A positivity property of the Satake isomorphism*,
Lemma 2.3, proved by Waldspurger's argument: `β` is a positive root of maximal height among those
whose simple-root coordinates are bounded by those of `mu - lam`.

```lean
RootPairing.stembridge_step.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [AddCommGroup M]
  [_root_.Module R M] [AddCommGroup N] [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι]
  [P.IsCrystallographic] (b : P.Base) {lam mu : M} (hlam : lam ∈ P.dominantChamber b)
  (hmu : mu ∈ P.dominantChamber b) (hne : lam ≠ mu) (hle : mu - lam ∈ TauCeti.posRootCone P b) :
  ∃ i,
    b.IsPos i ∧
      lam + P.root i ∈ P.dominantChamber b ∧ mu - (lam + P.root i) ∈ TauCeti.posRootCone P b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.stembridge_step`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Stembridge.html#RootPairing.stembridge_step).

## Sources

- [Tau Ceti documentation: `RootPairing.stembridge_step`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Stembridge.html#RootPairing.stembridge_step)
- [Source of `RootPairing.stembridge_step` in TauCeti/LinearAlgebra/RootSystem/Stembridge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Stembridge.lean#L55)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)
