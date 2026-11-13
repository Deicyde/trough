---
declaration: section
origin: cited
lean: Algebra.TensorProduct.connectedSpace_primeSpectrum, Algebra.isGeometricallyConnected_iff_forall_finite_separable, Algebra.IsGeometricallyConnected, Algebra.isGeometricallyConnected_iff_connectedSpace_primeSpectrum, geometricallyConnected_of_subalgebra, geometricallyConnected_of_forall_fg, geometricallyConnected_of_directedColimit, Algebra.TensorProduct.bijOn_isIdempotentElem_and_bijective_connectedComponentsMap
statement: formalized
proof: formalized
---

# 10.48 Geometrically connected algebras

Section 10.48 of the Stacks Project, [Tag 05DV](https://stacks.math.columbia.edu/tag/05DV). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 037R, a lemma

[Tag 037R](https://stacks.math.columbia.edu/tag/037R) in the Stacks Project.

**`Algebra.TensorProduct.connectedSpace_primeSpectrum`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/Connected.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TensorProduct/Connected.lean#L332). The attribute's comment: “Connectedness of the spectra of two `k`-algebras over a separably closed field `k` is inherited by the spectrum of their tensor product over `k`. Stated as an instance, with `Spec` read as `PrimeSpectrum` and `connected` as `ConnectedSpace`, which includes nonemptiness as the source's notion of a connected space does.”. References: SGA 3 X (9.7.2), “affine case”; SGA 3 X (9.7.1), “affine case, i = 1”.

> **Connectedness of the spectrum of a tensor product over a separably closed field.** Let `k`
> be a separably algebraically closed field and let `R` and `S` be `k`-algebras. If `Spec R` and
> `Spec S` are connected, then so is `Spec (R ⊗[k] S)`.

```lean
public instance connectedSpace_primeSpectrum (k : Type u) (R : Type v) (S : Type w) [Field k]
    [IsSepClosed k] [CommRing R] [Algebra k R] [CommRing S] [Algebra k S]
    [ConnectedSpace (PrimeSpectrum R)] [ConnectedSpace (PrimeSpectrum S)] :
    ConnectedSpace (PrimeSpectrum (R ⊗[k] S))
```

## Tag 037S, a lemma

[Tag 037S](https://stacks.math.columbia.edu/tag/037S) in the Stacks Project.

**`Algebra.isGeometricallyConnected_iff_forall_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected/Criteria.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected/Criteria.lean#L136). The attribute's comment: “Geometric connectedness of a `k`-algebra need only be tested on the finite separable extensions of `k`. Condition (1) of the lemma is `Algebra.IsGeometricallyConnected` (Stacks 037T), which is that condition verbatim; `Spec` is `PrimeSpectrum` and `connected` is `ConnectedSpace`, which includes nonemptiness as the source's notion does.”. References: EGA IV (8.4.5), “affine case”.

> **Geometric connectedness is detected by the finite separable extensions.** Let `k` be a
> field and let `R` be a `k`-algebra. Then `R` is geometrically connected over `k`, that is,
> `Spec (K ⊗[k] R)` is connected for every field extension `K/k`, if and only if `Spec (K ⊗[k] R)`
> is connected for every finite separable field extension `K/k`.

```lean
public theorem isGeometricallyConnected_iff_forall_finite_separable (k : Type u) (R : Type v)
    [Field k] [CommRing R] [Algebra k R] :
    IsGeometricallyConnected k R ↔
      ∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K] [Algebra.IsSeparable k K],
        ConnectedSpace (PrimeSpectrum (K ⊗[k] R))
```

## Tag 037T, a definition

[Tag 037T](https://stacks.math.columbia.edu/tag/037T) in the Stacks Project.

**`Algebra.IsGeometricallyConnected`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected/Defs.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected/Defs.lean#L68).

> A `k`-algebra `S` over a field `k` is *geometrically connected over `k`* if for every field
> extension `K/k` the spectrum of `K ⊗[k] S` is connected.

```lean
public class IsGeometricallyConnected (k : Type u) (S : Type v) [Field k] [CommRing S]
    [Algebra k S] : Prop
```

## Tag 037U, a lemma

[Tag 037U](https://stacks.math.columbia.edu/tag/037U) in the Stacks Project.

**`Algebra.isGeometricallyConnected_iff_connectedSpace_primeSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected.lean#L333).

> **Geometric connectedness over a separably closed field.** Let `k` be a separably
> algebraically closed field and let `R` be a `k`-algebra. Then `R` is geometrically connected
> over `k` if and only if `Spec R` is connected.

```lean
public theorem Algebra.isGeometricallyConnected_iff_connectedSpace_primeSpectrum
    (k : Type u) (R : Type v) [Field k] [IsSepClosed k] [CommRing R] [Algebra k R] :
    Algebra.IsGeometricallyConnected k R ↔ ConnectedSpace (PrimeSpectrum R)
```

## Tag 037V, a lemma

[Tag 037V](https://stacks.math.columbia.edu/tag/037V) in the Stacks Project.

**`geometricallyConnected_of_subalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected.lean#L117). The attribute's comment: “(1)”.

> If `S` is geometrically connected over `k`, then every `k`-subalgebra `R ⊆ S` is
> geometrically connected over `k`.

```lean
theorem geometricallyConnected_of_subalgebra
    (k : Type u) (S : Type v) [Field k] [CommRing S] [Algebra k S]
    (hS : Algebra.IsGeometricallyConnected k S) (R : Subalgebra k S) :
    Algebra.IsGeometricallyConnected k R
```

**`geometricallyConnected_of_forall_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected.lean#L131). The attribute's comment: “(2)”.

> If every finitely generated `k`-subalgebra of `S` is geometrically connected over `k`,
> then `S` is geometrically connected over `k`.

```lean
theorem geometricallyConnected_of_forall_fg
    (k : Type u) (S : Type v) [Field k] [CommRing S] [Algebra k S]
    (h : ∀ R : Subalgebra k S, R.FG → Algebra.IsGeometricallyConnected k R) :
    Algebra.IsGeometricallyConnected k S
```

**`geometricallyConnected_of_directedColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyConnected.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyConnected.lean#L192). The attribute's comment: “(3)”.

> A directed colimit of geometrically connected `k`-algebras is geometrically connected
> over `k`. The colimit `S` of the directed system `(S_i, φ_{ij})` with cocone maps
> `ψ_i : S_i →ₐ[k] S` is presented by its elementary universal property: the `ψ_i` are jointly
> surjective, and `ψ_i y = ψ_i z` holds only if `y` and `z` become equal after some transition map
> `φ_{ij}`.

```lean
theorem geometricallyConnected_of_directedColimit
    (k : Type u) [Field k]
    (ι : Type w) [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    (Sfun : ι → Type v) [(i : ι) → CommRing (Sfun i)] [(i : ι) → Algebra k (Sfun i)]
    (φ : (i j : ι) → i ≤ j → (Sfun i →ₐ[k] Sfun j))
    (hφcomp : ∀ (i j l : ι) (hij : i ≤ j) (hjl : j ≤ l),
      (φ j l hjl).comp (φ i j hij) = φ i l (le_trans hij hjl))
    (S : Type v) [CommRing S] [Algebra k S]
    (ψ : (i : ι) → (Sfun i →ₐ[k] S))
    (hψ : ∀ (i j : ι) (hij : i ≤ j), (ψ j).comp (φ i j hij) = ψ i)
    (hsurj : ∀ x : S, ∃ (i : ι) (y : Sfun i), ψ i y = x)
    (hsep : ∀ (i : ι) (y z : Sfun i), ψ i y = ψ i z →
      ∃ (j : ι) (hij : i ≤ j), φ i j hij y = φ i j hij z)
    (hgc : ∀ i, Algebra.IsGeometricallyConnected k (Sfun i)) :
    Algebra.IsGeometricallyConnected k S
```

## Tag 037W, a lemma

[Tag 037W](https://stacks.math.columbia.edu/tag/037W) in the Stacks Project.

**`Algebra.TensorProduct.bijOn_isIdempotentElem_and_bijective_connectedComponentsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/Connected.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TensorProduct/Connected.lean#L479). The attribute's comment: “Base change of an arbitrary `k`-algebra `R` along a geometrically connected `k`-algebra `S` induces a bijection on idempotents and a bijection on connected components of the spectra. Both assertions of the lemma; the second is stated as a bijection, as in the source, rather than as the homeomorphism of Varieties, Lemma 0385.”.

> **Base change along a geometrically connected algebra.** Let `k` be a field, let `S` be a
> geometrically connected `k`-algebra and let `R` be any `k`-algebra. Then `R → R ⊗[k] S`,
> `r ↦ r ⊗ 1`, restricts to a bijection from the idempotents of `R` onto the idempotents of
> `R ⊗[k] S`, and the induced map `Spec (R ⊗[k] S) → Spec R` is a bijection on connected
> components.

```lean
public theorem bijOn_isIdempotentElem_and_bijective_connectedComponentsMap
    (k : Type u) [Field k] (S : Type v) [CommRing S] [Algebra k S]
    [IsGeometricallyConnected k S] (R : Type w) [CommRing R] [Algebra k R] :
    Set.BijOn (algebraMap R (R ⊗[k] S)) {e | IsIdempotentElem e} {e | IsIdempotentElem e} ∧
      Function.Bijective (PrimeSpectrum.continuous_comap
        (algebraMap R (R ⊗[k] S))).connectedComponentsMap
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.48, Tag 05DV](https://stacks.math.columbia.edu/tag/05DV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
