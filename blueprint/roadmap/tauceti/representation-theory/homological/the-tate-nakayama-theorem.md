---
declaration: theorem
origin: cited
lean: TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective
statement: formalized
proof: formalized
---

# The Tate–Nakayama theorem

**The Tate–Nakayama theorem** (Nakayama, Ann. of Math. 65 (1957); Serre, *Local Fields*, IX §8).
Let `G` be a finite group, `C` a representation of `G` over `ℤ` and `u ∈ H²(G, C)`.
Suppose that for every subgroup `S` of `G` of prime-power order

* `H¹(S, C) = 0`,
* the restriction of `u` generates `H²(S, C)`, and
* `H²(S, C)` has `|S|` elements.

Then for every representation `M` with `Tor₁^ℤ(M, C) = 0`, in the form that `M ⊗ X → M ⊗ Y` is
injective for every short exact sequence `0 → X → Y → C → 0` of abelian groups, cup product with
`u` is a bijection `H^r(G, M) → H^{r+2}(G, M ⊗ C)` in every integer degree `r`.

```lean
TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective {G : Type} [Group G]
  [Fintype G] (M C : Rep.{0, 0, 0} ℤ G) (u : ↑(groupCohomology C 2))
  (h1 :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G),
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (groupCohomology (Rep.res S.subtype C) 1))
  (hgen :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G),
      IsPGroup p ↥S →
        ∀ (x : ↑(groupCohomology (Rep.res S.subtype C) 2)),
          ∃ m,
            m •
                (CategoryTheory.ConcreteCategory.hom
                    (groupCohomology.map S.subtype
                      (CategoryTheory.CategoryStruct.id (Rep.res S.subtype C)) 2))
                  u =
              x)
  (hcard :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G),
      IsPGroup p ↥S → Nat.card ↑(groupCohomology (Rep.res S.subtype C) 2) = Nat.card ↥S)
  (hM :
    ∀ {X Y : Type} [inst : AddCommGroup X] [inst_1 : _root_.Module ℤ X] [inst_2 : AddCommGroup Y]
      [inst_3 : _root_.Module ℤ Y] (f : X →ₗ[ℤ] Y) (g : Y →ₗ[ℤ] ↑C),
      Function.Injective ⇑f →
        Function.Exact ⇑f ⇑g →
          Function.Surjective ⇑g → Function.Injective ⇑(LinearMap.lTensor (↑M) f))
  (r r' : ℤ) (h : r + 2 = r') :
  Function.Bijective fun x =>
    ((TauCeti.TateCohomology.cup M C r 2 r' h) x)
      ((CategoryTheory.ConcreteCategory.hom ((TateCohomology.isoGroupCohomology 2).app C).inv) u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](corestriction-through-shapiros-lemma.md)
- [Nakayama–Rim, Sylow form](nakayama-rim-sylow-form.md)
- [Restriction through Shapiro's lemma](restriction-through-shapiros-lemma.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](tates-cohomological-triviality-criterion-milne-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateNakayama.html#TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateNakayama.html#TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective)
- [Source of `TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup_of_lTensor_injective` in TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateNakayama.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateNakayama.lean#L349)
