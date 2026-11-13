---
declaration: section
origin: cited
lean: codimension, PrimeSpectrum.height_vanishingIdeal_preimage, TopologicalSpace.IrreducibleCloseds.coheight_comapOpenEmbedding, TopologicalSpace.IrreducibleCloseds.coheight_restrictOpen, X.noetherianSpace_and_coheight_zeroAsIC_eq_top, IrreducibleClosedsCodim.IsCatenarySpace, CatenaryTopologicalSpace.isCatenary_iff_hasOpenCoveringByCatenarySpaces, CatenaryTopologicalSpace.isCatenary_of_isLocallyClosed
statement: formalized
proof: formalized
---

# 5.11 Codimension and catenary spaces

Section 5.11 of the Stacks Project, [Tag 02I0](https://stacks.math.columbia.edu/tag/02I0). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02I3, a definition

[Tag 02I3](https://stacks.math.columbia.edu/tag/02I3) in the Stacks Project.

**`codimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Codimension.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Codimension.lean#L64). References: EGA 0 (14.2.1), “codim of irreducible Z”; SGA 1 II (5.9).

> **Stacks 02I3**.
> The codimension of an irreducible closed subset `Y` of a topological space `X`, defined as the
> coheight of `Y` in the poset of irreducible closed subsets of `X` ordered by inclusion. This
> equals the supremum of the lengths of strict chains `Y = Y₀ ⊊ Y₁ ⊊ … ⊊ Y_e` of irreducible
> closed subsets starting with `Y`.

```lean
noncomputable def codimension {X : Type*} [TopologicalSpace X]
    (Y : IrreducibleCloseds X) : ℕ∞
```

## Tag 02I4, a lemma

[Tag 02I4](https://stacks.math.columbia.edu/tag/02I4) in the Stacks Project.

**`PrimeSpectrum.height_vanishingIdeal_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/CodimensionHeight.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/CodimensionHeight.lean#L196). The attribute's comment: “the codimension of one irreducible closed subset, as a height on an affine open”. References: EGA 0 (16.1.3), “codim(V(p)”; EGA IV (5.1.1), “special case”.

> **The exact codimension of an irreducible closed subset, read as a height on an open affine
> piece.** Let `Spec R` be an open subspace of a space `X` through an open embedding `f` and let
> `Y ⊆ X` be an irreducible closed subset meeting it. Then the prime ideal of `R` cutting out the
> trace `f ⁻¹' Y` has height exactly `codim(Y, X)`.
>
> This is the *equality* strengthening of
> `PrimeSpectrum.le_height_of_mem_minimalPrimes_of_isOpenEmbedding`, available because the
> irreducible closed subset is pinned rather than quantified over: the trace is an irreducible
> closed subset of `Spec R` whose codimension there is the height of its prime
> (`PrimeSpectrum.codimension_eq_height_vanishingIdeal`) and is `codim(Y, X)` by [Stacks, Tag 02I4]
> (`TopologicalSpace.IrreducibleCloseds.coheight_comapOpenEmbedding`).

```lean
theorem height_vanishingIdeal_preimage (hf : Topology.IsOpenEmbedding f)
    (Y : IrreducibleCloseds X) (hne : (f ⁻¹' (Y : Set X)).Nonempty) :
    (vanishingIdeal (f ⁻¹' (Y : Set X))).height = codimension Y
```

**`TopologicalSpace.IrreducibleCloseds.coheight_comapOpenEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CodimensionOpen.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/CodimensionOpen.lean#L132). References: EGA 0 (14.2.3), “Y irreducible”.

> For an open embedding `f : W → X`, the codimension of an irreducible closed subset `Y ⊆ X`
> meeting the image of `f` equals the codimension of its trace `f ⁻¹' Y` in `W`. No sobriety
> or separation hypothesis is needed.

```lean
theorem coheight_comapOpenEmbedding (Y : IrreducibleCloseds X) (hf : IsOpenEmbedding f)
    (h : (f ⁻¹' (Y : Set X)).Nonempty) :
    Order.coheight Y = Order.coheight (Y.comapOpenEmbedding hf h)
```

**`TopologicalSpace.IrreducibleCloseds.coheight_restrictOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CodimensionOpen.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/CodimensionOpen.lean#L190). References: EGA 0 (14.2.3), “Y irreducible”.

> **Stacks 02I4**.
> Let `X` be a topological space, `Y ⊆ X` an irreducible closed subset and `U ⊆ X` an open subset
> with `Y ∩ U ≠ ∅`. Then the codimension of `Y` in `X` equals the codimension of `Y ∩ U` in `U`:
>
>     codim (Y, X) = codim (Y ∩ U, U).
>
> Codimension is `Order.coheight` in the poset of irreducible closed subsets; see the module
> docstring. No sobriety or separation hypothesis is needed.

```lean
theorem coheight_restrictOpen (Y : IrreducibleCloseds X) (hU : IsOpen U)
    (h : ((Y : Set X) ∩ U).Nonempty) :
    Order.coheight Y = Order.coheight (Y.restrictOpen hU h)
```

## Tag 02I5, an example

[Tag 02I5](https://stacks.math.columbia.edu/tag/02I5) in the Stacks Project.

**`X.noetherianSpace_and_coheight_zeroAsIC_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CounterexampleCodimension.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/CounterexampleCodimension.lean#L400).

> **Stacks 02I5**.
> The space `X = [0, 1]` with the topology generated by the sets `(1 - 1/n, 1]` is a Noetherian
> topological space containing an irreducible closed subset `Y = {0}` of infinite codimension.

```lean
theorem noetherianSpace_and_coheight_zeroAsIC_eq_top :
    NoetherianSpace X ∧ IsIrreducible ({zero} : Set X) ∧
      IsClosed ({zero} : Set X) ∧ Order.coheight zeroAsIC = (⊤ : ℕ∞)
```

## Tag 02I1, a definition

[Tag 02I1](https://stacks.math.columbia.edu/tag/02I1) in the Stacks Project.

**`IrreducibleClosedsCodim.IsCatenarySpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Catenary.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Catenary.lean#L104).

> A topological space `X` is *catenary* if for every pair of irreducible closed subsets
> `Y ⊆ Y'`, the codimension `topCodim Y Y'` is finite and every *maximal* chain of irreducible
> closed subsets from `Y` to `Y'` has length equal to it.

```lean
def IsCatenarySpace (X : Type*) [TopologicalSpace X] : Prop
```

## Tag 02I2, a lemma

[Tag 02I2](https://stacks.math.columbia.edu/tag/02I2) in the Stacks Project.

**`CatenaryTopologicalSpace.isCatenary_iff_hasOpenCoveringByCatenarySpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/CatenaryOpenCovering.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/CatenaryOpenCovering.lean#L341).

> **Stacks 02I2.** A topological space is catenary if and only if it has an open covering by
> catenary spaces.

```lean
theorem isCatenary_iff_hasOpenCoveringByCatenarySpaces (X : Type*) [TopologicalSpace X] :
    IsCatenarySpace X ↔ HasOpenCoveringByCatenarySpaces X
```

**`CatenaryTopologicalSpace.isCatenary_of_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/CatenaryOpenCovering.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/CatenaryOpenCovering.lean#L404). The attribute's comment: “moreover: locally closed subspace is catenary”.

> **Stacks 02I2, moreover clause.** Every locally closed subspace of a catenary space is
> catenary: a locally closed `Z` is open in `closure Z`, which is a closed — hence catenary —
> subspace of `X`, and catenarity passes to open subspaces.

```lean
theorem isCatenary_of_isLocallyClosed (X : Type*) [TopologicalSpace X] (hX : IsCatenarySpace X)
    (Z : Set X) (hZ : IsLocallyClosed Z) : IsCatenarySpace Z
```

## Tag 02I6, a lemma

[Tag 02I6](https://stacks.math.columbia.edu/tag/02I6) in the Stacks Project.

**`isCatenarySpace_iff_codim_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CatenaryAdditive.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/CatenaryAdditive.lean#L437). References: EGA 0 (14.3.2).

> **Stacks 02I6**.
> A topological space `X` is catenary iff for every pair of irreducible closed subsets `Y ⊆ Y'`
> the codimension is finite, and for every triple `Y ⊆ Y' ⊆ Y''` of irreducible closed subsets we
> have the additivity formula `topCodim Y Y'' = topCodim Y Y' + topCodim Y' Y''`.

```lean
theorem isCatenarySpace_iff_codim_additive (X : Type*) [TopologicalSpace X] :
    IsCatenarySpace X ↔
      (∀ Y Y' : IrreducibleCloseds X, Y ≤ Y' → topCodim Y Y' ≠ ⊤) ∧
      (∀ Y Y' Y'' : IrreducibleCloseds X, Y ≤ Y' → Y' ≤ Y'' →
        topCodim Y Y'' = topCodim Y Y' + topCodim Y' Y'')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.11, Tag 02I0](https://stacks.math.columbia.edu/tag/02I0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
