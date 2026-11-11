---
declaration: theorem
origin: cited
lean: TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top
statement: formalized
proof: formalized
---

# Serre's criterion for the ramification filtration

when `S` is generated over `R` by a set
`s` and `G` acts by `R`-algebra automorphisms, membership in `G_i` is decided on `s` alone. This
is `TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top` at a power of the maximal ideal.

```lean
TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top.{u_1, u_2, u_3} {G : Type u_1}
  [Group G] {S : Type u_2} [CommRing S] [IsLocalRing S] [MulSemiringAction G S] {R : Type u_3}
  [CommSemiring R] [Algebra R S] [SMulCommClass G R S] {s : Set S} (hs : Algebra.adjoin R s = ⊤)
  {i : ℤ} {σ : G} :
  σ ∈ TauCeti.IsLocalRing.ramificationGroup G S i ↔
    ∀ x ∈ s, σ • x - x ∈ IsLocalRing.maximalIdeal S ^ (i + 1).toNat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's criterion](../ideal/serres-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/RamificationGroup.html#TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/RamificationGroup.html#TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top)
- [Source of `TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top` in TauCeti/RingTheory/LocalRing/RamificationGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LocalRing/RamificationGroup.lean#L195)
