---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.vectorBundle, AlgebraicGeometry.VectorBundle, AlgebraicGeometry.VectorBundle.category, AlgebraicGeometry.VectorBundle.degreeOneEquivalence
statement: formalized
proof: formalized
---

# 27.6 Vector bundles

Section 27.6 of the Stacks Project, [Tag 01M1](https://stacks.math.columbia.edu/tag/01M1). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01M2, a definition

[Tag 01M2](https://stacks.math.columbia.edu/tag/01M2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.vectorBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/VectorBundleOfModule.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/VectorBundleOfModule.lean#L72). The attribute's comment: “the vector bundle V(E) = Spec_S(Sym(E)) associated to a quasi-coherent module”. References: EGA II (1.7.8); EGA IV (16.4.7); EGA IV (16.5.12), “more general”; EGA IV (18.5.2); SGA 3 I (4.6.3.1), “partial”; SGA 3 VIB (11.5); SGA 4½ Sommes trig (4.6), “partial”; SGA 6 VIII (5.2).

> **The vector bundle `𝐕(ℰ) = Spec_S(Sym(ℰ))` associated to a quasi-coherent `𝒪_S`-module
> `ℰ`**: the relative spectrum of the symmetric algebra of `ℰ`.
>
> Following EGA II, Definition 1.7.8, `ℰ` is not assumed finite locally free.

```lean
def vectorBundle [E.IsQuasicoherent] : Scheme.{u}
```

## Tag 062M, a definition

[Tag 062M](https://stacks.math.columbia.edu/tag/062M) in the Stacks Project.

**`AlgebraicGeometry.VectorBundle`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/VectorBundle.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/VectorBundle.lean#L223). The attribute's comment: “vector bundles”.

> A vector bundle over `S`: a cone whose direct-image algebra is generated in degree one in the
> strongest sense, namely that every canonical map `Sym^n(ℰ_1) ⟶ ℰ_n` is an isomorphism.

```lean
structure VectorBundle (S : Scheme.{u}) extends AbstractCone S
```

**`AlgebraicGeometry.VectorBundle.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/VectorBundle.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/VectorBundle.lean#L236). The attribute's comment: “morphisms of vector bundles”.

> Vector bundles over a fixed base form a category, with the morphisms of the underlying
> cones as its morphisms.

```lean
instance category : Category (VectorBundle S)
```

## Tag 062N, a lemma

[Tag 062N](https://stacks.math.columbia.edu/tag/062N) in the Stacks Project.

**`AlgebraicGeometry.VectorBundle.degreeOneEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/VectorBundleEssSurj.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/VectorBundleEssSurj.lean#L422). The attribute's comment: “the anti-equivalence between vector bundles over S and quasi-coherent O_S-modules”.

> The category of vector bundles over a scheme `S` is anti-equivalent to the category of
> quasi-coherent `𝒪_S`-modules.
>
> The anti-equivalence is recorded in the contravariant form `(VectorBundle S)ᵒᵖ ≌ QCoh(𝒪_S)`, the
> functor being `V ↦ (π_* 𝒪_V)_1` and its quasi-inverse `ℰ ↦ 𝐕(ℰ) = Spec_S(Sym(ℰ))`. Of the two
> standard forms of an anti-equivalence this is the one with the opposite taken on the *geometric*
> side, which is the side the source's two functors are contravariant on, and it is the form of
> Tag 01SA's `(AffineOver S)ᵒᵖ ≌ QuasicoherentAlgebra S` that this one restricts.

```lean
def degreeOneEquivalence (S : Scheme.{u}) :
    (VectorBundle S)ᵒᵖ ≌ Scheme.QuasicoherentModules S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.6, Tag 01M1](https://stacks.math.columbia.edu/tag/01M1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
