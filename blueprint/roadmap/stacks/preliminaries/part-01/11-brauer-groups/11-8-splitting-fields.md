---
declaration: section
origin: cited
lean: Algebra.IsSplit, Algebra.IsSplit.exists_embedding, Algebra.isSplit_iff_exists_similar, DivisionRing.isSplit_of_maximal_comm, Algebra.IsSplit.degree_dvd_finrank, DivisionRing.exists_separable_maxSubfield, Algebra.IsCentralSimple.exists_finite_sep_split, Algebra.IsSplit.matrix_size_eq_degree
statement: formalized
proof: formalized
---

# 11.8 Splitting fields

Section 11.8 of the Stacks Project, [Tag 074X](https://stacks.math.columbia.edu/tag/074X). 6 tags here are carried by 9 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 074Y, a definition

[Tag 074Y](https://stacks.math.columbia.edu/tag/074Y) in the Stacks Project.

**`Algebra.IsSplit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Basic.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/Basic.lean#L34).

> A field extension `L` of `K` *splits* a `K`-algebra `A` if `L ⊗[K] A` is isomorphic
> to a (nontrivial) matrix algebra over `L`.

```lean
def IsSplit (L : Type w) [CommRing L] [Algebra K L] : Prop
```

## Tag 074Z, a theorem

[Tag 074Z](https://stacks.math.columbia.edu/tag/074Z) in the Stacks Project.

**`Algebra.IsSplit.exists_embedding`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Embedding.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/Embedding.lean#L156). The attribute's comment: “(1) ⇒ (2)”.

> **Every finite splitting field embeds into a representative of the Brauer class**: if a
> finite extension `L/K` splits the central simple algebra `A`, then the class of `A` has a
> representative `B` of dimension `[L : K]²` receiving a `K`-algebra embedding of `L`. This is
> the converse of `Algebra.IsCentralSimple.split_of_finrank`.

```lean
theorem exists_embedding {A : Type u} [Ring A] [Algebra K A] [FiniteDimensional K A]
    [IsSimpleRing A] [Algebra.IsCentral K A] [FiniteDimensional K L]
    (hs : Algebra.IsSplit K A L) :
    ∃ (B : Type u) (_ : Ring B) (_ : Algebra K B) (_ : FiniteDimensional K B)
      (_ : IsSimpleRing B) (_ : Algebra.IsCentral K B) (_ : L →ₐ[K] B),
      BrauerGroup.mk K B = BrauerGroup.mk K A ∧
      Module.finrank K B = Module.finrank K L ^ 2
```

**`Algebra.isSplit_iff_exists_similar`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Embedding.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/Embedding.lean#L189).

> **Stacks 074Z**, in full. For a *finite* extension `L/K` and a finite central simple
> `K`-algebra `A`, the following are equivalent:
>
> 1. `L` splits `A`;
> 2. some finite central simple algebra `B` similar to `A` contains `L` and has
>    `[B : K] = [L : K]²`.
>
> Forwards is `Algebra.IsSplit.exists_embedding`. Backwards combines
> `Algebra.IsCentralSimple.split_of_finrank` — which gives that `L` splits the *representative*
> `B` it is embedded in — with `Algebra.isSplit_congr`, which transports splitting along the
> similarity `B ∼ A`. Note the `pow_two` shuffle: the tag writes the dimension as a square,
> `split_of_finrank` as a product.

```lean
theorem _root_.Algebra.isSplit_iff_exists_similar {A : Type u} [Ring A] [Algebra K A]
    [FiniteDimensional K A] [IsSimpleRing A] [Algebra.IsCentral K A] [FiniteDimensional K L] :
    Algebra.IsSplit K A L ↔
      ∃ (B : Type u) (_ : Ring B) (_ : Algebra K B) (_ : FiniteDimensional K B)
        (_ : IsSimpleRing B) (_ : Algebra.IsCentral K B) (_ : L →ₐ[K] B),
        BrauerGroup.mk K B = BrauerGroup.mk K A ∧
        Module.finrank K B = Module.finrank K L ^ 2
```

## Tag 0750, a lemma

[Tag 0750](https://stacks.math.columbia.edu/tag/0750) in the Stacks Project.

**`DivisionRing.isSplit_of_maximal_comm`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/DivisionRing.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/DivisionRing.lean#L49).

> **Stacks 0750**: a maximal subfield of a finite central division algebra `D` over `k` is a
> splitting field for `D`.
>
> "Maximal subfield" is rendered as a subalgebra maximal among the *commutative* subalgebras.
> That is the same notion here: every subalgebra of a finite-dimensional division algebra is a
> division ring, and every commutative one is a field (`Subalgebra.fieldOfIsMulCommutative`), so
> the commutative subalgebras of `D` are exactly its subfields.
>
> Maximality is stated with `Maximal` rather than through the numerical criterion
> `Subalgebra.isMaximal_comm_iff_finrank`; the latter is 074V/074W content, and using it here
> would make the statement circular with its own proof.

```lean
theorem DivisionRing.isSplit_of_maximal_comm (L : Subalgebra k D) [IsMulCommutative L]
    (hL : Maximal (fun S : Subalgebra k D ↦ IsMulCommutative S) L) :
    Algebra.IsSplit k D L
```

## Tag 0751, a lemma

[Tag 0751](https://stacks.math.columbia.edu/tag/0751) in the Stacks Project.

**`Algebra.IsSplit.degree_dvd_finrank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Finrank.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/Finrank.lean#L194).

> **Stacks 0751**: for a finite central division algebra `D` over `k` with `d² = [D : k]`,
> the degree `d` *divides* `[L : k]` for every finite splitting field `L` of `D`.
>
> Note this is genuinely stronger than `d ≤ [L : k]`. The divisibility is what the dimension
> count actually produces — the cofactor is `finrank D (Fin m → L)` for the column module of
> the splitting — so the `≤` form is the corollary, not the other way round.
>
> The division hypothesis is essential, as for `DivisionRing.split_iff_finrank`: `M₂(k)` is
> split by `L = k` with `degree k M₂(k) = 2` and `finrank k k = 1`, and `2 ∤ 1`.

```lean
public theorem Algebra.IsSplit.degree_dvd_finrank {D : Type*} [DivisionRing D] [Algebra k D]
    [Module.Finite k D] [Algebra.IsCentral k D] [Module.Finite k L]
    (h : Algebra.IsSplit k D L) : degree k D ∣ Module.finrank k L
```

## Tag 0752, a proposition

[Tag 0752](https://stacks.math.columbia.edu/tag/0752) in the Stacks Project.

**`DivisionRing.exists_separable_maxSubfield`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Algebra/Subalgebra/DivisionRing.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Algebra/Subalgebra/DivisionRing.lean#L221). The attribute's comment: “the separable maximal subfield”.

> **Koethe's theorem**: a finite-dimensional central division algebra `D` over a field `k`
> contains a *separable maximal subfield*, stated here as: there is a commutative subalgebra
> `L` that is self-centralizing — equivalently maximal commutative, by
> `Subalgebra.maximal_comm_iff_self_centralizer` — and separable over `k`. Commutativity of
> `L` follows from self-centralizing-ness via `Subalgebra.le_centralizer_iff_isMulCommutative`.
>
> Proof strategy:
>
> 1. By Zorn's lemma, pick `L` maximal among commutative separable subalgebras of `D`
>    (directed suprema preserve both properties).
> 2. Suppose `L` is not self-centralizing and let `C ≠ L` be its centralizer. Then `C` is a
>    division ring (`Subalgebra.divisionRingOfFinite`), finite-dimensional over the field `L`
>    (`Subalgebra.fieldOfIsMulCommutative`), and *central* over `L`: by the double centralizer
>    theorem, `Z(C) = C ∩ C_D(C) = C ∩ L = L` (the scoped instance
>    `Subalgebra.isCentral_centralizer`).
> 3. By the Jacobson–Noether theorem (`exists_separable_and_not_isCentral'`) applied to the
>    noncommutative division algebra `C` over `L`, there is `x ∈ C \ L` separable over `L`.
> 4. `L' := k[L, x]` is commutative (since `x` centralizes `L`) and separable over `k` — it is
>    generated over `L` by the single separable element `x`, and separability is transitive in
>    the tower `k ⊆ L ⊆ L'` (`JacobsonNoether.adjoin_insert_mem_S`).
> 5. So `L'` is a member of the Zorn family strictly containing `L`, contradicting maximality.

```lean
theorem DivisionRing.exists_separable_maxSubfield [FiniteDimensional k D]
    [Algebra.IsCentral k D] :
    ∃ L : Subalgebra k D, Subalgebra.centralizer k (L : Set D) = L ∧
      Algebra.IsSeparable k L
```

**`Algebra.IsCentralSimple.exists_finite_sep_split`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/DivisionRing.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/DivisionRing.lean#L74). The attribute's comment: “in particular: every Brauer class has a finite separable splitting field”.

> **Stacks 0752**, the "in particular" clause: every Brauer class has a finite separable
> splitting field. Concretely, every finite central simple `k`-algebra is split by a finite
> separable subextension of any chosen algebraic closure.

```lean
theorem Algebra.IsCentralSimple.exists_finite_sep_split :
    ∃ K : IntermediateField k k_bar, Module.Finite k K ∧
      Algebra.IsSeparable k K ∧ Algebra.IsSplit k A K
```

## Tag 0753, a lemma

[Tag 0753](https://stacks.math.columbia.edu/tag/0753) in the Stacks Project.

**`Algebra.IsSplit.matrix_size_eq_degree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/CentralSimple.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/CentralSimple.lean#L87). The attribute's comment: “the integer d is called the degree of A”.

> **Stacks 0753**, closing sentence: the matrix size in *any* splitting of `A` is the degree
> of `A`. This is what licenses calling it "the" integer `d` — clauses (3), (4) and (5) of
> `Algebra.isCentralSimple_tfae` each quantify their own witness, and this identifies them all
> with `Algebra.IsCentralSimple.degree k A`.
>
> No central-simple hypotheses are needed: a splitting already forces `finrank k A = n * n`,
> and `degree` is by definition `Nat.sqrt` of that. In the tag's setting `A` is of course
> central simple, but the identification of the witness does not depend on it.

```lean
theorem Algebra.IsSplit.matrix_size_eq_degree (L : Type w) [Field L] [Algebra k L]
    {n : ℕ} (e : L ⊗[k] A ≃ₐ[L] Matrix (Fin n) (Fin n) L) :
    n = Algebra.IsCentralSimple.degree k A
```

**`Algebra.isCentralSimple_tfae`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/CentralSimple.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/CentralSimple.lean#L112). References: SGA 4½ Arcata (3.1.1).

> **Stacks 0753**: for a `k`-algebra `A` the following are equivalent.
>
> 1. `A` is a finite central simple `k`-algebra.
> 2. `A` is a finite-dimensional `k`-vector space, `k` is the centre of `A`, and `A` has no
>    nontrivial two-sided ideal.
> 3. `A ⊗ k̄` is a matrix algebra over `k̄`.
> 4. `A ⊗ kˢᵉᵖ` is a matrix algebra over `kˢᵉᵖ`.
> 5. `A ⊗ k'` is a matrix algebra over `k'` for some finite Galois `k'/k`.
> 6. `A ≅ Mat(n, K)` for some `n ≥ 1` and some finite central division algebra `K` over `k`.
>
> The proof is a star around (1): each of (2)–(6) is proved equivalent to (1) directly. The
> forward directions are the splitting constructions of §11.08; the return directions
> (3) ⇒ (1), (4) ⇒ (1), (5) ⇒ (1) all factor through
> `Algebra.IsSplit.finite_central_simple`.

```lean
theorem Algebra.isCentralSimple_tfae (k_bar : Type w) [Field k_bar] [Algebra k k_bar]
    [IsAlgClosed k_bar] [Algebra.IsAlgebraic k k_bar] :
    [ Module.Finite k A ∧ Algebra.IsCentral k A ∧ IsSimpleRing A,
      Module.Finite k A ∧ Subalgebra.center k A = ⊥ ∧ IsSimpleOrder (TwoSidedIdeal A),
      Algebra.IsSplit k A k_bar,
      Algebra.IsSplit k A (separableClosure k k_bar),
      ∃ K : IntermediateField k k_bar, Module.Finite k K ∧ IsGalois k K ∧ Algebra.IsSplit k A K,
      ∃ (n : ℕ) (_ : NeZero n) (D : Type v) (_ : DivisionRing D) (_ : Algebra k D)
        (_ : Module.Finite k D) (_ : Algebra.IsCentral k D),
        Nonempty (A ≃ₐ[k] Matrix (Fin n) (Fin n) D) ].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.8, Tag 074X](https://stacks.math.columbia.edu/tag/074X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
