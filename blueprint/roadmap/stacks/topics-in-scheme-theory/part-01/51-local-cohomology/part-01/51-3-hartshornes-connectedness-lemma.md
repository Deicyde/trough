---
declaration: section
origin: cited
lean: Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_of_two_le_depth, Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_henselization_of_two_le_depth, Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_strictHenselization_of_two_le_depth, Stacks.Equidimensional.equidimensional_of_isCatenary_of_propertySkRing_two
statement: formalized
proof: formalized
---

# 51.3 Hartshorne's connectedness lemma

Section 51.3 of the Stacks Project, [Tag 0FIV](https://stacks.math.columbia.edu/tag/0FIV). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BLR, a lemma

[Tag 0BLR](https://stacks.math.columbia.edu/tag/0BLR) in the Stacks Project.

**`Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_of_two_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectedness.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectedness.lean#L217). The attribute's comment: “the punctured spectrum of `A`”. References: EGA IV (5.10.7), “local ring case”; SGA 2 XII (4.6), “more general”.

> **Stacks Project, Tag 0BLR (first assertion).** The same statement in the
> complement-of-the-closed-point spelling, which is the one the source uses.

```lean
theorem isConnected_puncturedSpectrum_of_two_le_depth (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A) :
    IsConnected ({closedPoint A}ᶜ : Set (PrimeSpectrum A))
```

**`Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_henselization_of_two_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectednessHenselian.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectednessHenselian.lean#L86). The attribute's comment: “the punctured spectrum of `A^h`”.

> **Stacks Project, Tag 0BLR (second assertion).** The punctured spectrum of a henselization of
> a Noetherian local ring of depth at least two is connected.

```lean
theorem isConnected_puncturedSpectrum_henselization_of_two_le_depth
    (A Ah : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A) :
    IsConnected ({closedPoint Ah}ᶜ : Set (PrimeSpectrum Ah))
```

**`Stacks.PuncturedSpectrum.isConnected_puncturedSpectrum_strictHenselization_of_two_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectednessHenselian.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/HartshorneConnectednessHenselian.lean#L103). The attribute's comment: “the punctured spectrum of `A^sh`”.

> **Stacks Project, Tag 0BLR (third assertion).** The punctured spectrum of a strict
> henselization of a Noetherian local ring of depth at least two is connected.

```lean
theorem isConnected_puncturedSpectrum_strictHenselization_of_two_le_depth
    (A Ash : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    (κsep : Type v) [Field κsep] [Algebra (ResidueField A) κsep]
    [IsSepClosure (ResidueField A) κsep] [IsHenselization A κsep Ash]
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A) :
    IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash))
```

## Tag 0FIW, a lemma

[Tag 0FIW](https://stacks.math.columbia.edu/tag/0FIW) in the Stacks Project.

**`Stacks.Equidimensional.equidimensional_of_isCatenary_of_propertySkRing_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CatenaryEquidimensional.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CatenaryEquidimensional.lean#L154). References: EGA IV (5.10.9).

> **Stacks Project, Tag 0FIW** (EGA IV, Corollary 5.10.9). Let `A` be a Noetherian local ring
> which is catenary and satisfies Serre's condition `(S₂)`. Then `Spec(A)` is equidimensional.

```lean
theorem equidimensional_of_isCatenary_of_propertySkRing_two (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (hcat : Ring.IsCatenary A)
    (hS₂ : PropertySkRing A 2) :
    Equidimensional (PrimeSpectrum A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.3, Tag 0FIV](https://stacks.math.columbia.edu/tag/0FIV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
