---
declaration: section
origin: cited
lean: IsLocalHom, IsLocalRing, IsLocalRing.maximal_ideal_unique, IsLocalRing.maximalIdeal, IsLocalRing.ResidueField, IsLocalRing.residue, not_isLocalHom_algebraMap_atPrime, isLocalRing_iff_exists_maximal_isUnit
statement: formalized
proof: formalized
---

# 10.18 Local rings

Section 10.18 of the Stacks Project, [Tag 07BH](https://stacks.math.columbia.edu/tag/07BH). 4 tags here are carried by 5 declarations of the repository (all in StacksCore) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07BI, a definition

[Tag 07BI](https://stacks.math.columbia.edu/tag/07BI) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalHom#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Group/Units/Hom.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Group/Units/Hom.lean#L21) (StacksCore): “A local homomorphism of local rings: `φ(𝔪_R) ⊆ 𝔪_S`. Mathlib states the equivalent reflects-units condition, which needs no `IsLocalRing` instance; the equivalence is `IsLocalRing.local_hom_TFAE` (tag 07BJ).”. References: EGA 0 (10.3.1.3); EGA 0 (1.0.7); EGA IV (18.6.1).
- [`IsLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/Defs.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/Defs.lean#L20) (StacksCore): “A local ring is a ring with exactly one maximal ideal. Mathlib defines this by the equivalent condition that the ring is nontrivial and `a` or `b` is a unit whenever `a + b = 1`; see `IsLocalRing.maximal_ideal_unique` for the Stacks wording.”. References: EGA 0 (10.3.1.2); EGA 0 (10.3.1.3); EGA 0 (1.0.7); EGA 0 (22.4.1); EGA 0 (22.5.3); SGA 3 VIA (0.2).
- [`IsLocalRing.maximal_ideal_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.maximal_ideal_unique#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/MaximalIdeal/Basic.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/MaximalIdeal/Basic.lean#L26) (StacksCore): “`∃! I, I.IsMaximal` — the Stacks project's own phrasing of the definition of a local ring, which Mathlib derives from its `a + b = 1` formulation.”. References: EGA 0 (1.0.7), “partial”.
- [`IsLocalRing.maximalIdeal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.maximalIdeal#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/MaximalIdeal/Defs.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/MaximalIdeal/Defs.lean#L16) (StacksCore): “The maximal ideal `𝔪_R` of a local ring `R`, realised as the ideal of nonunits.”. References: EGA 0 (10.3.1.3); EGA 0 (1.0.7); EGA 0 (5.5.1); EGA I (1.1.1); EGA IV (17.15.8); EGA IV (3.4.1).
- [`IsLocalRing.ResidueField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.ResidueField#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/ResidueField/Defs.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/ResidueField/Defs.lean#L16) (StacksCore): “The residue field `κ = R/𝔪_R` of a local ring.”. References: EGA 0 (10.3.1.2); EGA 0 (10.3.1.3); EGA 0 (1.0.7); EGA 0 (5.5.1); EGA 0 (22.4.1); EGA 0 (22.5.3); EGA I (1.1.1); EGA I (2.4.5); EGA II (7.1.5); SGA 1 I (2.1); SGA 1 I (7.5); SGA 1 III (1.7); SGA 2 III (2.8), “special case”; SGA 3 VIIB (0.2.1); SGA 3 VIA (0.2).
- [`IsLocalRing.residue`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.residue#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/ResidueField/Defs.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/ResidueField/Defs.lean#L17) (StacksCore): “The quotient map `R → R/𝔪_R = κ` onto the residue field.”. References: EGA I (2.4.5).

## Tag 0H70, an example

[Tag 0H70](https://stacks.math.columbia.edu/tag/0H70) in the Stacks Project.

**`not_isLocalHom_algebraMap_atPrime`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Counterexamples/LocalHom.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Counterexamples/LocalHom.lean#L30).

> **Stacks 0H70**: for a local ring `R` and a non-maximal prime `𝔭`, the localization map
> `R → R_𝔭` is not a local homomorphism.
>
> The witness is any `x ∈ 𝔪_R \ 𝔭`, which exists precisely because `𝔭 ⊊ 𝔪_R`: it becomes a unit
> in `R_𝔭`, so a local homomorphism would force it to be a unit already in `R`, contradicting
> `x ∈ 𝔪_R`.

```lean
theorem not_isLocalHom_algebraMap_atPrime {R : Type*} [CommRing R] [IsLocalRing R]
    (p : Ideal R) [hp : p.IsPrime] (hne : p ≠ maximalIdeal R) :
    ¬ IsLocalHom (algebraMap R (Localization.AtPrime p))
```

## Tag 00E9, a lemma

[Tag 00E9](https://stacks.math.columbia.edu/tag/00E9) in the Stacks Project.

**`isLocalRing_iff_exists_maximal_isUnit`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/LocalRing/MaximalIdeal/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/MaximalIdeal/Basic.lean#L41). The attribute's comment: “(1) ⇔ (3)”.

> **Stacks 00E9**, clause (1) ⇔ (3): a ring is local if and only if it has a maximal ideal
> `m` such that every element outside `m` is a unit.
>
> The forward direction takes `m` to be `IsLocalRing.maximalIdeal R`, where being outside `m` is
> *definitionally* being a unit (`IsLocalRing.notMem_maximalIdeal`). The reverse direction cannot
> use `IsLocalRing.of_unique_max_ideal` directly — that wants uniqueness, which is not assumed —
> so it goes through `IsLocalRing.of_nonunits_add`: the hypothesis says every nonunit lies in `m`,
> and `m` is closed under addition. Nontriviality comes from `m ≠ ⊤`.

```lean
theorem isLocalRing_iff_exists_maximal_isUnit {R : Type*} [CommSemiring R] :
    IsLocalRing R ↔ ∃ m : Ideal R, m.IsMaximal ∧ ∀ x : R, x ∉ m → IsUnit x
```

**`isLocalRing_iff_existsUnique_isClosed_singleton`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L145). The attribute's comment: “(1) ⇔ (2)”. References: EGA I (2.4.1), “more general”.

> **Stacks 00E9**, clause (1) ⇔ (2): a ring is local if and only if its spectrum has exactly
> one closed point.
>
> The clause is genuinely topological, so it is stated that way rather than as uniqueness of a
> maximal ideal. `PrimeSpectrum.isClosed_singleton_iff_isMaximal` is what converts between the
> two, in both directions; the rest is transport between `PrimeSpectrum R` and `Ideal R` along
> `PrimeSpectrum.ext`.
>
> No nontriviality hypothesis is needed: for the zero ring the spectrum is empty, so it has no
> closed point at all and clause (2) fails on its own.

```lean
theorem isLocalRing_iff_existsUnique_isClosed_singleton {R : Type*} [CommSemiring R] :
    IsLocalRing R ↔ ∃! p : PrimeSpectrum R, IsClosed ({p} : Set (PrimeSpectrum R))
```

Declarations registered for the tag:

- [`IsLocalRing.isUnit_or_isUnit_one_sub_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.isUnit_or_isUnit_one_sub_self#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/Basic.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/Basic.lean#L24) (StacksCore): “(1) ⇒ (4): in a local ring, `x` or `1 - x` is a unit.”.
- [`IsLocalRing.of_isUnit_or_isUnit_one_sub_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.of_isUnit_or_isUnit_one_sub_self#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LocalRing/Basic.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/Basic.lean#L26) (StacksCore): “(4) ⇒ (1): a nontrivial ring in which `x` or `1 - x` is always a unit is local.”.

## Tag 00E7, a lemma

[Tag 00E7](https://stacks.math.columbia.edu/tag/00E7) in the Stacks Project.

**`Ideal.nontrivial_fiber_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Fiber.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/Fiber.lean#L75). The attribute's comment: “(2) ⇔ (3)”.

> **Stacks 00E7**, clause (2) ⇔ clause (3): the fibre `κ(𝔭) ⊗_R S` is nonzero if and only if
> `S_𝔭 / 𝔭 S_𝔭` is nonzero.
>
> Both are ways of saying the fibre of `Spec S → Spec R` over `𝔭` is nonempty; for the link to
> clause (1), that `𝔭` lies in the image, see `PrimeSpectrum.nontrivial_iff_mem_rangeComap`
> (tagged in `StacksCore.RingTheory.Spectrum.Prime.RingHom`).

```lean
theorem nontrivial_fiber_iff :
    Nontrivial (p.Fiber S) ↔ Nontrivial (Sp ⧸ p.map (algebraMap R Sp))
```

**`Ideal.nontrivial_quotient_localization_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Fiber.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/Fiber.lean#L128). The attribute's comment: “(3) ⇔ (4)”.

> **Stacks 00E7**, clause (3) ⇔ clause (4): `S_𝔭 / 𝔭 S_𝔭` is nonzero if and only if
> `(S/𝔭S)_𝔭` is nonzero.

```lean
theorem nontrivial_quotient_localization_iff :
    Nontrivial SpS ↔ Nontrivial (Sp ⧸ p.map (algebraMap R Sp))
```

Declarations registered for the tag:

- [`PrimeSpectrum.mem_range_comap_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.mem_range_comap_iff#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/RingHom.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/RingHom.lean#L43) (StacksCore): “(1) ⇔ (5): `𝔭` is in the image of `Spec S → Spec R` iff `𝔭 = φ⁻¹(𝔭S)`.”.
- [`PrimeSpectrum.nontrivial_iff_mem_rangeComap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.nontrivial_iff_mem_rangeComap#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/RingHom.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Spectrum/Prime/RingHom.lean#L45) (StacksCore): “(1) ⇔ (2): `𝔭` is in the image of `Spec S → Spec R` iff the fibre `κ(𝔭) ⊗[R] S` is nonzero. The tag writes the tensor product in the other order.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.18, Tag 07BH](https://stacks.math.columbia.edu/tag/07BH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
