---
declaration: section
origin: cited
lean: KaehlerDifferential.deRhamDifferential_comp_self, KaehlerDifferential.deRhamDifferential_comp_deRhamDifferential, Stacks.DeRham.DifferentialDescent.sourceDeRham, KaehlerDifferential.deRhamComplex, KaehlerDifferential.deRhamDifferential, KaehlerDifferential.deRhamDifferential_smul_ιMulti_D, KaehlerDifferential.deRhamDifferential_unique, KaehlerDifferential.isBaseChange_exteriorPower_and_deRhamDifferential_comm
statement: formalized
proof: formalized
---

# 10.132 The de Rham complex

Section 10.132 of the Stacks Project, [Tag 0FKF](https://stacks.math.columbia.edu/tag/0FKF). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FKF, the section

[Tag 0FKF](https://stacks.math.columbia.edu/tag/0FKF) in the Stacks Project.

**`KaehlerDifferential.deRhamDifferential_comp_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L720). The attribute's comment: “the complex property d ∘ d = 0 of the de Rham complex of a ring map, on the exterior powers of the Kaehler differentials”.

> **The de Rham differential of `B` over `A` squares to zero.**  The elements
> `b₀ · (d b₁ ∧ ⋯ ∧ d b_p)` span `Ω^p_{B/A}` over `A`, and on such an element the defining rule
> computes the composite as a wedge whose first factor is `d 1 = 0`.

```lean
public theorem deRhamDifferential_comp_self (p : ℕ) (ξ : ⋀[B]^p (Ω[B⁄A])) :
    deRhamDifferential (A := A) (p + 1) (deRhamDifferential p ξ) = 0
```

**`KaehlerDifferential.deRhamDifferential_comp_deRhamDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L738). The attribute's comment: “the complex property d ∘ d = 0 of the de Rham complex of a ring map, as an equality of A-linear maps”.

> **Consecutive de Rham differentials compose to zero**, as an equality of `A`-linear maps.
> This is the complex property of the de Rham complex of `B` over `A`.

```lean
public theorem deRhamDifferential_comp_deRhamDifferential (p : ℕ) :
    (deRhamDifferential (A := A) (B := B) (p + 1)).comp (deRhamDifferential p) = 0
```

**`Stacks.DeRham.DifferentialDescent.sourceDeRham`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L1087). The attribute's comment: “the de Rham complex of a ring map A → B, as the family of A-linear differentials on the exterior powers of the Kaehler differentials together with the defining rule on generators and the complex property d ∘ d = 0; this construction has no hypothesis”.

> **The de Rham complex of `B` over `A`**, as a term of `SourceDeRham A B`: the de Rham
> differentials `KaehlerDifferential.deRhamDifferential` on the exterior powers of `Ω[B⁄A]`, which
> obey the defining rule on generators by
> `KaehlerDifferential.deRhamDifferential_smul_ιMulti_D`.  Nothing is supposed: the descent datum
> of Tag 07HY is produced here, and its complex property is the theorem
> `KaehlerDifferential.deRhamDifferential_comp_deRhamDifferential`, reached through the default
> value of the field `complex`.

```lean
noncomputable def sourceDeRham (A B : Type u) [CommRing A] [CommRing B] [Algebra A B] :
    SourceDeRham A B
```

**`KaehlerDifferential.deRhamComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Complex.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Complex.lean#L77). The attribute's comment: “the de Rham complex Ω^0\_\{B/A} → Ω^1\_\{B/A} → ⋯ of a ring map A → B, as a CochainComplex of A-modules indexed by ℕ; the construction has no hypothesis”.

> The de Rham complex `Ω^0_{B/A} → Ω^1_{B/A} → Ω^2_{B/A} → ⋯` of `B` over `A`: the exterior
> powers of `Ω[B⁄A]`, as `A`-modules, with the de Rham differentials as its arrows.  The
> construction has no hypothesis — the arrows are `deRhamDifferential` and the square-zero
> condition is `deRhamDifferential_comp_deRhamDifferential`.

```lean
public noncomputable def deRhamComplex (A B : Type u) [CommRing A] [CommRing B]
    [Algebra A B] : CochainComplex (ModuleCat.{u} A) ℕ
```

## Tag 0FKG, an equation

[Tag 0FKG](https://stacks.math.columbia.edu/tag/0FKG) in the Stacks Project.

**`KaehlerDifferential.deRhamDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L667). The attribute's comment: “the differential itself”.

> The de Rham differential `d : Ω^p_{B/A} → Ω^{p+1}_{B/A}` in degree `p`: the `A`-linear map
> with `d (b₀ · d b₁ ∧ ⋯ ∧ d b_p) = d b₀ ∧ d b₁ ∧ ⋯ ∧ d b_p` for all `b₀, …, b_p ∈ B`, where
> `d : B → Ω[B⁄A]` is the universal `A`-derivation.  That rule is
> `deRhamDifferential_smul_ιMulti_D` and `deRhamDifferential_unique` says it pins the map down.

```lean
public noncomputable def deRhamDifferential (p : ℕ) :
    ⋀[B]^p (Ω[B⁄A]) →ₗ[A] ⋀[B]^(p + 1) (Ω[B⁄A])
```

**`KaehlerDifferential.deRhamDifferential_smul_ιMulti_D`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 678](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L678). The attribute's comment: “the defining rule of `deRhamDifferential`”.

> The defining rule of the de Rham differential:
> `d (b₀ · d b₁ ∧ ⋯ ∧ d b_p) = d b₀ ∧ d b₁ ∧ ⋯ ∧ d b_p`.  The leading scalar `b₀` contributes the
> factor `d b₀` through `dp_apply_smul`, and `G_exact` kills the wedge of exact forms.

```lean
public lemma deRhamDifferential_smul_ιMulti_D (p : ℕ) (b : Fin (p + 1) → B) :
    deRhamDifferential p (b 0 • exteriorPower.ιMulti B p fun i ↦ D A B (b i.succ)) =
      exteriorPower.ιMulti B (p + 1) fun i ↦ D A B (b i)
```

**`KaehlerDifferential.deRhamDifferential_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L696). The attribute's comment: “uniqueness of `deRhamDifferential`”.

> `deRhamDifferential p` is the only `A`-linear map `Ω^p_{B/A} → Ω^{p+1}_{B/A}` with
> `d (b₀ · d b₁ ∧ ⋯ ∧ d b_p) = d b₀ ∧ d b₁ ∧ ⋯ ∧ d b_p`, because those elements span
> `Ω^p_{B/A}` over `A`.

```lean
public theorem deRhamDifferential_unique (p : ℕ)
    (d : ⋀[B]^p (Ω[B⁄A]) →ₗ[A] ⋀[B]^(p + 1) (Ω[B⁄A]))
    (hd : ∀ b : Fin (p + 1) → B,
      d (b 0 • exteriorPower.ιMulti B p fun i ↦ D A B (b i.succ)) =
        exteriorPower.ιMulti B (p + 1) fun i ↦ D A B (b i)) :
    d = deRhamDifferential p
```

## Tag 0H8Y, a lemma

[Tag 0H8Y](https://stacks.math.columbia.edu/tag/0H8Y) in the Stacks Project.

**`KaehlerDifferential.isBaseChange_exteriorPower_and_deRhamDifferential_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 962](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L962). References: EGA IV (16.6.4), “affine case”.

> **Stacks 0H8Y.** Let `A → A'` and `A → B` be ring maps, let `B' = B ⊗_A A'`, and let `ψ` be
> the canonical map `⋀^p (KaehlerDifferential.map A A' B B')`.  Then `ψ` exhibits
> `Ω^•_{B'/A'}` as the base change of `Ω^•_{B/A}` along `A → A'`, i.e.
> `Ω^•_{B/A} ⊗_A A' = Ω^•_{B'/A'}`, and it is a map of complexes for the de Rham differentials
> of `B` over `A` and of `B'` over `A'`.

```lean
public theorem isBaseChange_exteriorPower_and_deRhamDifferential_comm
    {A A' B B' : Type*} [CommRing A] [CommRing A'] [CommRing B] [CommRing B']
    [Algebra A A'] [Algebra A B] [Algebra A B'] [Algebra A' B'] [Algebra B B']
    [IsScalarTower A A' B'] [IsScalarTower A B B'] [Algebra.IsPushout A A' B B']
    (ψ : ∀ p : ℕ, ⋀[B]^p (Ω[B⁄A]) →ₗ[B] ⋀[B']^p (Ω[B'⁄A']))
    (hψ : ∀ (p : ℕ) (ω : Fin p → Ω[B⁄A]),
      ψ p (exteriorPower.ιMulti B p ω) =
        exteriorPower.ιMulti B' p fun i ↦ map A A' B B' (ω i)) :
    (∀ p : ℕ, IsBaseChange A' ((ψ p).restrictScalars A)) ∧
      ∀ (p : ℕ) (ω : ⋀[B]^p (Ω[B⁄A])), ψ (p + 1) (deRhamDifferential p ω) =
        deRhamDifferential (A := A') (B := B') p (ψ p ω)
```

## Tag 07HY, a lemma

[Tag 07HY](https://stacks.math.columbia.edu/tag/07HY) in the Stacks Project.

**`exists_unique_quotient_deRhamDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/Basic.lean, line 1842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/Basic.lean#L1842).

> **Stacks 07HY.** Let `S` be the de Rham complex of `B` over `A` and let
> `π : Ω[B⁄A] → Ω` be a surjection of `B`-modules whose kernel is generated by elements `ω` with
> `π ω = 0` and `(⋀^2 π) (d ω) = 0`.  Then there is exactly one family of `A`-linear maps
> `Ω^p = ⋀[B]^p Ω → Ω^{p+1}` making the squares `d ∘ (⋀^p π) = (⋀^{p+1} π) ∘ d_{B/A}` commute;
> it obeys the same rule `d (f₀ · d f₁ ∧ ⋯ ∧ d f_p) = d f₀ ∧ ⋯ ∧ d f_p` on generators, with
> `d f = π (d_{B/A} f)`, and it is again a complex.

```lean
theorem exists_unique_quotient_deRhamDifferential
    (S : SourceDeRham A B)
    {Ω : Type u} [AddCommGroup Ω] [Module B Ω] (π : Ω[B⁄A] →ₗ[B] Ω)
    (hπ : Function.Surjective π)
    (hgen : S.GenerationHypothesis π) :
    ∃ dΩ : (∀ p, TgtA A B Ω p →ₗ[A] TgtA A B Ω (p + 1)),
      S.Commutes π dΩ ∧
      SatisfiesRule π dΩ ∧
      (∀ dΩ' : (∀ p, TgtA A B Ω p →ₗ[A] TgtA A B Ω (p + 1)), S.Commutes π dΩ' → dΩ' = dΩ) ∧
      (∀ p, (dΩ (p + 1)).comp (dΩ p) = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.132, Tag 0FKF](https://stacks.math.columbia.edu/tag/0FKF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
