---
declaration: section
origin: cited
lean: _root_.PIndependent, _root_.PBasis, exists_pBasis_extending, exists_pBasis, pIndependent_iff_linearIndependent_differentials, pBasis_iff_basis_differentials, intersection_subfields_07P3, iInf_ker_kaehlerDifferentialMap_eq_bot_and_frobeniusFieldRange_eq_iInf
statement: formalized
proof: formalized
---

# 15.47 Field extensions, revisited

Section 15.47 of the Stacks Project, [Tag 07P0](https://stacks.math.columbia.edu/tag/07P0). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07P1, a definition

[Tag 07P1](https://stacks.math.columbia.edu/tag/07P1) in the Stacks Project.

Declarations registered for the tag:

- [`_root_.PIndependent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.PIndependent#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/PBasisDifferentials.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasisDifferentials.lean#L121) (StacksFrontier): “p-independent families”.
- [`_root_.PBasis`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.PBasis#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/PBasisDifferentials.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasisDifferentials.lean#L125) (StacksFrontier): “p-bases”.

## Tag 07P2, a lemma

[Tag 07P2](https://stacks.math.columbia.edu/tag/07P2) in the Stacks Project.

**`exists_pBasis_extending`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasis.lean, line 1319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasis.lean#L1319). The attribute's comment: “extension to p-basis”. References: EGA 0 (21.4.2), “more general”.

> **Stacks 07P2** (extension to p-basis).
> Every `p`-independent family `{x_i}` over `k` extends to a `p`-basis: there is a subset `S ⊆ K`
> containing the range of `x` whose inclusion `S → K` is a `p`-basis of `K` over `k`.

```lean
theorem exists_pBasis_extending
    {I : Type*} (x : I → K) (p : ℕ) [hp : Fact (Nat.Prime p)] [CharP K p]
    (hx : PIndependent k x p) :
    ∃ S : Set K, Set.range x ⊆ S ∧ PBasis k (Subtype.val : S → K) p
```

**`exists_pBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasis.lean, line 1341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasis.lean#L1341). The attribute's comment: “existence of p-basis”. References: EGA 0 (21.4.2).

> **Stacks 07P2** (existence of p-basis).
> There is a subset of `K` that is a `p`-basis of `K` over `k`.

```lean
theorem exists_pBasis (p : ℕ) [hp : Fact (Nat.Prime p)] [CharP K p] :
    ∃ S : Set K, PBasis k (Subtype.val : S → K) p
```

**`pIndependent_iff_linearIndependent_differentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasis.lean, line 1368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasis.lean#L1368). The attribute's comment: “(1)<=>(2)”. References: EGA 0 (21.2.4), “partial”; EGA 0 (21.2.5), “partial”; EGA 0 (21.4.5); EGA 0 (21.4.6), “(b) ⇔ (c)”.

> **Stacks 07P2** ((1)<=>(2)).
> For a family `x : I → K`, the elements `{x_i}` are `p`-independent over `k` if and only if the
> differentials `{d x_i}` are `K`-linearly independent in `Ω_{K/k}`.

```lean
theorem pIndependent_iff_linearIndependent_differentials
    {I : Type*} (x : I → K) (p : ℕ) [hp : Fact (Nat.Prime p)] [CharP K p] :
    PIndependent k x p ↔
      LinearIndependent K (fun i => (KaehlerDifferential.D k K) (x i))
```

**`pBasis_iff_basis_differentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasis.lean, line 1402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasis.lean#L1402). The attribute's comment: “(a)<=>(b)”. References: EGA 0 (21.4.5), “p-base case”; EGA 0 (21.1.7), “a)⇒c), special case”; EGA 0 (21.2.4), “special case”; EGA 0 (21.2.5), “special case”; EGA 0 (21.4.4), “more general”.

> **Stacks 07P2** ((a)<=>(b)).
> For a family `x : I → K`, the elements `{x_i}` form a `p`-basis of `K` over `k` if and only if the
> differentials `{d x_i}` form a `K`-basis of `Ω_{K/k}`.

```lean
theorem pBasis_iff_basis_differentials
    {I : Type*} (x : I → K) (p : ℕ) [hp : Fact (Nat.Prime p)] [CharP K p] :
    PBasis k x p ↔
      (LinearIndependent K (fun i => (KaehlerDifferential.D k K) (x i)) ∧
        ⊤ ≤ Submodule.span K
          (Set.range (fun i => (KaehlerDifferential.D k K) (x i))))
```

## Tag 07P3, a lemma

[Tag 07P3](https://stacks.math.columbia.edu/tag/07P3) in the Stacks Project.

**`intersection_subfields_07P3`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/DirectedSubfields.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/DirectedSubfields.lean#L171). References: EGA 0 (21.8.1).

> Let `K/k` be a field extension and `{K_α}_{α ∈ A}` a nonempty directed family of
> intermediate fields with intersection `k`. Then for every `n` and every `K`-subspace
> `V ⊆ K^{⊕n}`, `V` meets `k^{⊕n}` nontrivially iff `V` meets every `K_α^{⊕n}` nontrivially.
>
> Here:
> * `hinf : ⨅ α, Kα α = ⊥` encodes the condition `k = ⋂_α K_α` (the intermediate
>   field `⊥` is the copy of `k` in `K`);
> * `hdir : ∀ α α', ∃ α'', Kα α'' ≤ Kα α ⊓ Kα α'` encodes downward directedness of the family;
> * the condition `k ⊆ K_α` is automatic from `Kα α : IntermediateField k K`.

```lean
theorem intersection_subfields_07P3 {A : Type*} [Nonempty A]
    (Kα : A → IntermediateField k K)
    (hinf : ⨅ α, Kα α = ⊥)
    (hdir : ∀ α α', ∃ α'', Kα α'' ≤ Kα α ⊓ Kα α')
    (n : ℕ) (V : Submodule K (Fin n → K)) :
    NonzeroSubset ((V : Set (Fin n → K)) ∩ coordSubset n (⊥ : IntermediateField k K)) ↔
    ∀ α, NonzeroSubset ((V : Set (Fin n → K)) ∩ coordSubset n (Kα α))
```

## Tag 07P4, a lemma

[Tag 07P4](https://stacks.math.columbia.edu/tag/07P4) in the Stacks Project.

**`iInf_ker_kaehlerDifferentialMap_eq_bot_and_frobeniusFieldRange_eq_iInf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasisDifferentials.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasisDifferentials.lean#L631). References: EGA 0 (21.8.5), “k₀=K^p, L/K finite”; EGA 0 (21.8.3), “a) => c), k₀=F_p”.

> Let `Kα` be a downward-directed family of subfields of a field `K` of characteristic
> `p`, each containing the `p`-th powers, and suppose their intersection is exactly the subfield
> of `p`-th powers. Then the kernels of the canonical maps from `Ω[K/(ZMod p)]` to
> `Ω[K/(Kα α)]` have trivial intersection. Moreover, after any finite extension `L / K`,
> the intersection of the composita `L^p Kα` is `L^p`.

```lean
public theorem iInf_ker_kaehlerDifferentialMap_eq_bot_and_frobeniusFieldRange_eq_iInf
    {p : ℕ} [Fact p.Prime] {K : Type u} [Field K] [CharP K p] [Algebra (ZMod p) K]
    {A : Type v} (Kα : A → IntermediateField (ZMod p) K)
    (hpow : ∀ α, (frobenius K p).fieldRange ≤ (Kα α).toSubfield)
    (hiInf : (frobenius K p).fieldRange = ⨅ α, (Kα α).toSubfield)
    (hdir : ∀ α α', ∃ α'', Kα α'' ≤ Kα α ⊓ Kα α') :
    (⨅ α, LinearMap.ker (KaehlerDifferential.map (ZMod p) (Kα α) K K)) = ⊥ ∧
      ∀ (L : Type w) [Field L] [Algebra K L] [FiniteDimensional K L],
        letI : CharP L p :=
          charP_of_injective_algebraMap (algebraMap K L).injective p
        (frobenius L p).fieldRange =
          ⨅ α, (frobenius L p).fieldRange ⊔ (Kα α).toSubfield.map (algebraMap K L)
```

## Tag 07P5, a lemma

[Tag 07P5](https://stacks.math.columbia.edu/tag/07P5) in the Stacks Project.

**`fractionFields_powerSeries_polynomial_subrings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PBasisDifferentials.lean, line 1230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PBasisDifferentials.lean#L1230). References: EGA 0 (21.8.8), “∩K_J=K^p, A_J⊂A finite”.

> Let `x` be a p-basis of a field `k` of characteristic `p`. Inside
> `A = k[[X₁, ..., Xₙ]][Y₁, ..., Yₘ]`, let `AJ` be obtained by taking coefficients in the
> subfield generated by `k^p` and the `x i` for `i ∉ J`, and replacing every `X` and `Y` by
> its p-th power. The fraction fields of the `AJ` form a downward-directed family whose
> intersection is the p-th-power subfield and each `AJ ⊆ A` is finite.

```lean
public theorem fractionFields_powerSeries_polynomial_subrings
    {p : ℕ} [Fact p.Prime] {k : Type u} [Field k] [CharP k p]
    [Algebra (ZMod p) k] {I : Type v} (x : I → k)
    (hx : _root_.PBasis (ZMod p) x p) (n m : ℕ) :
    let kJ : Finset I → Subfield k := fun J =>
      (frobenius k p).fieldRange ⊔ Subfield.closure (x '' {i | i ∉ J})
    let A := MvPolynomial (Fin m) (MvPowerSeries (Fin n) k)
    letI : IsDomain A := NoZeroDivisors.to_isDomain A
    letI : CharP A p :=
      charP_of_injective_algebraMap (algebraMap k A).injective p
    let K := FractionRing A
    letI : CharP K p :=
      charP_of_injective_algebraMap (IsFractionRing.injective A K) p
    let toA : (J : Finset I) →
        MvPolynomial (Fin m) (MvPowerSeries (Fin n) ↥(kJ J)) →+* A := fun J =>
      MvPolynomial.eval₂Hom
        ((MvPolynomial.C : MvPowerSeries (Fin n) k →+* A).comp
          ((MvPowerSeries.expand p (Nat.Prime.ne_zero Fact.out)).toRingHom.comp
            (MvPowerSeries.map (kJ J).subtype)))
        (fun i => MvPolynomial.X i ^ p)
    let AJ : Finset I → Subring A := fun J => RingHom.range (toA J)
    let KJ : Finset I → IntermediateField (ZMod p) K := fun J =>
      IntermediateField.adjoin (ZMod p) ((algebraMap A K) '' (AJ J : Set A))
    (∀ J, (frobenius K p).fieldRange ≤ (KJ J).toSubfield) ∧
      (frobenius K p).fieldRange = ⨅ J, (KJ J).toSubfield ∧
      (∀ J J', ∃ J'', KJ J'' ≤ KJ J ⊓ KJ J') ∧
      ∀ J, Module.Finite (AJ J) A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.47, Tag 07P0](https://stacks.math.columbia.edu/tag/07P0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
