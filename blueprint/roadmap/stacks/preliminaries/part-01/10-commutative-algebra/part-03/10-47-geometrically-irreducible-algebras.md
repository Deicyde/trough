---
declaration: section
origin: cited
lean: irreducibleSpace_primeSpectrum_of_isOpenMap_comap, irreducibleSpace_primeSpectrum_of_flat_finitePresentation, tensorProduct_unique_minimalPrime_of_isSepClosed_right_base, AlgebraicGeometry.geometricallyIrreducible_tfae, Algebra.IsGeometricallyIrreducible, Algebra.isGeometricallyIrreducible_iff_irreducibleSpace_primeSpectrum, isGeometricallyIrreducible_of_subalgebra, isGeometricallyIrreducible_of_forall_fg
statement: formalized
proof: formalized
---

# 10.47 Geometrically irreducible algebras

Section 10.47 of the Stacks Project, [Tag 00I2](https://stacks.math.columbia.edu/tag/00I2). 14 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00I6, a lemma

[Tag 00I6](https://stacks.math.columbia.edu/tag/00I6) in the Stacks Project.

**`irreducibleSpace_primeSpectrum_of_isOpenMap_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean#L122). The attribute's comment: “general form”. References: EGA IV (2.3.5), “(iii), special case”; EGA IV (4.4.2), “special case”.

> **Stacks 00I6** (algebraic form, more general statement). Let `R → S` be a
> ring map. Assume:
> * `Spec R` is irreducible;
> * the induced map `Spec S → Spec R` is open;
> * the topological fibres of `Spec S → Spec R` are irreducible for `p` in a
>   dense subset of `Spec R`.
>
> Then `Spec S` is irreducible.

```lean
theorem irreducibleSpace_primeSpectrum_of_isOpenMap_comap
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [IrreducibleSpace (PrimeSpectrum R)]
    (hopen : IsOpenMap (PrimeSpectrum.comap (algebraMap R S)))
    (D : Set (PrimeSpectrum R)) (hD : Dense D)
    (hfib : ∀ p ∈ D,
      IrreducibleSpace
        {q : PrimeSpectrum S // PrimeSpectrum.comap (algebraMap R S) q = p}) :
    IrreducibleSpace (PrimeSpectrum S)
```

**`irreducibleSpace_primeSpectrum_of_flat_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean#L140).

> **Stacks 00I6** (flat + finite-presentation form). Let `R → S` be a flat
> ring map of finite presentation. If `Spec R` is irreducible and the
> topological fibres of `Spec S → Spec R` are irreducible for `p` in a dense
> subset of `Spec R`, then `Spec S` is irreducible.

```lean
theorem irreducibleSpace_primeSpectrum_of_flat_finitePresentation
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [IrreducibleSpace (PrimeSpectrum R)]
    [Module.Flat R S] [Algebra.FinitePresentation R S]
    (D : Set (PrimeSpectrum R)) (hD : Dense D)
    (hfib : ∀ p ∈ D,
      IrreducibleSpace
        {q : PrimeSpectrum S // PrimeSpectrum.comap (algebraMap R S) q = p}) :
    IrreducibleSpace (PrimeSpectrum S)
```

## Tag 00I7, a lemma

[Tag 00I7](https://stacks.math.columbia.edu/tag/00I7) in the Stacks Project.

**`tensorProduct_unique_minimalPrime_of_isSepClosed_right_base`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleFibres.lean#L227). The attribute's comment: “Only the degenerate S = k case; the general R ⊗\_k S statement is not formalized.”.

> **Stacks Tag 00I7 (right-factor-is-the-base-field special case).**
> Let `k` be a field and let `R` be a `k`-algebra with a unique minimal prime.
> Then `R ⊗_k k` has a unique minimal prime.
>
> The full Stacks lemma asserts the same conclusion for `R ⊗_k S` for any pair
> of `k`-algebras `R`, `S` each with a unique minimal prime; that proof requires
> the algebraic closure of `k`, generic-fibre irreducibility for the flat
> finite-type map `R → R ⊗_k S` (Hilbert Nullstellensatz, Jacobson), and a limit
> argument over finitely generated subalgebras.
>
> Only the degenerate `S = k` case is formalized here, and it does not use
> separable closedness of `k`: it is `Algebra.TensorProduct.rid` transported along
> `unique_minimalPrime_of_ringEquiv`. Accordingly no `[IsSepClosed k]` hypothesis
> is assumed, and the `@[stacks 00I7]` attribute is qualified -- **tag 00I7 is
> still open** in the generality Stacks states.

```lean
alias tensorProduct_unique_minimalPrime_of_isSepClosed_right_base
```

## Tag 037K, a lemma

[Tag 037K](https://stacks.math.columbia.edu/tag/037K) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Criteria.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Criteria.lean#L403).

> **Stacks 037K.** Let `k` be a field, `R` a commutative `k`-algebra, `k^{sep}` a separable
> closure of `k` and `k̄` an algebraic closure of `k`. The following are equivalent:
> 1. the spectrum of `R ⊗[k] k'` is irreducible for every field extension `k'/k`;
> 2. the spectrum of `R ⊗[k] k'` is irreducible for every finite separable field extension `k'/k`;
> 3. the spectrum of `R ⊗[k] k^{sep}` is irreducible;
> 4. the spectrum of `R ⊗[k] k̄` is irreducible;
> 5. `Spec R ⟶ Spec k` is geometrically irreducible.

```lean
public theorem AlgebraicGeometry.geometricallyIrreducible_tfae (k R : Type u) [Field k]
    [CommRing R] [Algebra k R] (ksep kbar : Type u) [Field ksep] [Algebra k ksep]
    [IsSepClosure k ksep] [Field kbar] [Algebra k kbar] [IsAlgClosure k kbar] :
    List.TFAE
      [∀ (k' : Type u) [Field k'] [Algebra k k'], IrreducibleSpace (PrimeSpectrum (R ⊗[k] k')),
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
          [Algebra.IsSeparable k k'], IrreducibleSpace (PrimeSpectrum (R ⊗[k] k')),
        IrreducibleSpace (PrimeSpectrum (R ⊗[k] ksep)),
        IrreducibleSpace (PrimeSpectrum (R ⊗[k] kbar)),
        GeometricallyIrreducible (Spec.map (ofHom (algebraMap k R)))]
```

## Tag 037L, a definition

[Tag 037L](https://stacks.math.columbia.edu/tag/037L) in the Stacks Project.

**`Algebra.IsGeometricallyIrreducible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Defs.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Defs.lean#L133). References: EGA IV (4.5.2), “special case”; EGA IV (4.5.9).

> A `k`-algebra `S` is **geometrically irreducible over `k`** if every base change of
> `Spec S ⟶ Spec k` along a field-valued point of `Spec k` is an irreducible space, equivalently
> if for every field extension `k'/k` the spectrum of `S ⊗[k] k'` is irreducible
> (`Algebra.isGeometricallyIrreducible_iff_irreducibleSpace_primeSpectrum_tensorProduct`). An
> irreducible space is nonempty, so this forces every such `S ⊗[k] k'` to be nonzero.

```lean
public abbrev Algebra.IsGeometricallyIrreducible (k S : Type u) [Field k] [CommRing S]
    [Algebra k S] : Prop
```

## Tag 037M, a lemma

[Tag 037M](https://stacks.math.columbia.edu/tag/037M) in the Stacks Project.

**`Algebra.isGeometricallyIrreducible_iff_irreducibleSpace_primeSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Criteria.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Criteria.lean#L528).

> **Stacks 037M.** Let `k` be a separably algebraically closed field and let `R` be a
> `k`-algebra. Then `R` is geometrically irreducible over `k` if and only if the spectrum of `R`
> is irreducible.

```lean
public theorem Algebra.isGeometricallyIrreducible_iff_irreducibleSpace_primeSpectrum
    (k R : Type u) [Field k] [IsSepClosed k] [CommRing R] [Algebra k R] :
    Algebra.IsGeometricallyIrreducible k R ↔ IrreducibleSpace (PrimeSpectrum R)
```

## Tag 037N, a lemma

[Tag 037N](https://stacks.math.columbia.edu/tag/037N) in the Stacks Project.

**`isGeometricallyIrreducible_of_subalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean#L189). The attribute's comment: “(1)”.

> **Statement 1 (Subalgebras).** If `S` is geometrically irreducible over `k`, then
> every `k`-subalgebra `S' ⊆ S` is geometrically irreducible over `k`.

```lean
theorem isGeometricallyIrreducible_of_subalgebra
    (k : Type u) [Field k] (S : Type u) [CommRing S] [Algebra k S]
    (hS : Algebra.IsGeometricallyIrreducible k S)
    (S' : Subalgebra k S) :
    Algebra.IsGeometricallyIrreducible k S'
```

**`isGeometricallyIrreducible_of_forall_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean#L278). The attribute's comment: “(2)”.

> **Statement 2 (Detection by finitely generated subalgebras).** If every finitely
> generated `k`-subalgebra of `S` is geometrically irreducible over `k`, then `S` is
> geometrically irreducible over `k`.
>
> Proof outline: for each field extension `k'/k`, reduce
> `IrreducibleSpace (PrimeSpectrum (S ⊗[k] k'))` to `(nilradical (S ⊗[k] k')).IsPrime`
> via `irreducibleSpace_primeSpectrum_iff_nilradical_isPrime`, then build `IsPrime` from
> its two pieces: `ne_top` (from `nontrivial_tensorProduct_of_forall_fg`) and `mem_or_mem`
> (from `nilradical_tensorProduct_mem_or_mem_of_forall_fg`).

```lean
theorem isGeometricallyIrreducible_of_forall_fg
    (k : Type u) [Field k] (S : Type u) [CommRing S] [Algebra k S]
    (hS : ∀ (S' : Subalgebra k S), S'.FG →
      Algebra.IsGeometricallyIrreducible k S') :
    Algebra.IsGeometricallyIrreducible k S
```

**`isGeometricallyIrreducible_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Subalgebra.lean#L708). The attribute's comment: “(3)”.

> **Statement 3 (Directed colimits).** A directed colimit of geometrically
> irreducible `k`-algebras is geometrically irreducible over `k`.
>
> The directed system is given by a directed preorder `ι`, `k`-algebras `G i`, and
> transition ring homomorphisms `f i j : G i →+* G j` (for `i ≤ j`) that commute with
> the structure maps from `k` (`hf`) and form a `DirectedSystem`.  The colimit is
> `Ring.DirectLimit G f`, equipped with the `k`-algebra structure `dlAlg k G f`.
>
> Proof outline: for each field extension `k'/k`, reduce to
> `(nilradical (DirectLimit ⊗ k')).IsPrime` via
> `irreducibleSpace_primeSpectrum_iff_nilradical_isPrime`, then assemble `IsPrime` from
> `nontrivial_directLimit_tensorProduct` (nontriviality ⇒ `ne_top`) and
> `nilradical_directLimit_tensorProduct_mem_or_mem` (the prime implication).

```lean
theorem isGeometricallyIrreducible_directLimit
    (k : Type u) [Field k]
    {ι : Type u} [Preorder ι] [IsDirected ι (· ≤ ·)] [Nonempty ι]
    (G : ι → Type u) [∀ i, CommRing (G i)] [∀ i, Algebra k (G i)]
    (f : (i j : ι) → i ≤ j → G i →+* G j)
    (hf : ∀ (i j : ι) (h : i ≤ j) (x : k),
      f i j h (algebraMap k (G i) x) = algebraMap k (G j) x)
    [DirectedSystem G (fun i j h => (f i j h : G i → G j))]
    (hG : ∀ i, Algebra.IsGeometricallyIrreducible k (G i)) :
    letI := dlAlg k G (fun i j h => (f i j h : G i → G j))
    Algebra.IsGeometricallyIrreducible k
      (Ring.DirectLimit G (fun i j h => (f i j h : G i → G j)))
```

## Tag 037O, a lemma

[Tag 037O](https://stacks.math.columbia.edu/tag/037O) in the Stacks Project.

**`Algebra.IsGeometricallyIrreducible.bijOn_irreducibleComponents_primeSpectrum_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/IrreducibleComponents.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/IrreducibleComponents.lean#L190).

> **Stacks 037O.** Let `k` be a field, let `S` be a geometrically irreducible `k`-algebra and
> let `R` be any `k`-algebra. Then the map `Spec (R ⊗[k] S) → Spec R` induced by `r ↦ r ⊗ₜ 1`
> induces a bijection on irreducible components: taking images along it is a bijection from the
> irreducible components of `Spec (R ⊗[k] S)` onto the irreducible components of `Spec R`.

```lean
public theorem
    Algebra.IsGeometricallyIrreducible.bijOn_irreducibleComponents_primeSpectrum_tensorProduct
    (k R S : Type u) [Field k] [CommRing R] [Algebra k R] [CommRing S] [Algebra k S]
    [Algebra.IsGeometricallyIrreducible k S] :
    Set.BijOn (fun Z ↦ PrimeSpectrum.comap (algebraMap R (R ⊗[k] S)) '' Z)
      (irreducibleComponents (PrimeSpectrum (R ⊗[k] S)))
      (irreducibleComponents (PrimeSpectrum R))
```

## Tag 037P, a lemma

[Tag 037P](https://stacks.math.columbia.edu/tag/037P) in the Stacks Project.

**`Algebra.IsGeometricallyIrreducible.of_algebraicClosure_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean#L190).

> Let `K/k` be a field extension. If `k` is algebraically closed in `K`, that is, if the relative
> algebraic closure `algebraicClosure k K` is trivial, then `K` is geometrically irreducible over
> `k`.

```lean
public theorem Algebra.IsGeometricallyIrreducible.of_algebraicClosure_eq_bot (k K : Type u)
    [Field k] [Field K] [Algebra k K] (h : algebraicClosure k K = ⊥) :
    Algebra.IsGeometricallyIrreducible k K
```

## Tag 0G30, a lemma

[Tag 0G30](https://stacks.math.columbia.edu/tag/0G30) in the Stacks Project.

**`Algebra.IsGeometricallyIrreducible.trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean#L96).

> Let `K/k` be a geometrically irreducible field extension and let `S` be a geometrically
> irreducible `K`-algebra. Then `S` is geometrically irreducible over `k`.

```lean
public theorem Algebra.IsGeometricallyIrreducible.trans (k K S : Type u) [Field k] [Field K]
    [CommRing S] [Algebra k K] [Algebra K S] [Algebra k S] [IsScalarTower k K S]
    [Algebra.IsGeometricallyIrreducible k K] [Algebra.IsGeometricallyIrreducible K S] :
    Algebra.IsGeometricallyIrreducible k S
```

## Tag 0G31, a lemma

[Tag 0G31](https://stacks.math.columbia.edu/tag/0G31) in the Stacks Project.

**`AlgebraicGeometry.GeometricallyIrreducible.iff_ratFunc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/AdjoinTranscendental.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/AdjoinTranscendental.lean#L179).

> An extension of fields `K/k` is geometrically irreducible if and only if the induced extension
> `K(X)/k(X)` of purely transcendental extensions in one variable is geometrically irreducible.

```lean
public theorem AlgebraicGeometry.GeometricallyIrreducible.iff_ratFunc (k K : Type u) [Field k]
    [Field K] [Algebra k K] :
    GeometricallyIrreducible (Spec.map (ofHom (algebraMap k K))) ↔
      GeometricallyIrreducible (Spec.map (ofHom (algebraMap k⟮X⟯ K⟮X⟯)))
```

## Tag 0G32, a lemma

[Tag 0G32](https://stacks.math.columbia.edu/tag/0G32) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducible_specMap_adjoin_of_transcendental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/AdjoinTranscendental.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/AdjoinTranscendental.lean#L370).

> Let `K/L/M` be a tower of fields with `L` geometrically irreducible over `M`, and let
> `x : K` be transcendental over `L`. Then `L(x)` is geometrically irreducible over `M(x)`,
> where `M(x) = M⟮x⟯` and `L(x)` is the `M⟮x⟯`-subfield of `K` generated by the image
> of `L`.

```lean
public theorem AlgebraicGeometry.geometricallyIrreducible_specMap_adjoin_of_transcendental
    {M L K : Type u} [Field M] [Field L] [Field K] [Algebra M L] [Algebra M K] [Algebra L K]
    [IsScalarTower M L K]
    [GeometricallyIrreducible (Spec.map (CommRingCat.ofHom (algebraMap M L)))]
    {x : K} (hx : Transcendental L x) :
    GeometricallyIrreducible (Spec.map (CommRingCat.ofHom
      (algebraMap ↥M⟮x⟯ ↥(adjoin ↥M⟮x⟯ (Set.range (algebraMap L K))))))
```

## Tag 0G33, a lemma

[Tag 0G33](https://stacks.math.columbia.edu/tag/0G33) in the Stacks Project.

**`separableClosure.eq_bot_iff_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/Tower.lean#L328).

> Let `K/k` be an extension of fields. The separable closure of `k` in `K` is trivial — every
> element of `K` separably algebraic over `k` lies in `k` — if and only if `K` is geometrically
> irreducible over `k`.

```lean
public theorem separableClosure.eq_bot_iff_geometricallyIrreducible (k K : Type u) [Field k]
    [Field K] [Algebra k K] :
    separableClosure k K = ⊥ ↔ GeometricallyIrreducible (Spec.map (ofHom (algebraMap k K)))
```

## Tag 037Q, a lemma

[Tag 037Q](https://stacks.math.columbia.edu/tag/037Q) in the Stacks Project.

**`part2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/SeparableClosure/SeparableTensor.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/SeparableClosure/SeparableTensor.lean#L287). The attribute's comment: “(2)”.

> Statement 2 (Finiteness of `[k' : k]`). If `K/k` is a finitely generated field extension
> (Definition 4 — finite generation as a field, encoded by `(⊤ : IntermediateField k K).FG`),
> then `k'` is finite over `k`, i.e. `Module.Finite k k'` (equivalently `[k' : k] < ∞`).

```lean
theorem part2 (k K : Type*) [Field k] [Field K] [Algebra k K]
    (hfg : (⊤ : IntermediateField k K).FG) :
    Module.Finite k (separableClosure k K)
```

**`part1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/SeparableClosure/SeparablyClosedBase.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/SeparableClosure/SeparablyClosedBase.lean#L806). The attribute's comment: “(1)”. References: EGA IV (4.3.2), “special case”; EGA IV (4.3.3), “special case”; EGA IV (4.4.4), “special case”; EGA IV (4.5.21), “special case”.

> Statement 1 (Geometric irreducibility over `k'`). `K` is geometrically irreducible over `k' =
> separableClosure k K`: for every field extension `L/k'` the spectrum `Spec(K ⊗\_\{k'} L)` is
> irreducible.

```lean
theorem part1 (k K : Type*) [Field k] [Field K] [Algebra k K] :
    ∀ (L : Type) [Field L] [Algebra (separableClosure k K) L],
      IrreducibleSpace (PrimeSpectrum (K ⊗[separableClosure k K] L))
```

## Tag 04KP, a lemma

[Tag 04KP](https://stacks.math.columbia.edu/tag/04KP) in the Stacks Project.

**`gal_acts_transitively_on_primes_of_isGalois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIrreducible/GaloisAction.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIrreducible/GaloisAction.lean#L317). References: SGA 1 V (1.1), “(ii), special case”.

> Statement 1 (Stacks Tag 04KP). The Galois group `Gal(kbar/k)` of a Galois extension
> `kbar/k` acts transitively on the primes of `kbar ⊗[k] K`: for every pair of prime ideals
> `P, Q` there exists `σ ∈ Gal(kbar/k)` whose induced map on the prime spectrum
> (via `comap` of `σ ⊗ id_K`) carries `Q` to `P`. A separable algebraic closure of `k`, the case
> the source states, is Galois over `k`.

```lean
theorem gal_acts_transitively_on_primes_of_isGalois
    {k K kbar : Type*}
    [Field k] [Field K] [Field kbar]
    [Algebra k K] [Algebra k kbar] [IsGalois k kbar] :
    ∀ (P Q : PrimeSpectrum (kbar ⊗[k] K)),
      ∃ σ : kbar ≃ₐ[k] kbar,
        PrimeSpectrum.comap
          (Algebra.TensorProduct.congr σ (AlgEquiv.refl (R := k) (A₁ :=
              K))).toAlgHom.toRingHom Q = P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.47, Tag 00I2](https://stacks.math.columbia.edu/tag/00I2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
