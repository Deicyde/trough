---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self, TauCeti.ContCohomology.dualityMap0_bijective_of_bijective_discreteCoind, TauCeti.ContCohomology.dualityMap1_bijective_of_smul_eq_self, TauCeti.ContCohomology.dualityMap1_bijective_of_injective_discreteCoind, TauCeti.ContCohomology.dualityMap2_bijective_of_smul_eq_self, TauCeti.ContCohomology.dualityMap2_bijective_of_bijective_discreteCoind
statement: formalized
proof: formalized
---

# Tate's duality map `α₀` on a module with trivial action

Let `N` be a discrete `G`-module
with trivial action, `N ≃+ ZMod n` and `H²(G, N) ≃+ ZMod n`, on which `α₀`, `α₁` are bijective and
`α₂` is injective. Then `α₀ : H⁰(G, A) → Hom(H²(G, A'), H²(G, N))` is bijective for every finite
discrete `G`-module `A` killed by `n` on which `G` acts trivially.

```lean
TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self.{uG, uN, uA} {G : Type uG} [Group G]
  {N : Type uN} [AddCommGroup N] [DistribMulAction G N] {n : ℕ} [NeZero n]
  (hN : ∀ (g : G) (y : N), g • y = y) (e : N ≃+ ZMod n) [TopologicalSpace G] [IsTopologicalGroup G]
  [TopologicalSpace N] [DiscreteTopology N] [ContinuousSMul G N]
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n)
  (h₀ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G N N))
  (h₁ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G N N))
  (h₂ : Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G N N)) (A : Type uA)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (g : G) (a : A), g • a = a) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G A N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.html#TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self).

## Other forms

**Tate's duality map `α₀` through a normal subgroup of finite index.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap0_bijective_of_bijective_discreteCoind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/DimensionShifting.html#TauCeti.ContCohomology.dualityMap0_bijective_of_bijective_discreteCoind).

```lean
TauCeti.ContCohomology.dualityMap0_bijective_of_bijective_discreteCoind.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] {V : Subgroup G} [V.Normal]
  [V.FiniteIndex] {N : Type u} [AddCommGroup N] [TopologicalSpace N] [DiscreteTopology N]
  [DistribMulAction G N] [ContinuousSMul G N] {n : ℕ} [NeZero n] (e : N ≃+ ZMod n)
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n) (hN : ∀ v ∈ V, ∀ (y : N), v • y = y)
  (hcoind :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A] [DiscreteTopology A]
      [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [inst_5 : Finite A],
      (∀ (a : A), n • a = 0) →
        (∀ v ∈ V, ∀ (a : A), v • a = a) →
          Function.Bijective
              ⇑(TauCeti.ContCohomology.dualityMap0 G (TauCeti.DiscreteCoind G V A) N) ∧
            Function.Bijective
                ⇑(TauCeti.ContCohomology.dualityMap1 G (TauCeti.DiscreteCoind G V A) N) ∧
              Function.Injective
                ⇑(TauCeti.ContCohomology.dualityMap2 G (TauCeti.DiscreteCoind G V A) N))
  (A : Type u) [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAV : ∀ v ∈ V, ∀ (a : A), v • a = a) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G A N)
```

**Tate's duality map `α₁` on a module with trivial action.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap1_bijective_of_smul_eq_self`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.html#TauCeti.ContCohomology.dualityMap1_bijective_of_smul_eq_self).

```lean
TauCeti.ContCohomology.dualityMap1_bijective_of_smul_eq_self.{uG, uN, uA} {G : Type uG} [Group G]
  {N : Type uN} [AddCommGroup N] [DistribMulAction G N] {n : ℕ} [NeZero n]
  (hN : ∀ (g : G) (y : N), g • y = y) (e : N ≃+ ZMod n) [TopologicalSpace G] [IsTopologicalGroup G]
  [TopologicalSpace N] [DiscreteTopology N] [ContinuousSMul G N]
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n)
  (h₀ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G N N))
  (h₁ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G N N))
  (h₂ : Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G N N)) (A : Type uA)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (g : G) (a : A), g • a = a) [Finite (TauCeti.ContCohomology.H1 G N)] :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G A N)
```

**Tate's duality map `α₁` through a normal subgroup of finite index.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap1_bijective_of_injective_discreteCoind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/DimensionShifting.html#TauCeti.ContCohomology.dualityMap1_bijective_of_injective_discreteCoind).

```lean
TauCeti.ContCohomology.dualityMap1_bijective_of_injective_discreteCoind.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] {V : Subgroup G} [V.Normal]
  [V.FiniteIndex] {N : Type u} [AddCommGroup N] [TopologicalSpace N] [DiscreteTopology N]
  [DistribMulAction G N] [ContinuousSMul G N] {n : ℕ} [NeZero n] (e : N ≃+ ZMod n)
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n) (hN : ∀ v ∈ V, ∀ (y : N), v • y = y)
  (hcoind₁ :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A] [DiscreteTopology A]
      [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [inst_5 : Finite A],
      (∀ (a : A), n • a = 0) →
        (∀ v ∈ V, ∀ (a : A), v • a = a) →
          Function.Bijective
              ⇑(TauCeti.ContCohomology.dualityMap0 G (TauCeti.DiscreteCoind G V A) N) ∧
            Function.Injective
              ⇑(TauCeti.ContCohomology.dualityMap1 G (TauCeti.DiscreteCoind G V A) N))
  (A : Type u) [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0) (hAV : ∀ v ∈ V, ∀ (a : A), v • a = a)
  [Finite (TauCeti.ContCohomology.H1 G (TauCeti.InternalHom G A N))] :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G A N)
```

**Tate's duality map `α₂` on a module with trivial action.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap2_bijective_of_smul_eq_self`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.html#TauCeti.ContCohomology.dualityMap2_bijective_of_smul_eq_self).

```lean
TauCeti.ContCohomology.dualityMap2_bijective_of_smul_eq_self.{uG, uN, uA} {G : Type uG} [Group G]
  {N : Type uN} [AddCommGroup N] [DistribMulAction G N] {n : ℕ} [NeZero n]
  (hN : ∀ (g : G) (y : N), g • y = y) (e : N ≃+ ZMod n) [TopologicalSpace G] [IsTopologicalGroup G]
  [TopologicalSpace N] [DiscreteTopology N] [ContinuousSMul G N]
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n)
  (h₀ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G N N))
  (h₁ : Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G N N))
  (h₂ : Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G N N)) (A : Type uA)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (g : G) (a : A), g • a = a) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 G A N)
```

**Tate's duality map `α₂` through a normal subgroup of finite index.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap2_bijective_of_bijective_discreteCoind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/DimensionShifting.html#TauCeti.ContCohomology.dualityMap2_bijective_of_bijective_discreteCoind).

```lean
TauCeti.ContCohomology.dualityMap2_bijective_of_bijective_discreteCoind.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] {V : Subgroup G} [V.Normal]
  [V.FiniteIndex] {N : Type u} [AddCommGroup N] [TopologicalSpace N] [DiscreteTopology N]
  [DistribMulAction G N] [ContinuousSMul G N] {n : ℕ} [NeZero n] (e : N ≃+ ZMod n)
  (e₂ : TauCeti.ContCohomology.H2 G N ≃+ ZMod n) (hN : ∀ v ∈ V, ∀ (y : N), v • y = y)
  (hcoind :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A] [DiscreteTopology A]
      [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [inst_5 : Finite A],
      (∀ (a : A), n • a = 0) →
        (∀ v ∈ V, ∀ (a : A), v • a = a) →
          Function.Bijective
              ⇑(TauCeti.ContCohomology.dualityMap0 G (TauCeti.DiscreteCoind G V A) N) ∧
            Function.Bijective
                ⇑(TauCeti.ContCohomology.dualityMap1 G (TauCeti.DiscreteCoind G V A) N) ∧
              Function.Injective
                ⇑(TauCeti.ContCohomology.dualityMap2 G (TauCeti.DiscreteCoind G V A) N))
  (A : Type u) [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction G A]
  [ContinuousSMul G A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAV : ∀ v ∈ V, ∀ (a : A), v • a = a) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 G A N)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.html#TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self)
- [Source of `TauCeti.ContCohomology.dualityMap0_bijective_of_smul_eq_self` in TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/TrivialAction.lean#L295)
