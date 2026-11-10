---
declaration: section
origin: cited
lean: RestrictedPowerSeries.existsUnique_continuousAlgHom_extends, RestrictedPowerSeries.limitCompleteSpace, RestrictedPowerSeries.isHomeomorph_adicCompletionEquiv, RestrictedPowerSeries.adicCompletionEquiv
statement: formalized
proof: formalized
---

# 87.28 Restricted power series

Section 87.28 of the Stacks Project, [Tag 0AKZ](https://stacks.math.columbia.edu/tag/0AKZ). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AJM, a remark

[Tag 0AJM](https://stacks.math.columbia.edu/tag/0AJM) in the Stacks Project.

**`RestrictedPowerSeries.existsUnique_continuousAlgHom_extends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RestrictedPowerSeries.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RestrictedPowerSeries.lean#L650). References: EGA 0 (7.5.3).

> The universal property of restricted power series: every polynomial algebra map into a
> complete linearly topologized algebra extends by a unique continuous algebra map.

```lean
public theorem existsUnique_continuousAlgHom_extends
    {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    {C : Type x} [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra A C]
    {ι : Type w} [Preorder ι] [Nonempty ι] [IsDirected ι (· ≤ ·)]
    (J : ι → Ideal A) (hJ : Antitone J)
    (_ : ∀ i, IsOpen (J i : Set A))
    (hfund : ∀ U ∈ nhds (0 : A), ∃ i, (J i : Set A) ⊆ U)
    (hAC : Continuous (algebraMap A C))
    (hC : TopologicalRing.IsComplete C)
    {σ : Type v} (f : MvPolynomial σ A →ₐ[A] C) :
    ∃! g : RestrictedPowerSeriesOfIdeals J hJ σ →ₐ[A] C,
      Continuous g ∧ g.comp (idealSystemPolynomialAlgHom J hJ σ) = f
```

## Tag 0AL0, a remark

[Tag 0AL0](https://stacks.math.columbia.edu/tag/0AL0) in the Stacks Project.

**`RestrictedPowerSeries.limitCompleteSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RestrictedPowerSeries.lean, line 799](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RestrictedPowerSeries.lean#L799). The attribute's comment: “limit\_completeness”.

> Restricted power series are complete for their inverse-limit topology.

```lean
public instance limitCompleteSpace {A : Type u} [CommRing A]
    (I : Ideal A) (σ : Type v) :
    let _ : UniformSpace (RestrictedPowerSeries I σ) :=
      limitUniformSpace I σ
    CompleteSpace (RestrictedPowerSeries I σ)
```

**`RestrictedPowerSeries.isHomeomorph_adicCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RestrictedPowerSeries.lean, line 969](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RestrictedPowerSeries.lean#L969). The attribute's comment: “finite\_generation\_topology”.

> The canonical completion equivalence is an isomorphism of topological rings when the
> coefficient ideal is finitely generated.

```lean
public theorem isHomeomorph_adicCompletionEquiv {A : Type u} [CommRing A]
    (I : Ideal A) (σ : Type v) (hI : I.FG) :
    let _ : TopologicalSpace (RestrictedPowerSeries I σ) :=
      limitTopology I σ
    let _ : TopologicalSpace
      (AdicCompletion (I.map (MvPolynomial.C : A →+* MvPolynomial σ A))
        (MvPolynomial σ A)) := polynomialCompletionAdicTopology I σ
    IsHomeomorph (adicCompletionEquiv I σ)
```

Declarations registered for the tag:

- [`RestrictedPowerSeries.adicCompletionEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RestrictedPowerSeries.lean#L368), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/RestrictedPowerSeries.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RestrictedPowerSeries.lean#L787) (StacksFrontier): “ring\_identification”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.28, Tag 0AKZ](https://stacks.math.columbia.edu/tag/0AKZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
