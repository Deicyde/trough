---
declaration: section
origin: cited
lean: withConstructibleTopology_t2_totallyDisconnected_compact, spectralMap_continuous_withConstructibleTopology, spectralMap_fibre_isCompact, spectralMap_range_isClosed_withConstructibleTopology, TopologicalSpace.isSpectralMap_iff_continuous_constructibleTopology, spectralSpace_of_isClosed_constructibleTopology, specializes_and_isClosed_and_isOpen_of_constructible, Topology.exists_specializes_or_exists_disjoint_nhds
statement: formalized
proof: formalized
---

# 5.23 Spectral spaces

Section 5.23 of the Stacks Project, [Tag 08YF](https://stacks.math.columbia.edu/tag/08YF). 14 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0901, a lemma

[Tag 0901](https://stacks.math.columbia.edu/tag/0901) in the Stacks Project.

**`withConstructibleTopology_t2_totallyDisconnected_compact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/ConstructibleProfinite.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/ConstructibleProfinite.lean#L97). References: EGA IV (1.9.15), “(ii)(iii) suff, spectral”.

> **Stacks 0901**.
> For a spectral space `X`, the constructible topology on `X` is Hausdorff, totally
> disconnected and quasi-compact.

```lean
theorem withConstructibleTopology_t2_totallyDisconnected_compact (X : Type*) [TopologicalSpace X]
  [SpectralSpace X] :
    T2Space (WithConstructibleTopology X) ∧
      TotallyDisconnectedSpace (WithConstructibleTopology X) ∧
        CompactSpace (WithConstructibleTopology X)
```

## Tag 0A2S, a lemma

[Tag 0A2S](https://stacks.math.columbia.edu/tag/0A2S) in the Stacks Project.

**`spectralMap_continuous_withConstructibleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/SpectralMaps.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/SpectralMaps.lean#L667). The attribute's comment: “continuity in the constructible topology”. References: EGA IV (1.9.14), “iii, special case”.

> **Stacks 0A2S** (continuity in the constructible topology).
> A spectral map `f : X → Y` is continuous for the constructible topologies on `X` and `Y`.

```lean
theorem spectralMap_continuous_withConstructibleTopology
    (f : X → Y) (hf : IsSpectralMap f) :
    Continuous
      (fun x : WithConstructibleTopologyTypeSynonym X =>
        WithConstructibleTopologyTypeSynonym.of (f (WithConstructibleTopologyTypeSynonym.out
            x)))
```

**`spectralMap_fibre_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/SpectralMaps.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/SpectralMaps.lean#L685). The attribute's comment: “quasi-compact fibres”.

> **Stacks 0A2S** (quasi-compact fibres).
> The fibres of a spectral map between spectral spaces are quasi-compact.

```lean
theorem spectralMap_fibre_isCompact
    (f : X → Y) (hf : IsSpectralMap f) (y : Y) :
    IsCompact (f ⁻¹' {y})
```

**`spectralMap_range_isClosed_withConstructibleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/SpectralMaps.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/SpectralMaps.lean#L703). The attribute's comment: “closed image in the constructible topology”. References: EGA IV (1.9.14), “iv, special case”.

> **Stacks 0A2S** (closed image in the constructible topology).
> The image of a spectral map between spectral spaces is closed in the constructible topology on the
> target.

```lean
theorem spectralMap_range_isClosed_withConstructibleTopology
    (f : X → Y) (hf : IsSpectralMap f) :
    IsClosed (Set.range (fun x => WithConstructibleTopologyTypeSynonym.of (f x)))
```

## Tag 0G1J, a lemma

[Tag 0G1J](https://stacks.math.columbia.edu/tag/0G1J) in the Stacks Project.

**`TopologicalSpace.isSpectralMap_iff_continuous_constructibleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/SpectralMapConstructible.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/SpectralMapConstructible.lean#L108). References: EGA IV (1.9.14), “(iii)”.

> **Stacks 0G1J.** Let `X` and `Y` be spectral spaces and let `f : X → Y` be continuous.
> Then `f` is a spectral map if and only if it is continuous for the constructible topologies
> on `X` and `Y`.

```lean
theorem isSpectralMap_iff_continuous_constructibleTopology
    [SpectralSpace X] [SpectralSpace Y] (f : X → Y) (hf : Continuous f) :
    IsSpectralMap f ↔ Continuous[constructibleTopology X, constructibleTopology Y] f
```

## Tag 0902, a lemma

[Tag 0902](https://stacks.math.columbia.edu/tag/0902) in the Stacks Project.

**`spectralSpace_of_isClosed_constructibleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/ConstructiblyClosed.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/ConstructiblyClosed.lean#L286). References: SGA 4 IV (9.1.11), “partial”.

> **Stacks 0902**.
> For a spectral space `X` and a subset `E ⊆ X` closed in the constructible topology on `X`, the set
> `E` with the subspace topology inherited from `X` is a spectral space.

```lean
theorem spectralSpace_of_isClosed_constructibleTopology
    {X : Type*} [TopologicalSpace X] [SpectralSpace X]
    (E : Set X)
    (hE : @IsClosed X (constructibleTopology X) E) :
    SpectralSpace E
```

## Tag 0903, a lemma

[Tag 0903](https://stacks.math.columbia.edu/tag/0903) in the Stacks Project.

**`specializes_and_isClosed_and_isOpen_of_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/ConstructiblyClosedStable.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/ConstructiblyClosedStable.lean#L162).

> **Stacks 0903**.
> For a spectral space `X`: a point of the closure of a constructibly closed set is a specialization
> of a point of that set; a constructibly closed set stable under specialization is closed; and a
> constructibly open set stable under generalization is open.

```lean
theorem specializes_and_isClosed_and_isOpen_of_constructible [SpectralSpace X] :
    (∀ {E : Set X}, IsClosed[constructibleTopology X] E →
        ∀ {x : X}, x ∈ closure E → ∃ y ∈ E, y ⤳ x) ∧
      (∀ {E : Set X}, IsClosed[constructibleTopology X] E →
        StableUnderSpecialization E → IsClosed E) ∧
      (∀ {E' : Set X}, IsOpen[constructibleTopology X] E' →
        StableUnderGeneralization E' → IsOpen E')
```

## Tag 0904, a lemma

[Tag 0904](https://stacks.math.columbia.edu/tag/0904) in the Stacks Project.

**`Topology.exists_specializes_or_exists_disjoint_nhds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/Generization.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/Generization.lean#L82).

> **Stacks 0904.** For any two points `x`, `y` of a spectral space, either there is a point
> `z` specializing to both (equivalently, `x` and `y` both lie in `closure {z}`), or `x` and `y`
> have disjoint open neighbourhoods.

```lean
theorem exists_specializes_or_exists_disjoint_nhds [SpectralSpace X] (x y : X) :
    (∃ z : X, z ⤳ x ∧ z ⤳ y) ∨
      ∃ U V : Set X, IsOpen U ∧ IsOpen V ∧ x ∈ U ∧ y ∈ V ∧ Disjoint U V
```

## Tag 0905, a lemma

[Tag 0905](https://stacks.math.columbia.edu/tag/0905) in the Stacks Project.

**`spectralSpace_profinite_of_t2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/ProfiniteCharacterization.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/ProfiniteCharacterization.lean#L219).

> **Stacks 0905**.
> A Hausdorff spectral space is profinite: it is both Hausdorff and totally disconnected
> (quasi-compactness is automatic from `SpectralSpace`).

```lean
theorem spectralSpace_profinite_of_t2 [SpectralSpace X] [T2Space X] :
    T2Space X ∧ TotallyDisconnectedSpace X
```

## Tag 0906, a lemma

[Tag 0906](https://stacks.math.columbia.edu/tag/0906) in the Stacks Project.

**`connectedComponents_isProfinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/ComponentSpace.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/ComponentSpace.lean#L286).

> **Stacks 0906**.
> For a spectral space `X` the space of connected components `π₀(X) = ConnectedComponents X` is
> profinite: Hausdorff, quasi-compact and totally disconnected.

```lean
theorem connectedComponents_isProfinite
    (X : Type*) [TopologicalSpace X] [SpectralSpace X] :
    T2Space (ConnectedComponents X) ∧
    CompactSpace (ConnectedComponents X) ∧
    TotallyDisconnectedSpace (ConnectedComponents X)
```

## Tag 0907, a lemma

[Tag 0907](https://stacks.math.columbia.edu/tag/0907) in the Stacks Project.

**`prod_spectralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/Products.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/Products.lean#L165).

> The product of two spectral spaces is a spectral space.

```lean
theorem prod_spectralSpace (X Y : Type*)
    [TopologicalSpace X] [TopologicalSpace Y]
    [SpectralSpace X] [SpectralSpace Y] :
    SpectralSpace (X × Y)
```

## Tag 09XU, a lemma

[Tag 09XU](https://stacks.math.columbia.edu/tag/09XU) in the Stacks Project.

**`Topology.isHomeomorph_of_isSpectralMap_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/BijectionHomeomorph.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/BijectionHomeomorph.lean#L223).

> **Stacks 09XU.** Let `f : X → Y` be a spectral, bijective map of spectral topological
> spaces. If generalizations or specializations lift along `f`, then `f` is a homeomorphism.

```lean
theorem isHomeomorph_of_isSpectralMap_of_bijective [SpectralSpace X] [SpectralSpace Y]
    {f : X → Y} (hspec : IsSpectralMap f) (hbij : Function.Bijective f)
    (hlift : GeneralizingMap f ∨ SpecializingMap f) : IsHomeomorph f
```

## Tag 09XV, a lemma

[Tag 09XV](https://stacks.math.columbia.edu/tag/09XV) in the Stacks Project.

**`spectralSpace_inverseLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/InverseLimitFiniteSober.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/InverseLimitFiniteSober.lean#L181).

> **Stacks 09XV**. The inverse limit of a directed inverse system of finite sober topological
> spaces is a spectral topological space. Here a sober space in the sense of the Stacks project is a
> space that is both `T0Space` and `QuasiSober`.

```lean
theorem spectralSpace_inverseLimit [Nonempty I] [IsDirectedOrder I] [∀ i, Finite (X i)]
    [∀ i, T0Space (X i)] [∀ i, QuasiSober (X i)]
    (hf : ∀ ⦃i j : I⦄ (h : i ≤ j), Continuous (f h)) :
    SpectralSpace (inverseLimit f)
```

## Tag 09XW, a lemma

[Tag 09XW](https://stacks.math.columbia.edu/tag/09XW) in the Stacks Project.

**`Topology.spectralSpace_iff_exists_isClosed_withConstructibleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/SierpinskiEmbedding.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/SierpinskiEmbedding.lean#L577).

> A topological space is spectral if and only if it is homeomorphic to a subset of a product of
> copies of the Sierpinski space which is closed for the constructible topology of that product.

```lean
theorem spectralSpace_iff_exists_isClosed_withConstructibleTopology (X : Type u)
    [TopologicalSpace X] :
    SpectralSpace X ↔
      ∃ (I : Type u) (S : Set (SierpinskiProduct I)),
        IsClosed[constructibleTopology (SierpinskiProduct I)] S ∧ Nonempty (X ≃ₜ S)
```

## Tag 09XX, a lemma

[Tag 09XX](https://stacks.math.columbia.edu/tag/09XX) in the Stacks Project.

**`spectralSpace_iff_isDirectedInverseLimitOfFiniteSober`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/AsDirectedInverseLimit.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/AsDirectedInverseLimit.lean#L175).

> A topological space is spectral if and only if it is a directed inverse limit of finite
> sober topological spaces.

```lean
theorem spectralSpace_iff_isDirectedInverseLimitOfFiniteSober
    (X : Type u) [TopologicalSpace X] :
    SpectralSpace X ↔ IsDirectedInverseLimitOfFiniteSober X
```

## Tag 0A2T, a lemma

[Tag 0A2T](https://stacks.math.columbia.edu/tag/0A2T) in the Stacks Project.

**`UniversalSoberMap.compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/UniversalSoberMap.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/UniversalSoberMap.lean#L291). The attribute's comment: “part (1): quasi-compactness”.

> **Statement (1).** If `X` is quasi-compact, then so is `X'`.
> This is the first part of Stacks Project Lemma 5.23.15 (tag `0A2T`).

```lean
theorem UniversalSoberMap.compactSpace
    {X X' : Type*} [TopologicalSpace X] [TopologicalSpace X']
    (c : UniversalSoberMap X X') [CompactSpace X] :
    CompactSpace X'
```

**`UniversalSoberMap.spectralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/UniversalSoberMap.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/UniversalSoberMap.lean#L385). The attribute's comment: “part (2): spectral”.

> **Statement (2).** If `X` is quasi-compact, has a basis of quasi-compact opens, and the
> intersection of any two quasi-compact opens of `X` is quasi-compact, then `X'` is a spectral
> topological space. This is the second part of Stacks Project Lemma 5.23.15 (tag `0A2T`).

```lean
theorem UniversalSoberMap.spectralSpace
    {X X' : Type*} [TopologicalSpace X] [TopologicalSpace X']
    (c : UniversalSoberMap X X')
    [CompactSpace X] [PrespectralSpace X] [QuasiSeparatedSpace X] :
    SpectralSpace X'
```

**`UniversalSoberMap.noetherianSpectralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/UniversalSoberMap.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/UniversalSoberMap.lean#L415). The attribute's comment: “part (3): Noetherian spectral”.

> **Statement (3).** If `X` is Noetherian, then `X'` is a Noetherian spectral space.
> This is the third part of Stacks Project Lemma 5.23.15 (tag `0A2T`).

```lean
theorem UniversalSoberMap.noetherianSpectralSpace
    {X X' : Type*} [TopologicalSpace X] [TopologicalSpace X']
    (c : UniversalSoberMap X X') [NoetherianSpace X] :
    NoetherianSpace X' ∧ SpectralSpace X'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.23, Tag 08YF](https://stacks.math.columbia.edu/tag/08YF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
