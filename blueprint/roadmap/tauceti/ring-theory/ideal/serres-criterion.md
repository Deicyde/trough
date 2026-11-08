---
declaration: theorem
origin: cited
lean: TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top, TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top, TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two
statement: formalized
proof: formalized
---

# Serre's criterion

When `S` is generated over `R` by a set `s` and `G` acts by `R`-algebra
automorphisms, membership in the inertia subgroup of a two-sided ideal `I` is decided on `s` alone:
the elements moved into `I` form an `R`-subalgebra.

```lean
TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top.{u_1, u_2, u_3} {G : Type u_1} [Group G]
  {S : Type u_2} [Ring S] [MulSemiringAction G S] {R : Type u_3} [CommSemiring R] [Algebra R S]
  [SMulCommClass G R S] {I : Ideal S} [I.IsTwoSided] {s : Set S} (hs : Algebra.adjoin R s = ⊤)
  {σ : G} : σ ∈ Ideal.inertia G I ↔ ∀ x ∈ s, σ • x - x ∈ I
```

## Depends on

- [Module.SatisfiesSerreS](../scheme-stack-cohomology-and-intersection-foundat/module-satisfiesserres.md)
- [Ring.SatisfiesSerreR](../scheme-stack-cohomology-and-intersection-foundat/ring-satisfiesserrer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/Inertia.html#TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top).

## Other forms

**Serre's criterion for the ramification filtration.** Formalized in Tau Ceti as [`TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/RamificationGroup.html#TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top).

```lean
TauCeti.IsLocalRing.mem_ramificationGroup_iff_of_adjoin_eq_top.{u_1, u_2, u_3} {G : Type u_1}
  [Group G] {S : Type u_2} [CommRing S] [IsLocalRing S] [MulSemiringAction G S] {R : Type u_3}
  [CommSemiring R] [Algebra R S] [SMulCommClass G R S] {s : Set S} (hs : Algebra.adjoin R s = ⊤)
  {i : ℤ} {σ : G} :
  σ ∈ TauCeti.IsLocalRing.ramificationGroup G S i ↔
    ∀ x ∈ s, σ • x - x ∈ IsLocalRing.maximalIdeal S ^ (i + 1).toNat
```

**Serre's criterion for normality.** Formalized in Tau Ceti as [`TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Normal.html#TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two).

```lean
TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two.{u}
  {R : Type u} [CommRing R] [IsNoetherianRing R] :
  (∀ (p : Ideal R) [inst : p.IsPrime],
      IsDomain (Localization.AtPrime p) ∧ IsIntegrallyClosed (Localization.AtPrime p)) ↔
    Ring.SatisfiesSerreR 1 R ∧ Module.SatisfiesSerreS 2 R R
```

## Sources

- [Tau Ceti documentation: `TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/Inertia.html#TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top)
- [Source of `TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top` in TauCeti/RingTheory/Ideal/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Ideal/Inertia.lean#L44)
