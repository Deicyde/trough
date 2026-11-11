---
declaration: theorem
origin: cited
lean: TauCeti.groupCohomology.isZero_of_isZero_sylow
statement: formalized
proof: formalized
---

# The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)

if,
for every prime `p` dividing the order of `G`, `Hⁿ⁺¹(P, A) = 0` for some Sylow `p`-subgroup `P`,
then `Hⁿ⁺¹(G, A) = 0`.

```lean
TauCeti.groupCohomology.isZero_of_isZero_sylow.{u} {k G : Type u} [CommRing k] [Group G] [Finite G]
  (A : Rep.{u, u, u} k G) (n : ℕ)
  (h :
    ∀ (p : ℕ) [Fact (Nat.Prime p)],
      p ∣ Nat.card G →
        ∃ P, CategoryTheory.Limits.IsZero (groupCohomology (Rep.res (↑P).subtype A) (n + 1))) :
  CategoryTheory.Limits.IsZero (groupCohomology A (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](restriction-through-shapiros-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.isZero_of_isZero_sylow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Sylow.html#TauCeti.groupCohomology.isZero_of_isZero_sylow).

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.isZero_of_isZero_sylow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Sylow.html#TauCeti.groupCohomology.isZero_of_isZero_sylow)
- [Source of `TauCeti.groupCohomology.isZero_of_isZero_sylow` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Sylow.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/GroupCohomology/Sylow.lean#L96)
